"""Build one static page per work in w/<slug>.html, plus sitemap.xml and robots.txt.

Run from the repo root after any change to data/works.js (it also stamps
the data file's version into index.html, so browsers never pair new code with a cached library):
    python3 tools/build_pages.py

Each work gets a stable `slug` stored back into data/works.js (never changed once set,
so shared links keep working). The page shows the image, the museum label and the note
for art; the pull quote, credit and note for writing. It never shows a full text, so
writing still in copyright stays at the one-line quote. Each page links into the app
at index.html#w/<id>, which opens the work.

A page is also a front door (25 Nov 2026): most strangers arrive on one from a search
engine or a shared link, so under the work it shows More like this (data/similar.json),
more by the same maker, the wordmark and a search box that lead onto the wall, and the
full-size file for art. Every neighbour is a plain link to that work's own page, so the
pages link to each other and a crawler can walk the whole collection.
"""
import html, json, os, re, unicodedata
from urllib.parse import quote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://www.paulmartincurry.com/artchive/'
# GitHub Pages still serves the files (paulmartincurry.com/artchive is a Vercel rewrite of it); a visitor who lands on github.io is sent on.
MOVE = '<script>if(location.hostname.endsWith("github.io"))location.replace("https://www.paulmartincurry.com"+location.pathname+location.search+location.hash)</script>'
DATA = os.path.join(ROOT, 'data', 'works.js')

