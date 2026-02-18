# GA1 — Q25: AI Cost Optimization for StreamAnalytics

## Problem Summary
StreamAnalytics processes 3,867 moderation requests per day using LLMs.

Given:
- 489 input tokens per request
- 168 output tokens per request
- 3,867 requests/day
- Monthly budget: $1775
- Quality requirement: ≥ 80%

We must:
1. Choose a model meeting quality requirements
2. Design at least 2 optimization strategies
3. Calculate optimized monthly cost
4. Justify trade-offs

---

## Model Selection

Chosen Model: **gpt-4o-mini**

Reason:
- Quality Score: 83% (meets ≥ 80%)
- Lowest cost among qualifying models

Pricing (per 1M tokens):
- Input: $0.16
- Output: $0.54

---

## Baseline Usage Calculation

Requests per month:
3867 × 30 = 116,010 requests

Baseline tokens:
- Input: 116,010 × 489 = 56,728,890 tokens
- Output: 116,010 × 168 = 19,489,680 tokens

Baseline cost:
Input: 56.72889M × 0.16 = $9.08  
Output: 19.48968M × 0.54 = $10.52  

Total Baseline ≈ **$19.60**

(Already far below $1775 budget.)

---

## Optimization Strategies

1. **Caching (40% hit rate)**
   - Only 60% of requests require model call
   - Reduces billed requests significantly

2. **Prompt Compression**
   - Reduce input from 489 → 389 tokens
   - Remove verbose examples and redundant instructions

3. **Output Capping**
   - Restrict explanation to 2–3 sentences
   - Reduce output from 168 → 120 tokens

---

## Optimized Cost Calculation

Billed requests:
116,010 × 0.6 = 69,606

Input tokens:
69,606 × 389 = 27,076,734 (27.076734M)

Output tokens:
69,606 × 120 = 8,352,720 (8.35272M)

Cost:
Input: 27.076734M × 0.16 = $4.33  
Output: 8.35272M × 0.54 = $4.51  

Total Optimized ≈ **$8.84**

---

## Final JSON Submitted

```json
{
  "model": "gpt-4o-mini",
  "monthlyCost": 8.84,
  "strategies": [
    "Cache identical/near-identical moderation results (assume 40% cache hit rate).",
    "Compress prompts by removing redundant examples (~100 token reduction).",
    "Cap explanations to 2–3 sentences to reduce output tokens."
  ],
  "justification": "gpt-4o-mini meets the 80% quality threshold at lowest cost. Even baseline cost is well below budget, and optimizations reduce monthly spend to under $10 while maintaining required accuracy."
}

