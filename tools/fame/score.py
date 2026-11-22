"""Recognition score for the writing, from Bartlett's Familiar Quotations (10th ed., 1919, and the
# Run from a working folder holding bart1922.txt and bart1914.txt (archive.org: familia00bart and
# familiarquotati00dolegoog, the _djvu.txt files) and publictest.json. Then write 'fame' into works.js and run build_pages.
1914 printing, both open on archive.org). Three signals, each read from the books, not guessed:
  line  - share of the pull quote's 5-word runs that Bartlett's prints (the line itself is famous)
  work  - whether any 7-word run of the longer passage is in Bartlett's (the work is quoted)
  maker - how often the writer's surname appears (how much room the canon gives them)
Pieces added in the public-test rounds (AUDIT.md) as works people search for get a floor of 65.
Writes pop/fame.json: {id: {fame 0-100, line, work, maker}}."""
import json, re, math, sys, collections

def norm(t):
    t = t.lower().replace('ſ', 's')
    t = re.sub(r"[’'`]", '', t)
    return re.sub(r'[^a-z]+', ' ', t).split()

bart = []
for f in ('bart1922.txt', 'bart1914.txt'):
    bart += norm(open(f, encoding='utf-8', errors='ignore').read())
print('bartlett words', len(bart), file=sys.stderr)

def grams(ws, n):
    return {' '.join(ws[i:i + n]) for i in range(len(ws) - n + 1)}

G5, G7 = grams(bart, 5), grams(bart, 7)
count = collections.Counter(bart)

src = open('/home/claude/artchive/data/works.js', encoding='utf-8').read()
works = json.loads(src[src.index('['):src.rindex(']') + 1])
lit = [w for w in works if w.get('shelf')]
tx = {}
try:
    tx = json.load(open('/home/claude/artchive/data/texts.json'))
except Exception:
    pass

STOP = {'the', 'of', 'and', 'de', 'von', 'van', 'la', 'le', 'unknown', 'anonymous', 'maker', 'sir', 'saint', 'st'}
out = {}
PT = set(json.load(open('publictest.json')))
for w in lit:
    hook = norm(w.get('hook', ''))
    g = grams(hook, 5)
    line = (sum(1 for x in g if x in G5) / len(g)) if g else 0.0
    full = w.get('fullText') or (tx.get(w['id'], {}) or {}).get('fullText', '') if isinstance(tx.get(w['id']), dict) else w.get('fullText', '')
    fw = norm(full or '')
    work = 1.0 if any(x in G7 for x in grams(fw, 7)) else 0.0
    if not work and line >= 0.3:
        work = 1.0
    name = re.sub(r'\(.*?\)', '', w.get('artist', ''))
    parts = [p for p in norm(name) if p not in STOP and len(p) > 2]
    FIRST = {'john','william','thomas','james','george','robert','henry','charles','edward','richard','samuel','mary','elizabeth','walter','joseph','francis','alexander','lord','emily','christina'}
    cand = [p for p in parts if p not in FIRST] or parts[-1:]
    sur = max(cand, key=lambda p: count.get(p, 0)) if cand else ''
    maker = count.get(sur, 0) if sur else 0
    m = min(1.0, math.log1p(maker) / math.log1p(400))   # about 400 mentions is the top of the canon
    fame = round(100 * (0.55 * min(1.0, line * 1.6) + 0.25 * work + 0.20 * m))
    if w['id'] in PT: fame = min(100, max(fame, 55) + 10)   # added in the public-test rounds as a piece people look for
    out[w['id']] = {'fame': fame, 'line': round(line, 2), 'work': work, 'maker': maker, 'sur': sur}

json.dump(out, open('fame.json', 'w'), indent=0)
vals = sorted(v['fame'] for v in out.values())
print('n', len(vals), 'p25/50/75/90', [vals[int(len(vals) * q)] for q in (.25, .5, .75, .9)], file=sys.stderr)
print('line>=.5:', sum(v['line'] >= .5 for v in out.values()), ' work:', sum(v['work'] for v in out.values()), file=sys.stderr)
