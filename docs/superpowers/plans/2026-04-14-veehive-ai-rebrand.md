# Veehive.ai Website Rebrand — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rebrand the veehivelabs.com website to veehive.ai, removing HiveLabs content and unused pages, updating all domain references, and configuring a new Firebase project + GitHub repo.

**Architecture:** Static HTML site with 4 pages (index, about, team, hivelink). No build process. All changes are in-place edits to HTML files plus config file updates. Firebase Hosting for deployment, new GitHub repo for source.

**Tech Stack:** HTML, CSS (Tailwind CDN), vanilla JS, Firebase Hosting, GitHub

---

### Task 1: Delete Removed Pages & Verification Files

**Files:**
- Delete: `public/hivelabs.html`
- Delete: `public/request-quote.html`
- Delete: `public/case-studies.html`
- Delete: `public/google37d8949def1ce798.html`
- Delete: `public/BingSiteAuth.xml`

- [ ] **Step 1: Delete the 5 files**

```bash
cd "/Users/imsats/myproject/Website Veehive.ai"
rm public/hivelabs.html public/request-quote.html public/case-studies.html public/google37d8949def1ce798.html public/BingSiteAuth.xml
```

- [ ] **Step 2: Verify only expected files remain**

```bash
ls public/
```

Expected output:
```
Veehive.ai.svg
about.html
dubai-ai-seal.png
hivelink.html
index.html
robots.txt
sitemap.xml
team.html
```

- [ ] **Step 3: Commit**

```bash
git add -u public/
git commit -m "Remove HiveLabs, request-quote, case-studies pages and verification files"
```

---

### Task 2: Update sitemap.xml

**Files:**
- Modify: `public/sitemap.xml`

- [ ] **Step 1: Replace sitemap.xml content**

Replace the entire file with:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>https://veehive.ai/</loc>
        <lastmod>2026-04-14</lastmod>
        <changefreq>weekly</changefreq>
        <priority>1.0</priority>
    </url>
    <url>
        <loc>https://veehive.ai/about.html</loc>
        <lastmod>2026-04-14</lastmod>
        <changefreq>weekly</changefreq>
        <priority>0.9</priority>
    </url>
    <url>
        <loc>https://veehive.ai/team.html</loc>
        <lastmod>2026-04-14</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.7</priority>
    </url>
    <url>
        <loc>https://veehive.ai/hivelink.html</loc>
        <lastmod>2026-04-14</lastmod>
        <changefreq>weekly</changefreq>
        <priority>0.9</priority>
    </url>
</urlset>
```

- [ ] **Step 2: Commit**

```bash
git add public/sitemap.xml
git commit -m "Update sitemap.xml for veehive.ai domain, remove deleted pages"
```

---

### Task 3: Update robots.txt

**Files:**
- Modify: `public/robots.txt`

- [ ] **Step 1: Replace robots.txt content**

```
# Robots.txt for Veehive.ai
# https://veehive.ai

User-agent: *
Allow: /

# Sitemap
Sitemap: https://veehive.ai/sitemap.xml

