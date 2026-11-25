# -*- coding: utf-8 -*-
"""Individual products per product line, and division contacts (2026.11.24, client feedback 2.0)

Sources, same as the Chinese site:
- Fiber & yarn: Yarn Division intro / product introduction / FAQ
- Sintered felt: Filter Media Division intro (.doc) and product manual (.xlsx)
- Technical textiles: "QL Glass Market Product Brochure" (Thermal Division) and its product manual
- Filter elements: Machining workshop introduction (.docx) — product names only; plus elements from the 2025 brochure
- Oil recovery: Purification Division website pack
Images: jl-fiber.com product photos (cleaned up) and photos from the client's shared material. No AI images.
"""

LINE_PRODUCTS = {
    "p-fiber.html": [
        ("fiber", "QL metal fiber", "img/pc-yarn-fiber.webp",
         "Micron-scale fiber drawn from stainless steel and other metal wire, supplied as long filament or staple. It keeps the strength, conductivity and heat resistance of metal with the flexibility of a textile fiber."),
        ("thread", "QL metal fiber thread", "img/pc-yarn-thread.webp",
         "Single or multi-ply thread twisted from 100% stainless steel filament — soft, flexible and conductive. Used for sewing high-temperature filter bags, heating cores, conductive routing and static elimination."),
        ("yarn", "QL metal fiber yarn", "img/pc-yarn-spun.webp",
         "Flexible yarn spun from 100% metal fiber sliver — the core raw material for knitted and woven metal fiber fabric, sleeves and tape."),
        ("blend", "Blended yarn", "img/pc-yarn-blend.webp",
         "Metal fiber blended with aramid, polyester, PPS or cotton for anti-static and shielding fabric; the steel content sets the conductivity."),
        ("insulated", "QL insulated metal fiber thread", "img/pc-yarn-coat.webp",
         "Metal fiber thread core with an insulating jacket — conductive and heat resistant, safe to sew directly. Used in heated garments, seat heating and smart clothing."),
        ("tape", "QL metal fiber woven tape", "img/pc-yarn-tape-spool.webp",
         "Tape woven from metal fiber: heat resistant, flame retardant and effective for static elimination and equipment earthing."),
    ],
    "p-felt.html": [
        ("felt", "Sintered metal fiber felt", "img/pc-media-felt.webp",
         "Non-woven filter medium made from randomly laid short metal fibers, sintered at high temperature so the fibers bond into a uniform, connected pore structure. Mainstream material 316L stainless steel."),
        ("composite", "Mesh-reinforced sintered felt", "img/pc-media-composite.webp",
         "Sintered felt laminated with a metal wire mesh support layer for higher structural strength; fiber diameter, mesh structure and layer sequence can be adjusted."),
        ("alloy", "Special-alloy sintered felt", "img/pc-media-alloy.webp",
         "Sintered felt in FeCrAl, pure nickel, Hastelloy or Inconel for corrosive and high-temperature oxidising environments."),
    ],
    "p-textile.html": [
        ("rope", "High-temperature metal fiber rope", "img/pc-thermo-rope.webp",
         "High-strength rope, rated 350–1100 °C, abrasion and corrosion resistant with a smooth surface. Used to cover automotive glass mould frames and container-glass pusher bars (L-frames), and as anti-static or high-temperature sealing rope. Φ1–12 mm, square or round."),
        ("felt", "High-temperature metal fiber felt", "img/pc-thermo-felt.webp",
         "Three-dimensional porous cushioning material, rated 350–1100 °C, that damps vibration and absorbs impact. Commonly used as heat-resistant pads for glass suction cups and clamps. 2–3 mm thick."),
        ("thread", "High-temperature metal fiber thread", "img/pc-thermo-thread.webp",
         "Flexible, conductive thread rated 350–1100 °C and resistant to acid, alkali and salt. Used to wind chemical-tempering racks, as functional thread in specialty clothing and in high-performance wiring."),
        ("elastic", "High-temperature elastic metal fiber sleeve", "img/pc-thermo-elastic.webp",
         "Elastic tubular protection rated 350–1100 °C — keeps its shape, does not crack or powder at end of life. Typical use: ceramic roller sleeves in physical tempering furnaces. TGZ series."),
        ("braid", "High-temperature braided metal fiber sleeve", "img/pc-thermo-braid.webp",
         "Braided tubular protection rated 350–1100 °C, resistant to potassium nitrate, sulphuric acid and dilute hydrochloric acid, with lasting EMI shielding. Typical use: rack protection in chemical tempering furnaces. TGBX series."),
        ("tape", "High-temperature metal fiber tape / cloth", "img/pc-thermo-tape.webp",
         "Flat heat-resistant material, rated 350–1100 °C, smooth, breathable and drapable. Used as mould-covering tape and mould cloth in glass forming, and for wiping and cushioning hot parts. 0.35–0.5 mm thick; widths 1000 / 1200 / 1500 mm."),
    ],
    "p-element.html": [
        ("hydraulic", "Hydraulic filter elements", "img/pc-mach-hydraulic.webp",
         "Made to drawing in our machining and filter element workshop — media cutting, pleating, forming, bonding, end-cap assembly and pressure testing on one line."),
        ("dust", "Dust collection filter elements", "img/pc-mach-dust.webp",
         "Made to drawing in our machining and filter element workshop — media cutting, pleating, forming, bonding, end-cap assembly and pressure testing on one line."),
        ("air", "Air compressor filter elements", "img/pc-mach-air.webp",
         "Made to drawing in our machining and filter element workshop — media cutting, pleating, forming, bonding, end-cap assembly and pressure testing on one line."),
        ("fluid", "Industrial fluid filter elements", "img/pc-mach-sinter.webp",
         "Made to drawing in our machining and filter element workshop — media cutting, pleating, forming, bonding, end-cap assembly and pressure testing on one line."),
        ("cartridge", "Pleated metal fiber cartridges", "img/pc-mach-fluid.webp",
         "Pleated cartridges built from our own sintered metal fiber felt with support and protective mesh, sized to your housing."),
        ("parts", "Filter cores and metal components", "img/pc-mach-parts.webp",
         "Turning, milling, drilling, grinding and CNC machining of filter cores and other metal components, in carbon steel and stainless steel, with dimensional and geometric tolerance control."),
    ],
    "p-equipment.html": [
        ("tank", "Tank-type oil recovery system", "img/pc-purify-tank.webp",
         "Coalescing oil removal unit for smaller flows; skid-mountable and connected directly to site pipework."),
        ("trough", "Trough-type oil recovery system", "img/pc-purify-trough.webp",
         "Coalescing oil removal for large-flow applications."),
        ("retrofit", "Retrofit of an existing clarifier", "img/pc-purify-retrofit.webp",
         "Oil recovery built into the customer's existing clarifier or trough — lower investment, no change to the process layout."),
    ],
}

