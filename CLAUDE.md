# CLAUDE.md — Arthashastra Insights

**Owner:** Manish Mishra | SEBI Registered Research Analyst (Individual, Part-Time)
**SEBI Reg. No.:** INH000024620 | **NISM Cert. No.:** 202400095615
**Live site:** https://www.arthashastrainsights.com
**Repo:** github.com/apnamanish9/arthashastrainsights
**Local:** D:\Claude code folder\arthashastrainsights

---

## 1. Tech Stack Decision

**Current:** Vanilla HTML/CSS/JS → Cloudflare Pages
**Target:** Astro (static site generator) → Cloudflare Pages (same deployment)

### Why Astro (not Next.js, not staying vanilla)

| Concern | Vanilla HTML | Astro | Next.js |
|---|---|---|---|
| Blog/CMS | Manual HTML per post | Markdown in `src/content/blog/` | MDX or external CMS |
| Nav/footer duplication | 4 copies today; grows to 10+ | Single component, zero drift | Single component |
| Performance | Already excellent | 100 Lighthouse by default | Cold-start edge risks |
| Cloudflare deploy | `wrangler pages deploy .` | `astro build` then `wrangler pages deploy ./dist` | Complex `@cloudflare/next-on-pages` |
| Learning curve | Zero | Low (Astro files = HTML + frontmatter) | High |
| Form backend | Formspree (3rd party) | Cloudflare Pages Functions | API routes |
| Cost | Free | Free | Free (within limits) |

**Decision rationale:** The site is fundamentally static content + compliance pages + a blog. Astro generates pure static HTML (zero JS shipped by default), maps naturally to the existing HTML/CSS skill set, has a native Cloudflare adapter, and lets Markdown blog posts be committed directly to git without a headless CMS. Next.js is overkill and the Cloudflare integration is fragile. Staying vanilla becomes unmaintainable beyond ~6 pages due to duplicated nav/footer.

---

## 2. Folder Structure (Astro)

```
arthashastrainsights/
├── functions/                        # Cloudflare Pages Functions (form backends)
│   └── api/
│       ├── contact.js                # Handles contact form → sends email via Resend
│       └── grievance.js              # Handles grievance form → sends email via Resend
├── public/                           # Static assets served as-is
│   ├── assets/
│   │   ├── images/
│   │   │   ├── Arthashastrainsights_logo1.png
│   │   │   └── manish-mishra.jpg     # Professional headshot (add this!)
│   │   ├── MITC.pdf
│   │   └── RA-Investor-Charter.pdf
│   ├── robots.txt
│   └── favicon.png
├── src/
│   ├── components/
│   │   ├── ComplianceTicker.astro    # The gold scrolling compliance bar
│   │   ├── Nav.astro                 # Sticky navbar (hamburger + links)
│   │   ├── Footer.astro              # Full footer with SEBI disclosure strip
│   │   ├── ServiceCard.astro         # Research service card
│   │   ├── TrainingCard.astro        # Course card
│   │   ├── ContactForm.astro         # Contact form (POST to /api/contact)
│   │   └── GrievanceForm.astro       # Grievance form (POST to /api/grievance)
│   ├── layouts/
│   │   ├── Base.astro                # Head + ticker + nav + footer + cookie + scripts
│   │   └── Legal.astro               # Base + page-hero + breadcrumb (for legal pages)
│   ├── pages/
│   │   ├── index.astro               # Homepage (hero, ticker, about, services, training, V&M, why, contact)
│   │   ├── about.astro               # Dedicated About/Credibility page
│   │   ├── services.astro            # Services & Pricing page (with actual prices)
│   │   ├── blog/
│   │   │   ├── index.astro           # Blog listing
│   │   │   └── [...slug].astro       # Blog post page
│   │   ├── contact.astro             # Standalone contact page
│   │   ├── disclaimer.astro
│   │   ├── privacy-policy.astro      # Separate from disclaimer
│   │   ├── terms-of-use.astro
│   │   ├── investor-charter.astro    # HTML version of the charter PDF
│   │   └── grievance-redressal.astro
│   ├── content/
│   │   ├── config.ts                 # Blog collection schema
│   │   └── blog/
│   │       └── *.md                  # Blog posts (Markdown)
│   └── styles/
│       └── global.css                # Current style.css content (unchanged)
├── astro.config.mjs
├── package.json
├── wrangler.toml
└── CLAUDE.md                         # This file
```

