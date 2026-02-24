# Skill Configuration Conventions

This document describes the standard approach for storing non-sensitive configuration options in agent skills. It is provider-agnostic and works across Claude Code, Cursor, RooCode, Codex, Copilot, and any other agent environment.

## Core Principle

Skill configuration does not belong in version control by default, and it does not belong in any provider-specific config system. It belongs in the OS-standard config locations (XDG) for machine-wide settings, and in a gitignored project directory for project-scoped settings.

> **Secrets are a separate concern.** This document covers non-sensitive configuration only (paths, preferences, formats, toggles). Secrets belong in a secrets manager or environment variables — never in skill config files.

---

## Machine-Wide Configuration

Use the [XDG Base Directory Specification](https://specifications.freedesktop.org/basedir-spec/latest/) for config that should apply everywhere the skill runs on this machine.

**Location:** `$XDG_CONFIG_HOME/<skill-name>/config.json`

On most systems this resolves to:
- Linux/macOS: `~/.config/<skill-name>/config.json`
- Windows: `%APPDATA%\<skill-name>\config.json` (fallback if XDG not set)

```python
import os
from pathlib import Path

def xdg_config_home() -> Path:
    xdg = os.environ.get("XDG_CONFIG_HOME")
    if xdg:
        return Path(xdg)
    return Path.home() / ".config"

def global_config_path(skill_name: str) -> Path:
    return xdg_config_home() / skill_name / "config.json"
```

This file is never inside any project directory, so there is no risk of accidentally committing it.

---

## Project-Scoped Configuration

For config that is specific to a project, use a `.skill-config/` directory at the project root.

```
project-root/
  .skill-config/
    my-skill.json          # committable project defaults (optional)
    my-skill.local.json    # local overrides, never committed
```

- `my-skill.json` — safe to commit if it contains only non-sensitive defaults the whole team should share.
- `my-skill.local.json` — machine-local overrides. Always gitignored.

### Gitignore Convention

Ship a `.gitignore` entry or bootstrap it into `.git/info/exclude` on first run:

```
# .gitignore or .git/info/exclude
.skill-config/*.local.json
```

If you want to prevent the entire `.skill-config/` directory from being committed:

```
.skill-config/
```

### Bootstrap Helper

On first run, a skill should write the local pattern into `.git/info/exclude` so it is protected even if the project has no `.gitignore`:

```python
def bootstrap_gitexclude(project_root: Path, pattern: str = ".skill-config/*.local.json") -> None:
    exclude = project_root / ".git" / "info" / "exclude"
    if not exclude.exists():
        return
    content = exclude.read_text()
    if pattern not in content:
        with exclude.open("a") as f:
            f.write(f"\n{pattern}\n")
```

---

## Config Precedence

A skill should load and merge config in this order, with later sources winning:

1. **Machine-wide defaults** — `~/.config/<skill-name>/config.json`
2. **Project committed config** — `.skill-config/<skill-name>.json`
3. **Project local overrides** — `.skill-config/<skill-name>.local.json`

```python
import json
from pathlib import Path

def load_config(skill_name: str, project_root: Path | None = None) -> dict:
    result = {}

    sources = [global_config_path(skill_name)]

    if project_root:
        sources.append(project_root / ".skill-config" / f"{skill_name}.json")
        sources.append(project_root / ".skill-config" / f"{skill_name}.local.json")

    for path in sources:
        if path.exists():
            data = json.loads(path.read_text())
            result.update(data)

    return result
```

---

## First-Run Bootstrap Flow

When a skill needs config that does not yet exist, it should:

1. Check if the required keys exist in the merged config.
2. Prompt the user for any missing values (or apply documented defaults).
3. Ask the user which scope to save to: machine-wide or project-local.
4. Write the config to the appropriate file, creating directories as needed.
5. Run `bootstrap_gitexclude()` if writing to a project-local file.

```python
def write_config(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2))
```

---

## What Does Not Belong Here

| Thing | Where it belongs |
|-------|-----------------|
| API keys, tokens, passwords | Environment variables or a secrets manager |
| Provider-specific agent settings | The provider's own config (e.g. `.claude/settings.json`) |
| Runtime state or caches | `$XDG_CACHE_HOME/<skill-name>/` (`~/.cache/<skill-name>/`) |
| Logs | `$XDG_STATE_HOME/<skill-name>/` (`~/.local/state/<skill-name>/`) |

---

## Summary

| Scope | File | Committed? |
|-------|------|------------|
| Machine-wide | `~/.config/<skill-name>/config.json` | N/A (never in a repo) |
| Project shared | `.skill-config/<skill-name>.json` | Optional |
| Project local | `.skill-config/<skill-name>.local.json` | Never |
