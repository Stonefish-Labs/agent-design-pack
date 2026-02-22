---
id: know-mcp-retrieval-architectures
title: "MCP Retrieval Architectures"
domain: knowledge-retrieval
kind: pattern
status: active
last_reviewed: 2026-02-22
update_cadence: quarterly
tags:
  - mcp
  - retrieval
  - shared-services
related:
  - know-retrieval-approach-matrix
  - toolsec-mcp-patterns
  - core-governance-model
---

# MCP Retrieval Architectures

## Intent
Use MCP-based retrieval when teams need shared searchable corpora and centralized controls.

## Diagnostic Questions
- What assumption about service interface is currently implicit and needs to be made explicit?
- Which constraint around query mediation will break first under growth or stress?
- What evidence will prove that shared lifecycle is working in production, not just in demos?

## Recommended Moves
- Define a policy for service interface before implementation choices are made.
- Attach measurable acceptance criteria to decisions about query mediation.
- Add a review gate that validates shared lifecycle at release boundaries.
- Record rejected alternatives and why they were rejected to prevent decision drift.

## Failure Modes to Avoid
- Treating service interface as static even when runtime constraints change.
- Optimizing for short-term speed while leaving query mediation undefined.
- Assuming shared lifecycle without instrumented verification.

## Expected Deliverables
- A decision note that freezes the policy for service interface.
- An execution checklist tied to query mediation risk controls.
- A review artifact showing pass or fail evidence for shared lifecycle.

## Related References
- `know-retrieval-approach-matrix`
- `toolsec-mcp-patterns`
- `core-governance-model`

## Review Cadence
Review this reference on a `quarterly` cadence or sooner when operating constraints materially change.
