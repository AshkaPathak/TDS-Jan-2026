# GA4 — Q11: FastAPI Batch Sentiment Analysis Endpoint

This README summarizes the question folder. The detailed solution remains in `q11_fastapi_batch_sentiment_analysis.md`.

## Method

Implemented a FastAPI endpoint with explicit request/response behavior, local testing, and deployment-ready dependencies.

The implementation keeps the question-specific assets beside the writeup so the answer can be inspected and reproduced without searching elsewhere.

## Files

| File | Purpose |
| --- | --- |
| `main.py` | Python API/service code |
| `q11_fastapi_batch_sentiment_analysis.md` | Detailed question writeup |
| `requirements.txt` | Python dependencies |

## Run or Reproduce

```bash
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 7860
```

## Verification

Verification is documented in the detailed writeup when applicable. In general, the check is based on the final artifact expected by the grader: an API response, computed answer, generated file, deployed endpoint, or command output.
