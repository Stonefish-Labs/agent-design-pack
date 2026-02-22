---
id: toolsec-script-patterns
title: "Script Patterns"
domain: tooling-security
kind: pattern
status: active
last_reviewed: 2026-02-22
update_cadence: quarterly
tags:
  - scripts
  - self-contained
  - portability
related:
  - toolsec-tooling-selection-matrix
  - toolsec-secrets-configuration-patterns
  - core-maintenance-playbook
---

# Script Patterns

## Intent
Use scripts for portable, low-overhead capabilities where direct execution is acceptable.

## Diagnostic Questions
- What assumption about single-purpose scripts is currently implicit and needs to be made explicit?
- Which constraint around progressive disclosure will break first under growth or stress?
- What evidence will prove that deterministic output is working in production, not just in demos?

## Recommended Moves
- Define a policy for single-purpose scripts before implementation choices are made.
- Attach measurable acceptance criteria to decisions about progressive disclosure.
- Add a review gate that validates deterministic output at release boundaries.
- Record rejected alternatives and why they were rejected to prevent decision drift.

## Failure Modes to Avoid
- Treating single-purpose scripts as static even when runtime constraints change.
- Optimizing for short-term speed while leaving progressive disclosure undefined.
- Assuming deterministic output without instrumented verification.

## Expected Deliverables
- A decision note that freezes the policy for single-purpose scripts.
- An execution checklist tied to progressive disclosure risk controls.
- A review artifact showing pass or fail evidence for deterministic output.

## Related References
- `toolsec-tooling-selection-matrix`
- `toolsec-secrets-configuration-patterns`
- `core-maintenance-playbook`

## Review Cadence
Review this reference on a `quarterly` cadence or sooner when operating constraints materially change.
