# -*- coding: utf-8 -*-
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from layout import head, header, footer, w, CTA_BAND, crumb, page_hero, subnav, SUB_PROD, SITE

LINES=[("01","p-fiber.html","Metal Fiber & Yarn","img/prod-yarn.webp",
        "Bundle-drawn stainless steel fiber from 2 µm, in filament, chopped and tow form — and the pure, blended and insulated yarns spun from it.",
        ["2 µm monofilament","0.5–100% steel blends","1–64 Ω/m conductive thread"],"fiber yarn"),
       ("02","p-felt.html","Sintered Felt & Media","img/sh-felt.webp",
        "Graded-pore metal fiber felt, 10–60 µm absolute at 72–86% porosity — depth filtration that can be cleaned and returned to service.",
        ["10–60 µm absolute","72–86% porosity","480 °C service"],"felt media filtration"),
       ("03","p-textile.html","Technical Textiles & Sleeves","img/sh-sleeve.webp",
        "Knitted, braided and woven metal fiber: sleeves, cloth, tape and rope rated 350 °C continuous and 1100 °C short term.",
        ["350 °C continuous","Φ5–60 mm sleeves","1500 mm cloth width"],"textile glass"),
       ("04","p-element.html","Filter Elements","img/sh-cartridge.webp",
        "Pleated cartridges, sintered mesh elements and high-temperature filter bags, built in house from our own media.",
        ["5–60 µm rating","30 MPa working pressure","425–1250 mm length"],"element filtration"),
       ("05","p-equipment.html","Oil Recovery Systems","img/fts-bamo-02.webp",
        "Coalescing oil–water separation for extraction circuits — no demulsifier, no chemical sludge, and the organic phase goes back into the process.",
        ["600 m³/h largest unit","~70% oil removal","1–2 year payback"],"equipment filtration")]

FORMS=[("Fiber (filament, chopped, sliver)","●","●","●","○","●","○"),
       ("Yarn & thread (pure, blended, insulated)","●","●","●","—","●","—"),
       ("Textiles (sleeve, tape, cloth, rope)","●","●","●","●","●","○"),
       ("Felt (sintered, needled, damping)","○","●","●","●","○","●"),
       ("Panels (porous plate, burner sheet, sintered mesh)","○","●","●","●","—","●"),
       ("Filter elements","—","●","●","●","—","—"),
       ("Separation equipment","—","○","●","—","—","—")]
PROPS=["Conductive","High temperature","Corrosion resistant","Porous / permeable","Flexible / weavable","Damping / acoustic"]

def dot(v):
    cls={"●":"dot","○":"dot o","—":"dot n"}[v]
    lab={"●":"Core property","○":"Available on request","—":"Not a primary use"}[v]
    return f'<td><span class="{cls}" title="{lab}" aria-label="{lab}"></span></td>'

cards="".join(f'''<a class="line rv" href="{f}">
  <div class="im"><img src="{img}" alt="{name}" loading="lazy" width="600" height="400"></div>
  <div class="bd"><span class="n">{idx}</span><h3>{name}</h3><p>{lead}</p>
    <ul class="kpis">{"".join(f"<li>{k}</li>" for k in kpi)}</ul>
    <span class="more">View product line<svg class="i" style="width:13px;height:13px"><use href="#i-arrow"/></svg></span></div></a>'''
 for idx,f,name,img,lead,kpi,tag in LINES)

matrix='<div class="matrix"><div class="tbl-wrap"><table class="mx"><thead><tr><th style="text-align:left">Product form</th>' + \
  "".join(f'<th>{p}</th>' for p in PROPS) + '</tr></thead><tbody>' + \
  "".join('<tr><th scope="row">'+r[0]+'</th>'+"".join(dot(v) for v in r[1:])+'</tr>' for r in FORMS) + \
  '</tbody></table></div></div>'

