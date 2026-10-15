"""Generates the static Midha Limited website into ./site.

Each page is plain HTML (no build step needed on Cloudflare Pages).
Edit the content below and re-run:  python3 build.py
"""
import json, os, html, datetime

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "site")
SITE = "https://midha.co.nz"
PHONE = "022 407 8603"
TEL = "+64224078603"
EMAIL = "midhalimited@gmail.com"
NZBN = "9429051638016"
HOURS = "Mon–Sat 7:30am–6:00pm"
TODAY = datetime.date(2026, 10, 15).isoformat()

e = html.escape

# ---------------------------------------------------------------- icons
def icon(name, size=24, color="currentColor"):
    paths = {
        "tag": '<path d="M20.6 13.4 13.4 20.6a2 2 0 0 1-2.8 0L3 13V3h10l7.6 7.6a2 2 0 0 1 0 2.8Z"/><circle cx="7.5" cy="7.5" r="1.5"/>',
        "fan": '<circle cx="12" cy="12" r="2"/><path d="M12 10c0-4 1-7 4-7s3 4-1 7"/><path d="M14 12c4 0 7 1 7 4s-4 3-7-1"/><path d="M12 14c0 4-1 7-4 7s-3-4 1-7"/><path d="M10 12c-4 0-7-1-7-4s4-3 7 1"/>',
        "bulb": '<path d="M9 18h6"/><path d="M10 22h4"/><path d="M12 2a7 7 0 0 0-4 12.7c.6.5 1 1.3 1 2.1V18h6v-1.2c0-.8.4-1.6 1-2.1A7 7 0 0 0 12 2Z"/>',
        "phone": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2Z"/>',
        "mail": '<rect x="2" y="4" width="20" height="16" rx="3"/><path d="m22 7-10 6L2 7"/>',
        "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
        "pin": '<path d="M12 22s7-6.2 7-12a7 7 0 0 0-14 0c0 5.8 7 12 7 12Z"/><circle cx="12" cy="10" r="2.5"/>',
        "shield": '<path d="M12 22s8-3.5 8-10V5l-8-3-8 3v7c0 6.5 8 10 8 10Z"/><path d="m9 12 2 2 4-4"/>',
        "qr": '<rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><path d="M14 14h3v3h-3zM20 14v.01M14 20h.01M17 20h4v-3"/>',
        "dollar": '<circle cx="12" cy="12" r="9"/><path d="M15 9.5c-.5-1-1.6-1.5-3-1.5-1.7 0-3 .9-3 2.2 0 3 6 1.6 6 4.6 0 1.3-1.3 2.2-3 2.2-1.4 0-2.6-.6-3-1.6M12 6.5V8m0 8v1.5"/>',
        "leaf": '<path d="M11 20A7 7 0 0 1 4 13c0-6 7-9 16-9 0 9-3 16-9 16Z"/><path d="M4 20c4-4 7-6 11-8"/>',
        "home": '<path d="m3 11 9-8 9 8"/><path d="M5 10v10h14V10"/><path d="M10 20v-6h4v6"/>',
        "plug": '<path d="M9 2v6M15 2v6"/><path d="M6 8h12v4a6 6 0 0 1-12 0Z"/><path d="M12 18v4"/>',
        "bolt": '<path d="M13 2 4 14h7l-1 8 9-12h-7l1-8Z"/>',
        "wrench": '<path d="M14.7 6.3a4 4 0 0 0 5 5L22 14l-8 8-2.3-2.3a4 4 0 0 0-5-5L2 10l8-8 2.3 2.3a4 4 0 0 0 2.4 2Z"/>',
        "star": '<path d="m12 3 2.8 5.7 6.2.9-4.5 4.4 1.1 6.2L12 17.3 6.4 20.2l1.1-6.2L3 9.6l6.2-.9Z"/>',
        "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
        "chev": '<path d="m6 9 6 6 6-6"/>',
    }
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" '
            f'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">{paths[name]}</svg>')

def pic(name, alt, w=800, cls="", sizes="(max-width: 860px) 100vw, 50vw", eager=False, big=False):
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    srcset_webp = f"/assets/img/{name}-800.webp 800w" + (f", /assets/img/{name}-1600.webp 1600w" if big else "")
    srcset_jpg = f"/assets/img/{name}-800.jpg 800w" + (f", /assets/img/{name}-1600.jpg 1600w" if big else "")
    c = f' class="{cls}"' if cls else ""
    return (f'<picture><source type="image/webp" srcset="{srcset_webp}" sizes="{sizes}">'
            f'<img src="/assets/img/{name}-800.jpg" srcset="{srcset_jpg}" sizes="{sizes}" alt="{e(alt)}"{c} {load} decoding="async"></picture>')

# ---------------------------------------------------------------- shared data
SERVICES = [
    ("test-tag", "/test-and-tag/", "Test & Tag", "tag"),
    ("heat-pump", "/heat-pump-cleaning/", "Heat Pump Cleaning", "fan"),
    ("electrical", "/electrical-services/", "Electrical Services", "bulb"),
]
AREAS = [
    ("Wainuiomata", "Same day / next day", "Our home base. No callout surcharge in Wainuiomata.", ["Wainuiomata", "Arakura", "Homedale"]),
    ("Lower Hutt", "Within 24 hours", "Homes, rentals, workshops and offices across the valley floor.", ["Petone", "Gracefield", "Epuni", "Waterloo", "Naenae"]),
    ("Upper Hutt", "Same week", "Regular runs up the valley for homes and businesses.", ["Silverstream", "Trentham", "Upper Hutt Central"]),
    ("Tawa", "24–48 hours", "Heat pump cleans and workplace tagging in the northern suburbs.", ["Tawa", "Linden", "Redwood"]),
    ("Newlands", "Flexible booking", "Booked around your schedule, including Johnsonville.", ["Newlands", "Johnsonville", "Paparangi"]),
    ("Porirua & Greater Wellington", "Scheduled dispatch", "Planned visits across Porirua and the wider region.", ["Porirua", "Wellington City (by arrangement)"]),
]
REVIEWS = [
    ("Craig Henderson", "Workshop Manager · Hutt Valley Engineering", "Test & Tag", "Feb 2026",
     "Midha tested over 350 power tools and industrial units across our facility. The QR tags make tracking effortless, and our audit register was emailed that evening. Punctual, polite, and top-tier Kiwi professionals."),
    ("Sarah McLachlan", "Homeowner · Silverstream, Upper Hutt", "Heat Pump Cleaning", "Jan 2026",
     "Our heat pump smelled musty whenever we turned on heat mode. Midha took the unit apart, treated the coils with foam sanitiser and flushed it thoroughly. The difference in air quality and heating speed was immediate. Highly recommend!"),
    ("Tania Ross", "Senior Property Manager · Wellington Residential Rentals", "Healthy Homes Heating", "Dec 2025",
     "We use Midha Limited for our rental heat pump compliance and annual servicing. Their digital reports are thorough and have satisfied every Tenancy Services audit. Extremely reliable."),
    ("Marcus Davies", "Site Foreman · Lower Hutt Construction", "Test & Tag", "Nov 2025",
     "Having a Kiwi technician who understands WorkSafe rules and shows up at 7am before the boys hit the tools is invaluable. Replaced two frayed cords on the spot too."),
    ("Elena Petrov", "Resident · Tawa", "Heat Pump Cleaning", "Oct 2025",
     "Our power bill shot up last winter. Midha cleaned out the caked lint and the leaves in the outdoor coil, and our power use dropped noticeably the next month. Super clean, zero mess left in the living room."),
    ("Kev & Aroha Broughton", "Homeowners · Wainuiomata", "Heat Pump Cleaning", "Sep 2025",
     "Friendly local lads. Gave us honest advice on our heat pump placement and did a great job cleaning both units. Great to support a Kiwi-owned business right here in Wainui."),
    ("Liam O'Connor", "Cafe Owner · Petone", "Test & Tag", "Aug 2025",
     "Tested all our kitchen appliances, coffee grinders and POS gear without disrupting the lunch rush. Clean, quiet, and very reasonably priced. We'll use them every 12 months."),
    ("Priya Sharma", "Landlord · Newlands", "Healthy Homes Heating", "Jul 2025",
     "Booked online and had the assessment done within 48 hours. The report was concise and clear. Great communication from start to finish."),
]
SERVICE_OPTIONS = [
    ("Heat pump – Elite Clean ($129)", "elite"),
    ("Heat pump – Pro Clean ($79)", "pro"),
    ("Heat pump – Comprehensive Clean ($189)", "comprehensive"),
    ("Heat pump – Filter replacement / repairs / pipe insulation", "heat-pump-other"),
    ("Healthy Homes heating compliance", "healthy-homes"),
    ("Test & Tag (workplace)", "test-tag"),
    ("Electrical services (lighting, power points, cords)", "electrical"),
    ("Something else", "other"),
]

