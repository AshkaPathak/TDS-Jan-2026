# GA8 — Q10: GCP Cloud Functions — HTTP Triggered Text Processor

## Problem Summary
In this question, the task was to create and deploy an HTTP-triggered text processor. The endpoint had to accept a JSON body containing a text string and return structured analysis results.

The deployed app had to accept:

```json
{"text":"docker-microservice-kubernetes-deployment-devops"}
```

The unique seeded text assigned here was:

```text
docker-microservice-kubernetes-deployment-devops
```

The deployed endpoint had to return:

- `"uppercase"` as the uppercase version of the text
- `"char_count"` as the character count after removing hyphens and spaces
- `"word_count"` as the number of words after splitting on hyphens
- `"sha256"` as the first 16 characters of the SHA-256 hash of the original text
- `"verify"` as the first 12 characters of the SHA-256 hash of the derived summary string

Azure deployment URLs were accepted by the grader, so the service was deployed on Azure App Service.

---

## Required Output Format

The endpoint had to return JSON in exactly this structure:

```json
{"uppercase":"DOCKER-MICROSERVICE-KUBERNETES-DEPLOYMENT-DEVOPS","char_count":44,"word_count":5,"sha256":"5f316a0fc6e85f87","verify":"aa93e3676c9c"}
```

The verification hash was generated from:

```text
upper:DOCKER-MICROSERVICE-KUBERNETES-DEPLOYMENT-DEVOPS:chars:44:words:5
```

---

## Step-by-Step Solution

### Step 1 — Create the FastAPI Application

A FastAPI application was created in `main.py`. It exposes a health check endpoint and text processing endpoints.

The app accepts `POST /` and `POST /text-processor` so the grader can submit either the base Azure URL or the explicit path.

Final `main.py` used:

```python
import hashlib

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(title="GA8 Q10 Text Processor")


class TextRequest(BaseModel):
    text: str


def analyze_text(text: str) -> dict[str, int | str]:
    uppercase = text.upper()
    char_count = len(text.replace("-", "").replace(" ", ""))
    word_count = len(text.replace("-", " ").split())
    sha = hashlib.sha256(text.encode()).hexdigest()[:16]
    verify = hashlib.sha256(
        f"upper:{uppercase}:chars:{char_count}:words:{word_count}".encode()
    ).hexdigest()[:12]

    return {
        "uppercase": uppercase,
        "char_count": char_count,
        "word_count": word_count,
        "sha256": sha,
        "verify": verify,
    }


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/")
@app.post("/text-processor")
async def process_text(req: TextRequest):
    if "text" not in req.model_fields_set:
        raise HTTPException(status_code=400, detail='Missing "text" field in JSON body')
    return analyze_text(req.text)
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

COPY main.py .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

### Step 4 — Test Locally

The text processing logic was tested locally before deployment.

Input:

```text
docker-microservice-kubernetes-deployment-devops
```

Expected values:

```json
{"uppercase":"DOCKER-MICROSERVICE-KUBERNETES-DEPLOYMENT-DEVOPS","char_count":44,"word_count":5,"sha256":"5f316a0fc6e85f87","verify":"aa93e3676c9c"}
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
python -m uvicorn main:app --host 0.0.0.0 --port 8000
```

The following app settings were configured:

```text
WEBSITES_PORT=8000
SCM_DO_BUILD_DURING_DEPLOYMENT=true
```

---

## Deployment Issue Faced and Resolved

The Azure for Students subscription had region restrictions. Based on the previous deployment, `southeastasia` was used because it supported the free Linux App Service plan successfully.

The app was created under the existing free App Service plan and deployed using zip deployment.

---

## Step 6 — Verify the Deployed Endpoint

After deployment, the service was tested using the public Azure URL.

Health endpoint:

```text
https://tds-ga8-q10-text-ashka.azurewebsites.net/health
```

Response:

```json
{"status":"ok"}
```

Base POST endpoint:

```bash
curl -X POST https://tds-ga8-q10-text-ashka.azurewebsites.net/ \
  -H "Content-Type: application/json" \
  -d '{"text":"docker-microservice-kubernetes-deployment-devops"}'
```

Response:

```json
{"uppercase":"DOCKER-MICROSERVICE-KUBERNETES-DEPLOYMENT-DEVOPS","char_count":44,"word_count":5,"sha256":"5f316a0fc6e85f87","verify":"aa93e3676c9c"}
```

Explicit text processor endpoint:

```text
https://tds-ga8-q10-text-ashka.azurewebsites.net/text-processor
```

This endpoint returns the same response for the same JSON input.

---

## Final Submitted URL

```text
https://tds-ga8-q10-text-ashka.azurewebsites.net
```

---

## Conclusion

This question demonstrated how to deploy an HTTP-triggered text processing endpoint and verify deterministic string analysis output. The final Azure App Service deployment satisfied the required behavior and returned the expected hash values for the seeded text.
