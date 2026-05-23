# Validation Plan

## Overview

This plan defines the security and accuracy gates for the EHCCA clinical assistant.

---

## Automated Evaluation Strategy (Sprint 005)

We utilize the **Vertex AI Evaluation API** to measure clinical accuracy and safety autonomously.

### Core Metrics & SLOs

| Metric | Target (SLO) | Method |
|---|---|---|
| **PHI Leakage** | 0.0% | Multi-pass scanning via GCP Sensitive Data Protection (DLP). |
| **Grounding Score** | > 0.90 | Vertex AI Evaluation API checking against `data_gold`. |
| **Faithfulness** | > 0.95 | Measures how accurately the response reflects the source snippets. |
| **System Latency** | P95 < 5.0s | End-to-end request timing from Gateway ingress to egress. |

---

## Observability & Monitoring

Every AI interaction is logged to the **Governance Sink** (BigQuery) for long-term monitoring.

### Monitoring Dimensions

- **Accuracy Drift:** Tracking average Grounding scores over 7-day windows.
- **Latency Bottlenecks:** Comparing DLP vs. Agent vs. Model generation times.
- **HITL Volume:** Monitoring the percentage of requests routed to human review.

## Final System Validation (Production Handover)

| Date | Status | Report |
|---|---|---|
| 23 May 2026 | **PASS** | `reports/system_validation_report.md` |

---

## PHI Detection Strategy

1. **Pre-Processing:** All user prompts are scanned for 50+ InfoTypes (SSN, Name, MRN).
2. **Masking:** Detected PHI is replaced with synthetic tokens before model ingestion.
3. **Post-Processing:** Model completions are scanned for unexpected PHI "recovery" before display.

---

## HITL Trigger Thresholds

- **Grounding Score < 0.85:** Immediate route to clinical reviewer.
- **Safety Violation:** Block response and alert Security Officer.
- **Unknown Clinical Term:** Log for Architect review and add to `DOMAIN.md`.

---

## Validation Checklist

| Area | Validation Method | Status | Notes |
|---|---|---|---|
| **Data Encryption** | Verify KMS key usage on BigQuery datasets. | Pending | Mandatory for PHI compliance. |
| **Network Isolation** | Audit VPC-SC ingress/egress logs. | Pending | |
| **Model Traceability** | Verify every response has a `governance_log_id`. | Pending | |