# ---------------------------------------------------------------- layout
def head(title, desc, path, extra_ld=None):
    url = SITE + path
    ld = [{
        "@context": "https://schema.org", "@type": "LocalBusiness", "@id": SITE + "/#business",
        "name": "Midha Limited", "url": SITE + "/", "telephone": TEL, "email": EMAIL,
        "image": SITE + "/assets/img/og-image.jpg", "logo": SITE + "/assets/img/logo-512.png",
        "description": "Test & tag, heat pump cleaning and electrical services across Greater Wellington.",
        "address": {"@type": "PostalAddress", "addressLocality": "Wainuiomata", "addressRegion": "Wellington", "addressCountry": "NZ"},
        "areaServed": [a[0] for a in AREAS],
        "openingHoursSpecification": [{"@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"], "opens": "07:30", "closes": "18:00"}],
        "identifier": {"@type": "PropertyValue", "propertyID": "NZBN", "value": NZBN},
    }]
    if extra_ld: ld += extra_ld
    return f"""<!doctype html>
<html lang="en-NZ" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#FDFCF8">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Midha Limited">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/img/og-image.jpg">
<meta property="og:locale" content="en_NZ">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" href="/favicon.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://api.fontshare.com" crossorigin>
<link rel="preconnect" href="https://cdn.fontshare.com" crossorigin>
<link rel="stylesheet" href="https://api.fontshare.com/v2/css?f[]=general-sans@600,700&amp;f[]=switzer@400,500,600&amp;display=swap">
<link rel="stylesheet" href="/assets/css/styles.css">
<script src="/assets/js/main.js" defer></script>
<script type="application/ld+json">{json.dumps(ld if len(ld) > 1 else ld[0], ensure_ascii=False)}</script>
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
"""

def nav(active):
    def cur(p): return ' aria-current="page"' if active == p else ""
    services = "".join(
        f'<li><a href="{href}"{cur(href)}>{icon(ic, 18)} {e(name)}</a></li>' for _, href, name, ic in SERVICES)
    areas = "".join(f'<li><a href="/service-areas/#{slug(a[0])}">{e(a[0])}</a></li>' for a in AREAS)
    return f"""<div class="announce" role="region" aria-label="Promotion">Win a free heat pump clean, Wellington only. <a href="/heat-pump-cleaning/#giveaway">How to enter</a></div>
<header class="site-header">
  <div class="wrap header-inner">
    <a class="brand" href="/" aria-label="Midha Limited, home">
      <img src="/assets/img/logo-96.png" width="48" height="48" alt="">
      <span class="brand-name"><strong>Midha Limited</strong><span>Test &amp; tag · Heat pumps · Electrical</span></span>
    </a>
    <nav class="nav" id="site-nav" aria-label="Main">
      <ul>
        <li class="has-sub"><button class="nav-parent" type="button" aria-expanded="false" aria-controls="sub-services">Services {icon("chev", 16)}</button>
          <ul class="submenu" id="sub-services">{services}</ul></li>
        <li class="has-sub"><button class="nav-parent" type="button" aria-expanded="false" aria-controls="sub-areas">Service areas {icon("chev", 16)}</button>
          <ul class="submenu" id="sub-areas">{areas}<li><a href="/service-areas/">All areas</a></li></ul></li>
        <li><a href="/reviews/"{cur("/reviews/")}>Reviews</a></li>
        <li><a href="/about/"{cur("/about/")}>About</a></li>
        <li><a href="/contact/"{cur("/contact/")}>Contact</a></li>
      </ul>
    </nav>
    <div class="header-cta">
      <a class="header-phone" href="tel:{TEL}">{PHONE}</a>
      <a class="btn btn--primary" href="/contact/#quote">Get a quote</a>
      <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="site-nav" aria-label="Open menu">{icon("menu", 22)}</button>
    </div>
  </div>
</header>
"""

def footer():
    services = "".join(f'<li><a href="{h}">{e(n)}</a></li>' for _, h, n, _ in SERVICES)
    areas = "".join(f'<li><a href="/service-areas/#{slug(a[0])}">{e(a[0])}</a></li>' for a in AREAS)
    return f"""<footer class="site-footer on-dark">
  <div class="wrap">
    <div class="footer-grid">
      <div class="footer-brand">
        <a class="brand" href="/"><img src="/assets/img/logo-96.png" width="48" height="48" alt=""><span class="brand-name"><strong>Midha Limited</strong></span></a>
        <p>Test &amp; tag, heat pump cleaning and electrical services for homes and businesses across Greater Wellington. Based in Wainuiomata.</p>
        <p class="footer-small">NZBN {NZBN}<br>100% NZ owned &amp; operated</p>
      </div>
      <div><h2>Services</h2><ul>{services}<li><a href="/heat-pump-cleaning/#healthy-homes">Healthy Homes heating</a></li></ul></div>
      <div><h2>Service areas</h2><ul>{areas}</ul></div>
      <div><h2>Get in touch</h2><ul>
        <li><a href="tel:{TEL}">{PHONE}</a></li>
        <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li>{HOURS}</li>
        <li>Wainuiomata, Wellington</li>
        <li><a href="/contact/#quote">Request a quote</a></li>
      </ul></div>
    </div>
    <div class="footer-bottom">
      <span>© <span id="year">2026</span> Midha Limited. All rights reserved.</span>
      <span><a href="/privacy/">Privacy</a> · <a href="/about/">About</a> · <a href="/reviews/">Reviews</a> · <a href="/contact/">Contact</a></span>
    </div>
  </div>
</footer>
<div class="action-bar" role="region" aria-label="Quick contact">
  <a class="call" href="tel:{TEL}">Call now</a>
  <a class="quote-btn" href="/contact/#quote">Get a quote</a>
</div>
</body>
</html>
"""

def slug(s):
    return "".join(ch.lower() if ch.isalnum() else "-" for ch in s).strip("-").replace("--", "-").replace("--", "-")

