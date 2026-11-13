# -*- coding: utf-8 -*-
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from layout import (head, header, footer, w, CTA_BAND, crumb, page_hero, subnav,
                    SUB_APP, SITE)

def tbl(caption, heads, rows, note=""):
    th = "".join(f'<th{" class=\"num\"" if h.startswith("#") else ""}>{h.lstrip("#")}</th>' for h in heads)
    tr = "".join("<tr>" + "".join(
        f'<td{" class=\"num\"" if str(c).startswith("#") else ""}>{str(c).lstrip("#")}</td>' for c in r) + "</tr>"
        for r in rows)
    n = f'<p class="tnote">{note}</p>' if note else ""
    return (f'<div class="rv"><div class="tbl-wrap"><table class="spec"><caption>{caption}</caption>'
            f'<thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>{n}</div>')

def bullets(items):
    return '<ul>' + "".join(f'<li>{i}</li>' for i in items) + '</ul>'

APPS = [
dict(f="a-glass.html", idx="01", en="GLASS PROCESSING", bg="img/sleeve-03.webp",
 h1="Roller sleeves and textiles that outlive the furnace cycle",
 lead="For tempering, bending and forming lines: heat-resistant metal fiber sleeves, fabrics, tapes and ropes that keep glass surfaces clean and cut the cost of stopping a furnace to change consumables.",
 kpis=[("1100","°C","Short-term peak rating"),("350","°C","Continuous service"),("0","MOQ","No minimum order")],
 buyers="Physical tempering furnace OEMs and parts suppliers · architectural and automotive glass processors · electronic and chemically strengthened glass plants · container glass works",
 conds="Ceramic rollers in physical tempering furnaces (350–1100 °C), molten potassium nitrate in chemical strengthening, hot bending moulds, suction cups and clamps, container pusher bars",
 products="TGZ112 elastic knitted sleeve · TGBX112 / TGBX113 braided sleeve · metal fiber woven cloth and tape · high-temperature rope · damping felt",
 verify="Send samples for a live furnace trial, then compare service life and glass surface quality",
 problems=[
  "Roller sleeves have a short service life, and every change means furnace downtime and labour.",
  "Aged sleeves crack, powder or shed fibers, leaving scratches or imprints on the glass surface.",
  "Molten potassium nitrate in chemical strengthening furnaces attacks the toothed bars and rack protection.",
  "Different furnace types and roller diameters need different sizes, and suppliers struggle to adapt.",
  "Imported consumables are expensive, lead times are long, and stock pressure is high."],
 prio=[("A","Physical tempering furnace OEMs and parts suppliers; architectural and automotive glass processors","Sleeves are a continuously consumed item, and an OEM can carry volume into every machine it ships"),
       ("B","Electronic glass and chemically strengthened glass plants","Higher technical threshold and unit value; braided sleeves hold a clear advantage against molten salt"),
       ("C","Container glass works and decorative glass shops","Pusher-bar covers and mould needs are scattered, so they sit alongside the main accounts")],
 combo=[("Ceramic roller protection in physical tempering","TGZ112 elastic knitted sleeve, Φ35 / 50 / 55 / 60 mm, rated 350–1100 °C","316L stainless steel fiber knitted for elasticity; grips the roller closely, presents a smooth lint-free surface, and does not crack or powder at end of life"),
        ("Toothed bars and rack protection in chemical strengthening","TGBX112 / TGBX113 braided sleeve, Φ5–14 mm; metal fiber tape wrapping","Resists nitrate, sulphuric acid, dilute hydrochloric acid, alkali and salt corrosion; stays intact over long service"),
        ("Hot bending mould covers for automotive glass","Metal fiber woven cloth — plain 0.35 mm / twill 0.5 mm, widths 1000 / 1200 / 1500 mm; metal fiber tape","Breathable, ductile and heat resistant; reduces forming marks"),
        ("Suction cup and clamp cushioning","High-temperature metal fiber damping felt, 2–3 mm thick","Three-dimensional porous structure damps vibration, rated 350–1100 °C, resists ageing"),
        ("Container pusher bars and sealing","High-temperature metal fiber rope, Φ1–12 mm, square or round","Abrasion and shear resistant with a smooth surface")],
 terms=["No minimum order quantity — we can supply by the metre so a single furnace can be trialled first.",
        "Indicative FOB: TGZ112 approximately USD 19.5–45 / m depending on tube diameter; TGBX113 approximately USD 1.05–2.55 / m; TGBX112 quoted by tube diameter.",
        "Sizes are made to your furnace type, roller diameter and temperature requirement; matched kits can be supplied to furnace OEMs."],
 checks=["Service life and change interval at the same furnace temperature.",
         "Whether scratches, imprints and optical defects on the glass surface are reduced.",
         "How closely the sleeve fits, how easily it installs, and how consistent the sizing is."],
 pitch="Roller sleeves that crack, shed fibers or mark the glass cost you downtime and rejected panels. QL's TGZ112 elastic knitted sleeves are made from 316L stainless steel fiber, rated 350–1100 °C, fit snugly around ceramic rollers and keep a smooth, lint-free surface without cracking or dusting at end of life. For chemical tempering, our TGBX braided sleeves resist molten potassium nitrate, acids and alkalis. No minimum order — tell us your furnace type and roller diameter and we will send matching samples.",
 sell="Rated to 1100 °C, lint-free and non-marking — fewer furnace stops and fewer rejected panels.",
 gal=[("img/sleeve-03.webp","Tempering line in operation"),("img/sleeve-04.webp","Sleeved rollers on the line"),
      ("img/sh-sleeve.webp","Braided metal fiber sleeve"),("img/yarn-glassbelt.webp","Metal fiber woven tape")]),

dict(f="a-filtration.html", idx="02", en="FILTRATION & SEPARATION", bg="img/fts-huayou-02.webp",
 h1="Cleanable all-metal media, and oil recovery without chemicals",
 lead="For polymer melt, viscose, hot gas and solvent extraction: sintered metal fiber media that can be washed and reused, and coalescing oil recovery that turns a consumable cost into recovered organic phase.",
 kpis=[("10","–60 µm","Absolute filtration rating"),("30","MPa","Max working pressure"),("600","m³/h","Largest unit in service")],
 buyers="Polyester, viscose and film plants · petrochemical and fine chemical works · filter housing manufacturers · nickel-cobalt and copper-cobalt hydrometallurgy plants · high-temperature dust removal contractors",
 conds="High-temperature, high-viscosity polymer melt; viscose dope; high-pressure hydraulic and fuel oil; 300–600 °C flue gas; oil removal from extraction liquor",
 products="Sintered metal fiber felt · pleated cartridges · sintered mesh · high-temperature metal filter bags · oil recovery systems",
 verify="Filtration testing, material analysis, trial cartridges, on-site trial of an oil recovery unit",
 problems=[
  "Differential pressure across the melt or process-liquid filter rises quickly, elements are changed often, and downtime is expensive.",
  "Organic and paper media do not survive the temperature or the chemistry, and fail early in hot service.",
  "Imported metal media is expensive with long lead times, and buyers worry whether a domestic alternative can hold the rating and the consistency.",
  "Emulsified and dispersed oil in extraction liquor is hard to remove; activated carbon consumption and hazardous waste disposal are costly.",
  "Retrofit projects are short of floor space and want equipment that is compact and simple to run."],
 prio=[("A","Polyester, viscose and film plants; nickel-cobalt hydrometallurgy","Conditions overlap closely with our existing applications, consumption is high and repeat purchase is stable"),
       ("B","Petrochemical and fine chemical works; filter housing makers and distributors","Product fit is good, and they can enter as a media supplier into existing housings"),
       ("C","High-temperature dust removal contractors; copper-cobalt and lithium projects","Longer project cycles, followed up as a second phase")],
 combo=[("Polymer melt and viscose filtration","KIA3 / KIA3K / KIC4 sintered felt, 10–60 µm absolute, porosity 72–86%; pleated elements","Multi-layer graded pores give high dirt-holding capacity, slow pressure rise, and the media can be back-washed and regenerated"),
        ("High-pressure hydraulic and process-liquid filtration","Pleated cartridges Φ35–60 mm, length 425–1250 mm, max working pressure 30 MPa; sintered mesh 2–100 µm","Pressure resistant, temperature resistant and suitable for in-line back-flushing"),
        ("High-temperature gas and dust filtration","High-temperature metal filter bags and needled metal fiber media, rated 350–1000 °C, porosity above 90%","Graded fiber layers hold low emissions over long periods and clean down easily"),
        ("Oil removal and recovery from extraction liquor","Tank-type oil recovery (≤30 m³/h), trough-type systems, retrofit of existing troughs; largest unit in service 600 m³/h","Purely physical coalescence with no demulsifier; the recovered oil goes straight back into the process and the coalescing element lasts for years"),
        ("Precision filtration packages","Precision filter housings, basket strainers, pleated / wound / melt-blown elements, mist eliminators, ceramic membranes","Combined with metal media to supply a single filtration package")],
 terms=["Media is quoted by the sheet, elements by the piece, and equipment is priced per project to your specification.",
        "Oil recovery systems can be trialled on your conditions before a proposal is issued.",
        "Filtration testing, material property analysis and trial elements are available to support qualification."],
 checks=["Whether filtration rating, bubble point, air permeability and dirt-holding capacity meet the duty.",
         "How far performance recovers after cleaning, and how many regeneration cycles the media takes.",
         "Oil removal rate, outlet oil content, footprint and running cost of the recovery system."],
 pitch="Struggling with fast pressure build-up, frequent filter changes or costly oil removal in your solvent-extraction circuit? QL manufactures sintered metal fiber felts (10–60 µm absolute), pleated metal filter cartridges rated up to 30 MPa, and high-temperature metal filter bags — all cleanable and reusable. For hydrometallurgy, our coalescing oil recovery systems remove emulsified and dispersed oil physically, without demulsifiers, and let you reuse the recovered organic phase. Send us your process conditions and we will recommend a configuration and arrange filtration testing.",
 sell="All-metal media you can wash and reuse, plus chemical-free oil recovery — filtration and oil removal stop being a pure consumable.",
 gal=[("img/fts-huayou-02.webp","Oil recovery system, 600 m³/h"),("img/fts-bamo-02.webp","Trough-type system, 160 m³/h"),
      ("img/sh-cartridge.webp","Pleated metal fiber cartridge"),("img/sh-felt.webp","Sintered metal fiber felt")]),

dict(f="a-emi.html", idx="03", en="EMI SHIELDING & ANTI-STATIC", bg="img/ind-emi.webp",
 h1="Conductivity that does not wash out",
 lead="100% metal conductive fiber for anti-static and shielding products — supplied as tow, blended yarn, chopped fiber, conductive thread, braided sleeve and woven tape, in every form your process already runs.",
 kpis=[("0.5","–100%","Steel content in blended yarn"),("1","–64 Ω/m","Conductive thread resistance"),("2","µm","Finest fiber diameter")],
 buyers="Anti-static and shielding fabric mills · non-woven producers · conductive plastics compounders · shielding gasket and cable protection suppliers · anti-static brush and earthing component makers",
 conds="Static elimination in flammable and explosive environments, electronic equipment shielding, cable screening, conductive compounds",
 products="Metal fiber blended yarn · conductive thread · fiber tow · chopped fiber · braided sleeve · woven tape and cloth",
 verify="Small-lot trial spinning, trial weaving, trial compounding, resistance and shielding effectiveness testing",
 problems=[
  "Coated or plated conductive materials lose conductivity after washing and abrasion.",
  "Conductive fiber disperses poorly when blended with ordinary fiber, and spins badly.",
  "Shielding materials degrade in high-temperature and corrosive environments.",
  "A stable resistance range is needed to meet the product standard."],
 prio=[("A","Anti-static and shielding fabric mills; non-woven producers","Volume is steady, and tow or blended yarn can go straight onto the machine"),
       ("B","Conductive plastics compounders; shielding gasket and cable protection suppliers","Chopped fiber and braided sleeve match their needs closely"),
       ("C","Anti-static brush and earthing component makers","Demand is fragmented and sits alongside the main accounts")],
 combo=[("Anti-static and shielding fabric","Pre-blended fiber tow and blended yarn — stainless steel content 0.5–100%, blendable with aramid, polyester, PPS or cotton","Good spinnability and dispersion; steel content is matched to the anti-static or shielding class required"),
        ("Anti-static non-wovens","Fiber tow and chopped fiber","Used as the conductive raw material in non-woven webs"),
        ("Conductive plastic masterbatch","Chopped fiber, length 1–38 mm","Disperses in the polymer matrix and carries both current and heat"),
        ("Cable and equipment shielding","Braided sleeve, metal fiber woven cloth, conductive thread (1–64 Ω/m)","Durable shielding, flexible and bendable, corrosion resistant"),
        ("Equipment earthing and static elimination","Metal fiber woven tape, anti-static brush fiber","Heat resistant, flame retardant and electrically stable")],
 terms=["Quoted by specification, by weight or by the metre; small-lot trial spinning and trial weaving are supported.",
        "Blend ratio, fiber length, yarn count and twist are set to your process.",
        "If you need a resistance limit, state it at enquiry — fiber resistance at room temperature varies with the state of the stainless steel fiber, so we recommend testing samples before qualification."],
 checks=["Whether resistance and shielding effectiveness meet the target, and the retention rate after washing.",
         "Spinnability on your machines, end-break rate and weaving efficiency.",
         "Resistance consistency between batches."],
 pitch="If your conductive fabrics lose performance after washing, the problem is usually the conductive layer, not the fabric. QL supplies 100% stainless steel fibers in every form you need — blended tow, blended yarn (0.5–100% steel content with aramid, polyester, PPS or cotton), chopped fiber for conductive compounds, conductive thread (1–64 Ω/m) and braided sleeves. Because the conductor is pure metal, anti-static and shielding performance does not fade with washing. We can blend to your ratio and send trial yarn for your machines.",
 sell="Pure metal conductive fiber — anti-static and shielding performance does not fade with washing.",
 gal=[("img/ind-emi.webp","Shielded enclosure and cabinets"),("img/yarn-fabric.webp","Metal fiber woven cloth"),
      ("img/sh-yarn.webp","Blended metal fiber yarn"),("img/sh-belt.webp","Metal fiber woven tape")]),

dict(f="a-specialty.html", idx="04", en="SPECIALTY MATERIALS", bg="img/sh-felt.webp",
 h1="Where ceramics crack and foams give up",
 lead="Metal fiber formed into porous plates, burner media, sintered felts and damping mats — for surface combustion, gas distribution, thermal shock, vibration and precision gas duties that ordinary porous materials cannot hold.",
 kpis=[("50","–90%","Porosity, by design"),("1100","°C","Peak service rating"),("2","–3 mm","Damping felt thickness")],
 buyers="Burner and thermal equipment makers · exhaust treatment and catalyst substrate producers · water-electrolysis hydrogen equipment makers · industrial vibration, noise control and high-temperature sealing component makers",
 conds="Surface combustion, high-temperature gas distribution, thermal shock, vibration and noise, high-temperature corrosive filtration",
 products="Metal fiber porous plate · metal burner plate · sintered felt · damping felt · specialty fibers including PBO",
 verify="Sample testing, bench testing, small-batch machine build",
 problems=[
  "Ceramic porous materials are brittle, take thermal shock badly and have a short life.",
  "Burner surface temperature is uneven, with flashback or local overheating.",
  "Damping and sound-absorbing materials age and fail in high-temperature environments.",
  "A specific porosity, thickness or shape is required, and standard parts cannot meet it."],
 prio=[("A","Burner and thermal equipment makers","Metal burner plates and porous plates are mature applications"),
       ("B","Exhaust treatment and catalyst substrate producers; industrial vibration and noise control component makers","Porous plates and damping felts match their requirements closely"),
       ("C","Water-electrolysis hydrogen equipment makers","An emerging requirement, co-developed to the equipment specification")],
 combo=[("Surface combustion and thermal processing","Metal burner plate in FeCrAl, NiCrFe, titanium or stainless steel fiber","Even radiating surface, fast response and tolerant of extreme temperature swings"),
        ("Gas distribution and fluidisation","Metal fiber porous plate, porosity 50–90% by design","Three-dimensional open-pore structure, weldable and machinable, resists thermal shock without fracturing"),
        ("Exhaust treatment and catalyst substrates","Porous plate, sintered porous media, chopped fiber","Heat resistant and able to carry catalyst"),
        ("Damping, sound absorption and high-temperature cushioning","Damping felt 2–3 mm thick, rated 350–1100 °C; needled felt","High damping, ageing resistant and free of outgassing in vacuum"),
        ("Gas diffusion layers for hydrogen production","Titanium or nickel fiber felt","Co-developed to the equipment maker's specification"),
        ("High-strength heat-resistant fibers","PBO and aramid specialty fibers","Complementing high-temperature conveyor belts, sewing thread and protective materials")],
 terms=["Shape, thickness, porosity and alloy are made to your drawing or sample.",
        "Build samples for bench or rig testing first, then move to small-batch supply."],
 checks=["Porosity, flow resistance and integrity after thermal shock.",
         "Uniformity of the combustion surface temperature and service life.",
         "Damping and sound absorption, and performance retention after high-temperature ageing."],
 pitch="When ceramics crack under thermal shock and foams lose strength, metal fiber offers a different answer. QL sinters micron-scale metal fibers into porous plates (50–90% porosity by design), burner media in FeCrAl, Inconel, titanium or stainless steel, and damping felts rated 350–1100 °C. They can be cut, welded and shaped to your drawing. Share your operating conditions and we will propose a material, build samples and support your bench testing.",
 sell="The strength of metal with the flexibility and porosity of a fiber — built for heat and thermal shock.",
 gal=[("img/sh-felt.webp","Sintered metal fiber felt"),("img/micro-network.webp","Three-dimensional fiber network"),
      ("img/sh-pad.webp","Metal fiber damping element"),("img/media-02.webp","Sintered media and mesh")]),

dict(f="a-automotive.html", idx="05", en="AUTOMOTIVE", bg="img/ind-auto.webp",
 h1="From glass forming to heated seats, one material family",
 lead="Metal fiber components across the automotive chain — bending mould covers, insulated heating wire, chopped fiber for friction materials, sintered porous media for exhaust treatment and hydraulic filtration.",
 kpis=[("1","–64 Ω/m","Heating wire resistance options"),("30","MPa","Hydraulic element rating"),("12","µm","Monofilament diameter")],
 buyers="Automotive glass forming plants · seat heating and wiring harness suppliers · brake pad makers · exhaust after-treatment and hydraulic component manufacturers",
 conds="Automotive glass hot bending, seat and steering-wheel heating, friction materials, diesel exhaust treatment, hydraulic system filtration",
 products="Metal fiber woven cloth · insulated heating wire · chopped fiber · sintered porous media · hydraulic elements",
 verify="Sample trial, bench testing, component qualification",
 problems=[
  "Hot bending mould cover materials have a short life, and forming marks affect the appearance of the glass.",
  "Heating wire resistance is unstable, heat is uneven, and wires break after repeated flexing.",
  "Friction materials and exhaust treatment components need heat- and wear-resistant reinforcing fiber.",
  "Component suppliers need materials that stay stable and batch-consistent over a long programme."],
 prio=[("A","Automotive glass forming plants","Shares products with the glass processing solution, so it is the fastest entry point"),
       ("B","Seat heating and wiring harness suppliers; brake pad makers","Insulated heating wire and chopped fiber match their needs closely"),
       ("C","Exhaust after-treatment and hydraulic component makers","Long qualification cycles, pursued in a second phase")],
 combo=[("Hot bending mould covers for automotive glass","Metal fiber woven cloth — plain or twill — and metal fiber tape","Heat resistant, breathable and ductile; reduces forming marks"),
        ("Seat and steering-wheel heating","Insulated heating wire and metal fiber thread","Stable resistance and even heat; the insulation allows the wire to be sewn directly and survive repeated bending"),
        ("Friction materials","Chopped metal fiber","Reinforces the matrix, conducts heat away and improves high-temperature stability"),
        ("Exhaust after-treatment","Sintered porous media and porous plate","Heat resistant and able to act as a catalyst substrate"),
        ("Hydraulic and lubrication filtration","Pleated elements and metal mesh sintered elements","High-pressure capable and suitable for back-flushing")],
 terms=["We support the sample qualification process used by component suppliers, and provide material parameters and test data.",
        "Heating wire resistance, wire diameter and insulation material are specified to your design."],
 checks=["Service life of the mould cover fabric and the appearance pass rate of the glass.",
         "Resistance tolerance, flex cycles and insulation performance of the heating wire.",
         "Batch consistency and long-term supply capability."],
 pitch="From bending moulds for automotive glass to heated seats and friction materials, metal fiber does jobs that ordinary fibers cannot. QL supplies stainless steel fiber fabrics for glass bending mould covers, insulated heating wire with stable resistance for seat and steering-wheel heating, chopped fiber for friction materials, and sintered porous media for exhaust treatment. Tell us your part and specification — we will match the material and support your validation.",
 sell="From glass forming to seat heating — stable metal fiber materials that improve component consistency.",
 gal=[("img/ind-auto.webp","Seat heating layer"),("img/prod-heatwire.webp","Insulated heating wire"),
      ("img/yarn-fabric.webp","Metal fiber woven cloth"),("img/sh-cartridge.webp","Hydraulic filter element")]),

dict(f="a-textiles.html", idx="06", en="FUNCTIONAL TEXTILES & SMART WEARABLES", bg="img/ind-wear.webp",
 h1="Conductive and heating yarns your machines already accept",
 lead="Weavable, sewable and washable metal fiber yarns and insulated heating wires — so apparel brands and contract manufacturers can add heating, conductivity and protection without changing their weaving or sewing process.",
 kpis=[("1","–64 Ω/m","Resistance options"),("12","µm","Monofilament diameter"),("100","%","Steel content available")],
 buyers="Electric heating apparel, heated blanket and glove brands and contract manufacturers · smart garment developers · anti-static and live-line workwear makers · cut-resistant and protective product makers",
 conds="Low-voltage heating, signal transmission, static protection, shielding for live-line work",
 products="Metal fiber thread · insulated heating wire · blended yarn · conductive sewing thread",
 verify="Small-lot trial weaving, trial sewing, wash and flex testing",
 problems=[
  "Heating is uneven, with local overheating affecting safety and comfort.",
  "Conductive thread breaks or drifts in resistance after repeated flexing and washing.",
  "Conductive materials are hard to run on standard sewing and knitting machines.",
  "Multiple resistance grades are needed to match different battery designs."],
 prio=[("A","Electric heating apparel, heated blanket and heated glove manufacturers","Insulated heating wire and metal fiber thread are mature applications with real volume"),
       ("B","Anti-static and live-line workwear makers","Blended yarn covers everything from anti-static to high-level shielding"),
       ("C","Smart garment developers","Project-based and low volume, pursued as a technical partnership")],
 combo=[("Heated apparel, blankets and gloves","Insulated heating wire and metal fiber thread — 12 µm monofilament, multiple ply counts, 1–64 Ω/m","Stable resistance and even heat; the insulation lets the wire be sewn directly and survive flexing and washing"),
        ("Signal routing in smart garments","Metal fiber thread and insulated wire","Soft, durable and electrically stable"),
        ("Anti-static workwear","Blended yarn, 0.5–5% stainless steel content","Anti-static performance does not decline with washing"),
        ("High-voltage live-line workwear","Blended yarn, 20–100% stainless steel content","Shields the electric field, with steel content matched to the protection class"),
        ("Conductive sewing","Conductive sewing thread and heat-resistant sewing thread","No joints, and it runs straight on the machine")],
 terms=["Specified by resistance, wire diameter, ply count and insulation material; small-lot trial sewing is supported.",
        "We can supply samples and parameters to fit a brand's product development cycle."],
 checks=["Resistance tolerance and heating uniformity.",
         "Resistance retention after wash and flex cycles.",
         "Machine efficiency in sewing and weaving."],
 pitch="Heated jackets, gloves and blankets fail when the heating element drifts, breaks or overheats. QL's stainless steel fiber yarns and insulated heating wires deliver stable resistance (1–64 Ω/m options), even heat and long flex and wash life — and they run on standard sewing and weaving equipment. For workwear, our blended yarns provide anti-static and shielding performance that lasts through washing. Tell us your voltage and heating layout and we will recommend a resistance and send samples.",
 sell="Weavable, sewable, washable conductive and heating yarn — safer, longer-lasting wearables.",
 gal=[("img/ind-wear.webp","Heating layout in a garment lining"),("img/yarn-heatpad.webp","Metal fiber heating panel"),
      ("img/prod-heatwire.webp","Insulated heating wire"),("img/sh-yarn.webp","Blended metal fiber yarn")]),
]

