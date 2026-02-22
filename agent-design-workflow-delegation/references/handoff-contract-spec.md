---
id: work-handoff-contract-spec
title: "Handoff Contract Specification"
domain: workflow-delegation
kind: spec
status: active
last_reviewed: 2026-02-22
update_cadence: quarterly
tags:
  - handoff
  - contract
  - schema
related:
  - work-context-budgeting
  - work-review-gate-patterns
  - out-constrained-decoding-schema
---

# Handoff Contract Specification

## Intent
Define mandatory artifact structure for subagent handoffs so downstream stages remain deterministic.

## Diagnostic Questions
- What assumption about required fields is currently implicit and needs to be made explicit?
- Which constraint around quality gates will break first under growth or stress?
- What evidence will prove that contract evolution is working in production, not just in demos?

## Recommended Moves
- Define a policy for required fields before implementation choices are made.
- Attach measurable acceptance criteria to decisions about quality gates.
- Add a review gate that validates contract evolution at release boundaries.
- Record rejected alternatives and why they were rejected to prevent decision drift.

## Specification
### Required Inputs
- Current-state description for required fields.
- Target-state constraints for quality gates.
- Validation criteria for contract evolution.
### Required Outputs
- Decision outcome with rationale and owner.
- Risk register with controls and escalation path.
- Verification plan with pass or fail evidence.

## Failure Modes to Avoid
- Treating required fields as static even when runtime constraints change.
- Optimizing for short-term speed while leaving quality gates undefined.
- Assuming contract evolution without instrumented verification.

## Expected Deliverables
- A decision note that freezes the policy for required fields.
- An execution checklist tied to quality gates risk controls.
- A review artifact showing pass or fail evidence for contract evolution.

## Related References
- `work-context-budgeting`
- `work-review-gate-patterns`
- `out-constrained-decoding-schema`

## Review Cadence
Review this reference on a `quarterly` cadence or sooner when operating constraints materially change.
