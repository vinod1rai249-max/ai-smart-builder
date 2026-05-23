# Sprint 003 Acceptance Criteria

This sprint is complete when:

- [ ] **Multi-Agent System:**
  - Orchestrator correctly routes prompts to Claims vs Clinical agents based on intent.
  - Agents can successfully retrieve data from their respective "Silver" or "Gold" layers (simulated or live).
- [ ] **HITL Triggers:**
  - A claim query for an amount > $5,000 triggers a `NEEDS_REVIEW` response.
  - Low confidence clinical responses are flagged for human review.
- [ ] **Security Hardening:**
  - `docs/SECURITY_HARDENING.md` details the VPC-SC perimeter and IAM policy configurations.
- [ ] **State:**
  - `planning/STATE.md` is updated.
