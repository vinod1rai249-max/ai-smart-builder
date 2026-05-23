# Sprint 008 Requirements — Frontend & HITL Dashboard

## Goal
Implement the user-facing interfaces for the clinical assistant and the operational dashboard for human review.

---

## 1. Clinical Assistant UI
- **Chat Interface:** A clean, secure chat UI for healthcare professionals to query claims and clinical data.
- **Features:**
  - Input field for natural language prompts.
  - Message history showing user prompts and AI responses.
  - Citations/Evidence display for grounded clinical answers.
  - Status indicators (e.g., "Processing", "Needs Review").

---

## 2. HITL Review Dashboard
- **Review Queue:** A tabular view of interaction IDs flagged for human review (`NEEDS_REVIEW`).
- **Review Detail View:** 
  - Show original (redacted) prompt.
  - Show agent-retrieved data and the flagged AI response.
  - Display the specific `hitl_reason`.
- **Actions:** Buttons for `Approve`, `Edit & Release`, and `Reject`.

---

## 3. Technical Integration
- **API Client:** Use `axios` or `fetch` to communicate with the AI Gateway endpoints:
  - `POST /generate`
  - `GET /hitl/queue`
  - `POST /hitl/resolve`

---

## In Scope
- React/TypeScript component scaffolding.
- State management for chat and review queue.
- Basic styling using Vanilla CSS.

---

## Out of Scope
- User authentication/SSO implementation (Architecture defined, implementation in future sprint).
- Persistent frontend state (Redux/Zustand) unless required for basic functionality.
