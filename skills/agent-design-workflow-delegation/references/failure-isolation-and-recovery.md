---
id: work-failure-isolation-recovery
title: "Failure Isolation and Recovery"
domain: workflow-delegation
kind: playbook
status: active
last_reviewed: 2026-02-22
update_cadence: quarterly
tags:
  - failure
  - isolation
  - recovery
related:
  - work-monolith-vs-staged-tradeoffs
  - arch-termination-recovery
  - work-delegation-security-rules
---

# Failure Isolation and Recovery

## Intent
Design stage boundaries to contain failures and enable targeted retries instead of global reruns.

## Diagnostic Questions
- What assumption about blast radius is currently implicit and needs to be made explicit?
- Which constraint around retry contract will break first under growth or stress?
- What evidence will prove that fallback path is working in production, not just in demos?

## Recommended Moves
- Define a policy for blast radius before implementation choices are made.
- Attach measurable acceptance criteria to decisions about retry contract.
- Add a review gate that validates fallback path at release boundaries.
- Record rejected alternatives and why they were rejected to prevent decision drift.

## Failure Modes to Avoid
- Treating blast radius as static even when runtime constraints change.
- Optimizing for short-term speed while leaving retry contract undefined.
- Assuming fallback path without instrumented verification.

## Expected Deliverables
- A decision note that freezes the policy for blast radius.
- An execution checklist tied to retry contract risk controls.
- A review artifact showing pass or fail evidence for fallback path.

## Related References
- `work-monolith-vs-staged-tradeoffs`
- `arch-termination-recovery`
- `work-delegation-security-rules`

## Review Cadence
Review this reference on a `quarterly` cadence or sooner when operating constraints materially change.
