---
id: core-taxonomy
title: "Agent Design Taxonomy"
domain: core
kind: concept
status: active
last_reviewed: 2026-02-22
update_cadence: monthly
tags:
  - taxonomy
  - classification
  - scope
related:
  - core-glossary
  - core-decision-axes
  - core-routing-playbook
---

# Agent Design Taxonomy

## Intent
Define the canonical classification model used across the suite so routing and governance stay consistent.

## Diagnostic Questions
- What assumption about problem framing is currently implicit and needs to be made explicit?
- Which constraint around decision ownership will break first under growth or stress?
- What evidence will prove that execution boundary is working in production, not just in demos?

## Recommended Moves
- Define a policy for problem framing before implementation choices are made.
- Attach measurable acceptance criteria to decisions about decision ownership.
- Add a review gate that validates execution boundary at release boundaries.
- Record rejected alternatives and why they were rejected to prevent decision drift.

## Failure Modes to Avoid
- Treating problem framing as static even when runtime constraints change.
- Optimizing for short-term speed while leaving decision ownership undefined.
- Assuming execution boundary without instrumented verification.

## Expected Deliverables
- A decision note that freezes the policy for problem framing.
- An execution checklist tied to decision ownership risk controls.
- A review artifact showing pass or fail evidence for execution boundary.

## Related References
- `core-glossary`
- `core-decision-axes`
- `core-routing-playbook`

## Review Cadence
Review this reference on a `monthly` cadence or sooner when operating constraints materially change.
