# -*- coding: utf-8 -*-
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from layout import (head, header, footer, w, crumb, page_hero, subnav, SUB_CON,
                    SITE, COMPANY, ADDR, MAIL, TEL, CN_SITE)

def field(name,label,typ="text",req=True,ph="",half=False,opts=None,rows_=0):
    r=' required' if req else ''
    star='<i>*</i>' if req else ''
    if opts is not None:
        ctl=f'<select name="{name}" id="{name}"{r}>'+"".join(f'<option value="{o}">{o}</option>' for o in opts)+'</select>'
    elif rows_:
        ctl=f'<textarea name="{name}" id="{name}" rows="{rows_}" placeholder="{ph}"{r}></textarea>'
    else:
        ctl=f'<input type="{typ}" name="{name}" id="{name}" placeholder="{ph}"{r}>'
    return f'<div class="f{"" if half else " full"}"><label for="{name}">{label}{star}</label>{ctl}</div>'

ASIDE=f'''<aside class="aside rv d1">
  <h4>Direct contact</h4>
  <p><a href="mailto:{MAIL}">{MAIL}</a><br>{TEL}<br>WeChat / WhatsApp on the same number</p>
  <p class="small">We reply within one working day, Monday to Friday, GMT+8.</p>
  <h4>Head office and plant</h4>
  <p>{COMPANY}<br>{ADDR}</p>
  <h4>Useful links</h4>
  <p><a href="products.html">Product lines</a><br><a href="applications.html">Applications</a><br>
     <a href="downloads.html">Downloads</a><br><a href="{CN_SITE}" rel="noopener">Chinese website</a></p>
</aside>'''

ASKCARDS=[("Operating conditions","Medium, temperature in service and at peak, pressure and differential pressure, flow. These decide the alloy and the structure before anything else."),
 ("Particles and load","Particle size distribution and solids load, if the duty is filtration. This is what sets dirt-holding capacity and change-out interval."),
 ("Dimensions or a drawing","Element length and diameter, sleeve diameter, cloth width, or the housing you need to fit. A sketch is enough to start."),
 ("What you use now","The current product and why it is being replaced — life, pressure drop, marking, cost. The fastest route to a useful proposal.")]
cards="".join(f'<div class="card rv"><h4>{t}</h4><p>{b}</p></div>' for t,b in ASKCARDS)

FORM_NOTE='<p class="fnote">Fields marked <i>*</i> are required. What you send is used to answer your enquiry and is not shared with third parties. See our <a href="privacy.html">privacy policy</a>.</p>'

# --------------------------------------------------------------------- Contact
sc=json.dumps({"@context":"https://schema.org","@type":"ContactPage","name":"Contact",
 "url":f"{SITE}/contact.html","mainEntity":{"@type":"Organization","name":COMPANY,
 "email":MAIL,"telephone":TEL,"address":{"@type":"PostalAddress","streetAddress":ADDR,
 "addressLocality":"Longyan","addressRegion":"Fujian","addressCountry":"CN"}}},ensure_ascii=False)

html = head(f"Contact — Talk to an Engineer | {COMPANY}",
 "Send your operating conditions and our engineers will recommend a configuration, quote it and arrange samples. Reply within one working day.",
 "contact.html","contact metal fiber manufacturer, metal fiber supplier China", sc, "img/inq-yarn.webp"
 ) + header("contact.html") + crumb([("Contact","contact.html"),("Contact Us",None)]) + page_hero(
 "01","CONTACT","Tell us the duty, not the part number",
 "The fastest enquiries are the ones that describe the conditions. Give us the medium, the temperature, the pressure and the flow, and the first reply will already contain a candidate material.",
 None,"img/inq-yarn.webp") + subnav(SUB_CON,"contact.html") + f"""
<main>
<section class="sec"><div class="wrap">
  <div class="form-wrap">
    <form class="form rv" name="enquiry" method="POST" data-netlify="true" netlify-honeypot="bot-field" action="thanks.html">
      <input type="hidden" name="form-name" value="enquiry">
      <p hidden><label>Do not fill this in: <input name="bot-field"></label></p>
      <div class="fgrid">
        {field("name","Your name",half=True)}
        {field("company","Company",half=True)}
        {field("email","Work email","email",half=True)}
        {field("country","Country / region",half=True)}
        {field("role","Your role",req=False,half=True,opts=["","Engineering","Purchasing","Quality","R&D","Management","Distribution","Other"])}
        {field("product","Product area",req=False,half=True,opts=["","Metal fiber & yarn","Sintered felt & media","Technical textiles & sleeves","Filter elements","Oil recovery systems","Not sure yet"])}
        {field("message","What do you need",req=True,rows_=7,ph="Medium and chemistry, temperature in service and at peak, pressure and differential pressure, flow, particle size and load, cleaning regime, dimensions or a drawing, and what you use now.")}
      </div>
      <div class="fconsent"><label><input type="checkbox" name="consent" required> I agree that my details may be used to answer this enquiry, as described in the <a href="privacy.html">privacy policy</a>.</label></div>
      <button class="btn btn-pri" type="submit">Send enquiry<svg><use href="#i-arrow"/></svg></button>
      {FORM_NOTE}
    </form>
    {ASIDE}
  </div>
</div></section>

<section class="sec alt"><div class="wrap">
  <div class="sec-h"><div class="eyebrow rv">What we ask for, and why</div>
    <h2 class="h-lg rv d1" style="margin-top:14px">Four things that decide the answer</h2></div>
  <div class="cards4">{cards}</div>
</div></section>
</main>
""" + footer()
w("contact.html", html)

