# Wrist Buddy Privacy Policy

This repository hosts the Privacy Policy for the
[Wrist Buddy](https://github.com/mariolonghi/WristBuddy) iPhone + Apple
Watch app.

The published policy is served via GitHub Pages and is the canonical URL
referenced from the App Store listing:

**https://mariolonghi.com/wristbuddy-privacy/**

The site is restyled with the WristBuddy design system (mint accent,
Bricolage Grotesque, optional dark mode) and is available in all six
languages the app ships in.

---

## Repository layout

```
.
├── index.md                 ← English source (default at /)
├── es/index.md              ← Spanish     (/es/)
├── fr/index.md              ← French      (/fr/)
├── de/index.md              ← German      (/de/)
├── pt-br/index.md           ← Brazilian Portuguese (/pt-br/)
├── sv/index.md              ← Swedish     (/sv/)
│
├── _config.yml              ← Jekyll config (baseurl, no theme)
├── _data/
│   ├── locales.yml          ← Source of truth for the 6 supported locales
│   └── i18n.yml             ← Header / footer / a11y chrome strings
├── _layouts/
│   └── default.html         ← Brand shell + language switcher + dark toggle
├── assets/
│   ├── styles.css           ← Design-token CSS
│   ├── icon-rounded.svg     ← Header / footer logo
│   └── ...                  ← Other brand SVGs
├── favicon/                 ← 16/32/180/192/512 favicons
├── og-image.png             ← Social-card image (1200×630)
├── site.webmanifest         ← PWA manifest
│
└── .github/
    ├── workflows/
    │   └── translation-sync.yml   ← CI gates (see below)
    └── scripts/
        ├── check_translation_sync.py
        └── check_app_parity.py
```

---

## How to update the policy

The English file (`index.md`) is the source of truth. Edits flow:

1. **Edit `index.md`** — make your content change.
2. **Bump the date** — change both `effective_date:` (if newly in
   force) and `last_updated:` in the YAML front matter.
3. **Translate the change into all five other locales** —
   `es/`, `fr/`, `de/`, `pt-br/`, `sv/`.
4. **Bump each translation's `last_updated:`** to match the English
   value so the sync gate is satisfied.
5. Commit, push. GitHub Pages rebuilds in ~1 min.

If you only want to ship a small structural fix (typo, link), the
process is the same — every translation must be touched and its
`last_updated` bumped. This forces translations to never silently rot.

---

## CI translation gates

Two GitHub Actions checks run on every PR and push to `main`:

### Gate 1 — translations in sync with English

Runs `.github/scripts/check_translation_sync.py`. Reads
`_data/locales.yml`, parses each locale's front-matter `last_updated`
date, and asserts they all match the English source's date. Fails the
build if any translation is missing or outdated, with a precise
remediation message identifying the offending files.

This is the forcing function: you cannot ship an update to the English
policy without also updating every translation in the same PR.

### Gate 2 — site locales mirror the app's String Catalog

Runs `.github/scripts/check_app_parity.py`. Fetches the WristBuddy iOS
String Catalog (`WristBuddy/Localizable.xcstrings`) via the GitHub
Contents API and compares the locales it ships against
`_data/locales.yml`. Fails on any mismatch — either the app added a
language the privacy site doesn't follow, or the privacy site has a
stale entry the app dropped.

A scheduled run on Mondays catches divergence even when nothing in this
repo changed.

#### Configuration (only needed if defaults break)

The gate's defaults assume the catalog is publicly fetchable at
`mariolonghi/WristBuddy → WristBuddy/WristBuddy/Localizable.xcstrings`.
If that's not true, configure via repo settings:

| Setting type | Name | Purpose |
| ------------ | ---- | ------- |
| Variable     | `APP_REPO`         | `owner/repo` of the iOS app |
| Variable     | `APP_CATALOG_PATH` | Path inside that repo to the `.xcstrings` |
| Secret       | `APP_REPO_TOKEN`   | PAT with `Contents: read` if the repo is private |

Strict mode (network failure → CI failure) is off by default so a
transient GitHub outage never blocks a docs PR. Flip
`STRICT: "true"` in `.github/workflows/translation-sync.yml` if you'd
rather have hard enforcement.

---

## Adding or removing a language

1. **Add a new entry to `_data/locales.yml`** with `code`, `name`,
   `file`, `path`. Use Apple's BCP-47 code (e.g. `pt-BR`, not `pt-br`)
   so it matches the app catalog.
2. **Create the translation file** at the declared `file` path. Copy
   `index.md` as a starting point, set its front-matter `lang:` to the
   new code, and translate the body.
3. **Add the locale's chrome strings to `_data/i18n.yml`** (header /
   footer / a11y labels — six keys).
4. **Push.** Both CI gates verify the addition is consistent: gate 1
   confirms the new translation's date matches English, gate 2 confirms
   the app catalog also ships that locale.

To remove a language: delete its row from `_data/locales.yml`, delete
its `<dir>/index.md`, and remove its block from `_data/i18n.yml`.

---

## Local preview (optional)

The site is plain Jekyll without third-party plugins, so any GitHub
Pages-compatible Ruby setup will render it:

```bash
bundle init
bundle add jekyll github-pages
bundle exec jekyll serve --baseurl /wristbuddy-privacy
# → http://127.0.0.1:4000/wristbuddy-privacy/
```

The CI scripts can also be run locally (requires PyYAML):

```bash
pip install pyyaml
python3 .github/scripts/check_translation_sync.py
python3 .github/scripts/check_app_parity.py
```
