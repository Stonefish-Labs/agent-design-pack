---
id: work-guardian-broker-architecture
title: "Guardian Broker Architecture"
domain: workflow-delegation
kind: spec
status: active
last_reviewed: 2026-02-22
update_cadence: quarterly
tags:
  - guardian
  - broker
  - provisioning
related:
  - work-ephemeral-isolation-pattern
  - work-delegation-security-rules
  - toolsec-mcp-patterns
---

# Guardian Broker Architecture

## Intent
Specify broker responsibilities for approval, provisioning, credential injection, routing, and teardown.

## Diagnostic Questions
- What assumption about approval interception is currently implicit and needs to be made explicit?
- Which constraint around provisioning control will break first under growth or stress?
- What evidence will prove that audit events is working in production, not just in demos?

## Recommended Moves
- Define a policy for approval interception before implementation choices are made.
- Attach measurable acceptance criteria to decisions about provisioning control.
- Add a review gate that validates audit events at release boundaries.
- Record rejected alternatives and why they were rejected to prevent decision drift.

## Specification
### Required Inputs
- Current-state description for approval interception.
- Target-state constraints for provisioning control.
- Validation criteria for audit events.
### Required Outputs
- Decision outcome with rationale and owner.
- Risk register with controls and escalation path.
- Verification plan with pass or fail evidence.

## Failure Modes to Avoid
- Treating approval interception as static even when runtime constraints change.
- Optimizing for short-term speed while leaving provisioning control undefined.
- Assuming audit events without instrumented verification.

## Expected Deliverables
- A decision note that freezes the policy for approval interception.
- An execution checklist tied to provisioning control risk controls.
- A review artifact showing pass or fail evidence for audit events.

## Related References
- `work-ephemeral-isolation-pattern`
- `work-delegation-security-rules`
- `toolsec-mcp-patterns`

## Review Cadence
Review this reference on a `quarterly` cadence or sooner when operating constraints materially change.