---

## 3. Coding Standards & Content Rules

### HTML/Astro
- Use semantic HTML5 elements (`<main>`, `<article>`, `<section>`, `<header>`, `<footer>`, `<nav>`)
- Every page must include `lang="en"` on `<html>`; add `lang="hi"` attributes on Hindi-language text spans
- `aria-label` on all interactive elements without visible text labels
- No inline styles on repeating elements — use CSS classes

### CSS
- Keep CSS variables in `:root` (navy, gold, fonts, radii, transitions)
- All new styles go in `src/styles/global.css`; no per-component `<style>` blocks except for minor layout overrides
- Mobile-first: base styles for ≤768px, then progressive enhancement with `@media (min-width: ...)`
- Never use `!important` except to override third-party widget styles

### JavaScript
- Vanilla JS only (no frameworks in client JS)
- IIFE pattern: `(function () { 'use strict'; ... })()`
- No `console.log` in committed code
- Form submissions: POST to `/api/contact` or `/api/grievance` (Cloudflare Pages Functions), not Formspree

### Deployment
```bash
# Standard deploy (run from project root)
git add <files>
git commit -m "Description"
git push
npm run build                                                          # astro build → outputs to ./dist
npx wrangler pages deploy ./dist --project-name=arthashastrainsights  # deploy to Cloudflare
```

### During Astro migration only (pre-build-step)
```bash
# Legacy deploy (current, pre-Astro)
git add .
git commit -m "Website update"
git push
npx wrangler pages deploy . --project-name=arthashastrainsights
```

---

## 4. SEBI Compliance Rules — NON-NEGOTIABLE

### Standard SEBI RA Disclaimer (verbatim — never paraphrase)
Every page with financial language (services, pricing, research, recommendations) must include:

> **Manish Mishra** | SEBI Registered Research Analyst (Individual, Part-Time) | Reg. No. **INH000024620** | NISM Cert. No.: 202400095615 | **Arthashastra Insights is a brand name and NOT a SEBI registered entity.** Investments in securities market are subject to market risk. Read all related documents carefully before investing. Past performance is not indicative of future results. Registration granted by SEBI and certification from NISM in no way guarantee performance or assurance of returns.

### Rules
1. **Compliance ticker** (`ComplianceTicker.astro`) must appear on EVERY page, above the nav bar
2. **Footer SEBI strip** must appear on EVERY page with full registration details
3. The phrase "brand name and NOT a SEBI registered entity" must appear verbatim; cannot be paraphrased
4. **Never display historical performance/returns** without the exact SEBI disclaimer that past performance is not indicative of future results
5. **Pricing page**: Must show SEBI fee cap disclosure (max ₹1,51,000 per annum per client family per household per SEBI circular)
6. **Research reports** (if published): Must include per-report analyst disclosure (holdings, conflicts, basis) per Reg. 19(1) of SEBI RA Regulations 2014
7. **Testimonials**: Never attribute specific returns/gains to any client. Testimonials about service quality are acceptable; testimonials claiming "I made X% profit" are not
8. **Privacy Policy** must be separate from Disclaimer (DPDPA 2023 compliance)
9. **Grievance tables**: Must be updated monthly (by the 7th of each month for the prior month). Current tables are in `grievance-redressal.html`/`.astro`
10. **SCORES + SmartODR links**: Must be present on grievance page and in footer

### Mandatory pages (all must exist and be accessible)
- `/disclaimer` — full disclaimer including conflict of interest
- `/privacy-policy` — standalone (separate from disclaimer)
- `/terms-of-use` — full ToU
- `/investor-charter` — HTML version (not just PDF)
- `/grievance-redressal` — with active form + SEBI complaint data tables
- `/assets/MITC.pdf` — publicly accessible
- `/assets/RA-Investor-Charter.pdf` — publicly accessible

---

## 5. Phase Plan Summary

