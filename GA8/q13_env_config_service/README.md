# GA8 — Q13: GCP Cloud Run — Environment Variable Configuration

This README summarizes the question folder. The detailed solution remains in `q13_env_config_service.md`.

## Method

Prepared a cloud-deployable API or script, with runtime dependencies and endpoint verification.

The implementation keeps the question-specific assets beside the writeup so the answer can be inspected and reproduced without searching elsewhere.

## Files

| File | Purpose |
| --- | --- |
| `Dockerfile` | Docker deployment |
| `app.py` | Python API/service code |
| `q13_env_config_service.md` | Detailed question writeup |
| `requirements.txt` | Python dependencies |

## Run or Reproduce

```bash
pip install -r requirements.txt
uvicorn app:app --host 0.0.0.0 --port 7860
docker build -t tds-question .
```

## Verification

Verification is documented in the detailed writeup when applicable. In general, the check is based on the final artifact expected by the grader: an API response, computed answer, generated file, deployed endpoint, or command output.
