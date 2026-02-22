---
id: work-review-gate-patterns
title: "Review Gate Patterns"
domain: workflow-delegation
kind: pattern
status: active
last_reviewed: 2026-02-22
update_cadence: quarterly
tags:
  - review
  - quality-gates
  - validation
related:
  - work-handoff-contract-spec
  - out-rubric-evaluation-design
  - core-governance-model
---

# Review Gate Patterns

## Intent
Insert explicit review gates where high-risk transitions need human or rubric verification.

## Diagnostic Questions
- What assumption about gate placement is currently implicit and needs to be made explicit?
- Which constraint around approval criteria will break first under growth or stress?
- What evidence will prove that rework loop is working in production, not just in demos?

## Recommended Moves
- Define a policy for gate placement before implementation choices are made.
- Attach measurable acceptance criteria to decisions about approval criteria.
- Add a review gate that validates rework loop at release boundaries.
- Record rejected alternatives and why they were rejected to prevent decision drift.

## Failure Modes to Avoid
- Treating gate placement as static even when runtime constraints change.
- Optimizing for short-term speed while leaving approval criteria undefined.
- Assuming rework loop without instrumented verification.

## Expected Deliverables
- A decision note that freezes the policy for gate placement.
- An execution checklist tied to approval criteria risk controls.
- A review artifact showing pass or fail evidence for rework loop.

## Related References
- `work-handoff-contract-spec`
- `out-rubric-evaluation-design`
- `core-governance-model`

## Review Cadence
Review this reference on a `quarterly` cadence or sooner when operating constraints materially change.