sc=json.dumps({"@context":"https://schema.org","@type":"ItemList","name":"Product lines",
  "itemListElement":[{"@type":"ListItem","position":i+1,"name":n,"url":f"{SITE}/{f}"}
                     for i,(_,f,n,*_r) in enumerate(LINES)]},ensure_ascii=False)

html = head("Products — Metal Fiber, Felt, Textiles, Elements and Systems | QL Metal Fiber",
   "Five product lines built on one material: bundle-drawn metal fiber. Fiber and yarn, sintered felt, technical textiles, filter elements and oil recovery systems.",
   "products.html","metal fiber products, sintered felt, metal fiber sleeve, filter element, oil recovery system",
   sc,"img/sh-felt.webp") + header("products.html") + crumb([("Products",None)]) + page_hero(
   "", "PRODUCTS", "One material, five product lines",
   "Everything we make starts as bundle-drawn metal fiber. What changes is the form it takes — and the form is chosen from your operating conditions, not from a catalogue page.",
   [("5","lines","From fiber to finished system"),("2","µm","Finest monofilament"),("62","patents","Granted and pending")],
   "img/sh-felt.webp") + subnav(SUB_PROD,"products.html") + f"""
<main>
<section class="sec"><div class="wrap">
  <div class="sec-h"><div class="eyebrow rv">Product lines</div>
    <h2 class="h-lg rv d1" style="margin-top:14px">Choose by form, or tell us the <em>duty</em></h2>
    <p class="lead rv d2" style="margin-top:16px">If you already know the form you need, start here. If you know only the temperature, the medium and the pressure, go to Applications — we will work back from the conditions.</p></div>
  <div class="lines">{cards}</div>
</div></section>

<section class="sec alt"><div class="wrap">
  <div class="sec-h"><div class="eyebrow rv">Capability matrix</div>
    <h2 class="h-lg rv d1" style="margin-top:14px">What each form is actually good at</h2>
    <p class="lead rv d2" style="margin-top:16px">Metal fiber is a platform material rather than a single product. This is the honest map of which form carries which property.</p></div>
  <div class="rv">{matrix}</div>
  <div class="mx-key rv"><span><span class="dot"></span> Core property</span>
    <span><span class="dot o"></span> Achievable on request</span>
    <span><span class="dot n"></span> Not a primary use</span></div>
</div></section>

<section class="sec"><div class="wrap">
  <div class="g2" style="gap:56px;align-items:start">
    <div class="prose rv"><div class="eyebrow">How selection works</div>
      <h2 class="h-md" style="margin:14px 0 18px">Conditions first, material second</h2>
      <p>Send the operating conditions and we work back to the material: medium and its chemistry, temperature in service and at peak, pressure and differential pressure, flow, particle size and load, cycle and cleaning regime, and the space the part has to fit into.</p>
      <p>We then propose one or two candidates, test them in our own laboratory, and send samples for a trial on your line. Specification follows the trial, not the other way round.</p>
    </div>
    <div class="rv d1"><div class="rows">
      <div class="row-i"><div class="dt">Step 1</div><div><h4>Conditions</h4><p>You send the duty — medium, temperature, pressure, flow, particles, cycle.</p></div></div>
      <div class="row-i"><div class="dt">Step 2</div><div><h4>Selection</h4><p>We propose one or two candidate materials and explain the trade-off between them.</p></div></div>
      <div class="row-i"><div class="dt">Step 3</div><div><h4>Laboratory test</h4><p>Bubble point, permeability, efficiency and metallography, measured in house.</p></div></div>
      <div class="row-i"><div class="dt">Step 4</div><div><h4>Sample trial</h4><p>Samples on your line. No minimum order on most textile products.</p></div></div>
      <div class="row-i"><div class="dt">Step 5</div><div><h4>Qualification</h4><p>Small-batch validation, then series supply with lot inspection reports.</p></div></div>
    </div></div>
  </div>
</div></section>

{CTA_BAND}
</main>
""" + footer()
w("products.html", html)
