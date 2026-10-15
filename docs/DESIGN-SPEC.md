# Midha Limited website: design specification and build handoff

Version 1 · 15 October 2026 · Direction: "Earth & Stone"
Built as a static site for Cloudflare Pages (see `DEPLOY-TO-CLOUDFLARE.md`).

## A. Decisions and assumptions log

| Topic | Decision | Source |
|---|---|---|
| Business | Midha Limited, Wainuiomata. NZBN 9429051638016. 022 407 8603. midhalimited@gmail.com. Mon–Sat 7:30am–6:00pm | Blueprint, confirmed |
| Services | Three separate lines: **Test & Tag**, **Heat Pump Cleaning**, **Electrical Services** | Client |
| AS/NZS 3760:2010 | Shown on Test & Tag content only, never as a business-wide badge | Client |
| Heat pump packages | Pro $79, Elite $129 (Most popular), Comprehensive $189. Per heat pump, GST incl. | Client |
| Pro vs Elite | Pro: indoor vacuum clean, outdoor pressure wash. Elite: indoor and outdoor pressure wash, plus check sheet | Client |
| Mould guarantee | 3 months, free re-clean (old site said 12 months; corrected) | Client |
| Under Heat Pump Cleaning | Filter replacement, emergency repairs, pipe insulation repair, Healthy Homes heating compliance. Quote on request | Client |
| Electrical Services | Light installations, LED downlights, security and sensor lights, power points, cord and lead repairs | Client |
| RCD testing | Under Test & Tag | Client |
| Stats | 14,500+ items tested (commercial test & tag), 200+ home heat pumps serviced, < 2 hr reply, 5.0 Google | Client |
| Reviews | The 8 existing reviews kept for now | Client |
| Giveaway | "Win a free heat pump clean" is running; banner + section. Entry: like post, tag 3 Wellington friends | Client, promo image |
| Logo | Cartoon technician mascot, used as supplied | Client |
| Domain / host | midha.co.nz on Cloudflare (Pages) | Client |
| Form | Formspree to midhalimited@gmail.com; until set up, falls back to opening the visitor's email app | Client agreed Formspree |
| Test & tag image | No real photo yet and stock photos couldn't be downloaded here, so a drawn test-tag illustration is used | [ASSUMPTION] |
| "Licensed", "WorkSafe compliant", "insured" claims | Left off the site until confirmed | [NEEDS INPUT] |

## B. Reference digest (from the DNA blueprint)

**Kept:** sticky header with phone and quote button; quote form at the end of every page; stats row; service cards; reviews; service-area list with response times; FAQ accordion; breadcrumbs; LocalBusiness/FAQ structured data.
**Adapted:** one-page-per-service structure (the old site mixed everything into one Services page); dark navy + orange became stone, sage, charcoal and the client's gold; hero is a real job photo with a frosted panel instead of a faded stock image.
**Dropped:** scrolling USP ticker (distracting, poor for accessibility); Ken Burns zoom; scroll progress bar; unverified claims; the 404'd Service Areas link (now a real page).

## C. Strategy

**Positioning:** One local Wainuiomata team for workplace test & tag, heat pump deep cleaning and small electrical jobs, with fixed upfront prices and quick replies.
**Audiences and their questions:**
- Homeowners: How much? Will it fix the smell / power bill? Will you make a mess? → per-unit prices, package comparison, "mess-free" section, guarantee.
- Landlords / property managers: Will this satisfy Healthy Homes? Can I get a report? → Healthy Homes card, digital report.
- Businesses: Is it to the standard? Will it disrupt us? Do I get a register? → AS/NZS 3760, QR tags, PDF register, flexible hours.

**Brand cues:** calm, premium, trustworthy, Kiwi. Plain wording ("sorted", "no surprises"), suburbs named, real photos.

## D. Sitemap and navigation

```
/                      Home
/test-and-tag/         Test & Tag
/heat-pump-cleaning/   Heat Pump Cleaning (packages, extras, Healthy Homes, giveaway)
/electrical-services/  Electrical Services
/service-areas/        Service Areas (anchors per area)
/reviews/              Reviews
/about/                About
/contact/              Contact + quote form
/privacy/              Privacy note
/thanks/               Form success (noindex)
/404.html              Not found
```

**Primary nav:** Services ▾ (Test & Tag, Heat Pump Cleaning, Electrical Services) · Service areas ▾ · Reviews · About · Contact · phone · **Get a quote**.
**Mobile:** hamburger opens a full-width panel; floating Call / Get a quote bar is fixed at the bottom.
**Footer:** brand + NZBN, Services, Service areas, Get in touch, Privacy.
**Redirects:** `/services` → `/heat-pump-cleaning/` and other old addresses (see `_redirects`).