def breadcrumbs(items):
    lis = "".join(
        (f'<li><a href="{h}">{e(n)}</a></li>' if h else f'<li aria-current="page">{e(n)}</li>') for n, h in items)
    ld = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, **({"item": SITE + h} if h else {})} for i, (n, h) in enumerate(items)]}
    return f'<nav class="breadcrumbs" aria-label="Breadcrumb"><ol>{lis}</ol></nav>', ld

def page_hero(crumbs, eyebrow, h1, lead, ctas=True, badge=""):
    bc, ld = breadcrumbs(crumbs)
    btns = f"""<div class="btn-row"><a class="btn btn--primary" href="/contact/#quote">Get a free quote</a><a class="btn btn--light" href="tel:{TEL}">Call {PHONE}</a></div>""" if ctas else ""
    return f"""<section class="page-hero"><div class="wrap">{bc}
  <div class="hero-meta">{badge}<span class="eyebrow">{eyebrow}</span></div>
  <h1>{h1}</h1>
  <p class="lead">{lead}</p>{btns}
</div></section>""", ld

def quote_section(heading="Get a fixed-price quote", sub="Tell us what you need and we’ll reply within 2 hours during business hours.", sage=False):
    opts = "".join(f'<option value="{v}">{e(l)}</option>' for l, v in SERVICE_OPTIONS)
    return f"""<section class="section{' section--sage' if sage else ''}" id="quote" aria-labelledby="quote-title">
<div class="wrap quote">
  <div class="quote-info reveal">
    <span class="eyebrow">Free quote · no obligation</span>
    <h2 id="quote-title">{heading}</h2>
    <p class="lead">{sub}</p>
    <ul class="contact-list">
      <li>{icon("phone")}<span><a href="tel:{TEL}">{PHONE}</a><br><span class="note">Call or text</span></span></li>
      <li>{icon("mail")}<span><a href="mailto:{EMAIL}">{EMAIL}</a></span></li>
      <li>{icon("clock")}<span>{HOURS}<br><span class="note">Urgent callouts available</span></span></li>
      <li>{icon("pin")}<span>Based in Wainuiomata, serving Greater Wellington</span></li>
    </ul>
  </div>
  <div class="form-card reveal">
    <form class="quote-form" novalidate>
      <div class="form-grid">
        <div class="field"><label for="name">Your name</label><input id="name" name="name" autocomplete="name"></div>
        <div class="field"><label for="phone">Phone number <span aria-hidden="true">*</span></label><input id="phone" name="phone" type="tel" autocomplete="tel" required aria-describedby="phone-err"><span class="error" id="phone-err">Please enter a phone number so we can reach you.</span></div>
        <div class="field"><label for="email">Email</label><input id="email" name="email" type="email" autocomplete="email" aria-describedby="email-err"><span class="error" id="email-err">That email doesn’t look right.</span></div>
        <div class="field"><label for="suburb">Suburb</label><input id="suburb" name="suburb" autocomplete="address-level2"></div>
        <div class="field full"><label for="service">What do you need? <span aria-hidden="true">*</span></label><select id="service" name="service" required aria-describedby="service-err"><option value="">Choose a service</option>{opts}</select><span class="error" id="service-err">Please choose a service.</span></div>
        <div class="field full"><label for="details">Job details <span class="hint">(optional: number of heat pumps or items, timing)</span></label><textarea id="details" name="details"></textarea></div>
        <div class="hp-field" aria-hidden="true"><label for="_gotcha">Leave this empty</label><input id="_gotcha" name="_gotcha" tabindex="-1" autocomplete="off"></div>
        <div class="full"><button class="btn btn--primary btn--block" type="submit">Send my request</button></div>
      </div>
      <div class="form-status" role="status" aria-live="polite"></div>
      <ul class="seals"><li><span class="tick">✓</span>Fixed price</li><li><span class="tick">✓</span>No obligation</li><li><span class="tick">✓</span>Your details stay private</li></ul>
      <p class="form-note">* Required. We only use your details to reply to you. See our <a href="/privacy/">privacy note</a>.</p>
    </form>
  </div>
</div></section>"""

def faq(items, title="Common questions", sage=False, eyebrow="FAQ"):
    body = "".join(f'<details{" open" if i == 0 else ""}><summary>{e(q)}</summary><div><p>{a}</p></div></details>' for i, (q, a) in enumerate(items))
    ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": html.unescape(a.replace("<a ", "<a ")).replace("&amp;", "&")}} for q, a in items]}
    return f"""<section class="section{' section--sage' if sage else ''}" aria-labelledby="faq-title"><div class="wrap">
<div class="section-head"><span class="eyebrow">{eyebrow}</span><h2 id="faq-title">{title}</h2></div>
<div class="faq">{body}</div></div></section>""", ld

def review_card(r):
    name, who, svc, date, text = r
    return f"""<article class="card review reveal">
  <div class="stars" role="img" aria-label="5 out of 5 stars">★★★★★</div>
  <blockquote><p>“{e(text)}”</p></blockquote>
  <div class="meta"><p class="who"><strong>{e(name)}</strong><br>{e(who)}</p><span class="badge badge--soft">{e(svc)}</span></div>
  <p class="note">{e(date)}</p>
</article>"""

def write(path, content):
    full = os.path.join(OUT, path.strip("/"), "index.html") if not path.endswith(".html") else os.path.join(OUT, path.strip("/"))
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)

TAG_SVG = """<svg viewBox="0 0 220 300" role="img" aria-label="Illustration of a test tag reading Tested, Passed">
<rect x="20" y="20" width="180" height="260" rx="24" fill="#FDFCF8" stroke="#1C1C1C" stroke-width="4"/>
<circle cx="110" cy="58" r="14" fill="#E2E8E4" stroke="#1C1C1C" stroke-width="4"/>
<text x="110" y="118" text-anchor="middle" font-family="General Sans, sans-serif" font-weight="700" font-size="26" fill="#1C1C1C">TESTED</text>
<text x="110" y="150" text-anchor="middle" font-family="Switzer, sans-serif" font-weight="600" font-size="16" fill="#6E6354">AS/NZS 3760</text>
<line x1="44" y1="176" x2="176" y2="176" stroke="#978B7A" stroke-width="3" stroke-dasharray="8 6"/>
<rect x="44" y="194" width="58" height="58" rx="6" fill="none" stroke="#1C1C1C" stroke-width="4"/>
<rect x="56" y="206" width="14" height="14" fill="#1C1C1C"/><rect x="76" y="226" width="14" height="14" fill="#1C1C1C"/><rect x="56" y="230" width="10" height="10" fill="#1C1C1C"/>
<text x="118" y="214" font-family="Switzer, sans-serif" font-weight="600" font-size="14" fill="#1C1C1C">PASSED</text>
<text x="118" y="238" font-family="Switzer, sans-serif" font-size="13" fill="#4A4A45">Retest due</text>
</svg>"""

BULB_SVG = """<svg viewBox="0 0 220 220" role="img" aria-label="Illustration of a ceiling downlight">
<rect x="20" y="30" width="180" height="16" rx="8" fill="#1C1C1C"/>
<path d="M70 46h80l-10 34H80Z" fill="#FDFCF8" stroke="#1C1C1C" stroke-width="4"/>
<path d="M60 92 30 190M110 92v100M160 92l30 98" stroke="#978B7A" stroke-width="4" stroke-linecap="round" stroke-dasharray="2 12"/>
<ellipse cx="110" cy="84" rx="30" ry="6" fill="#D4AF37"/>
</svg>"""

