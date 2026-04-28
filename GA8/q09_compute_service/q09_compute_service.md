# GA8 — Q9: GCP Cloud Run — Deploy a Compute Service

## Problem Summary
In this question, the task was to deploy a containerized compute API that performs arithmetic operations and returns a verification hash. The deployed app had to expose two endpoints:

- `GET /health` returning `{"status":"ok"}`
- `POST /compute` accepting JSON with `a` and `b`, and returning:
  - `"sum"` as an integer
  - `"product"` as an integer
  - `"verify"` as the first 10 characters of a SHA-256 hash

The unique parameters assigned here were:

- `A = 15`
- `B = 15`

The deployed API had to be publicly accessible on an accepted cloud platform. Azure deployment URLs were accepted by the grader.

---

## Required Output Format

The `/compute` endpoint had to return JSON in exactly this structure:

```json
{"sum":30,"product":225,"verify":"89efa83eb3"}
```

The verification hash was generated from:

```text
sum:30:product:225
```

---

## Step-by-Step Solution

### Step 1 — Create the FastAPI Application

A FastAPI application was created in `main.py`. It exposes a health check endpoint and a compute endpoint.

Final `main.py` used:

```python
import hashlib

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(title="GA8 Q9 Compute Service")


class ComputeRequest(BaseModel):
    a: int
    b: int


@app.get("/")
async def root():
    return {
        "message": "GA8 Q9 Compute Service is running",
        "endpoints": ["/health", "/compute"],
    }


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/compute")
async def compute(req: ComputeRequest):
    total = req.a + req.b
    product = req.a * req.b

    verify = hashlib.sha256(
        f"sum:{total}:product:{product}".encode()
    ).hexdigest()[:10]

    return {
        "sum": total,
        "product": product,
        "verify": verify,
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

A `Dockerfile` was included for container-based deployment.

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

The app was tested locally before deployment.

Health check:

```bash
curl http://127.0.0.1:8009/health
```

Expected response:

```json
{"status":"ok"}
```

Compute test:

```bash
curl -X POST http://127.0.0.1:8009/compute \
  -H "Content-Type: application/json" \
  -d '{"a":15,"b":15}'
```

Expected response:

```json
{"sum":30,"product":225,"verify":"89efa83eb3"}
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

The first deployment attempt used `centralindia`, but Azure App Service could not create a free Linux plan in that region for this subscription. An attempt with `eastus` was blocked by the Azure for Students subscription policy.

Resolution:

- Created the free Linux App Service plan in `southeastasia`
- Created the web app on that plan
- Set the FastAPI startup command manually
- Uploaded the application as a zip deployment

This successfully deployed the app.

---

## Step 6 — Verify the Deployed Endpoints

After deployment, the service was tested using the public Azure URL.

Health endpoint:

```text
https://tds-ga8-q09-compute-ashka.azurewebsites.net/health
```

Response:

```json
{"status":"ok"}
```

Compute endpoint:

```bash
curl -X POST https://tds-ga8-q09-compute-ashka.azurewebsites.net/compute \
  -H "Content-Type: application/json" \
  -d '{"a":15,"b":15}'
```

Response:

```json
{"sum":30,"product":225,"verify":"89efa83eb3"}
```

---

## Final Submitted URL

```text
https://tds-ga8-q09-compute-ashka.azurewebsites.net
```

---

## Conclusion

This question demonstrated how to deploy a FastAPI compute API to a public cloud platform and verify it using deterministic arithmetic output plus a hash. The final Azure App Service deployment satisfied the required `/health` and `/compute` endpoints.
