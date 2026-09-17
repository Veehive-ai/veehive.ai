# Prompt: Rewrite Veehive.ai Landing Page

## Context

You are rewriting the landing page at `public/index.html` for Veehive.ai. This is a static HTML file using Tailwind CSS with a custom dark/light theme system. Keep the existing `<head>` (SEO, structured data, meta tags), `<nav>`, theme toggle, CSS variables, design system (card-glow, shimmer-badge, trust-card, reveal animations, ambient orbs), and `<footer>` exactly as they are. Only rewrite the `<body>` content between the nav and the footer.

## Critical Reframing

The current page sells Veehive.ai as a "unified AI marketing platform" that turns "one command into a complete campaign." **This product does not exist.** Delete all content that claims these four products work together as one system, including:

- The "One Brain, Three Agents" architecture diagram
- The "One prompt. Full campaign." narrative
- The Ramadan campaign walkthrough that chains all four products
- The "One System. Four Layers." solution section  
- The "agentic operating system for marketing execution" positioning
- Any stats that aggregate across products (e.g., "4 AI Modules")

## What Veehive.ai Actually Is

Veehive.ai is the **company** — a Dubai-based Applied AI company that builds four **independent** products for **different audiences**. The landing page should be a **product portfolio page** that:

1. Routes visitors to the right product fast
2. Builds trust in Veehive as a credible AI company
3. Captures leads (demo requests, contact info)

## The Four Real Products

