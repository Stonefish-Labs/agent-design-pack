---
id: out-output-reliability-anti-patterns
title: "Output Reliability Anti-Patterns"
domain: output-reliability
kind: anti-pattern
status: active
last_reviewed: 2026-02-22
update_cadence: quarterly
tags:
  - anti-patterns
  - output-quality
  - reliability
related:
  - out-quality-layer-model
  - core-anti-pattern-catalog
  - out-qa-checklists
---

# Output Reliability Anti-Patterns

## Intent
Document failure patterns where teams over-index on formatting while missing true quality controls.

## Diagnostic Questions
- What assumption about format-only thinking is currently implicit and needs to be made explicit?
- Which constraint around missing verification will break first under growth or stress?
- What evidence will prove that undefined acceptance is working in production, not just in demos?

## Recommended Moves
- Define a policy for format-only thinking before implementation choices are made.
- Attach measurable acceptance criteria to decisions about missing verification.
- Add a review gate that validates undefined acceptance at release boundaries.
- Record rejected alternatives and why they were rejected to prevent decision drift.

## Anti-Pattern Catalog
- **Invisible policy**: Teams assume alignment on format-only thinking without writing decision boundaries.
- **Unbounded scope**: Work expands around missing verification without explicit stop conditions.
- **Evidence debt**: Claims about undefined acceptance ship without measurable validation.

## Failure Modes to Avoid
- Treating format-only thinking as static even when runtime constraints change.
- Optimizing for short-term speed while leaving missing verification undefined.
- Assuming undefined acceptance without instrumented verification.

## Expected Deliverables
- A decision note that freezes the policy for format-only thinking.
- An execution checklist tied to missing verification risk controls.
- A review artifact showing pass or fail evidence for undefined acceptance.

## Related References
- `out-quality-layer-model`
- `core-anti-pattern-catalog`
- `out-qa-checklists`

## Review Cadence
Review this reference on a `quarterly` cadence or sooner when operating constraints materially change.
