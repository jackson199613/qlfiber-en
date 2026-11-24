# -*- coding: utf-8 -*-
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from layout import head, header, footer, w, CTA_BAND, crumb, page_hero, subnav, SUB_PROD, SITE
from products_en import prod_cards, dept_block, BY_KEY, LINE_DEPT

def tbl(caption, heads, rows, note=""):
    th = "".join(f'<th{" class=\"num\"" if h.startswith("#") else ""}>{h.lstrip("#")}</th>' for h in heads)
    tr = "".join("<tr>" + "".join(
        f'<td{" class=\"num\"" if str(c).startswith("#") else ""}>{str(c).lstrip("#")}</td>' for c in r) + "</tr>"
        for r in rows)
    n = f'<p class="tnote">{note}</p>' if note else ""
    return (f'<div class="rv"><div class="tbl-wrap"><table class="spec"><caption>{caption}</caption>'
            f'<thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>{n}</div>')

def ul(items): return '<ul>' + "".join(f'<li>{i}</li>' for i in items) + '</ul>'

FELT = [("10KIA3","#10","#0.30","#75","#3700","#110"),("15KIA3","#15","#0.37","#75","#2470","#190"),
        ("20KIA3","#20","#0.45","#80","#1850","#300"),("25KIA3","#25","#0.61","#80","#1480","#350"),
        ("30KIA3","#30","#0.63","#80","#1230","#500"),("40KIA3","#40","#0.66","#78","#925","#620"),
        ("60KIA3","#60","#0.70","#86","#620","#1200")]

