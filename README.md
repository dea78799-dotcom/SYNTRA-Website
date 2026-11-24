# SYNTRA Website

Official website source for SYNTRA Group.

Current website version: **v2.14**.

## v2.14 — Status Incident History

- Added a public Status page with clear separation between monitored website URLs and products without public endpoints.
- Added a scheduled GitHub Actions monitor that checks public pages every 30 minutes and updates the latest status data.
- Added a bounded incident history that records only status transitions and recovery events.\n- Kept monitoring scope explicit: HTTP reachability is not represented as full product health.
- Added Status navigation and sitemap coverage while preserving public-information and security boundaries.

## v2.12 — Public Changelog

- Added a dedicated Changelog page with project filters and text search.
- Summarized version notes from public project repositories and linked each entry to its source.
- Marked undated entries as not published instead of inferring dates; separated prototypes and unreleased notes from formal releases.
- Added Changelog navigation across the public website and listed the page in the sitemap.
- Preserved the existing security policy, public contact address and mobile-responsive visual identity.

## v2.11 — Homepage visual refinement

- Refined the homepage visual system with a restrained grid texture, softer ambient lighting and a more cohesive dark-and-muted-gold presentation.
- Improved navigation hover states, translucent header treatment, product cards, icon surfaces and download panels.
- Tuned mobile spacing and touch layouts while preserving reduced-motion behavior and existing page content.
- Kept the public Updates page concise and excluded internal development details.
- Preserved the existing security policy, public contact address, product links and release-status wording.

## Deploy with GitHub Pages

1. Open the repository **Settings**.
2. Select **Pages** in the sidebar.
3. Under **Build and deployment**, choose **Deploy from a branch**.
4. Select branch `main` and folder `/ (root)`, then save.
5. Wait for GitHub Pages to finish publishing. The website URL will appear in the Pages settings.

## Website files

