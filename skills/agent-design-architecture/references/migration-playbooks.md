---
id: arch-migration-playbooks
title: "Architecture Migration Playbooks"
domain: architecture
kind: playbook
status: active
last_reviewed: 2026-02-22
update_cadence: on-change
tags:
  - migration
  - evolution
  - refactoring
related:
  - arch-spectrum-model
  - arch-decision-matrix
  - core-maintenance-playbook
---

# Architecture Migration Playbooks

## Intent
Plan controlled movement between spectrum positions without losing reliability.

## Diagnostic Questions
- What assumption about migration trigger is currently implicit and needs to be made explicit?
- Which constraint around risk controls will break first under growth or stress?
- What evidence will prove that rollback plan is working in production, not just in demos?

## Recommended Moves
- Define a policy for migration trigger before implementation choices are made.
- Attach measurable acceptance criteria to decisions about risk controls.
- Add a review gate that validates rollback plan at release boundaries.
- Record rejected alternatives and why they were rejected to prevent decision drift.

## Failure Modes to Avoid
- Treating migration trigger as static even when runtime constraints change.
- Optimizing for short-term speed while leaving risk controls undefined.
- Assuming rollback plan without instrumented verification.

## Expected Deliverables
- A decision note that freezes the policy for migration trigger.
- An execution checklist tied to risk controls risk controls.
- A review artifact showing pass or fail evidence for rollback plan.

## Related References
- `arch-spectrum-model`
- `arch-decision-matrix`
- `core-maintenance-playbook`

## Review Cadence
Review this reference on a `on-change` cadence or sooner when operating constraints materially change.
