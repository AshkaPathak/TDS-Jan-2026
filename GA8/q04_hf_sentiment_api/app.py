from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="GA8 Q4 Sentiment API")

POSITIVE_WORDS = {
    "amazing",
    "awesome",
    "best",
    "enjoy",
    "excellent",
    "fantastic",
    "good",
    "great",
    "happy",
    "like",
    "love",
    "loved",
    "perfect",
    "positive",
    "wonderful",
}

NEGATIVE_WORDS = {
    "awful",
    "bad",
    "boring",
    "disappointing",
    "hate",
    "hated",
    "horrible",
    "negative",
    "poor",
    "sad",
    "terrible",
    "worst",
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
