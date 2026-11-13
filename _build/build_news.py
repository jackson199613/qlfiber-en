# -*- coding: utf-8 -*-
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from layout import head, header, footer, w, CTA_BAND, crumb, page_hero, subnav, SUB_CO, SITE, COMPANY

POSTS=[
 dict(s="article-1", cat="Technical", date="2026-09-18", read="7 min",
  t="Absolute rating is not the whole specification",
  sum="Two media with the same 20 µm absolute rating can behave completely differently on the same line. What actually sets change-out interval is dirt-holding capacity, and that is a function of structure, not rating.",
  img="img/en-micro-gradient.webp", cap="Graded pore structure: coarse upstream, fine downstream",
  body=["<p>Buyers usually specify filtration media by absolute rating, because it is the one number that appears on every data sheet. It answers a real question — what is the largest particle that gets through — but it says nothing about how long the element will last before differential pressure forces a change.</p>",
   "<h3>Where the capacity comes from</h3>",
   "<p>Sintered metal fiber felt filters in depth rather than at a surface. Layers of decreasing fiber diameter are laid so that pore size falls from the upstream face to the downstream face. Coarse particles are captured near the surface, fine particles deeper in, and the whole thickness is doing work. A surface filter at the same rating uses only its face, so it blinds faster at the same solids load.</p>",
   "<h3>What to compare instead</h3>",
   "<p>Ask for four numbers together: absolute rating, porosity, thickness and bubble point. Porosity tells you how much void there is to fill; thickness tells you how much depth is available; bubble point confirms the largest pore and rises as the rating gets finer. Air permeability at 200 Pa then shows what that structure costs you in pressure drop.</p>",
   "<p>In our KIA3 series, moving from 10KIA3 to 60KIA3 takes bubble point from about 3700 Pa down to 620 Pa and air permeability from 110 up to 1200. The thickened KIA3K series holds the same rating at 1.1 mm instead of 0.3–0.7 mm — more depth, more capacity, a longer interval between changes at the same rating.</p>",
   "<h3>The practical test</h3>",
   "<p>If your pressure differential is rising too quickly, the answer is usually not a coarser rating — which would let more through — but more depth or a different gradient. Send us the current element, the rating you need to hold, the flow and the interval you are getting now.</p>"]),
 dict(s="article-2", cat="Application", date="2026-07-02", read="6 min",
  t="Recovering oil from extraction liquor without demulsifier",
  sum="In hydrometallurgical extraction, the non-dissolved oil fraction is what drives activated carbon and resin consumption downstream. Removing it physically turns a consumable cost into recovered organic phase.",
  img="img/en-micro-coalesce.webp", cap="Coalescence: droplets captured, grown and floated off",
  body=["<p>Oil in an extraction liquor comes in two forms. A dissolved fraction, typically 5 to 40 ppm depending on the extractant and the mixing regime, which needs deep treatment. And a non-dissolved fraction, dispersed and emulsified, which can be recovered physically.</p>",
   "<h3>Why the non-dissolved fraction matters most</h3>",
   "<p>It is the fraction that loads activated carbon and resin beds downstream. Treat it as a chemical problem and you pay twice: once for demulsifier, once for the sludge it creates. Treat it as a physical one and the organic phase goes back into the circuit.</p>",
   "<h3>How coalescence works here</h3>",
   "<p>Surface-modified metal fiber is oleophilic and hydrophobic. Fine oil droplets are captured on the fiber surface, collide and grow, and once large enough they rise and are drawn off at the top. No chemical is added at any point, so there is no chemical sludge to dispose of.</p>",
   "<h3>What it delivers in practice</h3>",
   "<p>Around 70% oil removal, with outlet oil content typically 5 to 30 mg/L. A 15 m³/h installation has run at that level for three years. The largest single unit in service handles 600 m³/h. Footprint is roughly one third to two thirds of the hourly throughput figure, and the coalescing element is not a routine consumable — our longest installation has run five years without replacement. In nickel-cobalt applications payback is typically one to two years.</p>",
   "<p>Systems can be trialled on your own liquor before a proposal is issued.</p>"]),
 dict(s="article-3", cat="Application", date="2026-05-14", read="5 min",
  t="Why glass tempering lines keep coming back to metal fiber",
  sum="Ceramic roller covers, toothed bar protection and hot bending mould covers all fail the same way: the fabric survives the temperature but not the combination of temperature, abrasion and marking.",
  img="img/en-glass.webp", cap="Knitted metal fiber sleeve on tempering rollers",
  body=["<p>A glass tempering line is an unforgiving test for a textile. The material has to hold 350 °C continuously with short peaks far above it, resist abrasion from glass moving across it, and — the part that eliminates most candidates — leave no mark on the glass surface.</p>",
   "<h3>What metal fiber changes</h3>",
   "<p>Because the fiber is drawn metal rather than a coated or metallised yarn, there is no coating to burn off or shed onto the glass. 316L is the standard material; FeCrAl is available where the duty is hotter. Products are heat-set, so under normal cutting and handling they do not fuzz.</p>",
   "<h3>Where it goes on the line</h3>",
   "<p>Elastic knitted sleeves in Φ35 to 60 mm cover ceramic rollers. Braided sleeves in Φ5 to 14 mm protect toothed bars and racks in chemical strengthening, where resistance to molten potassium nitrate matters as much as temperature. Woven cloth in plain 0.35 mm or twill 0.5 mm, up to 1500 mm wide, covers hot bending moulds. Tape, rope and damping felt handle the rest: suction cups, clamps, container pusher bars, earthing.</p>",
   "<h3>Trying it</h3>",
   "<p>There is no minimum order on most of these products, and reference FOB pricing is available — roughly USD 19.5 to 45 per metre for TGZ112 depending on diameter, and USD 1.05 to 2.55 per metre for TGBX113. A trial can be a single roller.</p>"]),
 dict(s="article-4", cat="Company", date="2026-03-20", read="3 min",
  t="Largest coalescing oil recovery unit to date enters service at 600 m³/h",
  sum="A single-train coalescing oil recovery system rated 600 m³/h is now operating on a nickel-cobalt extraction circuit, the largest capacity we have supplied in one unit.",
  img="img/fts-huayou-02.webp", cap="600 m³/h coalescing oil recovery system",
  body=["<p>The unit is a trough-type configuration, selected because floor space on the plant was limited and an existing clarifier trough could be used as the basis for the installation.</p>",
   "<h3>Why trough type at this scale</h3>",
   "<p>Tank-type systems are skid-mountable and suit flows up to about 30 m³/h. Above that, a trough configuration keeps the footprint compact — roughly one third to two thirds of the hourly throughput figure — and allows retrofit into an existing clarifier rather than a new civil structure.</p>",
   "<p>The system is purely physical: no demulsifier is added and no chemical sludge is created. Recovered organic phase returns to the circuit, and the load on downstream activated carbon and resin falls accordingly.</p>",
   "<p>Our installed base in this application includes leading nickel-cobalt hydrometallurgy producers in China. Customer names are not published without written consent.</p>"]),
 dict(s="article-5", cat="Technical", date="2026-01-28", read="6 min",
  t="Specifying a conductive thread by resistance, not by steel content",
  sum="Blend ratio is a manufacturing parameter. What your product actually needs is a resistance per metre, held within a tolerance, lot after lot.",
  img="img/prod-heatwire.webp", cap="Insulated metal fiber heating wire",
  body=["<p>Enquiries for conductive yarn often arrive specified as a percentage of stainless steel. It is a reasonable starting point, but it is not what determines whether a heated garment reaches temperature or a shielded fabric meets its attenuation target.</p>",
   "<h3>What to specify</h3>",
   "<p>Resistance per metre, and the tolerance you can live with. We hold 1 to 64 Ω/m, set by ply count and core count rather than by blend ratio alone. Fiber resistance at room temperature varies with the state of the stainless steel fiber, so if your product has a hard limit, state it at enquiry and we will test samples before qualification rather than after.</p>",
   "<h3>The other half of the specification</h3>",
   "<p>Hand, drape and sewability matter as much as the electrical value in a wearable product. Blend ratios from 0.5 to 100% steel are possible with aramid, polyester, PPS or cotton, and the right ratio is usually found by trial-spinning two or three candidates and letting your own process decide.</p>",
   "<p>Because the conductor is drawn metal rather than a plated layer, the electrical behaviour does not fade with washing, flexing or time — which is what makes the qualification worth doing once.</p>"]),
 dict(s="article-6", cat="Company", date="2025-11-12", read="3 min",
  t="QL Metal Fiber at FILTECH: what buyers asked about",
  sum="Three questions came up repeatedly at the show: cleanability, lot-to-lot consistency, and whether elements can be made to fit existing housings.",
  img="img/expo-filtech2024.webp", cap="FILTECH exhibition stand",
  body=["<p>Trade shows are a good sample of what the market is actually worried about. Three questions dominated our conversations.</p>",
   "<h3>Can it really be cleaned?</h3>",
   "<p>Yes — the structure is all metal and metallurgically bonded at every fiber contact, so back-flushing, ultrasonic and chemical cleaning all return it to service. This is the main economic difference from disposable media, and it is why the comparison should be made on cost per operating hour rather than on unit price.</p>",
   "<h3>How consistent is it between lots?</h3>",
   "<p>Every lot is measured for bubble point, permeability, efficiency, porosity, thickness and weight, and ships with an inspection report. We keep a retained sample so a later lot can be compared against the one you approved.</p>",
   "<h3>Will it fit our housings?</h3>",
   "<p>Pleated cartridges run Φ35 to 60 mm and 425 to 1250 mm long with end fittings made to your drawing. Because we make the media, the support mesh assembly and the element, rating, strength and fit are specified together rather than negotiated between suppliers.</p>"]),
]