## E. User journeys and conversion

1. Homeowner searching "heat pump cleaning Lower Hutt" → Heat Pump page → compares packages → "Book Elite Clean" → contact form pre-selected with Elite → sent → /thanks/.
2. Business manager → Home → Test & Tag card → inclusions + reviews → quote form (count of items).
3. Landlord → Heat Pump page → Healthy Homes card → "Ask about Healthy Homes" → form pre-selected.
4. Phone-first visitor on mobile → taps **Call now** in the action bar.

**CTAs:** primary "Get a free quote" (header, hero, each service page, every package card, footer); secondary "Call 022 407 8603" (header, hero, action bar, contact list).
**Trust plan:** stats and 5.0 rating near the top; reviews filtered by service on service pages; fixed-price promise and privacy note at the form.

## F. Page templates

Every inner page: announcement bar → header → breadcrumb hero (eyebrow, H1, lead, CTAs) → content sections alternating stone / sage → FAQ (where useful) → quote section → footer → mobile action bar.

**Home:** photo hero with glass panel → three-service chooser (overlaps the hero) → stats → heat pump packages (compact) → Why Midha (dark) → 3 reviews → service areas → FAQ → quote form.
**Heat Pump Cleaning:** hero → 3 price cards with expandable "Everything included" → extras grid (filter, emergency repairs, pipe insulation before/after, Healthy Homes) → how we work (photos) → giveaway → FAQ → quote.
**Test & Tag:** hero with AS/NZS 3760 badge → inclusions + tag illustration → who we test for + 3 feature cards → test & tag reviews → FAQ → quote.
**Electrical Services:** hero → 5 service cards + "Ask us" card → how we work → FAQ → quote.
**Service Areas:** 6 area cards (response-time badge, suburbs, book link) → quote.
**Reviews:** 8 review cards → quote. **About:** story + photo → 3 commitments → quote. **Contact:** quote form first → service zone chips.

## G. Visual design system

**Colour**

| Role | Hex | Use | Contrast |
|---|---|---|---|
| Background (stone) | #FDFCF8 | page | — |
| Surface | #FFFFFF | cards | — |
| Sage | #E2E8E4 | alternating sections | — |
| Charcoal (primary) | #1C1C1C | text, primary buttons, dark sections | 16.6:1 on stone |
| Body text | #3A3A36 | paragraphs | 11:1 |
| Muted text | #4A4A45 | secondary | 8.7:1 |
| Brand gold | #978B7A | gold buttons/badges (with charcoal text) | 5.1:1 charcoal on gold |
| Deep gold | #6E6354 | small gold labels on light | 5.7:1 on stone |
| Bright gold | #D4AF37 | ticks/stars on charcoal only | 8.1:1 on charcoal |
| Icon gold | #B08A1E | ticks/stars on light (non-text) | 3.15:1 (meets 3:1 for graphics) |
| Urgent red | #DC2626 | real deadlines only (giveaway) | 4.8:1 white on red |
| Focus | #1C1C1C (white on dark) | 3px outline, 3px offset | — |
| Success / error | #2F6B47 / #B42318 | form messages | ≥ 5:1 |

**Typography:** General Sans 600–700 for headings (tracking −0.02em), Switzer 400–600 for body. Both free for commercial use from Fontshare (ITF Free Font Licence), loaded from `api.fontshare.com` with system fallbacks.
Scale (fluid with `clamp()`): H1 34→58px, H2 28→44px, H3 20→24px, body 17px/1.6, small 14px, eyebrow 13px uppercase +0.12em.

**Layout:** max width 1240px; gutter 16→32px; section padding 56→96px; 12-ish grid realised as 2/3/4-column CSS grids.
**Shape:** radius 40px (hero, CTA band), 32px (cards), 24px (FAQ items), pill buttons. Shadows: soft `0 8px 30px rgba(28,28,28,.06)`, lift `0 18px 40px rgba(28,28,28,.10)`. Glass: `rgba(253,252,248,.8)` + `backdrop-filter: blur(12px)` on header, hero panel and mobile bar.
**Icons:** inline outline SVG, 1.8px stroke, round caps (Lucide-style).

## H. Component library

