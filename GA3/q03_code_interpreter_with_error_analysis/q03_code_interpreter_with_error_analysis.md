# GA3 — Q3: Code Interpreter with AI Error Analysis

## Problem Summary

Build a FastAPI endpoint:

- **POST `/code-interpreter`**
- Accepts Python code as a string
- Executes it using `exec()`
- Returns exact stdout / traceback output
- If execution fails:
  - Identify the line number(s) where the error occurred
  - Use Gemini structured output (with fallback parsing)
- Enable CORS (`Access-Control-Allow-Origin: *`)

---

## Final Deployed Endpoint

```
https://ga3-q3-code-interpreter.onrender.com/code-interpreter
```

---

# Implementation

## Folder Structure

```
GA3/
└── q03_code_interpreter_with_error_analysis/
    ├── main.py
    ├── requirements.txt
    └── q03_code_interpreter_with_error_analysis.md
```

---

## main.py

```python
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

# Enable CORS
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


# -----------------------------------
# 1. Execute Python Code
# -----------------------------------
def execute_python_code(code: str) -> Dict[str, Any]:
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


# -----------------------------------
# 2. Structured Error Analysis
# -----------------------------------
class ErrorAnalysis(BaseModel):
    error_lines: List[int]


def _fallback_extract_lines(tb_text: str) -> List[int]:
    import re

    found = []
    for m in re.finditer(r'File "<string>", line (\d+)', tb_text):
        found.append(int(m.group(1)))

    # Deduplicate while preserving order
    seen = set()
    uniq = []
    for x in found:
        if x not in seen:
            seen.add(x)
            uniq.append(x)

    return uniq


def analyze_error_with_ai(code: str, tb_text: str) -> List[int]:
    api_key = os.environ.get("GEMINI_API_KEY")

    # Fallback if no API key
    if not api_key:
        return _fallback_extract_lines(tb_text)

    try:
        client = genai.Client(api_key=api_key)

        prompt = f"""
Analyze this Python code and its traceback.
Return the line number(s) where the error occurred.
Return only JSON: {{ "error_lines": [ ... ] }}

CODE:
{code}

TRACEBACK:
{tb_text}
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

        seen = set()
        uniq = []
        for x in parsed.error_lines:
            if x not in seen:
                seen.add(x)
                uniq.append(x)

        return uniq

    except Exception:
        return _fallback_extract_lines(tb_text)


# -----------------------------------
# 3. Endpoint
# -----------------------------------
@app.post("/code-interpreter", response_model=CodeResponse)
def code_interpreter(req: CodeRequest) -> CodeResponse:
    run = execute_python_code(req.code)

    if run["success"]:
        return CodeResponse(error=[], result=run["output"])

    error_lines = analyze_error_with_ai(req.code, run["output"])
    return CodeResponse(error=error_lines, result=run["output"])
```

---

## requirements.txt

```
fastapi
uvicorn
google-genai
pydantic
```

---

# Local Testing

## Run Server

```bash
python -m uvicorn main:app --reload --port 8000
```

---

## Success Case

```bash
curl -s -X POST http://127.0.0.1:8000/code-interpreter \
  -H "Content-Type: application/json" \
  -d '{"code":"print(2+3)\n"}'
```

Expected:

```json
{"error":[],"result":"5\n"}
```

---

## Error Case

```bash
curl -s -X POST http://127.0.0.1:8000/code-interpreter \
  -H "Content-Type: application/json" \
  -d '{"code":"x=1\ny=0\nx/y\n"}'
```

Expected:
- `error` contains `[3]`
- `result` contains traceback with `File "<string>", line 3`

---

## CORS Verification

```bash
curl -i -X OPTIONS "http://127.0.0.1:8000/code-interpreter" \
  -H "Origin: http://example.com" \
  -H "Access-Control-Request-Method: POST"
```

Expected header:

```
access-control-allow-origin: *
```

---

# Deployment (Render)

## Root Directory

```
GA3/q03_code_interpreter_with_error_analysis
```

## Build Command

```bash
pip install -r requirements.txt
```

## Start Command

```bash
python -m uvicorn main:app --host 0.0.0.0 --port $PORT
```

---

# Final Submission URL

```
https://ga3-q3-code-interpreter.onrender.com/code-interpreter
```

---

# Design Decisions

- Exact stdout and traceback returned (no formatting changes)
- AI used only when execution fails
- Structured JSON schema enforced for Gemini
- Fallback parsing ensures robustness without API key
- CORS enabled for portal validation
