# Veehive.ai Website Rebrand — Design Spec

**Date:** 2026-04-14
**Goal:** Convert the current veehivelabs.com website into a pure veehive.ai product website, separating it from the HiveLabs services brand.

## Brand Separation

- **veehive.ai** — Product company site: SnapaPro, mpliphi, Studio, HiveLink
- **veehivelabs.com** — Services/consulting site: custom AI dev, SLM, agentic, datalake, consultancy (separate project, not touched here)

The only link between the two sites is a single "Custom Development" link in nav + footer pointing to `https://veehivelabs.com`.

---

## 1. File Structure

### Delete

| File | Reason |
|------|--------|
| `hivelabs.html` | HiveLabs content moves to veehivelabs.com |
| `request-quote.html` | Not needed on product site |
| `case-studies.html` | Not needed on product site |
| `google37d8949def1ce798.html` | Tied to veehivelabs.com Search Console |
| `BingSiteAuth.xml` | Tied to veehivelabs.com Bing verification |

### Keep (with modifications)

| File | Changes |
|------|---------|
| `index.html` | Domain swap, HiveLabs removal, nav/footer update, structured data cleanup |
| `about.html` | Domain swap, HiveLabs/case-studies removal, nav/footer update, structured data cleanup |
| `team.html` | Domain swap, nav/footer update, structured data cleanup |
| `hivelink.html` | Domain swap, nav/footer update |
| `sitemap.xml` | Remove deleted pages, update domain to veehive.ai |
| `robots.txt` | Update domain to veehive.ai |
| `Veehive.ai.svg` | No changes |
| `dubai-ai-seal.png` | No changes |

---

## 2. Domain & URL Replacement

Global find-and-replace across all kept files:

| Find | Replace With |
|------|-------------|
| `https://veehivelabs.com` | `https://veehive.ai` |
| `veehivelabs.com` (remaining instances) | `veehive.ai` |
| `"Veehive Labs"` (as og:site_name, author, meta) | `"Veehive.ai"` |
| `"Veehive Products"` (alternate names) | Remove entirely |

GA4 tracking: update `isExternal` check from `!href.includes('veehivelabs.com')` to `!href.includes('veehive.ai')`.

---

## 3. HiveLabs Content Removal

### Structured Data (JSON-LD) — all pages

- Remove `"HiveLabs by Veehive"`, `"Veehive Labs"`, `"Veehive Products"` from all `alternateName` arrays
- Remove HiveLabs `Offer` from product catalog: `{"@type": "Service", "name": "HiveLabs", ...}`
- Remove "What is HiveLabs?" FAQ entry entirely
- Strip HiveLabs mentions from other FAQ answers (e.g. "Plus HiveLabs — custom agentic AI development services")
- Update `WebSite` description: remove "and HiveLabs"

### Meta Tags — all pages

- Remove "HiveLabs" from `description` and `keywords` meta tags
- Remove "case studies" from about.html title/descriptions
- Remove "Veehive Labs" from `author` meta tags — replace with "Veehive.ai"

### Navigation — all 4 remaining pages

- Remove the `HiveLabs` nav link (desktop + mobile)
- Add `Custom Dev` link pointing to `https://veehivelabs.com` (external, target="_blank")

### Footer — all 4 remaining pages

- Remove `HiveLabs Services` link
- Remove `Case Studies` link
- Remove `Request a Quote` link
- Add `Custom Development` link pointing to `https://veehivelabs.com`

### index.html — page-specific

- Remove the entire "HIVELABS — SERVICES" section (~lines 1183-1210)
- Update "Learn About Our Team & Case Studies" heading → "Learn About Our Team"
- Remove `request-quote.html` CTA link
- Clean meta description: remove "plus HiveLabs custom AI development"

### about.html — page-specific

- Remove "Explore HiveLabs" button
- Remove "Case Studies" button/link
- Remove HiveLabs card
- Remove "Enterprise Case Studies" card
- Clean description text that mentions HiveLabs custom development
- Remove "What case studies does Veehive have?" FAQ entry

---

## 4. GA4 Tracking Cleanup

All pages share the same GA4 tracking script. Changes:

- Remove `click_hivelabs` event (no more hivelabs.html links)
- Remove `click_request_quote` event (no more request-quote links)
- Remove `click_case_studies` event (no more case-studies links)
- Add `click_custom_dev` event for `veehivelabs.com` links
- Update `isExternal` domain check: `veehivelabs.com` → `veehive.ai`

---

## 5. Firebase Configuration

### New Firebase project

- User creates a new project in Firebase Console (e.g. `veehive-ai`)
- `.firebaserc` updated with new project ID
- `firebase.json` rewrites cleaned:
  - Keep `**` → `/index.html` fallback
  - Keep cache headers (images/CSS/JS: 1 year)
- User connects `veehive.ai` custom domain in Firebase Console

### Old project

- `veehivelabs` Firebase project is NOT touched

---

## 6. GitHub

- New repo: `Veehive-ai/veehive.ai`
- Fresh `git init` (no history from veehivelabs-website repo)
- Initial commit with all cleaned files
- Push to new remote

---

## 7. SEO Files

### sitemap.xml

Remove deleted pages, update domain:

```xml
<url><loc>https://veehive.ai/</loc>...</url>
<url><loc>https://veehive.ai/about.html</loc>...</url>
<url><loc>https://veehive.ai/team.html</loc>...</url>
<url><loc>https://veehive.ai/hivelink.html</loc>...</url>
```

Pages removed: `hivelabs.html`, `request-quote.html`, `case-studies.html`

### robots.txt

```
# Robots.txt for Veehive.ai
# https://veehive.ai

User-agent: *
Allow: /

Sitemap: https://veehive.ai/sitemap.xml
Crawl-delay: 1
```

---

## Out of Scope

- No visual/design changes (colors, layout, fonts stay as-is)
- No new pages or content
- No changes to product descriptions or features
- No changes to the veehivelabs Firebase project
- No changes to veehivelabs.com
- Search Console / Bing verification for veehive.ai — user will set up later