| Component | Variants | States | Used on | Notes |
|---|---|---|---|---|
| Announcement bar | — | link hover | all | Giveaway link |
| Header | sticky glass | scrolled | all | Phone + quote CTA; logo links home |
| Dropdown | Services, Areas | open/closed, focus | all | Button with `aria-expanded`; Esc closes |
| Mobile menu | — | open/closed | all ≤1080px | Toggle with `aria-controls` |
| Button | primary, light, outline, gold, block | hover scale 1.05, focus ring, disabled | all | ≥48px tall |
| Badge | urgent (pulse), gold, soft | — | hero, cards | Pulse off with reduced motion |
| Hero | photo + glass panel; breadcrumb hero | — | home; inner | One H1 per page |
| Service chooser card | light, ink | hover lift −4px | home | Whole card is a link |
| Price card | standard, featured (ink) | hover lift, details open | home, heat pump | `details` for inclusions |
| Feature item | light, on dark | — | home, test & tag | Icon chip + H3 + text |
| Review card | — | — | home, reviews, test & tag | Stars `role="img"` labelled |
| Before/after | — | — | heat pump | Captions as badges |
| Area card | — | — | service areas | Anchor IDs for nav |
| FAQ accordion | light, sage | open/closed | most pages | Native `details/summary`, first open; FAQPage schema |
| Quote form | — | default, invalid, sending, success, error | every page | Labels, required marks, inline errors, honeypot |
| Footer | — | — | all | 4 → 2 → 1 columns |
| Mobile action bar | — | — | all ≤760px | Call / Get a quote |

## I. Voice and microcopy

1. **Plain and direct.** Do: "Fixed price. No surprises." Don't: "Transparent value-driven pricing solutions."
2. **Local.** Do: name suburbs, "Wainui". Don't: generic "your area".
3. **Calm confidence.** Do: "Properly done." Don't: ALL CAPS urgency or fake scarcity.
4. **Helpful.** Do: tell people which package suits them. Don't: hide prices.

CTAs: "Get a free quote", "Book Elite Clean", "Call 022 407 8603". Errors: "Please enter a phone number so we can reach you." Success: "Thanks, we’ve got your request."

## J. Imagery

Client photos used: indoor coil wash (hero, about), outdoor unit wash, cleaning-bag setup, pipe insulation before/after, giveaway poster, logo. Resized to 800/1600px in WebP + JPEG, lazy-loaded below the fold, hero preloaded with high priority.
**Shot list still wanted:** technician tagging a power tool (replaces the illustration), QR tag close-up, LED downlight install, a finished clean with the unit reassembled, the van with branding. Daylight, real Wellington sites, warm natural grade, no posed stock smiles.
**Alt text:** describe what the person is doing and to what ("Midha technician washing the coil of an indoor heat pump").

## K. Responsive rules

Breakpoints: ≤420 (small phone: header quote button hidden), ≤560 (form single column), ≤680 (all grids 1 col), ≤760 (action bar appears, stats 2×2), ≤860/900 (split layouts and quote stack), ≤1000 (3-col → 2-col), ≤1080 (hamburger menu).
First mobile screen: promo strip, logo, hero headline, quote and call buttons, persistent action bar. Touch targets ≥44px.

## L. Interaction and motion

Buttons scale 1.05 on hover (200ms). Cards lift −4px with a deeper shadow (250ms). Sections fade up 16px on first view (600ms, ease `cubic-bezier(.2,.7,.2,1)`). Urgent badge pulses (2s). FAQ "+" rotates to "×". All motion is removed under `prefers-reduced-motion`.
Form: validates on submit, then live on blur; focuses the first invalid field; status message is announced (`role="status"`).

## M. Accessibility (WCAG 2.2 AA)

Skip link; landmarks (header, nav, main, footer); one H1 per page; visible 3px focus rings; dropdowns are real buttons with `aria-expanded`; Esc closes menus; form labels on every field, errors linked with `aria-describedby`, `aria-invalid` set; decorative SVGs `aria-hidden`; no text below 4.5:1; no horizontal scroll at 390px phone width or 1440px desktop (checked); 320px still to be tested.

## N. SEO and performance

| Page | Title |
|---|---|
| Home | Test & Tag, Heat Pump Cleaning & Electrical \| Midha Limited Wellington |
| Heat pump | Heat Pump Cleaning Wellington from $79 \| Midha Limited |
| Test & tag | Test and Tag Wellington \| AS/NZS 3760 \| Midha Limited |
| Electrical | Electrical Services Wellington \| Lighting & Power Points \| Midha |
| Areas | Service Areas \| Wainuiomata, Hutt Valley, Tawa, Porirua \| Midha Limited |

Each page has a meta description, canonical URL, Open Graph image (`og-image.jpg`), and JSON-LD: LocalBusiness (all pages), BreadcrumbList, FAQPage, Service with Offers (heat pump prices). `sitemap.xml` and `robots.txt` included.
Targets: LCP ≤ 2.5s (hero is a 240KB WebP with high fetch priority), CLS ≤ 0.1 (image sizes reserved), INP ≤ 200ms (one small script, no frameworks).

