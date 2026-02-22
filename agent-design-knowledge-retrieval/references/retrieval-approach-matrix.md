---
id: know-retrieval-approach-matrix
title: "Retrieval Approach Matrix"
domain: knowledge-retrieval
kind: decision-matrix
status: active
last_reviewed: 2026-02-22
update_cadence: quarterly
tags:
  - retrieval
  - rag
  - selection
related:
  - know-corpus-characterization
  - know-custom-rag-patterns
  - know-mcp-retrieval-architectures
---

# Retrieval Approach Matrix

## Intent
Choose full-context, indexed files, MCP search, or custom RAG based on corpus and operational constraints.

## Diagnostic Questions
- What assumption about approach selection is currently implicit and needs to be made explicit?
- Which constraint around scaling threshold will break first under growth or stress?
- What evidence will prove that operational overhead is working in production, not just in demos?

## Decision Matrix
| Signal | Prefer | Why |
|---|---|---|
| High uncertainty around approach selection | Use a staged approach with explicit gates | Keeps decision reversibility high while evidence matures |
| Tight delivery deadline with low risk around scaling threshold | Use the simplest controlled path | Reduces overhead without dropping core safeguards |
| Expanding blast radius linked to operational overhead | Add formal policy and review checkpoints | Prevents silent drift and late-stage surprises |

## Recommended Moves
- Define a policy for approach selection before implementation choices are made.
- Attach measurable acceptance criteria to decisions about scaling threshold.
- Add a review gate that validates operational overhead at release boundaries.
- Record rejected alternatives and why they were rejected to prevent decision drift.

## Failure Modes to Avoid
- Treating approach selection as static even when runtime constraints change.
- Optimizing for short-term speed while leaving scaling threshold undefined.
- Assuming operational overhead without instrumented verification.

## Expected Deliverables
- A decision note that freezes the policy for approach selection.
- An execution checklist tied to scaling threshold risk controls.
- A review artifact showing pass or fail evidence for operational overhead.

## Related References
- `know-corpus-characterization`
- `know-custom-rag-patterns`
- `know-mcp-retrieval-architectures`

## Review Cadence
Review this reference on a `quarterly` cadence or sooner when operating constraints materially change.
