import hashlib

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(title="GA8 Q10 Text Processor")


class TextRequest(BaseModel):
    text: str


def analyze_text(text: str) -> dict[str, int | str]:
    uppercase = text.upper()
    char_count = len(text.replace("-", "").replace(" ", ""))
    word_count = len(text.replace("-", " ").split())
    sha = hashlib.sha256(text.encode()).hexdigest()[:16]
    verify = hashlib.sha256(
        f"upper:{uppercase}:chars:{char_count}:words:{word_count}".encode()
    ).hexdigest()[:12]

    return {
        "uppercase": uppercase,
        "char_count": char_count,
        "word_count": word_count,
        "sha256": sha,
        "verify": verify,
    }


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/")
@app.post("/text-processor")
async def process_text(req: TextRequest):
    if "text" not in req.model_fields_set:
        raise HTTPException(status_code=400, detail='Missing "text" field in JSON body')
    return analyze_text(req.text)
