# Architecture

## Overview

The Enterprise Healthcare Claims & Clinical Assistant (EHCCA) is a multi-layered AI system hosted on Google Cloud Platform (GCP). It leverages Vertex AI for orchestration and model hosting, wrapped in strict security and governance gates to ensure PHI compliance.

---

## 12-Layer System Components

### 1. Foundation Layer (Data)
- **BigQuery:** Structured storage for claims and clinical data.
- **Cloud Storage (GCS):** Unstructured claim documents and audit logs.
- **KMS (CMEK):** Customer-Managed Encryption Keys for all data at rest.

### 2. AI Gateway Layer (Mediation)
- **Proxy Middleware:** Intercepts Vertex AI calls for safety filtering and PHI scanning.
- **Sensitive Data Protection (DLP):** Real-time PHI detection in prompts/responses.

### 3. Governance Layer (Policy)
- **Audit Sink:** Centralized logging of all model interactions in BigQuery.
- **Policy Enforcement:** Verification of user entitlements against claim sensitivity.

### 4. Multi-Agent Layer (Orchestration)
- **Task Agents:** Specialized agents for claims processing, clinical retrieval, and policy checking.
- **HITL Triggers:** Automated routing to human reviewers for high-risk decisions.

### 5. Security & Isolation
- **VPC Service Controls (VPC-SC):** Network isolation for the data perimeter.
- **Tenant Isolation:** Logical separation of patient data via BigQuery dataset partitioning.

### 6. RAG Layer (Knowledge)
- **Vertex AI Search:** Indexing service for clinical PDF/JSON documents in `data/gold/`.
- **Search Engine Tuning:** Optimized for healthcare-specific terminology.
- **Chunking:** Documents are segmented into 500-token chunks with 50-token overlap to maintain context.
- **Grounding Gate:** Cross-references agent summaries against search results to detect hallucinations.

---

## Data Flow

1. **Ingress:** Claims arrive in `data/raw/` (GCS/BigQuery).
2. **Sanitization:** PHI is identified and tokenized/de-identified into `data/silver/`.
3. **Reasoning:** Agents query `data/gold/` via the AI Gateway.
4. **Validation:** All outputs pass through the Evaluation Gate before reaching the user.

---

## External Services

- **Vertex AI:** Gemini models and evaluation APIs.
- **Cloud Logging/Monitoring:** Observability and alerting.
- **IAM:** Least-privilege access control.

---

## Architecture Decisions

See `planning/DECISIONS.md`.
