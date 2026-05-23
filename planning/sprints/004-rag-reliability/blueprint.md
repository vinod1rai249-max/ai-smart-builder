# Sprint 004 Blueprint — RAG Implementation & Failure Taxonomy

## Objective
Ground clinical reasoning in data and handle errors predictably.

---

## 1. Clinical RAG Architecture
### Vertex AI Search Setup
- **Data Store:** Connected to `gs://clinical-docs-gold-[PROJECT_ID]`.
- **Search Engine:** Configured with "Healthcare" industry tuning if available.

### Retrieval Flow
1. **Query Expansion:** LLM rewrites query for better retrieval performance.
2. **Search:** Call Vertex AI Search API to get top 5 snippets.
3. **Rerank:** (Optional for prototype) Sort snippets by relevance.
4. **Augment:** Inject snippets into the system prompt: "Answer using ONLY the following context...".

---

## 2. Failure Taxonomy Implementation
### Standard Error Response
```json
{
  "status": "error",
  "error_code": "LOW_GROUNDING_CONFIDENCE",
  "message": "I found some clinical data, but it's not specific enough to confirm this diagnosis.",
  "agent": "ClinicalAgent",
  "retryable": false
}
```

### Middleware Logic
- Wrap agent execution in a try-except block that maps internal exceptions to the Failure Taxonomy.
- Integrate with `check_hitl_triggers()` in the Gateway to ensure errors requiring human eyes are routed correctly.

---

## 3. Implementation Steps
1. Update `src/agents/clinical_agent.py` with RAG logic.
2. Create `src/utils/errors.py` to define the Failure Taxonomy.
3. Refine `src/agents/orchestrator.py` to handle agent errors.
4. Add RAG documentation to `docs/ARCHITECTURE.md`.
5. Update `planning/STATE.md`.
