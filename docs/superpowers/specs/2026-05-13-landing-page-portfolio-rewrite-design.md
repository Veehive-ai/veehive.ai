# Veehive.ai Landing Page — Portfolio Rewrite

**Date:** 2026-05-13
**File touched:** `public/index.html` (single file)
**Source brief:** `LANDING-PAGE-REWRITE-PROMPT.md` (root)

## Why

The current landing page sells Veehive.ai as a fictional "unified AI marketing platform" with one prompt driving all four products. That product does not exist. The four products (mpliphi, Studio, SnapaPro, Veehive Link) are independent tools for different audiences. The page misrepresents reality, confuses visitors who arrive looking for one specific product, and excludes audiences (support teams, project managers) whose problems Veehive already solves.

The rewrite reframes the page as an honest **company portfolio**: four independent products, four different audiences, one company that builds them.

## Goals

1. Route visitors to the right product in under 10 seconds
2. Replace the fictional unified-platform framing with accurate per-product positioning
3. Build trust in Veehive as a credible Dubai-based applied-AI company
4. Preserve the three working CTAs (Outlook booking, WhatsApp, mailto) — no new backend
5. Keep the existing design system intact (CSS variables, theme toggle, `card-glow` system, animations)

## Non-Goals

- Other pages (`about.html`, `team.html`, `privacy.html`, `terms.html`)
- Footer or nav changes
- New images or assets
- Form backend or Firebase Cloud Function
- A/B testing infrastructure
- Per-product deep dives (each product's own site handles that)

## Scope of Edit

- **File:** `public/index.html` only
- **Replace:** body content between `</nav>` (~line 836) and `<!-- FOOTER -->` (~line 1741) — approximately 900 lines
- **Update:** `<head>` — `<title>`, meta description, keywords, OG/Twitter cards, Organization JSON-LD `description`, FAQPage JSON-LD `mainEntity`
- **Preserve verbatim:** GA4 script, theme toggle, CSS variables, all `<style>` class definitions (`card-glow`, `card-glow-orchestrator/creator/planner/distributor`, `trust-card`, `shimmer-badge`, `fade-up`, `reveal`, `nav-blur`, ambient orb classes), `<nav>`, mobile menu, `<footer>`, scroll-reveal script

## New Body Structure

Seven sections, top to bottom. Each wrapped in `reveal` class for scroll-triggered fade-in.

### 1. Hero — Capability-first

- Eyebrow: keep existing **Dubai AI Seal Certified** shimmer badge
- Headline: **We build AI that works.**
- Sub: **Four independent products. Pick the one for your problem.**
- Pill row (chosen layout: neutral pills with colored dots). Each pill is an anchor link:
  - mpliphi → `#mpliphi` (green dot `#16A34A`)
  - Studio → `#studio` (purple dot `#7C3AED`)
  - SnapaPro → `#snapapro` (red dot `#DC2626`)
  - Veehive Link → `#veehive-link` (blue dot `#2563EB`)
- Primary CTA: **Book a Demo** → existing Outlook URL (`https://outlook.office.com/bookwithme/user/4b235448860a484991237c062357501e@veehive.ai?anonymous&ismsaljsauthenabled&ep=plink`)
- Remove: stats row, "one prompt, full campaign" copy, "4 AI modules" framing

### 2. Problem Matcher — Click to reveal

- Heading: **What problem are you solving?**
- Four pain-point cards in a 2×2 grid on desktop, single column on mobile. Each uses `trust-card` + `card-glow` with product-specific glow class for hover:
  1. **"Customer replies are drowning us"** — `card-glow-orchestrator` — recommends **mpliphi**
  2. **"Content takes too long to produce"** — `card-glow-creator` — recommends **Studio**
  3. **"Projects slip through the cracks"** — `card-glow-planner` — recommends **SnapaPro**
  4. **"Distribution is a mess of tools"** — `card-glow-distributor` — recommends **Veehive Link**
- Recommendation reveal: chosen behavior is **inline panel below the grid**. Clicking a card:
  - Adds a `selected` state to the clicked card (accent border in product color)
  - Removes `selected` from any previously selected card
  - Shows a recommendation panel below the grid with: product name (large), one-line pitch, "Explore →" external link
  - Selecting a different card swaps the panel's content
- Implementation: single inline `<script>` block (~20 lines vanilla JS). Cards have `data-product` attribute. One `<div id="problem-match-result">` toggles visibility and innerHTML.

### 3. Product Showcases (×4) — Stacked single column

Order: **mpliphi → Studio → SnapaPro → Veehive Link** (broadest appeal first).

Each card structure (chosen layout: stacked single column, generous whitespace):
- Audience eyebrow tag in product accent color (`text-transform: uppercase`, `letter-spacing: 0.1em`)
- Product name (large, bold)
- Category badge next to name
- 2–3 sentence pitch
- Three stats in a row (separated by `·` on mobile, in a flex row on desktop)
- "Explore [Product] →" external link with `target="_blank" rel="noopener noreferrer"`

Each card wrapper has the matching `card-glow-*` class and an `id` for hero pill anchors:

| Product | Card id | Glow class | Audience eyebrow | Category badge | Pitch | Stats | External URL |
|---|---|---|---|---|---|---|---|
| mpliphi | `mpliphi` | `card-glow-orchestrator` | For support + operations teams | AI Agents | AI agents that handle customer conversations on WhatsApp and email — autonomously or as copilots alongside your team. Choose fully autonomous or human-in-the-loop. 50+ languages out of the box. | 50K+ conversations / month · 50+ languages · From $299/mo | https://mpliphi.com |
| Studio | `studio` | `card-glow-creator` | For content + marketing teams | AI Video | Turn documents and PDFs into branded videos with AI avatars and voiceover. Built for training, marketing, and customer education. 30+ languages. | 10× faster creation · 30+ languages · From $1,300/mo | https://veehivestudio.com |
| SnapaPro | `snapapro` | `card-glow-planner` | For project managers + team leads | AI Planning | AI project management powered by three agents — Taj plans, Noor engages, Sats tracks time. Natural-language task creation, capacity planning, dashboards. | 3 AI agents · Natural-language tasks · Capacity planning | https://snapapro.com |
| Veehive Link | `veehive-link` | `card-glow-distributor` | For marketing + community managers | AI Distribution | Six modules in one: video hosting, social scheduling, community, events, CRM, campaigns. White-label with custom domains. On-premise available. | 6 modules in one · 24/7 AI agent · White-label + on-prem | https://veehivelink.com |

Do **not** describe how the products connect to each other. They are independent.

### 4. Trust & Credibility

Consolidate existing trust content into one section:
- Heading: **Built in Dubai. Trusted globally.**
- Partners & Accelerators row (keep existing logos: NVIDIA Inception, In5 Tech, Microsoft for Startups if present)
- Compliance badge row: Dubai AI Seal Tier E · SOC 2 Type II · ISO 27001 aligned · GDPR
- "As Seen In" logo row (keep if present in current page: The Hindu, Dubai One, Red Bull, World Economic Forum)
- Footer line: **Veehive Tech FZ LLC · In5 Tech, Dubai Internet City**

Drop the 8-bullet security deep dive — badges only here; individual product sites carry their own detail.

### 5. About Promo (kept, repositioned)

The existing "About Promo" section (currently at ~line 1605 of `public/index.html`) reinforces "we're a real company that builds things." Keep its inner content verbatim — pull the existing `<section>` block as-is and place it between Trust and Lead Capture. No copy changes.

### 6. Lead Capture / CTA — Three CTAs, no form

- Heading: **Not sure which product fits?**
- Sub: **Tell us what you're trying to solve. We'll point you to the right tool.**
- Three CTA buttons using existing button styles:
  1. **Book a Demo** (primary, blue) → existing Outlook URL
  2. **WhatsApp us** (secondary) → `https://wa.me/971564308275`
  3. **Email us** (tertiary) → `mailto:contact@veehive.ai`
- Section keeps `id="contact"` so the nav anchor still works
- No form, no email input — matches what the current page already does and what works with no backend

### 7. FAQ (rewrite)

Reuse existing accordion markup. Replace content with six entries:

| Question | Answer |
|---|---|
| What is Veehive.ai? | Veehive is a Dubai-based applied-AI company. We build four independent AI products for different teams — not a single unified platform. |
| What products does Veehive build? | mpliphi (customer-conversation agents), Studio (document-to-video AI), SnapaPro (AI project management), Veehive Link (content + community + CRM). |
| Are the products connected? | No. Each product solves one problem for one audience and stands on its own. Buy what you need. |
| Is Veehive secure? | Yes — Dubai AI Seal Tier E certified, SOC 2 Type II controls implemented, ISO 27001 aligned, GDPR-ready. |
| Where is Veehive based? | Dubai, UAE — at In5 Tech in Dubai Internet City. We operate as Veehive Tech FZ LLC. |
| What if I need custom AI development? | That's VeehiveLabs (veehivelabs.com) — our applied-AI consulting arm for bespoke builds. |

## `<head>` Updates

| Tag | New value |
|---|---|
| `<title>` | `Veehive.ai — Applied AI from Dubai. Four AI products, one company.` |
| `<meta name="description">` | `Veehive is a Dubai-based applied-AI company building four independent products: mpliphi (customer conversations), Studio (AI video), SnapaPro (project management), and Veehive Link (content + community). Dubai AI Seal Tier E certified.` |
| `<meta name="keywords">` | Remove "marketing execution", "AI operating system", "agentic operating system". Keep product names, "Dubai AI", "applied AI", "AI agents", "AI video", "AI project management", "Veehive Link", "Veehive Tech", "enterprise AI". |
| `og:title` / `twitter:title` | Match new `<title>` |
| `og:description` / `twitter:description` | Match new meta description |
| Organization JSON-LD `description` | Match new meta description |
| FAQPage JSON-LD `mainEntity` | Replace existing entries with the six new Q/A pairs from section 7 (verbatim text in the `acceptedAnswer.text` fields) |
| `og:image` / `twitter:image` | Unchanged (`og-image.png`) |

## Sections Deleted Entirely

All sell the fictional unified platform:
- "Who This Is For" (marketing-team checklist)
- "See It In Action" (Ramadan campaign walkthrough)
- "The Problem" (7+ tools / 3× longer / 40% wasted)
- "The Solution — One System, Four Layers"
- "The Veehive System" architecture diagram (One Brain, Three Agents)
- PLAN / RESPOND / CREATE / DISTRIBUTE module cards
- "How It Works" Intent-to-Execution four-step flow
- "Security & Compliance" eight-bullet deep dive (badges keep their slot in Trust)
- Hero stats row aggregating across products

## Technical Approach

- **Single-file edit** to `public/index.html`. No new files.
- **No new CSS classes.** Reuse `card-glow`, `card-glow-orchestrator/creator/planner/distributor`, `trust-card`, `shimmer-badge`, `fade-up`, `reveal`, `nav-blur`, existing button styles.
- **One new inline script** (~20 lines vanilla JS) for the Problem Matcher click→reveal. Place it adjacent to the existing scroll-reveal script at the bottom of `<body>`.
- **Smooth scroll:** add `html { scroll-behavior: smooth; }` to the `<style>` block if not already present, so hero pills scroll cleanly.
- **Responsive:** all new sections use the existing breakpoints (`lg:`) and grid patterns.
- **Reveal animations:** wrap each new section in `reveal`.
- **Analytics:** the global click handler in `<head>` already maps GA4 events for every URL we use (Outlook, WhatsApp, mailto, snapapro.com, mpliphi.com, veehivestudio.com, veehivelink.com). No new tracking code.
- **External links:** all four product cards use `target="_blank" rel="noopener noreferrer"`.

## Test Plan

1. Manual visual check at desktop, tablet (768–1024px), mobile (≤640px) via Chrome DevTools
2. Theme toggle works in both directions; product accent colors remain legible in light mode
3. Each of the four hero pills anchor-scrolls to its product card
4. Problem Matcher: clicking each card highlights it and reveals the matching recommendation; switching cards swaps the panel; previously selected card de-highlights
5. All four "Explore →" links open the correct external domain in a new tab
6. Three lead-capture CTAs fire correct GA4 events (verify in Network → `collect` calls): `click_book_demo`, `click_whatsapp`, `click_email`
7. Run existing Playwright test `tests/live-veehive-link.spec.ts` to confirm the Veehive Link link still resolves correctly
8. JSON-LD validates against the [Schema.org validator](https://validator.schema.org/)
9. Confirm `<head>` `<title>` and meta description render correctly in social-share previews (use a debugger like [opengraph.xyz](https://www.opengraph.xyz/))

## Risks & Mitigations

| Risk | Mitigation |
|---|---|
| 900-line body replacement could regress visual polish | Keep all CSS classes untouched; only HTML content changes |
| Existing FAQPage JSON-LD content already indexed by Google — sudden change may temporarily hurt rankings | Acceptable: current FAQ describes a fictional product, current state is worse than the change |
| Problem Matcher JS breaks on older browsers | Use only ES5-safe vanilla JS (no arrow functions, no `?.`); no dependencies |
| Theme variables on new accent colors look bad in light mode | Spot-check both modes during manual test; existing `card-glow-*` classes already have light-mode variants in the CSS |
| Hero pill anchors clash with nav-blur header on scroll | Add `scroll-margin-top` to each product card section equal to nav height (~80px) |