# Crawl-delay (optional, for politeness)
Crawl-delay: 1
```

- [ ] **Step 2: Commit**

```bash
git add public/robots.txt
git commit -m "Update robots.txt for veehive.ai domain"
```

---

### Task 4: Update index.html — GA4 Tracking Script

Every page has the same GA4 tracking script at the top. Update it on index.html first (this establishes the pattern for all other pages).

**Files:**
- Modify: `public/index.html` (lines 8)

- [ ] **Step 1: Update GA4 tracking script**

In the GA4 click-tracking script (line 8), make these changes:
1. Change `!href.includes('veehivelabs.com')` → `!href.includes('veehive.ai')`
2. Remove the `hivelabs.html` tracking line: `else if(href.includes('hivelabs.html'))evName='click_hivelabs';`
3. Remove the `request-quote` tracking line: `else if(href.includes('request-quote'))evName='click_request_quote';`
4. Remove the `case-studies` tracking line: `else if(href.includes('case-studies'))evName='click_case_studies';`
5. Add `veehivelabs.com` tracking: `else if(href.includes('veehivelabs.com'))evName='click_custom_dev';` (add before the `isExternal` check)

- [ ] **Step 2: Verify the tracking script is valid JS**

Open browser console or visually check the script has no syntax errors (balanced quotes, semicolons).

- [ ] **Step 3: Commit**

```bash
git add public/index.html
git commit -m "Update GA4 tracking: veehive.ai domain, add custom dev tracking, remove deleted page events"
```

---

### Task 5: Update index.html — Meta Tags & Structured Data

**Files:**
- Modify: `public/index.html` (lines 1-295)

- [ ] **Step 1: Update meta description (line 13)**

Remove "plus HiveLabs custom AI development" and "HiveLabs" from description:
```
"Veehive.ai is the agentic operating system for marketing execution. One command, complete campaigns. Four AI modules — SnapaPro (Planner), mpliphi (Orchestrator), Studio (Creator), HiveLink (Distributor). Dubai AI Seal Tier E certified. SOC 2 & ISO 27001 compliant."
```

- [ ] **Step 2: Update meta keywords (line 14)**

Remove "HiveLabs" and "custom AI development" from keywords:
```
"agentic AI, marketing execution, AI operating system, SnapaPro, mpliphi, Studio, HiveLink, Veehive, Dubai AI, enterprise AI, agentic architecture, AI automation"
```

- [ ] **Step 3: Update canonical and OG/Twitter URLs**

Replace all `veehivelabs.com` with `veehive.ai` in:
- Line 17: canonical
- Line 22: og:url
- Line 25: og:image
- Line 31: twitter:url
- Line 34: twitter:image

- [ ] **Step 4: Update Organization structured data (lines 44-109)**

- Remove `alternateName` array entirely (line 49): `"HiveLabs by Veehive", "Veehive Labs", "Veehive Products"`
- Change `"url": "https://veehivelabs.com"` → `"url": "https://veehive.ai"` (line 50)
- Change `"logo": "https://veehivelabs.com/logo.png"` → `"logo": "https://veehive.ai/logo.png"` (line 51)
- Update description (line 52): remove "plus HiveLabs custom agentic AI development services"
- Remove the HiveLabs Offer from `hasOfferCatalog` (line 106): `{"@type": "Offer", "itemOffered": {"@type": "Service", "name": "HiveLabs", "description": "Custom Agentic AI Development Labs"}}`

- [ ] **Step 5: Update BreadcrumbList (line 179)**

Change `"item": "https://veehivelabs.com/"` → `"item": "https://veehive.ai/"`

- [ ] **Step 6: Update WebSite structured data (lines 186-198)**

- Change `"url": "https://veehivelabs.com"` → `"url": "https://veehive.ai"` (line 191)
- Update description (line 192): remove "and HiveLabs" → `"The Agentic Operating System for Marketing Execution — SnapaPro, mpliphi, Studio, and HiveLink."`

- [ ] **Step 7: Update FAQ structured data (lines 201-289)**

- In "What is Veehive.ai?" answer (line 213): Remove "Plus HiveLabs — custom agentic AI development services." from the end.
- Remove the entire "What is HiveLabs?" FAQ entry (lines 225-230): the full Question object from `{"@type": "Question", "name": "What is HiveLabs?"...}` and its trailing comma.

- [ ] **Step 8: Commit**

```bash
git add public/index.html
git commit -m "Update index.html meta tags and structured data for veehive.ai"
```

---

### Task 6: Update index.html — Navigation

**Files:**
- Modify: `public/index.html` (lines 752-806)

- [ ] **Step 1: Replace HiveLabs nav link (desktop, line 767)**

Replace:
```html
<a href="hivelabs.html" class="nav-link px-3 py-1.5 text-[13px] rounded-md transition-colors" style="color: var(--text-secondary);">HiveLabs</a>
```
With:
```html
<a href="https://veehivelabs.com" target="_blank" rel="noopener noreferrer" class="nav-link px-3 py-1.5 text-[13px] rounded-md transition-colors" style="color: var(--text-secondary);">Custom Dev</a>
```

- [ ] **Step 2: Replace HiveLabs nav link (mobile, line 801)**

Replace:
```html
<a href="hivelabs.html" class="py-2.5 text-[14px]" style="color: var(--text-secondary);">HiveLabs</a>
```
With:
```html
<a href="https://veehivelabs.com" target="_blank" rel="noopener noreferrer" class="py-2.5 text-[14px]" style="color: var(--text-secondary);">Custom Dev</a>
```

- [ ] **Step 3: Commit**

```bash
git add public/index.html
git commit -m "Update index.html navigation: replace HiveLabs with Custom Dev link"
```

---

### Task 7: Update index.html — Remove HiveLabs Section & Update Footer/CTA

**Files:**
- Modify: `public/index.html` (lines 1180-1723)

- [ ] **Step 1: Remove the entire HIVELABS — SERVICES section (lines 1180-1268)**

Delete from `<div class="divider-gradient"></div>` (line 1180) through the closing `</section>` and the next `<div class="divider-gradient"></div>` (line 1268). This removes the divider-line before the section, the entire HiveLabs section, and the divider-line after it.

- [ ] **Step 2: Update About Promo heading (line 1568)**

Replace:
```html
<h3 class="text-xl md:text-2xl font-bold tracking-tight mb-2">Learn About Our Team & Case Studies</h3>
```
With:
```html
<h3 class="text-xl md:text-2xl font-bold tracking-tight mb-2">Learn About Our Team</h3>
```

- [ ] **Step 3: Update About Promo description (line 1569)**

Replace:
```html
<p class="text-[14px] text-white/40 leading-relaxed">Explore our credentials, capabilities, enterprise clients, and the team building the agentic operating system for marketing.</p>
```
With:
```html
<p class="text-[14px] text-white/40 leading-relaxed">Explore our credentials, capabilities, and the team building the agentic operating system for marketing.</p>
```

- [ ] **Step 4: Replace Request a Quote CTA with Book a Demo (lines 1596-1600)**

Replace the `request-quote.html` link block:
```html
<a href="request-quote.html"
   class="group inline-flex items-center justify-center gap-2.5 px-8 py-3.5 bg-[#3B5BFF] text-[14px] font-semibold rounded-full hover:bg-[#6B82FF] transition-all shadow-lg shadow-[#3B5BFF]/20 hover:-translate-y-0.5" style="color: var(--cta-text);">
    <svg class="w-[18px] h-[18px] shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M19.5 14.25v-2.625a3.375 3.375 0 00-3.375-3.375h-1.5A1.125 1.125 0 0113.5 7.125v-1.5a3.375 3.375 0 00-3.375-3.375H8.25m0 12.75h7.5m-7.5 3H12M10.5 2.25H5.625c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125V11.25a9 9 0 00-9-9z"/></svg>
    Request a Quote
