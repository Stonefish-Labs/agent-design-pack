---
id: toolsec-tooling-selection-matrix
title: "Tooling Selection Matrix"
domain: tooling-security
kind: decision-matrix
status: active
last_reviewed: 2026-02-22
update_cadence: quarterly
tags:
  - tooling
  - selection
  - tradeoffs
related:
  - toolsec-runtime-capability-assessment
  - toolsec-mcp-patterns
  - toolsec-script-patterns
---

# Tooling Selection Matrix

## Intent
Choose between native tools, hooks, MCP, and scripts with explicit security and portability criteria.

## Diagnostic Questions
- What assumption about mechanism choice is currently implicit and needs to be made explicit?
- Which constraint around enforcement boundary will break first under growth or stress?
- What evidence will prove that portability target is working in production, not just in demos?

## Decision Matrix
| Signal | Prefer | Why |
|---|---|---|
| High uncertainty around mechanism choice | Use a staged approach with explicit gates | Keeps decision reversibility high while evidence matures |
| Tight delivery deadline with low risk around enforcement boundary | Use the simplest controlled path | Reduces overhead without dropping core safeguards |
| Expanding blast radius linked to portability target | Add formal policy and review checkpoints | Prevents silent drift and late-stage surprises |

## Recommended Moves
- Define a policy for mechanism choice before implementation choices are made.
- Attach measurable acceptance criteria to decisions about enforcement boundary.
- Add a review gate that validates portability target at release boundaries.
- Record rejected alternatives and why they were rejected to prevent decision drift.

## Failure Modes to Avoid
- Treating mechanism choice as static even when runtime constraints change.
- Optimizing for short-term speed while leaving enforcement boundary undefined.
- Assuming portability target without instrumented verification.

## Expected Deliverables
- A decision note that freezes the policy for mechanism choice.
- An execution checklist tied to enforcement boundary risk controls.
- A review artifact showing pass or fail evidence for portability target.

## Related References
- `toolsec-runtime-capability-assessment`
- `toolsec-mcp-patterns`
- `toolsec-script-patterns`

## Review Cadence
Review this reference on a `quarterly` cadence or sooner when operating constraints materially change.
