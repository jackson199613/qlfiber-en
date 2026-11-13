# -*- coding: utf-8 -*-
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from layout import head, header, footer, w, CTA_BAND, crumb, page_hero, subnav, SUB_PROD, SITE

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
dict(f="p-fiber.html", idx="01", en="METAL FIBER & YARN", bg="img/en-sh-yarn.webp",
 h1="Stainless steel drawn down to 2 µm",
 lead="Bundle-drawn metal fiber in long filament, chopped and tow form, and the yarns spun from it — pure metal, blended or insulated. This is the raw material behind every other product line.",
 kpis=[("2","µm","Finest monofilament"),("0.5","–100%","Steel content in blends"),("1","–64 Ω/m","Conductive thread resistance")],
 intro="Metal fiber is made by bundle drawing: thousands of stainless steel wires are drawn together through successive dies until each filament reaches micron scale, then separated. Because the conductor is the metal itself rather than a plated layer, electrical and thermal behaviour does not fade with washing, flexing or time.",
 specs=[("Standard alloys","316L, 304, 302"),("Special alloys","FeCrAl, 904L, nickel-based alloys, copper, titanium"),
        ("Monofilament diameter","2 µm and up; 12 µm standard for textile use"),
        ("Fiber forms","Long filament, chopped fiber 1–38 mm, tow, sliver"),
        ("Yarn forms","Pure metal yarn, blended yarn (aramid, polyester, PPS, cotton), insulated heating wire"),
        ("Blend ratio","0.5–100% stainless steel content"),
        ("Conductive thread resistance","1–64 Ω/m, set by ply count and core count"),
        ("Service temperature","350 °C continuous, 850 °C short term depending on alloy")],
 uses=["Anti-static and EMI shielding fabric, non-wovens and conductive compounds",
       "Heated apparel, blankets, gloves, seat and steering-wheel heating",
       "Conductive sewing thread, signal routing in smart garments",
       "Reinforcing fiber for friction materials and high-temperature composites",
       "Feedstock for sintered felt, woven textiles and filter elements"],
 notes="Fiber resistance at room temperature varies with the state of the stainless steel fiber. If your product has a resistance limit, state it at enquiry and we will test samples before qualification.",
 gal=[("img/en-sh-yarn.webp","Metal fiber yarn on cone"),("img/en-sh-fiber.webp","Blended yarn"),
      ("img/en-micro-drawing.webp","Bundle drawing, schematic"),("img/prod-heatwire.webp","Insulated heating wire")]),

dict(f="p-felt.html", idx="02", en="SINTERED FELT & MEDIA", bg="img/en-sh-felt.webp",
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
 gal=[("img/en-sh-felt.webp","Sintered metal fiber felt"),("img/en-micro-gradient.webp","Graded pore structure"),
      ("img/en-micro-network.webp","Fiber network, micrograph"),("img/media-05.webp","Media and discs")]),

dict(f="p-textile.html", idx="03", en="TECHNICAL TEXTILES & SLEEVES", bg="img/en-sh-sleeve.webp",
 h1="Woven, knitted and braided metal — for heat that destroys fabric",
 lead="Elastic knitted sleeves, braided sleeves, woven cloth, tape and rope made from 316L metal fiber, rated 350 °C continuous and 1100 °C short term, with no coating to shed.",
 kpis=[("350","°C","Continuous service"),("1100","°C","Short-term peak"),("1500","mm","Maximum standard width")],
 intro="Metal fiber is soft enough to be knitted, braided and woven on textile machinery, so it can take the shape a part actually needs: a sleeve that grips a roller, a tape that wraps a toothed bar, a cloth that covers a bending mould. Finished goods are heat-set so that, under normal cutting and handling, they do not fuzz or shed.",
 specs=[("Standard material","316L stainless steel fiber; FeCrAl on request, subject to minimum order"),
        ("Elastic knitted sleeve","TGZ112, Φ35 / 50 / 55 / 60 mm"),
        ("Braided sleeve","TGBX112 / TGBX113, Φ5–14 mm"),
        ("Knitted metal sleeve","ZDJX113 / ZDJF113, conformable to irregular parts"),
        ("Woven cloth","Plain 0.35 mm, twill 0.5 mm"),
        ("Standard widths","1000 / 1200 / 1500 mm; slitting and narrow widths available"),
        ("Tape thickness","0.35–0.5 mm, custom thickness on evaluation"),
        ("Rope","Φ1–12 mm, square or round section"),
        ("Damping felt","2–3 mm thick")],
 uses=["Ceramic roller protection in glass tempering furnaces","Toothed bars and rack protection in chemical strengthening",
       "Hot bending mould covers for automotive glass","Thermocouple and cable sleeving",
       "Suction cup and clamp cushioning, container pusher bars","Equipment earthing and static elimination"],
 notes="Sharp cut edges and heavily abrasive duty still benefit from edge treatment — tell us the installation and we will advise whether the ends should be finished.",
 gal=[("img/en-sh-sleeve.webp","Braided metal fiber sleeve"),("img/sh-belt.webp","Metal fiber woven tape"),
      ("img/en-sh-cloth.webp","Metal fiber woven cloth"),("img/sleeve-04.webp","Sleeved rollers in service")]),

