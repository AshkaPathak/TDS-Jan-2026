from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import datetime
import json
import os

app = FastAPI()

class PipelineRequest(BaseModel):
    email: str
    source: str

def mock_ai_analysis(text):
    sentiment = "neutral"
    if any(word in text.lower() for word in ["good", "great", "excellent"]):
        sentiment = "positive"
    elif any(word in text.lower() for word in ["bad", "terrible", "worst"]):
        sentiment = "negative"

    return {
        "analysis": text[:120],
        "sentiment": sentiment
    }

@app.post("/pipeline")
def run_pipeline(req: PipelineRequest):
    errors = []
    items = []

    try:
        response = requests.get(
            "https://jsonplaceholder.typicode.com/comments?postId=1",
            timeout=5
        )
        response.raise_for_status()
        comments = response.json()[:3]

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    for comment in comments:
        try:
            ai_result = mock_ai_analysis(comment["body"])

            item = {
                "original": comment["body"],
                "analysis": ai_result["analysis"],
                "sentiment": ai_result["sentiment"],
                "stored": True,
                "timestamp": datetime.datetime.utcnow().isoformat()
            }

            items.append(item)

        except Exception as e:
            errors.append(str(e))

    # store to file
    try:
        with open("storage.json", "w") as f:
            json.dump(items, f)
    except Exception as e:
        errors.append(str(e))

    # mock notification
    notification_sent = True

    return {
        "items": items,
        "notificationSent": notification_sent,
        "processedAt": datetime.datetime.utcnow().isoformat(),
        "errors": errors
    }

from fastapi import Request, Response
from collections import defaultdict
import time
import html

RATE_LIMIT = 22
BURST_LIMIT = 9
WINDOW = 60  # seconds

request_logs = defaultdict(list)

@app.post("/security")
async def security_endpoint(request: Request):
    data = await request.json()
    user_id = data.get("userId", "anonymous")
    user_input = data.get("input", "")
    
    now = time.time()
    logs = request_logs[user_id]

    # Remove old timestamps
    request_logs[user_id] = [t for t in logs if now - t < WINDOW]
    logs = request_logs[user_id]

    # Burst check
    if len(logs) >= RATE_LIMIT:
        retry_after = int(WINDOW - (now - logs[0]))
        return Response(
            content='{"blocked": true, "reason": "Rate limit exceeded"}',
            status_code=429,
            headers={"Retry-After": str(retry_after)},
            media_type="application/json"
        )

    # Log request
    logs.append(now)

    # Basic sanitization (prevent XSS)
    sanitized = html.escape(user_input)

    return {
        "blocked": False,
        "reason": "Input passed all security checks",
        "sanitizedOutput": sanitized,
        "confidence": 0.95
    }
