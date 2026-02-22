---
id: arch-spectrum-model
title: "Architecture Spectrum Model"
domain: architecture
kind: concept
status: active
last_reviewed: 2026-02-22
update_cadence: quarterly
tags:
  - architecture
  - spectrum
  - orchestration
related:
  - arch-decision-matrix
  - arch-orchestration-authority
  - core-decision-axes
---

# Architecture Spectrum Model

## Intent
Frame programmatic, managed-agent, assistant, and autonomous architectures as a continuous spectrum.

## Diagnostic Questions
- What assumption about spectrum placement is currently implicit and needs to be made explicit?
- Which constraint around control model will break first under growth or stress?
- What evidence will prove that operating context is working in production, not just in demos?

## Recommended Moves
- Define a policy for spectrum placement before implementation choices are made.
- Attach measurable acceptance criteria to decisions about control model.
- Add a review gate that validates operating context at release boundaries.
- Record rejected alternatives and why they were rejected to prevent decision drift.

## Failure Modes to Avoid
- Treating spectrum placement as static even when runtime constraints change.
- Optimizing for short-term speed while leaving control model undefined.
- Assuming operating context without instrumented verification.

## Expected Deliverables
- A decision note that freezes the policy for spectrum placement.
- An execution checklist tied to control model risk controls.
- A review artifact showing pass or fail evidence for operating context.

## Related References
- `arch-decision-matrix`
- `arch-orchestration-authority`
- `core-decision-axes`

## Review Cadence
Review this reference on a `quarterly` cadence or sooner when operating constraints materially change.