</a>
```
With:
```html
<a href="mailto:hello@veehive.ai"
   class="group inline-flex items-center justify-center gap-2.5 px-8 py-3.5 bg-[#3B5BFF] text-[14px] font-semibold rounded-full hover:bg-[#6B82FF] transition-all shadow-lg shadow-[#3B5BFF]/20 hover:-translate-y-0.5" style="color: var(--cta-text);">
    <svg class="w-[18px] h-[18px] shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M21.75 6.75v10.5a2.25 2.25 0 01-2.25 2.25h-15a2.25 2.25 0 01-2.25-2.25V6.75m19.5 0A2.25 2.25 0 0019.5 4.5h-15a2.25 2.25 0 00-2.25 2.25m19.5 0v.243a2.25 2.25 0 01-1.07 1.916l-7.5 4.615a2.25 2.25 0 01-2.36 0L3.32 8.91a2.25 2.25 0 01-1.07-1.916V6.75"/></svg>
    Email Us
</a>
```

- [ ] **Step 5: Update footer — Products column (lines 1648-1658)**

Replace the HiveLabs link (line 1655):
```html
<li><a href="hivelabs.html" class="text-[14px] text-white/45 hover:text-white transition-colors">HiveLabs <span class="text-white/20 text-[11px]">Services</span></a></li>
```
With:
```html
<li><a href="https://veehivelabs.com" target="_blank" rel="noopener noreferrer" class="text-[14px] text-white/45 hover:text-white transition-colors">Custom Development <span class="text-white/20 text-[11px]">veehivelabs.com</span></a></li>
```

Change footer heading from "Modules & Services" to "Products":
```html
<h4 class="text-[12px] font-semibold uppercase tracking-[0.15em] text-white/30 mb-5">Products</h4>
```

- [ ] **Step 6: Update footer — Company column (lines 1660-1670)**

Remove these lines:
```html
<li><a href="case-studies.html" class="text-[14px] text-white/45 hover:text-white transition-colors">Case Studies</a></li>
```
```html
<li><a href="request-quote.html" class="text-[14px] text-white/45 hover:text-white transition-colors">Request a Quote</a></li>
```

- [ ] **Step 7: Commit**

```bash
git add public/index.html
git commit -m "Remove HiveLabs section, update CTA and footer for veehive.ai"
```

---

### Task 8: Update about.html — Meta Tags & Structured Data

**Files:**
- Modify: `public/about.html` (lines 1-320)

- [ ] **Step 1: Update title (line 12)**

Replace:
```
About Veehive | Dubai AI Company - Team, Case Studies & Capabilities
```
With:
```
About Veehive | Dubai AI Company - Team & Capabilities
```

- [ ] **Step 2: Update meta description (line 13)**

Remove "explore case studies with Rayna Tours, Costa Cruises, and" and "Veehive Labs" references:
```
"Veehive.ai is a Dubai-based applied AI innovation company. Products: SnapaPro, mpliphi, Studio, HiveLink. Meet our team and discover our AI capabilities. Dubai AI Seal certified."
```

- [ ] **Step 3: Update meta keywords (line 14)**

Remove "Veehive Labs" and "AI case studies":
```
"Veehive, Veehive Products, Dubai AI company, enterprise AI team, AI development Dubai, GenAI products, conversational AI, agentic AI, NVIDIA Inception, SnapaPro, mpliphi, Studio, HiveLink, TikTok for Business"
```

- [ ] **Step 4: Update author (line 15)**

Change `"Veehive Labs"` → `"Veehive.ai"`

- [ ] **Step 5: Update all veehivelabs.com URLs to veehive.ai**

Lines 17, 22, 25, 31, 34, 50, 57, 209, 215, 227 — replace `veehivelabs.com` with `veehive.ai`

- [ ] **Step 6: Update OG/Twitter descriptions**

- Line 24: Remove "case studies" → `"Meet the team behind Veehive. Explore our AI capabilities and enterprise credentials. Dubai AI Seal Tier E certified."`
- Line 26: Change `og:site_name` from `"Veehive Labs"` → `"Veehive.ai"`
- Line 33: Remove "case studies" → `"Meet the team behind Veehive. Explore our enterprise capabilities."`

- [ ] **Step 7: Update AboutPage structured data (line 49)**

Change description to remove "case studies":
```
"Veehive.ai is a Dubai-based applied AI innovation company building GenAI products faster and smarter. Products include SnapaPro, mpliphi, Studio, and HiveLink."
```

- [ ] **Step 8: Remove alternateName arrays**

- Line 56: Remove `"alternateName": ["HiveLabs by Veehive", "Veehive Labs"],`
- Line 162: Remove `"alternateName": ["HiveLabs by Veehive", "Veehive Labs"],`

- [ ] **Step 9: Update Organization name references**

Change `"Veehive Products"` to `"Veehive.ai"` wherever it appears as the Organization name (lines 55, 150, 161, 226).

- [ ] **Step 10: Update og:site_name (line 26)**

Change `"Veehive Labs"` → `"Veehive.ai"`

- [ ] **Step 11: Remove "What case studies" FAQ entry (lines 288-295)**

Delete the entire FAQ Question object for "What case studies does Veehive have?" and its trailing comma.

- [ ] **Step 12: Update GA4 tracking script (line 8)**

Same changes as Task 4:
1. `veehivelabs.com` → `veehive.ai` in isExternal check
2. Remove `hivelabs.html`, `request-quote`, `case-studies` event tracking
3. Add `veehivelabs.com` → `click_custom_dev` tracking

- [ ] **Step 13: Commit**

```bash
git add public/about.html
git commit -m "Update about.html meta tags and structured data for veehive.ai"
```

---

### Task 9: Update about.html — Navigation, Content & Footer

**Files:**
- Modify: `public/about.html` (lines 530-920)

- [ ] **Step 1: Update desktop nav — remove case-studies link and add Custom Dev**

The about.html nav has no HiveLabs link in desktop nav, but has case-studies in mobile. Add Custom Dev link after HiveLink in desktop nav (line 543 area):

After the HiveLink nav link, add:
```html
<a href="https://veehivelabs.com" target="_blank" rel="noopener noreferrer" class="px-3 py-1.5 text-[13px] text-white/50 hover:text-white transition-colors rounded-md hover:bg-white/[0.04]">Custom Dev</a>
```

- [ ] **Step 2: Update mobile nav (lines 569-580)**

Remove the case-studies link (line 576):
```html
<a href="case-studies.html" class="py-2.5 text-[14px] text-white/60 hover:text-white">Case Studies</a>
```

Add Custom Dev link after the About link:
```html
<a href="https://veehivelabs.com" target="_blank" rel="noopener noreferrer" class="py-2.5 text-[14px] text-white/60 hover:text-white">Custom Dev</a>
```

- [ ] **Step 3: Remove "Explore HiveLabs" and "Case Studies" buttons from hero (lines 613-619)**

Delete these two links:
```html
<a href="hivelabs.html" class="group inline-flex items-center gap-2 px-6 py-3 text-[14px] font-medium text-white/80 border border-white/[0.12] rounded-full hover:bg-white/[0.05] hover:border-white/[0.2] transition-all">
    Explore HiveLabs
    <svg ...></svg>
