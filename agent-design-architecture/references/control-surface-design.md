---
id: arch-control-surface-design
title: "Control Surface Design"
domain: architecture
kind: pattern
status: active
last_reviewed: 2026-02-22
update_cadence: quarterly
tags:
  - control-surface
  - gates
  - approvals
related:
  - arch-orchestration-authority
  - toolsec-security-boundaries-consent
  - work-review-gate-patterns
---

# Control Surface Design

## Intent
Design explicit approval and guardrail touchpoints around high-impact actions.

## Diagnostic Questions
- What assumption about approval points is currently implicit and needs to be made explicit?
- Which constraint around risk-based gating will break first under growth or stress?
- What evidence will prove that operator ergonomics is working in production, not just in demos?

## Recommended Moves
- Define a policy for approval points before implementation choices are made.
- Attach measurable acceptance criteria to decisions about risk-based gating.
- Add a review gate that validates operator ergonomics at release boundaries.
- Record rejected alternatives and why they were rejected to prevent decision drift.

## Failure Modes to Avoid
- Treating approval points as static even when runtime constraints change.
- Optimizing for short-term speed while leaving risk-based gating undefined.
- Assuming operator ergonomics without instrumented verification.

## Expected Deliverables
- A decision note that freezes the policy for approval points.
- An execution checklist tied to risk-based gating risk controls.
- A review artifact showing pass or fail evidence for operator ergonomics.

## Related References
- `arch-orchestration-authority`
- `toolsec-security-boundaries-consent`
- `work-review-gate-patterns`

## Review Cadence
Review this reference on a `quarterly` cadence or sooner when operating constraints materially change.
