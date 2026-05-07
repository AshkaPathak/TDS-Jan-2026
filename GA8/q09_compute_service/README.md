# GA8 — Q9: GCP Cloud Run — Deploy a Compute Service

This README summarizes the question folder. The detailed solution remains in `q09_compute_service.md`.

## Method

Prepared a cloud-deployable API or script, with runtime dependencies and endpoint verification.

The implementation keeps the question-specific assets beside the writeup so the answer can be inspected and reproduced without searching elsewhere.

## Files

| File | Purpose |
| --- | --- |
| `Dockerfile` | Docker deployment |
| `main.py` | Python API/service code |
| `q09_compute_service.md` | Detailed question writeup |
| `requirements.txt` | Python dependencies |

## Run or Reproduce

```bash
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 7860
docker build -t tds-question .
```

## Verification

Verification is documented in the detailed writeup when applicable. In general, the check is based on the final artifact expected by the grader: an API response, computed answer, generated file, deployed endpoint, or command output.
