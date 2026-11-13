# -*- coding: utf-8 -*-
import sys, os, json, datetime
sys.path.insert(0, os.path.dirname(__file__))
from layout import head, header, footer, w, crumb, SITE, COMPANY, ADDR, MAIL, NAV

PAGES=[("Home","index.html","Brand positioning, key figures, products, applications and enquiry."),
 ("Products","products.html","Product line navigation and the material capability matrix."),
 ("Metal Fiber & Yarn","p-fiber.html","Bundle-drawn fiber, chopped fiber, tow and spun yarn."),
 ("Sintered Felt & Media","p-felt.html","Graded-pore sintered metal fiber felt and media."),
 ("Technical Textiles & Sleeves","p-textile.html","Knitted, braided and woven metal fiber goods."),
 ("Filter Elements","p-element.html","Pleated cartridges, mesh elements and high-temperature bags."),
 ("Oil Recovery Systems","p-equipment.html","Coalescing oil–water separation for extraction circuits."),
 ("Product Detail Template","p-detail.html","Specification, media, applications, FAQ, downloads and enquiry."),
 ("Applications","applications.html","Industry navigation and co-development."),
 ("Glass Processing","a-glass.html","Roller covers, toothed bar protection and mould covers."),
 ("Filtration & Separation","a-filtration.html","Polymer melt, viscose, gas and hydraulic filtration."),
 ("EMI Shielding & Anti-static","a-emi.html","Shielding fabric, anti-static textiles and earthing."),
 ("Specialty Materials","a-specialty.html","Burners, hydrogen equipment, damping and acoustics."),
 ("Automotive","a-automotive.html","Seat, steering wheel and battery-adjacent heating."),
 ("Functional Textiles","a-textiles.html","Heated apparel, smart wearables and conductive thread."),
 ("R&D Overview","technology.html","Team, development method and research partnerships."),
 ("Lab & Testing","lab.html","In-house test methods and the qualification process."),
 ("Patents & Standards","patents.html","62 patents, six standards and recognitions."),
 ("Company Profile","company.html","Who we are, the four divisions and the plant."),
 ("History","history.html","Milestones from 2002."),
 ("Manufacturing","manufacturing.html","The eight process steps from wire to element."),
 ("Quality & Certifications","quality.html","ISO 9001, control plan and lot reports."),
 ("News & Blog","news.html","Technical articles and company news."),
 ("FAQ","resources.html","Answers on materials, filtration, textiles and working with us."),
 ("Downloads","downloads.html","Catalogues, data sheets and certificates on request."),
 ("Contact Us","contact.html","Enquiry form, address and direct contact."),
 ("Request a Sample","sample.html","Sample request form and how a trial runs."),
 ("Search","search.html","Site search."),
 ("Privacy Policy","privacy.html","How we handle the data you send us."),
 ("Sitemap","sitemap.html","Every page on this site.")]

# ------------------------------------------------------------------- Sitemap
groups=[("Home",PAGES[0:1]),("Products",PAGES[1:8]),("Applications",PAGES[8:15]),
        ("Technology",PAGES[15:18]),("Company",PAGES[18:23]),("Resources",PAGES[23:25]),
        ("Contact",PAGES[25:27]),("Utility",PAGES[27:])]
cols="".join(f'''<div class="smg rv"><h3>{g}</h3><ul>''' +
  "".join(f'<li><a href="{u}">{t}</a><span>{d}</span></li>' for t,u,d in items) + '</ul></div>'
  for g,items in groups)
html = head("Sitemap | "+COMPANY, "Every page on the QL Metal Fiber English site: product lines, application solutions, technology, company, resources and contact.", "sitemap.html"
 ) + header("") + crumb([("Sitemap",None)]) + f"""
<main><section class="sec" style="padding-top:70px"><div class="wrap">
  <div class="eyebrow rv">Sitemap</div>
  <h1 class="h-lg rv d1" style="margin:18px 0 44px">Every page on this site</h1>
  <div class="smgrid">{cols}</div>
</div></section></main>
""" + footer()
w("sitemap.html", html)

# ------------------------------------------------------------------- Privacy
SEC=[("What this policy covers","This policy explains what happens to the information you send us through this website — the enquiry form, the sample request form, or a direct email to the address published here. It does not cover other websites we link to."),
 ("What we collect","Only what you type into a form and what your message contains: your name, company, work email, country, role and product area if you choose them, and the description of your requirement. Our hosting provider also records standard technical data such as IP address and browser type for security and traffic statistics."),
 ("Why we use it","To answer your enquiry, prepare a quotation, arrange samples and keep a record of the technical conversation so that a later lot can be matched to what you approved. If you ask for a document, we use your email to send it and to tell you when that document is revised."),
 ("What we do not do","We do not sell your details, and we do not pass them to third parties for marketing. Information is shared outside our company only where it is necessary to fulfil your request — for example a courier needs the shipping address on a sample request."),
 ("Analytics","We use Google Analytics to understand which pages are read and from which countries. It sets cookies in your browser. You can block them in your browser settings or with a browser extension without affecting the rest of the site."),
 ("How long we keep it","Enquiry correspondence is kept while the commercial relationship is live and for as long as a technical record may be needed to support a product you have qualified. You can ask us to delete it at any time."),
 ("Your rights","Write to us and we will tell you what we hold about you, correct it, or delete it. If you are in a jurisdiction that grants specific data rights, such as the EU or the UK, we will handle your request under those rules."),
 ("Changes","If this policy changes we will update this page and the date below."),
 ("Contact","Questions about this policy, or a request about your data, go to "+f'<a class="tlink" href="mailto:{MAIL}">{MAIL}</a>'+f", or by post to {COMPANY}, {ADDR}.")]
