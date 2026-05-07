# GA8 — Q7: Pre-commit Hooks + CI Gate with Ruff

This README summarizes the question folder. The detailed solution remains in `q07_ruff_ci.md`.

## Method

Implemented the solution in Python with a small service or script and documented how to run it.

The implementation keeps the question-specific assets beside the writeup so the answer can be inspected and reproduced without searching elsewhere.

## Files

| File | Purpose |
| --- | --- |
| `.github/workflows/ruff-ci.yml` | question writeup and supporting files |
| `.pre-commit-config.yaml` | question writeup and supporting files |
| `analysis.py` | question writeup and supporting files |
| `main.py` | Python API/service code |
| `q07_ruff_ci.md` | Detailed question writeup |

## Run or Reproduce

```bash
uvicorn main:app --host 0.0.0.0 --port 7860
```

## Verification

Verification is documented in the detailed writeup when applicable. In general, the check is based on the final artifact expected by the grader: an API response, computed answer, generated file, deployed endpoint, or command output.
