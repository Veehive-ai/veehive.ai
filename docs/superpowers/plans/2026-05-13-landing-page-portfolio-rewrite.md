# Landing Page Portfolio Rewrite — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rewrite the body of [public/index.html](public/index.html) and refresh its `<head>` SEO so the page presents Veehive.ai as a company portfolio of four independent AI products (mpliphi, Studio, SnapaPro, Veehive Link), replacing the fictional "unified marketing platform" narrative.

**Architecture:** Single-file edit. Replace body content between `</nav>` (~line 836) and `<!-- FOOTER -->` (~line 1741) with seven new sections (Hero → Problem Matcher → 4 Product Showcases → Trust → About Promo → Lead Capture → FAQ). Refresh `<head>` `<title>`, meta description/keywords, OG/Twitter cards, Organization JSON-LD `description`, and FAQPage JSON-LD `mainEntity`. Reuse all existing CSS classes — no new styles. Add one ~30-line vanilla JS block for the Problem Matcher click-to-reveal (uses DOM methods, not innerHTML).

**Tech Stack:** Static HTML, Tailwind CSS (via `/tailwind.min.css`), vanilla ES5 JS, hosted on Firebase Hosting. No build step. No framework.

**Spec:** [docs/superpowers/specs/2026-05-13-landing-page-portfolio-rewrite-design.md](docs/superpowers/specs/2026-05-13-landing-page-portfolio-rewrite-design.md)

---

## Files Touched

- **Modify:** `public/index.html` (single file — every task below touches this file)

That's it. No new files. No asset changes. No CSS additions. No JS additions outside the inline `<script>` block.

## Reference Material You'll Need

Before starting, open these in tabs:
- The current file: [public/index.html](public/index.html) — 1850 lines
- The spec: `docs/superpowers/specs/2026-05-13-landing-page-portfolio-rewrite-design.md`
- The existing Playwright test: [tests/live-veehive-link.spec.ts](tests/live-veehive-link.spec.ts) — **runs against production `https://veehive.ai`, not localhost.** It won't validate the rewrite until deployed. We'll do manual verification before each commit instead.

## Key existing classes (do NOT redefine these — they're already in `<style>`)

| Class | What it does | Defined at (approx) |
|---|---|---|
| `card-glow` | Base card hover-glow effect | line ~539 |
| `card-glow-orchestrator` | Green hover glow (for mpliphi) | line 543 |
| `card-glow-creator` | Purple hover glow (for Studio) | line 545 |
| `card-glow-planner` | Red hover glow (for SnapaPro) | line 541 |
| `card-glow-distributor` | Blue hover glow (for Veehive Link) | line 547 |
| `card-glow-mustard` | Blue-violet glow used by About Promo today | line 551 |
| `trust-card` | Standard card background + border | line 562 |
| `shimmer-badge` | The animated eyebrow pill in the hero | (search file) |
| `fade-up` / `animate-fade-up` + `delay-N00` | Staggered fade-in on load | (search file) |
| `reveal` / `reveal.visible` | Scroll-triggered fade-in | line 587 |
| `faq-open` toggled on FAQ accordion item to expand | line 768 |
| `divider-gradient` | The thin horizontal divider used between sections | (search file) |
| `text-gradient` | Gradient text effect used for italic emphasis | (search file) |

`html { scroll-behavior: smooth; }` is **already present** at line 417 — no need to add it.

## Verification commands you'll re-use

```bash
# Open the page locally in your default browser
open "/Users/imsats/myproducts/Website Veehive.ai/public/index.html"

# Or serve via Firebase locally (preferred — matches production routing)
cd "/Users/imsats/myproducts/Website Veehive.ai" && npx firebase emulators:start --only hosting
# Then open http://localhost:5000

# Validate that JSON-LD is still parseable
node -e "const fs=require('fs');const html=fs.readFileSync('/Users/imsats/myproducts/Website Veehive.ai/public/index.html','utf8');const m=html.match(/<script type=\"application\\/ld\\+json\">([\\s\\S]*?)<\\/script>/g);if(!m){console.error('NO JSON-LD');process.exit(1);}m.forEach((s,i)=>{const body=s.replace(/<\\/?script[^>]*>/g,'');try{JSON.parse(body);console.log('block',i+1,'OK');}catch(e){console.error('block',i+1,'INVALID:',e.message);process.exit(1);}});"
```

---

## Strategy

We replace the body **in place, section by section**, so the file stays valid HTML at every commit. The order below mirrors the final page top-to-bottom — earlier tasks modify higher-up sections.

For each task: open the file, find the section by its marker comment, replace it. Commit after each task so any visual regression is bisectable.

**Branch safety:** before starting, confirm you're on `main` with no uncommitted work in `public/index.html`. Run:

```bash
cd "/Users/imsats/myproducts/Website Veehive.ai" && git status -s public/index.html
# Expected output: empty
```

If anything is shown, stash or commit it first.

---

## Task 1: Update the Hero section (replace, don't delete)

**Files:**
- Modify: `public/index.html` lines 838–914 (the `HERO SECTION` block)

The new hero keeps the shimmer badge but changes the headline, sub, CTAs, and removes the stats row.

- [ ] **Step 1: Read the existing hero**

Open `public/index.html` and locate the section delimited by `<!-- HERO SECTION -->` (line 839) and its closing `</section>` (line 914). Confirm those lines match — line numbers will drift as you edit.

- [ ] **Step 2: Replace the entire hero block**

Replace lines 838–914 with the following:

