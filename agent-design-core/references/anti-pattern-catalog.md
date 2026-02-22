---
id: core-anti-pattern-catalog
title: "Cross-Domain Anti-Pattern Catalog"
domain: core
kind: anti-pattern
status: active
last_reviewed: 2026-02-22
update_cadence: monthly
tags:
  - anti-patterns
  - risk
  - governance
related:
  - core-pattern-catalog
  - arch-anti-patterns
  - out-output-reliability-anti-patterns
---

# Cross-Domain Anti-Pattern Catalog

## Intent
Document recurring failure modes that degrade trust, reliability, or maintainability.

## Diagnostic Questions
- What assumption about implicit assumptions is currently implicit and needs to be made explicit?
- Which constraint around unchecked autonomy will break first under growth or stress?
- What evidence will prove that unowned drift is working in production, not just in demos?

## Recommended Moves
- Define a policy for implicit assumptions before implementation choices are made.
- Attach measurable acceptance criteria to decisions about unchecked autonomy.
- Add a review gate that validates unowned drift at release boundaries.
- Record rejected alternatives and why they were rejected to prevent decision drift.

## Anti-Pattern Catalog
- **Invisible policy**: Teams assume alignment on implicit assumptions without writing decision boundaries.
- **Unbounded scope**: Work expands around unchecked autonomy without explicit stop conditions.
- **Evidence debt**: Claims about unowned drift ship without measurable validation.

## Failure Modes to Avoid
- Treating implicit assumptions as static even when runtime constraints change.
- Optimizing for short-term speed while leaving unchecked autonomy undefined.
- Assuming unowned drift without instrumented verification.

## Expected Deliverables
- A decision note that freezes the policy for implicit assumptions.
- An execution checklist tied to unchecked autonomy risk controls.
- A review artifact showing pass or fail evidence for unowned drift.

## Related References
- `core-pattern-catalog`
- `arch-anti-patterns`
- `out-output-reliability-anti-patterns`

## Review Cadence
Review this reference on a `monthly` cadence or sooner when operating constraints materially change.