### mpliphi (mpliphi.com)
- **Audience:** Support teams, operations teams, CXOs
- **What it does:** AI agents that handle customer conversations autonomously or as copilots alongside human teams
- **Channels:** WhatsApp and Email native
- **Key stats:** 50K+ conversations/month, 50+ languages, starts at $299/mo
- **Two agent types:** Fully Autonomous (no human needed) and Co-Pilot (AI assists humans)
- **Color accent:** Green (#2c573e)

### Veehive Studio (veehivestudio.com)
- **Audience:** Content teams, marketing teams, agencies, training departments
- **What it does:** Turns documents/PDFs into branded videos with AI avatars and voiceover
- **Key stats:** 10x faster creation, 30+ languages, 95% cost reduction, starts at $1,300/mo
- **Capabilities:** Document processing, AI video creation, interactive mindmaps, omnichannel distribution
- **Color accent:** Purple (#7C3AED)

### SnapaPro (snapapro.com)
- **Audience:** Project managers, team leads
- **What it does:** AI project management powered by 3 AI agents (Taj the planner, Noor the engager, Sats the time tracker)
- **Key stats:** 3 AI agents, natural language task creation, team capacity planning, timesheets
- **Capabilities:** Dashboard, project health, resource planning, auto task extraction
- **Color accent:** Red (#DC2626)

### HiveLink / Veehive Link (veehivelink.com)
- **Audience:** Marketing managers, community managers
- **What it does:** One platform replacing video hosting, social scheduler, community tool, and CRM
- **Key stats:** 6 modules in one, 24/7 AI agent, white-label with custom domains, on-premise option
- **Capabilities:** Video channels, content approval workflow, social distribution, events/calendar, community groups, CRM + campaigns + forms
- **Color accent:** Blue (#2563EB)

## New Landing Page Structure

### Section 1: Hero
**Headline:** Position Veehive as a company that builds AI tools, not as a single product.  
**Suggested approach:** "We build AI that works" or "Four AI tools. Four problems solved." — keep it short and company-level.  
**Below headline:** Four product pills/buttons (mpliphi, Studio, SnapaPro, HiveLink) that anchor-scroll to each product's section. These should look clickable and be the primary navigation path.  
**CTA:** "Book a Demo" (keep existing Outlook booking link).  
**Remove:** All "one prompt, full campaign" messaging. Remove "50K conversations" and "4 AI modules" stats row — these belong to individual products, not the company.  
**Keep:** The "Dubai AI Seal Certified" shimmer badge.

### Section 2: Problem Matcher (Interactive)
**Purpose:** Help visitors self-identify which product they need.  
**Headline:** "What problem are you solving?"  
**Four clickable cards, each describing a pain point:**
1. "Customer replies are drowning us" → recommends mpliphi
2. "Content takes too long to produce" → recommends Studio
3. "Projects slip through the cracks" → recommends SnapaPro
4. "Distribution is a mess of tools" → recommends HiveLink

When clicked, highlight the selected card and show a recommendation below with a direct link to that product's site. Use existing card-glow and trust-card classes for styling.

### Section 3: Product Showcases
**Four full-width cards, one per product.** Each card should have:
- Audience tag at top (e.g., "For support + operations teams") in the product's accent color
- Product name (large, bold)
- Category badge (e.g., "AI Agents", "AI Video", "AI Planning", "AI Distribution")
- One-paragraph pitch (2-3 sentences max)
- Three key stats in a row
- "Explore [Product] →" link to external site

Use the existing `card-glow` + product-specific glow classes (`card-glow-orchestrator`, `card-glow-creator`, `card-glow-planner`, `card-glow-distributor`).  

**Order the products by broadest appeal:** mpliphi → Studio → SnapaPro → HiveLink.

**Do NOT:** Describe how the products connect to each other. They are independent.

### Section 4: Trust & Credibility
**Keep the existing content:** Partners & Accelerators row, Dubai AI Seal, SOC 2, ISO 27001, GDPR badges.  
**Add:** "Built in Dubai. Trusted Globally." + Veehive Tech FZ LLC, In5 Tech, Dubai Internet City.  
**Keep:** The "As Seen In" logos (The Hindu, Dubai One, Red Bull, World Economic Forum) if they exist.

### Section 5: Lead Capture / CTA
**Headline:** "Not sure which product fits?"  
**Sub:** "Tell us what you're trying to solve. We'll point you to the right tool."  
**Form:** Email input + "Get in touch" button. Keep it simple.  
**Alternative:** "Or WhatsApp us directly" + existing WhatsApp link.  
**Also keep:** "Book a Demo" as a secondary CTA linking to existing Outlook booking.

### Section 6: FAQ (Rewrite)
Rewrite the FAQ to reflect reality:
- "What is Veehive.ai?" → It's the company behind four AI products (not a platform)
- "What products does Veehive build?" → Brief on each product with links
- "Are the products connected?" → No, they are independent tools for different teams
- "Is Veehive secure?" → Yes, Dubai AI Seal, SOC 2, ISO 27001 (keep existing security content)
- "Where is Veehive based?" → Dubai, UAE (keep existing)
- "What if I need custom AI development?" → VeehiveLabs.com (keep existing)

## Sections to DELETE Entirely

Remove these sections from the current page — they all sell the fictional unified platform:

- "Who This Is For" (the marketing teams checklist) — too narrow, excludes PM and support audiences
- "See It In Action" (Ramadan campaign example) — implies products chain together
- "The Problem" (7+ tools, 3x longer, 40% wasted) — framing only makes sense for the unified product
- "The Solution" (One System, Four Layers)
- "The Veehive System" architecture diagram (One Brain, Three Agents)
- "PLAN / RESPOND / CREATE / DISTRIBUTE" module cards — replace with new product showcases
- "How It Works" (Intent to Execution four-step flow) — implies a single workflow
- The "Security & Compliance" deep dive — keep badges in the trust section but remove the full page section with its 8 feature bullets (it's overkill for a portfolio page; each product site handles this)

## Technical Notes

- Keep the existing CSS variables, theme system, and all class definitions in `<style>`
- Keep all animation classes (fade-up, reveal, shimmer-badge, etc.)
- Keep the `card-glow` system and module-specific glow colors
- Keep the Google Analytics tracking script in `<head>`
- Keep the structured data / JSON-LD in `<head>` (update the FAQPage schema to match new FAQ content)
- Keep the `<nav>` and `<footer>` exactly as-is
- Keep the ambient background orbs
- Maintain responsive design (mobile menu, grid breakpoints)
- Use `reveal` class on new sections for scroll-triggered fade-in
- All external product links should have `target="_blank" rel="noopener noreferrer"`
- The page should feel shorter and faster to scan than the current version

## Tone & Voice

- Confident but not salesy
- Company-level, not product-level
- Let each product speak for itself through its card
- No "AI-powered everything" fluff — be specific about what each product does
- The visitor should be able to identify which product is for them in under 10 seconds