# ---------------------------------------------------------------- Sample page
html = head(f"Request a Sample — Metal Fiber, Felt, Sleeves | {COMPANY}",
 "Stock samples ship in one to three days. Most technical textile products carry no minimum order, so a trial can be a single length.",
 "sample.html","metal fiber sample, sintered felt sample, free sample",
 json.dumps({"@context":"https://schema.org","@type":"WebPage","name":"Request a Sample","url":f"{SITE}/sample.html"},ensure_ascii=False),
 "img/sh-felt.webp") + header("contact.html") + crumb([("Contact","contact.html"),("Request a Sample",None)]) + page_hero(
 "02","REQUEST A SAMPLE","Test it on your own line",
 "A specification argued on paper is slower than a sample on a machine. Stock samples ship in one to three days, freight normally collect, and most technical textile products carry no minimum order.",
 [("1","–3 days","Stock sample lead time"),("0","MOQ","On most textile products"),("1","working day","Typical reply time")],
 "img/sh-felt.webp") + subnav(SUB_CON,"sample.html") + f"""
<main>
<section class="sec"><div class="wrap">
  <div class="form-wrap">
    <form class="form rv" name="sample" method="POST" data-netlify="true" netlify-honeypot="bot-field" action="thanks.html">
      <input type="hidden" name="form-name" value="sample">
      <p hidden><label>Do not fill this in: <input name="bot-field"></label></p>
      <div class="fgrid">
        {field("name","Your name",half=True)}
        {field("company","Company",half=True)}
        {field("email","Work email","email",half=True)}
        {field("country","Country / region",half=True)}
        {field("product","Product of interest",half=True,opts=["Metal fiber & yarn","Sintered felt & media","Technical textiles & sleeves","Filter elements","Oil recovery systems","Not sure — advise me"])}
        {field("spec","Grade or size, if known",req=False,half=True,ph="e.g. 20KIA3, Φ50 mm sleeve, 10 µm cartridge")}
        {field("conditions","Operating conditions",req=True,rows_=5,ph="Medium, temperature in service and at peak, pressure and differential pressure, flow, particle size and load, cleaning regime.")}
        {field("address","Shipping address",req=True,rows_=3,ph="Company, street, city, postcode, country — and a contact phone number for the courier.")}
      </div>
      <div class="fconsent"><label><input type="checkbox" name="consent" required> I agree that my details may be used to process this sample request, as described in the <a href="privacy.html">privacy policy</a>.</label></div>
      <button class="btn btn-pri" type="submit">Request sample<svg><use href="#i-arrow"/></svg></button>
      {FORM_NOTE}
    </form>
    {ASIDE}
  </div>
</div></section>

<section class="sec alt"><div class="wrap">
  <div class="sec-h"><div class="eyebrow rv">How a trial runs</div>
    <h2 class="h-lg rv d1" style="margin-top:14px">From request to qualification</h2></div>
  <div class="rows rv">
    <div class="row-i"><div class="dt">Day 1</div><div><h4>Enquiry and selection</h4><p>We read the conditions, propose one or two candidates and explain the trade-off between them.</p></div></div>
    <div class="row-i"><div class="dt">Day 1–3</div><div><h4>Sample dispatch</h4><p>Stock samples ship, freight normally collect. Made-to-order samples follow the agreed development schedule.</p></div></div>
    <div class="row-i"><div class="dt">Your trial</div><div><h4>Test on your line</h4><p>Under your own conditions. We will tell you in advance what to watch — usually pressure drop, life, marking or resistance.</p></div></div>
    <div class="row-i"><div class="dt">After</div><div><h4>Adjust or qualify</h4><p>If the trial misses, we change the structure rather than the catalogue number. If it holds, we move to small-batch validation with lot reports.</p></div></div>
  </div>
</div></section>
</main>
""" + footer()
w("sample.html", html)

# ---------------------------------------------------------------- Thanks page
html = head("Thank you | "+COMPANY, "Your message has been received. A QL Metal Fiber engineer will reply within one working day, Monday to Friday, GMT+8.", "thanks.html") + header("") + f"""
<main><section class="sec" style="padding:150px 0 130px"><div class="wrap" style="max-width:640px">
  <div class="eyebrow rv">Received</div>
  <h1 class="h-lg rv d1" style="margin:18px 0 18px">Thank you — your message is <em>with us</em>.</h1>
  <p class="lead rv d2">An engineer will reply within one working day, Monday to Friday, GMT+8. If your enquiry is urgent, email <a class="tlink" href="mailto:{MAIL}">{MAIL}</a> directly.</p>
  <div class="cta-row rv d3" style="margin-top:34px">
    <a class="btn btn-dark" href="index.html">Back to home<svg><use href="#i-arrow"/></svg></a>
    <a class="btn btn-line" href="products.html">Browse products</a>
  </div>
</div></section></main>
""" + footer()
w("thanks.html", html)