- `about/index.html` — SYNTRA GROUP introduction, mission, development principles and ecosystem overview.
- `index.html` — responsive SYNTRA landing page with accessible navigation and product overview.
- `products/syntra-os.html` — product overview for SYNTRA OS.
- `products/syntra-files.html` — product overview for SYNTRA FILES.
- `products/syntra-social.html` — product overview for SYNTRA SOCIAL.
- `changelog/index.html` — public project change history with filters, search and source links.
- `status/index.html` — public service-status dashboard.
- `status/data.json` — latest automated public endpoint checks.\n- `changelog/index.html` — public project change history with filters, search and source links.
- `updates/index.html` — public announcements only; internal development notes and sensitive technical details are not published here.
- `downloads/index.html` — public Download Center showing availability and official release links; unavailable packages remain clearly marked.
- `docs/index.html` — public-facing Documentation Center with product status and safe user guidance; internal architecture and CI details are not exposed.
- `support/index.html` — Support Center with product FAQs, GitHub issue links, safe bug-report guidance and public contact information.
- `community/index.html` — SYNTRA Community page.
- `assets/syntra-files-logo.svg` — SYNTRA FILES product logo.
- `assets/syntra-mark.svg` — shared SYNTRA brand mark and favicon.
- Product source repositories:
  - [SYNTRA OS](https://github.com/dea78799-dotcom/SyntraOS)
  - [SYNTRA FILES](https://github.com/dea78799-dotcom/Syntra-Files)
  - [SYNTRA SOCIAL](https://github.com/dea78799-dotcom/Syntra-Social)

## APK publishing

Do not present a CI artifact or source-code ZIP as a ready-to-install release. SYNTRA FILES and SYNTRA OS download actions remain unavailable until an official end-user package is published and verified. The Download Center links to the official release pages for status checking.

Public contact: vanhuong05042025@gmail.com

Support Center: https://dea78799-dotcom.github.io/SYNTRA-Website/support/

Community: https://dea78799-dotcom.github.io/SYNTRA-Website/community/

## v2.8 — Documentation privacy and mobile navigation QA

- Reworked Documentation Center into a public-facing product information hub.
- Removed direct links to internal architecture notes, CI workflows and detailed technical procedures from the public documentation page.
- Added compact, keyboard-accessible mobile navigation to Documentation, Support and Community pages.
- Verified navigation controls, ARIA state, responsive breakpoints, balanced HTML/CSS/JavaScript tags and absence of the private primary email across the 10 main pages.
- Browser/device rendering and live GitHub Pages deployment still require separate visual verification.

## v2.7 — Public information and Download Center refinement

- Replaced the detailed project changelog with a concise public announcements page.
- Removed detailed internal progress notes, implementation descriptions, architecture references and operational disclosures from Updates.
- Simplified Download Center to show product availability and official release-page links.
- Kept unavailable APK and OS installer downloads clearly disabled; no unverified package is presented as ready to install.
- Updated page descriptions and public navigation while preserving SYNTRA's dark and muted-gold visual identity.

## v2.6 — Product pages navigation refresh

- Unified SYNTRA OS, SYNTRA FILES and SYNTRA SOCIAL navigation with the About page and consistent ecosystem destinations.
- Added compact accessible mobile navigation menus with Escape-to-close and close-on-link/click-outside behavior.
- Added active-page navigation markers and improved menu focus/ARIA state.
- Preserved reduced-motion support, existing product information, repository links and public contact address.

## v2.5 — SYNTRA GROUP introduction page

- Added a dedicated About page describing SYNTRA's direction, mission and development principles.
- Added a clearly labeled ecosystem overview for SYNTRA OS, SYNTRA FILES, SYNTRA SOCIAL and SYNTRA NEXUS, with project states distinguished.
- Linked the homepage navigation to the new About page.
- Added responsive navigation, keyboard-accessible skip link, reduced-motion support and social metadata.
- Kept public contact details limited to the designated public email address.

## v2.4 — Homepage visual refresh

- Rebuilt the homepage hero into a responsive editorial layout with clearer SYNTRA positioning and a focused visual identity.
- Improved desktop project discovery with a three-column product grid, refined card hierarchy and restrained gold detailing.
- Added a compact research / engineering / improvement strip and clearer ecosystem messaging.
- Preserved mobile navigation, keyboard focus visibility, reduced-motion support, existing product routes and official contact details.

## v2.3 — Latest product version synchronization

- Synchronized SYNTRA FILES website, homepage, changelog and Download Center version to repository v0.75.0.
- Updated the latest SYNTRA FILES changelog entry for compact mobile navigation and overflow-menu organization.
- Synchronized SYNTRA SOCIAL product status and changelog to Prototype 1.8, including Creator Dashboard, community groups and local safety controls.
- Kept SYNTRA SOCIAL clearly labeled as a local prototype and kept APK installation disabled until an official package is verified.

## v2.2 — SYNTRA FILES v0.73.0 synchronization

- Updated the homepage latest-update panel and SYNTRA FILES product page to v0.73.0.
- Added v0.73.0 image-preview controls and v0.72.0 text-preview status-strip entries to the changelog.
- Kept the product status as early development and testing; no verified public APK release is claimed.

## v2.1 — Product version synchronization

- Updated the SYNTRA FILES product page and homepage latest-update panel to repository version v0.71.0.
- Updated the SYNTRA SOCIAL product page and homepage status to Prototype 1.0.
- Added a SYNTRA SOCIAL changelog entry and documented its local-only prototype limitations.
- Updated repository links and project descriptions.

## v2.0 — Download Center release verification

- Added a release verification standard covering official source, product/version/architecture identity, package integrity, release notes and SHA-256.
- Kept direct APK and OS installer actions disabled because no verified end-user package was confirmed.
- SYNTRA FILES remains in testing and upgrade.


## SEO and performance

- Every public HTML page includes a canonical URL and Open Graph/Twitter sharing metadata.
- `sitemap.xml` lists the public website pages for search engine discovery.
- `robots.txt` allows public crawling and points crawlers to the sitemap.
- Images use asynchronous decoding; the community QR image is lazy-loaded.
- The homepage and community page establish a preconnect hint for the external image host they use.
- SEO metadata and local file paths were checked at source level. Browser rendering, live deployment, and real-device performance measurements still require separate testing.

## Security baseline

- All public HTML pages include a browser Content Security Policy (CSP) meta policy and a strict-origin referrer policy.
- CSP allows same-origin scripts/styles, inline code currently used by the static pages, local assets, and images from the approved `raw.githubusercontent.com` host. It blocks object embeds and frames and restricts form submissions.
- `.github/workflows/security-baseline.yml` runs read-only static checks on pushes and pull requests.
- `scripts/security_audit.py` checks for common exposed credential patterns, missing browser policies, and broken local links/anchors.
- Dependabot checks GitHub Actions dependencies weekly.
- `SECURITY.md` documents private vulnerability reporting.
- GitHub Pages does not provide configurable HTTP response headers for this repository's default `github.io` hostname. The CSP meta policy is a browser-side baseline, not a replacement for HTTP security headers or an edge WAF.
- Cloudflare proxy/WAF cannot be placed in front of the existing shared `github.io` hostname without a custom domain. No DNS or hosting changes were made.
- Branch protection, account 2FA, and private vulnerability reporting settings must be reviewed in GitHub Settings; the connected integration did not grant access to read or change branch protection settings.
- Static checks do not prove resistance to DDoS, account takeover, or all application attacks. No load or penetration testing is performed.