dict(f="p-element.html", idx="04", en="FILTER ELEMENTS", bg="img/en-sh-element.webp",
 h1="Elements built from the media up",
 lead="Pleated cartridges, sintered mesh elements and high-temperature metal filter bags — made in house from our own media, so the rating, the structure and the end fittings are all specified together.",
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
 gal=[("img/en-sh-element.webp","Pleated metal fiber cartridge"),("img/cart-04.webp","Cartridges in production"),
      ("img/media-01.webp","Sintered media discs"),("img/media-02.webp","Sintered mesh and discs")]),

dict(f="p-equipment.html", idx="05", en="OIL RECOVERY SYSTEMS", bg="img/fts-bamo-02.webp",
 h1="Oil removal without a single drop of demulsifier",
 lead="Coalescing oil–water separation for solvent extraction circuits. Oleophilic metal fiber captures dispersed and emulsified oil, grows it into droplets that rise and are drawn off — and the recovered organic phase goes straight back into the process.",
 kpis=[("70","%","Typical oil removal rate"),("600","m³/h","Largest unit in service"),("5","–30 mg/L","Typical outlet oil content")],
 intro="In hydrometallurgical extraction, the oil in a liquor is partly dissolved and partly not. Dissolved oil needs deep treatment; non-dissolved oil can be recovered physically — and it is the non-dissolved fraction that drives the consumption of activated carbon and resin downstream. Removing it first turns a consumable cost into recovered organic phase.",
 specs=[("Principle","Surface-modified oleophilic, hydrophobic metal fiber coalescence — purely physical, no demulsifier, no chemical sludge"),
        ("Configurations","Tank type up to 30 m³/h, skid-mountable; trough type for large flow; retrofit of an existing clarifier trough"),
        ("Largest unit in service","600 m³/h"),
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
        [("Removal of non-dissolved oil","Poor","Moderate","Good","<b>Best</b>"),
         ("Footprint","Large","Medium","Medium, often multi-stage","<b>Small</b>, about ⅓–⅔ of hourly throughput"),
         ("Running cost","Low","Higher","Higher, element replaced about yearly","<b>Low</b>, coalescing element not routinely replaced"),
         ("Core material life","n/a","n/a","About one year, performance decays","<b>Long</b>, up to five years in service")],
        "Dissolved oil content in extraction liquor is generally 5–40 ppm depending on the extractant and mixing regime, and still requires deep treatment. Recovering the non-dissolved fraction first is what reduces that downstream load."),
 notes="Systems can be trialled on your own liquor before a proposal is issued. Customer names in China are not published without written consent; our installed base includes leading nickel-cobalt hydrometallurgy producers.",
 gal=[("img/fts-bamo-02.webp","Trough-type system, 160 m³/h"),("img/fts-huayou-02.webp","600 m³/h system"),
      ("img/fts-site-05.webp","Extraction plant installation"),("img/en-micro-coalesce.webp","Coalescence, schematic")]),
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
<section class="sec"><div class="wrap">
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

{f'<section class="sec alt"><div class="wrap">{extra}</div></section>' if extra else ''}

<section class="sec{'' if extra else ' alt'}"><div class="wrap">
  <div class="sec-h"><div class="eyebrow rv">Gallery</div>
    <h2 class="h-md rv d1" style="margin-top:14px">Product and application</h2></div>
  {gal}
</div></section>

{CTA_BAND}
</main>
""" + footer()
    w(L["f"], html)
print(f"产品线 {len(LINES)} 页完成")
