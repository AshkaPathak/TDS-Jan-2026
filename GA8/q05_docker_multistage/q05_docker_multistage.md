# GA8 — Q5: Docker Multi-stage Build — Train and Verify an ML Model

## Problem Summary
In this question, the task was to build a multi-stage Docker image that trains a `GradientBoostingClassifier` on the breast cancer dataset from scikit-learn, prints the model accuracy and a verification hash, and keeps the final image small by copying only the output file into the runtime stage.

The unique parameters assigned were:

- `n_estimators = 70`
- `random_state = 97`
- `test_size = 0.2`

The final answer had to be submitted in the format:

`accuracy_4dp,verify_12char,image_size_mb`

with the Docker image size under 500 MB.

---

## Step-by-Step Solution

### Step 1 — Create `compute.py`

A Python script was created to:

- load the breast cancer dataset
- split the dataset using the given `test_size` and `random_state`
- train a `GradientBoostingClassifier` with the given `n_estimators` and `random_state`
- compute the test accuracy
- generate a SHA256 verification hash using the required string format

Final `compute.py`:

```python
import hashlib
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split

# Your parameters
n_estimators = 70
random_state = 97
test_size = 0.2

# Load dataset
data = load_breast_cancer()

X_train, X_test, y_train, y_test = train_test_split(
    data.data,
    data.target,
    test_size=test_size,
    random_state=random_state
)

clf = GradientBoostingClassifier(
    n_estimators=n_estimators,
    random_state=random_state
)

clf.fit(X_train, y_train)

acc = clf.score(X_test, y_test)
print(f"Accuracy: {acc:.4f}")

# Compute hash
verify_input = f"{n_estimators}:{random_state}:{acc:.6f}"
verify = hashlib.sha256(verify_input.encode()).hexdigest()[:12]
print(f"Verify: {verify}")
```

---

### Step 2 — Create a multi-stage `Dockerfile`

A multi-stage Docker build was used so that the heavy training dependencies such as scikit-learn are installed only in the builder stage. The final runtime image contains only the generated output file, which keeps the image size much smaller.

Final `Dockerfile`:

```dockerfile
# Stage 1
FROM python:3.11-slim AS builder

WORKDIR /app

RUN pip install --no-cache-dir scikit-learn

COPY compute.py .

RUN python compute.py > output.txt

# Stage 2
FROM python:3.11-slim

WORKDIR /app

COPY --from=builder /app/output.txt .

CMD ["cat", "output.txt"]
```

---

### Step 3 — Build the Docker image

The Docker image was built with:

```bash
docker build -t mlops-verify .
```

Initially, Docker failed because the Docker daemon was not running. After starting Docker Desktop, there was another temporary issue while resolving the base image metadata from Docker Hub. This was fixed by pulling the base image manually first:

```bash
docker pull python:3.11-slim
```

After that, the image built successfully.

---

### Step 4 — Run the container

The built container was run using:

```bash
docker run --rm mlops-verify
```

This printed:

```text
Accuracy: 0.9737
Verify: 34ae3617a8d3
```

So the required values were:

- `accuracy_4dp = 0.9737`
- `verify_12char = 34ae3617a8d3`

---

### Step 5 — Measure the final image size

The final Docker image size was checked using:

```bash
docker images mlops-verify --format "{{.Size}}"
```

This returned:

```text
212MB
```

So the image size to submit was:

- `image_size_mb = 212`

This satisfies the requirement that the image size must be less than 500 MB.

---

## Final Submission

```text
0.9737,34ae3617a8d3,212
```

---

## Why the Multi-stage Build Worked

The builder stage installed scikit-learn and executed the training script, generating `output.txt`. The runtime stage did not include scikit-learn or the training script itself. It only copied `output.txt` from the builder stage and printed it when the container ran.

This reduced the final image size significantly while still preserving the required output.

---

## Conclusion

This solution satisfied all requirements:

- trained a `GradientBoostingClassifier` with the assigned parameters
- computed the correct accuracy
- generated the correct 12-character verification hash
- used a proper multi-stage Docker build
- kept the final image size under 500 MB

Final answer:

`0.9737,34ae3617a8d3,212`
