# -*- coding: utf-8 -*-
"""QL Metal Fiber · English site — shared layout"""
import os, json

SITE   = "https://qlfiber-en.netlify.app"
COMPANY = "Fujian QL Metal Fiber Co., Ltd."
BRAND  = "QL Metal Fiber"
TEL    = "+86 181 5982 1773"
TEL_RAW= "+8618159821773"
MAIL   = "export@qlfiber.com"
ADDR   = "No. 11 Huangbang Road, Longyan Economic & Technological Development Zone, Longyan, Fujian, China"
CN_SITE= "https://www.qlfiber.com/"

NAV = [("Products","products.html"),
       ("Applications","applications.html"),
       ("Technology","technology.html"),
       ("Resources","resources.html"),
       ("Company","company.html"),
       ("Contact","contact.html")]

FONTS = ("https://fonts.googleapis.com/css2?"
         "family=Instrument+Sans:ital,wght@0,400;0,500;0,600;0,700;1,400&"
         "family=IBM+Plex+Mono:wght@400;500&display=swap")

ICONS = """<svg style="display:none" aria-hidden="true"><defs>
<symbol id="i-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></symbol>
<symbol id="i-mail" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></symbol>
<symbol id="i-phone" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.4 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/></symbol>
<symbol id="i-doc" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6"/></symbol>
<symbol id="i-search" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></symbol>
</defs></svg>"""


def head(title, desc, canonical, keywords="", schema=None, og="img/hero-main.webp", extra_css=""):
    sc = f'\n<script type="application/ld+json">{schema}</script>' if schema else ""
    kw = f'\n<meta name="keywords" content="{keywords}">' if keywords else ""
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">{kw}
<link rel="canonical" href="{SITE}/{canonical}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{SITE}/{og}">
<meta property="og:url" content="{SITE}/{canonical}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
<link rel="stylesheet" href="assets/site.css">{extra_css}{sc}
</head>
<body>
{ICONS}
"""


def header(active=""):
    links = "".join(
        f'<a href="{u}"{" class=\"on\"" if u == active else ""}>{t}</a>' for t, u in NAV)
    return f"""<div class="topbar"><div class="wrap">
  <div class="tb-l">
    <span><i>●</i> ISO 9001 CERTIFIED</span>
    <span>NEEQ 872336</span>
    <span>EST. 2002 · FUJIAN, CHINA</span>
  </div>
  <div class="tb-r">
    <a href="mailto:{MAIL}">{MAIL}</a>
    <a href="{CN_SITE}" target="_blank" rel="noopener">中文</a>
  </div>
</div></div>

<header id="hdr"><div class="wrap nav">
  <a class="brand" href="index.html" aria-label="{BRAND} home">
    <img src="img/logo.png" alt="{BRAND}" width="40" height="40">
    <span><b>QL Metal Fiber</b><small>Fujian QL · Since 2002</small></span>
  </a>
  <nav class="menu" id="menu">{links}</nav>
  <div class="nav-r">
    <a class="btn btn-line" href="contact.html">Contact</a>
    <a class="btn btn-pri" href="sample.html">Request a sample<svg><use href="#i-arrow"/></svg></a>
    <button class="burger" id="burger" aria-label="Menu" aria-expanded="false"><span></span></button>
  </div>
</div></header>
"""


CTA_BAND = """<section class="band"><div class="wrap">
  <div class="eyebrow rv">Tell us your conditions</div>
  <h2 class="h-lg rv d1" style="margin:18px 0 16px;max-width:20ch">Send us your operating conditions, and we will send samples.</h2>
  <p class="lead rv d2">Temperature, medium, pressure, filtration rating, resistance or porosity — give us the numbers you work with and our engineers will recommend a configuration, quote it and arrange samples for your own testing.</p>
  <div class="cta-row rv d3">
    <a class="btn btn-pri" href="sample.html">Request a sample<svg><use href="#i-arrow"/></svg></a>
    <a class="btn btn-line" href="contact.html">Talk to an engineer</a>
  </div>
</div></section>
"""


def footer():
    cols = [
        ("Products", [("Metal Fiber & Yarn","p-fiber.html"),("Sintered Felt & Media","p-felt.html"),
                      ("Technical Textiles & Sleeves","p-textile.html"),("Filter Elements","p-element.html"),
                      ("Oil Recovery Systems","p-equipment.html")]),
        ("Applications", [("Filtration & Separation","a-filtration.html"),("Glass Processing","a-glass.html"),
                          ("EMI Shielding & Anti-static","a-emi.html"),("Specialty Materials","a-specialty.html"),
                          ("Automotive","a-automotive.html"),("Functional Textiles","a-textiles.html")]),
        ("Company", [("Company Profile","company.html"),("History","history.html"),
                     ("Manufacturing","manufacturing.html"),("Quality & Certifications","quality.html"),
                     ("News & Blog","news.html")]),
    ]
    colhtml = ""
    for h, items in cols:
        lis = "".join(f'<li><a href="{u}">{t}</a></li>' for t, u in items)
        colhtml += f'<div><h5>{h}</h5><ul>{lis}</ul></div>'
    return f"""<footer class="foot dk"><div class="wrap">
  <div class="foot-top">
    <div>
      <a class="brand" href="index.html" style="margin-bottom:20px">
        <img src="img/logo.png" alt="" width="40" height="40">
        <span><b style="color:#fff">QL Metal Fiber</b><small>Fujian QL · Since 2002</small></span>
      </a>
      <p class="blurb">A vertically integrated metal fiber manufacturer — from micron-scale stainless steel fibers to yarns, technical textiles, sintered media, filter elements and separation equipment.</p>
      <p style="font-size:13.4px;line-height:1.7">{ADDR}</p>
      <p style="margin-top:14px;font-size:13.4px">
        <a href="mailto:{MAIL}">{MAIL}</a><br>
        <a href="tel:{TEL_RAW}">{TEL}</a>
      </p>
    </div>
    {colhtml}
  </div>
  <div class="foot-bot">
    <span>© 2026 {COMPANY}</span>
    <span><a href="privacy.html">Privacy Policy</a> · <a href="sitemap.html">Sitemap</a> · <a href="{CN_SITE}" target="_blank" rel="noopener">中文官网</a></span>
  </div>
</div></footer>
<script src="assets/site.js" defer></script>
</body>
</html>
"""


def w(name, html):
    root = os.path.join(os.path.dirname(__file__), "..")
    with open(os.path.join(root, name), "w", encoding="utf-8") as f:
        f.write(html)
    print("  ✓", name)
