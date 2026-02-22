# Agent Design Pack

Multi-skill Claude plugin for agent design: architecture, tooling & security, knowledge retrieval, workflow delegation, and output reliability.

## Structure (bundle layout)

- **skills/** — Six domain skills (agent-design-core, -architecture, -tooling-security, -knowledge-retrieval, -workflow-delegation, -output-reliability). Core is the router and governance entrypoint.
- **agents/** — `agent-design-router`: suite entrypoint agent that routes to the right domain and enforces governance.

## Usage

Install as a Claude Code plugin (e.g. `--plugin-dir ./agent-design-pack` or via marketplace). Use the **agent-design-router** agent or the **agent-design-core** skill as the entrypoint for broad or multi-domain requests.

## Archived sources

The `archived_sources/` directory holds the original reference documents from which the suite was derived. Kept in-repo for posterity and traceability; the live references live under each skill’s `references/`.

## License

MIT. See [LICENSE](LICENSE).