def slugify(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode()
    s = re.sub(r'\(.*?\)', '', s.lower())
    s = re.sub(r'[^a-z0-9]+', '-', s).strip('-')
    return '-'.join(s.split('-')[:10])

def esc(s):
    return html.escape(s or '', quote=True)

def thumb(w):
    """A small picture for a row of neighbours: each holder's own 400 px size where it serves one (checked 25 Nov 2026)."""
    u = w.get('imageUrl') or ''
    if not u.startswith('http'):
        return '../' + u if u else ''
    u = re.sub(r'/\d+,/0/default\.jpg$', '/400,/0/default.jpg', u)                      # IIIF: NGA, Chicago, Getty, Rijksmuseum, SMK, LoC, Wellcome, NYPL
    u = re.sub(r'([?&]max=)\d+', r'\g<1>400', u)                                      # Smithsonian
    u = re.sub(r'(upload\.wikimedia\.org/.*/thumb/.*/)\d+px-', r'\g<1>330px-', u)    # Commons serves only its standard widths
    return u

NO_MAKER = re.compile(r'^(?:Maker unknown|Anonymous|Unknown|Traditional|Various)\b', re.I)

def neighbour(o, same_maker=False):
    """One neighbour as a link to its own page: a picture for art, the start of the pull quote for writing
    (credited to its writer, or to its title when the whole row is one writer)."""
    alt = esc(' by '.join(x for x in [o.get('title'), o.get('artist')] if x))
    if o.get('itemType') == 'literature':
        hook = ' '.join((o.get('hook') or '').split())
        cut = hook if len(hook) <= 90 else hook[:90].rsplit(' ', 1)[0] + '…'
        return f'<a class="ln" href="{o["slug"]}.html"><span>“{esc(cut)}”</span> <em>{esc((o.get("title") if same_maker else o.get("artist")) or "")}</em></a>'
    try:
        ar = min(2.2, max(0.5, float(o.get('ar') or 1)))
    except (TypeError, ValueError):
        ar = 1
    return f'<a href="{o["slug"]}.html" title="{alt}"><img loading="lazy" decoding="async" src="{esc(thumb(o))}" alt="{alt}" style="width:{round(112 * ar)}px"></a>'

def main():
    raw = open(DATA, encoding='utf-8').read()
    a, b = raw.index('['), raw.rindex(']') + 1
    works = json.loads(raw[a:b])

    used = {w['slug'] for w in works if w.get('slug')}
    for w in works:
        if w.get('slug'):
            continue
        base = slugify(w['title']) or w['id'].lower()
        maker = slugify(re.split(r'[;,(]', w.get('artist') or '')[0])
        cand = base if base not in used else f'{base}-{maker}' if maker else base
        n = 2
        while cand in used:
            cand = f'{base}-{n}'; n += 1
        w['slug'] = cand
        used.add(cand)

    open(DATA, 'w', encoding='utf-8').write(raw[:a] + json.dumps(works, ensure_ascii=False, separators=(',', ':')) + raw[b:])

    by_id = {w['id']: w for w in works}
    near = {}
    try:
        sim = json.load(open(os.path.join(ROOT, 'data', 'similar.json'), encoding='utf-8'))
        near = {i: [sim['ids'][k] for k in nb] for i, nb in zip(sim['ids'], sim['nb'])}
    except (OSError, ValueError, KeyError, IndexError):
        pass
    by_maker = {}
    for w in works:
        m = w.get('artist') or ''
        if m and not NO_MAKER.match(m):
            by_maker.setdefault((m, w.get('itemType') == 'literature'), []).append(w)
    for v in by_maker.values():
        v.sort(key=lambda o: -float(o.get('fame') or o.get('iconicScore') or 0))

    out = os.path.join(ROOT, 'w')
    os.makedirs(out, exist_ok=True)
    keep = set()
    for w in works:
        is_lit = w.get('itemType') == 'literature'
        title, maker = w.get('title') or '', w.get('artist') or ''
        note = w.get('note') or ''
        hook = (w.get('hook') or '').strip()
        label = [x for x in [maker, w.get('dateLabel'), None if is_lit else w.get('medium'), None if is_lit else w.get('dimensions'), None if is_lit else w.get('museum')] if x]
        desc = (hook.replace('\n', ' / ') if is_lit else note) or ', '.join(label)
        desc = desc[:200]
        img = '' if is_lit else (w.get('imageUrl') or '')
        page_img = img if img.startswith('http') else ('../' + img if img else '')
        if img and not img.startswith('http'):
            img = SITE + img
        app = f'../index.html#w/{w["id"]}'
        credit = ''
        if is_lit:
            bits = [w.get('translator') and f'Translated by {w["translator"]}', w.get('license')]
            credit = ' · '.join(x for x in bits if x)
        pc = f'Photo: {w["photoCredit"]}' if w.get('photoCredit') else ''
        if is_lit:
            rights = ''
        elif w.get('fairUse'):
            rights = ' · '.join(x for x in [w.get('rights') or 'In copyright. Look and learn: shown for study, not for download.', pc] if x)
        elif w.get('rightsTier') == 'free':
            rights = f'Free to use with credit. {pc}' if pc else 'Free to use'
        else:
            rights = ''
        body = []
        if img:
            body.append(f'<a href="{app}"><img class="hero" src="{esc(page_img)}" alt="{esc(title)} by {esc(maker)}"></a>')
        if is_lit and hook:
            body.append('<blockquote>' + '<br>'.join(esc(l) for l in hook.split('\n')) + '</blockquote>')
        body.append(f'<h1>{esc(title)}</h1>')
        body.append(f'<p class="label">{esc(" · ".join(label))}</p>')
        if credit:
            body.append(f'<p class="label">{esc(credit)}</p>')
        if rights:
            body.append(f'<p class="label">{esc(rights)}</p>')
        if note:
            body.append(f'<p class="note">{esc(note)}</p>')
        full = '' if is_lit or w.get('rightsTier') != 'free' else (w.get('highResUrl') or w.get('imageUrl') or '')
        if full and not full.startswith('http'):
            full = '../' + full
        body.append(f'<p class="go"><a href="{app}">Open in The Artchive</a>' + (f'<a href="{esc(full)}" target="_blank" rel="noopener">Full-size file ↗</a>' if full else '') + '</p>')
        # The front door: neighbours, the maker's other work, and the way onto the wall.
        like = [by_id[i] for i in near.get(w['id'], []) if i in by_id and by_id[i].get('slug')][:4 if is_lit else 6]
        row = 'lines' if is_lit else 'row'
        if like:
            body.append(f'<section><h2>More like this</h2><div class="{row}">' + ''.join(neighbour(o) for o in like) + '</div></section>')
        mine_all = [o for o in by_maker.get((maker, is_lit), []) if o is not w]
        shown = {o['id'] for o in like}
        mine = [o for o in mine_all if o['id'] not in shown and o.get('slug')][:4 if is_lit else 6]
        if mine:
            more = f'<a class="all" href="../index.html?q={quote(maker)}">All {len(mine_all) + 1} on the wall</a>' if len(mine_all) > len(mine) else ''
            body.append(f'<section><h2>More by {esc(maker)}</h2><div class="{row}">' + ''.join(neighbour(o, True) for o in mine) + f'</div>{more}</section>')
        page = f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
{MOVE}
<link rel="icon" href="{SITE}favicon.svg" type="image/svg+xml"><link rel="icon" href="{SITE}favicon-32.png" sizes="32x32" type="image/png"><link rel="apple-touch-icon" href="{SITE}apple-touch-icon.png">
<title>{esc(title)} — {esc(maker)} · The Artchive</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{SITE}w/{w["slug"]}.html">
<meta property="og:title" content="{esc(title)} — {esc(maker)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:type" content="article">
<meta property="og:url" content="{SITE}w/{w["slug"]}.html">
{f'<meta property="og:image" content="{esc(img)}"><meta name="twitter:card" content="summary_large_image">' if img else '<meta name="twitter:card" content="summary">'}
<style>
body{{margin:0;background:#0b0b0c;color:#eae8e3;font-family:Georgia,'Times New Roman',serif;line-height:1.55}}
header,main,footer{{max-width:760px;margin:0 auto;padding-left:22px;padding-right:22px}}
header{{display:flex;align-items:center;justify-content:space-between;gap:20px;padding-top:22px;font-family:-apple-system,Helvetica,Arial,sans-serif}}
.wm{{font-size:.8rem;letter-spacing:.32em;text-transform:uppercase;text-decoration:none;white-space:nowrap}}
header input{{width:170px;max-width:42vw;background:none;border:0;border-bottom:1px solid #3a3936;color:#eae8e3;font:inherit;font-size:.85rem;padding:6px 2px;border-radius:0;outline:0}}
header input:focus{{border-bottom-color:#eae8e3}}
header input::placeholder{{color:#8a8780}}
main{{padding-top:34px;padding-bottom:20px}}
.hero{{display:block;max-width:100%;max-height:78vh;margin:0 auto 28px;{"max-width:" + str(int(w["imageW"] * 1.5)) + "px;" if w.get("fairUse") and w.get("imageW") else ""}}}
blockquote{{margin:0 0 28px;font-size:1.35rem;line-height:1.5}}
h1{{font-weight:400;font-size:1.5rem;margin:0 0 6px}}
.label{{font-family:-apple-system,Helvetica,Arial,sans-serif;font-size:.82rem;color:#8a8780;margin:0 0 4px}}
.note{{margin:22px 0 0;color:#cfccc5}}
.go{{margin-top:30px;font-family:-apple-system,Helvetica,Arial,sans-serif;font-size:.85rem}}
.go a{{margin-right:22px}}
a{{color:#eae8e3}}
section{{margin-top:46px;padding-top:22px;border-top:1px solid #232220}}
h2{{font-family:-apple-system,Helvetica,Arial,sans-serif;font-weight:400;font-size:.68rem;letter-spacing:.16em;text-transform:uppercase;color:#8a8780;margin:0 0 16px}}
.row{{display:flex;flex-wrap:wrap;gap:10px}}
.row a{{display:block;line-height:0;background:#141416}}
.row img{{display:block;height:112px;object-fit:cover;opacity:.92;font-size:0;color:transparent}}
.row a:hover img{{opacity:1}}
.lines a{{display:block;text-decoration:none;margin:0 0 14px;font-size:1.05rem;line-height:1.45}}
.lines em{{display:block;margin-top:3px;font-family:-apple-system,Helvetica,Arial,sans-serif;font-style:normal;font-size:.76rem;color:#8a8780}}
.all{{display:inline-block;margin-top:16px;font-family:-apple-system,Helvetica,Arial,sans-serif;font-size:.8rem;color:#8a8780}}
footer{{margin-top:54px;padding-top:22px;padding-bottom:64px;border-top:1px solid #232220;font-family:-apple-system,Helvetica,Arial,sans-serif;font-size:.82rem;color:#8a8780}}
footer a{{margin-left:10px}}
</style></head>
<body>
<header><a class="wm" href="../index.html">The Artchive</a><form action="../index.html" method="get" role="search"><input type="search" name="q" placeholder="Search" aria-label="Search The Artchive" autocomplete="off"></form></header>
<main>
{chr(10).join(body)}
</main>
<footer>An archive of art, works, and words.<a href="../index.html">See the wall</a></footer>
<script>document.querySelectorAll('.row img').forEach(function(i){{function h(){{i.parentNode.style.display='none'}}i.addEventListener('error',h);if(i.complete&&!i.naturalWidth&&i.currentSrc)h()}})</script>
</body></html>
'''
        fn = f'{w["slug"]}.html'
        keep.add(fn)
        p = os.path.join(out, fn)
        if not os.path.exists(p) or open(p, encoding='utf-8').read() != page:
            open(p, 'w', encoding='utf-8').write(page)
    for fn in os.listdir(out):
        if fn.endswith('.html') and fn not in keep:
            os.remove(os.path.join(out, fn))

    # The site loads a slim copy of the library (data/site.js); data/works.js stays the full master record
    # with provenance fields the app never reads (auditNote unless it is shown, noteSource, craftSpec, etc.).
    DROP = {'noteSource', 'rawImageUrl', 'rawHighResUrl', 'crop', 'isSeed', 'noteRev', 'olderAuditNote', 'mediumUnchecked', 'license', 'craftSpec', 'grow',
            'seeText', 'colorFamilyOld', 'paletteOld'}  # seeText ships separately in data/see.json, loaded after the wall
    slim = []
    texts = {}   # full texts ship in data/texts.json, loaded just after the wall appears (speed pass, 21 Nov 2026)
    for w in works:
        r = {k: v for k, v in w.items() if k not in DROP}
        if r.get('itemType') == 'literature' and (r.get('fullText') or r.get('olderText')):
            texts[r['id']] = [r.pop('fullText', '') or ''] + ([r.pop('olderText')] if r.get('olderText') else [])
        if r.get('auditNote') and r.get('audit') not in ('attribution', 'unconfirmed'):
            del r['auditNote']
        if r.get('itemType') == 'literature':
            # Fields the app rebuilds on load (index.html, just after SEED_WORKS): drop them only when equal.
            derived = {'quote': r.get('hook'), 'quoteAuthor': f"{r.get('artist')} — {r.get('title')} ({r.get('dateLabel')})",
                       'highResUrl': r.get('sourceUrl', ''), 'excerpt': r.get('hook') or '',
                       'pocketNo': f"POCKET POETS · NO. {int(r['id'][4:])}" if re.fullmatch(r'LIT-\d+', r['id']) else None}
            for k, v in derived.items():
                if k in r and v is not None and r[k] == v:
                    del r[k]
        slim.append(r)
    site_js = 'window.SEED_WORKS=' + json.dumps(slim, ensure_ascii=False, separators=(',', ':')) + ';\n'
    texts_json = json.dumps(texts, ensure_ascii=False, separators=(',', ':'))
    TEXTS = os.path.join(ROOT, 'data', 'texts.json')
    if not os.path.exists(TEXTS) or open(TEXTS, encoding='utf-8').read() != texts_json:
        open(TEXTS, 'w', encoding='utf-8').write(texts_json)
    SITE_DATA = os.path.join(ROOT, 'data', 'site.js')
    if not os.path.exists(SITE_DATA) or open(SITE_DATA, encoding='utf-8').read() != site_js:
        open(SITE_DATA, 'w', encoding='utf-8').write(site_js)
    # Stamp the data file's version into index.html so a push never runs fresh code on a cached library.
    import hashlib
    # data/placards.json is fetched with the same stamp, so a change to it changes the stamp too
    PLAC = os.path.join(ROOT, 'data', 'placards.json')
    plac = open(PLAC, encoding='utf-8').read() if os.path.exists(PLAC) else ''
    ver = hashlib.sha1((site_js + texts_json + plac).encode('utf-8')).hexdigest()[:10]
    ip = os.path.join(ROOT, 'index.html')
    ih = open(ip, encoding='utf-8').read()
    ih2 = re.sub(r'<script src="data/(?:works|site)\.js(\?v=[0-9a-f]+)?"></script>', f'<script src="data/site.js?v={ver}"></script>', ih)
    if ih2 != ih:
        open(ip, 'w', encoding='utf-8').write(ih2)

    urls = [SITE] + [f'{SITE}w/{w["slug"]}.html' for w in works]
    open(os.path.join(ROOT, 'sitemap.xml'), 'w').write(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + ''.join(f'<url><loc>{u}</loc></url>\n' for u in urls) + '</urlset>\n')
    open(os.path.join(ROOT, 'robots.txt'), 'w').write(f'User-agent: *\nAllow: /\nSitemap: {SITE}sitemap.xml\n')
    print(len(works), 'pages')

if __name__ == '__main__':
    main()