# Each product line is looked after by one division (contacts from the client's contact sheet, 2026.11.24)
LINE_DEPT = {"p-fiber.html": "yarn", "p-felt.html": "media", "p-textile.html": "thermo",
             "p-element.html": "machining", "p-equipment.html": "purify"}

DEPTS = [
    {"key": "sales", "name": "Sales Management", "people": [("Ms. Luo", "+86 153 5992 7344"), ("Ms. Lai", "+86 195 5974 2413")], "email": "hcq@jl-jiber.com"},
    {"key": "media", "name": "Filter Media Division", "people": [("Ms. Fang", "+86 133 4834 2686"), ("Ms. Shi", "+86 189 5089 6159")], "email": "sale@jl-fiber.com"},
    {"key": "yarn", "name": "Yarn Division", "people": [("Mr. Ye", "+86 133 1399 4499"), ("Ms. Yang", "+86 181 5982 1773")], "email": "yrh@jl-jiber.com"},
    {"key": "purify", "name": "Purification Division", "people": [("Ms. Liao", "+86 139 5972 1647"), ("Ms. Jiang", "+86 198 5971 1431")], "email": "whr@jl-jiber.com"},
    {"key": "thermo", "name": "Thermal Division", "people": [("Ms. Shi", "+86 187 6010 2933"), ("Ms. Chen", "+86 199 0697 1337")], "email": "chejian@jl-fiber.com"},
    {"key": "machining", "name": "Machining Division", "people": [("Mr. Cao", "+86 180 0607 0316")], "email": ""},
    {"key": "hr", "name": "Administration & HR", "people": [("Ms. Zhong", "+86 597 279 9968"), ("Ms. Cao", "+86 157 5900 0025")], "email": ""},
]
BY_KEY = {d["key"]: d for d in DEPTS}
OFFICES = [
    ("Registered address", "No. 11 Huangbang Road, Longyan Economic & Technological Development Zone, Fujian, China"),
    ("Xiamen office", "Unit 204-7, No. 22 Guanri Road, Software Park Phase II, Xiamen Torch Hi-Tech Zone, Fujian, China"),
    ("Guangzhou office", "Unit 03, 9F, No. 15 Ruanjian Road, Tianhe District, Guangzhou, China"),
]

PHONE_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/></svg>'


def dept_block(d, title=None):
    rows = "".join(
        f'<li><span class="who">{p}</span><a class="tel" href="tel:{t.replace(" ", "")}">{t}</a>'
        + (f'<a class="mail" href="mailto:{d["email"]}">{d["email"]}</a>' if d["email"] else '<span class="mail"></span>') + '</li>'
        for p, t in d["people"])
    return f'<div class="cdept"><h3><i>{PHONE_SVG}</i>{title or d["name"]}</h3><ul>{rows}</ul></div>'


def prod_cards(line):
    out = ""
    for pid, name, img, desc in LINE_PRODUCTS[line]:
        out += (f'<article class="pcard rv" id="{pid}"><div class="im"><img src="{img}" alt="{name}" loading="lazy" width="600" height="450"></div>'
                f'<div class="bd"><h3>{name}</h3><p>{desc}</p><a class="tlink" href="#dvcontact">Ask about this product<svg class="i" style="width:13px;height:13px"><use href="#i-arrow"/></svg></a></div></article>')
    return out


PBY = {(line, pid): (line, name, img, desc) for line, items in LINE_PRODUCTS.items() for pid, name, img, desc in items}
