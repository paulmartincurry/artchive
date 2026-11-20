"""Merge a writing batch (out/g_<batch>.json) into works.js. Usage: python3 merge_lit.py w8a [--apply]"""
import sys, json, re, unicodedata
sys.path.insert(0, '/home/claude/tools')
from kit import norm
B = sys.argv[1]; APPLY = '--apply' in sys.argv
P = '/home/claude/artchive/data/works.js'
s = open(P, encoding='utf8').read(); a, b = s.index('['), s.rindex(']') + 1; d = json.loads(s[a:b])
N = json.load(open(f'/home/claude/out/g_{B}.json'))
try: LINES = json.load(open(f'/home/claude/out/line_{B}.json'))
except Exception: LINES = {}
pal = {}
for w in d:
    if w['id'].startswith('LIT'): pal.setdefault(w['colorFamily'], w['palette'])
def era(y): return 'Ancient & Medieval' if y < 1400 else '1400–1650' if y < 1650 else '1650–1800' if y < 1800 else '1800–1920' if y <= 1920 else '1920–Now'
nid = max(int(w['id'][4:]) for w in d if w['id'].startswith('LIT'))
seen = {(re.sub(r'\([^)]*\)', '', w['title']).strip().lower(), w['artist'].lower()) for w in d}
added, probs = [], []
for k in N:
    p = []
    if not all(norm(x) in norm(k['fullText']) for x in k['hook'].split('…') if len(norm(x)) > 3): p.append('hook not in fullText')
    if '"' in k['note']: p.append('quote marks in note')
    line = LINES.get(f"{B}-{k['key']}")
    if k.get('labelOnly') and not k.get('note','').strip(): pass
    elif not line or line['note'].strip() != k['note'].strip(): p.append('note not saved through save_line (or differs)')
    key = (re.sub(r'\([^)]*\)', '', k['title']).strip().lower(), k['artist'].lower())
    if key in seen: p.append('duplicate')
    if p: probs.append((k['key'], k['title'], p)); continue
    seen.add(key); nid += 1
    cf = k['colorFamily']
    r = {'id': f'LIT-{nid}', 'pocketNo': f'POCKET POETS · NO. {nid}', 'itemType': 'literature', 'title': k['title'], 'artist': k['artist'], 'dateLabel': k['dateLabel'], 'yearNum': k['yearNum'], 'eraBucket': era(int(k['yearNum'])),
         'colorFamily': cf, 'graphicForm': k['graphicForm'], 'craftSpec': '', 'searchTags': 'literature poetry prose quote ' + k['graphicForm'].lower() + ' ' + k.get('tags', ''),
         'region': k['region'], 'medium': k['medium'], 'subjectShort': k['subjectShort'], 'emotionShort': k['emotionShort'], 'macroRegion': k['macroRegion'], 'macroMedium': 'Literature & Verse',
         'hook': k['hook'], 'excerpt': k['hook'], 'fullText': k['fullText'], 'originalScript': k.get('originalScript', ''), 'scriptName': k.get('scriptName', ''), 'imageUrl': '', 'highResUrl': k['sourceUrl'], 'sourceUrl': k['sourceUrl'],
         'museum': 'Pocket Poets Canon', 'note': k['note'], 'quote': k['hook'], 'quoteAuthor': f"{k['artist']} — {k['title']} ({k['dateLabel']})", 'palette': pal[cf], 'iconicScore': 145, 'isSeed': True,
         'shelf': k['shelf'], 'audit': 'quoted' if k.get('quoted') else 'verified', 'auditNote': k['auditNote'], 'noteRev': 4, 'noteSource': (line or {}).get('source',''), 'grow': 'words'}
    if k.get('translator'): r['translator'] = k['translator']
    if k.get('license'): r['license'] = k['license']
    if k.get('labelOnly'): r['labelOnly'] = True
    d.append(r); added.append((r['id'], k['artist'], k['title']))
print(B, 'ok', len(added), 'problems', len(probs))
for x in probs: print('  ', x)
if APPLY:
    open(P, 'w', encoding='utf8').write(s[:a] + json.dumps(d, ensure_ascii=False, separators=(',', ':')) + s[b:])
    print('added', added[0][0] if added else None, '...', added[-1][0] if added else None)