# ---------------------------------------------------------------- pages
pages = []

def home():
    hero_img = pic("indoor-coil-clean", "Midha technician washing the coil of an indoor heat pump in a Wellington home", big=True, eager=True, sizes="100vw")
    chooser = f"""
<div class="wrap"><div class="chooser">
  <a class="card card--lift" href="/test-and-tag/">
    <div class="icon-chip">{icon("tag", 26)}</div><span class="num">For workplaces</span>
    <h2 class="h3" style="font-size:var(--fs-h3)">Test &amp; Tag</h2>
    <p>AS/NZS 3760 testing for tools, appliances, leads and RCDs, with QR tags and a digital register.</p>
    <span class="more">Test &amp; tag details →</span></a>
  <a class="card card--lift card--ink on-dark" href="/heat-pump-cleaning/">
    <div class="icon-chip">{icon("fan", 26, "#FFFFFF")}</div><span class="num" style="color:#C9BFAE">For homes &amp; rentals</span>
    <h2 style="font-size:var(--fs-h3)">Heat Pump Cleaning</h2>
    <p>Deep cleans from <strong style="color:#fff">$79 per unit</strong>, GST incl. Mould gone, airflow back, lower power bills.</p>
    <span class="more" style="color:#C9BFAE">See packages &amp; prices →</span></a>
  <a class="card card--lift" href="/electrical-services/">
    <div class="icon-chip">{icon("bulb", 26)}</div><span class="num">For homes &amp; businesses</span>
    <h2 style="font-size:var(--fs-h3)">Electrical Services</h2>
    <p>Light installations, LED downlights, security and sensor lights, power points, cord and lead repairs.</p>
    <span class="more">Electrical details →</span></a>
</div></div>"""
    stats = """
<div class="wrap"><div class="stats" aria-label="Midha in numbers">
  <div class="stat"><strong>14,500+</strong><span>items tested &amp; tagged for businesses</span></div>
  <div class="stat"><strong>200+</strong><span>home heat pumps serviced</span></div>
  <div class="stat"><strong>&lt; 2 hrs</strong><span>average quote reply</span></div>
  <div class="stat"><strong>5.0 <span class="star" aria-hidden="true">★</span></strong><span>Google rating</span></div>
</div></div>"""
    packages = packages_section(compact=True)
    why = f"""
<section class="section section--ink on-dark" aria-labelledby="why-title"><div class="wrap">
  <div class="section-head"><span class="eyebrow">Why Midha</span><h2 id="why-title">Local, upfront and properly done.</h2>
  <p style="color:#D9D6CE">We take the hassle out of compliance and heat pump care, whether you run a busy workshop or a family home.</p></div>
  <div class="feature-list">
    <div class="feature reveal"><div class="icon-chip">{icon("dollar", 24, "#FFFFFF")}</div><div><h3>Fixed, upfront pricing</h3><p>The price on your quote is the price you pay. No surprise travel or admin fees.</p></div></div>
    <div class="feature reveal"><div class="icon-chip">{icon("qr", 24, "#FFFFFF")}</div><div><h3>Digital QR reports</h3><p>Every tagged item gets a QR code, and your register arrives as a PDF with reminders before retests are due.</p></div></div>
    <div class="feature reveal"><div class="icon-chip">{icon("leaf", 24, "#FFFFFF")}</div><div><h3>A real deep clean</h3><p>Not just a filter wipe. We wash the coils and fan to clear mould and bacteria from the air you breathe.</p></div></div>
    <div class="feature reveal"><div class="icon-chip">{icon("pin", 24, "#FFFFFF")}</div><div><h3>Based in Wainuiomata</h3><p>Prompt callouts across the Hutt Valley, northern suburbs and Porirua. No callout surcharge in Wainui.</p></div></div>
  </div>
  <div class="btn-row" style="margin-top:36px"><a class="btn btn--gold" href="/about/">About Midha</a></div>
</div></section>"""
    reviews = "".join(review_card(r) for r in REVIEWS[:3])
    rev = f"""
<section class="section" aria-labelledby="rev-title"><div class="wrap">
  <div class="section-head"><span class="eyebrow">5.0 on Google</span><h2 id="rev-title">Trusted by homes and workplaces across Wellington.</h2></div>
  <div class="grid grid-3">{reviews}</div>
  <div class="btn-row" style="margin-top:28px"><a class="btn btn--outline" href="/reviews/">Read all reviews</a></div>
</div></section>"""
    areas = "".join(f'<li><a href="/service-areas/#{slug(a[0])}">{e(a[0])}</a> · {e(a[1])}</li>' for a in AREAS)
    area_sec = f"""
<section class="section section--sage" aria-labelledby="areas-title"><div class="wrap split">
  <div class="stack reveal"><span class="eyebrow">Service areas</span><h2 id="areas-title">Proudly serving Greater Wellington.</h2>
  <p class="lead">From our base in Wainuiomata we cover the Hutt Valley, Wellington’s northern suburbs and Porirua, with no hidden travel charges.</p>
  <a class="btn btn--primary" href="/service-areas/" style="align-self:flex-start">See all areas</a></div>
  <ul class="chips reveal" style="flex-direction:column;align-items:flex-start;gap:10px">{areas}</ul>
</div></section>"""
    fq, fld = faq([
        ("How much does a heat pump clean cost?", 'Our Pro Clean is $79, Elite Clean $129 and Comprehensive Clean $189. Prices are per heat pump and include GST. <a href="/heat-pump-cleaning/">Compare packages</a>.'),
        ("Do you only do test &amp; tag for businesses?".replace("&amp;", "&"), "Test &amp; tag is mainly for workplaces, construction sites, schools, cafés and offices, but we’re happy to test gear for anyone who needs it."),
        ("How quickly can you come out?", "We aim to reply to every quote request within 2 hours during business hours. Wainuiomata jobs can often be booked same day or next day; see our service areas for other suburbs."),
        ("Which areas do you cover?", 'Wainuiomata, Lower Hutt, Upper Hutt, Tawa, Newlands, Porirua and the wider Greater Wellington region. <a href="/service-areas/">See service areas</a>.'),
    ], title="Got questions?")
    ld = [fld]
    body = f"""<main id="main">
<section class="hero"><div class="wrap"><div class="hero-frame">
  {hero_img}
  <div class="hero-panel glass reveal">
    <div class="hero-meta"><span class="badge badge--urgent">Win a free heat pump clean</span><span>Wainuiomata-based · 100% NZ owned</span></div>
    <h1>Test &amp; tag, heat pump cleaning and electrical work, sorted.</h1>
    <p class="lead">One local team for Greater Wellington homes and workplaces. Fixed upfront prices, digital reports, and a reply within 2 hours.</p>
    <div class="btn-row"><a class="btn btn--primary" href="/contact/#quote">Get a free quote</a><a class="btn btn--light" href="tel:{TEL}">Call {PHONE}</a></div>
  </div>
</div></div></section>
<h2 class="visually-hidden">Our three services</h2>
{chooser}
{stats}
{packages}
{why}
{rev}
{area_sec}
{fq}
{quote_section()}
</main>"""
    write("/", head("Test & Tag, Heat Pump Cleaning & Electrical | Midha Limited Wellington",
                    "Wainuiomata-based test & tag, heat pump cleaning from $79 and electrical services across Lower Hutt, Upper Hutt, Tawa, Newlands and Porirua. Fixed prices.",
                    "/", ld) + nav("/") + body + footer())

