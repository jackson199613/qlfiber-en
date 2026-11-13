# -*- coding: utf-8 -*-
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from layout import head, header, footer, w, CTA_BAND, crumb, page_hero, subnav, SUB_RES, SITE

FAQ=[("Materials",[
 ("Which alloys can you supply as fiber?","316L, 304 and 302 are standard. FeCrAl, 904L, nickel-based alloys, Hastelloy, Monel, duplex alloys, copper and titanium are available, usually with a minimum quantity. Tell us the medium and temperature and we will propose the alloy rather than ask you to choose one."),
 ("How fine can the fiber be?","2 µm monofilament is the finest we draw. 12 µm is the usual diameter for textile and conductive applications, because it balances conductivity against the hand and strength of the yarn."),
 ("Is the metal plated on, or is the fiber solid metal?","Solid metal. The fiber is drawn from wire, so conductivity and corrosion resistance do not wash out, flex off or degrade with time, as they do with metallised or plated fibers."),
 ("What temperature can the material take?","Depends on the alloy and the form. 316L textiles are rated 350 °C continuous with short-term peaks to 1100 °C; sintered felt is generally used to 480 °C in the process medium; high-temperature filter bags are rated 350–1000 °C. Always state both normal and peak temperature at enquiry."),
]),("Filtration",[
 ("What does &ldquo;absolute rating&rdquo; mean for your felt?","It is the largest particle that passes under the stated test. Our standard KIA3 series runs 10 to 60 µm absolute at 72 to 86% porosity. Bubble point rises as the rating gets finer and air permeability falls — that trade-off is the main thing to balance at selection."),
 ("Can the media be cleaned and reused?","Yes. The structure is all metal and metallurgically bonded at every fiber contact, so it can be back-flushed, ultrasonically cleaned or chemically cleaned and returned to service. That is the main economic difference from a disposable medium."),
 ("My differential pressure rises too quickly. What changes?","Usually thickness or structure rather than rating. The thickened KIA3K series at 1.1 mm raises dirt-holding capacity and flow at the same absolute rating. Send us the current element, the rating, the flow and the change-out interval."),
 ("Can you make elements to fit our existing housings?","Yes. Pleated cartridges run Φ35–60 mm and 425–1250 mm long, with end fittings made to your drawing. We make the media, the support mesh assembly and the element, so rating, strength and fit are specified together."),
]),("Textiles and conductive products",[
 ("Do your sleeves shed fibers?","Finished goods are heat-set so that under normal cutting and handling they do not fuzz or shed. Sharp cut edges and heavily abrasive duty still benefit from edge treatment — describe the installation and we will advise."),
 ("What resistance can you hold on a conductive thread?","1 to 64 Ω/m, set by ply count and core count. Fiber resistance at room temperature varies with the state of the stainless steel fiber, so if your product has a resistance limit, state it at enquiry and we will test samples before qualification."),
 ("Can you blend metal fiber with our own yarn?","Yes. Blend ratios run from 0.5 to 100% stainless steel with aramid, polyester, PPS or cotton. We can trial-spin and trial-weave small quantities before you commit."),
]),("Working with us",[
 ("Is there a minimum order?","Most technical textile products have no minimum order — a trial can be a single length. Special alloys and custom constructions carry a minimum, which we state with the quotation."),
 ("How fast are samples?","Stock samples ship in one to three days, freight normally collect. Made-to-order samples follow the development schedule agreed for the project."),
 ("What do you need from us to quote?","Medium and its chemistry; temperature in service and at peak; pressure and differential pressure; flow; particle size and solids load; cleaning or change-out regime; dimensions or a drawing. The more of these you give, the fewer rounds it takes."),
 ("Do you supply through distributors?","Both direct from the factory and through distributors. Tell us your market and volume and we will say which route fits."),
])]

acc="".join(
 f'''<div class="qa-g rv"><h3 class="h-md">{cat}</h3>''' + "".join(
   f'''<details class="qa-i"><summary>{q}</summary><div class="qa-a"><p>{a}</p></div></details>'''
   for q,a in qs) + '</div>' for cat,qs in FAQ)

