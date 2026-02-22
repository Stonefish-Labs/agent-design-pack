---
id: work-monolith-vs-staged-tradeoffs
title: "Monolith vs Staged Tradeoffs"
domain: workflow-delegation
kind: decision-matrix
status: active
last_reviewed: 2026-02-22
update_cadence: quarterly
tags:
  - monolith
  - staged
  - tradeoffs
related:
  - work-decomposition-heuristics
  - work-context-budgeting
  - work-review-gate-patterns
---

# Monolith vs Staged Tradeoffs

## Intent
Compare token cost, resilience, and operational complexity between workflow structures.

## Diagnostic Questions
- What assumption about context accumulation is currently implicit and needs to be made explicit?
- Which constraint around handoff overhead will break first under growth or stress?
- What evidence will prove that recovery granularity is working in production, not just in demos?

## Decision Matrix
| Signal | Prefer | Why |
|---|---|---|
| High uncertainty around context accumulation | Use a staged approach with explicit gates | Keeps decision reversibility high while evidence matures |
| Tight delivery deadline with low risk around handoff overhead | Use the simplest controlled path | Reduces overhead without dropping core safeguards |
| Expanding blast radius linked to recovery granularity | Add formal policy and review checkpoints | Prevents silent drift and late-stage surprises |

## Recommended Moves
- Define a policy for context accumulation before implementation choices are made.
- Attach measurable acceptance criteria to decisions about handoff overhead.
- Add a review gate that validates recovery granularity at release boundaries.
- Record rejected alternatives and why they were rejected to prevent decision drift.

## Failure Modes to Avoid
- Treating context accumulation as static even when runtime constraints change.
- Optimizing for short-term speed while leaving handoff overhead undefined.
- Assuming recovery granularity without instrumented verification.

## Expected Deliverables
- A decision note that freezes the policy for context accumulation.
- An execution checklist tied to handoff overhead risk controls.
- A review artifact showing pass or fail evidence for recovery granularity.

## Related References
- `work-decomposition-heuristics`
- `work-context-budgeting`
- `work-review-gate-patterns`

## Review Cadence
Review this reference on a `quarterly` cadence or sooner when operating constraints materially change.