def packages_section(compact=False):
    pro_in = """<h4>Indoor unit cleaning</h4><ul><li>Vacuum clean and disinfect filters, housing and cover</li><li>Coil clean treatment and disinfection of evaporator coils</li><li>Clean condensate tray, fan and thermostat</li><li>Advice on any mould found</li></ul>
<h4>Indoor unit checks</h4><ul><li>Inspect evaporator coil for leaks and tighten electrical connections</li><li>Operational and temperature checks</li><li>Assess filters and unit for damage</li><li>Check fan speed and remote settings</li><li>Noise and vibration checks</li></ul>
<h4>Outdoor unit cleaning</h4><ul><li>Coil clean treatment and pressure wash of condenser coils</li><li>Clean condenser housing and fan</li><li>Remove debris and blockages</li></ul>
<h4>Outdoor unit checks</h4><ul><li>Inspect for damage, oil leaks and rodents</li><li>Check drain is flowing and connections are secure</li><li>Condenser safety and mounting stability</li><li>Inspect pipe insulation and check for corrosion</li><li>Noise and vibration assessment</li></ul>"""
    elite_in = """<ul><li>Everything in Pro Clean</li><li>Full pressure wash of the indoor unit to remove all contaminants</li><li>Full pressure wash of the outdoor unit</li><li>Completed maintenance check sheet for your records</li></ul>"""
    comp_in = """<ul><li>Everything in Elite Clean</li><li>Remove and clean the evaporator housing and cover</li><li>Pressure wash the blower fan and air well</li><li>Anti-mould treatment on filters, evaporator coils and condensate tray</li><li>Clean and sanitise all housing and cover parts</li><li>3-month mould-free guarantee: if mould comes back, we re-clean free</li></ul>"""
    det = lambda inner: "" if compact else f'<details class="inclusions"><summary>Everything included</summary>{inner}</details>'
    return f"""
<section class="section section--sage" id="packages" aria-labelledby="pk-title"><div class="wrap">
  <div class="section-head"><span class="eyebrow">Heat pump cleaning · prices per unit, GST incl.</span><h2 id="pk-title">Pick the clean your heat pump needs.</h2>
  <p>Every package includes a full set of indoor and outdoor safety checks. Got two heat pumps? Simply multiply by two.</p></div>
  <div class="grid grid-3 price-grid">
    <article class="card card--lift price-card reveal">
      <div class="head"><h3>Pro Clean</h3></div>
      <div class="price">$79 <small>per unit</small></div>
      <ul class="check-list"><li>Indoor unit vacuum clean and disinfect</li><li>Outdoor unit pressure wash</li><li>Full indoor and outdoor checks</li></ul>
      {det(pro_in)}
      <a class="btn btn--outline" href="/contact/?service=pro#quote" data-service="pro">Book Pro Clean</a>
    </article>
    <article class="card card--lift card--ink price-card on-dark reveal">
      <div class="head"><h3>Elite Clean</h3><span class="badge badge--gold">Most popular</span></div>
      <div class="price">$129 <small>per unit</small></div>
      <ul class="check-list"><li>Everything in Pro Clean</li><li>Indoor <em>and</em> outdoor units pressure washed</li><li>Completed maintenance check sheet</li></ul>
      {det(elite_in)}
      <a class="btn btn--gold" href="/contact/?service=elite#quote" data-service="elite">Book Elite Clean</a>
    </article>
    <article class="card card--lift price-card reveal">
      <div class="head"><h3>Comprehensive Clean</h3></div>
      <div class="price">$189 <small>per unit</small></div>
      <ul class="check-list"><li>Everything in Elite Clean</li><li>Housing, cover and blower fan deep clean</li><li>Anti-mould treatment with a 3-month mould-free guarantee</li></ul>
      {det(comp_in)}
      <a class="btn btn--outline" href="/contact/?service=comprehensive#quote" data-service="comprehensive">Book Comprehensive</a>
    </article>
  </div>
  {'<div class="btn-row" style="margin-top:28px"><a class="btn btn--primary" href="/heat-pump-cleaning/">See full heat pump details</a></div>' if compact else ''}
</div></section>"""