sc=json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
  {"@type":"Question","name":q.replace("&ldquo;","“").replace("&rdquo;","”"),
   "acceptedAnswer":{"@type":"Answer","text":a}} for cat,qs in FAQ for q,a in qs]},ensure_ascii=False)

html = head("FAQ — Metal Fiber, Filtration and Textiles | QL Metal Fiber",
  "Answers on alloys, filtration ratings, cleanability, conductive thread resistance, minimum orders and sample lead times.",
  "resources.html","metal fiber FAQ, sintered felt questions, conductive yarn resistance", sc, "img/media-01.webp"
 ) + header("resources.html") + crumb([("Resources","resources.html"),("FAQ",None)]) + page_hero(
  "01","RESOURCES","Questions buyers actually ask",
  "Grouped by subject rather than by product line. If your question is not here, send it — the answer usually ends up on this page.",
  None,"img/media-01.webp") + subnav(SUB_RES,"resources.html") + f"""
<main>
<section class="sec"><div class="wrap"><div class="qa-wrap">{acc}</div></div></section>
{CTA_BAND}
</main>
""" + footer()
w("resources.html", html)

# ------------------------------------------------------------------ Downloads
DL=[("Company profile","PDF","Company introduction, divisions, plant and capability","company-profile"),
 ("Sintered felt — KIA3 technical data","PDF","Rating, thickness, efficiency, bubble point and permeability by series","kia3-data"),
 ("Filter element catalogue","PDF","Pleated cartridges, sintered mesh elements, high-temperature bags","element-catalogue"),
 ("Technical textiles catalogue","PDF","Sleeves, cloth, tape, rope and damping felt for high-temperature service","textile-catalogue"),
 ("Conductive fiber and yarn data","PDF","Blend ratios, resistance per metre, constructions","yarn-data"),
 ("Oil recovery system brochure","PDF","Principle, configurations, typical results and payback","fts-brochure"),
 ("ISO 9001 certificate","PDF","Certificate and scope","iso9001"),
 ("Selection questionnaire","PDF","The conditions we need in order to quote","questionnaire")]

rowsd="".join(f'''<div class="row-i rv"><div class="dt">{k}</div>
  <div><h4>{t}</h4><p>{d}</p></div>
  <a class="tlink dlb" href="contact.html?doc={s}">Request<svg style="width:13px;height:13px"><use href="#i-arrow"/></svg></a></div>'''
  for t,k,d,s in DL)

html = head("Downloads — Catalogues, Data Sheets and Certificates | QL Metal Fiber",
  "Technical data sheets, catalogues, certificates and the selection questionnaire. Request any document and we will email it the same working day.",
  "downloads.html","metal fiber datasheet, sintered felt catalogue, ISO 9001 certificate",
  json.dumps({"@context":"https://schema.org","@type":"WebPage","name":"Downloads","url":f"{SITE}/downloads.html"},ensure_ascii=False),
  "img/media-02.webp") + header("resources.html") + crumb([("Resources","resources.html"),("Downloads",None)]) + page_hero(
  "02","DOWNLOADS","Documents for your supplier file",
  "Request any of the documents below and we will email it the same working day, with the data sheet matched to the grade you are considering rather than a generic range.",
  None,"img/media-02.webp") + subnav(SUB_RES,"downloads.html") + f"""
<main>
<section class="sec"><div class="wrap">
  <div class="sec-h"><div class="eyebrow rv">Available on request</div>
    <h2 class="h-lg rv d1" style="margin-top:14px">Catalogues, data and certificates</h2>
    <p class="lead rv d2" style="margin-top:16px">We send documents on request rather than publishing them for download, so that the data sheet you receive matches the grade and the conditions you are working with — and so we know who to tell when a specification changes.</p></div>
  <div class="rows">{rowsd}</div>
  <div class="note rv" style="margin-top:34px">Some certificates and standards documents exist in Chinese only. Where an English version is needed for a qualification file, we provide a certified English summary.</div>
</div></section>
{CTA_BAND}
</main>
""" + footer()
w("downloads.html", html)
