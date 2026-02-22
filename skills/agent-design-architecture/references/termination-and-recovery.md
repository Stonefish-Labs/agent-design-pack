---
id: arch-termination-recovery
title: "Termination and Recovery Strategy"
domain: architecture
kind: playbook
status: active
last_reviewed: 2026-02-22
update_cadence: quarterly
tags:
  - termination
  - recovery
  - resilience
related:
  - arch-orchestration-authority
  - arch-session-state-models
  - arch-anti-patterns
---

# Termination and Recovery Strategy

## Intent
Define completion criteria, rollback strategy, and degraded-mode behavior before runtime.

## Diagnostic Questions
- What assumption about done criteria is currently implicit and needs to be made explicit?
- Which constraint around retry policy will break first under growth or stress?
- What evidence will prove that recovery ownership is working in production, not just in demos?

## Recommended Moves
- Define a policy for done criteria before implementation choices are made.
- Attach measurable acceptance criteria to decisions about retry policy.
- Add a review gate that validates recovery ownership at release boundaries.
- Record rejected alternatives and why they were rejected to prevent decision drift.

## Failure Modes to Avoid
- Treating done criteria as static even when runtime constraints change.
- Optimizing for short-term speed while leaving retry policy undefined.
- Assuming recovery ownership without instrumented verification.

## Expected Deliverables
- A decision note that freezes the policy for done criteria.
- An execution checklist tied to retry policy risk controls.
- A review artifact showing pass or fail evidence for recovery ownership.

## Related References
- `arch-orchestration-authority`
- `arch-session-state-models`
- `arch-anti-patterns`

## Review Cadence
Review this reference on a `quarterly` cadence or sooner when operating constraints materially change.
