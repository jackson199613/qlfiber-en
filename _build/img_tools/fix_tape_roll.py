# -*- coding: utf-8 -*-
"""18 号（耐高温金属纤维带/布）：甲方原图里带卷顶部被画面裁掉，image2 把它画成了一条平切的边。
带卷端面是一圈圈同心的椭圆，这里用端面自身的前半部分，绕纸芯中心做 180° 对称，把后半个弧面补完整。"""
import sys, glob, cv2, numpy as np
sys.path.insert(0, '/home/claude/qianglun/_build/img_tools')
import variants as v

CX, CY, A, B = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])
Y0, Y1 = 150.0, 190.0          # 这一段从“补的”平滑过渡到“原有的”
src = cv2.imread(glob.glob('/mnt/user-data/uploads/修改过后的图/Image2-ef6d63*.png')[0])
im = v.flatten(src).astype(np.float32)
h, w = im.shape[:2]
yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
refl = cv2.remap(im, 2 * CX - xx, 2 * CY - yy, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
r = np.sqrt(((xx - CX) / A) ** 2 + ((yy - CY) / B) ** 2)
inside = np.clip((1 - r) * A / 1.5 + 0.5, 0, 1)             # 椭圆边缘 1.5px 抗锯齿
bg = np.empty_like(im); bg[:] = v.BG
cap = refl * inside[..., None] + bg * (1 - inside[..., None])   # 椭圆内用对称过来的端面，椭圆外是背景
wgt = np.clip((Y1 - yy) / (Y1 - Y0), 0, 1); wgt = (wgt * wgt * (3 - 2 * wgt))[..., None]
out = cap * wgt + im * (1 - wgt)
out = np.clip(out, 0, 255).astype(np.uint8)
cv2.imwrite('/home/claude/qw/final/18_pc-thermo-tape_fixed.png', out)
cv2.imwrite('/home/claude/qw/shots/tape_fix.jpg', np.hstack([im.astype(np.uint8)[0:520, 420:1220], out[0:520, 420:1220]]), [cv2.IMWRITE_JPEG_QUALITY, 92])
