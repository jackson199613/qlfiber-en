# -*- coding: utf-8 -*-
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from layout import head, header, footer, w, CTA_BAND, crumb, subnav, SUB_PROD, SITE, COMPANY

SPECS=[("Series","20KIA3"),("Material","316L stainless steel fiber"),("Absolute filtration rating","20 µm"),
 ("Thickness","0.45 mm"),("Filtration efficiency","80%"),("Bubble point","1850 Pa"),
 ("Air permeability at 200 Pa","300 L/min/dm²"),("Porosity","80%"),
 ("Maximum service temperature","480 °C in the process medium"),
 ("Chemical resistance","Acids, alkalis, organic solvents, pharmaceutical media"),
 ("Standard width","Up to 600 mm; slit to order"),("Fabrication","Cuttable, weldable, pleatable")]

FAQ=[("Can this grade be cleaned and reused?","Yes. The felt is metallurgically bonded at every fiber contact, so back-flushing, ultrasonic and chemical cleaning all return it to service."),
 ("What changes if my differential pressure rises too quickly?","Usually thickness rather than rating. The thickened 20KIA3K at 1.1 mm holds the same 20 µm rating with greater dirt-holding capacity."),
 ("Can you supply it as a finished element?","Yes. We make the media, the support mesh assembly and the element, so rating, strength and end fittings are specified together."),
 ("Are these values guaranteed?","They are typical values, confirmed on the inspection report for each lot. They apply to the stated test conditions and are a basis for selection, not a performance warranty.")]

DL=[("20KIA3 technical data sheet","PDF","kia3-20"),("KIA3 full series data","PDF","kia3-series"),
    ("ISO 9001 certificate","PDF","iso9001"),("Selection questionnaire","PDF","questionnaire")]

sc=json.dumps({"@context":"https://schema.org","@type":"Product","name":"20KIA3 sintered metal fiber felt",
 "description":"316L sintered metal fiber felt, 20 µm absolute rating, 0.45 mm thick, 80% porosity.",
 "sku":"20KIA3","url":f"{SITE}/p-detail.html","brand":{"@type":"Brand","name":"QL Metal Fiber"},
 "manufacturer":{"@type":"Organization","name":COMPANY},
 "image":f"{SITE}/img/sh-felt.webp"},ensure_ascii=False)

html = head("20KIA3 Sintered Metal Fiber Felt — 20 µm Absolute | QL Metal Fiber",
 "316L sintered metal fiber felt, 20 µm absolute rating, 0.45 mm thick, 80% porosity, 1850 Pa bubble point. Cleanable, weldable and pleatable.",
 "p-detail.html","20KIA3, sintered metal fiber felt, 20 micron filter media", sc, "img/sh-felt.webp"
 ) + header("products.html") + crumb([("Products","products.html"),
     ("Sintered Felt & Media","p-felt.html"),("20KIA3",None)]) + subnav(SUB_PROD,"p-felt.html") + f"""
<main>
<section class="sec" style="padding-top:56px"><div class="wrap">
  <div class="pd">
    <div class="pd-media rv">
      <figure class="pd-main"><img src="img/sh-felt.webp" alt="20KIA3 sintered metal fiber felt" width="900" height="675"></figure>
      <div class="pd-thumbs">
        <img src="img/micro-gradient.webp" alt="Graded pore structure" loading="lazy" width="300" height="225">
        <img src="img/micro-network.webp" alt="Fiber network micrograph" loading="lazy" width="300" height="225">
        <img src="img/media-05.webp" alt="Cut media and discs" loading="lazy" width="300" height="225">
      </div>
    </div>
    <div class="pd-info rv d1">
      <div class="eyebrow">Sintered Felt &amp; Media</div>
      <h1 class="h-lg" style="margin:14px 0 16px">20KIA3 sintered metal fiber felt</h1>
      <p class="lead">A 316L depth-filtration medium rated 20 µm absolute at 80% porosity and 0.45 mm thick — the middle of the KIA3 series, and the grade most often chosen as a starting point for polymer melt and high-temperature gas duty.</p>
      <ul class="kpi3">
        <li><b class="num">20</b><span>µm absolute</span></li>
        <li><b class="num">80</b><span>% porosity</span></li>
        <li><b class="num">480</b><span>°C service</span></li>
      </ul>
      <div class="cta-row" style="margin-top:30px">
        <a class="btn btn-pri" href="sample.html">Request a sample<svg><use href="#i-arrow"/></svg></a>
        <a class="btn btn-line" href="contact.html">Ask an engineer</a>
      </div>
      <p class="tnote" style="margin-top:20px">No minimum order on trial quantities of standard series. Stock samples ship in one to three days.</p>
    </div>
  </div>
</div></section>

<section class="sec alt"><div class="wrap">
  <div class="g2" style="gap:56px;align-items:start">
    <div class="rv"><div class="tbl-wrap"><table class="spec"><caption>Specification</caption>
      <thead><tr><th>Item</th><th>Value</th></tr></thead><tbody>
      {"".join(f"<tr><td>{a}</td><td>{b}</td></tr>" for a,b in SPECS)}
      </tbody></table></div>
      <p class="tnote">Typical values, confirmed on the inspection report for each lot.</p></div>
    <div class="prose rv d1">
      <div class="eyebrow">Where it is used</div>
      <h2 class="h-md" style="margin:14px 0 18px">Typical duty</h2>
      <ul>
        <li>Polymer melt filtration in chemical fiber and film lines</li>
        <li>Viscose dope filtration</li>
        <li>High-temperature gas filtration and dust removal</li>
        <li>Pre-filtration ahead of membranes and vacuum pump protection</li>
        <li>Hydraulic and fuel filtration in a pleated element</li>
      </ul>
      <h3>Selecting within the series</h3>
      <p>Moving finer raises bubble point and lowers permeability; moving coarser does the reverse. If the rating has to stay at 20 µm but the interval between changes is too short, the thickened 20KIA3K at 1.1 mm adds depth without changing the rating.</p>
      <div class="note">Send the medium, temperature, pressure drop, flow and solids load and we will confirm whether this grade is the right starting point — or propose the one that is.</div>
    </div>
  </div>
</div></section>

<section class="sec"><div class="wrap">
  <div class="g2" style="gap:56px;align-items:start">
    <div class="rv">
      <div class="eyebrow">Questions</div>
      <h2 class="h-md" style="margin:14px 0 20px">About this grade</h2>
      <div class="qa-g" style="margin:0">
      {"".join(f'<details class="qa-i"><summary>{q}</summary><div class="qa-a"><p>{a}</p></div></details>' for q,a in FAQ)}
      </div>
    </div>
    <div class="rv d1">
      <div class="eyebrow">Documents</div>
      <h2 class="h-md" style="margin:14px 0 20px">Available on request</h2>
      <div class="rows">
      {"".join(f'<div class="row-i"><div class="dt">{k}</div><div><h4>{t}</h4></div><a class="tlink dlb" href="contact.html?doc={s}">Request<svg style="width:13px;height:13px"><use href="#i-arrow"/></svg></a></div>' for t,k,s in DL)}
      </div>
    </div>
  </div>
</div></section>

{CTA_BAND}
</main>
""" + footer()
w("p-detail.html", html)
