# GA3 — Q17: Extract Structured Data with Schema Validation (1 mark)

## Problem Summary
Extract structured survey response data from unstructured text, define a JSON Schema, validate the extracted data against the schema, and return a single JSON object containing:
- `schema`
- `extracted`
- `validated`
- `confidence`
- `errors`
- `retryCount`
- `model`

The evaluation checks:
- Required fields exist
- Types are correct (numbers must be numbers, not strings)
- Output is valid JSON

---

## Given Sample Text
`Respondent R-123, Age: 35, Satisfaction: 8/10, Feedback: Great service but slow shipping. Likely to recommend: 9/10`

---

## Step 1 — Identify Fields
From the text:
- respondentId = `R-123`
- age = `35`
- satisfaction = `8` (store as number, not `"8/10"`)
- feedback = `Great service but slow shipping.`
- likelyToRecommend = `9` (optional)

---

## Step 2 — Define JSON Schema
Required:
- `respondentId` (string)
- `age` (number)
- `satisfaction` (number)
- `feedback` (string)

Optional:
- `likelyToRecommend` (number)

Also:
- Disallow unexpected fields using `additionalProperties: false`

---

## Step 3 — Validate
Checklist:
- All required fields present ✅
- Numeric fields are numbers (not strings) ✅
- Feedback is non-empty ✅

So:
- `validated = true`
- `errors = []`
- `retryCount = 0`
- High confidence since extraction is explicit in the text

---

## Final JSON (Paste into Portal)
```json
{
  "schema": {
    "type": "object",
    "properties": {
      "respondentId": { "type": "string" },
      "age": { "type": "number" },
      "satisfaction": { "type": "number" },
      "feedback": { "type": "string" },
      "likelyToRecommend": { "type": "number" }
    },
    "required": ["respondentId", "age", "satisfaction", "feedback"],
    "additionalProperties": false
  },
  "extracted": {
    "respondentId": "R-123",
    "age": 35,
    "satisfaction": 8,
    "feedback": "Great service but slow shipping.",
    "likelyToRecommend": 9
  },
  "validated": true,
  "confidence": 0.98,
  "errors": [],
  "retryCount": 0,
  "model": "gpt-5.2"
}
