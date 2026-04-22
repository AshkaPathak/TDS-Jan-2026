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
    return {"label": result["label"], "score": result["score"]}    result = classifier(request.text)[0]
    return {"label": result["label"], "score": result["score"]}