body="".join(f"<h3>{t}</h3><p>{b}</p>" for t,b in SEC)
html = head("Privacy Policy | "+COMPANY,"How QL Metal Fiber handles the information you send through this website.","privacy.html"
 ) + header("") + crumb([("Privacy Policy",None)]) + f"""
<main><section class="sec" style="padding-top:70px"><div class="wrap">
  <div class="eyebrow rv">Legal</div>
  <h1 class="h-lg rv d1" style="margin:18px 0 22px">Privacy policy</h1>
  <div class="prose rv d1" style="max-width:760px">{body}
    <p class="tnote" style="margin-top:34px">Last updated {datetime.date.today().isoformat()}. This policy is provided in good faith and in plain language; it is not legal advice, and we recommend your own counsel reviews it before you rely on it for a regulated market.</p>
  </div>
</div></section></main>
""" + footer()
w("privacy.html", html)

# -------------------------------------------------------------------- Search
idx=[{"t":t,"u":u,"d":d} for t,u,d in PAGES]
html = head("Search | "+COMPANY,"Search the QL Metal Fiber site by material, property or industry — fiber, sintered felt, sleeves, filter elements and oil recovery systems.","search.html"
 ) + header("") + crumb([("Search",None)]) + f"""
<main><section class="sec" style="padding-top:70px"><div class="wrap" style="max-width:860px">
  <div class="eyebrow rv">Search</div>
  <h1 class="h-lg rv d1" style="margin:18px 0 26px">Search this site</h1>
  <form class="sform rv d1" role="search" onsubmit="return false">
    <svg class="si"><use href="#i-search"/></svg>
    <input id="q" type="search" placeholder="Try &quot;sintered felt&quot;, &quot;sleeve&quot;, &quot;oil removal&quot;, &quot;resistance&quot;" autocomplete="off" autofocus>
  </form>
  <div id="sres" class="rows" style="margin-top:34px"></div>
  <p id="snone" class="tnote" hidden>Nothing matched. Try a material, a property or an industry — or <a class="tlink" href="contact.html">ask an engineer</a>.</p>
</div></section></main>
<script>
var IDX={json.dumps(idx,ensure_ascii=False)};
(function(){{var q=document.getElementById('q'),r=document.getElementById('sres'),n=document.getElementById('snone');
function run(){{var v=q.value.trim().toLowerCase();r.innerHTML='';if(!v){{n.hidden=true;return;}}
var hit=IDX.filter(function(p){{return (p.t+' '+p.d).toLowerCase().indexOf(v)>-1;}});
n.hidden=hit.length>0;
hit.forEach(function(p){{var a=document.createElement('a');a.className='row-i';a.href=p.u;
a.innerHTML='<div><h4>'+p.t+'</h4><p>'+p.d+'</p></div>';r.appendChild(a);}});}}
q.addEventListener('input',run);
var m=location.search.match(/[?&]q=([^&]*)/);if(m){{q.value=decodeURIComponent(m[1].replace(/\\+/g,' '));run();}}}})();
</script>
""" + footer()
w("search.html", html)

# ----------------------------------------------------------------------- 404
html = head("Page not found | "+COMPANY,"That page does not exist. Find metal fiber product lines, application solutions and contact details, or search the QL Metal Fiber site.","404.html") + header("") + f"""
<main><section class="sec" style="padding:150px 0 130px"><div class="wrap" style="max-width:640px">
  <div class="eyebrow rv">Error 404</div>
  <h1 class="h-lg rv d1" style="margin:18px 0 18px">That page is <em>not here</em>.</h1>
  <p class="lead rv d2">The link may be out of date, or the address mistyped. The product lines and applications are the fastest way back in — or search the site.</p>
  <div class="cta-row rv d3" style="margin-top:34px">
    <a class="btn btn-dark" href="index.html">Back to home<svg><use href="#i-arrow"/></svg></a>
    <a class="btn btn-line" href="search.html">Search</a>
  </div>
  <div class="rows rv d3" style="margin-top:50px">
    <a class="row-i" href="products.html"><div><h4>Products</h4><p>Five product lines, from fiber to finished system.</p></div></a>
    <a class="row-i" href="applications.html"><div><h4>Applications</h4><p>Six industries, each with its own selection logic.</p></div></a>
    <a class="row-i" href="contact.html"><div><h4>Contact</h4><p>Send your operating conditions and we will reply within a working day.</p></div></a>
  </div>
</div></section></main>
""" + footer()
w("404.html", html)
