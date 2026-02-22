---
id: toolsec-library-vs-cli-decision-guide
title: "Library vs CLI Decision Guide"
domain: tooling-security
kind: decision-matrix
status: active
last_reviewed: 2026-02-22
update_cadence: quarterly
tags:
  - library
  - cli
  - abstraction
related:
  - toolsec-native-tools-patterns
  - toolsec-security-boundaries-consent
  - toolsec-script-patterns
---

# Library vs CLI Decision Guide

## Intent
Prefer purpose-built libraries over broad CLI surfaces when reliability and least privilege matter.

## Diagnostic Questions
- What assumption about abstraction depth is currently implicit and needs to be made explicit?
- Which constraint around error surface will break first under growth or stress?
- What evidence will prove that credential control is working in production, not just in demos?

## Decision Matrix
| Signal | Prefer | Why |
|---|---|---|
| High uncertainty around abstraction depth | Use a staged approach with explicit gates | Keeps decision reversibility high while evidence matures |
| Tight delivery deadline with low risk around error surface | Use the simplest controlled path | Reduces overhead without dropping core safeguards |
| Expanding blast radius linked to credential control | Add formal policy and review checkpoints | Prevents silent drift and late-stage surprises |

## Recommended Moves
- Define a policy for abstraction depth before implementation choices are made.
- Attach measurable acceptance criteria to decisions about error surface.
- Add a review gate that validates credential control at release boundaries.
- Record rejected alternatives and why they were rejected to prevent decision drift.

## Failure Modes to Avoid
- Treating abstraction depth as static even when runtime constraints change.
- Optimizing for short-term speed while leaving error surface undefined.
- Assuming credential control without instrumented verification.

## Expected Deliverables
- A decision note that freezes the policy for abstraction depth.
- An execution checklist tied to error surface risk controls.
- A review artifact showing pass or fail evidence for credential control.

## Related References
- `toolsec-native-tools-patterns`
- `toolsec-security-boundaries-consent`
- `toolsec-script-patterns`

## Review Cadence
Review this reference on a `quarterly` cadence or sooner when operating constraints materially change.
