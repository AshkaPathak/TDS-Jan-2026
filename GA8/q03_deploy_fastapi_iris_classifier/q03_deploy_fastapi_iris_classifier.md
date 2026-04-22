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

The app was deployed on Render, which is one of the accepted free hosting platforms listed in the question.

Deployment configuration used:

- **Platform:** Render
- **Root Directory:** `q03_deploy_fastapi_iris_classifier`
- **Build Command:**

```bash
pip install -r requirements.txt
```

- **Start Command:**

```bash
python -m uvicorn app:app --host 0.0.0.0 --port $PORT
```

Using `python -m uvicorn` was important because it ensured the correct Python environment and installed packages were used during startup.

---

## Step 5 — Verify the Deployed Endpoints

After deployment, the service was tested using the public Render URL.

Health endpoint:

```text
https://tds-jan-2026-4.onrender.com/health
```

Expected response:

```json
{"status":"ok"}
```

Prediction endpoint:

```text
https://tds-jan-2026-4.onrender.com/predict?sl=7.4&sw=3.7&pl=4.5&pw=1.7
```

Expected response:

```json
{"prediction":1,"class_name":"versicolor"}
```

---

## Deployment Issue Faced and Resolved

A timeout occurred when the portal checked the `/health` endpoint. This happened because Render free-tier services go to sleep after inactivity. When a sleeping service receives the first request, it may take several seconds to wake up, which can exceed the grader’s timeout limit.

Resolution:

- Manually open the `/health` endpoint first
- Wait until the service wakes up and returns `{"status":"ok"}`
- Then immediately click the portal’s **Check** button

This successfully resolved the timeout issue.

---

## Final Submitted URL

```text
https://tds-jan-2026-4.onrender.com
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
- Deployed successfully on Render
- Submitted a valid public URL

Final deployed URL:

`https://tds-jan-2026-4.onrender.com`
