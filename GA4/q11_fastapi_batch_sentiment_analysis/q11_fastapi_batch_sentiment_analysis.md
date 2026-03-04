# GA4 — Q11: FastAPI Batch Sentiment Analysis Endpoint

## Problem Summary

Build a FastAPI service that performs batch sentiment analysis.

The API must:

- Accept a POST request with multiple sentences
- Return sentiment classification for each sentence
- Valid sentiment labels: **happy**, **sad**, **neutral**
- Preserve the order of input sentences
- Pass at least **7/10 evaluation test cases**

The evaluation system may send requests to either `/` or `/sentiment`, so both endpoints are supported.

---

# API Design

## Base URL

```
https://tds-jan-2026-3.onrender.com
```

---

## Health Check Endpoint

```
GET /
HEAD /
```

Response:

```json
{
  "status": "ok"
}
```

This ensures the portal validator can confirm the service is running.

---

# Sentiment Endpoint

### Request

```
POST /sentiment
Content-Type: application/json
```

Example request body:

```json
{
  "sentences": [
    "I love this product!",
    "This is terrible.",
    "The meeting is at 3 PM."
  ]
}
```

---

### Response

```json
{
  "results": [
    {"sentence": "I love this product!", "sentiment": "happy"},
    {"sentence": "This is terrible.", "sentiment": "sad"},
    {"sentence": "The meeting is at 3 PM.", "sentiment": "neutral"}
  ]
}
```

---

# Implementation

File: `main.py`

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = FastAPI()

# Allow portal/browser requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

analyzer = SentimentIntensityAnalyzer()

# Health check endpoint
@app.api_route("/", methods=["GET", "HEAD"])
def root():
    return {"status": "ok"}

def classify(text: str) -> str:
    score = analyzer.polarity_scores(text)["compound"]

    if score >= 0.2:
        return "happy"
    elif score <= -0.2:
        return "sad"
    else:
        return "neutral"

# Support both POST / and POST /sentiment
@app.post("/")
@app.post("/sentiment")
def sentiment(payload: dict):
    sentences = payload.get("sentences", [])

    results = []
    for s in sentences:
        results.append({
            "sentence": s,
            "sentiment": classify(s)
        })

    return {"results": results}
```

---

# Dependencies

File: `requirements.txt`

```
fastapi
uvicorn
vaderSentiment
```

---

# Local Setup

### 1. Create virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run server

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

---

# Testing Locally

### Health Check

```bash
curl http://127.0.0.1:8000/
```

Expected:

```json
{"status":"ok"}
```

---

### Sentiment Test

```bash
curl -X POST http://127.0.0.1:8000/sentiment \
-H "Content-Type: application/json" \
-d '{"sentences":["I love this product!","This is terrible.","The meeting is at 3 PM."]}'
```

Expected:

```json
{
  "results": [
    {"sentence":"I love this product!","sentiment":"happy"},
    {"sentence":"This is terrible.","sentiment":"sad"},
    {"sentence":"The meeting is at 3 PM.","sentiment":"neutral"}
  ]
}
```

---

# Deployment

The service was deployed using **Render**.

Start command:

```
uvicorn main:app --host 0.0.0.0 --port $PORT
```

Public URL:

```
https://tds-jan-2026-3.onrender.com
```

---

# Result

✔ API accepts batch input  
✔ Returns ordered sentiment results  
✔ Supports both `/` and `/sentiment` endpoints  
✔ Passes portal validation (≥7/10 test cases)

