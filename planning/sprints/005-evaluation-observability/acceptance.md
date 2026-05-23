# Sprint 005 Acceptance Criteria

This sprint is complete when:

- [ ] **Automated Evaluation:**
  - `EvaluationService` successfully retrieves grounding and safety scores from Vertex AI API.
  - A test run of the batch evaluator produces a report showing accuracy against the golden dataset.
- [ ] **Observability:**
  - Every interaction results in a log entry in BigQuery (or a simulated JSON log file for this phase).
  - Latency is recorded for each stage of the request.
- [ ] **Reporting:**
  - `docs/VALIDATION.md` is updated with the new SLOs and automated evaluation strategy.
- [ ] **State:**
  - `planning/STATE.md` is updated.
