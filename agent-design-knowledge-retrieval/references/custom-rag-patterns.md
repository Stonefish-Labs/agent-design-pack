---
id: know-custom-rag-patterns
title: "Custom RAG Patterns"
domain: knowledge-retrieval
kind: pattern
status: active
last_reviewed: 2026-02-22
update_cadence: quarterly
tags:
  - rag
  - ranking
  - chunking
related:
  - know-retrieval-approach-matrix
  - know-index-enrichment-design
  - out-factual-verification-patterns
---

# Custom RAG Patterns

## Intent
Apply custom retrieval pipelines when baseline methods cannot satisfy quality or scale requirements.

## Diagnostic Questions
- What assumption about retrieval tuning is currently implicit and needs to be made explicit?
- Which constraint around reranking policy will break first under growth or stress?
- What evidence will prove that evaluation loop is working in production, not just in demos?

## Recommended Moves
- Define a policy for retrieval tuning before implementation choices are made.
- Attach measurable acceptance criteria to decisions about reranking policy.
- Add a review gate that validates evaluation loop at release boundaries.
- Record rejected alternatives and why they were rejected to prevent decision drift.

## Failure Modes to Avoid
- Treating retrieval tuning as static even when runtime constraints change.
- Optimizing for short-term speed while leaving reranking policy undefined.
- Assuming evaluation loop without instrumented verification.

## Expected Deliverables
- A decision note that freezes the policy for retrieval tuning.
- An execution checklist tied to reranking policy risk controls.
- A review artifact showing pass or fail evidence for evaluation loop.

## Related References
- `know-retrieval-approach-matrix`
- `know-index-enrichment-design`
- `out-factual-verification-patterns`

## Review Cadence
Review this reference on a `quarterly` cadence or sooner when operating constraints materially change.
