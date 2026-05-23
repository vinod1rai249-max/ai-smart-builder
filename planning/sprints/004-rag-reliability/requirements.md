# Sprint 004 Requirements — RAG Implementation & Failure Taxonomy

## Goal
Enhance the Clinical Agent with RAG capabilities and ensure production readiness through a robust failure taxonomy.

---

## 1. RAG Implementation (Clinical Agent)
- **Vertex AI Search Integration:** Connect the Clinical Agent to the "Gold" data layer using Vertex AI Search (formerly Gen AI App Builder).
- **Chunking Strategy:** Implement a strategy for clinical document chunking (e.g., 500 tokens with 50-token overlap) in the data ingestion pipeline.
- **Grounding Validation:** Ensure every clinical response cites a source from the RAG store.
- **Reranking:** Integrate a reranking step to improve relevance of retrieved snippets.

---

## 2. Agent Failure Taxonomy
- **Explicit Error States:** Implement a standardized error object returned by all agents.
- **Taxonomy Categories:**
  - `DATA_SOURCE_UNAVAILABLE`: Data layer or API is down.
  - `LOW_GROUNDING_CONFIDENCE`: Retrieved context doesn't adequately support the answer.
  - `POLICY_VIOLATION`: Query or response violates healthcare safety/privacy guidelines.
  - `AMBIGUOUS_QUERY`: Intent cannot be clearly determined by the orchestrator.
  - `MODEL_TIMEOUT`: Vertex AI call exceeded the latency threshold.

---

## 3. Production Readiness
- **Latency Monitoring:** Add timing instrumentation to RAG retrieval and model generation.
- **Fallback Logic:** Define default "safe" responses for each category in the failure taxonomy.

---

## In Scope
- RAG retrieval logic in `ClinicalAgent`.
- Error handling middleware/utils for the Failure Taxonomy.
- Updated `docs/ARCHITECTURE.md` with RAG details.

---

## Out of Scope
- Full-scale data migration to the Gold layer.
- Advanced multi-modal RAG (images/scans).
