"""Cut grid screenshots (6 x 3, from grid.js) back into one image per work: shots/pNNN.jpg -> img/<id>.jpg (marked as screen captures)."""
import json, os, sys, glob
import numpy as np
from PIL import Image
L = json.load(open('shotlist.json')); cap = json.load(open('captured.json')) if os.path.exists('captured.json') else {}
for f in sorted(glob.glob('shots/p*.jpg')):
    k = int(os.path.basename(f)[1:4]); S = Image.open(f).convert('RGB'); W, H = S.size
    for j, (id_, u) in enumerate(L[k*18:k*18+18]):
        c, r = j % 6, j // 6
        x0, y0, x1, y1 = round(c*W/6)+7, round(r*H/3)+7, round((c+1)*W/6)-7, round((r+1)*H/3)-7
        t = S.crop((x0, y0, x1, y1)); a = np.asarray(t).max(2)
        rows = np.where(a.max(1) > 14)[0]; cols = np.where(a.max(0) > 14)[0]
        if len(rows) < 20 or len(cols) < 20: print('empty', k, id_); continue
        t = t.crop((cols[0], rows[0], cols[-1]+1, rows[-1]+1))
        t.save(f'img/{id_}.jpg', quality=92); cap[id_] = f
json.dump(cap, open('captured.json', 'w')); print('captured', len(cap))
