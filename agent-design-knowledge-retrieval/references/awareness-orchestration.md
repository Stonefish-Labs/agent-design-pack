---
id: know-awareness-orchestration
title: "Awareness Orchestration"
domain: knowledge-retrieval
kind: playbook
status: active
last_reviewed: 2026-02-22
update_cadence: quarterly
tags:
  - awareness
  - orchestration
  - coverage
related:
  - know-lookup-vs-discovery
  - know-index-enrichment-design
  - work-context-budgeting
---

# Awareness Orchestration

## Intent
Engineer prompt and workflow patterns that reliably trigger discovery behavior when stakes are high.

## Diagnostic Questions
- What assumption about awareness triggers is currently implicit and needs to be made explicit?
- Which constraint around context budget will break first under growth or stress?
- What evidence will prove that escalation rules is working in production, not just in demos?

## Recommended Moves
- Define a policy for awareness triggers before implementation choices are made.
- Attach measurable acceptance criteria to decisions about context budget.
- Add a review gate that validates escalation rules at release boundaries.
- Record rejected alternatives and why they were rejected to prevent decision drift.

## Failure Modes to Avoid
- Treating awareness triggers as static even when runtime constraints change.
- Optimizing for short-term speed while leaving context budget undefined.
- Assuming escalation rules without instrumented verification.

## Expected Deliverables
- A decision note that freezes the policy for awareness triggers.
- An execution checklist tied to context budget risk controls.
- A review artifact showing pass or fail evidence for escalation rules.

## Related References
- `know-lookup-vs-discovery`
- `know-index-enrichment-design`
- `work-context-budgeting`

## Review Cadence
Review this reference on a `quarterly` cadence or sooner when operating constraints materially change.
