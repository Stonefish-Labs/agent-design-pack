---
name: agent-design-knowledge-retrieval
description: Knowledge and retrieval consulting skill for corpus design, retrieval architecture selection, awareness orchestration, and staleness management. Use when designing file indexes, MCP retrieval services, custom RAG pipelines, or long-term knowledgebase maintenance.
---

# Agent Design Knowledge Retrieval

## Overview
Use this skill when agent answer quality depends on retrieval architecture, corpus structure, and discovery behavior.

## First References to Load
1. `references/corpus-characterization.md`
2. `references/lookup-vs-discovery.md`
3. `references/retrieval-approach-matrix.md`

Then load implementation details:
- metadata strategy: `references/index-and-enrichment-design.md`
- awareness controls: `references/awareness-orchestration.md`
- shared retrieval service: `references/mcp-retrieval-architectures.md`
- custom pipeline tuning: `references/custom-rag-patterns.md`
- lifecycle operations: `references/lifecycle-staleness-and-updates.md`

## Workflow
1. Characterize corpus type, authority model, and update velocity.
2. Separate lookup and discovery requirements.
3. Select baseline retrieval architecture.
4. Design enrichment and awareness orchestration.
5. Define lifecycle and scaling triggers.

## Cross-Skill Routing
- Tooling boundary and permission-model questions: `../agent-design-tooling-security`.
- Output verification controls for retrieved claims: `../agent-design-output-reliability`.
- Mixed strategy prompts: `../agent-design-core`.

## References
- `references/corpus-characterization.md`
- `references/lookup-vs-discovery.md`
- `references/retrieval-approach-matrix.md`
- `references/index-and-enrichment-design.md`
- `references/awareness-orchestration.md`
- `references/mcp-retrieval-architectures.md`
- `references/custom-rag-patterns.md`
- `references/lifecycle-staleness-and-updates.md`
- `references/scaling-inflection-playbook.md`
