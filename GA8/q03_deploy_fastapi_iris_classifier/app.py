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
