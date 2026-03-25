# GA6 — Q9: The Embedding Auditor

## Problem Summary

You are given 40 sentence pairs with precomputed 32-dimensional embeddings. Each pair belongs to one of three semantic categories: paraphrase, negation, or near_duplicate.

Each pair includes two embeddings (embedding_a and embedding_b), a similarity threshold, and a threshold operator (>= or <=).

Your task is to compute the cosine similarity between the embeddings, check whether each pair satisfies its threshold condition, and count the number of failures per category.

---

## Key Insight

The embeddings are already L2-normalised. Therefore, cosine similarity simplifies to the dot product:

cos(A, B) = A · B

This means we do not need to compute magnitudes — just compute the dot product directly.

---

## Invariance Rules

- paraphrase → similarity ≥ 0.80 → fails if similarity < threshold  
- negation → similarity ≤ 0.50 → fails if similarity > threshold  
- near_duplicate → similarity ≥ 0.97 → fails if similarity < threshold  

---

## Implementation Steps

1. Load the JSON file containing all pairs.
2. Define a function to compute the dot product.
3. Initialize counters for each type.
4. Iterate over each pair:
   - Compute similarity using dot product
   - Apply threshold condition based on threshold_op
   - Increment failure count if condition is violated
5. Output the counts.

---

## Reference Implementation (Python)

import json

with open("23f3002663_ds_study_iitm_ac_in_embeddings.json") as f:
    data = json.load(f)

def dot(a, b):
    return sum(x * y for x, y in zip(a, b))

counts = {
    "paraphrase": 0,
    "negation": 0,
    "near_duplicate": 0
}

for pair in data:
    sim = dot(pair["embedding_a"], pair["embedding_b"])

    if pair["threshold_op"] == ">=":
        fails = sim < pair["threshold"]
    else:
        fails = sim > pair["threshold"]

    if fails:
        counts[pair["type"]] += 1

print(counts)

---

## Final Answer

14,0,2

Where:
paraphrase_failures = 14  
negation_failures = 0  
near_duplicate_failures = 2  
