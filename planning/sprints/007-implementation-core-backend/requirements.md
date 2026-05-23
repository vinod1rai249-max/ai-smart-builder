# Sprint 007 Requirements — Core Backend & Data Pipelines

## Goal
Transition the EHCCA system from discovery scaffolds to a functional, production-ready backend foundation with real data pipelines.

---

## 1. Foundational Data Pipelines
- **Raw-to-Silver Pipeline:** Implement a pipeline (e.g., Cloud Functions or Dataflow) to ingest JSON claims from `data_raw`, redact/mask PHI using DLP, and store the normalized result in `data_silver`.
- **Silver-to-Gold Knowledge Extraction:** Implement logic to extract key clinical snippets from claims and store them in the `data_gold` dataset, optimized for RAG.
- **Metadata Management:** Ensure all data movements are logged with lineage tracking in the `governance_logs` table.

---

## 2. Production AI Gateway
- **API Realization:** Convert the FastAPI prototype into a robust service with production-grade error handling and structured logging.
- **Integration:** Connect the `DLPService` and `VertexService` to real GCP resources (Project ID, KMS Key, Vertex AI Search Engine).
- **RAG Activation:** Replace the simulated retrieval in `ClinicalAgent` with live calls to the Vertex AI Search API.

---

## 3. Security & Governance Implementation
- **CMEK Enforcement:** Verify that all new BigQuery tables and GCS objects are created with the designated KMS key.
- **Audit Sink:** Finalize the schema and implementation of the BigQuery governance sink.
- **HITL Integration:** Ensure the `/generate` endpoint correctly populates the `hitl_queue` table for review.

---

## In Scope
- Implementation of the `Raw-to-Silver` pipeline.
- Productionization of the AI Gateway (FastAPI).
- Live RAG integration in `ClinicalAgent`.
- BigQuery schema updates for `governance_logs` and `hitl_queue`.

---

## Out of Scope
- Frontend UI development (Sprint 008).
- Final VPC-SC perimeter enforcement (Manual step after deployment).
