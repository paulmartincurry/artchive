"""Measure colour for smarter colour search (21 Nov 2026). Replaces colour.py's families.

Per artwork, from its small copy in <vis>/img/<id>.jpg:
  - eight colour clusters in OKLab (k-means on a 96 px copy, outer 6% trimmed), each with
    its share of the area and its share weighted towards the centre (Gaussian, the subject
    is usually near the middle);
  - the ground: a light, low-chroma cluster that covers most of the border or 40% of the picture
    (paper, mount, gallery wall). It counts at a third of its weight for every name except Cream, and for
    exact-shade search;
  - a strength from 0 to 100 for each named colour (Red, Orange, Gold, Green, Blue, Brown,
    Black, Grey, Cream): weighted area of clusters with that name, vivid colour counting more;
  - the clusters themselves, for exact-shade search in the browser (data/colour.json).
Writes <vis>/colour2.json.   Run: python3 tools/search/colour2.py [/home/claude/vis]
"""
import json, os, sys, math
import numpy as np
from PIL import Image

VIS = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/vis'
NAMES = ['Red', 'Orange', 'Gold', 'Green', 'Blue', 'Brown', 'Black', 'Grey', 'Cream']


def srgb_to_oklab(rgb):
    c = rgb / 255.0
    c = np.where(c > 0.04045, ((c + 0.055) / 1.055) ** 2.4, c / 12.92)
    M1 = np.array([[0.4122214708, 0.5363325363, 0.0514459929],
                   [0.2119034982, 0.6806995451, 0.1073969566],
                   [0.0883024619, 0.2817188376, 0.6299787005]])
    lms = np.cbrt(c @ M1.T)
    M2 = np.array([[0.2104542553, 0.7936177850, -0.0040720468],
                   [1.9779984951, -2.4285922050, 0.4505937099],
                   [0.0259040371, 0.7827717662, -0.8086757660]])
    return lms @ M2.T


def kmeans(X, k=8, iters=14, seed=0):
    rng = np.random.default_rng(seed)
    C = X[rng.choice(len(X), k, replace=False)].copy()
    for _ in range(iters):
        lab = ((X[:, None, :] - C[None]) ** 2).sum(-1).argmin(1)
        for j in range(k):
            m = X[lab == j]
            if len(m): C[j] = m.mean(0)
    return C, lab


def name(L, a, b):
    C = math.hypot(a, b); h = (math.degrees(math.atan2(b, a)) + 360) % 360
    if L < 0.28 and C < 0.07: return 'Black'
    if C < 0.035:
        if L < 0.30: return 'Black'
        if L > 0.80: return 'Cream'
        return 'Grey'
    if L > 0.80 and C < 0.07 and (h < 120 or h > 330): return 'Cream'
    warm = 35 <= h <= 110
    if C < 0.055 and 20 <= h <= 110: return 'Brown' if L < 0.72 else 'Cream'
    if C < 0.045: return 'Grey'
    if (h >= 345 or h < 40) and C >= 0.11:
        if L > 0.80: return None                  # pale pinks: no name (pink is not a named swatch)
        return 'Red'
    if warm and L < 0.55: return 'Brown'          # umbers, siennas, dark ochre
    if warm and C < 0.10: return 'Brown' if L < 0.74 else 'Cream'   # aged paper, silk, tan
    if h >= 345 or h < 40: return 'Brown' if L < 0.6 else None      # dull reds: brown; dull pinks: none
    if h < 72: return 'Orange'
    if h < 115: return 'Gold'
    if h < 200: return 'Green'
    if h < 285: return 'Blue'
    return None                                   # purples and magentas: reached through shades


def measure(path):
    im = Image.open(path).convert('RGB'); w, h = im.size
    dx, dy = int(w * .06), int(h * .06)
    im = im.crop((dx, dy, w - dx, h - dy)); im.thumbnail((96, 96))
    a = np.asarray(im).astype(float); H, W, _ = a.shape
    px = a.reshape(-1, 3); ok = srgb_to_oklab(px)
    yy, xx = np.mgrid[0:H, 0:W]
    cw = np.exp(-(((xx - W / 2) / (W * .45)) ** 2 + ((yy - H / 2) / (H * .45)) ** 2)).reshape(-1)
    border = ((xx < 3) | (xx >= W - 3) | (yy < 3) | (yy >= H - 3)).reshape(-1)
    K, l = kmeans(ok, 8)
    out = []
    for j in range(len(K)):
        m = l == j
        if not m.any(): continue
        L_, a_, b_ = ok[m].mean(0)
        share = float(m.mean()); cshare = float((cw * m).sum() / cw.sum())
        bshare = float((m & border).sum() / border.sum())
        out.append(dict(L=float(L_), a=float(a_), b=float(b_), share=share, cshare=cshare, bshare=bshare,
                        rgb=px[m].mean(0)))
    # ground: light, low-chroma, most of the border
    ground = None
    for c in out:
        if c['L'] > 0.62 and math.hypot(c['a'], c['b']) < 0.06 and (c['bshare'] > 0.45 or c['share'] > 0.40):
            if ground is None or c['bshare'] > ground['bshare']: ground = c
    strengths = {n: 0.0 for n in NAMES}
    clusters = []
    for c in out:
        wgt = 0.5 * c['share'] + 0.5 * c['cshare']
        n = name(c['L'], c['a'], c['b'])
        Cc = math.hypot(c['a'], c['b'])
        g = c is ground
        if n:
            vivid = 1.0 if n in ('Black', 'Grey', 'Cream', 'Brown') else min(1.3, 0.4 + Cc / 0.15)
            strengths[n] += wgt * vivid * (1.0 if (not g or n == 'Cream') else 0.33)
        clusters.append([round(c['L'] * 100), round(c['a'] * 500), round(c['b'] * 500),
                         round(wgt * (0.1 if g else 1.0) * 1000)])
    s100 = {n: min(100, round(v * 100)) for n, v in strengths.items()}
    order = sorted(out, key=lambda c: -c['share'])
    palette = ['#%02X%02X%02X' % tuple(int(round(v)) for v in c['rgb']) for c in order[:5]]
    return s100, clusters, palette, bool(ground)


if __name__ == '__main__':
    res = {}
    for f in sorted(os.listdir(os.path.join(VIS, 'img'))):
        if not f.endswith('.jpg'): continue
        s, cl, pal, g = measure(os.path.join(VIS, 'img', f))
        res[f[:-4]] = {'s': s, 'cl': cl, 'pal': pal, 'ground': g}
    json.dump(res, open(os.path.join(VIS, 'colour2.json'), 'w'))
    from collections import Counter
    print(len(res), 'with ground', sum(v['ground'] for v in res.values()))
    for floor in (8, 12):
        print('>=', floor, dict(Counter(n for v in res.values() for n, x in v['s'].items() if x >= floor)))
