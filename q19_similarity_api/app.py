from __future__ import annotations

from typing import List

import numpy as np
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from sklearn.feature_extraction.text import TfidfVectorizer


app = FastAPI()

# CORS: allow everything (simple + passes browser preflight)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],  # includes OPTIONS + POST
    allow_headers=["*"],
)


class SimilarityRequest(BaseModel):
    docs: List[str] = Field(..., min_length=1)
    query: str = Field(..., min_length=1)


def top_k_tfidf(docs: List[str], query: str, k: int = 3) -> List[str]:
    # Fit TF-IDF on docs + query together to share vocabulary
    texts = docs + [query]
    vec = TfidfVectorizer()
    X = vec.fit_transform(texts)  # sparse matrix

    doc_mat = X[:-1]   # (n_docs, d)
    q_vec = X[-1]      # (1, d)

    # Cosine similarity for TF-IDF (already L2-normalized by default, but we’ll be safe)
    sims = (doc_mat @ q_vec.T).toarray().reshape(-1)  # (n_docs,)

    k = min(k, len(docs))
    top_idx = np.argsort(-sims)[:k]
    return [docs[i] for i in top_idx]


@app.post("/similarity")
def similarity(req: SimilarityRequest):
    docs = [d.strip() for d in req.docs]
    query = req.query.strip()

    if not query:
        raise HTTPException(status_code=400, detail="query cannot be empty")
    if any(not d for d in docs):
        raise HTTPException(status_code=400, detail="docs cannot contain empty strings")

    matches = top_k_tfidf(docs, query, k=3)
    return {"matches": matches}


@app.get("/")
def root():
    return {"status": "ok"}
