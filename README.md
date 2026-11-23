# SYNTRA Website

Official website source for SYNTRA Group.

Current website version: **v2.0**.

## Deploy with GitHub Pages

1. Open the repository **Settings**.
2. Select **Pages** in the sidebar.
3. Under **Build and deployment**, choose **Deploy from a branch**.
4. Select branch `main` and folder `/ (root)`, then save.
5. Wait for GitHub Pages to finish publishing. The website URL will appear in the Pages settings.

## Website files

- `index.html` — responsive SYNTRA landing page with accessible mobile navigation, social metadata, reading progress and latest-updates preview, project testing status, Download Center entry and Documentation Center, Support Center and Community navigation (v1.9; retained in v2.0).
- `products/syntra-os.html` — product overview for SYNTRA OS.
- `products/syntra-files.html` — product overview for SYNTRA FILES.
- `updates/index.html` — version history and project update notes for SYNTRA OS and SYNTRA FILES.
- `downloads/index.html` — Download Center with release status and a five-step release verification standard; direct installation links remain disabled until verified official packages are published (v2.0).
- `docs/index.html` — Documentation Center linking to product, build, contribution, architecture and QEMU testing documentation in the source repositories.
- `support/index.html` — Support Center with product FAQs, GitHub issue links, safe bug-report guidance and public contact information.
- `community/index.html` — SYNTRA Community page with the Discord invite and user-provided QR image.
- `assets/syntra-files-logo.svg` — SYNTRA FILES product logo.
- `assets/syntra-mark.svg` — shared SYNTRA brand mark and favicon.
- Product source repositories:
  - [SYNTRA OS](https://github.com/dea78799-dotcom/SyntraOS)
  - [SYNTRA FILES](https://github.com/dea78799-dotcom/Syntra-Files)

## APK publishing

SYNTRA FILES is currently in testing and upgrade (latest repository README checked for this website update: v0.40.0). The Download Center intentionally keeps APK installation disabled until a real official package has been built and checked. SYNTRA OS has no end-user installer confirmed. Never present a CI artifact or source-code ZIP as a ready-to-install release.

Public contact: vanhuong05042025@gmail.com

Support Center: https://dea78799-dotcom.github.io/SYNTRA-Website/support/

Community: https://dea78799-dotcom.github.io/SYNTRA-Website/community/

## v2.0 — Download Center release verification

- Added a five-step release verification standard covering official source, product/version/architecture identity, package integrity, release notes and SHA-256.
- Kept direct APK and OS installer actions disabled because no verified end-user package is currently confirmed.
- SYNTRA FILES remains in testing and upgrade.
