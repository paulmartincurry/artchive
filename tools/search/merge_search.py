"""Merge the measured colours and the hidden descriptions into data/works.js.

Inputs (working folder, default /home/claude/vis): colour.json from colour.py, desc/*.jsonl from the describers.
Per artwork it sets:
  palette      five colours measured from the image (old palette kept once as paletteOld)
  colorFamily  the main measured colour family (old value kept once as colorFamilyOld)
  colours      every family the picture clearly carries (the colour filter matches any of them)
  seeText      a plain description of what the picture shows, for search only; never displayed
               (build_pages.py leaves it out of site.js; it ships in data/see.json, which search loads later)
"""
import json, os, sys, glob
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VIS = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/vis'
DATA = os.path.join(ROOT, 'data', 'works.js')
raw = open(DATA, encoding='utf-8').read(); a = raw.index('['); b = raw.rindex(']') + 1
works = json.loads(raw[a:b])
col = json.load(open(os.path.join(VIS, 'colour.json')))
desc = {}
for f in sorted(glob.glob(os.path.join(VIS, 'desc', '*.jsonl'))):
    for line in open(f, encoding='utf-8'):
        line = line.strip()
        if not line: continue
        try: r = json.loads(line)
        except Exception: continue
        d = (r.get('d') or '').strip()
        if d and d != 'UNREADABLE' and len(d) > 30: desc[r['id']] = d
nc = nd = 0
for w in works:
    if w.get('itemType') == 'literature': continue
    c = col.get(w['id'])
    if c:
        if 'colorFamilyOld' not in w: w['colorFamilyOld'] = w.get('colorFamily', '')
        if 'paletteOld' not in w and w.get('palette'): w['paletteOld'] = w['palette']
        w['palette'] = c['palette']; w['colorFamily'] = c['family']; w['colours'] = c['all']; nc += 1
    if w['id'] in desc: w['seeText'] = desc[w['id']]; nd += 1
open(DATA, 'w', encoding='utf-8').write(raw[:a] + json.dumps(works, ensure_ascii=False, separators=(',', ':')) + raw[b:])
json.dump({w['id']: w['seeText'] for w in works if w.get('seeText')}, open(os.path.join(ROOT, 'data', 'see.json'), 'w'), ensure_ascii=False, separators=(',', ':'))
print('colours', nc, 'descriptions', nd)
