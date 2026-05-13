#!/usr/bin/env python3
"""Gate 2 — app/site locale parity check.

Fetches the WristBuddy iOS String Catalog from GitHub and verifies the
set of locales it ships matches `_data/locales.yml` in this repo.

Configuration (env vars, all optional):
    APP_REPO          owner/repo of the iOS app (default: mariolonghi/WristBuddy)
    APP_CATALOG_PATH  path inside that repo to the .xcstrings file
                      (default: WristBuddy/WristBuddy/Localizable.xcstrings)
    GH_TOKEN          GitHub token. Needed for private repos. The default
                      GITHUB_TOKEN works for public repos.
    STRICT            "true" makes network failures fail the build.
                      "false" (default) treats them as a warning.

Exit codes:
    0  parity OK (or soft-fail with STRICT=false on network error)
    1  divergence detected, OR STRICT=true and fetch failed
    2  malformed config / catalog
"""
from __future__ import annotations
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]

APP_REPO = os.environ.get("APP_REPO", "mariolonghi/WristBuddy").strip()
APP_CATALOG_PATH = os.environ.get(
    "APP_CATALOG_PATH", "WristBuddy/WristBuddy/Localizable.xcstrings"
).strip()
GH_TOKEN = os.environ.get("GH_TOKEN", "").strip()
STRICT = os.environ.get("STRICT", "false").strip().lower() == "true"


def fetch_catalog() -> str:
    """Fetch the .xcstrings file via the GitHub Contents API.

    The Contents API works for both public and private repos when a token
    is supplied. Using `Accept: application/vnd.github.raw` returns the
    file body directly (rather than a base64-encoded JSON envelope).
    """
    url = f"https://api.github.com/repos/{APP_REPO}/contents/{APP_CATALOG_PATH}"
    headers = {
        "Accept": "application/vnd.github.raw",
        "User-Agent": "wristbuddy-privacy-ci",
    }
    if GH_TOKEN:
        headers["Authorization"] = f"token {GH_TOKEN}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=20) as resp:
        return resp.read().decode("utf-8")


def app_languages(catalog_text: str) -> set[str]:
    """Extract the set of localized language codes from a .xcstrings file."""
    try:
        data = json.loads(catalog_text)
    except json.JSONDecodeError as e:
        sys.exit(f"FATAL: catalog isn't valid JSON: {e}")
    langs: set[str] = set()
    src = data.get("sourceLanguage")
    if src:
        langs.add(src)
    for entry in data.get("strings", {}).values():
        for code in (entry.get("localizations") or {}).keys():
            langs.add(code)
    return langs


def site_languages() -> set[str]:
    """Extract the set of language codes declared in _data/locales.yml."""
    locales_path = REPO_ROOT / "_data" / "locales.yml"
    data = yaml.safe_load(locales_path.read_text(encoding="utf-8")) or {}
    return {entry["code"] for entry in data.get("locales", [])}


def main() -> int:
    print(f"App repo:         {APP_REPO}")
    print(f"Catalog path:     {APP_CATALOG_PATH}")
    print(f"Strict mode:      {STRICT}")
    print()

    try:
        catalog_text = fetch_catalog()
    except urllib.error.HTTPError as e:
        msg = (
            f"Could not fetch app catalog at {APP_REPO}/{APP_CATALOG_PATH} "
            f"(HTTP {e.code}: {e.reason})."
        )
        if e.code == 404:
            msg += (
                "\nLikely cause: the path moved, the repo is private "
                "without a token, or the repo is renamed. Set the "
                "APP_REPO / APP_CATALOG_PATH repo Variables (Actions → "
                "Variables) and add APP_REPO_TOKEN secret if private."
            )
        if STRICT:
            print(f"FAIL: {msg}")
            return 1
        print(f"WARN: {msg}")
        print("(soft-fail — set STRICT=true to enforce)")
        return 0
    except (urllib.error.URLError, TimeoutError) as e:
        msg = f"Network error fetching catalog: {e}"
        if STRICT:
            print(f"FAIL: {msg}")
            return 1
        print(f"WARN: {msg}")
        print("(soft-fail — set STRICT=true to enforce)")
        return 0

    app = app_languages(catalog_text)
    site = site_languages()
    print(f"App locales:   {sorted(app)}")
    print(f"Site locales:  {sorted(site)}")

    missing_in_site = app - site
    extra_in_site = site - app

    if not missing_in_site and not extra_in_site:
        print()
        print(f"OK — app and site agree on {len(app)} locales.")
        return 0

    print()
    if missing_in_site:
        print(
            f"DIVERGENCE: app supports these locales but the privacy "
            f"site doesn't: {sorted(missing_in_site)}"
        )
        print("  → add an entry to _data/locales.yml AND create the")
        print("    matching <code>/index.md translation in the same PR.")
    if extra_in_site:
        print(
            f"DIVERGENCE: privacy site has these locales but the app "
            f"doesn't: {sorted(extra_in_site)}"
        )
        print("  → either drop them from _data/locales.yml + delete the")
        print("    translation file, or add them to the app catalog.")
    print()
    print(
        "If the app repo path moved, override APP_REPO / "
        "APP_CATALOG_PATH via Actions Variables."
    )
    return 1


if __name__ == "__main__":
    sys.exit(main())
