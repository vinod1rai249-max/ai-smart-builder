# Sprint 003 Requirements — Multi-Agent Orchestration & Security Hardening

## Goal
Implement a multi-agent system to handle claims and clinical queries, and harden the security perimeter for PHI.

---

## 1. Multi-Agent Orchestration
- **Specialized Agents:**
  - **Claims Agent:** Analyzes claim status, line items, and payment history.
  - **Clinical Agent:** Retrieves clinical context from the "Gold" data layer and provides medical reasoning.
- **Orchestrator:** A central agent (using Gemini 1.5 Pro) that routes user queries to the appropriate specialized agent.
- **Agent Failure Taxonomy:** Define explicit error states (e.g., `DATA_NOT_FOUND`, `POLICY_VIOLATION`, `LOW_CONFIDENCE`).

---

## 2. HITL (Human-In-The-Loop) Triggers
- **Confidence Thresholds:** Implement logic to trigger human review if the model's confidence score is below a certain threshold (e.g., < 0.85).
- **Trigger Events:**
  - High-dollar claims (e.g., > $5,000).
  - Ambiguous clinical reasoning.
  - Potential policy conflicts.

---

## 3. Security Hardening
- **VPC Service Controls (VPC-SC):** Document the configuration for the Service Perimeter protecting BigQuery and GCS.
- **Fine-Grained IAM:** Implement "Least Privilege" IAM policies for the Gateway and Agent service accounts.
- **Tokenization:** Refine the PHI redaction to use reversible tokenization for authorized HITL reviewers.

---

## In Scope
- Source code for Agent classes and Orchestrator.
- HITL trigger logic and routing service.
- VPC-SC configuration documentation.

---

## Out of Scope
- Full implementation of a frontend HITL dashboard.
- Live VPC-SC deployment (documentation only for this phase).
