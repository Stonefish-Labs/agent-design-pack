---
id: out-qa-checklists
title: "Output Reliability QA Checklists"
domain: output-reliability
kind: checklist
status: active
last_reviewed: 2026-02-22
update_cadence: on-change
tags:
  - qa
  - checklists
  - acceptance
related:
  - out-rubric-evaluation-design
  - out-factual-verification-patterns
  - core-governance-model
---

# Output Reliability QA Checklists

## Intent
Provide execution-ready checklists for release readiness and regression detection.

## Diagnostic Questions
- What assumption about preflight checks is currently implicit and needs to be made explicit?
- Which constraint around release gate will break first under growth or stress?
- What evidence will prove that post-incident review is working in production, not just in demos?

## Recommended Moves
- Define a policy for preflight checks before implementation choices are made.
- Attach measurable acceptance criteria to decisions about release gate.
- Add a review gate that validates post-incident review at release boundaries.
- Record rejected alternatives and why they were rejected to prevent decision drift.

## Checklist
- [ ] Explicitly document policy for preflight checks and assign an owner.
- [ ] Validate constraints around release gate against real runtime conditions.
- [ ] Confirm observable evidence exists for post-incident review.
- [ ] Confirm escalation route and fallback behavior are documented.
- [ ] Capture unresolved risks and next review date.

## Failure Modes to Avoid
- Treating preflight checks as static even when runtime constraints change.
- Optimizing for short-term speed while leaving release gate undefined.
- Assuming post-incident review without instrumented verification.

## Expected Deliverables
- A decision note that freezes the policy for preflight checks.
- An execution checklist tied to release gate risk controls.
- A review artifact showing pass or fail evidence for post-incident review.

## Related References
- `out-rubric-evaluation-design`
- `out-factual-verification-patterns`
- `core-governance-model`

## Review Cadence
Review this reference on a `on-change` cadence or sooner when operating constraints materially change.
