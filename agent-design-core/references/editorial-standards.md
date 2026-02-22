---
id: core-editorial-standards
title: "Editorial Standards"
domain: core
kind: checklist
status: active
last_reviewed: 2026-02-22
update_cadence: monthly
tags:
  - writing
  - quality
  - consistency
related:
  - core-glossary
  - core-governance-model
  - core-maintenance-playbook
---

# Editorial Standards

## Intent
Define writing standards for consulting-style references that remain practical and testable.

## Diagnostic Questions
- What assumption about decision completeness is currently implicit and needs to be made explicit?
- Which constraint around evidence quality will break first under growth or stress?
- What evidence will prove that actionability is working in production, not just in demos?

## Recommended Moves
- Define a policy for decision completeness before implementation choices are made.
- Attach measurable acceptance criteria to decisions about evidence quality.
- Add a review gate that validates actionability at release boundaries.
- Record rejected alternatives and why they were rejected to prevent decision drift.

## Checklist
- [ ] Explicitly document policy for decision completeness and assign an owner.
- [ ] Validate constraints around evidence quality against real runtime conditions.
- [ ] Confirm observable evidence exists for actionability.
- [ ] Confirm escalation route and fallback behavior are documented.
- [ ] Capture unresolved risks and next review date.

## Failure Modes to Avoid
- Treating decision completeness as static even when runtime constraints change.
- Optimizing for short-term speed while leaving evidence quality undefined.
- Assuming actionability without instrumented verification.

## Expected Deliverables
- A decision note that freezes the policy for decision completeness.
- An execution checklist tied to evidence quality risk controls.
- A review artifact showing pass or fail evidence for actionability.

## Related References
- `core-glossary`
- `core-governance-model`
- `core-maintenance-playbook`

## Review Cadence
Review this reference on a `monthly` cadence or sooner when operating constraints materially change.
