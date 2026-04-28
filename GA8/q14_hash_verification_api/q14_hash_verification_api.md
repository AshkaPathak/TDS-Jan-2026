# GA8 — Q14: GCP Cloud Run — Hash Verification API

## Problem Summary
In this question, the task was to deploy a hash verification API that performs string operations and returns cryptographic hash values.

The unique parameters assigned here were:

```text
input_string = "beta-build"
salt = 3218
```

The deployed app had to expose two endpoints:

- `GET /health` returning `{"status":"ok","service":"hash-api"}`
- `POST /hash` accepting JSON with `text` and `salt`

Azure deployment URLs were accepted by the grader, so the service was deployed on Azure App Service.

---

## Required Output Format

The `/hash` endpoint had to return JSON in this structure:

```json
{"sha256":"43943cbe49e0dc13","salted_sha256":"48bbbfeda60561aa","reversed":"dliub-ateb","length":10}
```

The values were computed as:

```text
sha256("beta-build")[:16] = 43943cbe49e0dc13
sha256("beta-build:3218")[:16] = 48bbbfeda60561aa
reverse("beta-build") = dliub-ateb
len("beta-build") = 10
```

---

## Step-by-Step Solution

### Step 1 — Create the FastAPI Application

A FastAPI application was created in `app.py`. It exposes a health endpoint and a hash computation endpoint.

Final `app.py` used:

```python
import hashlib

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(title="GA8 Q14 Hash Verification API")


class HashRequest(BaseModel):
    text: str
    salt: str


@app.get("/health")
async def health():
    return {"status": "ok", "service": "hash-api"}


@app.post("/hash")
async def compute_hash(req: HashRequest):
    text = req.text.strip()
    salt = req.salt.strip()

    if not text:
        return {"error": "text must not be empty"}, 400

    sha = hashlib.sha256(text.encode()).hexdigest()[:16]
    salted_sha = hashlib.sha256(f"{text}:{salt}".encode()).hexdigest()[:16]
    reversed_text = text[::-1]
    length = len(text)

    return {
        "sha256": sha,
        "salted_sha256": salted_sha,
        "reversed": reversed_text,
        "length": length,
    }
```

---

### Step 2 — Add Requirements

A `requirements.txt` file was created so the deployment platform could install the required dependencies.

Contents:

```text
fastapi
uvicorn
pydantic
```

---

### Step 3 — Add Dockerfile

A `Dockerfile` was included for container-based compatibility.

Contents:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

### Step 4 — Test Locally

The app was tested locally with the seeded values.

Request body:

```json
{"text":"beta-build","salt":"3218"}
```

Expected response:

```json
{"sha256":"43943cbe49e0dc13","salted_sha256":"48bbbfeda60561aa","reversed":"dliub-ateb","length":10}
```

---

## Step 5 — Deploy the App

The app was deployed on Azure App Service because the grader accepted Azure deployment URLs.

Deployment details:

- **Platform:** Azure App Service
- **Subscription:** Azure for Students
- **Resource Group:** `tds-ga8-rg`
- **App Service Plan:** `tds-ga8-plan-sea`
- **Region:** Southeast Asia
- **Runtime:** Python 3.11
- **Startup Command:**

```bash
python -m uvicorn app:app --host 0.0.0.0 --port 8000
```

The following app settings were configured:

```text
WEBSITES_PORT=8000
SCM_DO_BUILD_DURING_DEPLOYMENT=true
```

The service was deployed using zip deployment.

---

## Step 6 — Verify the Deployed Endpoints

After deployment, the service was tested using the public Azure URL.

Health endpoint:

```text
https://tds-ga8-q14-hash-ashka.azurewebsites.net/health
```

Response:

```json
{"status":"ok","service":"hash-api"}
```

Hash endpoint:

```bash
curl -X POST https://tds-ga8-q14-hash-ashka.azurewebsites.net/hash \
  -H "Content-Type: application/json" \
  -d '{"text":"beta-build","salt":"3218"}'
```

Response:

```json
{"sha256":"43943cbe49e0dc13","salted_sha256":"48bbbfeda60561aa","reversed":"dliub-ateb","length":10}
```

---

## Final Submitted URL

```text
https://tds-ga8-q14-hash-ashka.azurewebsites.net
```

---

## Conclusion

This question demonstrated how to expose a POST API that performs deterministic string operations and SHA-256 hash verification. The deployed Azure App Service returned the expected values for the seeded input string and salt.
