# Sprint 008 Blueprint — Frontend & HITL Dashboard

## Objective
Realize the operational interfaces for the EHCCA ecosystem.

---

## 1. Frontend Architecture
- **Tech Stack:** React (TypeScript), CSS Modules.
- **Directory:** `src/ui/`.

### Components
- `App.tsx`: Main router for switching between Assistant and Dashboard views.
- `Assistant/ChatContainer.tsx`: Manages the chat flow.
- `Assistant/Message.tsx`: Renders individual messages and citations.
- `Dashboard/ReviewTable.tsx`: Lists pending reviews.
- `Dashboard/ReviewModal.tsx`: Detail view and action handler.

---

## 2. Integration Plan
- **Mock Mode:** Implement a toggle to use mock data for UI testing without the backend.
- **Backend Mode:** Connect to `http://localhost:8080`.

---

## 3. Implementation Steps
1. Scaffold `src/ui/` directory structure.
2. Implement `api_client.ts` for Gateway communication.
3. Build the `ClinicalAssistant` view.
4. Build the `HitlDashboard` view.
5. Create a `sample_dashboard_data.json` for UI testing.
6. Update `planning/STATE.md`.
