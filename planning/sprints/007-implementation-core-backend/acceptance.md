# Sprint 007 Acceptance Criteria

This sprint is complete when:

- [ ] **Data Pipelines:**
  - A claim uploaded to `data_raw` GCS bucket is successfully processed, redacted, and appears in the `data_silver` BigQuery table.
  - Governance logs recorded the ingestion event and DLP redaction results.
- [ ] **AI Gateway:**
  - `/generate` endpoint returns a response grounded in real data from Vertex AI Search.
  - Evaluation scores (Grounding, Faithfulness) are real metrics from the Evaluation API.
- [ ] **Security:**
  - No PHI is found in the `data_silver` tables or Gateway logs (verified via a scan).
  - All resources are verified to be encrypted with CMEK.
- [ ] **State:**
  - `planning/STATE.md` reflects the completion of core backend implementation.
