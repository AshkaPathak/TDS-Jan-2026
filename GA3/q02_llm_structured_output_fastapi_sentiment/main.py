from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
import os, json

load_dotenv()

app = FastAPI()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://aipipe.org/openrouter/v1",
)

class CommentRequest(BaseModel):
    comment: str

@app.get("/")
def health():
    return {"ok": True}

@app.post("/comment")
async def analyze_comment(data: CommentRequest):
    try:
        resp = client.chat.completions.create(
            model="openai/gpt-4.1-nano",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a strict sentiment classifier. "
                        "Return ONLY JSON in this format: "
                        '{"sentiment": "positive|negative|neutral", "rating": 1-5}'
                    ),
                },
                {"role": "user", "content": data.comment},
            ],
        )

        content = resp.choices[0].message.content
        return json.loads(content)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
