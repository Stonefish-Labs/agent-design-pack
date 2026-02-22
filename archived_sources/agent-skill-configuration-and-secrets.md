---
id: agent-skill-configuration-and-secrets
title: "Agent Skills: Configuration and Secrets Management"
type: reference
scope: tooling
domain:
  - agent-development
  - architecture
  - security
stability: medium
intent: guide
tags:
  - skills
  - agent-scripts
  - secrets
  - configuration
  - secretstore
  - security
  - decision-framework
source: conversation
confidence: medium
created: 2026-02-15
---

# Agent Skills: Configuration and Secrets Management

Skills are stateless scripts. Each invocation may spawn a new shell, a new subagent, a new terminal. Environment variables set via `export` are scoped to the process tree that ran them — they don't survive across invocations.

MCP servers dodge this because they're persistent processes that hold their env for their lifetime. Skills have no such luxury. When a skill needs a secret — a webhook URL, an API key, a token — `os.getenv()` is a trap that works during manual testing and silently fails in production agentic workflows.

This document defines the standard pattern for how skills handle configuration and secrets reliably.

## The Process Boundary Problem

Consider a skill that sends Discord notifications. The MCP server version works fine with `DISCORD_WEBHOOK_URL` as an environment variable — the server starts once, reads the var, and holds it in memory for its lifetime. Convert that same logic to a skill script, and the env var must be present in whatever shell process the agent happens to invoke the script from.

That shell process might be:

- A fresh terminal spawned by a subagent
- A different terminal tab than the one where `export` was run
- A sandboxed execution environment with a clean env
- A CI/CD runner with no interactive history

In all of these cases, `export DISCORD_WEBHOOK_URL=...` from a previous session is gone. The skill fails with a cryptic "not set" error, and the agent either retries uselessly or asks the user to set the variable again — every single time.

This is not a bug in any specific skill. It's an architectural mismatch between how env vars work and how skills are invoked.

## The Pattern: secretstore with FileStorage

The `secretstore` library provides a backend-agnostic interface for storing and retrieving secrets. The **FileStorage** backend is the recommended default for skills:

```python
from secretstore import FileStorage

storage = FileStorage('my-skill')
storage.save('default', {'api_key': 'abc123', 'endpoint': 'https://...'})

# Later, in any process, any terminal, any agent invocation:
data = storage.get('default')
# {'api_key': 'abc123', 'endpoint': 'https://...'}
```

Secrets are stored as JSON at `~/.config/<service>/secrets.json` with `0600` file permissions and `0700` directory permissions. The location is:

- **Outside any project directory** — can't be accidentally committed to git
- **Persistent across processes** — survives terminal closures, agent restarts, machine reboots
- **XDG-compliant** — follows the `XDG_CONFIG_HOME` convention (defaults to `~/.config/`)
- **Runtime-agnostic** — works across Cursor, Claude Code, Codex, Roo, or any other agent runtime
- **Sandbox-safe** — no special permissions required, unlike system keychains

### Why Not the Other Backends?

| Backend | Problem for Skills |
|---------|--------------------|
| `EphemeralStorage` | Dies with the process — same failure mode as env vars |
| `EnvVarStorage` | Dies with the process — literally the problem we're solving |
| `KeyringStorage` | System keychains require elevated permissions; agents in sandboxed environments can't access them (documented in the github-publish skill's keychain issues) |
| `OnePasswordStorage` | Requires 1Password CLI and team setup — overkill for most skill configs |

`KeyringStorage` remains the upgrade path for users who want OS-level encryption at rest. But it can't be the *default* for skills because it fails in the exact environments skills run in most.

## Resolution Order

Skills that need secrets should resolve configuration in this order:

```
1. Environment variables     (highest priority — CI/CD, containers, one-off overrides)
2. Project pointer file      (.skill-profiles/<skill-name> → resolves a profile name)
3. FileStorage profile key   (secretstore get with the resolved profile name)
4. FileStorage 'default'     (fallback when no pointer file exists)
5. Error with instructions   (tell the agent how to set up the config)
```

This ordering means:

- **CI/CD and containers** can override everything with env vars — no config files needed in ephemeral environments
- **Per-project configuration** works via pointer files that reference named profiles
- **Single-project users** just need a `default` profile and nothing else
- **Failure is informative** — the error message tells the agent exactly what to do

### Per-Project Configuration via Profile Pointer Files

A single user-level config isn't always enough. Project A might notify `#deployments`, Project B might notify `#monitoring`. Same skill, different secrets.

The solution: **named profiles** stored user-level, selected per-project by a **pointer file** that contains zero secrets.

**Secrets live user-level** under named keys in `~/.config/<service>/secrets.json`:

```json
{
  "default": {"webhook_url": "https://discord.com/api/webhooks/aaa", "bot_name": "Agent"},
  "infra-alerts": {"webhook_url": "https://discord.com/api/webhooks/bbb", "bot_name": "Infra Bot"}
}
```

**Projects select a profile** via `.skill-profiles/<skill-name>` in the project root — a plain text file containing just the profile name (e.g., `infra-alerts`).

