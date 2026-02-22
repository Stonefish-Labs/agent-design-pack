---
id: core-glossary
title: "Agent Design Glossary"
domain: core
kind: concept
status: active
last_reviewed: 2026-02-22
update_cadence: monthly
tags:
  - glossary
  - definitions
  - alignment
related:
  - core-taxonomy
  - core-editorial-standards
  - core-pattern-catalog
---

# Agent Design Glossary

## Intent
Normalize critical terms so strategy discussions do not break on ambiguous language.

## Diagnostic Questions
- What assumption about term precision is currently implicit and needs to be made explicit?
- Which constraint around cross-team alignment will break first under growth or stress?
- What evidence will prove that decision traceability is working in production, not just in demos?

## Recommended Moves
- Define a policy for term precision before implementation choices are made.
- Attach measurable acceptance criteria to decisions about cross-team alignment.
- Add a review gate that validates decision traceability at release boundaries.
- Record rejected alternatives and why they were rejected to prevent decision drift.

## Failure Modes to Avoid
- Treating term precision as static even when runtime constraints change.
- Optimizing for short-term speed while leaving cross-team alignment undefined.
- Assuming decision traceability without instrumented verification.

## Expected Deliverables
- A decision note that freezes the policy for term precision.
- An execution checklist tied to cross-team alignment risk controls.
- A review artifact showing pass or fail evidence for decision traceability.

## Related References
- `core-taxonomy`
- `core-editorial-standards`
- `core-pattern-catalog`

## Review Cadence
Review this reference on a `monthly` cadence or sooner when operating constraints materially change.
