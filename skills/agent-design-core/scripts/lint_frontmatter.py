#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml"]
# ///

from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path

import yaml

REQUIRED_KEYS = {
    "id",
    "title",
    "domain",
    "kind",
    "status",
    "last_reviewed",
    "update_cadence",
    "tags",
    "related",
}

ENUMS = {
    "domain": {"core", "architecture", "tooling-security", "knowledge-retrieval", "workflow-delegation", "output-reliability"},
    "kind": {"concept", "decision-matrix", "pattern", "anti-pattern", "playbook", "checklist", "spec"},
    "status": {"active", "draft", "deprecated"},
    "update_cadence": {"monthly", "quarterly", "on-change"},
}

ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def parse_frontmatter(path: Path):
    text = path.read_text()
    if not text.startswith("---\n"):
        raise ValueError("missing frontmatter start")
    parts = text.split("---\n", 2)
    if len(parts) < 3:
        raise ValueError("missing frontmatter end")
    raw = parts[1]
    data = yaml.safe_load(raw)
    if not isinstance(data, dict):
        raise ValueError("frontmatter is not a map")
    return data


def iter_reference_files(suite_root: Path):
    skill_root = suite_root / "skills" if (suite_root / "skills").is_dir() else suite_root
    for skill_dir in sorted(skill_root.glob("agent-design-*")):
        refs = skill_dir / "references"
        if refs.exists():
            yield from sorted(refs.glob("*.md"))


def validate_file(path: Path, ids: set[str], errors: list[str]):
    try:
        fm = parse_frontmatter(path)
    except Exception as exc:
        errors.append(f"{path}: {exc}")
        return

    missing = REQUIRED_KEYS - set(fm.keys())
    if missing:
        errors.append(f"{path}: missing keys {sorted(missing)}")

    extra = set(fm.keys()) - REQUIRED_KEYS
    if extra:
        errors.append(f"{path}: unexpected keys {sorted(extra)}")

    rid = fm.get("id")
    if not isinstance(rid, str) or not ID_RE.match(rid):
        errors.append(f"{path}: invalid id '{rid}'")
    elif rid in ids:
        errors.append(f"{path}: duplicate id '{rid}'")
    else:
        ids.add(rid)

    title = fm.get("title")
    if not isinstance(title, str) or not title.strip():
        errors.append(f"{path}: invalid title")

    for key, allowed in ENUMS.items():
        value = fm.get(key)
        if value not in allowed:
            errors.append(f"{path}: {key} must be one of {sorted(allowed)}; got {value!r}")

    last_reviewed = fm.get("last_reviewed")
    if isinstance(last_reviewed, date):
        pass
    elif isinstance(last_reviewed, str) and DATE_RE.match(last_reviewed):
        pass
    else:
        errors.append(f"{path}: last_reviewed must be YYYY-MM-DD")

    tags = fm.get("tags")
    if not isinstance(tags, list) or not tags or not all(isinstance(x, str) and x.strip() for x in tags):
        errors.append(f"{path}: tags must be a non-empty list of strings")

    related = fm.get("related")
    if not isinstance(related, list) or not all(isinstance(x, str) and x.strip() for x in related):
        errors.append(f"{path}: related must be a list of strings")


def main():
    parser = argparse.ArgumentParser(description="Validate reference frontmatter schema across the agent-design suite.")
    parser.add_argument("--suite-root", required=True, help="Path containing agent-design-* skill directories")
    args = parser.parse_args()

    suite_root = Path(args.suite_root).resolve()
    if not suite_root.exists():
        print(f"[ERROR] suite root does not exist: {suite_root}")
        sys.exit(1)

    ref_files = list(iter_reference_files(suite_root))
    if not ref_files:
        print(f"[ERROR] no reference files found under {suite_root}")
        sys.exit(1)

    errors = []
    ids = set()
    for path in ref_files:
        validate_file(path, ids, errors)

    if errors:
        print("[FAIL] frontmatter validation errors:")
        for err in errors:
            print(f"- {err}")
        sys.exit(1)

    print(f"[OK] validated {len(ref_files)} reference files with {len(ids)} unique ids")


if __name__ == "__main__":
    main()
