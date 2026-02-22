---
id: toolsec-security-boundaries-consent
title: "Security Boundaries and Consent"
domain: tooling-security
kind: spec
status: active
last_reviewed: 2026-02-22
update_cadence: monthly
tags:
  - security
  - consent
  - boundaries
related:
  - toolsec-mcp-patterns
  - toolsec-hooks-patterns
  - work-delegation-security-rules
---

# Security Boundaries and Consent

## Intent
Specify hard and soft boundaries, approval flows, and risk-tiered escalation policy.

## Diagnostic Questions
- What assumption about trust boundary is currently implicit and needs to be made explicit?
- Which constraint around approval protocol will break first under growth or stress?
- What evidence will prove that audit trail is working in production, not just in demos?

## Recommended Moves
- Define a policy for trust boundary before implementation choices are made.
- Attach measurable acceptance criteria to decisions about approval protocol.
- Add a review gate that validates audit trail at release boundaries.
- Record rejected alternatives and why they were rejected to prevent decision drift.

## Specification
### Required Inputs
- Current-state description for trust boundary.
- Target-state constraints for approval protocol.
- Validation criteria for audit trail.
### Required Outputs
- Decision outcome with rationale and owner.
- Risk register with controls and escalation path.
- Verification plan with pass or fail evidence.

## Failure Modes to Avoid
- Treating trust boundary as static even when runtime constraints change.
- Optimizing for short-term speed while leaving approval protocol undefined.
- Assuming audit trail without instrumented verification.

## Expected Deliverables
- A decision note that freezes the policy for trust boundary.
- An execution checklist tied to approval protocol risk controls.
- A review artifact showing pass or fail evidence for audit trail.

## Related References
- `toolsec-mcp-patterns`
- `toolsec-hooks-patterns`
- `work-delegation-security-rules`

## Review Cadence
Review this reference on a `monthly` cadence or sooner when operating constraints materially change.
