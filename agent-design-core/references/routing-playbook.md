---
id: core-routing-playbook
title: "Suite Routing Playbook"
domain: core
kind: playbook
status: active
last_reviewed: 2026-02-22
update_cadence: on-change
tags:
  - routing
  - triage
  - orchestration
related:
  - core-taxonomy
  - core-decision-axes
  - core-maintenance-playbook
---

# Suite Routing Playbook

## Intent
Standardize how prompts are routed to one or more domain skills with clear escalation rules.

## Diagnostic Questions
- What assumption about intent triage is currently implicit and needs to be made explicit?
- Which constraint around skill selection will break first under growth or stress?
- What evidence will prove that cross-domain handoff is working in production, not just in demos?

## Recommended Moves
- Define a policy for intent triage before implementation choices are made.
- Attach measurable acceptance criteria to decisions about skill selection.
- Add a review gate that validates cross-domain handoff at release boundaries.
- Record rejected alternatives and why they were rejected to prevent decision drift.

## Failure Modes to Avoid
- Treating intent triage as static even when runtime constraints change.
- Optimizing for short-term speed while leaving skill selection undefined.
- Assuming cross-domain handoff without instrumented verification.

## Expected Deliverables
- A decision note that freezes the policy for intent triage.
- An execution checklist tied to skill selection risk controls.
- A review artifact showing pass or fail evidence for cross-domain handoff.

## Related References
- `core-taxonomy`
- `core-decision-axes`
- `core-maintenance-playbook`

## Review Cadence
Review this reference on a `on-change` cadence or sooner when operating constraints materially change.
