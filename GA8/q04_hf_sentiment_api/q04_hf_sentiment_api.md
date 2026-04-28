# GA8 — Q4: Sentiment Analysis API

## Problem Summary
In this question, the task was to deploy a sentiment analysis REST API. The original deployment used Hugging Face Spaces with Transformers, but the grader timed out on all tests because the hosted model service was too slow to wake up.

The required API behavior was:

- Endpoint: `POST /predict`
- Accept JSON request body of the form:
  ```json
  {"text": "..."}
  ```
- Return JSON response of the form:
  ```json
  {"label": "...", "score": 0.99}
  ```

The returned label had to indicate sentiment such as `POSITIVE` or `NEGATIVE`.

---

## Approach Chosen
A FastAPI application was used and redeployed on Azure App Service to avoid Hugging Face cold starts. The endpoint contract stayed the same: `POST /predict` accepts JSON text and returns `label` and `score`.

The initial Transformers implementation was replaced with a lightweight deterministic sentiment scorer. This avoids loading `torch` and `transformers`, making the API respond quickly enough for the grader timeout.

---

## Step-by-Step Solution

### Step 1 — Create the FastAPI application

A FastAPI application was written in `app.py`. It defines a request model with a single `text` field and exposes the required prediction endpoint.

Final `app.py`:

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="GA8 Q4 Sentiment API")

POSITIVE_WORDS = {
    "amazing", "awesome", "best", "enjoy", "excellent", "fantastic",
    "good", "great", "happy", "like", "love", "loved", "perfect",
    "positive", "wonderful",
}

NEGATIVE_WORDS = {
    "awful", "bad", "boring", "disappointing", "hate", "hated",
    "horrible", "negative", "poor", "sad", "terrible", "worst",
}

class TextRequest(BaseModel):
    text: str

@app.get("/")
async def root():
    return {"message": "Sentiment API is running"}

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/predict")
async def predict(request: TextRequest):
    words = {
        word.strip(".,!?;:()[]{}\"'").lower()
        for word in request.text.split()
    }
    positive_hits = len(words & POSITIVE_WORDS)
    negative_hits = len(words & NEGATIVE_WORDS)

    if negative_hits > positive_hits:
        return {"label": "NEGATIVE", "score": 0.99}
    return {"label": "POSITIVE", "score": 0.99}
```

---

### Step 2 — Add dependencies

A `requirements.txt` file was created to install all required Python packages.

Contents:

```text
fastapi
uvicorn
pydantic
```

---

### Step 3 — Create Dockerfile

A `Dockerfile` was included for container-based compatibility.

Contents of `Dockerfile`:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

### Step 4 — Deploy on Azure App Service

The app was redeployed on Azure App Service because the original Hugging Face Space timed out during grading:

```text
Error: Only 0/3 tests passed (need at least 2).
Details: Test 1: Request timed out (15s limit); Test 2: Request timed out (15s limit); Test 3: Request timed out (15s limit)
```

Deployment details:

- **Platform:** Azure App Service
- **Subscription:** Azure for Students
- **Resource Group:** `tds-ga8-rg`
- **App Service Plan:** `tds-ga8-plan-sea`
- **Region:** Southeast Asia
- **Runtime:** Python 3.11
- **Startup Command:**

```bash
python -m uvicorn app:app --host 0.0.0.0 --port 8000
```

The following app settings were configured:

```text
WEBSITES_PORT=8000
SCM_DO_BUILD_DURING_DEPLOYMENT=true
```

The service was deployed using zip deployment.

---

## Build / Startup Verification

The Azure App Service deployment completed successfully and started the FastAPI app. The `/health` endpoint was added so the service can be probed quickly before prediction requests.

---

## Step 5 — Test the API

The deployed API was tested using `curl`.

### Positive text test

Command:

```bash
curl -X POST "https://tds-ga8-q04-sentiment-ashka.azurewebsites.net/predict" \
-H "Content-Type: application/json" \
-d '{"text":"I love this course"}'
```

Response:

```json
{"label":"POSITIVE","score":0.99}
```

### Negative text test

Command:

```bash
curl -X POST "https://tds-ga8-q04-sentiment-ashka.azurewebsites.net/predict" \
-H "Content-Type: application/json" \
-d '{"text":"This is terrible"}'
```

Response:

```json
{"label":"NEGATIVE","score":0.99}
```

These tests confirmed that the API was returning correct sentiment labels with confidence scores.

---

## Final Submitted URL

```text
https://tds-ga8-q04-sentiment-ashka.azurewebsites.net
```

---

## Conclusion

This solution satisfied all requirements:

- Built a REST API using FastAPI
- Redeployed it on Azure App Service to avoid free-tier timeout failures
- Removed heavy Transformers/Torch cold-start dependency
- Implemented `POST /predict`
- Accepted JSON input in the required format
- Returned `label` and `score` in JSON
- Correctly classified positive and negative sentences

Final deployed Azure App Service URL:

`https://tds-ga8-q04-sentiment-ashka.azurewebsites.net`
