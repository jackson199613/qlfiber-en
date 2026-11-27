# -*- coding: utf-8 -*-
"""Put the image2-retouched photos into the site as img/pc-*.webp (4:3, 1600x1200) and keep numbered masters."""
import glob, os, shutil
from PIL import Image
SRC = '/mnt/user-data/uploads/修改过后的图'
SITE = '/home/claude/qianglun/img'
MAP = {  # 编号: (image2 文件名前缀, 网站文件名)
 1:('fdd09b','pc-media-felt'), 2:('3fb730','pc-media-alloy'), 3:('717758','pc-mach-dust'), 4:('c97829','pc-mach-parts'),
 5:('ba9058','pc-purify-retrofit'), 6:('dd7f94','pc-purify-trough'), 7:('ddcde2','pc-purify-tank'), 8:('ca1842','pc-mach-hydraulic'),
 9:('f27c0e','pc-mach-air'), 10:('b93299','pc-mach-fluid'), 11:('173c13','pc-media-composite'), 12:('0b3d72','pc-yarn-fiber'),
 13:('2d34a1','pc-yarn-spun'), 14:('b94ce4','pc-yarn-thread'), 15:('2c4900','pc-yarn-coat'), 16:('0b01e6','pc-yarn-tape'),
 17:('e3b770','pc-yarn-cloth'), 18:('ef6d63','pc-thermo-tape'), 19:('aff736','pc-thermo-elastic'), 20:('cf6137','pc-thermo-braid'),
 21:('1d7db2','pc-thermo-rope'), 22:('12aa40','pc-thermo-felt'), 23:('a6c1b6','pc-thermo-thread'), 24:('5586fe','sleeve-06'),
}
if __name__ == '__main__':
    for n, (pre, key) in MAP.items():
        f = glob.glob(f'{SRC}/Image2-{pre}*.png'); assert len(f) == 1, (n, pre, f)
        im = Image.open(f[0]).convert('RGB')
        im.save(f'/home/claude/qw/final/{n:02d}_{key}.png')
        if key.startswith('pc-'):
            assert abs(im.width / im.height - 4 / 3) < 0.01, im.size
            im.resize((1440, 1080), Image.LANCZOS).save(f'{SITE}/{key}.webp', quality=88, method=6)
        else:
            im.save(f'{SITE}/{key}.webp', quality=86, method=6)
        print(n, key, im.size, os.path.getsize(f'{SITE}/{key}.webp') // 1024, 'KB')
