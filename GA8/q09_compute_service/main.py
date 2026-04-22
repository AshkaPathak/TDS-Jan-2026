import hashlib
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ComputeRequest(BaseModel):
    a: int
    b: int

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/compute")
async def compute(req: ComputeRequest):
    s = req.a + req.b
    p = req.a * req.b
    v = hashlib.sha256(f"sum:{s}:product:{p}".encode()).hexdigest()[:10]
    return {"sum": s, "product": p, "verify": v}
