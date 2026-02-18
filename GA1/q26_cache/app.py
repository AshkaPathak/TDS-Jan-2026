# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "fastapi",
#   "uvicorn",
#   "numpy",
#   "scikit-learn",
# ]
# ///

from __future__ import annotations

import hashlib
import time
from dataclasses import dataclass
from typing import Dict, Optional, Tuple

import numpy as np
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sklearn.feature_extraction.text import HashingVectorizer

MAX_CACHE_SIZE = 1500
TTL_SECONDS = 24 * 60 * 60
SEMANTIC_THRESHOLD = 0.95

AVG_TOKENS_PER_REQUEST = 3000
MODEL_COST_PER_1M_TOKENS = 1.00


class QueryIn(BaseModel):
    query: str
    application: str = "document summarizer"


class QueryOut(BaseModel):
    answer: str
    cached: bool
    latency: int
    cacheKey: str


@dataclass
class CacheEntry:
    answer: str
    created_at: float
    last_access: float
    freq: int
    vec: np.ndarray
    exact_key: str


app = FastAPI(title="TDS GA1 Q26 - Intelligent Cache")

_vectorizer = HashingVectorizer(
    n_features=2**12,
    alternate_sign=False,
    norm=None,
    lowercase=True,
)

_cache: Dict[str, CacheEntry] = {}

_total_requests = 0
_cache_hits = 0
_cache_misses = 0
_latency_hit_ms_total = 0
_latency_miss_ms_total = 0


def _now() -> float:
    return time.time()


def _normalize(text: str) -> str:
    return " ".join(text.strip().lower().split())


def _exact_key(application: str, query: str) -> str:
    payload = f"{application}::{_normalize(query)}".encode("utf-8")
    return hashlib.md5(payload).hexdigest()


def _embed(text: str) -> np.ndarray:
    X = _vectorizer.transform([text])
    v = X.toarray().astype(np.float32)[0]
    n = np.linalg.norm(v)
    return v if n == 0 else (v / n)


def _cosine(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.dot(a, b))


def _is_expired(e: CacheEntry) -> bool:
    return (_now() - e.created_at) > TTL_SECONDS


def _evict_lru():
    expired = [k for k, e in _cache.items() if _is_expired(e)]
    for k in expired:
        _cache.pop(k, None)

    while len(_cache) > MAX_CACHE_SIZE:
        lru_key = min(_cache.items(), key=lambda kv: kv[1].last_access)[0]
        _cache.pop(lru_key, None)


def _semantic_lookup(vec: np.ndarray) -> Optional[Tuple[str, CacheEntry, float]]:
    best_key = None
    best_entry = None
    best_sim = -1.0

    for k, e in _cache.items():
        if _is_expired(e):
            continue
        sim = _cosine(vec, e.vec)
        if sim > best_sim:
            best_sim = sim
            best_key = k
            best_entry = e

    if best_entry is not None and best_sim >= SEMANTIC_THRESHOLD:
        return best_key, best_entry, best_sim
    return None


def _summarize_stub(query: str) -> str:
    q = query.strip()
    if not q:
        return "Summary: (empty query)"
    if len(q) > 400:
        q = q[:400] + "…"
    return f"Summary: {q}"


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/", response_model=QueryOut)
def main_endpoint(payload: QueryIn):
    global _total_requests, _cache_hits, _cache_misses
    global _latency_hit_ms_total, _latency_miss_ms_total

    start = time.perf_counter()
    _total_requests += 1

    if payload.application != "document summarizer":
        raise HTTPException(status_code=400, detail="application must be 'document summarizer'")

    q = payload.query or ""
    exact = _exact_key(payload.application, q)

    e = _cache.get(exact)
    if e and not _is_expired(e):
        e.last_access = _now()
        e.freq += 1
        latency_ms = int((time.perf_counter() - start) * 1000)
        _cache_hits += 1
        _latency_hit_ms_total += latency_ms
        return QueryOut(answer=e.answer, cached=True, latency=latency_ms, cacheKey=exact)

    vec = _embed(_normalize(q))
    sem = _semantic_lookup(vec)
    if sem:
        _, entry, _sim = sem
        entry.last_access = _now()
        entry.freq += 1
        latency_ms = int((time.perf_counter() - start) * 1000)
        _cache_hits += 1
        _latency_hit_ms_total += latency_ms
        return QueryOut(answer=entry.answer, cached=True, latency=latency_ms, cacheKey=entry.exact_key)

    answer = _summarize_stub(q)
    entry = CacheEntry(
        answer=answer,
        created_at=_now(),
        last_access=_now(),
        freq=1,
        vec=vec,
        exact_key=exact,
    )
    _cache[exact] = entry
    _evict_lru()

    latency_ms = int((time.perf_counter() - start) * 1000)
    _cache_misses += 1
    _latency_miss_ms_total += latency_ms

    return QueryOut(answer=answer, cached=False, latency=latency_ms, cacheKey=exact)


@app.get("/analytics")
def analytics():
    _evict_lru()

    total = _total_requests
    hits = _cache_hits
    misses = _cache_misses
    hit_rate = (hits / total) if total else 0.0

    cached_tokens = hits * AVG_TOKENS_PER_REQUEST
    baseline_tokens = total * AVG_TOKENS_PER_REQUEST

    cost_savings = (cached_tokens * MODEL_COST_PER_1M_TOKENS) / 1_000_000
    baseline_cost = (baseline_tokens * MODEL_COST_PER_1M_TOKENS) / 1_000_000
    savings_percent = (cost_savings / baseline_cost * 100) if baseline_cost else 0.0

    avg_hit_latency = (_latency_hit_ms_total / hits) if hits else 0.0
    avg_miss_latency = (_latency_miss_ms_total / misses) if misses else 0.0

    return {
        "hitRate": round(hit_rate, 4),
        "totalRequests": total,
        "cacheHits": hits,
        "cacheMisses": misses,
        "cacheSize": len(_cache),
        "avgHitLatencyMs": round(avg_hit_latency, 2),
        "avgMissLatencyMs": round(avg_miss_latency, 2),
        "costSavings": round(cost_savings, 4),
        "savingsPercent": round(savings_percent, 2),
        "strategies": ["exact match", "semantic similarity", "LRU eviction", "TTL expiration"],
        "semanticThreshold": SEMANTIC_THRESHOLD,
        "ttlSeconds": TTL_SECONDS,
        "maxCacheSize": MAX_CACHE_SIZE,
    }

