# q19 similarity api

This README summarizes the question folder. The detailed solution remains in the files in this folder.

## Method

Implemented the solution in Python with a small service or script and documented how to run it.

The implementation keeps the question-specific assets beside the writeup so the answer can be inspected and reproduced without searching elsewhere.

## Files

| File | Purpose |
| --- | --- |
| `__pycache__/app.cpython-313.pyc` | question writeup and supporting files |
| `app.py` | Python API/service code |
| `requirements.txt` | Python dependencies |
| `start.sh` | question writeup and supporting files |

## Run or Reproduce

```bash
pip install -r requirements.txt
uvicorn app:app --host 0.0.0.0 --port 7860
```

## Verification

Verification is documented in the detailed writeup when applicable. In general, the check is based on the final artifact expected by the grader: an API response, computed answer, generated file, deployed endpoint, or command output.