```html
    <!-- ═══════════════════════════════════════ -->
    <!-- HERO SECTION -->
    <!-- ═══════════════════════════════════════ -->
    <section class="relative z-10 pt-32 pb-20 lg:pt-40 lg:pb-28">
        <div class="max-w-7xl mx-auto px-6 lg:px-8">
            <!-- Status badge -->
            <div class="animate-fade-up mb-10">
                <div class="inline-flex items-center gap-2.5 px-4 py-2 rounded-full border border-white/[0.08] bg-white/[0.03] shimmer-badge">
                    <span class="relative flex h-2 w-2">
                        <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-[#3B5BFF] opacity-75"></span>
                        <span class="relative inline-flex rounded-full h-2 w-2 bg-[#3B5BFF]"></span>
                    </span>
                    <span class="text-[13px] text-white/60 font-medium">Dubai AI Seal Certified &middot; Applied AI from Dubai</span>
                </div>
            </div>

            <!-- Heading -->
            <h1 class="animate-fade-up delay-100">
                <span class="block text-[clamp(2.4rem,6.5vw,5rem)] font-display font-bold leading-[1.05] tracking-[-0.02em] text-white">We build AI</span>
                <span class="block text-[clamp(2.4rem,6.5vw,5rem)] font-display font-bold leading-[1.05] tracking-[-0.02em]">
                    <span class="text-gradient">that works.</span>
                </span>
            </h1>

            <!-- Subheading -->
            <p class="animate-fade-up delay-200 mt-8 text-lg md:text-xl max-w-2xl leading-relaxed font-light" style="color: var(--text-secondary);">
                Four independent AI products. Four different teams. Pick the one for your problem &mdash; or talk to us about all four.
            </p>

            <!-- Product pills (anchor links into showcases below) -->
            <div class="animate-fade-up delay-300 mt-10 flex flex-wrap gap-3">
                <a href="#mpliphi" class="inline-flex items-center gap-2.5 px-5 py-2.5 rounded-full border border-white/[0.1] bg-white/[0.04] text-[14px] font-semibold text-white hover:bg-white/[0.08] hover:border-white/[0.18] transition-all">
                    <span class="inline-block w-2 h-2 rounded-full" style="background:#16A34A"></span>
                    mpliphi
                </a>
                <a href="#studio" class="inline-flex items-center gap-2.5 px-5 py-2.5 rounded-full border border-white/[0.1] bg-white/[0.04] text-[14px] font-semibold text-white hover:bg-white/[0.08] hover:border-white/[0.18] transition-all">
                    <span class="inline-block w-2 h-2 rounded-full" style="background:#7C3AED"></span>
                    Studio
                </a>
                <a href="#snapapro" class="inline-flex items-center gap-2.5 px-5 py-2.5 rounded-full border border-white/[0.1] bg-white/[0.04] text-[14px] font-semibold text-white hover:bg-white/[0.08] hover:border-white/[0.18] transition-all">
                    <span class="inline-block w-2 h-2 rounded-full" style="background:#DC2626"></span>
                    SnapaPro
                </a>
                <a href="#veehive-link" class="inline-flex items-center gap-2.5 px-5 py-2.5 rounded-full border border-white/[0.1] bg-white/[0.04] text-[14px] font-semibold text-white hover:bg-white/[0.08] hover:border-white/[0.18] transition-all">
                    <span class="inline-block w-2 h-2 rounded-full" style="background:#2563EB"></span>
                    Veehive Link
                </a>
            </div>

            <!-- Primary CTA -->
            <div class="animate-fade-up delay-400 flex flex-wrap gap-3 mt-10">
                <a href="https://outlook.office.com/bookwithme/user/4b235448860a484991237c062357501e@veehive.ai?anonymous&ismsaljsauthenabled&ep=plink" target="_blank" rel="noopener noreferrer" class="group inline-flex items-center gap-2 px-7 py-3.5 bg-[#3B5BFF] text-white text-[14px] font-semibold rounded-full hover:bg-[#6B82FF] transition-all hover:-translate-y-0.5 shadow-lg shadow-[#3B5BFF]/20">
                    Book a Demo
                    <svg class="w-3.5 h-3.5 group-hover:translate-x-0.5 transition-transform" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5"><path stroke-linecap="round" stroke-linejoin="round" d="M13 7l5 5m0 0l-5 5m5-5H6"/></svg>
                </a>
                <a href="#contact" class="group inline-flex items-center gap-2 px-7 py-3.5 text-[14px] font-medium text-white/80 border border-white/[0.12] rounded-full hover:bg-white/[0.05] hover:border-white/[0.2] transition-all">
                    Get in touch
                    <svg class="w-3.5 h-3.5 opacity-40 group-hover:opacity-70 group-hover:translate-x-0.5 transition-all" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7"/></svg>
                </a>
            </div>
        </div>
    </section>
```

- [ ] **Step 3: Manual verification**

```bash
open "/Users/imsats/myproducts/Website Veehive.ai/public/index.html"
```

