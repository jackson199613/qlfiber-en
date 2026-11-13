# -*- coding: utf-8 -*-
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from layout import head, header, footer, w, CTA_BAND, crumb, page_hero, subnav, SUB_CO, SITE, ADDR, COMPANY

def rows(items):
    return '<div class="rows">' + "".join(
        f'<div class="row-i"><div class="dt">{d}</div><div><h4>{t}</h4><p>{b}</p></div></div>'
        for d,t,b in items) + '</div>'
def spec(caption, heads, data, note=""):
    th="".join(f"<th>{h}</th>" for h in heads)
    tr="".join("<tr>"+"".join(f"<td>{c}</td>" for c in r)+"</tr>" for r in data)
    n=f'<p class="tnote">{note}</p>' if note else ""
    return f'<div class="tbl-wrap"><table class="spec"><caption>{caption}</caption><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>{n}'
def gal(items):
    return '<div class="gal rv">' + "".join(
        f'<figure><img src="{u}" alt="{c}" loading="lazy" width="600" height="450"><figcaption>{c}</figcaption></figure>'
        for u,c in items) + '</div>'

# ------------------------------------------------------------- Company Profile
ORG = json.dumps({"@context":"https://schema.org","@type":"Organization","name":COMPANY,
  "url":SITE+"/","logo":f"{SITE}/img/logo.png","foundingDate":"2002",
  "address":{"@type":"PostalAddress","streetAddress":"No. 11 Huangbang Road, Longyan Economic & Technological Development Zone",
             "addressLocality":"Longyan","addressRegion":"Fujian","addressCountry":"CN"},
  "email":"export@qlfiber.com","telephone":"+86 181 5982 1773"}, ensure_ascii=False)

html = head(f"Company Profile — {COMPANY}",
  "Founded in 2002 in Longyan, Fujian. A NEEQ-listed metal fiber manufacturer covering fiber drawing, yarn and textiles, sintered media, filter elements and separation equipment.",
  "company.html","metal fiber manufacturer China, QL Metal Fiber company profile, Fujian",
  ORG,"img/plant-02.webp") + header("company.html") + crumb([("Company","company.html"),("Company Profile",None)]) + page_hero(
  "01","COMPANY","Twenty-four years on one material",
  "We have made metal fiber since 2002 and almost nothing else. The product range widened — yarn, textiles, media, elements, equipment — but it all still starts at the same drawing bench.",
  [("2002","","Founded"),("872336","","NEEQ listing code"),("4","","Business divisions")],
  "img/plant-02.webp") + subnav(SUB_CO,"company.html") + f"""
<main>
<section class="sec"><div class="wrap">
  <div class="g2" style="gap:56px;align-items:start">
    <div class="prose rv">
      <p class="lede">{COMPANY} is a Chinese manufacturer of metal fiber and the products built from it. We draw stainless steel and other alloys down to 2 µm, spin and weave it, lay and sinter it into porous media, and assemble that media into filter elements and separation equipment.</p>
      <p>The company was founded in 2002 in Longyan, Fujian, and is listed on China's National Equities Exchange and Quotations under code 872336. It is recognised as a National High-Tech Enterprise and as a national specialised and sophisticated &ldquo;Little Giant&rdquo; enterprise, and operates an ISO 9001 certified quality management system.</p>
      <p>What matters commercially is that the chain is continuous. A filter element supplier who buys media cannot change the pore structure when your differential pressure rises too quickly. We can, because the media is ours — and because the laboratory that measures the change is in the same building.</p>
      <h3>Four divisions</h3>
      <ul>
        <li><b>Filter media.</b> Sintered metal fiber felt, needled media, sintered mesh.</li>
        <li><b>Filter elements.</b> Pleated cartridges, mesh elements, high-temperature bags, housings.</li>
        <li><b>Purification equipment.</b> Coalescing oil recovery systems for hydrometallurgical extraction circuits.</li>
        <li><b>Thermal and power.</b> Metal fiber textiles for glass processing, burners and high-temperature service.</li>
      </ul>
      <p>A separate yarn business supplies conductive fiber, blended yarn and heating wire for textile and electronics customers.</p>
    </div>
    <div class="rv d1">
      {spec("Company facts", ["Item","Detail"], [
        ("Legal name", COMPANY),("Founded","2002"),("Listing","NEEQ 872336"),
        ("Head office and plant", ADDR),
        ("Quality system","ISO 9001 certified"),
        ("Status","National High-Tech Enterprise; national &ldquo;Little Giant&rdquo; enterprise"),
        ("Core material","Bundle-drawn metal fiber, 2 µm and up"),
        ("Alloys","316L, 304, 302, FeCrAl, nickel-based alloys, Hastelloy, Monel, copper, titanium"),
        ("Export markets","Europe, India, Southeast Asia, Türkiye and the Middle East, Japan and Korea, the Americas"),
        ("Contact","export@qlfiber.com"),
      ])}
      <div class="note" style="margin-top:26px">We supply direct from the factory and through distributors. Most technical textile products carry no minimum order, so a first trial can be a single length.</div>
    </div>
  </div>
</div></section>

<section class="sec alt"><div class="wrap">
  <div class="sec-h"><div class="eyebrow rv">The plant</div>
    <h2 class="h-lg rv d1" style="margin-top:14px">Where it is made</h2></div>
  {gal([("img/plant-02.webp","Production workshop"),("img/plant-07.webp","Sintering and lamination area"),
        ("img/plant-10.webp","Finished media and roll goods"),("img/team-cadre2024.webp","The team, 2024")])}
</div></section>

{CTA_BAND}
</main>
""" + footer()
w("company.html", html)