LINES = [
dict(f="p-fiber.html", idx="01", en="METAL FIBER & YARN", bg="img/jlw-yarn.webp",
 h1="Stainless steel drawn down to 2 µm",
 lead="Bundle-drawn metal fiber in long filament, chopped and tow form, and the yarns spun from it — pure metal, blended or insulated. This is the raw material behind every other product line.",
 kpis=[("2","µm","Monofilament down to"),("0.5","–100%","Steel content in blends"),("1","–64 Ω/m","Conductive thread resistance")],
 intro="Metal fiber is made by bundle drawing: thousands of stainless steel wires are drawn together through successive dies until each filament reaches micron scale, then separated. Because the conductor is the metal itself rather than a plated layer, electrical and thermal behaviour does not fade with washing, flexing or time.",
 specs=[("Standard alloys","316L, 304, 302"),("Special alloys","FeCrAl, 904L, nickel-based alloys, copper, titanium"),
        ("Monofilament diameter","2 µm and up; 12 µm standard for textile use"),
        ("Fiber forms","Long filament, chopped fiber 1–38 mm, tow, sliver"),
        ("Yarn forms","Pure metal yarn, blended yarn (aramid, polyester, PPS, cotton), insulated metal fiber thread"),
        ("Blend ratio","0.5–100% stainless steel content"),
        ("Conductive thread resistance","1–64 Ω/m"),
        ("Service temperature","350 °C continuous, 850 °C short term depending on alloy")],
 uses=["Anti-static and EMI shielding fabric, non-wovens and conductive compounds",
       "Heated apparel, blankets, gloves, seat and steering-wheel heating",
       "Conductive sewing thread, signal routing in smart garments",
       "Reinforcing fiber for friction materials and high-temperature composites",
       "Feedstock for sintered felt, woven textiles and filter elements"],
 notes="If your product has a resistance limit, state it at enquiry and we will test samples before qualification.",
 gal=[("img/yarn-real-set.webp","Metal fiber yarn and thread range"),("img/yarn-real-thread-set.webp","QL metal fiber thread"),
      ("img/yarn-real-silicone.webp","Silicone-insulated metal fiber thread"),("img/mfg-draw-line.webp","Bundle drawing, schematic")]),

dict(f="p-felt.html", idx="02", en="SINTERED FELT & MEDIA", bg="img/jlw-felt.webp",
 h1="Depth filtration you can wash and put back",
 lead="Non-woven metal fiber webs laminated and vacuum-sintered into a graded pore structure — 10 to 60 µm absolute, 72 to 86% porosity, and cleanable rather than disposable.",
 kpis=[("10","–60 µm","Absolute rating"),("72","–86%","Porosity"),("480","°C","Service temperature")],
 intro="Sintered metal fiber felt filters in depth. Fibers of decreasing diameter are layered so that pore size falls from the upstream face to the downstream face; coarse particles are held near the surface and fine ones deeper in, which is why dirt-holding capacity is high and differential pressure rises slowly. Because the structure is all metal and metallurgically bonded at every fiber contact, it can be cleaned and returned to service.",
 specs=[("Materials","316L stainless steel; also nickel, Hastelloy, iron-chromium alloys, Monel, duplex alloys"),
        ("Absolute filtration rating","10–60 µm, standard series; finer and coarser on request"),
        ("Porosity","72–86%"),("Thickness","0.30–0.70 mm standard; 1.1 mm in the KIA3K thickened series"),
        ("Service temperature","Up to 480 °C in the process medium; higher with heat-resistant alloys"),
        ("Chemical resistance","Acids, alkalis, organic solvents and pharmaceutical media"),
        ("Fabrication","Cuttable, weldable, pleatable; reinforced, thickened and dense-mesh versions available")],
 uses=["Polymer melt and viscose dope filtration","Polyester film and chemical fiber spinning",
       "High-temperature gas filtration and dust removal","Pre-filtration ahead of membranes, vacuum pump protection",
       "Hydraulic and fuel filtration","Membrane support layers"],
 table=("KIA3 standard series — typical values",
        ["Series","#Absolute rating µm","#Thickness mm","#Filtration efficiency %","#Bubble point Pa","#Air permeability at 200 Pa"],
        FELT,
        "Typical values for reference. Final values are confirmed on the factory inspection report for each lot. Bubble point reflects the largest pore and rises as the rating gets finer; air permeability moves in the opposite direction, which is the trade-off to balance at selection."),
 notes="Thickened KIA3K media (1.1 mm) raises dirt-holding capacity and flow at the same rating — useful when the rating is fixed but differential pressure is rising too quickly.",
 gal=[("img/jl-felt.webp","Sintered metal fiber felt"),("img/sem-felt-01.webp","Graded pore structure"),
      ("img/sem-felt-02.webp","Fiber network, micrograph"),("img/jl-felt-stack.webp","Felt sheets, stacked")]),

dict(f="p-textile.html", idx="03", en="TECHNICAL TEXTILES & SLEEVES", bg="img/sleeve-06.webp",
 h1="Heat-resistant cushioning materials for glass manufacturing",
 lead="Rope, felt, thread, elastic sleeves, braided sleeves and tape or cloth made from 316L metal fiber, rated 350–1100 °C — protection and cushioning for the hot side of glass production.",
 kpis=[("350–1100","°C","Service temperature"),("6","products","Rope, felt, thread, sleeves, tape / cloth"),("1500","mm","Maximum standard width")],
 intro="Metal fiber is soft enough to be knitted, braided and woven on textile machinery, so it can take the shape a part actually needs: a sleeve that grips a ceramic roller, a braided sleeve over a chemical-tempering rack, a cloth that covers a forming mould, a felt pad under a suction cup. All six products share the same core properties: rated 350–1100 °C, excellent oxidation resistance in hot air, strong, abrasion and shear resistant, with a smooth, burr-free surface.",
 specs=[("Standard material","316L stainless steel fiber; special materials and sizes on request"),
        ("Service temperature","350–1100 °C"),
        ("Elastic sleeve","TGZ111 / TGZ132 series, Φ50 / 55 / 60 / 65 mm"),
        ("Braided sleeve","TGBX112 / TGBP112 series, Φ8 / 10 / 12 mm"),
        ("Tape / cloth","0.35–0.5 mm thick; widths 1000 / 1200 / 1500 mm, tape width to order"),
        ("Rope","Φ1–12 mm, square or round section"),
        ("Felt","2–3 mm thick, up to 300 × 300 mm"),
        ("Thread","100 / 275 / 1000 series")],
 uses=["Ceramic roller sleeves in physical tempering furnaces","Rack protection in chemical tempering furnaces",
       "Mould-covering tape and mould cloth in glass forming","Cushioning pads for glass suction cups and clamps",
       "Covers for automotive glass mould frames and container-glass pusher bars","Gas turbines, cables, high-temperature equipment and EMI shielding"],
 notes="Source: QL glass market product brochure (Thermal Division). Tell us the furnace type, roller diameter and temperature, and we will send matching samples.",
 gal=[("img/sleeve-06.webp","Tempering line rollers"),("img/sleeve-04.webp","Sleeved rollers on the line"),
      ("img/rd-braid.webp","Braided metal fiber sleeve"),("img/rd-tape.webp","Metal fiber tape and cloth")]),

dict(f="p-element.html", idx="04", en="FILTER ELEMENTS", bg="img/jlw-cart-pleat.webp",
 h1="Elements built from the media up",
 lead="Hydraulic, dust collection, air compressor and industrial fluid filter elements made to drawing, plus pleated metal fiber cartridges built from our own media — with filter cores and metal parts machined in the same workshop.",
 kpis=[("30","MPa","Maximum working pressure"),("1250","mm","Maximum element length"),("1000","°C","Bag filter rating")],
 intro="An element is a system: the felt sets the rating and the dirt-holding capacity, the mesh sets the strength, and the end fittings decide whether it drops into your housing. Because we make the media, the support mesh assembly and the element, those three decisions are taken together rather than passed between suppliers.",
 specs=[("Pleated cartridge diameter","Φ35–60 mm"),("Pleated cartridge length","425–1250 mm"),
        ("Filtration rating","5–60 µm"),("Maximum working pressure","30 MPa"),
        ("Sintered mesh elements","2–100 µm"),
        ("Typical construction","316L sintered felt filter layer; 304 inner support mesh; 304 outer protective mesh; perforated core and end fittings in 304"),
        ("High-temperature filter bags","Rated 350–1000 °C, porosity above 90%"),
        ("Other elements","Precision filter housings, basket strainers, pleated, wound and melt-blown elements, mist eliminators, ceramic membranes")],
 uses=["Polymer melt filtration in chemical fiber and film lines","Viscose dope filtration",
       "High-pressure hydraulic and fuel filtration","High-temperature gas and dust filtration",
       "Vacuum pump protection and pre-filtration"],
 notes="A typical configuration: 316L sintered felt at 10 µm and 0.4 mm thick, inner support mesh 304 at 0.125 mm wire and 48 mesh, outer protective mesh 304 at 0.224 mm wire and 40 mesh. Dimensions and fittings are made to your housing.",
 gal=[("img/jl-cartridge-pleat.webp","Pleated metal fiber cartridge"),("img/jl-cartridge-set.webp","Cartridge range"),
      ("img/media-01.webp","Sintered media discs"),("img/jl-disc.webp","Leaf disc filter")]),

dict(f="p-equipment.html", idx="05", en="OIL RECOVERY SYSTEMS", bg="img/fts-bamo-02.webp",
 h1="Oil removal without a single drop of demulsifier",
 lead="Coalescing oil–water separation for solvent extraction circuits. Oleophilic metal fiber captures dispersed and emulsified oil, grows it into droplets that rise and are drawn off — and the recovered organic phase goes straight back into the process.",
 kpis=[("70","%","Typical oil removal rate"),("600","m³/h","Single-unit capacity up to"),("5","–30 mg/L","Typical outlet oil content")],
 intro="In hydrometallurgical extraction, the oil in a liquor is partly dissolved and partly not. Dissolved oil needs deep treatment; non-dissolved oil can be recovered physically — and it is the non-dissolved fraction that drives the consumption of activated carbon and resin downstream. Removing it first turns a consumable cost into recovered organic phase.",
 specs=[("Principle","Surface-modified oleophilic, hydrophobic metal fiber coalescence — purely physical, no demulsifier, no chemical sludge"),
        ("Configurations","Tank type up to 30 m³/h, skid-mountable; trough type for large flow; retrofit of an existing clarifier trough"),
        ("Single-unit capacity up to","600 m³/h"),
        ("Typical oil removal rate","Around 70%, stable over three years at a 15 m³/h installation"),
        ("Typical outlet oil content","5–30 mg/L, depending on conditions"),
        ("Footprint","Roughly one third to two thirds of the hourly throughput figure"),
        ("Coalescing element life","Long service; longest installation in use five years without replacement"),
        ("Payback","Typically one to two years in nickel-cobalt applications"),
        ("Recognition","Provincial first-of-its-kind major technical equipment recognition")],
 uses=["Oil removal from extraction liquor in nickel-cobalt and copper-cobalt hydrometallurgy",
       "Recovery of organic phase before deep treatment","Pre-treatment ahead of activated carbon or resin",
       "Retrofit of existing clarifier troughs where floor space is limited"],
 table=("Pre-treatment methods compared",
        ["Criterion","Settling","Flotation","Barrier coalescence","QL oil recovery"],
        [("Removal of non-dissolved oil","Poor","Moderate","Good","<b>Very good</b>"),
         ("Footprint","Large","Medium","Medium, often multi-stage","<b>Small</b>, about ⅓–⅔ of hourly throughput"),
         ("Running cost","Low","Higher","Higher, element replaced about yearly","<b>Low</b>, coalescing element not routinely replaced"),
         ("Core material life","n/a","n/a","About one year, performance decays","<b>Long</b>, up to five years in service")],
        "Dissolved oil content in extraction liquor is generally 5–40 ppm depending on the extractant and mixing regime, and still requires deep treatment. Recovering the non-dissolved fraction first is what reduces that downstream load."),
 notes="Systems can be trialled on your own liquor before a proposal is issued. Customer names in China are not published without written consent; our installed base includes nickel-cobalt hydrometallurgy producers.",
 gal=[("img/fts-bamo-02.webp","Trough-type system, 160 m³/h"),("img/fts-huayou-02.webp","600 m³/h system"),
      ("img/fts-site-05.webp","Extraction plant installation"),("img/fts-principle.webp","Coalescence, schematic")]),
]

