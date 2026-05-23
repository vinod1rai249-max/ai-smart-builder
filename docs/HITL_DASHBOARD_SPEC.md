# HITL Dashboard Specification

## Overview
The Human-In-The-Loop (HITL) Dashboard is the operational interface for clinical reviewers to validate AI outputs that trigger safety or accuracy flags.

## 1. Functional Requirements
- **Queue Management:** View a list of pending reviews sorted by priority/risk.
- **Side-by-Side Comparison:** View the original user prompt (redacted), the AI-generated response, and the clinical evidence (grounding context).
- **Decision Workflow:**
  - **Approve:** Direct release of the response.
  - **Edit:** Manual override of the text.
  - **Escalate:** Send to a senior clinical lead.
- **Audit Logging:** Record the `reviewer_id`, `action_taken`, `timestamp`, and `justification_notes`.

## 2. Technical API Specification
### GET `/hitl/queue`
- **Auth:** `ehcca-clinical-reviewer` role required.
- **Returns:** List of interaction IDs with `NEEDS_REVIEW` status.

### POST `/hitl/resolve`
- **Payload:**
  ```json
  {
    "interaction_id": "uuid",
    "action": "APPROVE | EDIT | REJECT",
    "corrected_text": "...",
    "notes": "..."
  }
  ```

## 3. Data Schema
Table: `ehcca_ops.hitl_queue`

| Column | Type | Description |
|---|---|---|
| `interaction_id` | STRING | Foreign key to `interaction_logs`. |
| `status` | STRING | PENDING, RESOLVED, ESCALATED. |
| `reviewer_id` | STRING | Identity of the human reviewer. |
| `decision` | STRING | The final action taken. |
| `notes` | STRING | Rationale for the decision. |

## 4. Security
- **MFA:** Mandatory Multi-Factor Authentication for all dashboard users.
- **Session Limits:** Strict 30-minute session timeout.
- **Data Protection:** PHI must remain redacted in the dashboard view unless the reviewer has explicit `PHI_VIEWER` entitlements.
