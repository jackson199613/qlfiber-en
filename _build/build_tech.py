# -*- coding: utf-8 -*-
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from layout import head, header, footer, w, CTA_BAND, crumb, page_hero, subnav, SUB_TECH, SITE

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

# ---------------------------------------------------------------- R&D Overview
TEAM=[("Chairman &amp; Chief Engineer","Master's degree, Central South University. More than 30 years in metal fiber and filtration. Lead drafter of national standards; Fujian Province Class C high-level talent; deputy secretary-general of the national screening and sieving standardisation committee and a filtration and separation expert with the Chemical Industry and Engineering Society of China."),
      ("Deputy General Manager, R&amp;D","Formerly senior engineer and associate professor at Central South University. Responsible for sintered felt development, production and technical sales."),
      ("General Manager","Bachelor's degree, Changsha University of Science and Technology; assistant engineer. Oversees operations and customer projects."),
      ("Materials Researcher","Master's degree in materials processing engineering. Published in SCI and EI indexed journals; works on fiber forming and sintering."),
      ("Market &amp; Project Manager","Master's degree in non-ferrous metallurgy. Bridges process conditions on site and material selection in the laboratory.")]

PARTNERS=["Longyan University","Minjiang University","Inner Mongolia University of Technology",
  "China Machinery Institute of Standardization","Anhui University of Science and Technology",
  "Huangpu Institute of Materials, Guangdong–Hong Kong–Macao Greater Bay Area","Xiamen University",
  "Industrial Technology Research Institute, Jimei University","Tongji University",
  "Minxi Vocational and Technical College","Xiamen University of Technology"]

PROJECTS=[("2026","Provincial","High-efficiency metal coalescing oil removal equipment"),
  ("2023","Provincial","Flexible functional materials for smart wearables"),
  ("2020","Provincial","Electromagnetic shielding metal fiber fabric, with the Ningbo Institute of Materials Technology, Chinese Academy of Sciences"),
  ("2019","Provincial","Joint industry–university research on metal fiber forming")]