This pointer file is git-safe because it contains no sensitive data. It's actually *useful* to commit — teammates see which profile the project expects and can set up their own local secrets under the same profile name.

## Security Considerations

### File Permissions

`FileStorage` creates directories with `0700` and files with `0600` — owner-only access. This prevents other users on a shared system from reading your secrets. It does not protect against:

- Root access (nothing on a local filesystem does)
- Malware running as your user (same limitation as `.ssh/` keys, `.netrc`, etc.)
- Physical access to the machine

For the threat model skills operate in — local development machines, personal CI runners — this is appropriate. You're protecting against accidental exposure, not nation-state actors.

### Secrets Never in the Project Directory

The entire point of `~/.config/` as the storage location is that secrets live outside any git-tracked directory. Project pointer files reference profile *names*, never secret *values*. Even if `.skill-profiles/discord-notifier` is committed to a public repo, all it reveals is "this project uses a profile called `infra-alerts`." The webhook URL is safe.

### When to Upgrade to KeyringStorage

If your threat model requires encryption at rest — not just file permissions — swap `FileStorage` for `KeyringStorage` in the skill script. The `secretstore` interface is identical:

```python
# File-based (default for skills)
storage = FileStorage('my-skill')

# Keychain-based (encrypted at rest)
storage = KeyringStorage('my-skill')
```

This only works in unsandboxed environments where the system keychain is accessible.

## SKILL.md Conventions

Skills that need secrets should document a **Setup** section (not "Prerequisites") that tells the agent how to create the configuration on first run.

### Setup Section Template

```markdown
## Setup (one-time)

This skill stores configuration in `~/.config/<skill-name>/secrets.json` using `secretstore`.

To configure, create the secret store entry:

\```python
from secretstore import FileStorage
storage = FileStorage('<skill-name>')
storage.save('default', {
    'api_key': '<your-api-key>',
    'other_setting': '<value>'
})
\```

Or create the file manually:

\```bash
mkdir -p ~/.config/<skill-name>
cat > ~/.config/<skill-name>/secrets.json << 'EOF'
{
  "default": {
    "api_key": "<your-api-key>",
    "other_setting": "<value>"
  }
}
EOF
chmod 600 ~/.config/<skill-name>/secrets.json
\```

### Per-project profiles

To use a different configuration for this project, create a pointer file:

\```bash
mkdir -p .skill-profiles
echo "profile-name" > .skill-profiles/<skill-name>
\```

Then ensure the named profile exists in `~/.config/<skill-name>/secrets.json`.

### Environment variable override

For CI/CD or containers, set environment variables instead:

\```bash
export SKILL_SPECIFIC_VAR="value"
\```
```

### First-Run Agent Behavior

When a skill script detects no configuration (no env var, no pointer file, no stored secret), it should print a structured error that tells the agent what to do:

```
ERROR: discord-notifier not configured.
Run: FileStorage('discord-notifier').save('default', {'webhook_url': '<url>', 'bot_name': '<name>'})
Or create ~/.config/discord-notifier/secrets.json manually.
Ask the user for their Discord webhook URL.
```

The agent reads this, asks the user for the missing values, saves them via `secretstore`, and retries. This only happens once — subsequent invocations find the stored config and proceed.

## Dependency Management with uv

Skills that use `secretstore` should declare it via PEP 723 inline script metadata so `uv run` handles installation transparently:

```python
#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["secretstore"]
# ///
```

Invoked as `uv run scripts/my_script.py` — no manual `pip install`, no virtualenv management. The dependency is resolved and cached automatically.

For `secretstore` to be resolvable by `uv`, it needs to be published to PyPI or installed from a local/git path. Skills bundled in the same workspace as `secretstore` can use a path dependency:

```python
# /// script
# requires-python = ">=3.10"
# dependencies = ["secretstore @ file:///path/to/secretstore"]
# ///
```

Or, if `secretstore` is published:

```python
# /// script
# requires-python = ">=3.10"
# dependencies = ["secretstore>=0.1.0"]
# ///
```

## When This Pattern Isn't Enough

Use an MCP server instead of a skill script when:

- **Secrets need encrypted-at-rest storage** and the system keychain is available — an MCP server runs in a persistent, unsandboxed process where `KeyringStorage` works reliably
- **Multiple tools share the same authenticated session** — a persistent MCP process can hold a token and reuse it across calls without re-reading from storage every time
- **Credential rotation or refresh logic is needed** — OAuth refresh flows, token expiry checks, and automatic re-authentication are better served by a long-running process than a stateless script
- **The secret has a short TTL** — if the credential expires in minutes, reading it from disk on every invocation adds latency and complexity. A persistent process can cache and refresh transparently.

The decision framework in *Agent Tooling: Choosing the Right Mechanism* covers the full MCP vs. script tradeoff space. This document addresses only the configuration and secrets dimension of that decision.

## Reference Implementation

The `discord-notifier` skill implements this pattern. See:

- `discord-notifier/scripts/send_alert.py` — resolution order, PEP 723 metadata, error handling
- `discord-notifier/SKILL.md` — Setup section, profile documentation
