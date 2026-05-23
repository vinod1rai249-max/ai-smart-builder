# Sprint 001 Blueprint — Discovery & Architecture

## Objective
Create the technical blueprint for the EHCCA Foundation and Gateway layers.

---

## 1. Foundational Data Layer Implementation Plan
1. **GCP Resource Mapping:**
   - Use BigQuery for structured clinical data.
   - Use Cloud Storage for unstructured claim documents.
   - Use Cloud KMS for CMEK management.
2. **Folder/Dataset Structure:**
   - `data/raw/`: Landing zone for incoming claims.
   - `data/silver/`: De-identified and normalized data.
   - `data/gold/`: Ground-truth clinical data for RAG.
3. **Security Constraints:**
   - Define VPC Service Controls (VPC-SC) perimeters.
   - Implement IAM roles with least privilege (e.g., `roles/bigquery.dataViewer` vs `roles/bigquery.admin`).

---

## 2. AI Gateway Evaluation Gates Implementation Plan
1. **Proxy Pattern:**
   - Design a middleware service (Node.js/Python) that wraps Vertex AI API calls.
2. **Evaluation Pipeline:**
   - **Pre-Processing:** Sensitive Data Protection (formerly Cloud DLP) scan on input prompts.
   - **Post-Processing:** Vertex AI Evaluation API for checking grounding and hallucination against `data/gold/`.
3. **HITL Trigger Logic:**
   - Define threshold scores (e.g., Accuracy < 0.85) that automatically route the response to a Human-In-The-Loop review.
4. **Audit Sink:**
   - Route all evaluation metadata to a dedicated BigQuery governance table.

---

## Files to Create/Update
- `docs/ARCHITECTURE.md`: Update with layer-specific diagrams.
- `docs/DATA_MODEL.md`: Define schemas for Raw, Silver, and Gold layers.
- `docs/VALIDATION.md`: Detail the evaluation metrics and thresholds.
- `planning/DECISIONS.md`: Record selection of DLP and KMS strategies.
