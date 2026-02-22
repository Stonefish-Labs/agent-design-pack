---
id: work-delegation-security-rules
title: "Delegation Security Rules"
domain: workflow-delegation
kind: checklist
status: active
last_reviewed: 2026-02-22
update_cadence: monthly
tags:
  - delegation
  - security
  - policy
related:
  - work-guardian-broker-architecture
  - toolsec-security-boundaries-consent
  - core-governance-model
---

# Delegation Security Rules

## Intent
Define enforceable policy for nested delegation, permission inheritance, and inter-agent communication.

## Diagnostic Questions
- What assumption about permission transfer is currently implicit and needs to be made explicit?
- Which constraint around spawn constraints will break first under growth or stress?
- What evidence will prove that message mediation is working in production, not just in demos?

## Recommended Moves
- Define a policy for permission transfer before implementation choices are made.
- Attach measurable acceptance criteria to decisions about spawn constraints.
- Add a review gate that validates message mediation at release boundaries.
- Record rejected alternatives and why they were rejected to prevent decision drift.

## Checklist
- [ ] Explicitly document policy for permission transfer and assign an owner.
- [ ] Validate constraints around spawn constraints against real runtime conditions.
- [ ] Confirm observable evidence exists for message mediation.
- [ ] Confirm escalation route and fallback behavior are documented.
- [ ] Capture unresolved risks and next review date.

## Failure Modes to Avoid
- Treating permission transfer as static even when runtime constraints change.
- Optimizing for short-term speed while leaving spawn constraints undefined.
- Assuming message mediation without instrumented verification.

## Expected Deliverables
- A decision note that freezes the policy for permission transfer.
- An execution checklist tied to spawn constraints risk controls.
- A review artifact showing pass or fail evidence for message mediation.

## Related References
- `work-guardian-broker-architecture`
- `toolsec-security-boundaries-consent`
- `core-governance-model`

## Review Cadence
Review this reference on a `monthly` cadence or sooner when operating constraints materially change.
