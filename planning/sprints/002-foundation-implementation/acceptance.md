# Sprint 002 Acceptance Criteria

This sprint is complete when:

- [ ] **Infrastructure:**
  - BigQuery datasets `data_raw`, `data_silver`, `data_gold` exist with CMEK enabled.
  - GCS buckets `claims-raw-landing` and `clinical-docs-gold` exist with CMEK enabled.
- [ ] **AI Gateway Proxy:**
  - Prototype can receive a prompt and successfully redact PHI (using a mock or live DLP call).
  - Prototype can successfully forward a redacted prompt to Vertex AI and return a response.
- [ ] **Data Ingestion:**
  - A script exists that can "upload" a claim file to the landing bucket.
- [ ] **Validation:**
  - Manual test shows that if a user prompt contains a name (e.g., "Tell me about John Doe's claim"), the model only sees a redacted version.
- [ ] **State:**
  - `planning/STATE.md` is updated.
