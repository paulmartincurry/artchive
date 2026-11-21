"""Measure each artwork's colour from its pixels.

palette: five colours, most-covering first (k-means in Lab on a 96px copy, edges trimmed so mounts and
scan borders count less). family: one of the site's six, chosen by what the eye reads first:
a strong colour that covers a fair share wins; otherwise the picture is dark (Black) or light (Cream).
"""
import json, os, sys
import numpy as np
from PIL import Image

FAMILIES = {
    'Crimson & Rust': 'red', 'Ochre & Gold': 'gold', 'Indigo & Prussian': 'blue',
    'Verdigris & Forest': 'green', 'Obsidian & Ink': 'black', 'Parchment & Bone': 'cream'}


def srgb_to_lab(rgb):
    c = rgb / 255.0
    c = np.where(c > 0.04045, ((c + 0.055) / 1.055) ** 2.4, c / 12.92)
    M = np.array([[0.4124, 0.3576, 0.1805], [0.2126, 0.7152, 0.0722], [0.0193, 0.1192, 0.9505]])
    xyz = c @ M.T / np.array([0.95047, 1.0, 1.08883])
    f = np.where(xyz > 0.008856, np.cbrt(xyz), 7.787 * xyz + 16 / 116)
    L = 116 * f[:, 1] - 16
    a = 500 * (f[:, 0] - f[:, 1])
    b = 200 * (f[:, 1] - f[:, 2])
    return np.stack([L, a, b], 1)


def kmeans(X, k=6, iters=12, seed=0):
    rng = np.random.default_rng(seed)
    C = X[rng.choice(len(X), k, replace=False)]
    for _ in range(iters):
        d = ((X[:, None, :] - C[None]) ** 2).sum(-1)
        lab = d.argmin(1)
        for j in range(k):
            m = X[lab == j]
            if len(m): C[j] = m.mean(0)
    return C, lab


def measure(path):
    im = Image.open(path).convert('RGB')
    w, h = im.size
    dx, dy = int(w * 0.06), int(h * 0.06)
    im = im.crop((dx, dy, w - dx, h - dy))
    im.thumbnail((96, 96))
    px = np.asarray(im).reshape(-1, 3).astype(float)
    lab = srgb_to_lab(px)
    C, l = kmeans(lab, 6)
    share = np.bincount(l, minlength=len(C)) / len(l)
    rgbC = np.array([px[l == j].mean(0) if (l == j).any() else [0, 0, 0] for j in range(len(C))])
    order = np.argsort(-share)
    palette = ['#%02X%02X%02X' % tuple(int(round(v)) for v in rgbC[j]) for j in order[:5]]

    # Family. Hue in Lab: angle of (a, b). Chroma = length.
    best, best_score = None, 0.0
    fams = {}
    for j in range(len(C)):
        L, a, b = C[j]
        chroma = (a * a + b * b) ** 0.5
        if chroma < 18 or share[j] < 0.04: continue
        hue = (np.degrees(np.arctan2(b, a)) + 360) % 360
        if hue < 50 or hue >= 345: fam = 'Crimson & Rust' if chroma >= 24 else None
        elif hue < 100:
            fam = 'Ochre & Gold' if (L > 35 and chroma >= 26) else ('Crimson & Rust' if chroma >= 34 else None)
        elif hue < 200: fam = 'Verdigris & Forest'
        elif hue < 305: fam = 'Indigo & Prussian'
        else: fam = 'Crimson & Rust'
        if fam is None: continue
        score = share[j] * chroma
        fams[fam] = fams.get(fam, 0) + score
    for fam, score in fams.items():
        if score > best_score: best, best_score = fam, score
    meanL = float((C[:, 0] * share).sum())
    if best is None or best_score < 4.5:
        best = 'Obsidian & Ink' if meanL < 52 else 'Parchment & Bone'
    # every colour that clearly carries, strongest first; neutrals join when they cover most of the picture
    BAR = {'Indigo & Prussian': 2.0, 'Verdigris & Forest': 2.0, 'Crimson & Rust': 3.0, 'Ochre & Gold': 3.5}
    also = [f for f, sc in sorted(fams.items(), key=lambda x: -x[1]) if sc >= BAR[f]]
    dark = float(share[C[:, 0] < 30].sum()); light = float(share[(C[:, 0] > 72) & (np.hypot(C[:, 1], C[:, 2]) < 22)].sum())
    if dark > 0.35: also.append('Obsidian & Ink')
    if light > 0.35: also.append('Parchment & Bone')
    if best not in also: also.insert(0, best)
    return palette, best, round(best_score, 2), round(meanL, 1), also


if __name__ == '__main__':
    out = {}
    ids = [f[:-4] for f in sorted(os.listdir('img')) if f.endswith('.jpg')]
    for i in ids:
        try:
            p, f, s, L, al = measure(f'img/{i}.jpg')
            out[i] = {'palette': p, 'family': f, 'score': s, 'L': L, 'all': al}
        except Exception as e:
            print('fail', i, e, file=sys.stderr)
    json.dump(out, open('colour.json', 'w'))
    from collections import Counter
    print(len(out), Counter(v['family'] for v in out.values()))
    print('any', Counter(f for v in out.values() for f in v['all']))
