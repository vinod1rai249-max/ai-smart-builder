# Sprint 006 Requirements — Production Hardening

## Goal
Secure the EHCCA system for enterprise production by enforcing network perimeters and finalizing the operational interface for human review.

---

## 1. VPC Service Controls (VPC-SC) Enforcement
- **Service Perimeter:** Implement a full dry-run and then enforced perimeter around all PHI-handling services (BigQuery, GCS, Vertex AI, DLP).
- **Ingress/Egress Rules:** Define strict rules for cross-project communication (e.g., between the AI Gateway and the Data Foundation projects).
- **Access Levels:** Restrict admin access to specific corporate IP ranges and identity groups.

---

## 2. HITL Dashboard Requirements
- **Review Queue:** A dedicated interface for human reviewers to see all `NEEDS_REVIEW` requests.
- **Workflow Actions:**
  - **Approve:** Forward the AI response to the user.
  - **Edit:** Manually correct the AI response before sending.
  - **Reject:** Inform the user that the request cannot be fulfilled.
- **Audit Logging:** Every human action must be logged with the reviewer's identity and the reason for the correction.

---

## 3. Production Deployment Checklist
- **Secrets Management:** Ensure all API keys and credentials move to Google Cloud Secret Manager.
- **Capacity Planning:** Set initial quotas for Vertex AI and DLP API usage.
- **Backup & Disaster Recovery:** Document the cross-region backup strategy for BigQuery datasets.

---

## In Scope
- `docs/VPC_SC_GUIDE.md`: Technical implementation guide for the perimeter.
- `docs/HITL_DASHBOARD_SPEC.md`: Functional and technical requirements for the dashboard.
- Finalized IAM role definitions in `docs/SECURITY_HARDENING.md`.

---

## Out of Scope
- Building the actual HITL dashboard frontend.
- Multi-region active-active deployment.