# ------------------------------------------------------------- History
HIST=[("2002","Founded","The company is established in Longyan, Fujian, to produce metal fiber by bundle drawing."),
  ("2006","Sintered felt","Vacuum sintering of multi-layer fiber webs begins, opening the filtration media business."),
  ("2010","Filter elements","Element assembly is brought in house — pleating, support mesh lamination, end fittings and welding."),
  ("2013","Textiles for glass","Knitted and braided sleeves for glass tempering rollers enter series production."),
  ("2016","Conductive yarn","Blended and insulated conductive yarn for heating and shielding applications is industrialised."),
  ("2019","Research partnerships","Provincial research on metal fiber forming; collaboration on electromagnetic shielding fabric with the Ningbo Institute of Materials Technology, Chinese Academy of Sciences."),
  ("2020","Oil recovery","The coalescing oil recovery system is commercialised for nickel-cobalt extraction circuits."),
  ("2021","NEEQ listing","The company lists on the National Equities Exchange and Quotations under code 872336."),
  ("2023","Smart wearables","A provincial project on flexible functional materials for smart wearables begins."),
  ("2024","Scale","The largest coalescing oil recovery system to date, at 600 m³/h, enters service."),
  ("2026","Equipment recognition","High-efficiency metal coalescing oil removal equipment is taken up as a provincial project and recognised as first-of-its-kind major technical equipment.")]

html = head("History — Metal Fiber Since 2002 | QL Metal Fiber",
  "From bundle-drawn fiber in 2002 to sintered media, filter elements, conductive textiles and 600 m³/h oil recovery systems today.",
  "history.html","QL Metal Fiber history, metal fiber manufacturer since 2002",
  json.dumps({"@context":"https://schema.org","@type":"WebPage","name":"History","url":f"{SITE}/history.html"},ensure_ascii=False),
  "img/plant-07.webp") + header("company.html") + crumb([("Company","company.html"),("History",None)]) + page_hero(
  "02","HISTORY","One capability at a time",
  "Each step below was taken because a customer's problem could not be solved with what we had. That is still how the range grows.",
  None,"img/plant-07.webp") + subnav(SUB_CO,"history.html") + f"""
<main>
<section class="sec"><div class="wrap">
  <div class="sec-h"><div class="eyebrow rv">Milestones</div>
    <h2 class="h-lg rv d1" style="margin-top:14px">2002 to today</h2></div>
  <div class="rv">{rows(HIST)}</div>
</div></section>
{CTA_BAND}
</main>
""" + footer()
w("history.html", html)

# ------------------------------------------------------------- Manufacturing
STEPS=[("01","Bundle drawing","Thousands of wires are drawn together through successive dies and then separated, giving filaments down to 2 µm. The conductor is the metal itself, so properties do not fade with washing or flexing."),
  ("02","Cutting, opening and blending","Filament is chopped to 1–38 mm, opened into sliver or tow, and blended with aramid, polyester, PPS or cotton at ratios from 0.5 to 100% steel."),
  ("03","Spinning, knitting, braiding, weaving","Yarn is spun and then knitted into elastic sleeves, braided into round sleeves, or woven into cloth and tape up to 1500 mm wide."),
  ("04","Web laying","Non-woven webs are laid with a controlled fiber diameter in each layer — this is where the graded pore structure of the finished felt is decided."),
  ("05","Vacuum sintering","Layers are laminated and sintered under vacuum so that every fiber contact is metallurgically bonded. The result is a one-piece metal structure, not a pressed mat."),
  ("06","Element assembly","Media is pleated or wound, laminated with inner support and outer protective mesh, fitted with a perforated core and end fittings, and welded."),
  ("07","Equipment fabrication","Tanks, troughs and skids for oil recovery systems are fabricated and the coalescing elements fitted."),
  ("08","Inspection","Bubble point, permeability, efficiency, porosity, thickness and weight are measured, and an inspection report is issued for the lot.")]

