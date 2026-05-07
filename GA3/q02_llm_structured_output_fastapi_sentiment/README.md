# GA3 – Q2: LLM Structured Output – FastAPI Sentiment Analysis

This README summarizes the question folder. The detailed solution remains in `q02_llm_structured_output_fastapi_sentiment.md`.

## Method

Implemented a FastAPI endpoint with explicit request/response behavior, local testing, and deployment-ready dependencies.

The implementation keeps the question-specific assets beside the writeup so the answer can be inspected and reproduced without searching elsewhere.

## Files

| File | Purpose |
| --- | --- |
| `.gitignore` | question writeup and supporting files |
| `Dockerfile` | Docker deployment |
| `main.py` | Python API/service code |
| `q02_llm_structured_output_fastapi_sentiment.md` | Detailed question writeup |
| `requirements.txt` | Python dependencies |

## Run or Reproduce

```bash
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 7860
docker build -t tds-question .
```

## Verification

Verification is documented in the detailed writeup when applicable. In general, the check is based on the final artifact expected by the grader: an API response, computed answer, generated file, deployed endpoint, or command output.