CATS=sorted({p["cat"] for p in POSTS})

cards="".join(f'''<a class="post rv" href="{p["s"]}.html" data-tag="{p["cat"]}">
  <div class="im"><img src="{p["img"]}" alt="{p["t"]}" loading="lazy" width="600" height="400"></div>
  <div class="bd"><div class="pmeta"><span class="tg">{p["cat"]}</span><span>{p["date"]}</span><span>{p["read"]} read</span></div>
    <h3>{p["t"]}</h3><p>{p["sum"]}</p>
    <span class="more">Read<svg class="i" style="width:13px;height:13px"><use href="#i-arrow"/></svg></span></div></a>''' for p in POSTS)

sc=json.dumps({"@context":"https://schema.org","@type":"ItemList","name":"News & Blog",
 "itemListElement":[{"@type":"ListItem","position":i+1,"name":p["t"],"url":f'{SITE}/{p["s"]}.html'}
                    for i,p in enumerate(POSTS)]},ensure_ascii=False)

html = head("News & Blog — Metal Fiber Technical Articles | QL Metal Fiber",
  "Technical articles and company news on metal fiber filtration, coalescing oil recovery, glass processing textiles and conductive yarn.",
  "news.html","metal fiber blog, filtration technical article, oil recovery news", sc, "img/en-micro-gradient.webp"
 ) + header("company.html") + crumb([("Company","company.html"),("News & Blog",None)]) + page_hero(
  "05","NEWS &amp; BLOG","What we have learned, written down",
  "Technical notes from selection and trial work, and the occasional company announcement. No product launches dressed as articles.",
  None,"img/en-micro-gradient.webp") + subnav(SUB_CO,"news.html") + f"""
<main>
<section class="sec"><div class="wrap">
  <div class="pills rv" data-filter=".post">
    <button class="on" data-k="all">All</button>
    {"".join(f'<button data-k="{c}">{c}</button>' for c in CATS)}
  </div>
  <div class="posts">{cards}</div>
</div></section>
{CTA_BAND}
</main>
""" + footer()
w("news.html", html)

