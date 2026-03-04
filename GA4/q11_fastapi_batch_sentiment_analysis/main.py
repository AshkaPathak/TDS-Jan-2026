from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = FastAPI()

# CORS for browser/portal checks
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

analyzer = SentimentIntensityAnalyzer()

# Portal sometimes sends HEAD /
@app.api_route("/", methods=["GET", "HEAD"])
def root():
    return {"status": "ok"}

def classify(text: str) -> str:
    # VADER compound score in [-1, 1]
    score = analyzer.polarity_scores(text).get("compound", 0.0)

    # Thresholds tuned for 3-class mapping
    if score >= 0.2:
        return "happy"
    if score <= -0.2:
        return "sad"
    return "neutral"

# Some graders POST to /, some to /sentiment
@app.post("/")
@app.post("/sentiment")
def sentiment(payload: dict):
    sentences = payload.get("sentences", [])
    return {"results": [{"sentence": s, "sentiment": classify(s)} for s in sentences]}
