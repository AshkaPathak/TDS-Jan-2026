---
title: ga2-q13-fastapi
emoji: 🚀
colorFrom: blue
colorTo: green
sdk: docker
app_port: 7860
pinned: false
---

# GA2 Q13: FastAPI CSV Server

This folder contains the deployable FastAPI service for GA2 Q13. The task is to expose student records from `q-fastapi.csv` through an HTTP endpoint that the course portal can call.

## Method

The service in `main.py`:

1. Starts a FastAPI app.
2. Enables permissive CORS so browser-based graders can call it.
3. Loads `q-fastapi.csv` with `csv.DictReader`.
4. Converts `studentId` values to integers.
5. Exposes `GET /api`.
6. Supports optional filtering with the query parameter `class`, implemented as `class_name: str = Query(None, alias="class")`.
7. Returns the response as a JSON object with a `students` array.

Example response:

```json
{
  "students": [
    {
      "studentId": 1,
      "class": "A"
    }
  ]
}
```

## Files

| File | Purpose |
| --- | --- |
| `main.py` | FastAPI application and CSV lookup logic |
| `q-fastapi.csv` | Source student data |
| `requirements.txt` | Python runtime dependencies |
| `Dockerfile` | Container configuration for deployment |

## Run Locally

```bash
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 7860
```

Example checks:

```bash
curl "http://localhost:7860/api"
curl "http://localhost:7860/api?class=A"
```

## Deployment Intent

The front matter is configured for a Docker-based app on port `7860`, matching Hugging Face Spaces style deployment metadata.
