---
id: work-ephemeral-isolation-pattern
title: "Ephemeral Isolation Pattern"
domain: workflow-delegation
kind: pattern
status: active
last_reviewed: 2026-02-22
update_cadence: quarterly
tags:
  - ephemeral
  - isolation
  - least-privilege
related:
  - work-guardian-broker-architecture
  - toolsec-security-boundaries-consent
  - work-delegation-security-rules
---

# Ephemeral Isolation Pattern

## Intent
Apply ephemeral workspaces and least-privilege templates to reduce contamination and lateral movement risk.

## Diagnostic Questions
- What assumption about workspace lifecycle is currently implicit and needs to be made explicit?
- Which constraint around template constraints will break first under growth or stress?
- What evidence will prove that teardown guarantees is working in production, not just in demos?

## Recommended Moves
- Define a policy for workspace lifecycle before implementation choices are made.
- Attach measurable acceptance criteria to decisions about template constraints.
- Add a review gate that validates teardown guarantees at release boundaries.
- Record rejected alternatives and why they were rejected to prevent decision drift.

## Failure Modes to Avoid
- Treating workspace lifecycle as static even when runtime constraints change.
- Optimizing for short-term speed while leaving template constraints undefined.
- Assuming teardown guarantees without instrumented verification.

## Expected Deliverables
- A decision note that freezes the policy for workspace lifecycle.
- An execution checklist tied to template constraints risk controls.
- A review artifact showing pass or fail evidence for teardown guarantees.

## Related References
- `work-guardian-broker-architecture`
- `toolsec-security-boundaries-consent`
- `work-delegation-security-rules`

## Review Cadence
Review this reference on a `quarterly` cadence or sooner when operating constraints materially change.
