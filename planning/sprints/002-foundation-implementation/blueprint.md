# Sprint 002 Blueprint — Foundation Implementation

## Objective
Establish the technical foundation for data storage and secure AI mediation.

---

## 1. Infrastructure Setup (GCP)
### KMS Key
- Location: `us-central1` (or user-preferred).
- Purpose: `encryption/decryption`.
- IAM: Grant `service-XXXXXXXXX@gcp-sa-bigquery.iam.gserviceaccount.com` and GCS service agent `cloud-kms.cryptoKeyEncrypterDecrypter` role.

### BigQuery
- `data_raw`: `default_encryption_configuration` set to the KMS key.
- `data_silver`: `default_encryption_configuration` set to the KMS key.
- `data_gold`: `default_encryption_configuration` set to the KMS key.

### GCS
- `claims-raw-landing`: CMEK enabled, versioning ON.
- `clinical-docs-gold`: CMEK enabled, versioning ON.

---

## 2. AI Gateway Proxy Development
### Stack
- **Language:** Node.js (Express) or Python (FastAPI).
- **Service Account:** Needs `roles/dlp.user` and `roles/aiplatform.user`.

### Logic Flow
1. **Receive Request:** User prompt via REST API.
2. **DLP Pipe:** 
   - Call `inspectContent` to find PHI.
   - Call `deidentifyContent` to mask PHI (e.g., replace with `[PATIENT_NAME]`).
3. **Vertex AI Pipe:** Send masked prompt to Gemini Pro 1.5.
4. **Governance Pipe:** Log masked prompt and response to `governance_logs` table.
5. **Return Response:** Return model output to user.

---

## 3. Implementation Steps
1. Create GCP resources (KMS, BQ, GCS).
2. Scaffold `src/gateway/` with basic server.
3. Implement `src/gateway/dlp_service.py` (or .js).
4. Implement `src/gateway/vertex_service.py` (or .js).
5. Create `scripts/simulate_ingest.py` for testing.
6. Update `planning/STATE.md`.
