from __future__ import annotations

import os
from typing import List

import numpy as np
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from openai import OpenAI

app = FastAPI()

# CORS: allow everything (simple + passes browser preflight)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],  # includes OPTIONS + POST
    allow_headers=["*"],
)

# AI Pipe (OpenAI-compatible) settings:
# Set these in environment (local + Render):
#   OPENAI_API_KEY   = your AI Pipe token (JWT)
#   OPENAI_BASE_URL  = https://aipipe.org/openai/v1
#
# If OPENAI_BASE_URL is not set, we default to AI Pipe.
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL", "https://aipipe.org/openai/v1"),
)

EMBED_MODEL = "text-embedding-3-small"


class SimilarityRequest(BaseModel):
    docs: List[str] = Field(..., min_length=1)
    query: str = Field(..., min_length=1)


def embed(texts: List[str]) -> np.ndarray:
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY is not set (AI Pipe token required)")

    resp = client.embeddings.create(
        model=EMBED_MODEL,
        input=texts,
    )
    return np.array([d.embedding for d in resp.data], dtype=np.float32)


def cosine_sim(matrix: np.ndarray, vec: np.ndarray) -> np.ndarray:
    # matrix: (n, d), vec: (d,)
    m = matrix / (np.linalg.norm(matrix, axis=1, keepdims=True) + 1e-12)
    v = vec / (np.linalg.norm(vec) + 1e-12)
    return m @ v


@app.post("/similarity")
def similarity(req: SimilarityRequest):
    docs = [d.strip() for d in req.docs]
    query = req.query.strip()

    if not query:
        raise HTTPException(status_code=400, detail="query cannot be empty")
    if any(not d for d in docs):
        raise HTTPException(status_code=400, detail="docs cannot contain empty strings")

    try:
        doc_vecs = embed(docs)          # (n, d)
        query_vec = embed([query])[0]   # (d,)

        sims = cosine_sim(doc_vecs, query_vec)  # (n,)

        k = min(3, len(docs))
        top_idx = np.argsort(-sims)[:k]
        matches = [docs[i] for i in top_idx]
        return {"matches": matches}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


