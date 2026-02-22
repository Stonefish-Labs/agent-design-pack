---
id: arch-decision-matrix
title: "Architecture Decision Matrix"
domain: architecture
kind: decision-matrix
status: active
last_reviewed: 2026-02-22
update_cadence: quarterly
tags:
  - decision-framework
  - tradeoffs
  - selection
related:
  - arch-spectrum-model
  - arch-migration-playbooks
  - core-decision-axes
---

# Architecture Decision Matrix

## Intent
Compare architecture options with repeatable criteria and tie-break rules.

## Diagnostic Questions
- What assumption about decision signals is currently implicit and needs to be made explicit?
- Which constraint around option ranking will break first under growth or stress?
- What evidence will prove that confidence threshold is working in production, not just in demos?

## Decision Matrix
| Signal | Prefer | Why |
|---|---|---|
| High uncertainty around decision signals | Use a staged approach with explicit gates | Keeps decision reversibility high while evidence matures |
| Tight delivery deadline with low risk around option ranking | Use the simplest controlled path | Reduces overhead without dropping core safeguards |
| Expanding blast radius linked to confidence threshold | Add formal policy and review checkpoints | Prevents silent drift and late-stage surprises |

## Recommended Moves
- Define a policy for decision signals before implementation choices are made.
- Attach measurable acceptance criteria to decisions about option ranking.
- Add a review gate that validates confidence threshold at release boundaries.
- Record rejected alternatives and why they were rejected to prevent decision drift.

## Failure Modes to Avoid
- Treating decision signals as static even when runtime constraints change.
- Optimizing for short-term speed while leaving option ranking undefined.
- Assuming confidence threshold without instrumented verification.

## Expected Deliverables
- A decision note that freezes the policy for decision signals.
- An execution checklist tied to option ranking risk controls.
- A review artifact showing pass or fail evidence for confidence threshold.

## Related References
- `arch-spectrum-model`
- `arch-migration-playbooks`
- `core-decision-axes`

## Review Cadence
Review this reference on a `quarterly` cadence or sooner when operating constraints materially change.