</a>
<a href="case-studies.html" class="inline-flex items-center gap-2 px-6 py-3 text-[14px] font-medium text-white/50 hover:text-white/80 transition-colors">
    Case Studies
</a>
```

- [ ] **Step 4: Update Mission text (line 737)**

Replace:
```
Build agentic AI systems that actually work. We combine four autonomous product modules with HiveLabs custom development to deliver enterprise-grade AI that plans, creates, distributes, and tracks — turning intent into execution in minutes.
```
With:
```
Build agentic AI systems that actually work. Our four autonomous product modules deliver enterprise-grade AI that plans, creates, distributes, and tracks — turning intent into execution in minutes.
```

- [ ] **Step 5: Replace "Explore More" section cards (lines 745-784)**

Replace the 3-card grid (HiveLabs card + Case Studies card + Team card) with a 2-card grid:

Replace `<div class="grid md:grid-cols-3 gap-5">` with `<div class="grid md:grid-cols-2 gap-5">`

Delete the HiveLabs card (lines 749-759):
```html
<a href="hivelabs.html" class="reveal group card-glow rounded-2xl p-8 block">
    ...HiveLabs card content...
</a>
```

Delete the Case Studies card (lines 760-770):
```html
<a href="case-studies.html" class="reveal group card-glow rounded-2xl p-8 block">
    ...Case Studies card content...
