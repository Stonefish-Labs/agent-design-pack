---
id: know-lookup-vs-discovery
title: "Lookup vs Discovery"
domain: knowledge-retrieval
kind: concept
status: active
last_reviewed: 2026-02-22
update_cadence: quarterly
tags:
  - lookup
  - discovery
  - awareness
related:
  - know-awareness-orchestration
  - know-retrieval-approach-matrix
  - core-decision-axes
---

# Lookup vs Discovery

## Intent
Separate search quality from awareness quality to prevent blind spots in retrieval design.

## Diagnostic Questions
- What assumption about known-needed retrieval is currently implicit and needs to be made explicit?
- Which constraint around unknown-needed discovery will break first under growth or stress?
- What evidence will prove that awareness policy is working in production, not just in demos?

## Recommended Moves
- Define a policy for known-needed retrieval before implementation choices are made.
- Attach measurable acceptance criteria to decisions about unknown-needed discovery.
- Add a review gate that validates awareness policy at release boundaries.
- Record rejected alternatives and why they were rejected to prevent decision drift.

## Failure Modes to Avoid
- Treating known-needed retrieval as static even when runtime constraints change.
- Optimizing for short-term speed while leaving unknown-needed discovery undefined.
- Assuming awareness policy without instrumented verification.

## Expected Deliverables
- A decision note that freezes the policy for known-needed retrieval.
- An execution checklist tied to unknown-needed discovery risk controls.
- A review artifact showing pass or fail evidence for awareness policy.

## Related References
- `know-awareness-orchestration`
- `know-retrieval-approach-matrix`
- `core-decision-axes`

## Review Cadence
Review this reference on a `quarterly` cadence or sooner when operating constraints materially change.
