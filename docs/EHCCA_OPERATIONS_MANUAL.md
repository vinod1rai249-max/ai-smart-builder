# EHCCA Operations Manual: A Beginner's Guide
**Enterprise Healthcare Claims & Clinical Assistant**

This manual provides a step-by-step guide on how to set up, operate, and maintain the EHCCA system using the **120x Architect/Builder Methodology**.

---

## 1. The 120x Philosophy
EHCCA was built using a separation of concerns. This ensures that security decisions are made before a single line of code is written.

### The Architect/Builder Lifecycle
```mermaid
graph LR
    A[Architect] -->|Creates Blueprint| B(Folder Handoff)
    B -->|Implementation| C[Builder]
    C -->|Validation| D{Production Ready}
    D -->|New Requirements| A
```

---

## 2. System Architecture
EHCCA protects Patient Health Information (PHI) by filtering it through multiple layers.

### Data Medallion Flow
```mermaid
graph TD
    subgraph "Untrusted Zone"
    RAW[Raw Claims / PDFs]
    end

    subgraph "Secure GCP Environment (VPC-SC)"
    SILVER[Silver Layer: Redacted Data]
    GOLD[Gold Layer: Verified Clinical Knowledge]
    end

    RAW -->|DLP Redaction Pipeline| SILVER
    SILVER -->|Clinical Extraction| GOLD
    GOLD -->|Vertex AI Search| Assistant[Clinical Assistant UI]
```

---

## 3. Getting Started (Setup)

### Step 1: GCP Configuration
You must have a Google Cloud Project with the following enabled:
*   **Vertex AI API**
*   **Sensitive Data Protection (DLP) API**
*   **BigQuery & Cloud Storage**

### Step 2: Environment Setup
1.  Install Python 3.9+
2.  Set your environment variables in a `.env` file:
    ```text
    GOOGLE_CLOUD_PROJECT=your-project-id
    KMS_KEY_ID=projects/your-project/locations/us-central1/keyrings/ehcca-keyring/cryptoKeys/ehcca-phi-key
    SEARCH_ENGINE_ID=your-search-engine-id
    ```

---

## 4. Operational Workflows

### How a User Request is Protected
When a user asks a question, the **AI Gateway** acts as a security proxy.

```mermaid
sequenceDiagram
    participant User as User (Adjuster/Doctor)
    participant GW as AI Gateway (FastAPI)
    participant DLP as Privacy Filter (DLP)
    participant RAG as Clinical Knowledge (Vertex Search)
    participant LLM as Vertex AI (Gemini)

    User->>GW: "Tell me about John Doe's claim"
    GW->>DLP: Remove PHI
    DLP-->>GW: "Tell me about [PERSON_NAME]'s claim"
    GW->>RAG: Retrieve verified clinical snippets
    RAG-->>GW: [Clinical Evidence]
    GW->>LLM: Generate grounded response
    LLM-->>GW: "The claim for [PERSON_NAME] is..."
    GW->>User: Secure, Grounded Answer
```

---

## 5. Testing & Validation

### End-to-End Evaluation
Run the following command to verify the system against the **Golden Dataset**:
```bash
python scripts/run_evaluation.py
```
This script checks:
1.  **PHI Redaction:** Does the system successfully hide names?
2.  **Grounding:** Is the answer based on real data?
3.  **HITL Triggers:** Do risky answers go to the human dashboard?

---

## 6. Human-In-The-Loop (HITL) Dashboard
If the AI is unsure, it triggers a human review. 

**Reviewer Actions:**
*   **Approve:** Release the AI response to the user.
*   **Edit:** Correct clinical errors before release.
*   **Reject:** Block the response for safety reasons.

---

## 7. Converting to PDF
To share this manual as a PDF:
1.  Open **VS Code**.
2.  Install the **"Markdown PDF"** extension by yyzhang.
3.  Open `docs/EHCCA_OPERATIONS_MANUAL.md`.
4.  Press `Ctrl+Shift+P` and type **"Markdown PDF: Export (pdf)"**.

---
*For technical implementation details, refer to `docs/ARCHITECTURE.md`.*
