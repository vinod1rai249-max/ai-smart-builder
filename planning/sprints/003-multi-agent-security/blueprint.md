# Sprint 003 Blueprint — Multi-Agent Orchestration & Security Hardening

## Objective
Build a robust, multi-agent reasoning system with built-in safety valves.

---

## 1. Agent Architecture
### Orchestrator Logic
1. **Classify:** Determine if the intent is `CLAIM_QUERY`, `CLINICAL_QUERY`, or `GENERAL`.
2. **Route:** Dispatch to the specialized agent.
3. **Synthesize:** Combine agent outputs into a final clinical/claims response.

### Specialized Agents
- **ClaimsAgent:** Uses BigQuery tool-calling to query `data_silver.claims`.
- **ClinicalAgent:** Uses Vertex AI Search (RAG) to query `data_gold.clinical_docs`.

---

## 2. HITL Trigger Implementation
### Logic Flow
- `evaluate_confidence()`: Checks the log-likelihood or a specific confidence field in the model response.
- `check_risk_factors()`: Checks claim amount and patient sensitivity.
- `route_to_hitl()`: If triggers fire, return a `NEEDS_REVIEW` status and log the payload to `planning/hitl_queue.json`.

---

## 3. Security Hardening Implementation
### VPC-SC Perimeter
- Service Perimeter Name: `ehcca-phi-perimeter`.
- Protected Services: `bigquery.googleapis.com`, `storage.googleapis.com`.
- Access Levels: Restrict to corporate CIDR or specific Identity.

### IAM Refinement
- Gateway Service Account: `ehcca-gateway@[PROJECT_ID].iam.gserviceaccount.com`.
- Roles: `roles/aiplatform.user`, `roles/dlp.user`, `roles/bigquery.dataViewer` (limited to specific datasets).

---

## 4. Implementation Steps
1. Scaffold `src/agents/` with `base_agent.py`, `claims_agent.py`, and `clinical_agent.py`.
2. Implement `orchestrator.py` logic.
3. Add HITL logic to `src/gateway/main.py`.
4. Create `docs/SECURITY_HARDENING.md` for VPC-SC and IAM docs.
5. Update `planning/STATE.md`.
