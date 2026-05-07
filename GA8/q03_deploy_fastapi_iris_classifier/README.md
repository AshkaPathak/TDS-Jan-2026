# GA8 — Q3: Deploy a FastAPI Iris Classifier

This README summarizes the question folder. The detailed solution remains in `q03_deploy_fastapi_iris_classifier.md`.

## Method

Implemented a FastAPI endpoint with explicit request/response behavior, local testing, and deployment-ready dependencies.

The implementation keeps the question-specific assets beside the writeup so the answer can be inspected and reproduced without searching elsewhere.

## Files

| File | Purpose |
| --- | --- |
| `Dockerfile` | Docker deployment |
| `app.py` | Python API/service code |
| `q03_deploy_fastapi_iris_classifier.md` | Detailed question writeup |
| `requirements.txt` | Python dependencies |

## Run or Reproduce

```bash
pip install -r requirements.txt
uvicorn app:app --host 0.0.0.0 --port 7860
docker build -t tds-question .
```

## Verification

Verification is documented in the detailed writeup when applicable. In general, the check is based on the final artifact expected by the grader: an API response, computed answer, generated file, deployed endpoint, or command output.
