# /// script
# requires-python = ">=3.11"
# dependencies = ["sentence-transformers", "Pillow", "numpy"]
# ///

from sentence_transformers import SentenceTransformer
from PIL import Image
import numpy as np
import os

TEXT_QUERY = "a snow-covered mountain peak with white slopes and clear sky"

model = SentenceTransformer("clip-ViT-B-32")

image_files = [f"img_{i:02d}.jpg" for i in range(1, 11)]

# Encode text
text_embedding = model.encode([TEXT_QUERY], convert_to_numpy=True)[0]
text_embedding = text_embedding / np.linalg.norm(text_embedding)

best_file = None
best_score = -1.0

for image_file in image_files:
    image = Image.open(image_file).convert("RGB")
    image_embedding = model.encode([image], convert_to_numpy=True)[0]
    image_embedding = image_embedding / np.linalg.norm(image_embedding)

    cosine_similarity = float(np.dot(text_embedding, image_embedding))

    print(f"{image_file}: {cosine_similarity:.6f}")

    if cosine_similarity > best_score:
        best_score = cosine_similarity
        best_file = image_file

print("\nMost similar image:")
print(best_file)

