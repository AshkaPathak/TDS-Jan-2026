# GA5 — Q2: Multimodal Embeddings — CLIP Image Search

## Problem Summary

The objective of this task was to identify which image among **10 candidate images** best matched the given natural language query using **CLIP embeddings** from the `sentence-transformers` library.

The text query provided was:

```text
a snow-covered mountain peak with white slopes and clear sky
```

The required workflow was:

1. Load all 10 images from the provided ZIP file.
2. Use the `sentence-transformers` CLIP model:

```text
clip-ViT-B-32
```

3. Compute:
   - the embedding for the text query
   - the embedding for each image
4. Measure **cosine similarity** between the text embedding and each image embedding.
5. Submit the filename of the image with the **highest similarity score**.

The required submission format was:

```text
img_XX.jpg
```

---

## Dataset

The provided ZIP archive was:

```text
q-multimodal-image-search.zip
```

After extraction, the folder contained:

```text
img_01.jpg
img_02.jpg
img_03.jpg
img_04.jpg
img_05.jpg
img_06.jpg
img_07.jpg
img_08.jpg
img_09.jpg
img_10.jpg
```

Repository location:

```text
GA5/q02_clip_image_search/
```

---

## Approach

## Step 1 — Extract the Image Files

The ZIP archive was extracted using:

```bash
unzip q-multimodal-image-search.zip
```

This made all 10 image files available in the same directory as the script.

---

## Step 2 — Load the CLIP Model

The required model was loaded using `sentence-transformers`:

```python
model = SentenceTransformer("clip-ViT-B-32")
```

This model maps both text and images into the same shared embedding space.

---

## Step 3 — Encode the Text Query

The given query:

```text
a snow-covered mountain peak with white slopes and clear sky
```

was encoded into a text embedding.

To ensure proper cosine similarity calculation, the embedding was normalized:

```python
text_embedding = text_embedding / np.linalg.norm(text_embedding)
```

---

## Step 4 — Encode Each Image

Each image from `img_01.jpg` to `img_10.jpg` was loaded using Pillow and converted to RGB format:

```python
image = Image.open(image_file).convert("RGB")
```

Then each image was encoded using the same CLIP model.

Each image embedding was also normalized before similarity comparison.

---

## Step 5 — Compute Cosine Similarity

Cosine similarity was computed between the text embedding and each image embedding using:

```python
cosine_similarity = float(np.dot(text_embedding, image_embedding))
```

Since both vectors were normalized, the dot product directly gave cosine similarity.

---

## Step 6 — Select the Best Matching Image

The image with the highest similarity score was tracked during iteration and printed at the end.

---

## Python Implementation

```python
# /// script
# requires-python = ">=3.11"
# dependencies = ["sentence-transformers", "Pillow", "numpy"]
# ///

from sentence_transformers import SentenceTransformer
from PIL import Image
import numpy as np

TEXT_QUERY = "a snow-covered mountain peak with white slopes and clear sky"

model = SentenceTransformer("clip-ViT-B-32")

image_files = [f"img_{i:02d}.jpg" for i in range(1, 11)]

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
```

---

## Output

Running the script:

```bash
uv run solution.py
```

produced:

```text
img_01.jpg: 0.101954
img_02.jpg: 0.317222
img_03.jpg: 0.096113
img_04.jpg: 0.128702
img_05.jpg: 0.129705
img_06.jpg: 0.129675
img_07.jpg: 0.115089
img_08.jpg: 0.137048
img_09.jpg: 0.131772
img_10.jpg: 0.181602

Most similar image:
img_02.jpg
```

---

## Final Answer Submitted

```text
img_02.jpg
```

---

## Repository Structure

```text
GA5/q02_clip_image_search/
├── img_01.jpg
├── img_02.jpg
├── img_03.jpg
├── img_04.jpg
├── img_05.jpg
├── img_06.jpg
├── img_07.jpg
├── img_08.jpg
├── img_09.jpg
├── img_10.jpg
├── q-multimodal-image-search.zip
├── solution.py
└── q02_clip_image_search.md
```

---

## Conclusion

Using the `clip-ViT-B-32` model from `sentence-transformers`, all 10 images were compared against the given query using cosine similarity.

The image with the highest similarity score was:

```text
img_02.jpg
```

This was the final submitted answer.