for L in LINES:
    sc = json.dumps({"@context":"https://schema.org","@type":"Product","name":L["h1"],
        "description":L["lead"],"url":f'{SITE}/{L["f"]}',
        "brand":{"@type":"Brand","name":"QL Metal Fiber"},
        "manufacturer":{"@type":"Organization","name":"Fujian QL Metal Fiber Co., Ltd."}}, ensure_ascii=False)
    spec = tbl("Specifications", ["Item","Value"], L["specs"])
    extra = tbl(*L["table"]) if L.get("table") else ""
    gal = '<div class="gal rv">' + "".join(
        f'<figure><img src="{u}" alt="{c}" loading="lazy" width="600" height="450"><figcaption>{c}</figcaption></figure>'
        for u,c in L["gal"]) + '</div>'
    html = head(f'{L["h1"]} | {L["en"].title()} — QL Metal Fiber', L["lead"], L["f"],
                f'{L["en"].lower()}, metal fiber, QL Metal Fiber, China manufacturer', sc, L["bg"]) \
        + header("products.html") + crumb([("Products","products.html"), (L["en"].title(), None)]) \
        + page_hero(L["idx"], L["en"], L["h1"], L["lead"], L["kpis"], L["bg"]) \
        + subnav(SUB_PROD, L["f"]) + f"""
<main>
<section class="sec tight-top"><div class="wrap">
  <div class="sec-h"><div class="eyebrow rv">Products</div>
    <h2 class="h-md rv d1" style="margin-top:14px">Products in this line</h2></div>
  <div class="pcards">{prod_cards(L["f"])}</div>
</div></section>

<section class="sec alt"><div class="wrap">
  <div class="g2" style="gap:56px;align-items:start">
    <div class="prose rv">
      <p class="lede">{L["intro"]}</p>
      <h3>Where it is used</h3>
      {ul(L["uses"])}
    </div>
    <div class="rv d1">{spec}</div>
  </div>
  <div class="note rv" style="margin-top:34px">{L["notes"]}</div>
</div></section>

{f'<section class="sec"><div class="wrap">{extra}</div></section>' if extra else ''}

<section class="sec{' alt' if extra else ''}"><div class="wrap">
  <div class="sec-h"><div class="eyebrow rv">Gallery</div>
    <h2 class="h-md rv d1" style="margin-top:14px">Product and application</h2></div>
  {gal}
</div></section>

<section class="sec{'' if extra else ' alt'}" id="dvcontact"><div class="wrap">
  <div class="sec-h"><div class="eyebrow rv">Contact</div>
    <h2 class="h-md rv d1" style="margin-top:14px">Talk to the {BY_KEY[LINE_DEPT[L["f"]]]["name"]}</h2>
    <p class="lead rv d2" style="margin-top:12px">The team that makes this product line answers directly — for selection, samples and quotations.</p></div>
  <div class="cdepts rv">{dept_block(BY_KEY[LINE_DEPT[L["f"]]])}{dept_block(BY_KEY["sales"], "Sales Management (general enquiries)")}</div>
</div></section>

{CTA_BAND}
</main>
""" + footer()
    w(L["f"], html)
print(f"产品线 {len(LINES)} 页完成")