| Phase | Deliverable | Exit Criteria |
|---|---|---|
| **1 — Critical Fixes** (now) | Fix all 404 nav links; add photo; fix copyright year inconsistency; update grievance table month; add og:image | Zero 404s on internal links; all 4 pages load on click |
| **2 — Compliance Hardening** | New: investor-charter.html, privacy-policy.html; add SEBI fee cap note to services; separate Disclosure per Reg 19 | All mandatory SEBI pages exist as HTML (not just PDF) |
| **3 — IA Restructure** | Standalone: about.html, services.html (with pricing), contact.html; fix sitemap to match real pages | Sitemap URLs return 200; nav links correct on all pages |
| **4 — Astro Migration** | Full Astro project; nav/footer as single components; Cloudflare Pages Functions replacing Formspree; blog skeleton | `npm run build` succeeds; all existing URLs return 200; forms work |
| **5 — Design Upgrade** | Real photo; consistent dark theme (remove white Why-Choose-Us island); hero without generic Unsplash; credential badge row; self-hosted fonts | Lighthouse Performance ≥ 90 on mobile; no external font/image deps at load |
| **6 — Content/Blog** | 6 published blog posts; YouTube embed section (latest 3 videos); email capture (Brevo free tier) | Blog indexed by Google; ≥1 post/week cadence set |
| **7 — Lead Gen & Conversion** | Telegram CTA; WhatsApp Business number; pricing page with conversion flow; newsletter drip sequence (3 emails) | Contact form submit rate ≥ baseline + 20% |
| **8 — SEO & Perf Hardening** | Person + Organization schema markup; Hindi meta alternate; Cloudflare Analytics wired; Core Web Vitals LCP < 2.5s; sitemap auto-generated | PageSpeed Insights mobile score ≥ 90; schema validated in Rich Results Test |

---

## 6. Known Issues (from April 2026 build — fix in Phase 1)

1. `about.html`, `services.html`, `stock-picks.html`, `contact.html`, `investor-charter.html` — referenced in footer/sitemap but **do not exist** (404)
2. About section has placeholder ("Your Photo") — no real photo
3. Copyright year: index.html says 2026, disclaimer.html + grievance-redressal.html say 2025
4. Disclaimer.html and grievance-redressal.html use old nav structure (`.main-nav`) referencing non-existent pages
5. Grievance table header says "MARCH 2026" — needs monthly updates
6. Cookie consent references "analytics" but no analytics script is loaded — misleading
7. `og:image` meta tag missing on all pages
8. Google Fonts loaded twice (CSS `@import` AND `<link>` tags) — remove the `@import` from CSS
9. "Why Choose Us" section uses `background:#F8F7F4` (light) — jarring against dark theme
10. Unsplash hero/card images are external CDN calls — self-host for reliability and performance
11. Personal Gmail (apnamanish9@gmail.com) used as professional contact — add domain email routing via Cloudflare Email Routing

---

## 7. Key External Dependencies

| Service | Purpose | Status | Alternative |
|---|---|---|---|
| Formspree xnjlvavz | Contact form | Active | Cloudflare Pages Function + Resend |
| Formspree xaqajwjl | Grievance form | Active | Cloudflare Pages Function + Resend |
| TradingView widget | Market ticker | Active | Keep (no good self-hosted alt) |
| Google Fonts (Inter + Playfair Display) | Typography | Active | Self-host via fontsource npm or local woff2 |
| Unsplash | Hero + card background images | Active | Download and serve from /public/assets/images/ |
| Cloudflare Pages | Hosting + CDN | Active | Keep |

---

## 8. Contacts & Credentials

- **Analyst:** Manish Mishra
- **SEBI Reg. No.:** INH000024620
- **NISM Cert. No.:** 202400095615
- **Registration type:** Individual, Part-Time Research Analyst
- **Email:** apnamanish9@gmail.com
- **Phone/WhatsApp:** +91 9480322410
- **YouTube:** https://www.youtube.com/@Arthashastrainsights
- **Address:** GF-06, Winds Of Change, Judicial Layout, Thalaghattapura, Bangalore - 560062, Karnataka, India
- **Jurisdiction:** Courts of Bangalore, Karnataka, India
- **Grievance escalation:** SEBI SCORES (scores.sebi.gov.in) → SmartODR (smartodr.in) → SEBI Toll Free: 1800 266 7575
