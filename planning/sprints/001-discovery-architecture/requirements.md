# Sprint 001 Requirements — Discovery & Architecture

## Goal
Define the architecture and standards for the Foundational Data Layer and AI Gateway Evaluation Gates to ensure PHI security and model reliability.

---

## 1. Foundational Data Layer Scaffold
**Objective:** Establish a secure, scalable, and isolated data foundation for PHI.

### Key Requirements
- **PHI Isolation:** Separate datasets for Raw, Silver (cleansed), and Gold (clinical-ready) data using BigQuery and Cloud Storage.
- **Encryption:** Mandatory use of Customer-Managed Encryption Keys (CMEK) via Google KMS.
- **Tenant Isolation:** Logical or physical isolation of patient data to prevent cross-tenant leakage.
- **Schema Management:** Automated schema validation and versioning for healthcare data formats (HL7, FHIR-like structures).

---

## 2. AI Gateway Evaluation Gates
**Objective:** Intercept and validate all AI model interactions for safety and accuracy.

### Key Requirements
- **PHI Leakage Detection:** Real-time scanning of prompts and completions for PHI before they leave/enter the clinical assistant.
- **Clinical Accuracy Gate:** Cross-reference model outputs against the "Gold" clinical data layer.
- **Safety & Bias Check:** Utilize Vertex AI Safety Filters and custom evaluation metrics.
- **Governance Logging:** Record all gate results (Pass/Fail/Bypass) in a secure audit log for compliance review.

---

## In Scope
- Architecture diagrams for Data Layer and AI Gateway.
- Schema definitions for core clinical entities.
- Evaluation metric definitions (Safety, Accuracy, Grounding).
- Infrastructure-as-Code (IaC) design patterns for GCP.

---

## Out of Scope
- Implementation of the actual data pipelines.
- Training or fine-tuning of LLMs.
- Development of the front-end clinical assistant.
