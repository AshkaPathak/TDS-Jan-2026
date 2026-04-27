import hashlib

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(title="GA8 Q9 Compute Service")


class ComputeRequest(BaseModel):
    a: int
    b: int


@app.get("/")
async def root():
    return {
        "message": "GA8 Q9 Compute Service is running",
        "endpoints": ["/health", "/compute"],
    }


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/compute")
async def compute(req: ComputeRequest):
    total = req.a + req.b
    product = req.a * req.b

    verify = hashlib.sha256(
        f"sum:{total}:product:{product}".encode()
    ).hexdigest()[:10]

    return {
        "sum": total,
        "product": product,
        "verify": verify,
    }
