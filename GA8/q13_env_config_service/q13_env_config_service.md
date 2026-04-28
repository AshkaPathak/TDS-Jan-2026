# GA8 — Q13: GCP Cloud Run — Environment Variable Configuration

## Problem Summary
In this question, the task was to deploy a service with environment variables configured at deployment time. The service had to expose its runtime configuration through a `/config` endpoint.

The required environment variables were:

```text
THEME_COLOR=slate
APP_MODE=staging
BUILD_NUMBER=287
```

The deployed app had to expose two endpoints:

- `GET /health` returning `{"status":"ok"}`
- `GET /config` returning the environment variable values and a verification hash

Azure deployment URLs were accepted by the grader, so the service was deployed on Azure App Service.

---

## Required Output Format

The `/config` endpoint had to return JSON in this structure:

```json
{"theme_color":"slate","app_mode":"staging","build_number":"287","config_hash":"0744efc1a8e8"}
```

The verification hash was generated from:

```text
slate:staging:287
```

SHA-256 hash, first 12 hex characters:

```text
0744efc1a8e8
```

---

## Step-by-Step Solution

### Step 1 — Create the FastAPI Application

A FastAPI application was created in `app.py`. It reads the required values from environment variables and computes the configuration hash.

Final `app.py` used:

```python
import hashlib
import os

from fastapi import FastAPI


app = FastAPI(title="GA8 Q13 Environment Configuration Service")


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/config")
async def config():
    theme = os.environ.get("THEME_COLOR", "NOT_SET")
    mode = os.environ.get("APP_MODE", "NOT_SET")
    build = os.environ.get("BUILD_NUMBER", "NOT_SET")
    config_str = f"{theme}:{mode}:{build}"
    config_hash = hashlib.sha256(config_str.encode()).hexdigest()[:12]
    return {
        "theme_color": theme,
        "app_mode": mode,
        "build_number": build,
        "config_hash": config_hash,
    }
```

---

### Step 2 — Add Requirements

A `requirements.txt` file was created so the deployment platform could install the required dependencies.

Contents:

```text
fastapi
uvicorn
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

The app was tested locally with the required environment variables.

Environment values:

```text
THEME_COLOR=slate
APP_MODE=staging
BUILD_NUMBER=287
```

Expected `/config` response:

```json
{"theme_color":"slate","app_mode":"staging","build_number":"287","config_hash":"0744efc1a8e8"}
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
THEME_COLOR=slate
APP_MODE=staging
BUILD_NUMBER=287
```

The service was deployed using zip deployment.

---

## Step 6 — Verify the Deployed Endpoints

After deployment, the service was tested using the public Azure URL.

Health endpoint:

```text
https://tds-ga8-q13-env-ashka.azurewebsites.net/health
```

Response:

```json
{"status":"ok"}
```

Config endpoint:

```text
https://tds-ga8-q13-env-ashka.azurewebsites.net/config
```

Response:

```json
{"theme_color":"slate","app_mode":"staging","build_number":"287","config_hash":"0744efc1a8e8"}
```

---

## Final Submitted URL

```text
https://tds-ga8-q13-env-ashka.azurewebsites.net
```

---

## Conclusion

This question demonstrated how to configure runtime environment variables for a deployed service and verify them through an HTTP endpoint. The Azure App Service deployment returned the required configuration values and the expected hash.