for a in APPS:
    sc = json.dumps({"@context":"https://schema.org","@type":"WebPage","name":a["h1"],
                     "description":a["lead"],"url":f'{SITE}/{a["f"]}'}, ensure_ascii=False)
    quick = tbl("Solution at a glance", ["Item","Detail"], [
        ("Target buyers", a["buyers"]), ("Typical conditions", a["conds"]),
        ("Lead products", a["products"]), ("How it is verified", a["verify"])])
    prio = tbl("Where we start", ["Priority","Buyer type","Why"],
               [(f'<b>{p}</b>', b, r) for p,b,r in a["prio"]])
    combo = tbl("Candidate products and selection logic", ["Application","Candidate products","Selection logic"],
                a["combo"])
    gal = '<div class="gal rv">' + "".join(
        f'<figure><img src="{u}" alt="{c}" loading="lazy" width="600" height="450"><figcaption>{c}</figcaption></figure>'
        for u,c in a["gal"]) + '</div>'
    html = head(f'{a["h1"]} | {a["en"].title()} Solutions — QL Metal Fiber',
                a["lead"], a["f"],
                f'{a["en"].lower()}, metal fiber, stainless steel fiber, QL Metal Fiber', sc, a["bg"]) \
        + header("applications.html") \
        + crumb([("Applications","applications.html"), (a["en"].title(), None)]) \
        + page_hero(a["idx"], a["en"], a["h1"], a["lead"], a["kpis"], a["bg"]) \
        + subnav(SUB_APP, a["f"]) + f"""
<main>
<section class="sec"><div class="wrap">
  <div class="g2" style="gap:56px;align-items:start">
    <div class="prose rv">
      <p class="lede">{a["sell"]}</p>
      <h3>What this solution is for</h3>
      {bullets(a["problems"])}
    </div>
    <div class="rv d1">{quick}</div>
  </div>
</div></section>

<section class="sec alt tight"><div class="wrap">
  <div class="sec-h"><div class="eyebrow rv">Priority order</div>
    <h2 class="h-md rv d1" style="margin-top:14px">Who we serve first, and why</h2></div>
  {prio}
</div></section>

<section class="sec"><div class="wrap">
  <div class="sec-h"><div class="eyebrow rv">Product fit</div>
    <h2 class="h-md rv d1" style="margin-top:14px">Candidate products and selection logic</h2>
    <p class="lead rv d2">Candidates are a starting point. Final suitability depends on your exact conditions, so we confirm it with samples and testing rather than on paper.</p></div>
  {combo}
</div></section>

<section class="sec alt"><div class="wrap">
  <div class="g2" style="gap:56px;align-items:start">
    <div class="prose rv"><h3 style="margin-top:0">How we work together</h3>{bullets(a["terms"])}</div>
    <div class="prose rv d1"><h3 style="margin-top:0">What buyers verify</h3>{bullets(a["checks"])}</div>
  </div>
  <div class="note rv" style="margin-top:34px">{a["pitch"]}</div>
</div></section>

<section class="sec"><div class="wrap">
  <div class="sec-h"><div class="eyebrow rv">In service</div>
    <h2 class="h-md rv d1" style="margin-top:14px">Products and applications</h2></div>
  {gal}
</div></section>

{CTA_BAND}
</main>
""" + footer()
    w(a["f"], html)

print(f"应用方案 {len(APPS)} 页完成")