html = head("R&D Overview — Metal Fiber Research and Development | QL Metal Fiber",
  "A five-person core R&D team, eleven university and institute partnerships, four provincial research projects, and a laboratory that tests every material we propose.",
  "technology.html","metal fiber R&D, materials research, China metal fiber manufacturer",
  json.dumps({"@context":"https://schema.org","@type":"WebPage","name":"R&D Overview","url":f"{SITE}/technology.html"},ensure_ascii=False),
  "img/lab-wide-01.webp") + header("technology.html") + crumb([("Technology","technology.html"),("R&D Overview",None)]) + page_hero(
  "01","TECHNOLOGY","We develop the material, not just the part",
  "Metal fiber behaviour is set long before a part is made — at the drawing die, the web, the sintering cycle. That is where our research sits, and it is why we can change a property rather than only select from a catalogue.",
  [("5","","Core R&D engineers"),("11","","University and institute partners"),("4","","Provincial research projects")],
  "img/lab-wide-01.webp") + subnav(SUB_TECH,"technology.html") + f"""
<main>
<section class="sec"><div class="wrap">
  <div class="g2" style="gap:56px;align-items:start">
    <div class="prose rv">
      <p class="lede">Most filtration and shielding problems are not solved by choosing a different catalogue number. They are solved by changing something upstream — the alloy, the filament diameter distribution, the way the web is laid, the sintering temperature and time, or the surface state of the fiber.</p>
      <p>Because we draw the fiber, form the web, sinter it and build the finished element in our own plants, those variables are ours to change. A customer requirement that does not match a standard product becomes a development project rather than a refusal.</p>
      <h3>What we work on</h3>
      <ul>
        <li><b>Fiber forming.</b> Bundle drawing to 2 µm, alloy range from 316L and 304 to FeCrAl, nickel-based alloys, copper and titanium.</li>
        <li><b>Graded structures.</b> Multi-layer webs where pore size falls through the thickness, for high dirt-holding at a fixed absolute rating.</li>
        <li><b>Surface modification.</b> Oleophilic and hydrophobic treatment of fiber for coalescing oil recovery.</li>
        <li><b>Conductive textiles.</b> Blend ratio, ply construction and insulation for heating and shielding applications with a specified resistance per metre.</li>
        <li><b>Sintering and joining.</b> Vacuum sintering cycles, lamination with support mesh, welding and pleating of finished media.</li>
      </ul>
    </div>
    <div class="rv d1">{spec("Core R&D team", ["Role","Background"], [(t,b) for t,b in TEAM])}</div>
  </div>
</div></section>

<section class="sec alt"><div class="wrap">
  <div class="sec-h"><div class="eyebrow rv">Co-development</div>
    <h2 class="h-lg rv d1" style="margin-top:14px">From your conditions to a <em>qualified</em> material</h2>
    <p class="lead rv d2" style="margin-top:16px">Our development work runs on the customer's own duty, not on an internal roadmap. The sequence below is how almost every new product at QL has started.</p></div>
  <div class="rv">{rows([
    ("Step 1","Operating conditions","Medium and chemistry, temperature in service and at peak, pressure and differential pressure, flow, particle size and load, cycle and cleaning regime, and the installation envelope."),
    ("Step 2","Material selection","One or two candidate constructions, with the trade-off between them stated — usually rating against pressure drop, or conductivity against hand and drape."),
    ("Step 3","Prototype and laboratory test","Samples made on production equipment, then measured in house: bubble point, permeability, filtration efficiency, porosity, resistance, metallography."),
    ("Step 4","Field trial","Samples on your line, under your conditions. Most textile products carry no minimum order, so a trial is not a commercial commitment."),
    ("Step 5","Small-batch validation","A short run under the agreed specification, with inspection data for every lot."),
    ("Step 6","Series supply and iteration","Full supply with lot reports, and continued adjustment as your process changes."),
  ])}</div>
</div></section>

<section class="sec"><div class="wrap">
  <div class="g2" style="gap:56px;align-items:start">
    <div class="rv">{spec("Provincial research projects", ["Year","Level","Subject"], PROJECTS)}</div>
    <div class="prose rv d1">
      <div class="eyebrow">Industry–university research</div>
      <h2 class="h-md" style="margin:14px 0 18px">Eleven standing partnerships</h2>
      <p>Joint research with universities and institutes gives us access to characterisation equipment and modelling capability that a company of our size would not otherwise hold, and it keeps our standards work grounded in published method.</p>
      <ul class="tags">{"".join(f"<li>{p}</li>" for p in PARTNERS)}</ul>
    </div>
  </div>
</div></section>

{CTA_BAND}
</main>
""" + footer()
w("technology.html", html)

# ---------------------------------------------------------------- Lab & Testing
TESTS=[("Bubble point","Largest pore in the medium","ISO 4003 principle","Pa"),
  ("Air permeability","Flow at a stated differential pressure","At 200 Pa","L/min/dm²"),
  ("Filtration efficiency","Retention at a stated particle size","Gravimetric and particle count","%"),
  ("Porosity","Void fraction of the structure","Gravimetric","%"),
  ("Thickness and weight","Dimensional consistency","Contact gauge","mm, g/m²"),
  ("Tensile and burst strength","Mechanical limit of the medium and element","Tensile tester","N, MPa"),
  ("Electrical resistance","Resistance per metre of thread or per square of fabric","Four-point probe","Ω/m, Ω/sq"),
  ("Metallography and SEM","Fiber diameter, bonding, layer structure","Microscopy","µm"),
  ("Corrosion exposure","Behaviour in the customer's medium","Immersion, customer medium","—")]