def heat_pump():
    hero, bld = page_hero([("Home", "/"), ("Heat Pump Cleaning", None)],
        "Heat pump cleaning · Greater Wellington", "Heat pump cleaning that clears the mould and cuts the power bill.",
        "Pro, Elite and Comprehensive cleans from $79 per unit, GST included. Plus filter replacement, emergency repairs, pipe insulation repair and Healthy Homes heating checks.")
    extras = f"""
<section class="section" aria-labelledby="extra-title"><div class="wrap">
  <div class="section-head"><span class="eyebrow">Also available · quote on request</span><h2 id="extra-title">Repairs, filters and compliance.</h2></div>
  <div class="grid grid-2">
    <article class="card reveal" id="filter-replacement"><div class="icon-chip">{icon("fan")}</div><h3>Filter replacement</h3><p>Worn or damaged filters let dust straight through. We replace them so your heat pump keeps delivering clean, healthy air.</p></article>
    <article class="card reveal" id="emergency-repairs"><div class="icon-chip">{icon("wrench")}</div><h3>Emergency repairs</h3><p>Heat pump stopped working, blowing cold or making strange noises? Call us for a prompt visit to diagnose the problem and get it running again.</p></article>
    <article class="card card--media reveal" id="pipe-insulation">
      <div class="before-after" style="padding:16px 16px 0">
        <figure>{pic("pipe-insulation-before", "Split and weathered heat pump pipe insulation before repair", sizes="(max-width: 680px) 45vw, 22vw")}<figcaption><span class="badge badge--soft">Before</span></figcaption></figure>
        <figure>{pic("pipe-insulation-after", "New black pipe insulation fitted to the same heat pump after repair", sizes="(max-width: 680px) 45vw, 22vw")}<figcaption><span class="badge badge--gold">After</span></figcaption></figure>
      </div>
      <div class="card-body"><h3>Pipe insulation repair</h3><p>Sun and weather break down the lagging on your outdoor pipes, which wastes energy. We strip the damaged insulation and fit new, UV-resistant lagging.</p></div>
    </article>
    <article class="card reveal" id="healthy-homes"><div class="icon-chip">{icon("home")}</div><h3>Healthy Homes heating compliance</h3>
      <p>For landlords and property managers. We check your heat pump meets the Healthy Homes heating requirement for the main living room and give you a clear report for your records.</p>
      <ul class="check-list"><li>Heating capacity assessment for the main living room</li><li>Check existing heat pumps are working well with clean airflow</li><li>Digital report for your tenancy records</li><li>Annual maintenance plans for property managers</li></ul>
      <a class="more" href="/contact/?service=healthy-homes#quote" data-service="healthy-homes">Ask about Healthy Homes →</a></article>
  </div>
</div></section>"""
    process = f"""
<section class="section" aria-labelledby="how-title"><div class="wrap split">
  <div class="split-media tall reveal">{pic("cleaning-bag-setup", "Heat pump with a waterproof cleaning bag fitted underneath and a step ladder ready")}</div>
  <div class="stack reveal"><span class="eyebrow">How we work</span><h2 id="how-title">Clean, careful and mess-free.</h2>
    <p class="lead">We fit a waterproof cleaning bag under the indoor unit, lay drop sheets, and wash the dirt straight into the bag. You get clean air without the mess.</p>
    <ul class="check-list"><li>Indoor unit opened and protected before we start</li><li>Coils and fan washed with a non-corrosive cleaner</li><li>Outdoor unit cleared of leaves and pressure washed</li><li>Everything tested before we leave</li></ul>
    <div class="split-media" style="margin-top:12px">{pic("outdoor-unit-wash", "Outdoor heat pump unit being gently pressure washed")}</div>
  </div>
</div></section>"""
    give = f"""
<section class="section section--sage" id="giveaway" aria-labelledby="give-title"><div class="wrap giveaway">
  {pic("giveaway-promo", "Midha giveaway poster: win one free heat pump cleaning in Wellington", sizes="320px")}
  <div class="stack"><span class="badge badge--urgent" style="align-self:flex-start">Giveaway now on</span>
    <h2 id="give-title">Win a free heat pump clean.</h2>
    <p class="lead">One lucky Wellington winner will be chosen at random. To enter, find our giveaway post on social media and:</p>
    <ul class="check-list"><li>Like the post</li><li>Tag 3 friends in Wellington</li><li>Live in the Wellington region</li></ul>
  </div>
</div></section>"""
    fq, fld = faq([
        ("Are your prices per heat pump?", "Yes. All package prices are per heat pump and include GST. For two heat pumps on the Elite Clean, the total is $258."),
        ("Which package should I choose?", "If your heat pump has been cleaned in the last year, Pro Clean is usually enough. Elite Clean is our most popular choice for a yearly service. Choose Comprehensive if you can smell mould or see black spots on the fan."),
        ("Why does my heat pump smell musty?", "Mould and bacteria grow on the damp coils and fan inside the indoor unit. A filter wipe won’t reach them. Our Elite and Comprehensive cleans wash them out, and Comprehensive adds an anti-mould treatment with a 3-month guarantee."),
        ("Why is my heat pump blowing cold air or using more power?", "Blocked filters, dirty coils and leaves in the outdoor unit make your heat pump work harder. A clean usually restores airflow and efficiency. If it still isn’t right, we’ll check for faults."),
        ("What does the 3-month mould-free guarantee cover?", "If mould comes back within 3 months of a Comprehensive Clean, we’ll come back and re-clean the unit for free."),
        ("How long does a clean take?", "Allow 1 to 2 hours per heat pump depending on the package and access. We’ll give you a time window when you book."),
    ], title="Heat pump questions")
    svc_ld = {"@context": "https://schema.org", "@type": "Service", "serviceType": "Heat pump cleaning", "provider": {"@id": SITE + "/#business"},
              "areaServed": "Greater Wellington", "offers": [
                  {"@type": "Offer", "name": n, "price": p, "priceCurrency": "NZD"} for n, p in (("Pro Clean", "79"), ("Elite Clean", "129"), ("Comprehensive Clean", "189"))]}
    body = f"""<main id="main">{hero}{packages_section()}{extras}{process}{give}{fq}{quote_section("Book your heat pump clean", "Choose a package below, or tell us what’s wrong and we’ll recommend one.")}</main>"""
    write("/heat-pump-cleaning/", head("Heat Pump Cleaning Wellington from $79 | Midha Limited",
        "Heat pump deep cleaning in Wainuiomata, Lower Hutt, Upper Hutt, Tawa and Porirua. Pro $79, Elite $129, Comprehensive $189 per unit, GST incl.",
        "/heat-pump-cleaning/", [bld, fld, svc_ld]) + nav("/heat-pump-cleaning/") + body + footer())

def test_tag():
    hero, bld = page_hero([("Home", "/"), ("Test & Tag", None)], "Workplace electrical safety",
        "Test &amp; tag for Wellington workplaces.",
        "Electrical testing and tagging to AS/NZS 3760:2010, with QR-coded tags, RCD testing and a digital register you can show any auditor.",
        badge='<span class="badge badge--gold">AS/NZS 3760:2010</span>')
    body_sec = f"""
<section class="section" aria-labelledby="tt-what"><div class="wrap split">
  <div class="stack reveal"><span class="eyebrow">What’s included</span><h2 id="tt-what">Everything you need for compliance.</h2>
    <p class="lead">Under the Health and Safety at Work Act, businesses must manage electrical risks. Regular testing and tagging to AS/NZS 3760:2010 is the accepted way to show you’re doing that.</p>
    <ul class="check-list">
      <li>Inspection and testing to AS/NZS 3760:2010</li>
      <li>Single-phase and three-phase equipment, power tools, leads and appliances</li>
      <li>RCD (safety switch) trip-time and push-button testing with logs</li>
      <li>A QR-coded tag on every item for instant digital lookup</li>
      <li>Digital PDF register, usually within 24 hours</li>
      <li>Reminders before your retests are due</li>
    </ul>
    <div class="btn-row" style="margin-top:8px"><a class="btn btn--primary" href="/contact/?service=test-tag#quote" data-service="test-tag">Get a test &amp; tag quote</a></div>
  </div>
  <div class="tag-illus reveal">{TAG_SVG}</div>
</div></section>
<section class="section section--sage" aria-labelledby="tt-who"><div class="wrap">
  <div class="section-head"><span class="eyebrow">Who we test for</span><h2 id="tt-who">From cafés to construction sites.</h2></div>
  <ul class="chips"><li>Workshops &amp; factories</li><li>Construction sites</li><li>Offices</li><li>Cafés &amp; restaurants</li><li>Schools &amp; early learning</li><li>Retail stores</li><li>Rental properties</li><li>Community halls</li></ul>
  <div class="grid grid-3" style="margin-top:32px">
    <div class="card reveal"><div class="icon-chip" style="background:var(--c-bg)">{icon("qr")}</div><h3>Smart QR tags</h3><p>Scan any tag to see its test history. No more hunting through paper logbooks.</p></div>
    <div class="card reveal"><div class="icon-chip" style="background:var(--c-bg)">{icon("clock")}</div><h3>Around your hours</h3><p>Early starts before the tools come out, or quiet times so your customers aren’t disturbed.</p></div>
    <div class="card reveal"><div class="icon-chip" style="background:var(--c-bg)">{icon("shield")}</div><h3>Faulty gear flagged</h3><p>Anything that fails is clearly tagged out of service, and we can repair or replace cords and leads on the spot.</p></div>
  </div>
</div></section>"""
    revs = "".join(review_card(r) for r in REVIEWS if r[2] == "Test & Tag")
    rev = f"""<section class="section" aria-labelledby="tt-rev"><div class="wrap"><div class="section-head"><span class="eyebrow">What clients say</span><h2 id="tt-rev">Trusted by local businesses.</h2></div><div class="grid grid-3">{revs}</div></div></section>"""
    fq, fld = faq([
        ("How often does equipment need testing?", "It depends on the environment. Construction and hire equipment is usually tested every 3 months, factories and workshops every 6 months, and offices and other low-risk places every 12 months or longer. We’ll recommend the right interval for your site."),
        ("How much does test &amp; tag cost?".replace("&amp;", "&"), "It depends on how many items you have and where they are. Tell us roughly how many items and we’ll send a fixed-price quote, usually within 2 hours."),
        ("Do you provide certificates for audits?", "Yes. You’ll receive a full digital PDF register of every item tested, usually within 24 hours of the job."),
        ("How does the QR tagging work?", "Each item gets a tag with a unique QR code. Scan it with a phone to see when it was tested, the result and when the next test is due."),
        ("Do you test RCDs (safety switches)?", "Yes. We test portable and fixed RCDs for trip time and push-button operation, and record the results in your register."),
    ], title="Test & tag questions")
    svc_ld = {"@context": "https://schema.org", "@type": "Service", "serviceType": "Electrical test and tag (AS/NZS 3760:2010)", "provider": {"@id": SITE + "/#business"}, "areaServed": "Greater Wellington"}
    body = f"""<main id="main">{hero}{body_sec}{rev}{fq}{quote_section("Get a test & tag quote", "Let us know roughly how many items and where they are, and we’ll come back with a fixed price.")}</main>"""
    write("/test-and-tag/", head("Test and Tag Wellington | AS/NZS 3760 | Midha Limited",
        "AS/NZS 3760:2010 electrical test and tag for Wellington workplaces. QR tags, RCD testing and a digital register. Based in Wainuiomata.",
        "/test-and-tag/", [bld, fld, svc_ld]) + nav("/test-and-tag/") + body + footer())

