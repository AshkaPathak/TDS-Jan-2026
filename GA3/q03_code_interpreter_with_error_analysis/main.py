import os
import sys
import traceback
from io import StringIO
from typing import List, Dict, Any

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from google import genai
from google.genai import types


app = FastAPI()

# CORS (required for testing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


class CodeRequest(BaseModel):
    code: str


class CodeResponse(BaseModel):
    error: List[int]
    result: str


def execute_python_code(code: str) -> Dict[str, Any]:
    """
    Execute Python code and return exact output.

    Returns:
      {
        "success": bool,
        "output": str  # exact stdout/stderr or traceback
      }
    """
    old_stdout = sys.stdout
    old_stderr = sys.stderr

    stdout_buf = StringIO()
    stderr_buf = StringIO()

    sys.stdout = stdout_buf
    sys.stderr = stderr_buf

    try:
        sandbox_globals = {"__name__": "__main__"}
        exec(code, sandbox_globals)
        out = stdout_buf.getvalue() + stderr_buf.getvalue()
        return {"success": True, "output": out}

    except Exception:
        tb = traceback.format_exc()
        out = stdout_buf.getvalue() + stderr_buf.getvalue() + tb
        return {"success": False, "output": out}

    finally:
        sys.stdout = old_stdout
        sys.stderr = old_stderr


class ErrorAnalysis(BaseModel):
    error_lines: List[int]


def _fallback_extract_lines(tb_text: str) -> List[int]:
    """
    Fallback: parse traceback lines like:
      File "<string>", line 3, in <module>
    """
    import re

    found = []
    for m in re.finditer(r'File "<string>", line (\d+)', tb_text):
        try:
            found.append(int(m.group(1)))
        except ValueError:
            pass

    # Deduplicate while preserving order
    seen = set()
    uniq = []
    for x in found:
        if x not in seen:
            seen.add(x)
            uniq.append(x)
    return uniq


def analyze_error_with_ai(code: str, tb_text: str) -> List[int]:
    """
    Use Gemini structured output to identify error line numbers.
    Only called when execution failed.

    If GEMINI_API_KEY is missing or Gemini call fails, fallback to parsing traceback.
    """
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return _fallback_extract_lines(tb_text)

    try:
        client = genai.Client(api_key=api_key)

        prompt = f"""
Analyze this Python code and its error traceback.
Identify the line number(s) in the CODE where the error occurred.

CODE:
{code}

TRACEBACK:
{tb_text}

Return ONLY the line number(s) as a JSON object with key "error_lines".
"""

        response = client.models.generate_content(
            model="gemini-2.0-flash-exp",
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=types.Schema(
                    type=types.Type.OBJECT,
                    properties={
                        "error_lines": types.Schema(
                            type=types.Type.ARRAY,
                            items=types.Schema(type=types.Type.INTEGER),
                        )
                    },
                    required=["error_lines"],
                ),
            ),
        )

        parsed = ErrorAnalysis.model_validate_json(response.text)

        # Deduplicate while preserving order
        seen = set()
        uniq = []
        for x in parsed.error_lines:
            if x not in seen:
                seen.add(x)
                uniq.append(x)
        return uniq

    except Exception:
        return _fallback_extract_lines(tb_text)


@app.post("/code-interpreter", response_model=CodeResponse)
def code_interpreter(req: CodeRequest) -> CodeResponse:
    run = execute_python_code(req.code)

    if run["success"]:
        return CodeResponse(error=[], result=run["output"])

    error_lines = analyze_error_with_ai(req.code, run["output"])
    return CodeResponse(error=error_lines, result=run["output"])
