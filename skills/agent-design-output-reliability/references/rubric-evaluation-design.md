---
id: out-rubric-evaluation-design
title: "Rubric Evaluation Design"
domain: output-reliability
kind: playbook
status: active
last_reviewed: 2026-02-22
update_cadence: quarterly
tags:
  - rubric
  - evaluation
  - quality-gates
related:
  - out-quality-layer-model
  - work-review-gate-patterns
  - out-qa-checklists
---

# Rubric Evaluation Design

## Intent
Define rubrics that measure semantic usefulness rather than only structural validity.

## Diagnostic Questions
- What assumption about rubric dimensions is currently implicit and needs to be made explicit?
- Which constraint around scoring anchors will break first under growth or stress?
- What evidence will prove that accept/reject thresholds is working in production, not just in demos?

## Recommended Moves
- Define a policy for rubric dimensions before implementation choices are made.
- Attach measurable acceptance criteria to decisions about scoring anchors.
- Add a review gate that validates accept/reject thresholds at release boundaries.
- Record rejected alternatives and why they were rejected to prevent decision drift.

## Failure Modes to Avoid
- Treating rubric dimensions as static even when runtime constraints change.
- Optimizing for short-term speed while leaving scoring anchors undefined.
- Assuming accept/reject thresholds without instrumented verification.

## Expected Deliverables
- A decision note that freezes the policy for rubric dimensions.
- An execution checklist tied to scoring anchors risk controls.
- A review artifact showing pass or fail evidence for accept/reject thresholds.

## Related References
- `out-quality-layer-model`
- `work-review-gate-patterns`
- `out-qa-checklists`

## Review Cadence
Review this reference on a `quarterly` cadence or sooner when operating constraints materially change.