</a>
```

Add a Custom Development card before the Team card:
```html
<a href="https://veehivelabs.com" target="_blank" rel="noopener noreferrer" class="reveal group card-glow rounded-2xl p-8 block">
    <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#8B5CFF]/10 border border-[#8B5CFF]/15 mb-4">
        <span class="text-[12px] font-semibold text-[#8B5CFF] uppercase tracking-wider">Services</span>
    </div>
    <h3 class="text-xl font-bold tracking-tight mb-2">Custom Development</h3>
    <p class="text-[14px] text-white/40 leading-relaxed mb-5">Need something bespoke? Custom AI agents, SLM configuration, and enterprise integrations.</p>
    <div class="flex items-center gap-2 text-[13px] font-medium text-white/50 group-hover:text-white transition-all">
        veehivelabs.com
        <svg class="w-3.5 h-3.5 group-hover:translate-x-0.5 transition-transform" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M13 7l5 5m0 0l-5 5m5-5H6"/></svg>
    </div>
</a>
```

- [ ] **Step 6: Update footer — remove case-studies link (line 877)**

Delete:
```html
<li><a href="case-studies.html" class="text-[14px] text-white/45 hover:text-white transition-colors">Case Studies</a></li>
```

Add Custom Development link in the Products column (after HiveLink, line 869):
```html
<li><a href="https://veehivelabs.com" target="_blank" rel="noopener noreferrer" class="text-[14px] text-white/45 hover:text-white transition-colors">Custom Development</a></li>
```

- [ ] **Step 7: Commit**

```bash
git add public/about.html
git commit -m "Update about.html: remove HiveLabs/case-studies content, add Custom Dev links"
```

---

### Task 10: Update team.html

**Files:**
- Modify: `public/team.html`

- [ ] **Step 1: Update GA4 tracking script (line 8)**

Same changes as Task 4 (veehive.ai domain, remove hivelabs/request-quote/case-studies events, add custom dev event).

- [ ] **Step 2: Update meta author (line 15)**

Change `"Veehive Labs"` → `"Veehive.ai"`

- [ ] **Step 3: Update all veehivelabs.com URLs**

Lines 17, 21, 24, 25, 38, 39, 40 — replace `veehivelabs.com` with `veehive.ai`

- [ ] **Step 4: Update og:site_name (line 25)**

Change `"Veehive Labs"` → `"Veehive.ai"`

- [ ] **Step 5: Update navigation**

The team.html nav follows a different pattern than index.html. Find the nav links and:
- Replace the HiveLabs link with Custom Dev link (both desktop and mobile)
- If case-studies link exists in nav, remove it

- [ ] **Step 6: Update footer**

Same pattern as other pages:
- Remove HiveLabs/case-studies/request-quote links
- Add Custom Development link

- [ ] **Step 7: Commit**

```bash
git add public/team.html
git commit -m "Update team.html for veehive.ai domain and navigation"
```

---

### Task 11: Update hivelink.html

**Files:**
- Modify: `public/hivelink.html`

- [ ] **Step 1: Update GA4 tracking script (line 8)**

Same changes as Task 4.

- [ ] **Step 2: Update all veehivelabs.com URLs in meta tags**

Replace all `veehivelabs.com` with `veehive.ai` in meta tags, canonical, og:url, og:image, twitter:url, twitter:image, and structured data.

- [ ] **Step 3: Update navigation**

Replace HiveLabs nav link with Custom Dev link (desktop + mobile), same pattern as Task 6.

- [ ] **Step 4: Update footer**

Same pattern as Task 7:
- Replace HiveLabs link with Custom Development link
- Remove case-studies and request-quote links

- [ ] **Step 5: Commit**

```bash
git add public/hivelink.html
git commit -m "Update hivelink.html for veehive.ai domain and navigation"
```

---

### Task 12: Update Firebase Configuration

**Files:**
- Modify: `.firebaserc`
- Modify: `firebase.json`

- [ ] **Step 1: Update .firebaserc with new project ID**

The user needs to create a new Firebase project first. Once they provide the project ID, update:

```json
{
  "projects": {
    "default": "<new-project-id>"
  }
}
```

- [ ] **Step 2: Update firebase.json rewrites**

Remove the `/about` rewrite (keeping clean URL fallback). Update to:

```json
{
  "hosting": {
    "public": "public",
    "ignore": [
      "firebase.json",
      "**/.*",
      "**/node_modules/**"
    ],
    "rewrites": [
      {
        "source": "**",
        "destination": "/index.html"
      }
    ],
    "headers": [
      {
        "source": "**/*.@(jpg|jpeg|gif|png|svg|webp|ico)",
        "headers": [
          {
            "key": "Cache-Control",
            "value": "max-age=31536000"
          }
        ]
      },
      {
        "source": "**/*.@(js|css)",
        "headers": [
          {
            "key": "Cache-Control",
            "value": "max-age=31536000"
          }
        ]
      }
    ]
  }
}
```

- [ ] **Step 3: Commit**

```bash
git add .firebaserc firebase.json
git commit -m "Update Firebase config for veehive.ai project"
```

---

### Task 13: Final Verification Sweep

- [ ] **Step 1: Search for any remaining veehivelabs.com references**

```bash
grep -r "veehivelabs" public/ .firebaserc firebase.json
```

Expected: No results. If any found, fix them.

- [ ] **Step 2: Search for any remaining hivelabs references**

```bash
grep -ri "hivelabs\|hive-labs\|hive labs" public/
```

Expected: No results (except possibly the new Custom Development link to veehivelabs.com). If any content references found, fix them.

- [ ] **Step 3: Search for references to deleted pages**

```bash
grep -r "request-quote\|case-studies\|google37d8949" public/
```

Expected: No results. If found, fix them.

- [ ] **Step 4: Search for "Veehive Labs" or "Veehive Products" branding**

```bash
grep -ri "Veehive Labs\|Veehive Products" public/
```

Expected: No results. If found, replace with "Veehive.ai".

- [ ] **Step 5: Open each page in browser and verify**

Check each page loads without 404s for links:
- `index.html` — nav links work, no HiveLabs section, footer clean
- `about.html` — no HiveLabs/case-studies buttons, explore section has 2 cards
- `team.html` — nav and footer clean
- `hivelink.html` — nav and footer clean

- [ ] **Step 6: Commit any fixes**

```bash
git add -A
git commit -m "Fix remaining veehivelabs references found during verification sweep"
```

---

### Task 14: Create New GitHub Repo & Push

- [ ] **Step 1: Create new GitHub repo**

```bash
gh repo create Veehive-ai/veehive.ai --public --description "Veehive.ai — The Agentic Operating System for Marketing Execution"
```

- [ ] **Step 2: Initialize fresh git and push**

```bash
cd "/Users/imsats/myproject/Website Veehive.ai"
# Remove old git history
rm -rf .git
git init
git add .
git commit -m "Initial commit: veehive.ai website"
git branch -M main
git remote add origin https://github.com/Veehive-ai/veehive.ai.git
git push -u origin main
```

Note: This is destructive to the old git history. The veehivelabs-website repo remains untouched on GitHub as a separate repo.

- [ ] **Step 3: Verify repo on GitHub**

```bash
gh repo view Veehive-ai/veehive.ai --web
```
