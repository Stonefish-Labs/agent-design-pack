---
id: core-source-coverage-matrix
title: "Source Coverage Matrix"
domain: core
kind: spec
status: active
last_reviewed: 2026-02-22
update_cadence: on-change
tags:
  - coverage
  - traceability
  - quality-gate
related:
  - core-maintenance-playbook
  - core-governance-model
  - core-editorial-standards
---

# Source Coverage Matrix

## Purpose
Track major source sections and confirm each section is represented in the rewritten suite.

## Rules
- Keep one row per source document H2 section.
- Keep `status` as `covered` when mapped and reviewed.
- Use coverage gate automation to detect missing rows or unresolved mappings.

## Coverage Table
| source_doc | section | mapped_ref | status | notes |
|---|---|---|---|---|
| agent-architecture-spectrum-programmatic-vs-agentic-vs-autonomous.md | The Spectrum | arch-spectrum-model | covered | Consolidated into rewritten suite reference. |
| agent-architecture-spectrum-programmatic-vs-agentic-vs-autonomous.md | The Key Architectural Axes | arch-orchestration-authority | covered | Consolidated into rewritten suite reference. |
| agent-architecture-spectrum-programmatic-vs-agentic-vs-autonomous.md | The Infrastructure Convergence | arch-infrastructure-convergence | covered | Consolidated into rewritten suite reference. |
| agent-architecture-spectrum-programmatic-vs-agentic-vs-autonomous.md | Decision Heuristics | arch-decision-matrix | covered | Consolidated into rewritten suite reference. |
| agent-architecture-spectrum-programmatic-vs-agentic-vs-autonomous.md | The Skills and Decentralized Stack Pattern | arch-control-surface-design | covered | Consolidated into rewritten suite reference. |
| agent-architecture-spectrum-programmatic-vs-agentic-vs-autonomous.md | Migrating Between Categories | arch-migration-playbooks | covered | Consolidated into rewritten suite reference. |
| agent-architecture-spectrum-programmatic-vs-agentic-vs-autonomous.md | Anti-Patterns | arch-anti-patterns | covered | Consolidated into rewritten suite reference. |
| agent-architecture-spectrum-programmatic-vs-agentic-vs-autonomous.md | The Core Design Principle | arch-decision-matrix | covered | Consolidated into rewritten suite reference. |
| agent-knowledge-architecture-retrieval-patterns.md | Understand Your Corpus | know-corpus-characterization | covered | Consolidated into rewritten suite reference. |
| agent-knowledge-architecture-retrieval-patterns.md | The Two Retrieval Problems | know-lookup-vs-discovery | covered | Consolidated into rewritten suite reference. |
| agent-knowledge-architecture-retrieval-patterns.md | Decision Heuristics | know-retrieval-approach-matrix | covered | Consolidated into rewritten suite reference. |
| agent-knowledge-architecture-retrieval-patterns.md | Full Context Injection | know-retrieval-approach-matrix | covered | Consolidated into rewritten suite reference. |
| agent-knowledge-architecture-retrieval-patterns.md | Index + On-Demand Retrieval (Files) | know-retrieval-approach-matrix | covered | Consolidated into rewritten suite reference. |
| agent-knowledge-architecture-retrieval-patterns.md | Service Resilience | know-corpus-characterization | covered | Consolidated into rewritten suite reference. |
| agent-knowledge-architecture-retrieval-patterns.md | MCP Search Server | know-mcp-retrieval-architectures | covered | Consolidated into rewritten suite reference. |
| agent-knowledge-architecture-retrieval-patterns.md | Custom RAG Pipeline | know-custom-rag-patterns | covered | Consolidated into rewritten suite reference. |
| agent-knowledge-architecture-retrieval-patterns.md | Enriched Documents: The Layer That Matters Most | know-index-enrichment-design | covered | Consolidated into rewritten suite reference. |
| agent-knowledge-architecture-retrieval-patterns.md | Orchestrating Discovery | know-awareness-orchestration | covered | Consolidated into rewritten suite reference. |
| agent-knowledge-architecture-retrieval-patterns.md | Tiered Architecture for Production | know-corpus-characterization | covered | Consolidated into rewritten suite reference. |
| agent-knowledge-architecture-retrieval-patterns.md | Maintenance and Lifecycle | know-lifecycle-staleness-updates | covered | Consolidated into rewritten suite reference. |
| agent-knowledge-architecture-retrieval-patterns.md | Scaling Inflection Points | know-scaling-inflection-playbook | covered | Consolidated into rewritten suite reference. |
| agent-knowledge-architecture-retrieval-patterns.md | Portability Across Agent Runtimes | know-corpus-characterization | covered | Consolidated into rewritten suite reference. |
| agent-knowledge-architecture-retrieval-patterns.md | The Core Design Principle | know-retrieval-approach-matrix | covered | Consolidated into rewritten suite reference. |
| agent-skill-configuration-and-secrets.md | The Process Boundary Problem | toolsec-secrets-configuration-patterns | covered | Consolidated into rewritten suite reference. |
| agent-skill-configuration-and-secrets.md | The Pattern: secretstore with FileStorage | toolsec-secrets-configuration-patterns | covered | Consolidated into rewritten suite reference. |
| agent-skill-configuration-and-secrets.md | Resolution Order | toolsec-secrets-configuration-patterns | covered | Consolidated into rewritten suite reference. |
| agent-skill-configuration-and-secrets.md | Security Considerations | toolsec-security-boundaries-consent | covered | Consolidated into rewritten suite reference. |
| agent-skill-configuration-and-secrets.md | SKILL.md Conventions | toolsec-secrets-configuration-patterns | covered | Consolidated into rewritten suite reference. |
| agent-skill-configuration-and-secrets.md | Setup (one-time) | toolsec-secrets-configuration-patterns | covered | Consolidated into rewritten suite reference. |
| agent-skill-configuration-and-secrets.md | Dependency Management with uv | toolsec-script-patterns | covered | Consolidated into rewritten suite reference. |
| agent-skill-configuration-and-secrets.md | When This Pattern Isn't Enough | toolsec-secrets-configuration-patterns | covered | Consolidated into rewritten suite reference. |
| agent-skill-configuration-and-secrets.md | Reference Implementation | toolsec-secrets-configuration-patterns | covered | Consolidated into rewritten suite reference. |
| agent-tooling-design-philosophy.md | The Question | toolsec-library-vs-cli-decision-guide | covered | Consolidated into rewritten suite reference. |
| agent-tooling-design-philosophy.md | The Core Principle | toolsec-library-vs-cli-decision-guide | covered | Consolidated into rewritten suite reference. |
| agent-tooling-design-philosophy.md | Security | toolsec-security-boundaries-consent | covered | Consolidated into rewritten suite reference. |
| agent-tooling-design-philosophy.md | Efficiency | toolsec-native-tools-patterns | covered | Consolidated into rewritten suite reference. |
| agent-tooling-design-philosophy.md | Portability and Operations | toolsec-tooling-selection-matrix | covered | Consolidated into rewritten suite reference. |
| agent-tooling-design-philosophy.md | Flexibility and Control | toolsec-mcp-patterns | covered | Consolidated into rewritten suite reference. |
| agent-tooling-design-philosophy.md | When CLI Tools Do Make Sense | toolsec-library-vs-cli-decision-guide | covered | Consolidated into rewritten suite reference. |
| agent-tooling-design-philosophy.md | Summary | toolsec-library-vs-cli-decision-guide | covered | Consolidated into rewritten suite reference. |
| agent-tooling-mcp-vs-scripts-vs-hooks.md | Know Your Runtime | toolsec-runtime-capability-assessment | covered | Consolidated into rewritten suite reference. |
| agent-tooling-mcp-vs-scripts-vs-hooks.md | Decision Heuristics | toolsec-tooling-selection-matrix | covered | Consolidated into rewritten suite reference. |
| agent-tooling-mcp-vs-scripts-vs-hooks.md | When to Use Hooks | toolsec-hooks-patterns | covered | Consolidated into rewritten suite reference. |
| agent-tooling-mcp-vs-scripts-vs-hooks.md | When to Use MCP Servers | toolsec-mcp-patterns | covered | Consolidated into rewritten suite reference. |
| agent-tooling-mcp-vs-scripts-vs-hooks.md | When to Use Agent-Executed Scripts | toolsec-script-patterns | covered | Consolidated into rewritten suite reference. |
| agent-tooling-mcp-vs-scripts-vs-hooks.md | Security Boundaries: Hard vs. Soft Enforcement | toolsec-security-boundaries-consent | covered | Consolidated into rewritten suite reference. |
| agent-tooling-mcp-vs-scripts-vs-hooks.md | Hybrid Layering | toolsec-tooling-selection-matrix | covered | Consolidated into rewritten suite reference. |
| agent-tooling-mcp-vs-scripts-vs-hooks.md | Coupling, Scope, and Portability | toolsec-tooling-selection-matrix | covered | Consolidated into rewritten suite reference. |
| agent-workflow-decomposition-subagent-delegation.md | Decision Heuristics | work-decomposition-heuristics | covered | Consolidated into rewritten suite reference. |
| agent-workflow-decomposition-subagent-delegation.md | Monolithic Agent | work-monolith-vs-staged-tradeoffs | covered | Consolidated into rewritten suite reference. |
| agent-workflow-decomposition-subagent-delegation.md | Staged Handoffs | work-monolith-vs-staged-tradeoffs | covered | Consolidated into rewritten suite reference. |
| agent-workflow-decomposition-subagent-delegation.md | The Handoff Contract | work-handoff-contract-spec | covered | Consolidated into rewritten suite reference. |
| agent-workflow-decomposition-subagent-delegation.md | Required Fields | work-decomposition-heuristics | covered | Consolidated into rewritten suite reference. |
| agent-workflow-decomposition-subagent-delegation.md | Optional Fields | work-decomposition-heuristics | covered | Consolidated into rewritten suite reference. |
| agent-workflow-decomposition-subagent-delegation.md | Context Budget | work-context-budgeting | covered | Consolidated into rewritten suite reference. |
| agent-workflow-decomposition-subagent-delegation.md | Reusability and Entry Points | work-decomposition-heuristics | covered | Consolidated into rewritten suite reference. |
| agent-workflow-decomposition-subagent-delegation.md | Error Handling and Resilience | work-failure-isolation-recovery | covered | Consolidated into rewritten suite reference. |
| agent-workflow-decomposition-subagent-delegation.md | The Review/Quality Gate Pattern | work-review-gate-patterns | covered | Consolidated into rewritten suite reference. |
| agent-workflow-decomposition-subagent-delegation.md | Cost and Complexity Tradeoffs | work-monolith-vs-staged-tradeoffs | covered | Consolidated into rewritten suite reference. |
| agent-workflow-decomposition-subagent-delegation.md | Anti-Patterns | work-delegation-security-rules | covered | Consolidated into rewritten suite reference. |
| agent-workflow-decomposition-subagent-delegation.md | Agent Teams — Explicit Non-Scope | work-decomposition-heuristics | covered | Consolidated into rewritten suite reference. |
| agent-workflow-decomposition-subagent-delegation.md | The Core Design Principle | work-decomposition-heuristics | covered | Consolidated into rewritten suite reference. |
| ephemeral-agent-design-pattern.md | Overview | work-ephemeral-isolation-pattern | covered | Consolidated into rewritten suite reference. |
| ephemeral-agent-design-pattern.md | Core Concepts | work-ephemeral-isolation-pattern | covered | Consolidated into rewritten suite reference. |
| ephemeral-agent-design-pattern.md | The Execution Lifecycle | work-guardian-broker-architecture | covered | Consolidated into rewritten suite reference. |
| ephemeral-agent-design-pattern.md | Advanced Rules: Delegation, Inheritance, and Networking | work-delegation-security-rules | covered | Consolidated into rewritten suite reference. |
| ephemeral-agent-design-pattern.md | Threat Model: Handling Indirect Prompt Injection | work-delegation-security-rules | covered | Consolidated into rewritten suite reference. |
| ephemeral-agent-design-pattern.md | Security, Performance, & Reliability Benefits | work-failure-isolation-recovery | covered | Consolidated into rewritten suite reference. |
| output-determinism-structured-vs-freeform-vs-rubric.md | The Four Layers of Output Quality | out-quality-layer-model | covered | Consolidated into rewritten suite reference. |
| output-determinism-structured-vs-freeform-vs-rubric.md | Constrained Decoding and Structured Outputs | out-constrained-decoding-schema | covered | Consolidated into rewritten suite reference. |
| output-determinism-structured-vs-freeform-vs-rubric.md | Free Generation with Post-Hoc Handling | out-layer-composition-patterns | covered | Consolidated into rewritten suite reference. |
| output-determinism-structured-vs-freeform-vs-rubric.md | Rubric-Based Evaluation | out-rubric-evaluation-design | covered | Consolidated into rewritten suite reference. |
| output-determinism-structured-vs-freeform-vs-rubric.md | Decision Heuristics | out-qa-checklists | covered | Consolidated into rewritten suite reference. |
| output-determinism-structured-vs-freeform-vs-rubric.md | Composing the Layers | out-layer-composition-patterns | covered | Consolidated into rewritten suite reference. |
| output-determinism-structured-vs-freeform-vs-rubric.md | The Model Capability Trajectory | out-model-capability-trajectory | covered | Consolidated into rewritten suite reference. |
| output-determinism-structured-vs-freeform-vs-rubric.md | Anti-Patterns | out-output-reliability-anti-patterns | covered | Consolidated into rewritten suite reference. |
| output-determinism-structured-vs-freeform-vs-rubric.md | The Core Design Principle | out-quality-layer-model | covered | Consolidated into rewritten suite reference. |

Total mapped sections: **77**.
