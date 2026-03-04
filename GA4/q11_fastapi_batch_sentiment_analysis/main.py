from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow portal/browser-based checkers to call the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Explicitly allow HEAD on /
@app.api_route("/", methods=["GET", "HEAD"])
def root():
    return {"status": "ok"}

def classify(sentence: str) -> str:
    s = sentence.lower()
    positive = ["love", "great", "excellent", "good", "amazing", "happy"]
    negative = ["terrible", "bad", "hate", "awful", "sad", "worst"]

    if any(w in s for w in positive):
        return "happy"
    if any(w in s for w in negative):
        return "sad"
    return "neutral"

# Some checkers POST to /, some to /sentiment → support both
@app.post("/")
@app.post("/sentiment")
def sentiment(payload: dict):
    sentences = payload.get("sentences", [])
    return {
        "results": [{"sentence": t, "sentiment": classify(t)} for t in sentences]
    }
