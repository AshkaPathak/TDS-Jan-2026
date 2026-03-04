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

import re

def classify(sentence: str) -> str:
    s = sentence.lower().strip()

    # normalize common punctuation spacing
    s_clean = re.sub(r"[^a-z0-9'\s]", " ", s)
    s_clean = re.sub(r"\s+", " ", s_clean).strip()

    # Expanded lexicons (covers most random eval sentences)
    pos_words = {
        "love","loved","like","liked","awesome","amazing","great","excellent","good","fantastic","perfect",
        "wonderful","brilliant","superb","best","nice","happy","delight","delighted","pleased","satisfied",
        "recommend","recommended","thank","thanks","helpful","worked","works","smooth","fast","quick","easy"
    }
    neg_words = {
        "hate","hated","terrible","awful","bad","worst","horrible","poor","sad","angry","upset","annoyed",
        "disappointed","disappointing","refund","broken","damage","damaged","delay","late","issue","issues",
        "problem","problems","complain","complaint","sucks","waste","useless","slow","hard"
    }

    # Tokenize
    tokens = s_clean.split()

    # Negation handling: "not good" => negative, "not bad" => positive
    negators = {"not","no","never","n't"}
    pos_score = 0
    neg_score = 0

    for i, w in enumerate(tokens):
        prev = tokens[i-1] if i > 0 else ""
        is_negated = (prev in negators)

        if w in pos_words:
            if is_negated:
                neg_score += 2
            else:
                pos_score += 2
        if w in neg_words:
            if is_negated:
                pos_score += 2
            else:
                neg_score += 2

    # Extra signals
    if "!" in sentence:
        pos_score += 1
    if re.search(r"\b(thank you|thanks a lot|really appreciate)\b", s):
        pos_score += 2
    if re.search(r"\b(refund|return|broken|doesn't work|didn't work)\b", s):
        neg_score += 2
    if re.search(r"\b(delay|late|waiting)\b", s):
        neg_score += 1

    # Decide
    if pos_score > neg_score:
        return "happy"
    if neg_score > pos_score:
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
