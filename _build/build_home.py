# -*- coding: utf-8 -*-
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from layout import head, header, footer, w, CTA_BAND, film_block, SITE, COMPANY, MAIL, TEL, ADDR

APPS = [
 ("a-glass.html","Glass Processing","Lead track",
  "Roller sleeves, braided sleeves and woven belts that take 1100&nbsp;°C, stay lint-free and leave no marks on the glass.",
  "img/en-glass.webp"),
 ("a-filtration.html","Filtration &amp; Separation","Highest value per account",
  "Cleanable, reusable all-metal media for polymer melt, viscose and hot gas — plus chemical-free oil recovery for solvent extraction.",
  "img/en-filtration.webp"),
 ("a-emi.html","EMI Shielding &amp; Anti-static","Broadest coverage",
  "Conductivity comes from the fiber itself, not a coating, so anti-static and shielding performance survives repeated washing.",
  "img/en-emi.webp"),
 ("a-specialty.html","Specialty Materials","",
  "Porous plates, burner media and damping felts where ceramics crack under thermal shock and foams lose strength.",
  "img/en-specialty.webp"),
 ("a-automotive.html","Automotive","",
  "From glass bending mould covers and heated seats to friction materials and hydraulic filtration.",
  "img/en-automotive.webp"),
 ("a-textiles.html","Functional Textiles &amp; Smart Wearables","",
  "Weavable, sewable, washable conductive and heating yarns that run on standard textile equipment.",
  "img/en-textiles.webp"),
 ("a-more.html","More Applications · Co-Development","",
  "Not on this list? Tell us your temperature, medium and target properties — we propose the fiber, the form and the alloy, and send samples.",
  "img/en-micro-network.webp"),
]

