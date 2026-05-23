# Domain Context

This file captures the client’s world: terminology, workflows, business rules, roles, and operational context.

---

## Client

Enterprise Healthcare (EHCCA)

---

## Business Goal

Develop a highly secure, clinical assistant for processing healthcare claims and patient data, ensuring strict PHI compliance and governance across 12 core security and AI layers on GCP.

---

## Users / Roles

- **Claims Adjuster:** Reviews automated claim processing results.
- **Clinical Researcher:** Interacts with clinical data assistants.
- **Security/Governance Officer:** Monitors PHI flow and policy enforcement.
- **AI Engineer:** Manages model hosting and evaluation gates.

---

## Current Workflow

1. Manual review of healthcare claims.
2. Siloed clinical data retrieval.
3. Complex, multi-step PHI handling with manual security oversight.
4. Limited automated governance for AI model usage.

---

## Key Terms

| Term | Meaning |
|---|---|
| PHI | Patient Health Information (highly sensitive). |
| Vertex AI | Google Cloud's unified AI platform used for model hosting. |
| RAG | Retrieval-Augmented Generation for grounding clinical data. |
| HITL | Human-In-The-Loop triggers for agent decision-making. |
| SLO | Service Level Objectives for AI observability. |

---

## Business Rules

- **Zero-Trust Security:** Strict tenant isolation and PHI encryption.
- **Governance First:** All model outputs must pass an evaluation gate.
- **PHI Compliance:** No PHI data can be stored outside of the foundational data layer.
- **HITL Requirement:** High-risk clinical decisions must trigger a human review.
