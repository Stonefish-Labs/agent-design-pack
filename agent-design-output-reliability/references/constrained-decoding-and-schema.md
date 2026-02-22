---
id: out-constrained-decoding-schema
title: "Constrained Decoding and Schema Design"
domain: output-reliability
kind: pattern
status: active
last_reviewed: 2026-02-22
update_cadence: quarterly
tags:
  - constrained-decoding
  - schema
  - typed-output
related:
  - out-quality-layer-model
  - work-handoff-contract-spec
  - out-coverage-determinism
---

# Constrained Decoding and Schema Design

## Intent
Use schema-constrained generation to guarantee parsable outputs and deterministic field presence.

## Diagnostic Questions
- What assumption about schema strictness is currently implicit and needs to be made explicit?
- Which constraint around enum control will break first under growth or stress?
- What evidence will prove that compatibility evolution is working in production, not just in demos?

## Recommended Moves
- Define a policy for schema strictness before implementation choices are made.
- Attach measurable acceptance criteria to decisions about enum control.
- Add a review gate that validates compatibility evolution at release boundaries.
- Record rejected alternatives and why they were rejected to prevent decision drift.

## Failure Modes to Avoid
- Treating schema strictness as static even when runtime constraints change.
- Optimizing for short-term speed while leaving enum control undefined.
- Assuming compatibility evolution without instrumented verification.

## Expected Deliverables
- A decision note that freezes the policy for schema strictness.
- An execution checklist tied to enum control risk controls.
- A review artifact showing pass or fail evidence for compatibility evolution.

## Related References
- `out-quality-layer-model`
- `work-handoff-contract-spec`
- `out-coverage-determinism`

## Review Cadence
Review this reference on a `quarterly` cadence or sooner when operating constraints materially change.
