---
id: work-decomposition-heuristics
title: "Workflow Decomposition Heuristics"
domain: workflow-delegation
kind: decision-matrix
status: active
last_reviewed: 2026-02-22
update_cadence: quarterly
tags:
  - decomposition
  - delegation
  - workflow
related:
  - work-monolith-vs-staged-tradeoffs
  - work-handoff-contract-spec
  - core-decision-axes
---

# Workflow Decomposition Heuristics

## Intent
Decide when to keep work monolithic versus splitting into staged handoffs.

## Diagnostic Questions
- What assumption about phase boundaries is currently implicit and needs to be made explicit?
- Which constraint around reuse potential will break first under growth or stress?
- What evidence will prove that failure isolation is working in production, not just in demos?

## Decision Matrix
| Signal | Prefer | Why |
|---|---|---|
| High uncertainty around phase boundaries | Use a staged approach with explicit gates | Keeps decision reversibility high while evidence matures |
| Tight delivery deadline with low risk around reuse potential | Use the simplest controlled path | Reduces overhead without dropping core safeguards |
| Expanding blast radius linked to failure isolation | Add formal policy and review checkpoints | Prevents silent drift and late-stage surprises |

## Recommended Moves
- Define a policy for phase boundaries before implementation choices are made.
- Attach measurable acceptance criteria to decisions about reuse potential.
- Add a review gate that validates failure isolation at release boundaries.
- Record rejected alternatives and why they were rejected to prevent decision drift.

## Failure Modes to Avoid
- Treating phase boundaries as static even when runtime constraints change.
- Optimizing for short-term speed while leaving reuse potential undefined.
- Assuming failure isolation without instrumented verification.

## Expected Deliverables
- A decision note that freezes the policy for phase boundaries.
- An execution checklist tied to reuse potential risk controls.
- A review artifact showing pass or fail evidence for failure isolation.

## Related References
- `work-monolith-vs-staged-tradeoffs`
- `work-handoff-contract-spec`
- `core-decision-axes`

## Review Cadence
Review this reference on a `quarterly` cadence or sooner when operating constraints materially change.