LINES = [
 ("p-fiber.html","01","Metal Fiber &amp; Yarn","Bundle-drawn stainless steel fiber down to 2&nbsp;µm, supplied as long fiber, chopped fiber, tow, pure-metal and blended yarn.","img/jl-yarn-blend.webp"),
 ("p-felt.html","02","Sintered Felt &amp; Media","KIA3 / KIA3K / KIC4 sintered felts, 10–60&nbsp;µm absolute, 72–86% porosity, cleanable and reusable.","img/jl-felt.webp"),
 ("p-textile.html","03","Technical Textiles &amp; Sleeves","Knitted and braided sleeves, woven fabrics, tapes and ropes rated 350–1100&nbsp;°C.","img/jl-sleeve-flat.webp"),
 ("p-element.html","04","Filter Elements","Pleated cartridges to 30&nbsp;MPa, sintered mesh elements, high-temperature metal filter bags.","img/jl-cartridge-set.webp"),
 ("p-equipment.html","05","Oil Recovery Systems","Coalescing oil–water separation for hydrometallurgy — no demulsifiers, largest unit in service 600&nbsp;m³/h.","img/fts-render-tank.webp"),
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
   "address":{"@type":"PostalAddress","streetAddress":"No. 11 Huangbang Road, Dongxiao Town, Longyan Economic & Technological Development Zone","addressLocality":"Longyan","addressRegion":"Fujian","addressCountry":"CN"},
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

INTRO = r"""
<div id="intro" aria-hidden="true" hidden>
  <canvas id="iCv"></canvas>
  <div class="i-read"><span class="lbl">FILAMENT &Oslash;</span><b id="iNum">1000</b><span class="u">&micro;m</span></div>
  <div class="i-brand">
    <div class="i-mark">QL<span>METAL FIBER</span></div>
    <div class="i-rule"></div>
    <p>Stainless steel, drawn down to two microns.</p>
  </div>
  <button class="i-skip" type="button">Skip</button>
  <div class="i-bar"><i id="iBar"></i></div>
</div>
<style>
#intro{position:fixed;inset:0;z-index:9999;background:#08090b;color:#fff;overflow:hidden;
  clip-path:inset(0 0 0 0);transition:clip-path 1s cubic-bezier(.76,0,.24,1)}
#intro.out{clip-path:inset(0 0 100% 0)}
#intro canvas{position:absolute;inset:0;width:100%;height:100%}
#intro .i-read{position:absolute;left:0;right:0;top:50%;margin-top:-152px;text-align:center;
  font-family:"IBM Plex Mono",ui-monospace,monospace;opacity:0;transition:opacity .5s ease}
#intro.s1 .i-read{opacity:1}
#intro.s3 .i-read{opacity:0}
#intro .i-read .lbl{display:block;font-size:10px;letter-spacing:.34em;color:#6f7781;margin-bottom:10px}
#intro .i-read b{font-size:clamp(40px,7vw,78px);font-weight:400;letter-spacing:-.03em;
  font-variant-numeric:tabular-nums;transition:color .4s ease}
#intro .i-read .u{font-size:17px;color:#9aa2ac;margin-left:7px}
#intro.fin .i-read b{color:#ffd400}
#intro .i-brand{position:absolute;left:0;right:0;top:50%;transform:translateY(14px);
  text-align:center;opacity:0;transition:opacity .9s ease,transform .9s cubic-bezier(.2,.7,.2,1);padding:0 24px}
#intro.s3 .i-brand{opacity:1;transform:translateY(-6px)}
#intro .i-mark{font-family:"Archivo",system-ui,sans-serif;font-weight:700;letter-spacing:-.03em;
  font-size:clamp(34px,5.6vw,62px);line-height:1;display:flex;align-items:baseline;gap:14px;justify-content:center}
#intro .i-mark span{font-size:clamp(12px,1.5vw,17px);font-weight:500;letter-spacing:.3em;color:#aeb5be}
#intro .i-rule{width:54px;height:2px;background:#ffd400;margin:22px auto 18px}
#intro .i-brand p{font-size:clamp(13px,1.5vw,16px);color:#8d949d;letter-spacing:.01em;margin:0}
#intro .i-skip{position:absolute;right:24px;bottom:26px;z-index:3;background:transparent;color:#848b94;
  border:1px solid #23262b;border-radius:999px;padding:9px 20px;font:inherit;font-size:12.5px;
  letter-spacing:.06em;cursor:pointer;transition:color .25s,border-color .25s}
#intro .i-skip:hover{color:#fff;border-color:#4a4f57}
#intro .i-bar{position:absolute;left:0;right:0;bottom:0;height:2px;background:rgba(255,255,255,.07)}
#intro .i-bar i{display:block;height:100%;width:0;background:#ffd400}
body.pre{overflow:hidden}
body.pre .rv{opacity:0!important;transform:translateY(22px)!important}
@media(prefers-reduced-motion:reduce){#intro{display:none}}
</style>
<script>
(function(){
  var d=document, q=location.search.indexOf('intro=1')>-1, seen=false;
  try{ seen = sessionStorage.getItem('qlEnIntro')==='1'; }catch(e){}
  if(matchMedia('(prefers-reduced-motion:reduce)').matches || (seen && !q)) return;
  var el=d.getElementById('intro'); if(!el) return;

  d.body.classList.add('pre'); el.hidden=false;
  var cv=d.getElementById('iCv'), cx=cv.getContext('2d');
  var num=d.getElementById('iNum'), bar=d.getElementById('iBar');
  var W,H,dpr=Math.min(2,window.devicePixelRatio||1), T0=performance.now(), raf, dead=false;
  function size(){ W=innerWidth; H=innerHeight; cv.width=W*dpr; cv.height=H*dpr; cx.setTransform(dpr,0,0,dpr,0,0); }
  size(); addEventListener('resize',size);

  var DIES=[.20,.38,.56,.74], STEPS=[1000,500,100,50,12,2];
  var N=innerWidth<620?96:160, F=[];
  for(var i=0;i<N;i++) F.push({ s:(i/(N-1))*2-1, ph:Math.random()*6.28, sp:.6+Math.random()*.9, g:Math.random()<.07 });

  // 束宽随 x 递减：每过一道模具收一档
  function base(){ return Math.min(H*0.92, W*0.46); }   // 竖屏按短边收敛，避免散开
  function spread(x){
    var t=x/W, k=0;
    for(var i=0;i<DIES.length;i++) if(t>DIES[i]) k=i+1;
    return base()*[.62,.42,.26,.128,.045][k];
  }
  function draw(t){
    var e=(t-T0)/1000, cy=H/2;
    cx.fillStyle='#08090b'; cx.fillRect(0,0,W,H);
    var head = e<2.0 ? (e/2.0)*W*1.02 : W*1.02;          // 拉拔头推进
    var burst = e>2.05 ? Math.min(1,(e-2.05)/0.75) : 0;   // 末端散开
    cx.lineWidth=1;
    for(var i=0;i<N;i++){
      var f=F[i];
      cx.beginPath();
      var started=false;
      for(var x=0;x<=Math.min(head,W);x+=9){
        var sp=spread(x)*(1+burst*5.5*Math.pow(x/W,2.2));
        var wob=Math.sin(x*0.012*f.sp+f.ph+e*1.6)*spread(x)*0.10;
        var y=cy+f.s*sp+wob;
        if(!started){cx.moveTo(x,y);started=true;} else cx.lineTo(x,y);
      }
      var a=(0.30+0.42*Math.abs(1-Math.abs(f.s)))*(1-burst*0.55);
      cx.strokeStyle = f.g ? 'rgba(255,212,0,'+(a*0.9)+')' : 'rgba(206,214,223,'+a+')';
      cx.stroke();
    }
    // 模具环
    for(var j=0;j<DIES.length;j++){
      var dx=DIES[j]*W, passed=head>dx, r=spread(dx+2)*1.5+16;
      var lit = passed && head<dx+W*0.10;
      cx.strokeStyle = lit ? 'rgba(255,212,0,.95)' : (passed?'rgba(255,255,255,.16)':'rgba(255,255,255,.07)');
      cx.lineWidth = lit?2:1;
      cx.beginPath(); cx.ellipse(dx,cy,10,r,0,0,6.2832); cx.stroke();
      if(lit){ cx.save(); cx.globalAlpha=.3; cx.filter='blur(6px)';
        cx.beginPath(); cx.ellipse(dx,cy,10,r,0,0,6.2832); cx.stroke(); cx.restore(); }
    }
    cx.lineWidth=1;
    bar.style.width=Math.min(100,e/3.5*100)+'%';
    if(!dead) raf=requestAnimationFrame(draw);
  }
  raf=requestAnimationFrame(draw);

  var tms=[];
  function at(ms,fn){ tms.push(setTimeout(fn,ms)); }
  at(120, function(){ el.classList.add('s1'); });
  STEPS.forEach(function(v,i){ at(260+i*300, function(){ num.textContent=v; if(v===2) el.classList.add('fin'); }); });
  at(2150, function(){ el.classList.add('s3'); });
  at(3250, finish);
  at(5200, finish);                                   // 保险：无论如何都收场

  function finish(){
    if(dead) return; dead=true;
    try{ sessionStorage.setItem('qlEnIntro','1'); }catch(e){}
    tms.forEach(clearTimeout); cancelAnimationFrame(raf);
    el.classList.add('out');
    d.body.classList.remove('pre');
    setTimeout(function(){ el.remove(); d.dispatchEvent(new CustomEvent('ql:intro-done')); }, 1050);
  }
  el.querySelector('.i-skip').addEventListener('click', finish);
  addEventListener('keydown', function(ev){ if(ev.key==='Escape'||ev.key===' ') finish(); });
  addEventListener('wheel', finish, {passive:true, once:true});
  addEventListener('touchstart', finish, {passive:true, once:true});
})();
</script>
"""

html = head(
 "QL Metal Fiber | Stainless Steel Fiber, Sintered Felt, Filter Elements & Oil Recovery",
 "Fujian QL Metal Fiber manufactures the full chain in-house: micron-scale stainless steel fiber from 2 µm, yarns, technical textiles, sintered filter media, filter elements and oil recovery systems. Samples and application testing before you commit.",
 "index.html",
 "metal fiber, stainless steel fiber, sintered metal fiber felt, metal filter element, knitted roller sleeve, conductive yarn, oil water separation, China manufacturer",
 SCHEMA) + header("") + INTRO + f"""
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
        <img src="img/en-hero.webp" alt="Sintered metal fiber felt, rolled" width="1200" height="900">
        <figcaption>Sintered metal fiber felt &mdash; 10&ndash;60&nbsp;µm absolute, 72&ndash;86% porosity, cleanable</figcaption>
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

{film_block("Corporate film", "Twenty-four years, in <em>four minutes</em>", "From the drawing bench to sintered media, filter elements and the systems built around them — the plants, the laboratory and the people behind the material. English narration with bilingual subtitles.")}

{CTA_BAND}
</main>
""" + footer()

w("index.html", html)
