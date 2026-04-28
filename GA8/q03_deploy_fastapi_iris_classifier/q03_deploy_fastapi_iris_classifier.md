# GA8 — Q3: Deploy a FastAPI Iris Classifier

## Problem Summary
In this question, the task was to deploy a public FastAPI Iris classifier. The grader accepted only these host types:

- Hugging Face Spaces: `*.hf.space`
- Vercel: `*.vercel.app`
- Render: `*.onrender.com`

The original Render deployment timed out during grading, and Azure was rejected because it was not an allowed host for this question. The final solution was redeployed on Hugging Face Spaces.

The required endpoints were:

- `GET /health` returning `{"status":"ok"}`
- `GET /predict?sl=...&sw=...&pl=...&pw=...` returning:
  - `"prediction"` as an integer
  - `"class_name"` as a string

The unique Iris sample assigned here was:

- Sepal Length (`sl`) = 7.4
- Sepal Width (`sw`) = 3.7
- Petal Length (`pl`) = 4.5
- Petal Width (`pw`) = 1.7

---

## Required Output Format

The `/predict` endpoint had to return:

```json
{"prediction":1,"class_name":"versicolor"}
```

---

## Step-by-Step Solution

### Step 1 — Create the FastAPI Application

To keep the Hugging Face Space fast enough for the grader timeout, the app uses a lightweight Iris decision rule instead of importing heavy ML dependencies at startup.

Final `app.py`:

```python
from fastapi import FastAPI

app = FastAPI(title="GA8 Q3 Iris Classifier")

CLASS_NAMES = ["setosa", "versicolor", "virginica"]


def classify(sl: float, sw: float, pl: float, pw: float) -> int:
    if pl < 2.5:
        return 0
    if pw < 1.8:
        return 1
    return 2


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/predict")
async def predict(sl: float, sw: float, pl: float, pw: float):
    pred = classify(sl, sw, pl, pw)
    return {"prediction": pred, "class_name": CLASS_NAMES[pred]}
```

---

### Step 2 — Add Requirements

```text
fastapi
uvicorn
```

---

### Step 3 — Add Dockerfile for Hugging Face Spaces

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 7860

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]
```

---

## Deployment Issue Faced and Resolved

The first Render URL failed with:

```text
Error: Request to https://tds-jan-2026-4.onrender.com/health timed out after 10 seconds.
```

An Azure replacement was also rejected by the grader because Q3 only allows Hugging Face Spaces, Vercel, or Render. The final fix was to deploy a lightweight Docker Space on Hugging Face.

---

## Verification

Health endpoint:

```text
https://ashkapathak-tds-ga8-q03-iris-ashka.hf.space/health
```

Response:

```json
{"status":"ok"}
```

Prediction endpoint:

```text
https://ashkapathak-tds-ga8-q03-iris-ashka.hf.space/predict?sl=7.4&sw=3.7&pl=4.5&pw=1.7
```

Response:

```json
{"prediction":1,"class_name":"versicolor"}
```

---

## Final Submitted URL

```text
https://ashkapathak-tds-ga8-q03-iris-ashka.hf.space
```

---

## Conclusion

The final Hugging Face Spaces deployment uses an accepted host, avoids cold-start timeout issues, and returns the expected `versicolor` classification for the assigned sample.
