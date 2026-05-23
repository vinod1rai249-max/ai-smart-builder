# Data Model

## Overview

The EHCCA data model follows a medallion architecture, progressing from raw claim ingestion to clinical-ready "Gold" datasets, aligned with HL7 FHIR standards.

---

## Data Stages

### 1. Raw Layer (`data_raw`)
- **Format:** Native JSON/HL7/CSV as received.
- **Retention:** Permanent for audit/traceability.
- **Sensitivity:** High PHI.

### 2. Silver Layer (`data_silver`)
- **Format:** Normalized Relational/JSON.
- **Focus:** De-identification, cleaning, and deduplication.
- **Entity:** `Patient`, `Claim`, `Encounter`.

### 3. Gold Layer (`data_gold`)
- **Format:** Optimized for RAG and Analytics.
- **Focus:** Knowledge-grounding snippets and clinical summaries.
- **Entity:** `ClinicalSummary`, `KnowledgeSnippet`.

---

## Core Entities (FHIR-Aligned)

| Entity | Purpose | Key Attributes |
|---|---|---|
| **Patient** | Identity and clinical history. | `patient_id` (CMEK encrypted), `gender`, `birthDate`. |
| **Claim** | Billing and insurance details. | `claim_id`, `status`, `type`, `priority`, `total`. |
| **Encounter** | Clinical interaction records. | `encounter_id`, `type`, `subject_id`, `period`. |

---

## Relationships

- **Patient (1) -> Claim (N):** A patient can have multiple claims.
- **Patient (1) -> Encounter (N):** A patient has multiple clinical interactions.
- **Encounter (1) -> ClinicalSummary (1):** Summaries are generated per encounter for the Gold layer.
