# -*- coding: utf-8 -*-
"""精修产品图 → 各种画幅的衍生图（2026.11.27 甲方 4.0）

精修图是 4:3 的影棚照。网站上有些位置不是 4:3（首页首屏拼图、内页首屏横幅、16:9 卡片），
直接铺满会把产品裁掉一截。这里不裁产品：先找到产品的外接框，把整件产品缩放到目标画幅的安全区内，
画幅不够的地方用原图自身的背景向外延伸（边缘复制 + 大半径模糊 + 羽化接缝），看不出拼接。

用法：python3 variants.py        # 生成全部衍生图
"""
import os
import numpy as np
import cv2

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
IMG = os.path.join(ROOT, 'img')


def read(key):
    im = cv2.imread(os.path.join(IMG, key + '.webp'), cv2.IMREAD_COLOR)
    assert im is not None, key
    return im


def product_box(im):
    """产品（含投影）的外接框：与四周背景亮度差、饱和度、边缘三者取并集"""
    h, w = im.shape[:2]
    lab = cv2.cvtColor(im, cv2.COLOR_BGR2LAB).astype(np.float32)
    L = lab[..., 0]
    border = np.concatenate([L[:12].ravel(), L[-12:].ravel(), L[:, :12].ravel(), L[:, -12:].ravel()])
    bg = np.median(border)
    chroma = np.hypot(lab[..., 1] - 128, lab[..., 2] - 128)
    edges = cv2.Canny(cv2.GaussianBlur(im, (0, 0), 1.2), 40, 110) > 0
    m = (np.abs(L - bg) > 26) | (chroma > 14) | edges
    m = cv2.morphologyEx(m.astype(np.uint8), cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
    n, lab_, stats, _ = cv2.connectedComponentsWithStats(m, 8)
    keep = np.zeros_like(m)
    for i in range(1, n):
        if stats[i, cv2.CC_STAT_AREA] > h * w * 0.0006:
            keep[lab_ == i] = 1
    ys, xs = np.where(keep > 0)
    return xs.min(), ys.min(), xs.max() + 1, ys.max() + 1


BG = (244, 246, 246)   # 统一背景色（BGR），接近页面的浅灰白


def product_mask(im):
    """产品与较深投影的蒙版（1=产品）。只用来把背景和产品分开估计光照，不用来抠图"""
    lab = cv2.cvtColor(im, cv2.COLOR_BGR2LAB).astype(np.float32)
    L = lab[..., 0]
    bgL = cv2.GaussianBlur(cv2.medianBlur(L.astype(np.uint8), 5).astype(np.float32), (0, 0), 3)
    border = np.concatenate([L[:12].ravel(), L[-12:].ravel(), L[:, :12].ravel(), L[:, -12:].ravel()])
    chroma = np.hypot(lab[..., 1] - 128, lab[..., 2] - 128)
    edges = cv2.Canny(cv2.GaussianBlur(im, (0, 0), 1.2), 30, 90) > 0
    m = (bgL < np.percentile(border, 20) - 22) | (chroma > 16) | edges
    m = cv2.morphologyEx(m.astype(np.uint8), cv2.MORPH_CLOSE, np.ones((25, 25), np.uint8))
    # 填实内部孔洞（亮色线盘、金属高光）
    ff = m.copy(); hh, ww = m.shape
    pad = cv2.copyMakeBorder(ff, 1, 1, 1, 1, cv2.BORDER_CONSTANT, value=0)
    cv2.floodFill(pad, None, (0, 0), 2)
    m = (pad[1:-1, 1:-1] != 2).astype(np.uint8)
    return cv2.dilate(m, np.ones((21, 21), np.uint8))


def flatten(im):
    """把影棚背景的明暗渐变和偏色校平成统一的 BG：按背景像素估计光照场，整图做平场校正。
    产品与投影的明暗关系保留（它们跟着同一个平滑增益走），所以不是抠图，边缘不会发虚。"""
    m = product_mask(im)
    h, w = im.shape[:2]
    sw = 180; sh = int(round(h * sw / w))          # 光照场很平滑，在小图上估计再放大
    xs = cv2.resize(im, (sw, sh), interpolation=cv2.INTER_AREA).astype(np.float32)
    bgw = (cv2.resize(m, (sw, sh), interpolation=cv2.INTER_AREA) == 0).astype(np.float32)
    field = np.zeros_like(xs); wsum = np.zeros((sh, sw), np.float32)
    for sig, wt in ((sw * 0.03, 1.0), (sw * 0.12, 0.05), (sw * 0.5, 0.002)):
        field += cv2.GaussianBlur(xs * bgw[..., None], (0, 0), sig) * wt
        wsum += cv2.GaussianBlur(bgw, (0, 0), sig) * wt
    field /= np.maximum(wsum, 1e-6)[..., None]
    gain = np.clip(np.array(BG, np.float32)[None, None, :] / np.maximum(field, 1), 0.85, 1.35)
    gain = cv2.resize(cv2.GaussianBlur(gain, (0, 0), 1.2), (w, h), interpolation=cv2.INTER_CUBIC)
    return np.clip(im.astype(np.float32) * gain, 0, 255).astype(np.uint8)


def _ramp(n, lo, hi, a, b):
    """一维权重：画布坐标 [lo,hi) 是原图；从原图边缘到产品外接框 [a,b) 之间由 0 平滑升到 1。原图边缘贴着画布边缘的一侧不需要过渡"""
    x = np.arange(n, dtype=np.float32)
    w = np.ones(n, np.float32)
    if lo > 0:
        m = max(a - lo, 6)
        w = np.minimum(w, np.clip((x - lo) / m, 0, 1))
    if hi < n:
        m = max(hi - b, 6)
        w = np.minimum(w, np.clip((hi - 1 - x) / m, 0, 1))
    return w * w * (3 - 2 * w)


def extend(im, W, H, scale, ox, oy, box):
    """把 im 缩放 scale 倍后放到 W×H 画布的 (ox, oy)，空出来的地方用背景延伸补齐。box 是产品外接框（原图坐标）"""
    sw, sh = int(round(im.shape[1] * scale)), int(round(im.shape[0] * scale))
    src = cv2.resize(im, (sw, sh), interpolation=cv2.INTER_AREA if scale < 1 else cv2.INTER_LANCZOS4)
    x0, y0 = max(ox, 0), max(oy, 0)
    x1, y1 = min(ox + sw, W), min(oy + sh, H)
    vis = src[y0 - oy:y1 - oy, x0 - ox:x1 - ox]
    pad = cv2.copyMakeBorder(vis, y0, H - y1, x0, W - x1, cv2.BORDER_REPLICATE)
    if (x0, y0, x1, y1) == (0, 0, W, H):
        return pad
    soft = np.empty_like(pad); soft[:] = BG      # 底图已做过平场校正，背景就是统一色，直接用它延伸
    # 接缝：从原图边缘到产品外接框之间整段渐变，背景的明暗过渡自然，不留方框
    bx0, by0, bx1, by1 = [v * scale for v in box]
    wx = _ramp(W, x0, x1, ox + bx0, ox + bx1)
    wy = _ramp(H, y0, y1, oy + by0, oy + by1)
    mask = np.minimum(wx[None, :], wy[:, None])[..., None]
    out = pad.astype(np.float32) * mask + soft.astype(np.float32) * (1 - mask)
    rng = np.random.default_rng(7)   # 轻微颗粒，避免大面积模糊出现色带
    out += rng.normal(0, 0.9, out.shape[:2])[..., None] * (1 - mask)
    return np.clip(out, 0, 255).astype(np.uint8)


def variant(key, out, W, H, max_w, max_h, cx=0.5, cy=0.5, quality=88, lift=0):
    """整件产品落在画布的安全区内：产品外接框宽 ≤ W*max_w、高 ≤ H*max_h，中心在 (cx, cy)"""
    im = read(key)
    bx0, by0, bx1, by1 = product_box(im)
    bw, bh = bx1 - bx0, by1 - by0
    scale = min(W * max_w / bw, H * max_h / bh)
    ox = int(round(W * cx - (bx0 + bw / 2) * scale))
    oy = int(round(H * cy - (by0 + bh / 2) * scale))
    res = extend(im, W, H, scale, ox, oy, (bx0, by0, bx1, by1))
    if lift:   # 横幅背景提亮到接近页面底色，产品同步略提亮
        g = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
        bgv = float(np.median(np.concatenate([g[:8].ravel(), g[-8:].ravel()])))
        res = np.clip(res.astype(np.float32) * min(lift / bgv, 1.07), 0, 255).astype(np.uint8)
    cv2.imwrite(os.path.join(IMG, out + '.webp'), res, [cv2.IMWRITE_WEBP_QUALITY, quality])
    print(f'{out}: {W}x{H} scale={scale:.2f} box={bw}x{bh}')


if __name__ == '__main__':
    # 首页首屏拼图：左侧竖幅（桌面约 0.57，手机约 0.49）与右侧两格（约 0.93–1.02）
    variant('pc-media-felt', 'pc-media-felt-tall', 1000, 2000, 0.86, 0.5, cy=0.46)
    variant('pc-mach-fluid', 'pc-mach-fluid-sq', 1200, 1200, 0.8, 0.74, cy=0.47)
    variant('pc-yarn-spun', 'pc-yarn-spun-sq', 1200, 1200, 0.8, 0.74, cy=0.47)
    # 内页首屏横幅（约 1440×416，顶部 80px 被导航栏盖住；宽屏时上下还会再裁掉一些）：
    # 产品只占画布一半高度、中心偏下、靠右，任何宽度下都完整，也不压到左侧标题
    variant('pc-mach-fluid', 'hero-jl-cart', 2400, 700, 0.25, 0.5, cx=0.835, cy=0.6)
    variant('pc-media-felt', 'hero-jl-felt', 2400, 700, 0.25, 0.5, cx=0.835, cy=0.6)
    variant('pc-yarn-spun', 'hero-jl-yarn', 2400, 700, 0.25, 0.5, cx=0.835, cy=0.6)
