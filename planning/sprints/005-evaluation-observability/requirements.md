# Sprint 005 Requirements — Evaluation & Observability

## Goal
Establish automated evaluation pipelines and observability instrumentation to ensure the EHCCA system meets clinical safety and performance standards.

---

## 1. Automated Evaluation (Vertex AI)
- **Evaluation Pipeline:** Implement a service to call the Vertex AI Evaluation API for assessing model completions.
- **Key Metrics:**
  - **Grounding Score:** How well the response is supported by the "Gold" context.
  - **Faithfulness:** Does the response accurately reflect the source data without hallucinations?
  - **Safety Violation Rate:** Detection of harmful or biased content.
- **Batch Evaluation:** Create a script to run evaluations against a "Golden Dataset" of 50+ known clinical scenarios.

---

## 2. Observability & Monitoring
- **Governance Sink:** Implement a logger that writes interaction metadata (including evaluation scores) to the `governance_logs` BigQuery table.
- **Latency Tracking:** Capture and log latency for each layer: DLP Redaction, Agent Retrieval, and Model Generation.
- **SLO Definitions:** Define initial Service Level Objectives (SLOs) for:
  - Availability (99.9%).
  - Grounding Score (> 0.90).
  - P95 Latency (< 5s).

---

## 3. Validation Reporting
- **Automated Reports:** Generate a summary of evaluation results after each batch run.
- **HITL Feedback Loop:** Log human review corrections back into the evaluation dataset to improve model grounding over time.

---

## In Scope
- `EvaluationService` implementation in `src/gateway/`.
- BigQuery logging logic for interaction metadata.
- Golden Dataset sample in `samples/golden_dataset.json`.

---

## Out of Scope
- Full implementation of a real-time Grafana/Cloud Monitoring dashboard.
- Advanced drift detection for model performance.
