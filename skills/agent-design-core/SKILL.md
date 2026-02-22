---
name: agent-design-core
description: Router and governance skill for the agent-design suite. Use when the request spans multiple agent-design domains, when deciding which domain skill(s) to invoke first, when enforcing suite-wide standards, or when maintaining the living knowledgebase quality gates and coverage controls.
---

# Agent Design Core

## Overview
Use this skill as the suite entrypoint for broad strategy prompts, cross-domain architecture consulting, and governance operations.

## Co-Installed Suite Assumption
Assume sibling skills are installed in the same parent directory:
- `../agent-design-architecture`
- `../agent-design-tooling-security`
- `../agent-design-knowledge-retrieval`
- `../agent-design-workflow-delegation`
- `../agent-design-output-reliability`

If any sibling is missing, continue with available skills and report the gap.

## Routing Workflow
1. Classify the prompt using `references/taxonomy.md`.
2. Apply routing criteria from `references/routing-playbook.md`.
3. Select one primary domain skill and optional secondary skill.
4. Hand off with explicit scope, assumptions, and expected artifact.
5. Run governance checks before final delivery.

## Routing Guide
- Architecture scope, orchestration authority, migration path: route to `../agent-design-architecture`.
- Tooling mechanism choice, security boundary design, secrets policy: route to `../agent-design-tooling-security`.
- Retrieval architecture, corpus indexing, awareness design: route to `../agent-design-knowledge-retrieval`.
- Decomposition, subagent handoff, isolation broker pattern: route to `../agent-design-workflow-delegation`.
- Output quality controls, schema constraints, rubric design: route to `../agent-design-output-reliability`.

## Governance Gates
Before finalizing any recommendation:
1. Check terminology consistency with `references/glossary.md`.
2. Check decision logic against `references/decision-axes.md`.
3. Check pattern hygiene against `references/pattern-catalog.md` and `references/anti-pattern-catalog.md`.
4. Verify coverage updates in `references/source-coverage-matrix.md` if source-derived material changed.

## Maintenance Commands
Use helper scripts in `scripts/` from the bundle root (parent of `skills/`). Pass the bundle root as `--suite-root`:
- `python3 skills/agent-design-core/scripts/lint_frontmatter.py --suite-root .`
- `python3 skills/agent-design-core/scripts/check_links.py --suite-root .`
- `python3 skills/agent-design-core/scripts/coverage_gate.py --source-pack ./design-considerations-pack --suite-root . --fail-on-missing`

## Reference Index
- `references/taxonomy.md`
- `references/glossary.md`
- `references/decision-axes.md`
- `references/pattern-catalog.md`
- `references/anti-pattern-catalog.md`
- `references/routing-playbook.md`
- `references/governance-model.md`
- `references/editorial-standards.md`
- `references/maintenance-playbook.md`
- `references/source-coverage-matrix.md`
