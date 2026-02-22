---
name: agent-design-output-reliability
description: Output reliability consulting skill for layering schema constraints, coverage determinism, factual verification, and rubric-based quality gates. Use when designing structured outputs, acceptance checks, quality scoring, or reliability guardrails for agent-generated artifacts.
---

# Agent Design Output Reliability

## Overview
Use this skill when teams need outputs that are not only parseable, but also complete, correct, and useful.

## First References to Load
1. `references/quality-layer-model.md`
2. `references/constrained-decoding-and-schema.md`
3. `references/coverage-determinism.md`

Load deeper controls as needed:
- factual validation: `references/factual-verification-patterns.md`
- rubric design: `references/rubric-evaluation-design.md`
- layer sequencing: `references/layer-composition-patterns.md`
- capability roadmapping: `references/model-capability-trajectory.md`
- known traps: `references/output-reliability-anti-patterns.md`
- execution checks: `references/qa-checklists.md`

## Workflow
1. Identify which quality layer is failing.
2. Apply the minimal control that closes that failure mode.
3. Compose controls in cost-aware sequence.
4. Define explicit acceptance thresholds.
5. Re-run anti-pattern and checklist review.

## Cross-Skill Routing
- Handoff schema and stage validation concerns: `../agent-design-workflow-delegation`.
- Retrieval-grounding quality concerns: `../agent-design-knowledge-retrieval`.
- Multi-domain strategy concerns: `../agent-design-core`.

## References
- `references/quality-layer-model.md`
- `references/constrained-decoding-and-schema.md`
- `references/coverage-determinism.md`
- `references/factual-verification-patterns.md`
- `references/rubric-evaluation-design.md`
- `references/layer-composition-patterns.md`
- `references/model-capability-trajectory.md`
- `references/output-reliability-anti-patterns.md`
- `references/qa-checklists.md`
