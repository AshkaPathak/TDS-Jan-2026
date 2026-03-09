# GA5 — Q1: Embeddings + K-Means Clustering

## Problem Summary

The objective of this task was to cluster **50 text descriptions** into **5 clusters** using vector embeddings generated from the model **text-embedding-3-small**, and then identify the **largest cluster**.

The required steps were:

1. Generate embeddings for each description.
2. Run **K-Means clustering** with:

```
n_clusters = 5
random_state = 42
n_init = 10
```

3. Count the number of items assigned to each cluster.
4. Return the label of the largest cluster and its size.

The portal requires the answer in the format:

```
cluster_label, count
```

---

# Dataset

The dataset file provided was:

```
q-embeddings-clustering.txt
```

Location in repository:

```
GA5/q01_embeddings_kmeans/q-embeddings-clustering.txt
```

The file contains **50 text descriptions**, one per line.

---

# Approach

## Step 1 — Load Descriptions

The descriptions were loaded line-by-line while removing empty lines to ensure only valid text inputs were embedded.

```python
descriptions = [line.strip() for line in f if line.strip()]
```

---

## Step 2 — Generate Embeddings

Embeddings were generated using the model:

```
text-embedding-3-small
```

The **IITM AI Pipe key** was used instead of direct OpenAI billing.

Environment variables used:

```bash
export AIPIPE_API_KEY="your_iitm_key"
export OPENAI_API_KEY="$AIPIPE_API_KEY"
export OPENAI_BASE_URL="https://aipipe.org/openai/v1"
```

This allows the OpenAI SDK to route requests through **AI Pipe**.

---

## Step 3 — Convert Embeddings to Numpy Array

The returned embedding vectors were converted to a numpy array for clustering.

```python
embeddings = np.array([item.embedding for item in response.data])
```

---

## Step 4 — Run K-Means Clustering

The embeddings were clustered using the specified parameters.

```python
kmeans = KMeans(
    n_clusters=5,
    random_state=42,
    n_init=10
)
```

Cluster assignments were obtained using:

```python
labels = kmeans.fit_predict(embeddings)
```

---

## Step 5 — Compute Cluster Sizes

The number of items in each cluster was computed using:

```python
counts = np.bincount(labels)
```

Example cluster distribution:

```
[10, 17, 8, 7, 8]
```

---

## Step 6 — Identify Largest Cluster

The cluster label containing the largest number of items was obtained using:

```python
largest_cluster = int(np.argmax(counts))
largest_count = int(counts[largest_cluster])
```

---

# Python Implementation

```python
# /// script
# dependencies = [
#   "openai",
#   "scikit-learn",
#   "numpy"
# ]
# ///

from openai import OpenAI
import numpy as np
from sklearn.cluster import KMeans

client = OpenAI()

with open("q-embeddings-clustering.txt", "r") as f:
    descriptions = [line.strip() for line in f if line.strip()]

response = client.embeddings.create(
    model="text-embedding-3-small",
    input=descriptions
)

embeddings = np.array([item.embedding for item in response.data])

kmeans = KMeans(n_clusters=5, random_state=42, n_init=10)
labels = kmeans.fit_predict(embeddings)

counts = np.bincount(labels)
largest_cluster = int(np.argmax(counts))
largest_count = int(counts[largest_cluster])

print(f"{largest_cluster}, {largest_count}")
```

---

# Output

Running the script:

```bash
uv run solution.py
```

produced the output:

```
1, 17
```

---

# Final Answer Submitted

```
1, 17
```

This indicates:

- **Cluster label:** 1  
- **Number of items in largest cluster:** 17

---

# Repository Structure

```
GA5/q01_embeddings_kmeans/
├── q-embeddings-clustering.txt
├── solution.py
└── q01_embeddings_kmeans.md
```