# ------------------------------------------------------------- article pages
for i,p in enumerate(POSTS):
    prev=POSTS[i-1] if i>0 else None
    nxt=POSTS[i+1] if i<len(POSTS)-1 else None
    sc=json.dumps({"@context":"https://schema.org","@type":"TechArticle" if p["cat"]!="Company" else "NewsArticle",
      "headline":p["t"],"description":p["sum"],"datePublished":p["date"],
      "image":f'{SITE}/{p["img"]}',"mainEntityOfPage":f'{SITE}/{p["s"]}.html',
      "author":{"@type":"Organization","name":COMPANY},
      "publisher":{"@type":"Organization","name":COMPANY,"logo":{"@type":"ImageObject","url":f"{SITE}/img/logo.png"}}},ensure_ascii=False)
    nav=""
    if prev or nxt:
        nav='<nav class="art-nav">' + (f'<a href="{prev["s"]}.html"><span>Previous</span><b>{prev["t"]}</b></a>' if prev else '<span></span>') + \
            (f'<a class="nx" href="{nxt["s"]}.html"><span>Next</span><b>{nxt["t"]}</b></a>' if nxt else '<span></span>') + '</nav>'
    html = head(f'{p["t"]} | QL Metal Fiber', p["sum"], f'{p["s"]}.html',
       "metal fiber, "+p["cat"].lower(), sc, p["img"]) + header("company.html") + \
       crumb([("Company","company.html"),("News & Blog","news.html"),(p["t"],None)]) + f"""
<main>
<article class="art">
  <header class="art-head wrap">
    <div class="pmeta rv"><span class="tg">{p["cat"]}</span><span>{p["date"]}</span><span>{p["read"]} read</span></div>
    <h1 class="h-lg rv d1">{p["t"]}</h1>
    <p class="lead rv d2">{p["sum"]}</p>
  </header>
  <figure class="art-fig wrap rv"><img src="{p["img"]}" alt="{p["cap"]}" width="1200" height="800"><figcaption>{p["cap"]}</figcaption></figure>
  <div class="wrap"><div class="prose art-body rv">{"".join(p["body"])}</div>
    <div class="note rv" style="max-width:760px;margin:40px auto 0">Values quoted apply to the stated test or operating conditions and are a basis for selection, not a performance warranty. Final suitability is established by a trial under your own conditions.</div>
    {nav}
  </div>
</article>
{CTA_BAND}
</main>
""" + footer()
    w(f'{p["s"]}.html', html)
