"""Merge colour2.py's measurements into the site (21 Nov 2026).
  works.js   colourStrength: nine numbers 0-100, in the order of NAMES below, for every artwork
  data/colour.json   {"ids": [...], "cl": [[L, a, b, w], ...] per work}: OKLab clusters for exact-shade search
                     (L x100, a and b x500, w = weight x1000 with the ground already discounted)
"""
import json, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VIS = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/vis'
NAMES = ['Red', 'Orange', 'Gold', 'Green', 'Blue', 'Brown', 'Black', 'Grey', 'Cream']
R = json.load(open(os.path.join(VIS, 'colour2.json')))
DATA = os.path.join(ROOT, 'data', 'works.js')
raw = open(DATA, encoding='utf-8').read(); a = raw.index('['); b = raw.rindex(']') + 1
works = json.loads(raw[a:b]); n = 0; ids = []; cl = []
# Works measured in an earlier session keep their clusters from the current data/colour.json.
try:
    _old = json.load(open(os.path.join(ROOT, 'data', 'colour.json'))); OLD = dict(zip(_old['ids'], _old['cl']))
except Exception: OLD = {}
for w in works:
    if w.get('itemType') == 'literature': continue
    r = R.get(w['id'])
    if r:
        w['colourStrength'] = [r['s'][k] for k in NAMES]; n += 1
        ids.append(w['id']); cl.append(r['cl'])
    elif w['id'] in OLD:
        ids.append(w['id']); cl.append(OLD[w['id']])
open(DATA, 'w', encoding='utf-8').write(raw[:a] + json.dumps(works, ensure_ascii=False, separators=(',', ':')) + raw[b:])
json.dump({'names': NAMES, 'ids': ids, 'cl': cl}, open(os.path.join(ROOT, 'data', 'colour.json'), 'w'), separators=(',', ':'))
print('strengths', n, 'clusters', len(ids))
