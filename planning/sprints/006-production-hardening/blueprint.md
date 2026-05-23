# Sprint 006 Blueprint — Production Hardening

## Objective
Lock down the perimeter and define the human operational workflow.

---

## 1. VPC-SC Perimeter Strategy
### Perimeter Layout
- **Protected Resources:** `ehcca-data-project`, `ehcca-ai-project`.
- **Restricted Services:** 
  - `bigquery.googleapis.com`
  - `storage.googleapis.com`
  - `aiplatform.googleapis.com`
  - `dlp.googleapis.com`

### Implementation Steps
1. Create Access Level (IP-based).
2. Create Service Perimeter in "Dry Run" mode.
3. Analyze `dryrun_log` entries in Cloud Logging for 24 hours.
4. Correct any missing Ingress/Egress rules.
5. Move Perimeter to "Enforced" mode.

---

## 2. HITL Dashboard Specification
### Core Components
- **Dashboard API:** Extend `src/gateway/` with `/hitl/queue` and `/hitl/resolve` endpoints.
- **Data Store:** Use a dedicated BigQuery table `ehcca_ops.hitl_queue` to track pending reviews.
- **UI Mockups:** (Documented in `docs/HITL_DASHBOARD_SPEC.md`).

---

## 3. Deployment & Secret Management
1. Move `GOOGLE_CLOUD_PROJECT` and other config to Secret Manager.
2. Implement a `ConfigManager` utility to fetch secrets at startup.
3. Update `src/gateway/main.py` to use `ConfigManager`.

---

## 4. Implementation Steps
1. Create `docs/VPC_SC_GUIDE.md`.
2. Create `docs/HITL_DASHBOARD_SPEC.md`.
3. Update `docs/SECURITY_HARDENING.md` with final IAM and VPC-SC details.
4. Update `planning/STATE.md`.