def electrical():
    hero, bld = page_hero([("Home", "/"), ("Electrical Services", None)], "Electrical services",
        "Lighting, power points and repairs, done tidily.",
        "Light installations, LED downlights, security and sensor lights, new power points, and cord and lead repairs for homes and businesses across Greater Wellington.")
    items = [
        ("bulb", "Light installations", "New light fittings, pendants and replacements for tired or broken lights, inside and out."),
        ("bolt", "LED downlights", "Swap old halogens for energy-efficient LED downlights that run cooler and cost less to run."),
        ("shield", "Security & sensor lights", "Motion-sensor and security lighting for driveways, entrances and yards."),
        ("plug", "Power points", "Extra or relocated power points, including double and USB outlets."),
        ("wrench", "Cord & lead repairs", "Damaged extension leads and appliance cords repaired or replaced, often on the spot."),
    ]
    cards = "".join(f'<article class="card card--lift reveal"><div class="icon-chip">{icon(i)}</div><h3>{e(t)}</h3><p>{e(d)}</p></article>' for i, t, d in items)
    cards += f'<article class="card card--ink on-dark reveal"><h3>Not sure what you need?</h3><p>Describe the job and we’ll let you know how we can help.</p><a class="btn btn--gold" style="margin-top:auto;align-self:flex-start" href="/contact/?service=electrical#quote" data-service="electrical">Ask us</a></article>'
    sec = f"""
<section class="section section--sage" aria-labelledby="el-title"><div class="wrap">
  <div class="section-head"><span class="eyebrow">What we do</span><h2 id="el-title">Electrical jobs we take on.</h2></div>
  <div class="grid grid-3">{cards}</div>
</div></section>
<section class="section" aria-labelledby="el-why"><div class="wrap split">
  <div class="stack reveal"><span class="eyebrow">How we work</span><h2 id="el-why">Clear quotes, clean work.</h2>
    <p class="lead">We quote a fixed price before we start, turn up when we say we will, and leave your place as tidy as we found it.</p>
    <ul class="check-list"><li>Fixed, upfront quotes</li><li>Drop sheets and clean boots</li><li>Old fittings taken away</li><li>Everything tested before we leave</li></ul>
  </div>
  <div class="tag-illus reveal">{BULB_SVG}</div>
</div></section>"""
    fq, fld = faq([
        ("Do you do small jobs?", "Yes. Swapping a light fitting or adding a power point is exactly the kind of job we’re happy to take on."),
        ("Can you switch my old downlights to LED?", "Yes. LED downlights use far less power and run cooler than halogens. We’ll quote for the number of lights you want changed."),
        ("How do I get a price?", 'Fill in the quote form or call <a href="tel:' + TEL + '">' + PHONE + '</a> with a quick description and a photo if you can. We’ll come back with a fixed price.'),
    ], title="Electrical questions")
    body = f"""<main id="main">{hero}{sec}{fq}{quote_section("Get an electrical quote", "Tell us what you’d like done, and add a photo by email if it helps.")}</main>"""
    write("/electrical-services/", head("Electrical Services Wellington | Lighting & Power Points | Midha",
        "Light installations, LED downlights, security and sensor lights, power points and cord repairs across Lower Hutt, Upper Hutt and Wellington.",
        "/electrical-services/", [bld, fld]) + nav("/electrical-services/") + body + footer())

def areas_page():
    hero, bld = page_hero([("Home", "/"), ("Service Areas", None)], "Where we work", "Proudly serving Greater Wellington.",
        "Based in Wainuiomata and covering the Hutt Valley, Wellington’s northern suburbs and Porirua, with no hidden travel charges.")
    cards = "".join(f"""<article class="card area-card reveal" id="{slug(n)}"><h2 style="font-size:var(--fs-h3)">{e(n)}</h2><span class="badge badge--soft">{e(sp)}</span><p>{e(d)}</p><ul>{''.join(f'<li>{e(s)}</li>' for s in subs)}</ul>
<a class="more" href="/contact/#quote">Book in {e(n.split(' &')[0])} →</a></article>""" for n, sp, d, subs in AREAS)
    sec = f"""<section class="section section--sage"><div class="wrap"><div class="grid grid-3">{cards}</div>
<p class="note" style="margin-top:24px">Typical booking times shown. Urgent callouts are available. Just call {PHONE}.</p></div></section>"""
    body = f"""<main id="main">{hero}{sec}{quote_section()}</main>"""
    write("/service-areas/", head("Service Areas | Wainuiomata, Hutt Valley, Tawa, Porirua | Midha Limited",
        "Midha Limited covers Wainuiomata, Lower Hutt, Upper Hutt, Tawa, Newlands, Porirua and Greater Wellington for test & tag, heat pump and electrical work.",
        "/service-areas/", [bld]) + nav("/service-areas/") + body + footer())

def reviews_page():
    hero, bld = page_hero([("Home", "/"), ("Reviews", None)], "5.0 Google rating", "What our customers say.",
        "Feedback from property managers, workshop supervisors and homeowners across Greater Wellington.")
    cards = "".join(review_card(r) for r in REVIEWS)
    sec = f"""<section class="section section--sage"><div class="wrap"><div class="grid grid-3">{cards}</div></div></section>"""
    body = f"""<main id="main">{hero}{sec}{quote_section("Experience it for yourself")}</main>"""
    write("/reviews/", head("Customer Reviews | Midha Limited Wellington",
        "Read reviews from Wellington homeowners, landlords and businesses who use Midha Limited for test & tag, heat pump cleaning and electrical work.",
        "/reviews/", [bld]) + nav("/reviews/") + body + footer())

