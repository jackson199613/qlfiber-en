# -*- coding: utf-8 -*-
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from layout import head, header, footer, w, CTA_BAND, SITE, COMPANY, MAIL, TEL, ADDR

APPS = [
 ("a-glass.html","Glass Processing","Lead track",
  "Roller sleeves, braided sleeves and woven belts that take 1100&nbsp;°C, stay lint-free and leave no marks on the glass.",
  "img/sleeve-03.webp"),
 ("a-filtration.html","Filtration &amp; Separation","Highest value per account",
  "Cleanable, reusable all-metal media for polymer melt, viscose and hot gas — plus chemical-free oil recovery for solvent extraction.",
  "img/fts-huayou-02.webp"),
 ("a-emi.html","EMI Shielding &amp; Anti-static","Broadest coverage",
  "Conductivity comes from the fiber itself, not a coating, so anti-static and shielding performance survives repeated washing.",
  "img/ind-emi.webp"),
 ("a-specialty.html","Specialty Materials","",
  "Porous plates, burner media and damping felts where ceramics crack under thermal shock and foams lose strength.",
  "img/sh-felt.webp"),
 ("a-automotive.html","Automotive","",
  "From glass bending mould covers and heated seats to friction materials and hydraulic filtration.",
  "img/ind-auto.webp"),
 ("a-textiles.html","Functional Textiles &amp; Smart Wearables","",
  "Weavable, sewable, washable conductive and heating yarns that run on standard textile equipment.",
  "img/ind-wear.webp"),
]

LINES = [
 ("p-fiber.html","01","Metal Fiber &amp; Yarn","Bundle-drawn stainless steel fiber down to 2&nbsp;µm, supplied as long fiber, chopped fiber, tow, pure-metal and blended yarn.","img/prod-yarn.webp"),
 ("p-felt.html","02","Sintered Felt &amp; Media","KIA3 / KIA3K / KIC4 sintered felts, 10–60&nbsp;µm absolute, 72–86% porosity, cleanable and reusable.","img/sh-felt.webp"),
 ("p-textile.html","03","Technical Textiles &amp; Sleeves","Knitted and braided sleeves, woven fabrics, tapes and ropes rated 350–1100&nbsp;°C.","img/sh-sleeve.webp"),
 ("p-element.html","04","Filter Elements","Pleated cartridges to 30&nbsp;MPa, sintered mesh elements, high-temperature metal filter bags.","img/sh-cartridge.webp"),
 ("p-equipment.html","05","Oil Recovery Systems","Coalescing oil–water separation for hydrometallurgy — no demulsifiers, largest unit in service 600&nbsp;m³/h.","img/fts-bamo-02.webp"),
]

MATRIX = [
 ("Fiber — long, chopped, tow",        1,1,1,0,1,0),
 ("Wire &amp; yarn — pure, blended, insulated", 1,1,1,-1,1,-1),
 ("Textiles — sleeve, tape, cloth, rope", 1,1,1,1,1,0),
 ("Felt — sintered, needled, damping", 0,1,1,1,0,1),
 ("Plate — porous, burner, sintered mesh", 0,1,1,1,-1,1),
 ("Filter elements",                   -1,1,1,1,-1,-1),
 ("Separation equipment",              -1,0,1,-1,-1,-1),
]
MCOLS = ["Conductive","High&nbsp;temp","Corrosion","Porous / permeable","Flexible / weavable","Damping"]

FAQ = [
 ("What is the finest fiber you can produce, and in which alloys?",
  "Our bundle-drawing line produces stainless steel fiber down to 2&nbsp;µm. Standard alloys are 316L, 304 and 302; we also run FeCrAl, 904L, nickel-based alloys, copper and titanium. Alloy choice is driven by the service temperature and the chemistry of your medium, so tell us both and we will propose the material."),
 ("Do you have a minimum order quantity?",
  "There is no minimum order for glass-processing sleeves — we can supply by the metre so you can trial them on one furnace first. Other product lines are quoted by specification and operating conditions, and we support sampling and application testing before any volume commitment."),
 ("How do I choose between a sintered felt and a wire mesh?",
  "Sintered felt filters in depth: a graded pore structure traps contaminant throughout the thickness, so differential pressure rises slowly and service intervals are long. Woven and sintered mesh filters mainly at the surface and offers higher rigidity, which suits high pressure and frequent back-flushing. Most of our filter elements combine both — felt for the rating, mesh for the structure."),
 ("Will the conductivity of your yarn fade after washing?",
  "No. The conductor is the stainless steel fiber itself, not a metallic coating, so there is no plated layer to crack, oxidise or wear off. Blended yarns can be laundered like ordinary fabric; anti-static and shielding performance does not decline with wash cycles."),
 ("Can you make material to our drawing?",
  "Yes. Fiber diameter, fiber length, yarn count and twist, sleeve inner and outer diameter, filtration rating, thickness, porosity, element dimensions and end fittings are all specified to the application. Separation equipment is sized to the flow you need to treat."),
 ("What do you need from me to recommend a configuration?",
  "Operating temperature, the medium and its chemistry, pressure or flow, the filtration rating or resistance range you need, and what the incumbent material is and how long it lasts. With those five answers we can normally come back with a configuration and a sample plan."),
]

