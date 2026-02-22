---
name: agent-design-architecture
description: Architecture consulting skill for choosing and evolving agent system topology across programmatic, assistant, and autonomous models. Use when deciding orchestration authority, termination logic, control surfaces, migration paths, or architecture anti-pattern mitigations.
---

# Agent Design Architecture

## Overview
Use this skill for architecture-level decisions about control ownership, runtime model, recovery strategy, and migration.

## First References to Load
1. `references/spectrum-model.md`
2. `references/decision-matrix.md`
3. `references/anti-patterns.md`

Load specialized references based on the active question:
- orchestration owner: `references/orchestration-authority.md`
- completion and rollback: `references/termination-and-recovery.md`
- state model: `references/session-and-state-models.md`
- approval and control points: `references/control-surface-design.md`
- migration planning: `references/migration-playbooks.md`

## Workflow
1. Place current state on the architecture spectrum.
2. Evaluate with the decision matrix.
3. Propose target state and migration sequence.
4. Attach explicit ownership, termination, and recovery controls.
5. Run anti-pattern checks before finalizing.

## Cross-Skill Routing
- If tooling boundary choices dominate, route to `../agent-design-tooling-security`.
- If workflow decomposition and subagent contracts dominate, route to `../agent-design-workflow-delegation`.
- If output quality controls dominate, route to `../agent-design-output-reliability`.
- For mixed requests, use `../agent-design-core` for orchestration.

## References
- `references/spectrum-model.md`
- `references/orchestration-authority.md`
- `references/termination-and-recovery.md`
- `references/session-and-state-models.md`
- `references/control-surface-design.md`
- `references/infrastructure-convergence.md`
- `references/migration-playbooks.md`
- `references/decision-matrix.md`
- `references/anti-patterns.md`
