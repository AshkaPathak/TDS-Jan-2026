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