SCHEMA = json.dumps({
 "@context":"https://schema.org","@graph":[
  {"@type":"Organization","@id":SITE+"/#org","name":COMPANY,"alternateName":"QL Metal Fiber",
   "url":SITE+"/","logo":SITE+"/img/logo.png","foundingDate":"2002",
   "description":"Vertically integrated metal fiber manufacturer: micron-scale stainless steel fibers, yarns, technical textiles, sintered filter media, filter elements and separation equipment.",
   "address":{"@type":"PostalAddress","streetAddress":"No. 11 Huangbang Road, Longyan Economic & Technological Development Zone","addressLocality":"Longyan","addressRegion":"Fujian","addressCountry":"CN"},
   "email":MAIL,"telephone":TEL,
   "hasCredential":["ISO 9001 certified quality management system","National High-Tech Enterprise",
                    "National Specialized, Refined, Distinctive and Innovative \"Little Giant\" Enterprise"]},
  {"@type":"WebSite","@id":SITE+"/#web","url":SITE+"/","name":"QL Metal Fiber","publisher":{"@id":SITE+"/#org"},
   "inLanguage":"en"},
  {"@type":"FAQPage","mainEntity":[
    {"@type":"Question","name":q.replace("&nbsp;"," "),
     "acceptedAnswer":{"@type":"Answer","text":a.replace("&nbsp;"," ")}} for q,a in FAQ]}
 ]}, ensure_ascii=False)


def dot(v):
    return '<span class="dot"></span>' if v == 1 else ('<span class="dot o"></span>' if v == 0 else '<span class="dot n"></span>')

app_cards = "".join(
 f'''<a class="appc rv{' d'+str(i%3) if i%3 else ''}" href="{u}">
      <div class="im"><img src="{img}" alt="{t.replace('&amp;','and')}" loading="lazy" width="800" height="600">
        {f'<span class="tag">{tag}</span>' if tag else ''}</div>
      <div class="bd"><h3>{t}</h3><p>{d}</p><span class="more">View solution<svg class="i" style="width:13px;height:13px"><use href="#i-arrow"/></svg></span></div>
     </a>''' for i,(u,t,tag,d,img) in enumerate(APPS))

line_cards = "".join(
 f'''<a class="line rv" href="{u}"><div class="im"><img src="{img}" alt="{t.replace('&amp;','and')}" loading="lazy" width="600" height="400"></div>
      <div class="bd"><span class="n">{n}</span><h3>{t}</h3><p>{d}</p></div></a>'''
 for u,n,t,d,img in LINES)

mx_head = "".join(f"<th>{c}</th>" for c in MCOLS)
mx_rows = "".join(
 "<tr><th>" + r[0] + "</th>" + "".join(f"<td>{dot(v)}</td>" for v in r[1:]) + "</tr>" for r in MATRIX)

faq_html = "".join(
 f'''<div class="qa rv"><button type="button" aria-expanded="false"><h3>{q}</h3><span class="pm"></span></button>
     <div class="ans"><div><p>{a}</p></div></div></div>''' for q,a in FAQ)

