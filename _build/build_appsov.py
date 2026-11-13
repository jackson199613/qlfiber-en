# -*- coding: utf-8 -*-
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from layout import head, header, footer, w, CTA_BAND, crumb, page_hero, subnav, SUB_APP, SITE

CARDS = [
 ("a-glass.html","01","Glass Processing","Lead track","img/sleeve-03.webp",
  "Heat-resistant sleeves, fabrics, tapes and ropes for tempering, bending and forming lines.",
  "Rated to 1100 °C, lint-free, non-marking"),
 ("a-filtration.html","02","Filtration &amp; Separation","Highest value per account","img/fts-huayou-02.webp",
  "Cleanable all-metal media for melt, viscose and hot gas, plus chemical-free oil recovery.",
  "10–60 µm absolute · 30 MPa · 600 m³/h"),
 ("a-emi.html","03","EMI Shielding &amp; Anti-static","Broadest coverage","img/ind-emi.webp",
  "Conductive fiber, blended yarn, thread, braided sleeve and tape for shielding and static control.",
  "0.5–100% steel · 1–64 Ω/m"),
 ("a-specialty.html","04","Specialty Materials","","img/sh-felt.webp",
  "Porous plates, burner media and damping felts for combustion, thermal shock and vibration.",
  "50–90% porosity · to 1100 °C"),
 ("a-automotive.html","05","Automotive","","img/ind-auto.webp",
  "Mould covers, heating wire, chopped fiber, sintered media and hydraulic elements.",
  "Glass forming to seat heating"),
 ("a-textiles.html","06","Functional Textiles &amp; Smart Wearables","","img/ind-wear.webp",
  "Weavable, sewable, washable conductive and heating yarns for apparel and workwear.",
  "1–64 Ω/m · 12 µm monofilament"),
]

STEPS = [
 ("Tell us the conditions","Temperature, medium, pressure or load, conductivity or porosity targets — the numbers you actually run."),
 ("We select the material","From fiber diameter and alloy through to product form, we propose a configuration rather than a catalogue number."),
 ("Samples and testing","QL lab testing plus your own trial on the line. We send the data with the sample."),
 ("Small-batch validation","Confirm performance and batch consistency before anything is scaled."),
 ("Stable supply","Specifications are frozen and production runs to them."),
 ("Keep improving","Adjust with feedback from service."),
]

cards = "".join(
 f'''<a class="appc rv{' d'+str(i%3) if i%3 else ''}" href="{u}">
   <div class="im"><img src="{img}" alt="{t.replace('&amp;','and')}" loading="lazy" width="800" height="600">
     {f'<span class="tag">{tag}</span>' if tag else ''}</div>
   <div class="bd"><span class="n num" style="font-size:10.5px;letter-spacing:.16em;color:var(--muted-2)">{n}</span>
     <h3 style="margin:8px 0 9px">{t}</h3><p>{d}</p>
     <p style="margin-top:12px;font-family:var(--mono);font-size:12px;color:var(--ink)">{k}</p>
     <span class="more">View solution<svg style="width:13px;height:13px"><use href="#i-arrow"/></svg></span></div></a>'''
 for i,(u,n,t,tag,img,d,k) in enumerate(CARDS))

steps = "".join(
 f'''<div style="display:flex;gap:20px;padding:20px 0;border-top:1px solid var(--line)">
   <span class="num" style="font-size:12px;color:var(--muted-2);padding-top:4px;flex:none;width:28px">{i:02d}</span>
   <div><h3 style="font-size:17.5px;margin-bottom:6px">{t}</h3>
   <p style="color:var(--muted);font-size:14.6px;line-height:1.7">{d}</p></div></div>'''
 for i,(t,d) in enumerate(STEPS,1))

sc = json.dumps({"@context":"https://schema.org","@type":"ItemList","name":"Application Solutions",
 "itemListElement":[{"@type":"ListItem","position":i+1,"name":t.replace("&amp;","and"),
                     "url":f"{SITE}/{u}"} for i,(u,n,t,tag,img,d,k) in enumerate(CARDS)]}, ensure_ascii=False)

html = head("Application Solutions | Metal Fiber by Operating Condition — QL Metal Fiber",
 "Six metal fiber application solutions — glass processing, filtration and separation, EMI shielding and anti-static, specialty materials, automotive, functional textiles — plus co-development for conditions outside them.",
 "applications.html",
 "metal fiber applications, glass processing sleeve, metal fiber filtration, EMI shielding fiber, conductive yarn",
 sc, "img/fts-huayou-02.webp") \
 + header("applications.html") + crumb([("Applications", None)]) \
 + page_hero("", "APPLICATION SOLUTIONS",
   "Six solutions, organised by the conditions you run",
   "Buyers rarely ask what products we have. They ask whether a material will survive their furnace temperature, their solvent, their precision requirement — and for how long. Each solution starts from that question and ends with a sample on your line.",
   [("6","","Application solutions"),("7","forms","Product forms available"),("2","µm","Finest fiber diameter")],
   "img/fts-huayou-02.webp") \
 + subnav(SUB_APP, "applications.html") + f"""
<main>
<section class="sec"><div class="wrap">
  <div class="g3">{cards}</div>
</div></section>

<section class="sec alt"><div class="wrap">
  <div class="g2" style="gap:56px;align-items:start">
    <div>
      <div class="eyebrow rv">More Applications · Co-Development</div>
      <h2 class="h-lg rv d1" style="margin:16px 0 16px">Your conditions, our fiber.</h2>
      <p class="lead rv d2">Metal fiber is a platform material, not a single product. If your process needs the heat, corrosion and conductivity of metal together with the flexibility and porosity of a fiber, the application does not have to be on this list. Tell us the conditions and we will propose the fiber, the form and the alloy, build samples in our lab and work with you through small-batch validation to stable supply.</p>
      <p class="rv d3" style="margin-top:14px;color:var(--muted);font-size:14.8px;line-height:1.75">Directions already in service include regenerative heat-exchanger media, high-temperature silencer and sound-absorbing material, resin grinding wheels, high-temperature conveyor belts and seat moulds, fluidised-bed gas distribution plates, membrane supports, catalyst carriers, vacuum-pump protection filtration, pipeline freeze-protection heating, heating elements for medical devices and robot cabling.</p>
      <div class="cta-row rv d3"><a class="btn btn-dark" href="contact.html">Start a co-development<svg><use href="#i-arrow"/></svg></a></div>
    </div>
    <div class="rv d1">{steps}</div>
  </div>
</div></section>

{CTA_BAND}
</main>
""" + footer()
w("applications.html", html)