def about_page():
    hero, bld = page_hero([("Home", "/"), ("About", None)], "100% Kiwi owned &amp; operated", "About Midha Limited",
        "Keeping your whānau, team and property safe and comfortable, with straightforward local service.", ctas=False)
    sec = f"""
<section class="section"><div class="wrap split">
  <div class="stack reveal"><span class="eyebrow">Our story</span><h2>Safety, reliability and clean air.</h2>
    <p class="lead">Midha Limited started with a simple idea: every Kiwi workplace and home deserves reliable safety compliance and heating care, without red tape or hidden fees.</p>
    <p>Based in Wainuiomata and working right across Lower Hutt, Upper Hutt, Tawa, Newlands and Porirua, we combine careful technical work with friendly, approachable service.</p>
    <p class="note">Midha Limited is a registered New Zealand company. NZBN {NZBN}.</p>
  </div>
  <div class="split-media reveal">{pic("indoor-coil-clean", "Midha technician cleaning an indoor heat pump coil")}</div>
</div></section>
<section class="section section--sage"><div class="wrap">
  <div class="section-head"><span class="eyebrow">What we stand for</span><h2>Our commitments.</h2></div>
  <div class="grid grid-3">
    <div class="card reveal"><div class="icon-chip" style="background:var(--c-bg)">{icon("shield")}</div><h3>Safety without shortcuts</h3><p>Electrical faults cost lives and livelihoods. We follow the standards fully, every time.</p></div>
    <div class="card reveal"><div class="icon-chip" style="background:var(--c-bg)">{icon("dollar")}</div><h3>Honest fixed pricing</h3><p>What we quote is what you pay. No surprise travel, admin or disposal fees.</p></div>
    <div class="card reveal"><div class="icon-chip" style="background:var(--c-bg)">{icon("home")}</div><h3>Respect for your place</h3><p>Clean boots, drop sheets and genuine care in every home and workplace.</p></div>
  </div>
</div></section>"""
    body = f"""<main id="main">{hero}{sec}{quote_section()}</main>"""
    write("/about/", head("About Midha Limited | Wainuiomata, Wellington",
        "Midha Limited is a 100% Kiwi-owned business in Wainuiomata providing test & tag, heat pump cleaning and electrical services across Greater Wellington.",
        "/about/", [bld]) + nav("/about/") + body + footer())

def contact_page():
    hero, bld = page_hero([("Home", "/"), ("Contact", None)], "Reply within 2 hours", "Contact Midha Limited",
        f"Call or text {PHONE}, email {EMAIL}, or send the form below. We’re available {HOURS}, with urgent callouts available.", ctas=False)
    zone = f"""<section class="section section--sage"><div class="wrap split">
  <div class="stack"><span class="eyebrow">Our base</span><h2>Our Greater Wellington service zone.</h2>
  <p class="lead">Based in Wainuiomata, covering Petone, Gracefield, Epuni, Waterloo, Silverstream, Trentham, Tawa, Newlands, Johnsonville and Porirua.</p></div>
  <ul class="chips"><li>No travel surcharge in Wainuiomata</li><li>Same day / next day in Wainui</li><li>After-hours slots for businesses</li><li>Urgent callouts available</li></ul>
</div></section>"""
    body = f"""<main id="main">{hero}{quote_section("Book a service or request a quote", "Annual test & tag, a heat pump clean or an electrical job? Tell us what you need.")}{zone}</main>"""
    write("/contact/", head("Contact Midha Limited | Book Test & Tag, Heat Pump or Electrical",
        f"Get a free, fixed-price quote. Call {PHONE} or email {EMAIL}. Serving Wainuiomata, the Hutt Valley, Tawa, Newlands and Porirua.",
        "/contact/", [bld]) + nav("/contact/") + body + footer())

def simple(path, title, desc, h1, inner, robots=None):
    hd = head(title, desc, path)
    if robots: hd = hd.replace("<link rel=\"canonical\"", f'<meta name="robots" content="{robots}">\n<link rel="canonical"')
    write(path, hd + nav(path) + f'<main id="main"><section class="page-hero"><div class="wrap"><h1>{h1}</h1></div></section><section class="section" style="padding-top:0"><div class="wrap prose">{inner}</div></section></main>' + footer())

def misc():
    simple("/thanks/", "Thanks | Midha Limited", "Thanks for your enquiry.", "Thanks, we’ve got your request.",
           f'<p class="lead">We’ll be in touch within 2 hours during business hours ({HOURS}). If it’s urgent, call <a href="tel:{TEL}">{PHONE}</a>.</p><p><a class="btn btn--primary" href="/">Back to home</a></p>', robots="noindex")
    simple("/privacy/", "Privacy | Midha Limited", "How Midha Limited handles your personal information.", "Privacy note",
           f"""<p>We collect the details you give us in our quote form, by phone or by email (such as your name, phone number, email, suburb and job details) so we can reply to you, quote and carry out your job.</p>
<p>We don’t sell or share your details with anyone else, except service providers that help us run the business (such as our email and form provider), and only as needed.</p>
<p>Under the Privacy Act 2020, you can ask to see or correct the information we hold about you. Email <a href="mailto:{EMAIL}">{EMAIL}</a> or call {PHONE}.</p>
<h2>Website analytics</h2><p>If we use privacy-friendly website analytics (such as Cloudflare Web Analytics), it counts visits without cookies and doesn’t identify you.</p>""")
    simple("/404.html", "Page not found | Midha Limited", "Page not found.", "Sorry, we can’t find that page.",
           f'<p class="lead">Try one of these instead:</p><ul class="chips"><li><a href="/heat-pump-cleaning/">Heat pump cleaning</a></li><li><a href="/test-and-tag/">Test &amp; tag</a></li><li><a href="/electrical-services/">Electrical services</a></li><li><a href="/contact/">Contact</a></li></ul>', robots="noindex")

def cloudflare_files():
    with open(os.path.join(OUT, "_headers"), "w") as f:
        f.write("""/*
  X-Content-Type-Options: nosniff
  X-Frame-Options: DENY
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: camera=(), microphone=(), geolocation=()
  Strict-Transport-Security: max-age=31536000; includeSubDomains

/assets/*
  Cache-Control: public, max-age=31536000, immutable

/assets/css/*
  Cache-Control: public, max-age=86400

/assets/js/*
  Cache-Control: public, max-age=86400
""")
    with open(os.path.join(OUT, "_redirects"), "w") as f:
        f.write("""# Old page addresses -> new pages (301 = permanent)
/services            /heat-pump-cleaning/   301
/services/           /heat-pump-cleaning/   301
/heat-pump           /heat-pump-cleaning/   301
/heat-pumps          /heat-pump-cleaning/   301
/test-tag            /test-and-tag/         301
/electrical          /electrical-services/  301
/about-us            /about/                301
/contact-us          /contact/              301
/book                /contact/#quote        302
""")
    with open(os.path.join(OUT, "robots.txt"), "w") as f:
        f.write(f"User-agent: *\nAllow: /\nDisallow: /thanks/\n\nSitemap: {SITE}/sitemap.xml\n")
    urls = ["/", "/heat-pump-cleaning/", "/test-and-tag/", "/electrical-services/", "/service-areas/", "/reviews/", "/about/", "/contact/", "/privacy/"]
    with open(os.path.join(OUT, "sitemap.xml"), "w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for u in urls:
            f.write(f"  <url><loc>{SITE}{u}</loc><lastmod>{TODAY}</lastmod></url>\n")
        f.write("</urlset>\n")
    with open(os.path.join(OUT, "site.webmanifest"), "w") as f:
        json.dump({"name": "Midha Limited", "short_name": "Midha", "start_url": "/", "display": "browser",
                   "background_color": "#FDFCF8", "theme_color": "#FDFCF8",
                   "icons": [{"src": "/assets/img/logo-192.png", "sizes": "192x192", "type": "image/png"},
                             {"src": "/assets/img/logo-512.png", "sizes": "512x512", "type": "image/png"}]}, f, indent=2)

if __name__ == "__main__":
    home(); heat_pump(); test_tag(); electrical(); areas_page(); reviews_page(); about_page(); contact_page(); misc(); cloudflare_files()
    print("built", OUT)