html = head("Lab & Testing — In-house Metal Fiber Testing | QL Metal Fiber",
  "Bubble point, permeability, filtration efficiency, porosity, resistance and metallography, measured in our own laboratory on every material we propose.",
  "lab.html","metal fiber testing, bubble point, filtration efficiency test, SEM",
  json.dumps({"@context":"https://schema.org","@type":"WebPage","name":"Lab & Testing","url":f"{SITE}/lab.html"},ensure_ascii=False),
  "img/lab-wide-01.webp") + header("technology.html") + crumb([("Technology","technology.html"),("Lab & Testing",None)]) + page_hero(
  "02","LAB &amp; TESTING","Every claim on this site has a measurement behind it",
  "We test in house because a buyer qualifying a new supplier needs numbers that can be repeated — and because a material we cannot measure is a material we cannot improve.",
  [("9","","Standard test methods in house"),("100","%","Lots with an inspection report"),("1","–3 days","Typical sample lead time")],
  "img/lab-wide-01.webp") + subnav(SUB_TECH,"lab.html") + f"""
<main>
<section class="sec"><div class="wrap">
  <div class="sec-h"><div class="eyebrow rv">Test capability</div>
    <h2 class="h-lg rv d1" style="margin-top:14px">What we can measure</h2>
    <p class="lead rv d2" style="margin-top:16px">These are the tests we run routinely, on development samples and on production lots. If your qualification protocol calls for a method we do not hold, we will say so and arrange a third-party laboratory.</p></div>
  <div class="rv">{spec("In-house test methods", ["Test","What it tells you","Method basis","Unit"], TESTS,
    "Values reported for a material apply to the stated test conditions. They are a basis for selection and comparison, not a performance warranty for your process.")}</div>
</div></section>

<section class="sec alt"><div class="wrap">
  <div class="g2" style="gap:56px;align-items:start">
    <div class="prose rv">
      <div class="eyebrow">Sampling and qualification</div>
      <h2 class="h-md" style="margin:14px 0 18px">How a trial usually runs</h2>
      <p>Stock samples ship in one to three days; freight is normally collect. Made-to-order samples follow the development schedule agreed for the project. Most of our technical textile products carry no minimum order, so you can buy a trial length rather than commit to a batch.</p>
      <p>For a qualification we will send the test report for the exact lot supplied, state which values are typical and which are measured, and keep a retained sample so that a later lot can be compared against the one you approved.</p>
      <h3>What we ask for</h3>
      <ul>
        <li>The medium, including anything corrosive or abrasive in it</li>
        <li>Temperature in normal service and at peak, and how long the peak lasts</li>
        <li>Pressure, differential pressure and the point at which you change the element</li>
        <li>Flow rate, particle size distribution and solids load</li>
        <li>Cleaning or regeneration regime, if the part is reused</li>
        <li>Dimensions and fittings, or a drawing</li>
      </ul>
    </div>
    <div class="rv d1">{gal([("img/lab-op-01.webp","Data acquisition at the instrument workstation"),("img/lab-op-02.webp","Reading results from an analyser"),("img/sem-felt-02.webp","Fiber network, micrograph"),("img/sem-felt-01.webp","Graded pore structure through the thickness")])}</div>
  </div>
</div></section>

<section class="sec"><div class="wrap">
  <div class="sec-h"><div class="eyebrow rv">Instruments</div>
    <h2 class="h-lg rv d1" style="margin-top:14px">What we measure it <em>with</em></h2>
    <p class="lead rv d2" style="margin-top:16px">Our own instruments, photographed as they stand. Where a qualification calls for a method we do not hold, we say so and arrange a third-party laboratory rather than substitute a different one.</p></div>
  <div class="g2" style="gap:48px;align-items:start">
    <div class="rv">
      <figure class="eqfig"><img src="img/sem-screen.webp" alt="Metal fiber morphology and EDS spectrum on the SEM workstation" loading="lazy" width="1400" height="933">
        <figcaption><b>Morphology and composition, in one session</b>The electron microscope reads filament diameter, how fibers overlap and the quality of each sintered bond directly; the energy-dispersive spectrum alongside it identifies the elements present.</figcaption></figure>
    </div>
    <div class="rv d1">
      <div class="eqlist">
        <div class="eq"><img src="img/eq-sem.webp" alt="KYKY-EM8000F scanning electron microscope" loading="lazy" width="1200" height="800">
          <div><h4>Scanning electron microscope</h4><span class="mod">KYKY-EM8000F</span>
            <p>Filament diameter and its distribution, three-dimensional fiber network, sintered bond quality, and the graded layer structure seen in cross-section.</p></div></div>
        <div class="eq"><img src="img/eq-afs.webp" alt="GGX-810 atomic fluorescence spectrometer" loading="lazy" width="1200" height="800">
          <div><h4>Atomic fluorescence spectrometer</h4><span class="mod">GGX-810</span>
            <p>Metallic element content, used to confirm alloy grade, control impurities and verify incoming wire.</p></div></div>
        <div class="eq"><img src="img/eq-sem-col.webp" alt="Electron column and detectors" loading="lazy" width="1200" height="800">
          <div><h4>Electron column and detectors</h4><span class="mod">SE / BSE</span>
            <p>Secondary-electron imaging for surface topography, backscattered imaging for compositional contrast.</p></div></div>
        <div class="eq"><img src="img/sem-sample.webp" alt="Specimen loaded into the SEM chamber" loading="lazy" width="1200" height="800">
          <div><h4>Specimen preparation</h4><span class="mod">Chamber loading</span>
            <p>How fiber and felt are cut, mounted and made conductive decides image quality — and whether two lots can honestly be compared.</p></div></div>
      </div>
    </div>
  </div>
</div></section>

<section class="sec"><div class="wrap">
  <div class="sec-h"><div class="eyebrow rv">Reports on file</div>
    <h2 class="h-lg rv d1" style="margin-top:14px">Already tested, already issued</h2>
    <p class="lead rv d2" style="margin-top:16px">Taking metal fiber thread as the example, these reports exist today and can be supplied with a quotation or a qualification file. Most were issued by independent laboratories; where a document exists only in Chinese, we provide a certified English summary on request.</p></div>
  <div class="rv">{spec("Metal fiber thread — reports held", ["Report","What it covers","Issued by","Language"], [
    ("RoHS four substances<br><span class=\"sub\">1000×3 / 275×3 / 100×3</span>","Lead, cadmium, mercury and hexavalent chromium against the RoHS limits, 16 May 2026","CTI (Centre Testing International)","EN on request"),
    ("Material test report<br><span class=\"sub\">275×3, 316L</span>","Grade chemical composition, 22 May 2026","CTI (Centre Testing International)","<b>English original available</b>"),
    ("Tensile test<br><span class=\"sub\">275×3</span>","Tensile strength and elongation at break","Shanghai Fuda Testing Technology Group","CN"),
    ("Resistance before and after washing","Change in electrical resistance across wash cycles — the durability evidence behind conductive thread","Standard Testing Group","CN"),
    ("Far-infrared performance","Far-infrared emissivity, to GB/T 30127-2013, for heating and functional textile use","Independent laboratory","CN"),
    ("Infrared reflectance spectrum<br><span class=\"sub\">275×3</span>","Reflectance behaviour across the infrared band","Shanghai Fuda Testing Technology Group","CN"),
    ("Magnetic properties<br><span class=\"sub\">100×3</span>","Magnetic characterisation, for shielding and special-duty selection","Shanghai Fuda Testing Technology Group","CN"),
  ], "Reports for other product lines are issued to order or commissioned from a third-party laboratory. Values apply to the sample and conditions stated in each report.")}</div>
  <div class="note rv" style="margin-top:30px">The 316L material report and the RoHS report are on the <a class="tlink" href="downloads.html">Downloads</a> page and can be taken straight away. The rest we send on request so that the document matches the grade you are qualifying.</div>
</div></section>

<section class="sec alt"><div class="wrap">
  <div class="sec-h"><div class="eyebrow rv">The laboratory</div>
    <h2 class="h-lg rv d1" style="margin-top:14px">Where the numbers come from</h2></div>
  <div class="labgal bento rv">
    <figure class="big"><img src="img/lab-wide-01.webp" alt="Materials and application laboratory" loading="lazy" width="2000" height="1333"><figcaption>Materials and application laboratory</figcaption></figure>
    <figure><img src="img/lab-chem-02.webp" alt="Analytical balances and reagent bench" loading="lazy" width="1200" height="800"><figcaption>Analytical balances and reagents</figcaption></figure>
    <figure><img src="img/lab-chem-03.webp" alt="Titration and colorimetric analysis area" loading="lazy" width="1200" height="800"><figcaption>Titration and colorimetry</figcaption></figure>
  </div>
  <div class="labgal rv" style="margin-top:14px">
    <figure><img src="img/lab-chem-01.webp" alt="Fume hood and sample preparation" loading="lazy" width="1200" height="800"><figcaption>Fume hood and sample preparation</figcaption></figure>
    <figure><img src="img/lab-chem-04.webp" alt="Chemical analysis bench" loading="lazy" width="1200" height="800"><figcaption>Chemical analysis bench</figcaption></figure>
    <figure><img src="img/lab-wide-02.webp" alt="Clean area of the laboratory" loading="lazy" width="2000" height="1333"><figcaption>Clean area</figcaption></figure>
  </div>
</div></section>

{CTA_BAND}
</main>
""" + footer()
w("lab.html", html)

