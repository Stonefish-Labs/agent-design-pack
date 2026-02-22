---
id: core-decision-axes
title: "Cross-Domain Decision Axes"
domain: core
kind: decision-matrix
status: active
last_reviewed: 2026-02-22
update_cadence: monthly
tags:
  - decision-framework
  - tradeoffs
  - governance
related:
  - core-taxonomy
  - arch-decision-matrix
  - toolsec-tooling-selection-matrix
---

# Cross-Domain Decision Axes

## Intent
Provide reusable axes for evaluating architecture, tooling, workflow, retrieval, and quality decisions.

## Diagnostic Questions
- What assumption about control authority is currently implicit and needs to be made explicit?
- Which constraint around failure tolerance will break first under growth or stress?
- What evidence will prove that operational cost is working in production, not just in demos?

## Decision Matrix
| Signal | Prefer | Why |
|---|---|---|
| High uncertainty around control authority | Use a staged approach with explicit gates | Keeps decision reversibility high while evidence matures |
| Tight delivery deadline with low risk around failure tolerance | Use the simplest controlled path | Reduces overhead without dropping core safeguards |
| Expanding blast radius linked to operational cost | Add formal policy and review checkpoints | Prevents silent drift and late-stage surprises |

## Recommended Moves
- Define a policy for control authority before implementation choices are made.
- Attach measurable acceptance criteria to decisions about failure tolerance.
- Add a review gate that validates operational cost at release boundaries.
- Record rejected alternatives and why they were rejected to prevent decision drift.

## Failure Modes to Avoid
- Treating control authority as static even when runtime constraints change.
- Optimizing for short-term speed while leaving failure tolerance undefined.
- Assuming operational cost without instrumented verification.

## Expected Deliverables
- A decision note that freezes the policy for control authority.
- An execution checklist tied to failure tolerance risk controls.
- A review artifact showing pass or fail evidence for operational cost.

## Related References
- `core-taxonomy`
- `arch-decision-matrix`
- `toolsec-tooling-selection-matrix`

## Review Cadence
Review this reference on a `monthly` cadence or sooner when operating constraints materially change.
