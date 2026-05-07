# GA3 — Q3: Code Interpreter with AI Error Analysis

This README summarizes the question folder. The detailed solution remains in `q03_code_interpreter_with_error_analysis.md`.

## Method

Implemented the solution in Python with a small service or script and documented how to run it.

The implementation keeps the question-specific assets beside the writeup so the answer can be inspected and reproduced without searching elsewhere.

## Files

| File | Purpose |
| --- | --- |
| `main.py` | Python API/service code |
| `q03_code_interpreter_with_error_analysis.md` | Detailed question writeup |
| `requirements.txt` | Python dependencies |

## Run or Reproduce

```bash
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 7860
```

## Verification

Verification is documented in the detailed writeup when applicable. In general, the check is based on the final artifact expected by the grader: an API response, computed answer, generated file, deployed endpoint, or command output.