html = head("Manufacturing — From Wire to Finished Element | QL Metal Fiber",
  "Bundle drawing, spinning and weaving, web laying, vacuum sintering, element assembly and equipment fabrication — the whole chain in our own plants.",
  "manufacturing.html","metal fiber manufacturing, bundle drawing, vacuum sintering",
  json.dumps({"@context":"https://schema.org","@type":"WebPage","name":"Manufacturing","url":f"{SITE}/manufacturing.html"},ensure_ascii=False),
  "img/plant-10.webp") + header("company.html") + crumb([("Company","company.html"),("Manufacturing",None)]) + page_hero(
  "03","MANUFACTURING","Wire in at one end, qualified element out at the other",
  "Eight process steps, all under one roof. The reason it matters is not pride in vertical integration — it is that a change at step four can solve a problem that appears at step eight.",
  [("2","µm","Finest filament drawn"),("1500","mm","Maximum cloth width"),("8","","Process steps in house")],
  "img/plant-10.webp") + subnav(SUB_CO,"manufacturing.html") + f"""
<main>
<section class="sec"><div class="wrap">
  <div class="sec-h"><div class="eyebrow rv">Process</div>
    <h2 class="h-lg rv d1" style="margin-top:14px">The chain, step by step</h2></div>
  <div class="rv">{rows(STEPS)}</div>
</div></section>
<section class="sec alt"><div class="wrap">
  <div class="sec-h"><div class="eyebrow rv">Inside the plant</div>
    <h2 class="h-md rv d1" style="margin-top:14px">Production and finished goods</h2></div>
  {gal([("img/plant-02.webp","Production workshop"),("img/plant-10.webp","Roll goods and finished media"),
        ("img/cart-04.webp","Element assembly"),("img/media-05.webp","Media, discs and cut parts")])}
</div></section>
{CTA_BAND}
</main>
""" + footer()
w("manufacturing.html", html)

# ------------------------------------------------------------- Quality & Certifications
CERT=[("ISO 9001","Quality management system","Certified; certificate and scope available on request","Whole company"),
  ("National High-Tech Enterprise","National recognition","Subject to periodic re-assessment","Whole company"),
  ("National &ldquo;Little Giant&rdquo; enterprise","Specialised and sophisticated SME","National level","Whole company"),
  ("NEEQ 872336","Public listing","Audited annual reports","Whole company"),
  ("Provincial first-of-its-kind equipment","Major technical equipment recognition","Provincial level","Oil recovery system")]
QC=[("Incoming","Raw wire and alloy","Certificate of analysis checked against the alloy specification"),
  ("In process","Filament diameter","Sampled through the drawing sequence"),
  ("In process","Web weight and uniformity","Measured before lamination"),
  ("In process","Sintering cycle","Temperature and time recorded for each load"),
  ("Final","Bubble point and permeability","Every lot of media"),
  ("Final","Filtration efficiency","To the agreed method for the product"),
  ("Final","Dimensions and weld integrity","Every element"),
  ("Release","Lot inspection report","Issued with the shipment; retained sample kept")]

html = head("Quality & Certifications — ISO 9001, Lot Reports | QL Metal Fiber",
  "ISO 9001 certified quality management, inspection at incoming, in-process, final and release stages, and a lot inspection report with every shipment.",
  "quality.html","ISO 9001 metal fiber, quality certification, lot inspection report",
  json.dumps({"@context":"https://schema.org","@type":"WebPage","name":"Quality & Certifications","url":f"{SITE}/quality.html"},ensure_ascii=False),
  "img/lab-02.webp") + header("company.html") + crumb([("Company","company.html"),("Quality & Certifications",None)]) + page_hero(
  "04","QUALITY &amp; CERTIFICATIONS","Numbers you can put in a supplier file",
  "A new supplier is qualified on documents before it is qualified on performance. Everything in this section exists so that your purchasing and quality departments can close that file quickly.",
  [("9001","ISO","Certified quality system"),("100","%","Lots with an inspection report"),("8","","Control points from wire to release")],
  "img/lab-02.webp") + subnav(SUB_CO,"quality.html") + f"""
<main>
<section class="sec"><div class="wrap">
  <div class="g2" style="gap:56px;align-items:start">
    <div class="rv">{spec("Certifications and recognition", ["Item","Type","Status","Scope"], CERT,
      "Certificates are issued in Chinese and English where available. Send us the fields your supplier portal requires and we will complete them.")}</div>
    <div class="prose rv d1">
      <div class="eyebrow">What we commit to</div>
      <h2 class="h-md" style="margin:14px 0 18px">Consistency, and evidence of it</h2>
      <p>Buyers rarely fail a metal fiber product on its first lot. They fail it on the fourth, when something has drifted. Our answer is to measure the same things in the same way on every lot, issue the report with the shipment, and keep a retained sample so a later lot can be compared against the one you approved.</p>
      <p>Where your qualification protocol requires a test we do not hold in house, we will say so plainly and arrange a third-party laboratory rather than substitute a different method.</p>
      <div class="note">Performance values published on this site apply to the stated test conditions. They are a basis for selection and comparison, not a warranty for your process. Final suitability is established by a trial under your own conditions.</div>
    </div>
  </div>
</div></section>
<section class="sec alt"><div class="wrap">
  <div class="sec-h"><div class="eyebrow rv">Control plan</div>
    <h2 class="h-lg rv d1" style="margin-top:14px">Where it is checked</h2></div>
  <div class="rv">{spec("Inspection points", ["Stage","What is checked","How"], QC)}</div>
</div></section>
{CTA_BAND}
</main>
""" + footer()
w("quality.html", html)
