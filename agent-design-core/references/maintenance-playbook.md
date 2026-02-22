---
id: core-maintenance-playbook
title: "Maintenance Playbook"
domain: core
kind: playbook
status: active
last_reviewed: 2026-02-22
update_cadence: on-change
tags:
  - maintenance
  - operations
  - lifecycle
related:
  - core-governance-model
  - core-editorial-standards
  - core-source-coverage-matrix
---

# Maintenance Playbook

## Intent
Operationalize monthly and on-change maintenance for references, links, and coverage guarantees.

## Diagnostic Questions
- What assumption about drift detection is currently implicit and needs to be made explicit?
- Which constraint around review workflows will break first under growth or stress?
- What evidence will prove that quality automation is working in production, not just in demos?

## Recommended Moves
- Define a policy for drift detection before implementation choices are made.
- Attach measurable acceptance criteria to decisions about review workflows.
- Add a review gate that validates quality automation at release boundaries.
- Record rejected alternatives and why they were rejected to prevent decision drift.

## Failure Modes to Avoid
- Treating drift detection as static even when runtime constraints change.
- Optimizing for short-term speed while leaving review workflows undefined.
- Assuming quality automation without instrumented verification.

## Expected Deliverables
- A decision note that freezes the policy for drift detection.
- An execution checklist tied to review workflows risk controls.
- A review artifact showing pass or fail evidence for quality automation.

## Related References
- `core-governance-model`
- `core-editorial-standards`
- `core-source-coverage-matrix`

## Review Cadence
Review this reference on a `on-change` cadence or sooner when operating constraints materially change.
