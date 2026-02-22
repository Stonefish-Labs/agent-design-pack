---
id: toolsec-runtime-capability-assessment
title: "Runtime Capability Assessment"
domain: tooling-security
kind: playbook
status: active
last_reviewed: 2026-02-22
update_cadence: quarterly
tags:
  - runtime
  - capabilities
  - assessment
related:
  - toolsec-tooling-selection-matrix
  - toolsec-native-tools-patterns
  - core-routing-playbook
---

# Runtime Capability Assessment

## Intent
Audit what native runtime capabilities already exist before adding custom tooling.

## Diagnostic Questions
- What assumption about native primitives is currently implicit and needs to be made explicit?
- Which constraint around capability gaps will break first under growth or stress?
- What evidence will prove that extension criteria is working in production, not just in demos?

## Recommended Moves
- Define a policy for native primitives before implementation choices are made.
- Attach measurable acceptance criteria to decisions about capability gaps.
- Add a review gate that validates extension criteria at release boundaries.
- Record rejected alternatives and why they were rejected to prevent decision drift.

## Failure Modes to Avoid
- Treating native primitives as static even when runtime constraints change.
- Optimizing for short-term speed while leaving capability gaps undefined.
- Assuming extension criteria without instrumented verification.

## Expected Deliverables
- A decision note that freezes the policy for native primitives.
- An execution checklist tied to capability gaps risk controls.
- A review artifact showing pass or fail evidence for extension criteria.

## Related References
- `toolsec-tooling-selection-matrix`
- `toolsec-native-tools-patterns`
- `core-routing-playbook`

## Review Cadence
Review this reference on a `quarterly` cadence or sooner when operating constraints materially change.
