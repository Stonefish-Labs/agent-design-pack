---
id: out-factual-verification-patterns
title: "Factual Verification Patterns"
domain: output-reliability
kind: pattern
status: active
last_reviewed: 2026-02-22
update_cadence: quarterly
tags:
  - factuality
  - verification
  - ground-truth
related:
  - out-quality-layer-model
  - know-custom-rag-patterns
  - out-qa-checklists
---

# Factual Verification Patterns

## Intent
Introduce deterministic checks against ground truth for claims used in decisions or automation.

## Diagnostic Questions
- What assumption about evidence source is currently implicit and needs to be made explicit?
- Which constraint around verification step will break first under growth or stress?
- What evidence will prove that confidence thresholds is working in production, not just in demos?

## Recommended Moves
- Define a policy for evidence source before implementation choices are made.
- Attach measurable acceptance criteria to decisions about verification step.
- Add a review gate that validates confidence thresholds at release boundaries.
- Record rejected alternatives and why they were rejected to prevent decision drift.

## Failure Modes to Avoid
- Treating evidence source as static even when runtime constraints change.
- Optimizing for short-term speed while leaving verification step undefined.
- Assuming confidence thresholds without instrumented verification.

## Expected Deliverables
- A decision note that freezes the policy for evidence source.
- An execution checklist tied to verification step risk controls.
- A review artifact showing pass or fail evidence for confidence thresholds.

## Related References
- `out-quality-layer-model`
- `know-custom-rag-patterns`
- `out-qa-checklists`

## Review Cadence
Review this reference on a `quarterly` cadence or sooner when operating constraints materially change.