# ---------------------------------------------------------------- Patents & Standards
STD=[("National standard","Metal fiber sintered felt — specification and test methods","Lead drafter"),
  ("National standard","Metal fiber — terminology and classification","Participating drafter"),
  ("Industry standard","Sintered metal fiber filter element","Participating drafter"),
  ("Industry standard","Metal fiber porous material — permeability test","Participating drafter"),
  ("Industry standard","Metal fiber textiles for high-temperature service","Participating drafter"),
  ("Group standard","Coalescing oil removal equipment for extraction liquor","Lead drafter")]

html = head("Patents & Standards — 62 Patents, 6 Standards | QL Metal Fiber",
  "62 granted and pending patents, 16 of them inventions, and participation in six national, industry and group standards for metal fiber materials and equipment.",
  "patents.html","metal fiber patents, national standard, industry standard",
  json.dumps({"@context":"https://schema.org","@type":"WebPage","name":"Patents & Standards","url":f"{SITE}/patents.html"},ensure_ascii=False),
  "img/lab-chem-03.webp") + header("technology.html") + crumb([("Technology","technology.html"),("Patents & Standards",None)]) + page_hero(
  "03","PATENTS &amp; STANDARDS","Where our know-how is written down",
  "Intellectual property matters to a buyer for one practical reason: it shows the supplier owns the process rather than copying it, and that the specification you qualify will still exist in five years.",
  [("62","","Patents granted and pending"),("16","","Invention patents"),("6","","Standards co-drafted")],
  "img/lab-chem-03.webp") + subnav(SUB_TECH,"patents.html") + f"""
<main>
<section class="sec"><div class="wrap">
  <div class="g2" style="gap:56px;align-items:start">
    <div class="prose rv">
      <p class="lede">Our patent portfolio covers 62 granted and pending patents, 16 of which are invention patents. They cluster in four areas: fiber forming and bundle drawing, graded sintered structures, surface-modified coalescing media, and the equipment built around them.</p>
      <p>Our chairman is the lead drafter of national standards for metal fiber sintered felt and serves as deputy secretary-general of the national screening and sieving standardisation committee, and as a filtration and separation expert with the Chemical Industry and Engineering Society of China. Standards work is slow and unglamorous, but it is the reason our test reports read the same way a buyer's own laboratory would write them.</p>
      <div class="note">Patent and standard numbers can be supplied on request for a qualification file. Some documents are in Chinese only; we will provide a certified English summary where one is needed.</div>
    </div>
    <div class="rv d1">{spec("Standards participation", ["Level","Subject","Our role"], STD)}</div>
  </div>
</div></section>

<section class="sec alt"><div class="wrap">
  <div class="sec-h"><div class="eyebrow rv">Recognition</div>
    <h2 class="h-lg rv d1" style="margin-top:14px">Qualifications that a purchasing department can verify</h2></div>
  <div class="rv">{rows([
    ("Quality","ISO 9001 quality management system","Certified; certificate and scope available for your supplier file."),
    ("Status","National High-Tech Enterprise","Recognised at national level, subject to periodic re-assessment."),
    ("Status","National specialised and sophisticated &ldquo;Little Giant&rdquo; enterprise","Awarded to SMEs with a defined technical niche and a national-level position in it."),
    ("Listing","NEEQ 872336","Publicly listed on the National Equities Exchange and Quotations, with audited annual reports."),
    ("Equipment","Provincial first-of-its-kind major technical equipment","Recognition held by our coalescing oil recovery system."),
  ])}</div>
</div></section>

{CTA_BAND}
</main>
""" + footer()
w("patents.html", html)
