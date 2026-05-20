# Wrist Buddy Privacy Policy — archived

> **The privacy policy has moved.**
>
> **New canonical location:** https://wristbuddy.app/privacy/
>
> **Source repo for the new site:** https://github.com/mariolonghi/wristbuddy-app

This repo is kept alive solely as a 301-redirect source for the legacy URL `mariolonghi.com/wristbuddy-privacy/`. Every page here uses [`jekyll-redirect-from`](https://github.com/jekyll/jekyll-redirect-from) to forward visitors (and search engines) to the matching path under `wristbuddy.app/privacy/`.

## URL mapping

| Old (this repo, mariolonghi.com) | New (wristbuddy.app) |
| -------------------------------- | -------------------- |
| `/wristbuddy-privacy/`           | `/privacy/`          |
| `/wristbuddy-privacy/es/`        | `/privacy/es/`       |
| `/wristbuddy-privacy/fr/`        | `/privacy/fr/`       |
| `/wristbuddy-privacy/de/`        | `/privacy/de/`       |
| `/wristbuddy-privacy/pt-br/`     | `/privacy/pt-br/`    |
| `/wristbuddy-privacy/sv/`        | `/privacy/sv/`       |

Each old URL serves a tiny HTML stub: meta-refresh redirect + `<link rel="canonical">` pointing at the new location. Browsers redirect on render; search engines pick up the canonical and update their index.

## Why keep this repo at all?

Two reasons:
1. **Preserve external links.** Anyone who bookmarked the old URL, anyone who cited it in an external doc, anyone who cached the URL in a notes app — they all keep working.
2. **Git history.** The 13 commits in `git log` capture how the privacy policy was drafted, restyled with the design system, and translated into 6 languages. That history is useful context even though the live content has moved.

## Don't edit content here

To update the privacy policy, edit it in the new repo: https://github.com/mariolonghi/wristbuddy-app — specifically `privacy/index.md` (English source) plus the 5 locale variants. The translation-sync CI gate enforces that all 6 stay in lockstep.

## Future deprecation

If, after a year or two, traffic to the old URL drops to zero, this repo can be deleted entirely. Until then it costs nothing (GitHub Pages free tier, zero maintenance) and protects a small but real long-tail of inbound traffic.
