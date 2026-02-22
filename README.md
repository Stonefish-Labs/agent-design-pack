# Agent Design Pack

Multi-skill Claude plugin for agent design: architecture, tooling & security, knowledge retrieval, workflow delegation, and output reliability.

## Skills

- **agent-design-core** — Router and governance; suite entrypoint and cross-domain strategy.
- **agent-design-architecture** — Spectrum model, orchestration authority, migration, termination.
- **agent-design-tooling-security** — Tooling boundaries, MCP/scripts/hooks, secrets, consent.
- **agent-design-knowledge-retrieval** — RAG, indexing, awareness, lookup vs discovery.
- **agent-design-workflow-delegation** — Decomposition, subagent handoff, broker pattern, isolation.
- **agent-design-output-reliability** — Schemas, rubrics, verification, quality layers.

## Usage

Install as a Claude Code plugin (e.g. `--plugin-dir ./agent-design-pack` or via marketplace). Use **agent-design-core** as the entrypoint for broad or multi-domain requests.

## Archived sources

The `archived_sources/` directory holds the original reference documents from which the suite was derived. Kept in-repo for posterity and traceability; the live references live under each skill’s `references/`.

## License

MIT. See [LICENSE](LICENSE).
