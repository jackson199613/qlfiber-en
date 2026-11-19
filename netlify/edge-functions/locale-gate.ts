// 合同附件二「支持屏蔽中文浏览器访问，防止国内同行抄袭网站」
//
// 做法：按浏览器语言判断，中文环境的访客不直接进入英文站，
// 而是看到一个提示页并引导至中文官网。不做硬屏蔽的原因是——
// 硬屏蔽会连带挡掉搜索引擎和海外华人买家，得不偿失。
//
// 放行：搜索引擎与 AI 爬虫、已点「继续浏览」的访客（带 cookie）、
//      静态资源与表单 POST。

import type { Context } from "https://edge.netlify.com";

const BOTS =
  /(googlebot|bingbot|duckduckbot|baiduspider|yandex|applebot|slurp|gptbot|oai-searchbot|chatgpt-user|claudebot|claude-web|anthropic-ai|perplexitybot|facebookexternalhit|twitterbot|linkedinbot|whatsapp|telegrambot|ahrefsbot|semrushbot|netlify|lighthouse|pagespeed|headlesschrome)/i;

const PASS_COOKIE = "ql_en_ok";
const CN_SITE = "https://www.qlfiber.com/";

export default async (request: Request, context: Context) => {
  const url = new URL(request.url);

  // 只拦页面本身，不拦资源与表单提交
  if (request.method !== "GET") return;
  const p = url.pathname;
  if (/\.(css|js|webp|png|jpg|jpeg|svg|ico|xml|txt|json|woff2?|mp4|pdf)$/i.test(p)) return;
  if (p.startsWith("/.netlify")) return;

  // 访客自己选择了继续浏览
  const cookie = request.headers.get("cookie") || "";
  if (cookie.includes(`${PASS_COOKIE}=1`)) return;
  if (url.searchParams.has("en")) {
    const res = await context.next();
    res.headers.append(
      "Set-Cookie",
      `${PASS_COOKIE}=1; Path=/; Max-Age=31536000; SameSite=Lax; Secure`,
    );
    return res;
  }

  // 搜索引擎与 AI 爬虫一律放行，避免影响 Google 收录
  const ua = request.headers.get("user-agent") || "";
  if (BOTS.test(ua)) return;

  // 浏览器语言为中文才提示
  const al = (request.headers.get("accept-language") || "").toLowerCase();
  const first = al.split(",")[0].trim();
  if (!first.startsWith("zh")) return;

  return new Response(GATE_HTML, {
    status: 200,
    headers: {
      "content-type": "text/html; charset=utf-8",
      "cache-control": "no-store",
      "x-robots-tag": "noindex",
    },
  });
};

export const config = { path: "/*" };

const GATE_HTML = `<!doctype html>
<html lang="zh-CN"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>福建强纶新材料股份有限公司</title>
<style>
  :root{--ink:#121417;--gold:#ffd400;--muted:#878e98;--line:#30343b}
  *{box-sizing:border-box}
  body{margin:0;min-height:100vh;display:flex;align-items:center;justify-content:center;
    background:var(--ink);color:#fff;padding:24px;
    font-family:"Inter Tight",-apple-system,BlinkMacSystemFont,"PingFang SC","Microsoft YaHei",sans-serif;
    -webkit-font-smoothing:antialiased}
  .box{max-width:560px;width:100%}
  .eye{font-size:11px;letter-spacing:.2em;color:var(--gold);margin-bottom:26px;
    font-family:ui-monospace,SFMono-Regular,Menlo,monospace}
  h1{font-size:clamp(24px,4.6vw,33px);line-height:1.38;margin:0 0 20px;font-weight:600;letter-spacing:-.02em}
  p{color:#a7aeb7;line-height:1.85;font-size:15.4px;margin:0 0 16px}
  .row{display:flex;gap:12px;flex-wrap:wrap;margin-top:32px}
  a.b{display:inline-flex;align-items:center;gap:9px;padding:14px 26px;border-radius:999px;
    text-decoration:none;font-size:14.6px;font-weight:560;transition:.25s}
  .p{background:var(--gold);color:#1a1703}
  .p:hover{background:#e8c200}
  .s{border:1px solid var(--line);color:#fff}
  .s:hover{border-color:#fff}
  .ft{margin-top:40px;padding-top:22px;border-top:1px solid var(--line);
    font-size:12.6px;color:var(--muted);line-height:1.8}
  .ft a{color:var(--muted)}
</style></head><body>
<div class="box">
  <div class="eye">QL METAL FIBER · 福建强纶新材料</div>
  <h1>您似乎正在使用中文浏览器</h1>
  <p>这里是强纶新材料的英文外贸站，面向海外客户。中文官网的内容更完整，包含产品中心、选型中心、技术专栏与完整的客户案例。</p>
  <p>如果您确实需要查看英文版，也可以直接继续。</p>
  <div class="row">
    <a class="b p" href="${CN_SITE}">前往中文官网 →</a>
    <a class="b s" href="/?en=1">继续浏览英文站</a>
  </div>
  <div class="ft">
    福建强纶新材料股份有限公司 · 新三板 872336<br>
    外贸业务：<a href="mailto:hcq@jl-jiber.com">hcq@jl-jiber.com</a>
  </div>
</div></body></html>`;
