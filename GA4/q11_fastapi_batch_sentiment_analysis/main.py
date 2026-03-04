from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/sentiment")
def sentiment(data: dict):
    results = []

    positive_words = ["love", "great", "excellent", "good", "amazing"]
    negative_words = ["terrible", "bad", "hate", "awful"]

    for sentence in data["sentences"]:
        s = sentence.lower()

        if any(word in s for word in positive_words):
            sentiment = "happy"
        elif any(word in s for word in negative_words):
            sentiment = "sad"
        else:
            sentiment = "neutral"

        results.append({
            "sentence": sentence,
            "sentiment": sentiment
        })

    return {"results": results}
