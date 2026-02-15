# GA1 — Q8: AI Tool Selection and Architecture Design

## Problem Summary

The client requires a Competitive Intelligence system that:

- Analyzes 71+ documents per week  
- Extracts key information, methodology, and insights  
- Compares documents and identifies trends  
- Handles documents up to 73 pages  
- Produces professional-grade outputs  
- Operates within a $456/month budget  

The system must balance:
- Accuracy
- Context window size
- Cost
- Scalability
- Structured output requirements

---

## Key Design Considerations

1. Large context window requirement for long documents  
2. High analytical accuracy for professional content  
3. Retrieval across multiple documents for trend comparison  
4. Budget constraint ($456/month)  
5. Need for structured JSON outputs  

---

## Tool Selection Strategy

- Use Retrieval-Augmented Generation (RAG) to reduce token costs.
- Use a managed vector database for scalability and operational simplicity.
- Use a high-quality LLM for multi-document synthesis.
- Separate metadata storage from vector storage.
- Add caching to control cost.

---

## Final JSON Submission

```json
{
  "llm": {
    "choice": "GPT-4o",
    "justification": "High accuracy is required for professional competitive-intelligence summaries and trend analysis. GPT-4o provides stronger reasoning consistency and structured output reliability compared to smaller models. Its large context window helps synthesize multiple retrieved document chunks. Higher cost is controlled through retrieval and caching."
  },
  "vectorDB": {
    "choice": "Pinecone",
    "justification": "Managed vector database chosen for scalability, low-latency similarity search, and reduced DevOps overhead. It supports efficient retrieval across 71+ weekly documents and simplifies production deployment compared to self-hosted alternatives."
  },
  "additionalTools": [
    "FastAPI: API layer for ingestion, querying, authentication, and orchestration.",
    "PostgreSQL: Stores document metadata, extracted entities, and generated reports.",
    "LangChain: Manages chunking, embeddings workflow, retrieval pipeline, and structured output control."
  ],
  "architecture": "1) User uploads document via FastAPI ingestion endpoint. Metadata stored in PostgreSQL and raw file saved. 2) Text extracted and chunked into overlapping segments. 3) Embeddings generated for each chunk and stored in Pinecone with metadata. 4) User query received through FastAPI. 5) Query embedded and top-K relevant chunks retrieved from Pinecone. 6) Retrieved context + instructions passed to GPT-4o for structured insight generation. 7) Final JSON output stored in PostgreSQL for auditing and comparison. 8) Response returned to user. Caching applied to embeddings and summaries to control costs.",
  "costEstimate": {
    "total": 456,
    "breakdown": {
      "LLM API calls": 250,
      "Vector DB": 80,
      "Infrastructure hosting": 70,
      "Storage": 30,
      "Other": 26
    }
  },
  "assumptions": "71 documents per week, ~50 pages average, chunk size ~1000 tokens with overlap, 50 queries/day, top-K retrieval=8, 30% cache hit rate.",
  "tradeoffs": [
    "Chose GPT-4o over cheaper models to prioritize accuracy and reduce hallucinations.",
    "Used managed Pinecone instead of self-hosted vector DB to reduce operational complexity.",
    "Implemented RAG instead of sending full documents to the LLM to reduce token cost and improve scalability."
  ],
  "risks": [
    "High token usage exceeding budget during peak demand. Mitigation: caching, top-K limits, query rate control.",
    "Retrieval misses critical information. Mitigation: hybrid retrieval (semantic + keyword filtering) and periodic evaluation."
  ]
}
```

---

## Result
PASS
