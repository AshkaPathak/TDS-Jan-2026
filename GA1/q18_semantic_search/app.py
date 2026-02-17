import json
import os
import time
from pathlib import Path
from typing import Any, Dict, List, Optional

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from rank_bm25 import BM25Okapi

app = FastAPI(title="GA1 Q18 Semantic Search")

# ✅ CORS REQUIRED (portal fetch)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATA_PATH = Path(__file__).parent / "data" / "abstracts.json"
ABSTRACTS_URL = os.getenv("ABSTRACTS_URL")  # optional remote JSON

_docs: List[Dict[str, Any]] = []
_tfidf: Optional[TfidfVectorizer] = None
_tfidf_mat = None
_bm25: Optional[BM25Okapi] = None
_tokenized: List[List[str]] = []


class SearchRequest(BaseModel):
    query: str = Field(..., min_length=1)
    k: int = Field(8, ge=1, le=50)
    rerank: bool = True
    rerankK: int = Field(5, ge=1, le=50)


def _normalize_0_1(scores: List[float]) -> List[float]:
    if not scores:
        return scores
    mn, mx = min(scores), max(scores)
    if mx - mn < 1e-12:
        return [1.0 for _ in scores]
    return [(s - mn) / (mx - mn) for s in scores]


def _tokenize(text: str) -> List[str]:
    return [t for t in "".join(ch.lower() if ch.isalnum() else " " for ch in text).split() if t]


def _load_docs_local() -> List[Dict[str, Any]]:
    if not DATA_PATH.exists():
        return []
    with DATA_PATH.open("r", encoding="utf-8") as f:
        return json.load(f)


def _load_docs_remote(url: str) -> List[Dict[str, Any]]:
    import urllib.request
    with urllib.request.urlopen(url, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def _extract_text(doc: Dict[str, Any]) -> str:
    for key in ("content", "abstract", "text", "body"):
        if key in doc and isinstance(doc[key], str):
            return doc[key]
    return json.dumps(doc, ensure_ascii=False)


def _extract_metadata(doc: Dict[str, Any]) -> Dict[str, Any]:
    md = doc.get("metadata")
    if isinstance(md, dict):
        return md
    meta = {}
    for k in ("source", "title", "year", "authors"):
        if k in doc:
            meta[k] = doc[k]
    return meta


def _build_index(docs: List[Dict[str, Any]]) -> None:
    global _docs, _tfidf, _tfidf_mat, _bm25, _tokenized
    _docs = docs
    texts = [_extract_text(d) for d in _docs]

    _tfidf = TfidfVectorizer(stop_words="english")
    _tfidf_mat = _tfidf.fit_transform(texts)

    _tokenized = [_tokenize(t) for t in texts]
    _bm25 = BM25Okapi(_tokenized)


@app.on_event("startup")
def startup() -> None:
    docs = _load_docs_local()
    if not docs and ABSTRACTS_URL:
        try:
            docs = _load_docs_remote(ABSTRACTS_URL)
        except Exception:
            docs = []

    if docs:
        _build_index(docs)


@app.get("/")
def health() -> Dict[str, Any]:
    return {"ok": True, "totalDocs": len(_docs)}


@app.post("/search")
def search(req: SearchRequest) -> Dict[str, Any]:
    if not _docs or _tfidf is None or _tfidf_mat is None:
        raise HTTPException(
            status_code=500,
            detail="Abstract corpus not loaded. Provide data/abstracts.json or set ABSTRACTS_URL.",
        )

    t0 = time.time()
    query = req.query.strip()

    q_vec = _tfidf.transform([query])
    cos = cosine_similarity(q_vec, _tfidf_mat).flatten()

    k = min(req.k, len(_docs))
    top_idx = cos.argsort()[::-1][:k].tolist()
    top_scores = [float(cos[i]) for i in top_idx]
    norm_top_scores = _normalize_0_1(top_scores)

    results = []
    for i, s in zip(top_idx, norm_top_scores):
        d = _docs[i]
        results.append(
            {
                "id": d.get("id", i),
                "score": round(float(s), 6),
                "content": _extract_text(d),
                "metadata": _extract_metadata(d),
                "_idx": i,  # internal
            }
        )

    reranked = False
    if req.rerank and _bm25 is not None:
        rerankK = min(req.rerankK, len(results))
        candidates = results[:rerankK]

        q_tokens = _tokenize(query)
        bm25_scores = [_bm25.get_score(q_tokens, c["_idx"]) for c in candidates]
        bm25_norm = _normalize_0_1([float(x) for x in bm25_scores])

        for c, s in zip(candidates, bm25_norm):
            c["score"] = round(float(s), 6)

        candidates_sorted = sorted(candidates, key=lambda x: x["score"], reverse=True)
        results = candidates_sorted + results[rerankK:]
        reranked = True

    for r in results:
        r.pop("_idx", None)

    latency_ms = int((time.time() - t0) * 1000)

    return {
        "results": results[: min(5, len(results))],
        "reranked": reranked,
        "metrics": {"latency": latency_ms, "totalDocs": len(_docs)},
    }
