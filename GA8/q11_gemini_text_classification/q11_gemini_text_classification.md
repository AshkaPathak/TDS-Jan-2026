# GA8 — Q11: GCP AI Studio — Gemini Text Classification

## Problem Summary
In this question, the task was to classify three seeded sentences as either `POSITIVE` or `NEGATIVE`, then compute a verification hash from the labels and total word count.

The unique sentences assigned here were:

1. The customer service was absolutely terrible and I will never return.
2. The repair cost was outrageously expensive and the problem still is not fixed.
3. This is the best movie I have ever seen in my entire life!

Final submission format:

```text
labels_csv,total_words,verify_hash
```

---

## Step-by-Step Solution

### Step 1 — Classify the Sentences

Each sentence was classified using sentiment meaning:

| Sentence | Reason | Label |
|---|---|---|
| The customer service was absolutely terrible and I will never return. | Strong negative words: `terrible`, `never return` | `NEGATIVE` |
| The repair cost was outrageously expensive and the problem still is not fixed. | Negative experience: `expensive`, `problem`, `not fixed` | `NEGATIVE` |
| This is the best movie I have ever seen in my entire life! | Strong positive praise: `best movie`, `ever seen` | `POSITIVE` |

Labels CSV:

```text
NEGATIVE,NEGATIVE,POSITIVE
```

---

### Step 2 — Count Total Words

Words were counted using whitespace-separated tokens across all three sentences.

Sentence 1:

```text
The customer service was absolutely terrible and I will never return.
```

Word count:

```text
11
```

Sentence 2:

```text
The repair cost was outrageously expensive and the problem still is not fixed.
```

Word count:

```text
13
```

Sentence 3:

```text
This is the best movie I have ever seen in my entire life!
```

Word count:

```text
13
```

Total words:

```text
37
```

---

### Step 3 — Count Total Characters

The hash formula uses total characters across all three sentences, including spaces and punctuation.

Character counts:

```text
Sentence 1: 69
Sentence 2: 78
Sentence 3: 58
```

Total characters:

```text
205
```

---

### Step 4 — Compute Verify Hash

Formula:

```text
sha256(email:labels_csv:total_words:total_chars)[:14]
```

Email used:

```text
23f3002663@ds.study.iitm.ac.in
```

Constructed input string:

```text
23f3002663@ds.study.iitm.ac.in:NEGATIVE,NEGATIVE,POSITIVE:37:205
```

SHA-256 hash, first 14 hex characters:

```text
f1c51776a2f83b
```

---

## Reproducible Script

The calculation was saved in `classify_sentiment.py`.

```python
import hashlib


EMAIL = "23f3002663@ds.study.iitm.ac.in"

sentences = [
    "The customer service was absolutely terrible and I will never return.",
    "The repair cost was outrageously expensive and the problem still is not fixed.",
    "This is the best movie I have ever seen in my entire life!",
]

labels = [
    "NEGATIVE",
    "NEGATIVE",
    "POSITIVE",
]


def main() -> None:
    total_words = 0
    total_chars = 0

    for i, (sentence, label) in enumerate(zip(sentences, labels), start=1):
        words = sentence.split()
        total_words += len(words)
        total_chars += len(sentence)
        print(f"Sentence {i}: {label} (words={len(words)}, chars={len(sentence)})")

    labels_csv = ",".join(labels)
    verify_input = f"{EMAIL}:{labels_csv}:{total_words}:{total_chars}"
    verify_hash = hashlib.sha256(verify_input.encode()).hexdigest()[:14]

    print(f"\nLabels: {labels_csv}")
    print(f"Total words: {total_words}")
    print(f"Total chars: {total_chars}")
    print(f"Verify input: {verify_input}")
    print(f"Verify hash: {verify_hash}")
    print(f"\nSubmit: {labels_csv},{total_words},{verify_hash}")


if __name__ == "__main__":
    main()
```

Script output:

```text
Sentence 1: NEGATIVE (words=11, chars=69)
Sentence 2: NEGATIVE (words=13, chars=78)
Sentence 3: POSITIVE (words=13, chars=58)

Labels: NEGATIVE,NEGATIVE,POSITIVE
Total words: 37
Total chars: 205
Verify input: 23f3002663@ds.study.iitm.ac.in:NEGATIVE,NEGATIVE,POSITIVE:37:205
Verify hash: f1c51776a2f83b

Submit: NEGATIVE,NEGATIVE,POSITIVE,37,f1c51776a2f83b
```

---

## Final Submission

```text
NEGATIVE,NEGATIVE,POSITIVE,37,f1c51776a2f83b
```

---

## Conclusion

The first two sentences are negative customer or repair experiences, while the third sentence is positive praise for a movie. The total word count is `37`, and the verification hash is `f1c51776a2f83b`.
