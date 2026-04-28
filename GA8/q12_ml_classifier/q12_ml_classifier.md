# GA8 — Q12: GCP Cloud Run — Deploy an ML Classifier

## Problem Summary
In this question, the task was to train a machine learning model and deploy it as a public inference API. The deployed app had to expose three endpoints:

- `GET /health` returning service health and model name
- `GET /info` returning model metadata
- `GET /predict?sl=...&sw=...&pl=...&pw=...` returning an Iris class prediction

The unique Iris sample assigned here was:

| Feature | Value |
|---|---:|
| Sepal Length (`sl`) | 7.7 |
| Sepal Width (`sw`) | 2.3 |
| Petal Length (`pl`) | 2.1 |
| Petal Width (`pw`) | 1 |

Azure deployment URLs were accepted by the grader, so the service was deployed on Azure App Service.

---

## Required Output Format

The `/predict` endpoint had to return JSON in this structure:

```json
{"prediction":0,"class_name":"setosa","confidence":1.0}
```

The required endpoints were:

| Endpoint | Method | Expected Response |
|---|---|---|
| `/health` | `GET` | `{"status":"ok","model":"iris-classifier"}` |
| `/info` | `GET` | Model metadata, including model type, random state, dataset, and classes |
| `/predict?sl=7.7&sw=2.3&pl=2.1&pw=1` | `GET` | Prediction JSON |

---

## Step-by-Step Solution

### Step 1 — Create the FastAPI Application

A FastAPI application was created in `app.py`. It loads the Iris dataset, trains a `DecisionTreeClassifier`, and exposes the required endpoints.

Final `app.py` used:

```python
import numpy as np
from fastapi import FastAPI
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier


app = FastAPI(title="GA8 Q12 Iris Classifier")


iris = load_iris()
model = DecisionTreeClassifier(random_state=42)
model.fit(iris.data, iris.target)
CLASS_NAMES = ["setosa", "versicolor", "virginica"]


@app.get("/health")
async def health():
    return {"status": "ok", "model": "iris-classifier"}


@app.get("/info")
async def info():
    return {
        "model_type": "DecisionTreeClassifier",
        "random_state": 42,
        "dataset": "iris",
        "classes": CLASS_NAMES,
    }


@app.get("/predict")
async def predict(sl: float, sw: float, pl: float, pw: float):
    features = np.array([[sl, sw, pl, pw]])
    pred = int(model.predict(features)[0])
    proba = model.predict_proba(features)[0]
    confidence = float(max(proba))
    return {
        "prediction": pred,
        "class_name": CLASS_NAMES[pred],
        "confidence": round(confidence, 4),
    }
```

---

### Step 2 — Add Requirements

A `requirements.txt` file was created so the deployment platform could install the required dependencies.

Contents:

```text
fastapi
uvicorn
scikit-learn
numpy
```

---

### Step 3 — Add Dockerfile

A `Dockerfile` was included for container-based compatibility.

Contents:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

### Step 4 — Test Locally

The model was tested locally with the seeded feature values.

Prediction input:

```text
sl=7.7, sw=2.3, pl=2.1, pw=1
```

Expected response:

```json
{"prediction":0,"class_name":"setosa","confidence":1.0}
```

---

## Step 5 — Deploy the App

The app was deployed on Azure App Service because the grader accepted Azure deployment URLs.

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

## Step 6 — Verify the Deployed Endpoints

After deployment, all required public endpoints were tested.

Health endpoint:

```text
https://tds-ga8-q12-iris-ashka.azurewebsites.net/health
```

Response:

```json
{"status":"ok","model":"iris-classifier"}
```

Info endpoint:

```text
https://tds-ga8-q12-iris-ashka.azurewebsites.net/info
```

Response:

```json
{"model_type":"DecisionTreeClassifier","random_state":42,"dataset":"iris","classes":["setosa","versicolor","virginica"]}
```

Prediction endpoint:

```text
https://tds-ga8-q12-iris-ashka.azurewebsites.net/predict?sl=7.7&sw=2.3&pl=2.1&pw=1
```

Response:

```json
{"prediction":0,"class_name":"setosa","confidence":1.0}
```

---

## Final Submitted URL

```text
https://tds-ga8-q12-iris-ashka.azurewebsites.net
```

---

## Conclusion

This question demonstrated the full ML deployment path: train a Decision Tree model on the Iris dataset, expose inference through FastAPI, deploy the service publicly, and verify all required endpoints. The deployed Azure App Service returned the expected `setosa` prediction for the assigned sample.
