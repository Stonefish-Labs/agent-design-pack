---
id: core-pattern-catalog
title: "Cross-Domain Pattern Catalog"
domain: core
kind: pattern
status: active
last_reviewed: 2026-02-22
update_cadence: monthly
tags:
  - patterns
  - playbooks
  - scaling
related:
  - core-anti-pattern-catalog
  - core-routing-playbook
  - work-review-gate-patterns
---

# Cross-Domain Pattern Catalog

## Intent
Capture reusable design patterns that repeatedly deliver reliable outcomes across agent systems.

## Diagnostic Questions
- What assumption about bounded delegation is currently implicit and needs to be made explicit?
- Which constraint around explicit contracts will break first under growth or stress?
- What evidence will prove that progressive disclosure is working in production, not just in demos?

## Recommended Moves
- Define a policy for bounded delegation before implementation choices are made.
- Attach measurable acceptance criteria to decisions about explicit contracts.
- Add a review gate that validates progressive disclosure at release boundaries.
- Record rejected alternatives and why they were rejected to prevent decision drift.

## Failure Modes to Avoid
- Treating bounded delegation as static even when runtime constraints change.
- Optimizing for short-term speed while leaving explicit contracts undefined.
- Assuming progressive disclosure without instrumented verification.

## Expected Deliverables
- A decision note that freezes the policy for bounded delegation.
- An execution checklist tied to explicit contracts risk controls.
- A review artifact showing pass or fail evidence for progressive disclosure.

## Related References
- `core-anti-pattern-catalog`
- `core-routing-playbook`
- `work-review-gate-patterns`

## Review Cadence
Review this reference on a `monthly` cadence or sooner when operating constraints materially change.
