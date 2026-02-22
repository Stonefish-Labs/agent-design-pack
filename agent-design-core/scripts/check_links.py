#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml"]
# ///

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def parse_frontmatter(path: Path):
    text = path.read_text()
    if not text.startswith("---\n"):
        return None
    parts = text.split("---\n", 2)
    if len(parts) < 3:
        return None
    data = yaml.safe_load(parts[1])
    return data if isinstance(data, dict) else None


def iter_skill_dirs(suite_root: Path):
    return sorted([p for p in suite_root.glob("agent-design-*") if p.is_dir()])


def collect_reference_ids(skill_dirs: list[Path]):
    out = {}
    for skill in skill_dirs:
        refs = skill / "references"
        if not refs.exists():
            continue
        for path in refs.glob("*.md"):
            fm = parse_frontmatter(path)
            if fm and isinstance(fm.get("id"), str):
                out[fm["id"]] = path
    return out


def check_related(skill_dirs: list[Path], id_map: dict[str, Path], errors: list[str]):
    for skill in skill_dirs:
        refs = skill / "references"
        if not refs.exists():
            continue
        for path in refs.glob("*.md"):
            fm = parse_frontmatter(path) or {}
            related = fm.get("related", [])
            if isinstance(related, list):
                for rid in related:
                    if rid not in id_map:
                        errors.append(f"{path}: related id '{rid}' does not resolve")


def resolve_local_link(base: Path, target: str) -> Path | None:
    if target.startswith("http://") or target.startswith("https://") or target.startswith("mailto:"):
        return None
    if target.startswith("#"):
        return None
    cleaned = target.split("#", 1)[0].strip()
    if not cleaned:
        return None
    return (base / cleaned).resolve()


def check_markdown_links(path: Path, errors: list[str]):
    text = path.read_text()
    for link in LINK_RE.findall(text):
        resolved = resolve_local_link(path.parent, link)
        if resolved is None:
            continue
        if not resolved.exists():
            errors.append(f"{path}: broken link '{link}'")


def main():
    parser = argparse.ArgumentParser(description="Check related-id links and markdown file links across agent-design suite.")
    parser.add_argument("--suite-root", required=True, help="Path containing agent-design-* skill directories")
    args = parser.parse_args()

    suite_root = Path(args.suite_root).resolve()
    skill_dirs = iter_skill_dirs(suite_root)
    if not skill_dirs:
        print(f"[ERROR] no agent-design-* skill folders found under {suite_root}")
        sys.exit(1)

    id_map = collect_reference_ids(skill_dirs)
    errors = []
    check_related(skill_dirs, id_map, errors)

    for skill in skill_dirs:
        skill_md = skill / "SKILL.md"
        if skill_md.exists():
            check_markdown_links(skill_md, errors)
        refs = skill / "references"
        if refs.exists():
            for path in refs.glob("*.md"):
                check_markdown_links(path, errors)

    if errors:
        print("[FAIL] link checks failed:")
        for err in errors:
            print(f"- {err}")
        sys.exit(1)

    print(f"[OK] related ids and markdown links resolved across {len(skill_dirs)} skills")


if __name__ == "__main__":
    main()
