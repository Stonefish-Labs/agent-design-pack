---
id: toolsec-mcp-patterns
title: "MCP Patterns"
domain: tooling-security
kind: pattern
status: active
last_reviewed: 2026-02-22
update_cadence: quarterly
tags:
  - mcp
  - servers
  - typed-tools
related:
  - toolsec-tooling-selection-matrix
  - toolsec-security-boundaries-consent
  - know-mcp-retrieval-architectures
---

# MCP Patterns

## Intent
Design MCP servers for typed interfaces, policy enforcement, and shared multi-agent access.

## Diagnostic Questions
- What assumption about schema contracts is currently implicit and needs to be made explicit?
- Which constraint around permission mediation will break first under growth or stress?
- What evidence will prove that remote boundary design is working in production, not just in demos?

## Recommended Moves
- Define a policy for schema contracts before implementation choices are made.
- Attach measurable acceptance criteria to decisions about permission mediation.
- Add a review gate that validates remote boundary design at release boundaries.
- Record rejected alternatives and why they were rejected to prevent decision drift.

## Failure Modes to Avoid
- Treating schema contracts as static even when runtime constraints change.
- Optimizing for short-term speed while leaving permission mediation undefined.
- Assuming remote boundary design without instrumented verification.

## Expected Deliverables
- A decision note that freezes the policy for schema contracts.
- An execution checklist tied to permission mediation risk controls.
- A review artifact showing pass or fail evidence for remote boundary design.

## Related References
- `toolsec-tooling-selection-matrix`
- `toolsec-security-boundaries-consent`
- `know-mcp-retrieval-architectures`

## Review Cadence
Review this reference on a `quarterly` cadence or sooner when operating constraints materially change.
