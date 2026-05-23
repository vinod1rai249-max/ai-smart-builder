# Sprint 004 Acceptance Criteria

This sprint is complete when:

- [ ] **Clinical RAG:**
  - Clinical Agent can retrieve relevant snippets from a simulated or live RAG store.
  - Responses include "Sources" or citations from the retrieved text.
- [ ] **Failure Taxonomy:**
  - Standardized error codes are returned for common failure modes (Data missing, Policy, etc.).
  - Orchestrator gracefully handles `error` status from any sub-agent.
- [ ] **Reliability:**
  - System logs "Latency" for retrieval vs generation phases.
- [ ] **State:**
  - `planning/STATE.md` is updated.
