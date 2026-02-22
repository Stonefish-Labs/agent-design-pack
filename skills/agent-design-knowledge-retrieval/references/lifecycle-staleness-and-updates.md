---
id: know-lifecycle-staleness-updates
title: "Lifecycle, Staleness, and Updates"
domain: knowledge-retrieval
kind: playbook
status: active
last_reviewed: 2026-02-22
update_cadence: monthly
tags:
  - lifecycle
  - staleness
  - maintenance
related:
  - know-index-enrichment-design
  - core-maintenance-playbook
  - core-source-coverage-matrix
---

# Lifecycle, Staleness, and Updates

## Intent
Manage update cadences, staleness detection, and re-index workflows for living corpora.

## Diagnostic Questions
- What assumption about update cadence is currently implicit and needs to be made explicit?
- Which constraint around staleness signal will break first under growth or stress?
- What evidence will prove that refresh automation is working in production, not just in demos?

## Recommended Moves
- Define a policy for update cadence before implementation choices are made.
- Attach measurable acceptance criteria to decisions about staleness signal.
- Add a review gate that validates refresh automation at release boundaries.
- Record rejected alternatives and why they were rejected to prevent decision drift.

## Failure Modes to Avoid
- Treating update cadence as static even when runtime constraints change.
- Optimizing for short-term speed while leaving staleness signal undefined.
- Assuming refresh automation without instrumented verification.

## Expected Deliverables
- A decision note that freezes the policy for update cadence.
- An execution checklist tied to staleness signal risk controls.
- A review artifact showing pass or fail evidence for refresh automation.

## Related References
- `know-index-enrichment-design`
- `core-maintenance-playbook`
- `core-source-coverage-matrix`

## Review Cadence
Review this reference on a `monthly` cadence or sooner when operating constraints materially change.
