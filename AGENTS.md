# AGENTS.md

## Project

**Name:** EHCCA (Enterprise Healthcare Claims & Clinical Assistant)  
**Client:** Enterprise Healthcare  
**Description:** A PHI-compliant clinical assistant using 12 security and AI layers on GCP.  
**Tech stack:** GCP, Vertex AI, Node.js/Python, Multi-Agent Framework  
**Created:** 23 May 2026

---

## Operating Model

This project uses the 120x Architect / Builder methodology.

The handoff is a folder, not a conversation.

The Builder must read project files before making changes and must build to the approved sprint blueprint.

---

## First Files to Read

Read these in order at the start of every session:

1. `AGENTS.md`
2. `planning/STATE.md`
3. `planning/DECISIONS.md`
4. `planning/DOMAIN.md`
5. Active sprint files under `planning/sprints/`
6. Relevant docs under `docs/`

---

## Project Structure

```text
.
├── docs/                  # Durable technical documentation
├── planning/              # Project planning, domain context, decisions, risks, sprints
├── src/                   # Production application code
├── tests/                 # Automated tests
├── scripts/               # One-off and repeatable utility scripts
├── samples/               # Local sample files; usually gitignored if sensitive
└── references/            # Reference material used by the Architect/Builder
```

---

## Builder Rules

- Do not redefine project scope.
- Do not invent business rules.
- Do not overwrite existing files without explicit approval.
- Do not store secrets in the repo.
- Prefer small, testable changes.
- Update `planning/STATE.md` at the end of each meaningful session.
- Record durable decisions in `planning/DECISIONS.md`.
- Update `docs/ARCHITECTURE.md` when architecture changes.
- Add or update tests when behavior changes.

---

## Sprint Workflow

Each sprint lives in:

```text
planning/sprints/###-{sprint-name}/
```

Each sprint should include:

- `requirements.md` — what and why
- `blueprint.md` — how to build it
- `acceptance.md` — what done means
- `handoff-prompt.md` — exact Builder prompt

The Builder should read all four before implementation.

---

## Completion Standard

A task is complete only when:

- The requested behavior is implemented.
- Relevant tests pass or a clear reason is documented.
- Acceptance criteria are satisfied.
- State and documentation are updated where needed.
- Any unresolved risks or questions are recorded.
