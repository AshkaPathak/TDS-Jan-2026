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
