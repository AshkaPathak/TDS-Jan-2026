from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/")
@app.post("/sentiment")
def sentiment(data: dict):
    results = []

    positive_words = ["love", "great", "excellent", "good", "amazing"]
    negative_words = ["terrible", "bad", "hate", "awful"]

    for sentence in data["sentences"]:
        s = sentence.lower()

        if any(w in s for w in positive_words):
            label = "happy"
        elif any(w in s for w in negative_words):
            label = "sad"
        else:
            label = "neutral"

        results.append({
            "sentence": sentence,
            "sentiment": label
        })

    return {"results": results}
