# Sprint 002 Requirements — Foundation Implementation

## Goal
Implement the core infrastructure for the Foundational Data Layer and the initial AI Gateway Proxy with PHI protection.

---

## 1. Cloud Infrastructure (GCP)
- **KMS Setup:** Create a Customer-Managed Encryption Key (CMEK) for PHI protection.
- **BigQuery Datasets:** Initialize `data_raw`, `data_silver`, and `data_gold` datasets with CMEK enabled.
- **GCS Buckets:** Initialize `claims-raw-landing` and `clinical-docs-gold` buckets with CMEK and Uniform Bucket-Level Access.

---

## 2. AI Gateway Proxy Prototype
- **Core Engine:** A Node.js or Python service to intercept calls to Vertex AI (Gemini).
- **DLP Integration:** Implement a "Redaction" pipe that uses GCP Sensitive Data Protection to identify and mask PHI in user prompts.
- **Audit Logging:** Initial implementation of logging requests/responses (masked) to a local file or temporary BigQuery table.

---

## 3. Data Ingestion Scaffold
- **Landing Script:** A Python script to simulate moving a claim file into the `data_raw` GCS bucket.
- **Schema Validation:** Basic check to ensure incoming JSON claims match the expected "Raw" schema.

---

## In Scope
- IaC (Terraform or Deployment Manager) or documented manual steps for GCP resource creation.
- Source code for the AI Gateway Proxy (minimal viable prototype).
- Utility scripts for data movement simulation.

---

## Out of Scope
- Full VPC Service Controls (VPC-SC) enforcement (Discovery done, implementation in Sprint 003).
- Complex RAG chunking logic.
- Production-grade deployment (Kubernetes/Cloud Run).