## O. Functional requirements

| Function | Status | Tool | Priority |
|---|---|---|---|
| Quote form | Built | Formspree (add ID in `main.js`); mailto fallback | REQUIRED |
| Click-to-call / email | Built | `tel:` / `mailto:` | REQUIRED |
| Service pre-select from "Book" buttons | Built | `?service=` URL parameter | REQUIRED |
| Redirects from old URLs | Built | Cloudflare `_redirects` | REQUIRED |
| Security and cache headers | Built | Cloudflare `_headers` | REQUIRED |
| Analytics | Not built | Cloudflare Web Analytics (toggle in dashboard) | OPTIONAL |
| Live Google reviews | Not built | Manual for now | LATER |
| Online booking calendar | Not built | — | LATER |
| Cookie banner | Not needed | No cookies are set | — |

## P. Design tokens

```yaml
colors:
  primary: "#1C1C1C"
  secondary: "#E2E8E4"
  accent: "#978B7A"
  background: "#FDFCF8"
  surface: "#FFFFFF"
  text: "#1C1C1C"
  text_muted: "#4A4A45"
  border: "#EEEAE1"
  cta: "#1C1C1C"
  cta_hover: "#000000"
  focus: "#1C1C1C"
  success: "#2F6B47"
  warning: "#D4AF37"
  error: "#B42318"
  urgent: "#DC2626"
typography:
  font_heading: "General Sans, Hanken Grotesk, system-ui, sans-serif"
  font_body: "Switzer, Instrument Sans, system-ui, sans-serif"
  scale: { h1: "clamp(2.1rem,1.3rem+3.4vw,3.6rem)", h2: "clamp(1.75rem,1.2rem+2vw,2.75rem)", h3: "clamp(1.25rem,1.1rem+.5vw,1.5rem)", body: "1.0625rem", small: "0.875rem", caption: "0.8125rem" }
  weights: { body: 400, medium: 500, semibold: 600, bold: 700 }
  line_heights: { heading: 1.05, body: 1.6 }
  letter_spacing: { heading: "-0.02em", eyebrow: "0.12em" }
spacing:
  scale: [4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 96]
  section_padding: "clamp(56px, 8vw, 96px)"
layout:
  max_width: "1240px"
  grid_columns: [2, 3, 4]
  gutter: "clamp(16px, 4vw, 32px)"
  breakpoints: { mobile: "<760px", tablet: "760-1079px", desktop: ">=1080px", wide: ">=1440px" }
radius: { xl: "40px", lg: "32px", md: "24px", pill: "999px" }
shadows: { soft: "0 8px 30px rgba(28,28,28,.06)", lift: "0 18px 40px rgba(28,28,28,.10)" }
borders: { default: "1px solid #EEEAE1", input: "1px solid #CFCAC0" }
motion:
  durations: { fast: "200ms", base: "250ms", reveal: "600ms", pulse: "2s" }
  easings: { standard: "cubic-bezier(.2,.7,.2,1)" }
z_index: { header: 50, action_bar: 60, skip_link: 100 }
```

The matching CSS custom properties are at the top of `site/assets/css/styles.css`.

## Q. Build specification

- **Stack:** static HTML/CSS/JS, no framework, no build step on Cloudflare. Pages are generated from `build.py` (kept with the project files, not deployed) so header, footer and form stay identical everywhere. Edit `build.py`, run `python3 build.py`, redeploy `site/`.
- **Static vs dynamic:** all content static. Form posts to Formspree. No CMS. Reviews and prices are edited in `build.py` (`REVIEWS`, `packages_section`).
- **Consistency:** components use tokens only; no inline colours except a few one-off layout tweaks.
- **Later phases:** individual suburb landing pages, real test & tag photography, Google reviews widget, online booking.

## R. Quality check and open items

- **Originality:** no copy, logo, imagery or palette reused from the reference preview's visual identity. The client's own facts, reviews and photos are used with permission.
- **Checked:** every page renders at 390px and 1440px with no horizontal scroll and no script errors; mobile menu and form validation tested.
- **Open items [NEEDS INPUT]:**
  1. Formspree form ID (form uses email-app fallback until added).
  2. Giveaway closing date and the link to the giveaway post.
  3. Real photo for Test & Tag (and electrical work).
  4. Confirm before adding: "licensed", "WorkSafe compliant", "public liability insurance".
  5. The 8 reviews: confirm they are real customer reviews, or replace them with Google reviews.
  6. Approximate test & tag pricing if you want to show "from $X per item".
