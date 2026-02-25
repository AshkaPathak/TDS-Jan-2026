# GA3 – Q2: LLM Structured Output – FastAPI Sentiment Analysis

## Objective
Build a FastAPI endpoint that:
- Accepts a comment via POST `/comment`
- Uses GPT-4.1-mini
- Enforces structured JSON output using schema
- Returns consistent sentiment analysis

---

## Endpoint Details

### URL
```
https://tds-jan-2026-ga3-q2.onrender.com/comment
```

### Method
POST

### Request Format
```json
{
  "comment": "This product is amazing!"
}
```

### Response Format
```json
{
  "sentiment": "positive",
  "rating": 5
}
```

---

## Structured Output Schema

The model is forced to return:

- `sentiment` → string ("positive", "negative", "neutral")
- `rating` → integer (1–5)

Schema enforcement ensures:
- No parsing required
- Consistent JSON structure
- Production-safe output

---

## Tech Stack

- FastAPI
- OpenAI Python SDK
- GPT-4.1-mini
- AI Pipe API
- Render deployment
- CORS middleware enabled

---

## Deployment Steps

### 1. Local Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Run Locally

```bash
uvicorn main:app --reload
```

### 3. Deploy to Render

- Root directory:
  ```
  GA3/q02_llm_structured_output_fastapi_sentiment
  ```
- Build command:
  ```
  pip install -r requirements.txt
  ```
- Start command:
  ```
  uvicorn main:app --host 0.0.0.0 --port $PORT
  ```
- Add environment variable:
  ```
  OPENAI_API_KEY=<AI Pipe Token>
  ```

---

## Testing

Example:

```bash
curl -X POST https://tds-jan-2026-ga3-q2.onrender.com/comment \
  -H "Content-Type: application/json" \
  -d '{"comment":"This is amazing!"}'
```

Response:

```json
{"sentiment":"positive","rating":5}
```

---

## Notes

- CORS enabled to support browser-based grading
- Structured outputs ensure exact match of fields
- Error handling implemented for API failures

---

## Status

✅ Successfully deployed  
✅ Returns structured JSON  
✅ Passed portal validation  
