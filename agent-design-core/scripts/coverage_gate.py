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


def clean_heading(h: str) -> str:
    h = re.sub(r"^##\s+", "", h).strip()
    h = h.replace("*", "")
    h = re.sub(r"\s+", " ", h)
    return h.strip().lower()


def extract_source_sections(source_pack: Path):
    rows = []
    for path in sorted(source_pack.glob("*.md")):
        for line in path.read_text().splitlines():
            if line.startswith("## "):
                rows.append((path.name, clean_heading(line)))
    return rows


def parse_frontmatter(path: Path):
    text = path.read_text()
    if not text.startswith("---\n"):
        return None
    parts = text.split("---\n", 2)
    if len(parts) < 3:
        return None
    data = yaml.safe_load(parts[1])
    return data if isinstance(data, dict) else None


def collect_reference_ids(suite_root: Path):
    ids = set()
    for skill in suite_root.glob("agent-design-*"):
        refs = skill / "references"
        if refs.exists():
            for path in refs.glob("*.md"):
                fm = parse_frontmatter(path)
                if fm and isinstance(fm.get("id"), str):
                    ids.add(fm["id"])
    return ids


def parse_matrix_rows(matrix_path: Path):
    rows = []
    in_table = False
    for raw in matrix_path.read_text().splitlines():
        line = raw.strip()
        if line.startswith("| source_doc |"):
            in_table = True
            continue
        if not in_table:
            continue
        if not line.startswith("|"):
            continue
        if set(line.replace("|", "").strip()) <= {"-", " "}:
            continue
        cols = [c.strip() for c in line.strip("|").split("|")]
        if len(cols) < 5:
            continue
        source_doc, section, mapped_ref, status, notes = cols[:5]
        rows.append((source_doc, section.lower(), mapped_ref, status.lower(), notes))
    return rows


def main():
    parser = argparse.ArgumentParser(description="Validate that major source sections are mapped in source-coverage-matrix.md")
    parser.add_argument("--source-pack", required=True)
    parser.add_argument("--suite-root", required=True)
    parser.add_argument("--fail-on-missing", action="store_true")
    args = parser.parse_args()

    source_pack = Path(args.source_pack).resolve()
    suite_root = Path(args.suite_root).resolve()
    matrix_path = suite_root / "agent-design-core" / "references" / "source-coverage-matrix.md"

    if not source_pack.exists():
        print(f"[ERROR] source pack not found: {source_pack}")
        sys.exit(1)
    if not matrix_path.exists():
        print(f"[ERROR] coverage matrix not found: {matrix_path}")
        sys.exit(1)

    source_sections = extract_source_sections(source_pack)
    matrix_rows = parse_matrix_rows(matrix_path)
    matrix_lookup = {(d, s): (m, st) for d, s, m, st, _ in matrix_rows}
    known_ids = collect_reference_ids(suite_root)

    missing = []
    bad_status = []
    bad_refs = []

    for source_doc, section in source_sections:
        entry = matrix_lookup.get((source_doc, section))
        if entry is None:
            missing.append((source_doc, section))
            continue
        mapped_ref, status = entry
        if status != "covered":
            bad_status.append((source_doc, section, status))
        if mapped_ref not in known_ids:
            bad_refs.append((source_doc, section, mapped_ref))

    if missing:
        print("[WARN] missing matrix rows:")
        for doc, sec in missing:
            print(f"- {doc} :: {sec}")

    if bad_status:
        print("[WARN] non-covered status rows:")
        for doc, sec, st in bad_status:
            print(f"- {doc} :: {sec} :: status={st}")

    if bad_refs:
        print("[WARN] mapped_ref id not found in suite:")
        for doc, sec, rid in bad_refs:
            print(f"- {doc} :: {sec} :: mapped_ref={rid}")

    failures = len(missing) + len(bad_status) + len(bad_refs)
    if failures and args.fail_on_missing:
        print(f"[FAIL] coverage gate failed with {failures} issue(s)")
        sys.exit(1)

    print(f"[OK] coverage gate checked {len(source_sections)} source H2 sections")
    if failures:
        print(f"[WARN] gate reported {failures} issue(s), fail-on-missing disabled")


if __name__ == "__main__":
    main()
