#!/usr/bin/env python3
"""Gate 1 — translation sync check.

Reads _data/locales.yml. For each locale:
  1. Verifies the declared `file` exists.
  2. Parses the YAML front matter.
  3. Asserts `last_updated` is present and equals the English source's.

Fails CI on any divergence so that updates to the English policy can
never ship without matching updates to every translation.

Run locally:
    python3 .github/scripts/check_translation_sync.py
"""
from __future__ import annotations
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]


def parse_front_matter(path: Path) -> dict:
    """Extract the YAML front matter dict from a .md file."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        sys.exit(f"FATAL: {path} has no YAML front matter")
    parts = text.split("---", 2)
    if len(parts) < 3:
        sys.exit(f"FATAL: {path} front matter is malformed (no closing ---)")
    fm = yaml.safe_load(parts[1]) or {}
    if not isinstance(fm, dict):
        sys.exit(f"FATAL: {path} front matter did not parse to a mapping")
    return fm


def load_locales() -> list[dict]:
    locales_path = REPO_ROOT / "_data" / "locales.yml"
    if not locales_path.exists():
        sys.exit(f"FATAL: {locales_path} not found")
    data = yaml.safe_load(locales_path.read_text(encoding="utf-8")) or {}
    locales = data.get("locales") or []
    if not locales:
        sys.exit("FATAL: _data/locales.yml has no `locales:` entries")
    for entry in locales:
        for required in ("code", "name", "file", "path"):
            if required not in entry:
                sys.exit(
                    f"FATAL: locale entry is missing `{required}`: {entry}"
                )
    return locales


def main() -> int:
    locales = load_locales()
    en = next((l for l in locales if l["code"] == "en"), None)
    if not en:
        sys.exit("FATAL: _data/locales.yml has no `en` entry")

    en_path = REPO_ROOT / en["file"]
    if not en_path.exists():
        sys.exit(f"FATAL: English source missing at {en_path}")

    en_fm = parse_front_matter(en_path)
    en_last = en_fm.get("last_updated")
    if not en_last:
        sys.exit(
            f"FATAL: English source {en_path} has no `last_updated` "
            "in front matter — add `last_updated: YYYY-MM-DD`"
        )
    print(f"English source ({en['file']}) last_updated = {en_last}")

    missing: list[str] = []
    out_of_sync: list[tuple[str, str]] = []

    for entry in locales:
        if entry["code"] == "en":
            continue
        path = REPO_ROOT / entry["file"]
        if not path.exists():
            missing.append(entry["file"])
            continue
        fm = parse_front_matter(path)
        last = fm.get("last_updated")
        if last is None:
            sys.exit(
                f"FATAL: {entry['file']} has no `last_updated` in front "
                "matter — add `last_updated: YYYY-MM-DD`"
            )
        if str(last) != str(en_last):
            out_of_sync.append((entry["file"], str(last)))

    if missing:
        print()
        print("MISSING translations:")
        for m in missing:
            print(f"  • {m}")

    if out_of_sync:
        print()
        print(f"OUT-OF-SYNC translations (English is {en_last}):")
        for fp, ts in out_of_sync:
            print(f"  • {fp:<24}  last_updated = {ts}")

    if missing or out_of_sync:
        print()
        print("How to fix:")
        print("  1. Update each listed translation to reflect the new")
        print("     English content (translate the changed sections).")
        print("  2. Bump that file's `last_updated:` in the front matter")
        print(f"     to {en_last} so it matches the English source.")
        print("  3. Re-run this script (or push) to verify.")
        return 1

    print()
    print(
        f"OK — all {len(locales)} locales in sync at {en_last} "
        "(English + 5 translations)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
