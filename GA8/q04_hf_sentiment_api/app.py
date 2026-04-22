from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

classifier = pipeline("sentiment-analysis")

class TextRequest(BaseModel):
    text: str

@app.post("/predict")
async def predict(request: TextRequest):
    result = classifier(request.text)[0]
    return {"label": result["label"], "score": result["score"]}