html = head(
 "QL Metal Fiber | Stainless Steel Fiber, Sintered Felt, Filter Elements & Oil Recovery",
 "Fujian QL Metal Fiber manufactures the full chain in-house: micron-scale stainless steel fiber from 2 µm, yarns, technical textiles, sintered filter media, filter elements and oil recovery systems. Samples and application testing before you commit.",
 "index.html",
 "metal fiber, stainless steel fiber, sintered metal fiber felt, metal filter element, knitted roller sleeve, conductive yarn, oil water separation, China manufacturer",
 SCHEMA) + header("") + f"""
<main>
<section class="hero dk">
  <div class="wrap">
    <div class="hero-grid">
      <div>
        <div class="eyebrow rv">Metal fiber, end to end</div>
        <h1 class="h-xl rv d1">When heat, chemistry or current <em>destroys</em> the material you use now, <mark>metal fiber holds.</mark></h1>
        <p class="lead rv d2">We draw stainless steel down to 2&nbsp;µm and build it into yarns, technical textiles, sintered media, filter elements and separation equipment — in our own plants, to your operating conditions.</p>
        <div class="hero-cta rv d3">
          <a class="btn btn-pri" href="applications.html">Find your application<svg><use href="#i-arrow"/></svg></a>
          <a class="btn btn-line" href="sample.html">Request a sample</a>
        </div>
      </div>
      <figure class="hero-fig rv d2" style="margin:0">
        <img src="img/film-poster.webp" alt="Metal fiber web being formed on the production line" width="1200" height="675">
      </figure>
    </div>

    <div class="stats">
      <div class="stat rv"><b class="num"><span data-count="2">2</span><sup>µm</sup></b><span>Finest fiber diameter we draw</span></div>
      <div class="stat rv d1"><b class="num"><span data-count="62">62</span><sup>pat.</sup></b><span>Granted patents, 16 of them inventions</span></div>
      <div class="stat rv d2"><b class="num"><span data-count="6">6</span><sup>std.</sup></b><span>National &amp; industry standards co-drafted</span></div>
      <div class="stat rv d3"><b class="num"><span data-count="600">600</span><sup>m³/h</sup></b><span>Largest oil recovery unit in service</span></div>
    </div>
  </div>
</section>

<div class="trust"><div class="wrap">
  <span class="chip"><i></i>Established <b>2002</b></span>
  <span class="chip"><i></i>NEEQ-listed <b>872336</b></span>
  <span class="chip"><i></i><b>ISO 9001</b> quality management</span>
  <span class="chip"><i></i>National High-Tech Enterprise</span>
  <span class="chip"><i></i>National &ldquo;Little Giant&rdquo; Enterprise</span>
  <span class="chip"><i></i>In-house SEM &amp; pore-size lab</span>
</div></div>

<section class="sec">
  <div class="wrap">
    <div class="sec-h">
      <div class="eyebrow rv">Application solutions</div>
      <h2 class="h-lg rv d1">Start from your process, not our catalogue.</h2>
      <p class="lead rv d2">Buyers rarely ask what products we have. They ask whether a material will survive their furnace temperature, their solvent, their precision requirement — and for how long. So we organise everything by the conditions you run.</p>
    </div>
    <div class="g3">{app_cards}</div>
    <p class="rv" style="margin-top:34px"><a class="tlink" href="applications.html">All application solutions, including co-development<svg class="i" style="width:14px;height:14px"><use href="#i-arrow"/></svg></a></p>
  </div>
</section>

<section class="sec alt">
  <div class="wrap">
    <div class="sec-h">
      <div class="eyebrow rv">Material capability map</div>
      <h2 class="h-lg rv d1">One material, seven forms, six properties.</h2>
      <p class="lead rv d2">Metal fiber is a platform, not a single product. The table shows which property each form is actually built for — useful when your requirement does not match a standard catalogue item.</p>
    </div>
    <div class="matrix rv"><div class="tbl-wrap"><table class="mx">
      <thead><tr><th style="text-align:left">Product form</th>{mx_head}</tr></thead>
      <tbody>{mx_rows}</tbody>
    </table></div></div>
    <div class="mx-key rv">
      <span><span class="dot"></span> Core property</span>
      <span><span class="dot o"></span> Achievable on request</span>
      <span><span class="dot n"></span> Not a primary use</span>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-h">
      <div class="eyebrow rv">Product lines</div>
      <h2 class="h-lg rv d1">From a 2&nbsp;µm filament to a 600&nbsp;m³/h skid.</h2>
      <p class="lead rv d2">Every step — drawing, sintering, spinning, weaving, element fabrication and equipment assembly — runs on our own lines, which is why specifications stay consistent batch to batch and customisation does not need a third party.</p>
    </div>
    <div class="lines">{line_cards}</div>
  </div>
</section>

<section class="sec alt">
  <div class="wrap">
    <div class="g2" style="gap:56px;align-items:start">
      <div>
        <div class="eyebrow rv">Why buyers test us first</div>
        <h2 class="h-lg rv d1" style="margin:16px 0 18px">Samples and data before you commit.</h2>
        <p class="lead rv d2">We would rather spend a sample than win an argument. Send the conditions, take the samples, run them on your own line — then decide.</p>
        <div class="cta-row rv d3">
          <a class="btn btn-dark" href="sample.html">Request a sample<svg><use href="#i-arrow"/></svg></a>
        </div>
      </div>
      <div class="rv d1">
        {''.join(f'''<div style="display:flex;gap:18px;padding:22px 0;border-top:1px solid var(--line)">
          <span class="num" style="font-size:12px;color:var(--muted-2);padding-top:4px">{i:02d}</span>
          <div><h3 class="h-md" style="font-size:18.5px;margin-bottom:7px">{t}</h3>
          <p style="color:var(--muted);font-size:14.6px;line-height:1.7">{d}</p></div></div>'''
          for i,(t,d) in enumerate([
            ("Everything made in-house","Fiber drawing, sintering, spinning, weaving, element fabrication and equipment assembly are all ours — so is the responsibility when something needs to change."),
            ("Testing you can check","In-house SEM, pore-size distribution, particle analysis and filtration rigs. We send the data with the sample, not instead of it."),
            ("Standards and patents behind it","Co-drafted 5 national and 1 industry standard; 62 granted patents including 16 inventions."),
            ("Proven at industrial scale","Sintered felt supplied to China's viscose and chemical-fibre industry; oil recovery systems running at leading nickel-cobalt hydrometallurgy producers, up to 600 m³/h per unit."),
          ],1))}
      </div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-h">
      <div class="eyebrow rv">Common questions</div>
      <h2 class="h-lg rv d1">Answers before the first email.</h2>
    </div>
    <div class="rv">{faq_html}</div>
    <p class="rv" style="margin-top:30px"><a class="tlink" href="resources.html">Full FAQ and downloads<svg class="i" style="width:14px;height:14px"><use href="#i-arrow"/></svg></a></p>
  </div>
</section>

{CTA_BAND}
</main>
""" + footer()

w("index.html", html)
