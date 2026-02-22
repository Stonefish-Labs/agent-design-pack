---
id: arch-anti-patterns
title: "Architecture Anti-Patterns"
domain: architecture
kind: anti-pattern
status: active
last_reviewed: 2026-02-22
update_cadence: quarterly
tags:
  - anti-patterns
  - failure-modes
  - reliability
related:
  - arch-decision-matrix
  - arch-termination-recovery
  - core-anti-pattern-catalog
---

# Architecture Anti-Patterns

## Intent
Prevent recurring architecture mistakes that increase ambiguity or operational fragility.

## Diagnostic Questions
- What assumption about hidden autonomy is currently implicit and needs to be made explicit?
- Which constraint around undefined ownership will break first under growth or stress?
- What evidence will prove that recovery gaps is working in production, not just in demos?

## Recommended Moves
- Define a policy for hidden autonomy before implementation choices are made.
- Attach measurable acceptance criteria to decisions about undefined ownership.
- Add a review gate that validates recovery gaps at release boundaries.
- Record rejected alternatives and why they were rejected to prevent decision drift.

## Anti-Pattern Catalog
- **Invisible policy**: Teams assume alignment on hidden autonomy without writing decision boundaries.
- **Unbounded scope**: Work expands around undefined ownership without explicit stop conditions.
- **Evidence debt**: Claims about recovery gaps ship without measurable validation.

## Failure Modes to Avoid
- Treating hidden autonomy as static even when runtime constraints change.
- Optimizing for short-term speed while leaving undefined ownership undefined.
- Assuming recovery gaps without instrumented verification.

## Expected Deliverables
- A decision note that freezes the policy for hidden autonomy.
- An execution checklist tied to undefined ownership risk controls.
- A review artifact showing pass or fail evidence for recovery gaps.

## Related References
- `arch-decision-matrix`
- `arch-termination-recovery`
- `core-anti-pattern-catalog`

## Review Cadence
Review this reference on a `quarterly` cadence or sooner when operating constraints materially change.
