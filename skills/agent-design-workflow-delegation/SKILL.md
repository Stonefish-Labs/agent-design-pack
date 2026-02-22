---
name: agent-design-workflow-delegation
description: Workflow decomposition and delegation consulting skill for deciding monolith vs staged handoffs, specifying subagent contracts, and designing isolation-broker patterns. Use when planning subagent boundaries, context budgeting, review gates, recovery paths, or delegation security rules.
---

# Agent Design Workflow Delegation

## Overview
Use this skill to design multi-stage agent workflows with explicit handoff contracts and controlled blast radius.

## First References to Load
1. `references/decomposition-heuristics.md`
2. `references/monolith-vs-staged-tradeoffs.md`
3. `references/handoff-contract-spec.md`

Load execution controls next:
- token and context economics: `references/context-budgeting.md`
- quality gates: `references/review-gate-patterns.md`
- resilience controls: `references/failure-isolation-and-recovery.md`
- isolation architecture: `references/ephemeral-isolation-pattern.md`
- broker specification: `references/guardian-broker-architecture.md`
- policy guardrails: `references/delegation-security-rules.md`

## Workflow
1. Identify natural phase boundaries and failure domains.
2. Choose monolithic or staged strategy per phase.
3. Define handoff contract schema and acceptance criteria.
4. Add review gates and recovery loops.
5. Validate delegation security and isolation controls.

## Cross-Skill Routing
- Runtime mechanism and secrets concerns: `../agent-design-tooling-security`.
- Architecture-spectrum migration concerns: `../agent-design-architecture`.
- Broad strategy and governance: `../agent-design-core`.

## References
- `references/decomposition-heuristics.md`
- `references/monolith-vs-staged-tradeoffs.md`
- `references/handoff-contract-spec.md`
- `references/context-budgeting.md`
- `references/review-gate-patterns.md`
- `references/failure-isolation-and-recovery.md`
- `references/ephemeral-isolation-pattern.md`
- `references/guardian-broker-architecture.md`
- `references/delegation-security-rules.md`
