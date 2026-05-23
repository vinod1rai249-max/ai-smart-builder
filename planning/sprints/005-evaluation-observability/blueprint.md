# Sprint 005 Blueprint — Evaluation & Observability

## Objective
Measure what matters and log everything for clinical accountability.

---

## 1. Evaluation Architecture
### Evaluation Service (`evaluation_service.py`)
- **API:** `google.cloud.aiplatform.v1.EvaluationServiceClient`.
- **Logic:**
  1. Receive `prompt`, `context`, and `response`.
  2. Call `evaluate_instances` with `PointwiseMetricConfig` (Grounding, Faithfulness).
  3. Return scores and explanations.

### Batch Evaluator (`scripts/run_evaluation.py`)
1. Load `samples/golden_dataset.json`.
2. Run each case through the Gateway `/generate` endpoint.
3. Compare result against "Expected Output" and "Grounding Context".
4. Export results to `reports/eval_results_YYYYMMDD.csv`.

---

## 2. Observability Implementation
### BigQuery Governance Sink
- Table: `ehcca_monitoring.interaction_logs`.
- Schema:
  - `timestamp`: TIMESTAMP
  - `user_id`: STRING
  - `prompt_id`: STRING
  - `agent_type`: STRING (Claims/Clinical)
  - `grounding_score`: FLOAT
  - `safety_status`: STRING (Pass/Fail)
  - `latency_ms`: INTEGER
  - `hitl_triggered`: BOOLEAN

---

## 3. Implementation Steps
1. Create `src/gateway/evaluation_service.py`.
2. Update `src/gateway/main.py` to call evaluation logic post-generation.
3. Create `src/utils/logger.py` for BigQuery logging.
4. Create `samples/golden_dataset.json` with 5 sample clinical cases.
5. Create `scripts/run_evaluation.py` for batch testing.
6. Update `docs/VALIDATION.md` with new automated metrics.
7. Update `planning/STATE.md`.
