# Sprint 007 Blueprint — Core Backend & Data Pipelines

## Objective
Build the production data engine and secure AI orchestration layer.

---

## 1. Data Pipeline Implementation
- **Source:** `gs://claims-raw-landing-[PROJECT_ID]`
- **Processing:** 
  - Trigger: GCS Finalize Event.
  - Logic: Parse JSON -> DLP `deidentify` -> BigQuery `data_silver.claims` insert.
- **Tools:** Python, `google-cloud-dlp`, `google-cloud-bigquery`.

---

## 2. AI Gateway Productionization
- **Structure:**
  - `src/gateway/main.py`: Update with production logging and health checks.
  - `src/gateway/evaluation_service.py`: Replace mocks with real `aiplatform.v1.EvaluationServiceClient`.
- **Environment Config:** Use a `.env` or Secret Manager to store `PROJECT_ID`, `KMS_KEY_ID`, and `SEARCH_ENGINE_ID`.

---

## 3. Clinical RAG Activation
- **Agent:** `src/agents/clinical_agent.py`.
- **logic:**
  - Call `google.cloud.discoveryengine_v1.SearchServiceClient`.
  - Format snippets into the prompt.
  - Extract citations from `document.struct_data`.

---

## 4. Implementation Steps
1. Initialize the `data_silver` and `data_gold` BigQuery schemas in `scripts/init_db.py`.
2. Implement the `src/pipelines/claim_ingestion.py` service.
3. Update `src/gateway/` services with real GCP SDK calls.
4. Update `src/agents/` with live data retrieval.
5. Create `tests/test_pipelines.py` to verify the end-to-end PHI flow.
6. Update `planning/STATE.md`.
