# 🛡️ EHCCA Project: Beginner's User Guide
**Enterprise Healthcare Claims & Clinical Assistant**

---

## 🌟 1. Introduction: What is EHCCA?
EHCCA is a highly secure AI system built for the healthcare industry. It allows doctors and insurance adjusters to talk to their data (claims, medical records) using AI, while keeping every piece of sensitive patient information (PHI) inside a virtual vault.

### The EHCCA "Vault" Model
*   **Privacy First:** It hides names and Social Security Numbers automatically.
*   **Fact-Checked:** It only answers using real clinical documents.
*   **Human Safety Valve:** If the AI is confused, it pauses and asks a human expert for help.

---

## 🌊 2. How the Data Flows (Visual)

We use a **"Water Filter"** approach called Medallion Architecture. Data gets cleaner and safer at every step.

```mermaid
graph TD
    subgraph "Untrusted Zone (Raw)"
        A[📄 Raw Claims & Invoices]
    end

    subgraph "Secure GCP Perimeter (The Vault)"
        A -->|DLP Privacy Filter| B(🛡️ Silver Layer: Redacted Data)
        B -->|Expert Analysis| C{✨ Gold Layer: Verified Facts}
    end

    subgraph "User Interface"
        C -->|RAG| D[🤖 Clinical Assistant]
        D -->|Risky/Complex Query| E[🚩 Human Review Dashboard]
    end

    style A fill:#ffcccc,stroke:#333
    style B fill:#e6e6e6,stroke:#333
    style C fill:#fff2cc,stroke:#333
    style D fill:#d9ead3,stroke:#333
    style E fill:#fff4dd,stroke:#d4a017
```

---

## 🛡️ 3. How a Request is Secured (Step-by-Step)

Every time you ask the AI a question, it passes through these **5 Security Gates**:

```mermaid
sequenceDiagram
    autonumber
    actor User as Adjuster / Doctor
    participant Gateway as AI Gateway
    participant DLP as Privacy Filter
    participant RAG as Knowledge Base
    participant Gemini as AI Brain
    participant Eval as Accuracy Checker

    User->>Gateway: "Tell me about John Doe's claim"
    Gateway->>DLP: Hide sensitive names
    DLP-->>Gateway: Redacted: "[REDACTED] Claim Query"
    Gateway->>RAG: Find Facts in Clinical Records
    RAG-->>Gateway: Found: Claim CLM-123 ($1,200)
    Gateway->>Gemini: Summarize the facts
    Gateway->>Eval: Is this answer 100% accurate?
    
    alt If Accuracy is High (>90%)
        Gateway-->>User: "The claim for [REDACTED] is $1,200"
    else If Accuracy is Low
        Gateway-->>User: "🚩 Routing to Human Review for Safety"
    end
```

---

## 🚀 4. Quick Start: Testing the System

You can test the whole system with three simple commands in your terminal:

### Step 1: Turn on the "Brain" (The Gateway)
```bash
python -m src.gateway.main
```
*Wait until you see: "Uvicorn running on http://0.0.0.0:8080"*

### Step 2: Upload your first test Data
This sends a "Fake" claim into the secure vault.
```bash
python scripts/simulate_ingest.py --project [ID] --bucket [NAME] --file samples/sample_claim.json
```

### Step 3: Run the "Final Exam"
This runs 5 automated scenarios (including privacy leaks) to see if the system stops them.
```bash
python scripts/run_evaluation.py
```
*Look for a file called `evaluation_report.csv` in your project folder!*

---

## 📄 5. How to Save this Guide as a PDF

To create a professional PDF version of this guide:

1.  **Open the file:** `docs/EHCCA_USER_GUIDE.md` in **VS Code**.
2.  **Install the Tool:** In the Extensions view (`Ctrl+Shift+X`), search for **"Markdown PDF"** (by yyzhang) and install it.
3.  **Export:**
    *   Right-click anywhere in the guide.
    *   Select **"Markdown PDF: Export (pdf)"**.
4.  **Done!** Your PDF will appear in the `docs/` folder instantly.

---
**Status:** Production Ready  
**Created:** 23 May 2026  
**Methodology:** 120x Architect/Builder