Confirm in the browser:
- Shimmer badge displays "Dubai AI Seal Certified · Applied AI from Dubai"
- Headline reads "We build AI that works." with "that works." in gradient
- Four pills appear, each with its colored dot
- Clicking each pill jumps the page (anchors don't exist yet — that's expected; we'll verify navigation after Task 4)
- Stats row is gone

- [ ] **Step 4: Commit**

```bash
cd "/Users/imsats/myproducts/Website Veehive.ai"
git add public/index.html
git commit -m "Rewrite hero: company-level positioning + product pills

Replaces 'set a campaign goal' headline and unified-platform copy with
'We build AI that works.' framing. Adds four anchor pills to the product
showcases (mpliphi, Studio, SnapaPro, Veehive Link). Removes the
cross-product stats row that aggregated across products.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

---

## Task 2: Replace "Who This Is For" with the Problem Matcher section

**Files:**
- Modify: `public/index.html` — the section delimited by `<!-- WHO THIS IS FOR -->` (line 917) through its closing `</section>` (line 948)
- Modify: the existing scroll-reveal `<script>` block at the bottom of `<body>` (search for `<!-- Scroll reveal + Theme toggle script -->`)

- [ ] **Step 1: Locate the section**

Find the comment `<!-- WHO THIS IS FOR -->` in `public/index.html`. Its closing `</section>` is the next one after that comment. Line numbers will have shifted from Task 1 — search by comment, not by line number.

- [ ] **Step 2: Replace the entire section**

Replace the WHO THIS IS FOR section (from the comment line through its closing `</section>`) with:

```html
    <!-- ═══════════════════════════════════════ -->
    <!-- PROBLEM MATCHER -->
    <!-- ═══════════════════════════════════════ -->
    <section class="relative z-10 py-20 lg:py-28">
        <div class="max-w-5xl mx-auto px-6 lg:px-8">
            <div class="reveal text-center mb-12">
                <p class="text-[13px] font-semibold uppercase tracking-[0.2em] text-[#3B5BFF]/60 mb-4">Problem Matcher</p>
                <h2 class="text-3xl md:text-4xl font-bold tracking-tight">What problem are you solving?</h2>
                <p class="mt-3 text-base text-white/40 max-w-xl mx-auto">Click the one that fits. We&rsquo;ll point you to the product built for it.</p>
            </div>

            <div class="reveal grid sm:grid-cols-2 gap-4" id="problem-matcher-grid">
                <button type="button" class="problem-card trust-card card-glow card-glow-orchestrator rounded-xl p-6 text-left transition-all" data-product="mpliphi">
                    <span class="block text-[12px] font-semibold uppercase tracking-[0.15em] mb-2" style="color:#16A34A">Support &amp; ops</span>
                    <span class="block text-[17px] font-semibold text-white/85 leading-snug">&ldquo;Customer replies are drowning us.&rdquo;</span>
                </button>
                <button type="button" class="problem-card trust-card card-glow card-glow-creator rounded-xl p-6 text-left transition-all" data-product="studio">
                    <span class="block text-[12px] font-semibold uppercase tracking-[0.15em] mb-2" style="color:#A78BFA">Content &amp; marketing</span>
                    <span class="block text-[17px] font-semibold text-white/85 leading-snug">&ldquo;Content takes too long to produce.&rdquo;</span>
                </button>
                <button type="button" class="problem-card trust-card card-glow card-glow-planner rounded-xl p-6 text-left transition-all" data-product="snapapro">
                    <span class="block text-[12px] font-semibold uppercase tracking-[0.15em] mb-2" style="color:#F87171">Project mgmt</span>
                    <span class="block text-[17px] font-semibold text-white/85 leading-snug">&ldquo;Projects slip through the cracks.&rdquo;</span>
                </button>
                <button type="button" class="problem-card trust-card card-glow card-glow-distributor rounded-xl p-6 text-left transition-all" data-product="veehive-link">
                    <span class="block text-[12px] font-semibold uppercase tracking-[0.15em] mb-2" style="color:#60A5FA">Marketing &amp; community</span>
                    <span class="block text-[17px] font-semibold text-white/85 leading-snug">&ldquo;Distribution is a mess of tools.&rdquo;</span>
                </button>
            </div>

            <div id="problem-match-result" class="reveal mt-6 hidden trust-card rounded-xl p-6 md:p-8" aria-live="polite"></div>
        </div>
    </section>
```

- [ ] **Step 3: Inject the click-to-reveal script (uses safe DOM methods)**

Find the existing scroll-reveal `<script>` block at the bottom of `<body>`. Search for `<!-- Scroll reveal + Theme toggle script -->` (around line 1817 originally). Open that script tag and **append** the following code immediately before its closing `</script>`:

```javascript

  /* Problem Matcher click-to-reveal. Uses DOM methods (no innerHTML)
     so trusted-types / CSP-strict environments stay happy. */
  (function () {
    var PRODUCTS = {
      'mpliphi':       { name: 'mpliphi',         color: '#16A34A', pitch: 'AI agents that handle customer conversations on WhatsApp and email — autonomously or as copilots alongside your team.', url: 'https://mpliphi.com' },
      'studio':        { name: 'Veehive Studio',  color: '#A78BFA', pitch: 'Turn documents and PDFs into branded videos with AI avatars and voiceover. Built for training, marketing, and customer education.', url: 'https://veehivestudio.com' },
      'snapapro':      { name: 'SnapaPro',        color: '#F87171', pitch: 'AI project management powered by three agents — Taj plans, Noor engages, Sats tracks time. Natural-language task creation and capacity planning.', url: 'https://snapapro.com' },
      'veehive-link':  { name: 'Veehive Link',    color: '#60A5FA', pitch: 'Six modules in one: video hosting, social scheduling, community, events, CRM, campaigns. White-label with custom domains.', url: 'https://veehivelink.com' }
    };
    var grid = document.getElementById('problem-matcher-grid');
    var panel = document.getElementById('problem-match-result');
    if (!grid || !panel) return;
    var cards = grid.querySelectorAll('.problem-card');

    function clearSelection() {
      for (var i = 0; i < cards.length; i++) {
        cards[i].style.borderColor = '';
        cards[i].style.boxShadow = '';
      }
    }

    function renderPanel(p) {
      // Clear panel
      while (panel.firstChild) panel.removeChild(panel.firstChild);
      // Eyebrow
      var eyebrow = document.createElement('div');
      eyebrow.className = 'text-[12px] font-semibold uppercase tracking-[0.15em] mb-2';
      eyebrow.style.color = p.color;
      eyebrow.textContent = 'We recommend';
      panel.appendChild(eyebrow);
      // Name
      var name = document.createElement('div');
      name.className = 'text-2xl md:text-3xl font-bold mb-3';
      name.textContent = p.name;
      panel.appendChild(name);
      // Pitch
      var pitch = document.createElement('p');
      pitch.className = 'text-[15px] text-white/55 leading-relaxed mb-5 max-w-2xl';
      pitch.textContent = p.pitch;
      panel.appendChild(pitch);
      // Explore link
      var link = document.createElement('a');
      link.href = p.url;
      link.target = '_blank';
      link.rel = 'noopener noreferrer';
      link.className = 'inline-flex items-center gap-1.5 text-[14px] font-semibold';
      link.style.color = p.color;
      link.textContent = 'Explore ' + p.name + ' →';
      panel.appendChild(link);
    }

    for (var i = 0; i < cards.length; i++) {
      cards[i].addEventListener('click', function () {
        var key = this.getAttribute('data-product');
        var p = PRODUCTS[key];
        if (!p) return;
        clearSelection();
        this.style.borderColor = p.color;
        this.style.boxShadow = '0 0 0 1px ' + p.color + ', 0 0 40px -12px ' + p.color;
        panel.classList.remove('hidden');
        renderPanel(p);
        if (panel.scrollIntoView) panel.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      });
    }
  })();
```

- [ ] **Step 4: Manual verification**

Reload the page in your browser. Confirm:
- The Problem Matcher heading appears
- Four cards display, each with a colored eyebrow and pain-point quote
- Clicking each card highlights it in its accent color and reveals a recommendation panel below
- Clicking a second card de-highlights the first and updates the panel
- The "Explore →" link in the panel points to the correct external URL and opens in a new tab

- [ ] **Step 5: Commit**

```bash
cd "/Users/imsats/myproducts/Website Veehive.ai"
git add public/index.html
git commit -m "Replace 'Who This Is For' with interactive Problem Matcher

Four pain-point cards (support overload / slow content / dropped
projects / scattered distribution) that, when clicked, reveal a
recommendation panel pointing to the matching product site. Vanilla
ES5 JS using createElement/textContent (not innerHTML), no
dependencies.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

---

## Task 3: Delete the cross-product narrative sections

We delete four sections that all sell the fictional unified platform. Doing this as one commit because they share a single removal pattern and removing them in isolation creates an awkward intermediate state.

**Sections to delete entirely:**
1. `<!-- SEE IT IN ACTION -->` (Ramadan walkthrough)
2. `<!-- PROBLEM STATEMENT -->` (7+ tools / 3× longer / 40% wasted)
3. `<!-- SOLUTION OVERVIEW -->` (One System, Four Layers)
4. `<!-- THE VEEHIVE SYSTEM — FLOW DIAGRAM -->` (One Brain, Three Agents + the PLAN/RESPOND/CREATE/DISTRIBUTE module cards + the four-step "How It Works" flow — these are all inside this large architecture section)

The `<!-- PARTNERS & ACCELERATORS -->` section (currently between WHO THIS IS FOR and SEE IT IN ACTION) is KEPT.

- [ ] **Step 1: Identify the deletion range**

In `public/index.html`, find these markers in order and delete from the start of `<!-- SEE IT IN ACTION -->` through the end of the section containing the architecture diagram. The next surviving section will be a separate large block. To find the exact end boundary, look for the first `<!-- BUILT IN DUBAI -->` marker that comes **after** the architecture section — everything before that marker (and after the PARTNERS section's closing `</section>`) gets deleted.

You will also delete any `<div class="divider-gradient"></div>` lines that fall between these deleted sections, but keep one `divider-gradient` between the surviving PARTNERS section and the next surviving section (BUILT IN DUBAI).

- [ ] **Step 2: Perform the deletion**

Open `public/index.html` and delete content according to the markers. After deletion, the file should flow from `<!-- PARTNERS & ACCELERATORS -->` directly to `<!-- BUILT IN DUBAI -->` with at most one `<div class="divider-gradient"></div>` between them.

- [ ] **Step 3: Verify the file is still well-formed**

```bash
cd "/Users/imsats/myproducts/Website Veehive.ai"
# Count section tags — must be balanced
grep -c "<section" public/index.html
grep -c "</section>" public/index.html
# These two counts must match exactly.
```

If they don't match, restore from git and try again carefully.

- [ ] **Step 4: Manual verification**

Reload the page in your browser. Confirm:
- After the Problem Matcher, only the Partners row remains before jumping straight to "Built in Dubai"
- The Ramadan campaign, problem-statement-with-stats, "One System Four Layers", and the architecture diagram are all gone
- No broken layout — visual flow continues cleanly

- [ ] **Step 5: Commit**

```bash
cd "/Users/imsats/myproducts/Website Veehive.ai"
git add public/index.html
git commit -m "Delete cross-product narrative sections

Removes 'See It In Action' (Ramadan walkthrough), 'The Problem'
(7+ tools), 'The Solution' (one-system-four-layers), and the
architecture diagram (Veehive System / How It Works / module cards).
All sold the fictional unified-platform story. Product cards replace
the module cards in Task 4.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

---

## Task 4: Insert the four Product Showcase sections

After the Partners row, before BUILT IN DUBAI, we insert four new product showcases.

**Files:**
- Modify: `public/index.html` — insert four new `<section>` blocks between `<!-- PARTNERS & ACCELERATORS -->` (closing `</section>`) and `<!-- BUILT IN DUBAI -->`.

- [ ] **Step 1: Locate the insertion point**

Find the closing `</section>` of `<!-- PARTNERS & ACCELERATORS -->`. The next line should currently be either a `<div class="divider-gradient">` or the `<!-- BUILT IN DUBAI -->` comment. Insert the new content immediately after the partners' `</section>` closing tag, and before any divider that precedes BUILT IN DUBAI.

- [ ] **Step 2: Insert the four product cards**

Add the following block of HTML at the insertion point identified in Step 1:

```html

    <div class="divider-gradient"></div>

    <!-- ═══════════════════════════════════════ -->
    <!-- PRODUCT SHOWCASES -->
    <!-- ═══════════════════════════════════════ -->

    <!-- mpliphi -->
    <section id="mpliphi" class="relative z-10 py-20 lg:py-24" style="scroll-margin-top:96px">
        <div class="max-w-5xl mx-auto px-6 lg:px-8">
            <div class="reveal card-glow card-glow-orchestrator rounded-2xl p-8 md:p-12">
                <p class="text-[12px] font-semibold uppercase tracking-[0.15em] mb-3" style="color:#16A34A">For support &amp; operations teams</p>
                <div class="flex flex-wrap items-baseline gap-3 mb-5">
                    <h2 class="text-3xl md:text-5xl font-bold tracking-tight">mpliphi</h2>
                    <span class="px-3 py-1 rounded-md text-[11px] font-semibold uppercase tracking-[0.08em]" style="background:rgba(22,163,74,0.15); color:#16A34A">AI Agents</span>
                </div>
                <p class="text-[16px] md:text-[17px] text-white/60 leading-relaxed max-w-2xl mb-8">AI agents that handle customer conversations on WhatsApp and email &mdash; autonomously or as copilots alongside your team. Choose fully autonomous or human-in-the-loop. 50+ languages out of the box.</p>
                <div class="flex flex-wrap gap-x-10 gap-y-4 mb-8">
                    <div>
                        <div class="text-2xl md:text-3xl font-bold text-white">50K+</div>
                        <div class="text-[12px] text-white/35 uppercase tracking-wider mt-1">Conversations / month</div>
                    </div>
                    <div>
                        <div class="text-2xl md:text-3xl font-bold text-white">50+</div>
                        <div class="text-[12px] text-white/35 uppercase tracking-wider mt-1">Languages</div>
                    </div>
                    <div>
                        <div class="text-2xl md:text-3xl font-bold text-white">$299</div>
                        <div class="text-[12px] text-white/35 uppercase tracking-wider mt-1">Starting / month</div>
                    </div>
                </div>
                <a href="https://mpliphi.com" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-2 text-[14px] font-semibold" style="color:#16A34A">Explore mpliphi <span aria-hidden="true">&rarr;</span></a>
            </div>
        </div>
    </section>

    <!-- Studio -->
    <section id="studio" class="relative z-10 py-20 lg:py-24" style="scroll-margin-top:96px">
        <div class="max-w-5xl mx-auto px-6 lg:px-8">
            <div class="reveal card-glow card-glow-creator rounded-2xl p-8 md:p-12">
                <p class="text-[12px] font-semibold uppercase tracking-[0.15em] mb-3" style="color:#A78BFA">For content &amp; marketing teams</p>
                <div class="flex flex-wrap items-baseline gap-3 mb-5">
                    <h2 class="text-3xl md:text-5xl font-bold tracking-tight">Veehive Studio</h2>
                    <span class="px-3 py-1 rounded-md text-[11px] font-semibold uppercase tracking-[0.08em]" style="background:rgba(124,58,237,0.18); color:#A78BFA">AI Video</span>
                </div>
                <p class="text-[16px] md:text-[17px] text-white/60 leading-relaxed max-w-2xl mb-8">Turn documents and PDFs into branded videos with AI avatars and voiceover. Built for training, marketing, and customer education. 30+ languages.</p>
                <div class="flex flex-wrap gap-x-10 gap-y-4 mb-8">
                    <div>
                        <div class="text-2xl md:text-3xl font-bold text-white">10&times;</div>
                        <div class="text-[12px] text-white/35 uppercase tracking-wider mt-1">Faster creation</div>
                    </div>
                    <div>
                        <div class="text-2xl md:text-3xl font-bold text-white">30+</div>
                        <div class="text-[12px] text-white/35 uppercase tracking-wider mt-1">Languages</div>
                    </div>
                    <div>
                        <div class="text-2xl md:text-3xl font-bold text-white">$1,300</div>
                        <div class="text-[12px] text-white/35 uppercase tracking-wider mt-1">Starting / month</div>
                    </div>
                </div>
                <a href="https://veehivestudio.com" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-2 text-[14px] font-semibold" style="color:#A78BFA">Explore Veehive Studio <span aria-hidden="true">&rarr;</span></a>
            </div>
        </div>
    </section>

    <!-- SnapaPro -->
    <section id="snapapro" class="relative z-10 py-20 lg:py-24" style="scroll-margin-top:96px">
        <div class="max-w-5xl mx-auto px-6 lg:px-8">
            <div class="reveal card-glow card-glow-planner rounded-2xl p-8 md:p-12">
                <p class="text-[12px] font-semibold uppercase tracking-[0.15em] mb-3" style="color:#F87171">For project managers &amp; team leads</p>
                <div class="flex flex-wrap items-baseline gap-3 mb-5">
                    <h2 class="text-3xl md:text-5xl font-bold tracking-tight">SnapaPro</h2>
                    <span class="px-3 py-1 rounded-md text-[11px] font-semibold uppercase tracking-[0.08em]" style="background:rgba(220,38,38,0.18); color:#F87171">AI Planning</span>
                </div>
                <p class="text-[16px] md:text-[17px] text-white/60 leading-relaxed max-w-2xl mb-8">AI project management powered by three agents &mdash; Taj plans, Noor engages, Sats tracks time. Natural-language task creation, capacity planning, dashboards.</p>
                <div class="flex flex-wrap gap-x-10 gap-y-4 mb-8">
                    <div>
                        <div class="text-2xl md:text-3xl font-bold text-white">3</div>
                        <div class="text-[12px] text-white/35 uppercase tracking-wider mt-1">AI agents</div>
                    </div>
                    <div>
                        <div class="text-2xl md:text-3xl font-bold text-white">NL</div>
                        <div class="text-[12px] text-white/35 uppercase tracking-wider mt-1">Natural-language tasks</div>
                    </div>
                    <div>
                        <div class="text-2xl md:text-3xl font-bold text-white">&infin;</div>
                        <div class="text-[12px] text-white/35 uppercase tracking-wider mt-1">Capacity planning</div>
                    </div>
                </div>
                <a href="https://snapapro.com" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-2 text-[14px] font-semibold" style="color:#F87171">Explore SnapaPro <span aria-hidden="true">&rarr;</span></a>
            </div>
        </div>
    </section>

    <!-- Veehive Link -->
    <section id="veehive-link" class="relative z-10 py-20 lg:py-24" style="scroll-margin-top:96px">
        <div class="max-w-5xl mx-auto px-6 lg:px-8">
            <div class="reveal card-glow card-glow-distributor rounded-2xl p-8 md:p-12">
                <p class="text-[12px] font-semibold uppercase tracking-[0.15em] mb-3" style="color:#60A5FA">For marketing &amp; community managers</p>
                <div class="flex flex-wrap items-baseline gap-3 mb-5">
                    <h2 class="text-3xl md:text-5xl font-bold tracking-tight">Veehive Link</h2>
                    <span class="px-3 py-1 rounded-md text-[11px] font-semibold uppercase tracking-[0.08em]" style="background:rgba(37,99,235,0.18); color:#60A5FA">AI Distribution</span>
                </div>
                <p class="text-[16px] md:text-[17px] text-white/60 leading-relaxed max-w-2xl mb-8">Six modules in one: video hosting, social scheduling, community, events, CRM, campaigns. White-label with custom domains. On-premise available.</p>
                <div class="flex flex-wrap gap-x-10 gap-y-4 mb-8">
                    <div>
                        <div class="text-2xl md:text-3xl font-bold text-white">6</div>
                        <div class="text-[12px] text-white/35 uppercase tracking-wider mt-1">Modules in one</div>
                    </div>
                    <div>
                        <div class="text-2xl md:text-3xl font-bold text-white">24/7</div>
                        <div class="text-[12px] text-white/35 uppercase tracking-wider mt-1">AI agent</div>
                    </div>
                    <div>
                        <div class="text-2xl md:text-3xl font-bold text-white">WL</div>
                        <div class="text-[12px] text-white/35 uppercase tracking-wider mt-1">White-label + on-prem</div>
                    </div>
                </div>
                <a href="https://veehivelink.com" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-2 text-[14px] font-semibold" style="color:#60A5FA">Explore Veehive Link <span aria-hidden="true">&rarr;</span></a>
            </div>
        </div>
    </section>
```

- [ ] **Step 3: Manual verification**

Reload the page. Confirm:
- Four product cards display in the order mpliphi → Studio → SnapaPro → Veehive Link
- Each card has its accent-color eyebrow, big product name, category badge, three stats, and "Explore →" link
- Each "Explore →" link points to the correct domain and opens in a new tab
- Hero pills now scroll smoothly to the matching card (since each card has the right `id`)
- The scroll lands cleanly below the nav (no overlap), thanks to `scroll-margin-top:96px`

- [ ] **Step 4: Confirm there are still ≥3 `veehivelink.com` links on the page**

```bash
cd "/Users/imsats/myproducts/Website Veehive.ai"
grep -c "https://veehivelink.com" public/index.html
# Expected: >= 3 (covers product card, Problem Matcher script, plus JSON-LD)
```

Required by the existing Playwright test (`tests/live-veehive-link.spec.ts`).

- [ ] **Step 5: Commit**

```bash
cd "/Users/imsats/myproducts/Website Veehive.ai"
git add public/index.html
git commit -m "Add four product showcase sections

mpliphi (green) -> Veehive Studio (purple) -> SnapaPro (red) ->
Veehive Link (blue). Each card uses the existing card-glow-* class
matching its product accent. Cards have anchor ids matching the hero
pills. scroll-margin-top:96px keeps the scroll target below the nav.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

---

## Task 5: Update About Promo copy line (one-line edit)

The About Promo section currently sits between BUILT IN DUBAI and FAQ — its position already matches the spec. We only update one outdated copy line.

**Files:**
- Modify: `public/index.html` — the `<!-- ABOUT PROMO -->` section

- [ ] **Step 1: Locate and edit one copy line**

Find this exact line in the About Promo section:

```html
<p class="text-[14px] text-white/40 leading-relaxed">Explore our credentials, capabilities, and the team building the agentic operating system for marketing.</p>
```

Replace it with:

```html
<p class="text-[14px] text-white/40 leading-relaxed">Explore our credentials, capabilities, and the team behind Veehive&rsquo;s four AI products.</p>
```

- [ ] **Step 2: Manual verification**

Reload. Confirm the About Promo card now reads "...team behind Veehive's four AI products." with the rest of the section unchanged.

- [ ] **Step 3: Commit**

```bash
cd "/Users/imsats/myproducts/Website Veehive.ai"
git add public/index.html
git commit -m "Update About Promo copy to match four-product framing

Removes 'agentic operating system for marketing' phrasing from the
About Promo blurb. Position is unchanged.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

---

## Task 6: Rewrite the Lead Capture / CTA section

The current CTA section heading says "Ready to Execute?" and frames itself around "turns one command into a complete marketing campaign." We rewrite the heading, sub, and three CTAs.

**Files:**
- Modify: `public/index.html` — the section delimited by `<!-- CTA SECTION -->` and its `id="contact"` `<section>` block

- [ ] **Step 1: Locate the section**

Find `<!-- CTA SECTION -->` and the `<section id="contact"` that follows.

- [ ] **Step 2: Replace the section**

Replace the entire `<!-- CTA SECTION -->` block (from the comment line through its closing `</section>`) with:

```html
    <!-- ═══════════════════════════════════════ -->
    <!-- LEAD CAPTURE / CTA -->
    <!-- ═══════════════════════════════════════ -->
    <section id="contact" class="relative z-10 py-24 lg:py-32">
        <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[400px] bg-gradient-to-r from-[#3B5BFF]/[0.06] via-[#3B5BFF]/[0.03] to-transparent rounded-full blur-[120px] pointer-events-none"></div>
        <div class="max-w-3xl mx-auto px-6 lg:px-8 text-center relative">
            <p class="text-[13px] font-semibold uppercase tracking-[0.2em] text-white/30 mb-5">Get in touch</p>
            <h2 class="text-3xl md:text-5xl font-bold tracking-tight mb-4">
                Not sure which <span class="font-display italic text-gradient">product fits?</span>
            </h2>
            <p class="text-base text-white/40 mb-10 max-w-lg mx-auto leading-relaxed">
                Tell us what you&rsquo;re trying to solve. We&rsquo;ll point you to the right tool.
            </p>
            <div class="flex flex-col sm:flex-row justify-center items-center gap-3 sm:gap-4">
                <a href="https://outlook.office.com/bookwithme/user/4b235448860a484991237c062357501e@veehive.ai?anonymous&ismsaljsauthenabled&ep=plink" target="_blank" rel="noopener noreferrer"
                   class="group inline-flex items-center justify-center gap-2.5 px-8 py-3.5 bg-[#3B5BFF] text-[14px] font-semibold rounded-full hover:bg-[#6B82FF] transition-all shadow-lg shadow-[#3B5BFF]/20 hover:-translate-y-0.5" style="color: var(--cta-text);">
                    Book a Demo
                    <svg class="w-3.5 h-3.5 group-hover:translate-x-0.5 transition-transform" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5"><path stroke-linecap="round" stroke-linejoin="round" d="M13 7l5 5m0 0l-5 5m5-5H6"/></svg>
                </a>
                <a href="https://wa.me/971564308275" target="_blank" rel="noopener noreferrer"
                   class="group inline-flex items-center justify-center gap-2.5 px-8 py-3.5 text-[14px] font-medium border border-white/[0.12] rounded-full hover:bg-white/[0.05] hover:border-white/[0.2] transition-all text-white/80 hover:-translate-y-0.5">
                    <svg class="w-[18px] h-[18px] shrink-0" fill="currentColor" viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
                    WhatsApp us
                </a>
                <a href="mailto:contact@veehive.ai" class="group inline-flex items-center justify-center gap-2.5 px-8 py-3.5 text-[14px] font-medium border border-white/[0.12] rounded-full hover:bg-white/[0.05] hover:border-white/[0.2] transition-all text-white/80 hover:-translate-y-0.5">
                    <svg class="w-[18px] h-[18px] shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M21.75 6.75v10.5a2.25 2.25 0 01-2.25 2.25h-15a2.25 2.25 0 01-2.25-2.25V6.75m19.5 0A2.25 2.25 0 0019.5 4.5h-15a2.25 2.25 0 00-2.25 2.25m19.5 0v.243a2.25 2.25 0 01-1.07 1.916l-7.5 4.615a2.25 2.25 0 01-2.36 0L3.32 8.91a2.25 2.25 0 01-1.07-1.916V6.75"/></svg>
                    Email us
                </a>
            </div>
            <p class="mt-8 text-[13px] text-white/30">contact@veehive.ai &nbsp;&middot;&nbsp; +971&nbsp;56&nbsp;430&nbsp;8275</p>
        </div>
    </section>
```

- [ ] **Step 3: Manual verification**

Reload. Confirm:
- Heading reads "Not sure which **product fits?**" (with "product fits?" in gradient italic)
- Sub reads "Tell us what you're trying to solve..."
- Three CTAs visible: Book a Demo (primary blue), WhatsApp us, Email us
- All three CTAs open the correct destinations
- Section id is still `contact` (the nav anchor relies on this)

- [ ] **Step 4: Commit**

```bash
cd "/Users/imsats/myproducts/Website Veehive.ai"
git add public/index.html
git commit -m "Rewrite lead capture: three CTAs, no form

Replaces 'Ready to Execute?' heading and unified-campaign copy with
'Not sure which product fits?' framing. Three CTAs: Book a Demo
(Outlook), WhatsApp, Email — matching what already works site-wide.
Section keeps id='contact' so the nav anchor still resolves.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

---

## Task 7: Rewrite the FAQ entries (HTML + JSON-LD together)

We rewrite both the visible FAQ accordion and the FAQPage JSON-LD in one commit so they don't drift out of sync.

**Files:**
- Modify: `public/index.html` — the FAQ accordion (in `<!-- FAQ -->`) and the FAQ JSON-LD block (in `<head>`, `<!-- Structured Data - FAQ for AEO -->`)

- [ ] **Step 1: Replace the FAQ accordion**

Find `<!-- FAQ -->` in `public/index.html`. The accordion is the `<div class="reveal space-y-3">` immediately inside that section. Replace **only the items inside `<div class="reveal space-y-3">...</div>`** (not the outer section/heading) with these six entries:

```html
                <div class="trust-card rounded-xl overflow-hidden">
                    <button class="w-full px-6 py-5 flex justify-between items-center text-left" onclick="this.parentElement.classList.toggle('faq-open')">
                        <span class="text-[15px] font-semibold text-white/80 pr-4">What is Veehive.ai?</span>
                        <svg class="w-4 h-4 text-white/30 shrink-0 transition-transform duration-300" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7"/></svg>
                    </button>
                    <div class="max-h-0 overflow-hidden transition-all duration-300">
                        <div class="px-6 pb-5 text-[14px] text-white/45 leading-relaxed">Veehive is a Dubai-based applied-AI company. We build four independent AI products for different teams &mdash; not a single unified platform.</div>
                    </div>
                </div>
                <div class="trust-card rounded-xl overflow-hidden">
                    <button class="w-full px-6 py-5 flex justify-between items-center text-left" onclick="this.parentElement.classList.toggle('faq-open')">
                        <span class="text-[15px] font-semibold text-white/80 pr-4">What products does Veehive build?</span>
                        <svg class="w-4 h-4 text-white/30 shrink-0 transition-transform duration-300" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7"/></svg>
                    </button>
                    <div class="max-h-0 overflow-hidden transition-all duration-300">
                        <div class="px-6 pb-5 text-[14px] text-white/45 leading-relaxed"><strong class="text-white/60"><a href="https://mpliphi.com" target="_blank" rel="noopener noreferrer" class="hover:text-white">mpliphi</a></strong> (customer-conversation agents), <strong class="text-white/60"><a href="https://veehivestudio.com" target="_blank" rel="noopener noreferrer" class="hover:text-white">Veehive Studio</a></strong> (document-to-video AI), <strong class="text-white/60"><a href="https://snapapro.com" target="_blank" rel="noopener noreferrer" class="hover:text-white">SnapaPro</a></strong> (AI project management), <strong class="text-white/60"><a href="https://veehivelink.com" target="_blank" rel="noopener noreferrer" class="hover:text-white">Veehive Link</a></strong> (content + community + CRM).</div>
                    </div>
                </div>
                <div class="trust-card rounded-xl overflow-hidden">
                    <button class="w-full px-6 py-5 flex justify-between items-center text-left" onclick="this.parentElement.classList.toggle('faq-open')">
                        <span class="text-[15px] font-semibold text-white/80 pr-4">Are the products connected?</span>
                        <svg class="w-4 h-4 text-white/30 shrink-0 transition-transform duration-300" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7"/></svg>
                    </button>
                    <div class="max-h-0 overflow-hidden transition-all duration-300">
                        <div class="px-6 pb-5 text-[14px] text-white/45 leading-relaxed">No. Each product solves one problem for one audience and stands on its own. Buy what you need.</div>
                    </div>
                </div>
                <div class="trust-card rounded-xl overflow-hidden">
                    <button class="w-full px-6 py-5 flex justify-between items-center text-left" onclick="this.parentElement.classList.toggle('faq-open')">
                        <span class="text-[15px] font-semibold text-white/80 pr-4">Is Veehive secure?</span>
                        <svg class="w-4 h-4 text-white/30 shrink-0 transition-transform duration-300" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7"/></svg>
                    </button>
                    <div class="max-h-0 overflow-hidden transition-all duration-300">
                        <div class="px-6 pb-5 text-[14px] text-white/45 leading-relaxed">Yes &mdash; Dubai AI Seal Tier E certified, SOC 2 Type II controls implemented, ISO 27001 aligned, GDPR-ready. Your data never trains our models.</div>
                    </div>
                </div>
                <div class="trust-card rounded-xl overflow-hidden">
                    <button class="w-full px-6 py-5 flex justify-between items-center text-left" onclick="this.parentElement.classList.toggle('faq-open')">
                        <span class="text-[15px] font-semibold text-white/80 pr-4">Where is Veehive based?</span>
                        <svg class="w-4 h-4 text-white/30 shrink-0 transition-transform duration-300" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7"/></svg>
                    </button>
                    <div class="max-h-0 overflow-hidden transition-all duration-300">
                        <div class="px-6 pb-5 text-[14px] text-white/45 leading-relaxed">Dubai, UAE &mdash; at In5 Tech in Dubai Internet City. We operate as Veehive Tech FZ LLC. Contact us at contact@veehive.ai or WhatsApp +971564308275.</div>
                    </div>
                </div>
                <div class="trust-card rounded-xl overflow-hidden">
                    <button class="w-full px-6 py-5 flex justify-between items-center text-left" onclick="this.parentElement.classList.toggle('faq-open')">
                        <span class="text-[15px] font-semibold text-white/80 pr-4">What if I need custom AI development?</span>
                        <svg class="w-4 h-4 text-white/30 shrink-0 transition-transform duration-300" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7"/></svg>
                    </button>
                    <div class="max-h-0 overflow-hidden transition-all duration-300">
                        <div class="px-6 pb-5 text-[14px] text-white/45 leading-relaxed">That&rsquo;s <a href="https://veehivelabs.com" target="_blank" rel="noopener noreferrer" class="text-[#3B5BFF] hover:text-[#6B82FF] transition-colors">VeehiveLabs</a> &mdash; our applied-AI consulting arm for bespoke builds.</div>
                    </div>
                </div>
```

- [ ] **Step 2: Replace the FAQPage JSON-LD**

Find `<!-- Structured Data - FAQ for AEO -->` near the top of the file (~line 264). Replace the entire `<script type="application/ld+json">...</script>` block immediately after that comment with:

```html
    <!-- Structured Data - FAQ for AEO -->
    <script type="application/ld+json">
    {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "dateModified": "2026-05-13",
        "mainEntity": [
            {
                "@type": "Question",
                "name": "What is Veehive.ai?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "Veehive is a Dubai-based applied-AI company. We build four independent AI products for different teams — not a single unified platform."
                }
            },
            {
                "@type": "Question",
                "name": "What products does Veehive build?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "mpliphi (customer-conversation agents at mpliphi.com), Veehive Studio (document-to-video AI at veehivestudio.com), SnapaPro (AI project management at snapapro.com), and Veehive Link (content + community + CRM at veehivelink.com)."
                }
            },
            {
                "@type": "Question",
                "name": "Are the Veehive products connected?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "No. Each product solves one problem for one audience and stands on its own. Buy what you need."
                }
            },
            {
                "@type": "Question",
                "name": "Is Veehive secure?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "Yes. Veehive is Dubai AI Seal Tier E certified, implements SOC 2 Type II controls, follows ISO 27001 aligned practices, and is GDPR-ready. Customer data never trains our models."
                }
            },
            {
                "@type": "Question",
                "name": "Where is Veehive based?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "Dubai, UAE — at In5 Tech in Dubai Internet City. We operate as Veehive Tech FZ LLC. Contact: contact@veehive.ai or WhatsApp +971564308275."
                }
            },
            {
                "@type": "Question",
                "name": "What if I need custom AI development?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "Veehive Labs (veehivelabs.com) is our applied-AI consulting arm for bespoke builds."
                }
            }
        ]
    }
    </script>
```

- [ ] **Step 3: Validate JSON-LD parses**

```bash
cd "/Users/imsats/myproducts/Website Veehive.ai"
node -e "const fs=require('fs');const html=fs.readFileSync('public/index.html','utf8');const m=html.match(/<script type=\"application\\/ld\\+json\">([\\s\\S]*?)<\\/script>/g);if(!m){console.error('NO JSON-LD');process.exit(1);}m.forEach((s,i)=>{const body=s.replace(/<\\/?script[^>]*>/g,'');try{JSON.parse(body);console.log('block',i+1,'OK');}catch(e){console.error('block',i+1,'INVALID:',e.message);process.exit(1);}});"
```

Expected: every block prints `OK`. If any block prints `INVALID`, fix the JSON syntax before continuing.

- [ ] **Step 4: Manual verification**

Reload. Confirm:
- The FAQ section displays the six new questions in the order above
- Each accordion expands and collapses on click
- The "What products does Veehive build?" answer contains four working external links
- The "What if I need custom AI development?" answer links to veehivelabs.com

- [ ] **Step 5: Commit**

```bash
cd "/Users/imsats/myproducts/Website Veehive.ai"
git add public/index.html
git commit -m "Rewrite FAQ: six entries for the four-product reality

Replaces the unified-platform FAQ with honest Q/As covering: what
Veehive is, what we build, whether products are connected (no),
security, location, and Labs for custom work. Updates the FAQPage
JSON-LD to match.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

---

## Task 8: Refresh `<head>` SEO — title, meta, OG, Twitter, Organization JSON-LD

The FAQPage JSON-LD was handled in Task 7. This task covers the remaining head tags.

**Files:**
- Modify: `public/index.html` lines ~18–41 (title, meta tags, OG, Twitter) and the Organization JSON-LD block (line ~50)

- [ ] **Step 1: Update title and meta**

Locate this block (around lines 18–24):

```html
    <title>Veehive.ai — AI Marketing Platform | Plan, Create, Distribute</title>
    <meta name="description" content="AI marketing platform that plans, creates, distributes, and tracks campaigns from a single prompt. Four modules. One platform. Dubai AI Seal certified.">
    <meta name="keywords" content="agentic AI, marketing execution, AI operating system, SnapaPro, mpliphi, Studio, Veehive Link, Veehive, Dubai AI, enterprise AI, agentic architecture, AI automation">
```

Replace with:

```html
    <title>Veehive.ai — Applied AI from Dubai. Four AI products, one company.</title>
    <meta name="description" content="Veehive is a Dubai-based applied-AI company building four independent products: mpliphi (customer conversations), Veehive Studio (AI video), SnapaPro (project management), and Veehive Link (content + community). Dubai AI Seal Tier E certified.">
    <meta name="keywords" content="applied AI, AI agents, AI video, AI project management, mpliphi, Veehive Studio, SnapaPro, Veehive Link, Veehive Tech, Dubai AI, enterprise AI">
```

- [ ] **Step 2: Update Open Graph tags**

Locate (around lines 29–30):

```html
    <meta property="og:title" content="Veehive.ai — AI Marketing Platform | Plan, Create, Distribute">
    <meta property="og:description" content="Turn one command into a complete campaign. Veehive.ai plans, creates, distributes, and tracks marketing execution through a unified AI-driven system.">
```

Replace with:

```html
    <meta property="og:title" content="Veehive.ai — Applied AI from Dubai. Four AI products, one company.">
    <meta property="og:description" content="Veehive is a Dubai-based applied-AI company building four independent products: mpliphi (customer conversations), Veehive Studio (AI video), SnapaPro (project management), and Veehive Link (content + community). Dubai AI Seal Tier E certified.">
```

- [ ] **Step 3: Update Twitter tags**

Locate (around lines 38–39):

```html
    <meta name="twitter:title" content="Veehive.ai — AI Marketing Platform | Plan, Create, Distribute">
    <meta name="twitter:description" content="Turn one command into a complete campaign. Four AI modules. One unified system.">
```

Replace with:

```html
    <meta name="twitter:title" content="Veehive.ai — Applied AI from Dubai. Four AI products, one company.">
    <meta name="twitter:description" content="Four independent AI products. Four different teams. mpliphi, Veehive Studio, SnapaPro, Veehive Link. Dubai AI Seal Tier E certified.">
```

- [ ] **Step 4: Update Organization JSON-LD `description`**

Locate the Organization JSON-LD block (starts at `<!-- Structured Data - Organization -->`, ~line 49). Find this line inside it:

```json
        "description": "AI marketing platform with four modules — Plan (SnapaPro), Create (Studio), Distribute (Veehive Link), Respond (mpliphi). Dubai AI Seal Tier E certified. Based in Dubai, UAE.",
```

Replace with:

```json
        "description": "Veehive is a Dubai-based applied-AI company building four independent products: mpliphi (customer conversations), Veehive Studio (AI video), SnapaPro (project management), and Veehive Link (content + community). Dubai AI Seal Tier E certified.",
```

- [ ] **Step 5: Validate JSON-LD parses**

```bash
cd "/Users/imsats/myproducts/Website Veehive.ai"
node -e "const fs=require('fs');const html=fs.readFileSync('public/index.html','utf8');const m=html.match(/<script type=\"application\\/ld\\+json\">([\\s\\S]*?)<\\/script>/g);if(!m){console.error('NO JSON-LD');process.exit(1);}m.forEach((s,i)=>{const body=s.replace(/<\\/?script[^>]*>/g,'');try{JSON.parse(body);console.log('block',i+1,'OK');}catch(e){console.error('block',i+1,'INVALID:',e.message);process.exit(1);}});"
```

Expected: every block prints `OK`.

- [ ] **Step 6: Confirm Playwright test invariants still hold**

```bash
cd "/Users/imsats/myproducts/Website Veehive.ai"
# The existing test requires these to be present:
grep -c '"Veehive Link"' public/index.html
# Expected: >= 1 (lives in the Organization knowsAbout array and elsewhere)
grep -c "veehivelink.com" public/index.html
# Expected: >= 5 (hero pill href, product card href, Problem Matcher script PRODUCTS map, FAQ link, JSON-LD references)
grep -c 'href="https://veehivelink.com"' public/index.html
# Expected: >= 3 (product card "Explore", FAQ "What products" link, footer module-list link)
```

If `href="https://veehivelink.com"` count is less than 3, the test `homepage: Veehive Link nav, footer, and module card link to veehivelink.com in new tab` will fail post-deploy. Check the footer module-list and Add another anchor to veehivelink.com in the FAQ or elsewhere before committing.

- [ ] **Step 7: Manual verification**

```bash
open "/Users/imsats/myproducts/Website Veehive.ai/public/index.html"
```

In the browser, view source (or DevTools → Elements → `<head>`). Confirm:
- `<title>` reads "Veehive.ai — Applied AI from Dubai. Four AI products, one company."
- `<meta name="description">` matches the new copy
- OG and Twitter titles/descriptions match the new copy
- Organization JSON-LD `description` field matches

- [ ] **Step 8: Commit**

```bash
cd "/Users/imsats/myproducts/Website Veehive.ai"
git add public/index.html
git commit -m "Refresh head SEO: title, meta, OG, Twitter, Organization JSON-LD

Replaces 'AI Marketing Platform | Plan, Create, Distribute' positioning
with 'Applied AI from Dubai. Four AI products, one company.' across
title, meta description, keywords, Open Graph, Twitter cards, and the
Organization JSON-LD description field.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

---

## Task 9: Cross-browser smoke test + final verification

Now we run end-to-end checks across the full page.

- [ ] **Step 1: Section-count sanity check**

```bash
cd "/Users/imsats/myproducts/Website Veehive.ai"
grep -c "<section" public/index.html
grep -c "</section>" public/index.html
# Both must match exactly
```

If they don't, find the unbalanced section and fix it before continuing.

- [ ] **Step 2: External link audit**

```bash
cd "/Users/imsats/myproducts/Website Veehive.ai"
# All four product external sites must appear at least once
for url in mpliphi.com veehivestudio.com snapapro.com veehivelink.com; do
  count=$(grep -c "https://$url" public/index.html)
  echo "$url: $count occurrences"
  [ "$count" -lt 1 ] && echo "  WARN: missing"
done
# Veehive Link must appear at least 3 times (Playwright test req)
echo "---"
echo "veehivelink.com total: $(grep -c veehivelink.com public/index.html)"
```

Expected: each product URL appears at least once. Veehive Link appears ≥3 times.

- [ ] **Step 3: JSON-LD final validation**

```bash
cd "/Users/imsats/myproducts/Website Veehive.ai"
node -e "const fs=require('fs');const html=fs.readFileSync('public/index.html','utf8');const m=html.match(/<script type=\"application\\/ld\\+json\">([\\s\\S]*?)<\\/script>/g);if(!m){console.error('NO JSON-LD');process.exit(1);}m.forEach((s,i)=>{const body=s.replace(/<\\/?script[^>]*>/g,'');try{JSON.parse(body);console.log('block',i+1,'OK');}catch(e){console.error('block',i+1,'INVALID:',e.message);process.exit(1);}});"
```

Expected: every block prints `OK`.

- [ ] **Step 4: Visual smoke test in browser**

```bash
open "/Users/imsats/myproducts/Website Veehive.ai/public/index.html"
```

Walk the page top to bottom and confirm each of these visually:

1. **Hero:** badge → "We build AI that works." headline → four pills with colored dots → Book a Demo + Get in touch buttons
2. **Problem Matcher:** four pain-point cards, clicking each one highlights it and reveals the recommendation panel
3. **Partners row:** unchanged
4. **Product showcases:** mpliphi (green) → Studio (purple) → SnapaPro (red) → Veehive Link (blue), each with stats and Explore link
5. **Built in Dubai:** unchanged section with the trust card
6. **About Promo:** updated copy line about "four AI products"
7. **Lead capture:** "Not sure which product fits?" + three CTAs
8. **FAQ:** six new entries, each expands on click

- [ ] **Step 5: Theme toggle smoke test**

In the browser, click the theme toggle in the nav. Switch to light mode and walk the page again. Confirm:
- Pill colors are still legible
- Product accent colors (green/purple/red/blue) still read against the white background
- Card glows behave reasonably (existing CSS has light-mode variants for all `card-glow-*` classes at lines 747–752)

- [ ] **Step 6: Mobile responsive smoke test**

Open Chrome DevTools → toggle device toolbar → iPhone 14 (390×844). Walk the page again. Confirm:
- Hero pills wrap to multiple lines cleanly
- Problem Matcher grid collapses to one column
- Product showcase stats wrap
- Lead capture CTAs stack vertically
- FAQ items remain clickable

- [ ] **Step 7: Anchor-link smoke test**

In the browser, click each hero pill (mpliphi, Studio, SnapaPro, Veehive Link) in turn. Confirm each one smooth-scrolls to its product card, and the card sits below the nav (not hidden behind it).

- [ ] **Step 8: GA4 click-event smoke test**

Open Chrome DevTools → Network tab → filter on `collect`. Click each of the three lead-capture CTAs (Book a Demo, WhatsApp, Email). Confirm each click produces a `collect` request to `google-analytics.com` with an event name matching:
- Book a Demo → `click_book_demo`
- WhatsApp → `click_whatsapp`
- Email → `click_email`

These are mapped by the inline handler at line 8 of the file.

- [ ] **Step 9: Final commit (if any fixes needed)**

If steps 1–8 surface any fixes, make them and commit:

```bash
cd "/Users/imsats/myproducts/Website Veehive.ai"
git add public/index.html
git commit -m "Polish landing page rewrite

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

If nothing needs fixing, skip the commit.

- [ ] **Step 10: Summary check**

```bash
cd "/Users/imsats/myproducts/Website Veehive.ai"
git log --oneline -10
```

You should see ~8 new commits from this plan, plus the design-spec commit before it. Confirm the chain reads sensibly.

---

## Notes on the Playwright test

The existing test at `tests/live-veehive-link.spec.ts` runs against **production** (`https://veehive.ai`). It will not exercise local changes. Running it now will reflect the **deployed** site, not your edits.

After this branch is merged and deployed (via Firebase Hosting), run:

```bash
cd "/Users/imsats/myproducts/Website Veehive.ai"
npx playwright test tests/live-veehive-link.spec.ts
```

Expected: all tests pass. The two assertions most likely to break:

- **`homepage: Veehive Link nav, footer, and module card link to veehivelink.com in new tab`** — requires `>= 3` static `<a>` tags pointing to `https://veehivelink.com` with `target="_blank"`. Sources after this rewrite:
  - Footer's existing module-list link (unchanged by this plan)
  - Product card "Explore Veehive Link" (added in Task 4)
  - FAQ "What products does Veehive build?" inline link (added in Task 7)
  Verify with `grep -c 'href="https://veehivelink.com"' public/index.html` — must be ≥ 3.

- **`homepage schema.org JSON-LD names "Veehive Link" with veehivelink.com URL`** — both strings must appear inside `<script type="application/ld+json">`. Confirm with `grep` (Task 8 Step 6).

---

## Self-Review Notes (from plan author)

- **Spec coverage:** Hero, Problem Matcher, four product showcases (Tasks 1, 2, 4), Trust kept (BUILT IN DUBAI unchanged), About Promo repositioned/updated (Task 5), Lead Capture rewritten (Task 6), FAQ rewritten (Task 7), head SEO updated (Tasks 7+8). Deletions in Task 3. Every section in the spec has a task.
- **Placeholders:** none. All HTML, JSON, and shell snippets are complete.
- **Type consistency:** the Problem Matcher script uses `data-product` keys (`mpliphi`, `studio`, `snapapro`, `veehive-link`) that match the product card `id` attributes from Task 4. The product names match: mpliphi, Veehive Studio, SnapaPro, Veehive Link.
- **Security review:** the Problem Matcher script uses `createElement`/`textContent` instead of `innerHTML`. All values originate from the script's own `PRODUCTS` constant — no DOM input flows in — but using safe DOM methods keeps strict-CSP environments happy.
- **Known small deviation from spec:** Spec uses "Studio" as the product name. The actual brand name on veehivestudio.com is "Veehive Studio" — used throughout this plan for clarity. If you want bare "Studio", do a find/replace.
