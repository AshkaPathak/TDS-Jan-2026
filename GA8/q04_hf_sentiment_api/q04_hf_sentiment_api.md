# GA8 — Q4: Hugging Face Spaces Sentiment Analysis API

## Problem Summary
In this question, the task was to deploy a machine learning model as a REST API on Hugging Face Spaces. The API had to perform sentiment analysis using the Hugging Face Transformers library.

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
A FastAPI application was used and deployed on Hugging Face Spaces using the **Docker SDK**. This was a reliable choice because the question explicitly allowed REST API deployment, and FastAPI maps directly to the required `POST /predict` endpoint.

The Hugging Face `pipeline("sentiment-analysis")` was used to load a pretrained sentiment analysis model from Transformers.

---

## Step-by-Step Solution

### Step 1 — Create the FastAPI application

A FastAPI application was written in `app.py`. It defines a request model with a single `text` field, loads the sentiment analysis pipeline, and exposes the required prediction endpoint.

Final `app.py`:

```python
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

classifier = pipeline(
    "sentiment-analysis",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
)

class TextRequest(BaseModel):
    text: str

@app.get("/")
async def root():
    return {"message": "Sentiment API is running"}

@app.post("/predict")
async def predict(request: TextRequest):
    result = classifier(request.text)[0]
    return {"label": result["label"], "score": result["score"]}
```

---

### Step 2 — Add dependencies

A `requirements.txt` file was created to install all required Python packages.

Contents:

```text
fastapi
uvicorn
transformers
torch
```

---

### Step 3 — Create Dockerfile for Hugging Face Spaces

Since the Space was created with the **Docker** SDK, a `Dockerfile` was required.

Contents of `Dockerfile`:

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 7860

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]
```

This file ensures that Hugging Face installs the dependencies, copies the application files, and starts the FastAPI app on port `7860`, which is the expected port for Spaces.

---

### Step 4 — Deploy on Hugging Face Spaces

A new Hugging Face Space was created with the following configuration:

- **Space name:** `sentiment-api`
- **Owner:** `AshkaPathak`
- **SDK:** `Docker`
- **Visibility:** Public

The following files were uploaded to the Space:

- `app.py`
- `requirements.txt`
- `Dockerfile`

After committing the files, Hugging Face built and launched the app.

---

## Build / Startup Verification

The Space logs showed successful startup:

- `Application startup complete.`
- `Uvicorn running on http://0.0.0.0:7860`

There was also a `GET / ... 404 Not Found` log initially, which was not an error in the API itself. It happened because the main required endpoint was `POST /predict`, not `/`. A root route was then added so the Space would respond cleanly at `/` as well.

---

## Step 5 — Test the API

The deployed API was tested using `curl`.

### Positive text test

Command:

```bash
curl -X POST "https://ashkapathak-sentiment-api.hf.space/predict" \
-H "Content-Type: application/json" \
-d '{"text":"I love this course"}'
```

Response:

```json
{"label":"POSITIVE","score":0.999883770942688}
```

### Negative text test

Command:

```bash
curl -X POST "https://ashkapathak-sentiment-api.hf.space/predict" \
-H "Content-Type: application/json" \
-d '{"text":"This is terrible"}'
```

Response:

```json
{"label":"NEGATIVE","score":0.9996459484100342}
```

These tests confirmed that the API was returning correct sentiment labels with confidence scores.

---

## Final Submitted URL

```text
https://ashkapathak-sentiment-api.hf.space
```

---

## Conclusion

This solution satisfied all requirements:

- Built a REST API using FastAPI
- Deployed it on Hugging Face Spaces
- Used a pretrained sentiment analysis model from Transformers
- Implemented `POST /predict`
- Accepted JSON input in the required format
- Returned `label` and `score` in JSON
- Correctly classified positive and negative sentences

Final deployed Hugging Face Space URL:

`https://ashkapathak-sentiment-api.hf.space`
