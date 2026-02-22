---
id: work-context-budgeting
title: "Context Budgeting"
domain: workflow-delegation
kind: playbook
status: active
last_reviewed: 2026-02-22
update_cadence: quarterly
tags:
  - context
  - budget
  - token-economy
related:
  - work-monolith-vs-staged-tradeoffs
  - know-awareness-orchestration
  - out-layer-composition-patterns
---

# Context Budgeting

## Intent
Allocate context intentionally across stages to balance quality, cost, and auditability.

## Diagnostic Questions
- What assumption about context allocation is currently implicit and needs to be made explicit?
- Which constraint around summarization boundary will break first under growth or stress?
- What evidence will prove that handoff compression is working in production, not just in demos?

## Recommended Moves
- Define a policy for context allocation before implementation choices are made.
- Attach measurable acceptance criteria to decisions about summarization boundary.
- Add a review gate that validates handoff compression at release boundaries.
- Record rejected alternatives and why they were rejected to prevent decision drift.

## Failure Modes to Avoid
- Treating context allocation as static even when runtime constraints change.
- Optimizing for short-term speed while leaving summarization boundary undefined.
- Assuming handoff compression without instrumented verification.

## Expected Deliverables
- A decision note that freezes the policy for context allocation.
- An execution checklist tied to summarization boundary risk controls.
- A review artifact showing pass or fail evidence for handoff compression.

## Related References
- `work-monolith-vs-staged-tradeoffs`
- `know-awareness-orchestration`
- `out-layer-composition-patterns`

## Review Cadence
Review this reference on a `quarterly` cadence or sooner when operating constraints materially change.
