"""Merge a round's records into works.js. Usage: python3 merge.py r1a [--apply]"""
import json, re, sys, os
R = sys.argv[1]; APPLY = '--apply' in sys.argv
P = '/home/claude/artchive/data/works.js'; ROOT = '/home/claude/artchive/'
s = open(P, encoding='utf-8').read(); d = json.loads(s[s.index('['):s.rindex(']') + 1])
V = json.load(open('/home/claude/big/vocab.json'))
recs = json.load(open(f'/home/claude/big/{R}/records.json'))
def key(t, a): return re.sub(r'[^a-z0-9]', '', re.sub(r'\(.*?\)', '', t or '').lower()) + '|' + re.sub(r'[^a-z0-9]', '', re.sub(r'\(.*?\)', '', a or '').lower())
have = {key(w['title'], w['artist']): w['id'] for w in d}
imgs = {w.get('imageUrl'): w['id'] for w in d if w.get('imageUrl')}
REQ = ['title', 'artist', 'dateLabel', 'yearNum', 'eraBucket', 'graphicForm', 'region', 'medium', 'subjectShort', 'emotionShort', 'macroRegion', 'macroMedium', 'imageUrl', 'sourceUrl', 'palette', 'colorFamily', 'searchTags', 'auditNote', 'rightsTier']
def era(y):
    return 'Ancient & Medieval' if y < 1400 else '1400–1650' if y < 1650 else '1650–1800' if y < 1800 else '1800–1920' if y <= 1920 else '1920–Now'
ok, bad = [], []
seen = set()
for r in recs:
    p = []
    for f in REQ:
        if f=='medium' and r.get('mediumBlank'): continue  # a blank medium is allowed when no source states it
        if r.get(f) in (None, '', []): p.append('missing ' + f)
    try: r['yearNum'] = int(r['yearNum'])
    except Exception: p.append('yearNum')
    if not p and r['eraBucket'] != era(r['yearNum']): r['eraBucket'] = era(r['yearNum'])
    for f, vk in [('subjectShort', 'subjectShort'), ('emotionShort', 'emotionShort'), ('macroRegion', 'macroRegion'), ('macroMedium', 'macroMedium'), ('graphicForm', 'graphicForm'), ('colorFamily', 'colorFamily')]:
        if r.get(f) and r[f] not in V[vk]: p.append(f'bad {f}={r[f]}')
    k = key(r.get('title'), r.get('artist'))
    if k in have: p.append('duplicate of ' + have[k])
    if k in seen: p.append('duplicate inside batch')
    seen.add(k)
    if r.get('imageUrl') in imgs: p.append('same image as ' + imgs[r['imageUrl']])
    if r.get('rightsTier') not in ('free', 'look'): p.append('rightsTier')
    if r.get('rightsTier') == 'look':
        if not r.get('fairUse'): p.append('look without fairUse')
        if not r.get('note'): p.append('look without note')
        if r.get('highResUrl'): r['highResUrl'] = ''
        r.setdefault('rights', 'In copyright. Look and learn: shown for study, not for download.')
    if r.get('imageUrl') and not r['imageUrl'].startswith('http') and not os.path.exists(ROOT + r['imageUrl']): p.append('local image missing ' + r['imageUrl'])
    if r.get('note'):
        if not r.get('noteSource'): p.append('note without noteSource')
        r['noteRev'] = 4
    else:
        r['labelOnly'] = True; r['note'] = ''
    if r.get('photoCredit') and re.search(r'(?i)unknown|=|\[\[|\{\{', r['photoCredit']): p.append('odd photoCredit ' + r['photoCredit'])
    (bad if p else ok).append((r, p))
print(R, 'ok', len(ok), 'problems', len(bad))
for r, p in bad: print('  ', r.get('pid'), (r.get('title') or '')[:50], '|', '; '.join(p))
if APPLY:
    n = max(int(w['id'][6:]) for w in d if w['id'].startswith('VAULT-'))
    added = []
    for r, _ in ok:
        n += 1
        rec = {'id': f'VAULT-{n}', 'itemType': 'art'}
        for f, v in r.items():
            if f in ('pid', 'id', 'itemType'): continue
            rec[f] = v
        rec.setdefault('craftSpec', ''); rec.setdefault('isPantheon', True); rec.setdefault('isSeed', True); rec.setdefault('audit', 'verified'); rec.setdefault('highResUrl', rec['imageUrl'] if rec.get('rightsTier') == 'free' else '')
        rec.setdefault('iconicScore', 230); rec.setdefault('museum', '')
        rec['_pid'] = r.get('pid')
        d.append(rec); added.append(rec['id'])
    for w in d: w.pop('_pid', None)
    open(P, 'w', encoding='utf-8').write(s[:s.index('[')] + json.dumps(d, ensure_ascii=False, separators=(',', ':')) + s[s.rindex(']') + 1:])
    json.dump({r.get('pid'): i for (r, _), i in zip(ok, added)}, open(f'/home/claude/big/{R}/merged_ids.json', 'w'))
    print('added', added[0] if added else None, '...', added[-1] if added else None, len(added))
