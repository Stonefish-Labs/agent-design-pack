---
name: agent-design-tooling-security
description: Tooling and security consulting skill for selecting native tools, hooks, MCP, or scripts with explicit security boundaries and secrets strategy. Use when designing agent tool interfaces, permission models, consent gating, or durable configuration and secret handling.
---

# Agent Design Tooling Security

## Overview
Use this skill when the key decision is how an agent should access capabilities safely and reliably.

## First References to Load
1. `references/runtime-capability-assessment.md`
2. `references/tooling-selection-matrix.md`
3. `references/security-boundaries-and-consent.md`

Load mechanism-specific references after mechanism selection:
- native capabilities: `references/native-tools-patterns.md`
- event automation: `references/hooks-patterns.md`
- typed remote interfaces: `references/mcp-patterns.md`
- portable local logic: `references/script-patterns.md`

## Workflow
1. Inventory runtime-native capabilities before building custom tooling.
2. Select mechanism using the tooling matrix.
3. Define boundary enforcement and consent protocol.
4. Define secret and config lifecycle.
5. Validate against library-vs-CLI guidance and anti-drift controls.

## Cross-Skill Routing
- Retrieval-service architecture concerns: `../agent-design-knowledge-retrieval`.
- Delegation security and broker concerns: `../agent-design-workflow-delegation`.
- Broad multi-domain consulting: `../agent-design-core`.

## References
- `references/runtime-capability-assessment.md`
- `references/tooling-selection-matrix.md`
- `references/native-tools-patterns.md`
- `references/hooks-patterns.md`
- `references/mcp-patterns.md`
- `references/script-patterns.md`
- `references/library-vs-cli-decision-guide.md`
- `references/security-boundaries-and-consent.md`
- `references/secrets-and-configuration-patterns.md`
