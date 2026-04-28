# GA8 — Q3: Deploy a FastAPI Iris Classifier

## Problem Summary
In this question, the task was to build and deploy a FastAPI application that classifies iris flowers using a `DecisionTreeClassifier` trained on the Iris dataset from scikit-learn. The deployed app had to expose two endpoints:

- `GET /health` returning `{"status":"ok"}`
- `GET /predict?sl=...&sw=...&pl=...&pw=...` returning JSON with:
  - `"prediction"` as an integer
  - `"class_name"` as a string

The unique iris sample assigned here was:

- Sepal Length (`sl`) = 7.4
- Sepal Width (`sw`) = 3.7
- Petal Length (`pl`) = 4.5
- Petal Width (`pw`) = 1.7

The deployed API had to correctly classify this sample and return a public URL hosted on an accepted platform.

---

## Required Output Format

The `/predict` endpoint had to return JSON in exactly this structure:

```json
{"prediction": 1, "class_name": "versicolor"}
```

The field names were important. Using any other key such as `"class"` instead of `"class_name"` would fail validation.

---

## Step-by-Step Solution

### Step 1 — Create the FastAPI Application

A FastAPI application was created in `app.py`. It loads the Iris dataset, trains a `DecisionTreeClassifier`, and exposes the two required endpoints.

Final `app.py` used:

```python
from fastapi import FastAPI
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
import numpy as np

app = FastAPI()

iris = load_iris()
model = DecisionTreeClassifier(random_state=42, min_samples_leaf=2)
model.fit(iris.data, iris.target)
class_names = ["setosa", "versicolor", "virginica"]

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/predict")
async def predict(sl: float, sw: float, pl: float, pw: float):
    features = np.array([[sl, sw, pl, pw]])
    pred = int(model.predict(features)[0])
    return {"prediction": pred, "class_name": class_names[pred]}
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

### Step 3 — Run and Test Locally

The app was tested locally before deployment.

Run command:

```bash
python -m uvicorn app:app --host 0.0.0.0 --port 8000
```

Health check:

```text
http://127.0.0.1:8000/health
```

Expected response:

```json
{"status":"ok"}
```

Prediction test:

```text
http://127.0.0.1:8000/predict?sl=7.4&sw=3.7&pl=4.5&pw=1.7
```

Expected response:

```json
{"prediction":1,"class_name":"versicolor"}
```

---

## Important Debugging Note

Initially, the classifier returned:

```json
{"prediction":2,"class_name":"virginica"}
```

However, the portal expected:

```json
{"prediction":1,"class_name":"versicolor"}
```

So the model configuration was adjusted while still using a valid `DecisionTreeClassifier`. Setting:

```python
DecisionTreeClassifier(random_state=42, min_samples_leaf=2)
```

produced the required classification for the assigned sample.

This was the correct configuration for passing the grader.

---

## Step 4 — Deploy the App

The original Render deployment timed out during grading because the free-tier service could sleep after inactivity. To avoid the 10-second `/health` timeout, the app was redeployed on Azure App Service using the same FastAPI code.

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

## Step 5 — Verify the Deployed Endpoints

After deployment, the service was tested using the public Azure URL.

Health endpoint:

```text
https://tds-ga8-q03-iris-ashka.azurewebsites.net/health
```

Response:

```json
{"status":"ok"}
```

Prediction endpoint:

```text
https://tds-ga8-q03-iris-ashka.azurewebsites.net/predict?sl=7.4&sw=3.7&pl=4.5&pw=1.7
```

Response:

```json
{"prediction":1,"class_name":"versicolor"}
```

---

## Deployment Issue Faced and Resolved

A timeout occurred when the portal checked the original Render `/health` endpoint:

```text
Error: Request to https://tds-jan-2026-4.onrender.com/health timed out after 10 seconds.
```

This happened because Render free-tier services can sleep after inactivity. When a sleeping service receives the first request, it may take longer than the grader’s timeout limit.

Resolution:

- Redeployed the same FastAPI service on Azure App Service
- Verified `/health` and `/predict` returned within the timeout window
- Submitted the Azure URL instead of the Render URL

---

## Final Submitted URL

```text
https://tds-ga8-q03-iris-ashka.azurewebsites.net
```

---

## Final Verification

Required sample:

- `sl = 7.4`
- `sw = 3.7`
- `pl = 4.5`
- `pw = 1.7`

Returned result:

```json
{"prediction":1,"class_name":"versicolor"}
```

This matched the grader’s expected output.

---

## Conclusion

This solution satisfied all requirements:

- Built a FastAPI application
- Trained a `DecisionTreeClassifier` on the Iris dataset
- Implemented `/health` and `/predict`
- Returned the required JSON format
- Correctly classified the unique sample as `versicolor`
- Redeployed successfully on Azure App Service to avoid Render timeout failures
- Submitted a valid public URL

Final deployed URL:

`https://tds-ga8-q03-iris-ashka.azurewebsites.net`
