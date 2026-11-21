"""Build one static page per work in w/<slug>.html, plus sitemap.xml and robots.txt.

Run from the repo root after any change to data/works.js (it also stamps
the data file's version into index.html, so browsers never pair new code with a cached library):
    python3 tools/build_pages.py

Each work gets a stable `slug` stored back into data/works.js (never changed once set,
so shared links keep working). The page shows the image, the museum label and the note
for art; the pull quote, credit and note for writing. It never shows a full text, so
writing still in copyright stays at the one-line quote. Each page links into the app
at index.html#w/<id>, which opens the work.
"""
import html, json, os, re, unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://paulmartincurry.github.io/artchive/'
DATA = os.path.join(ROOT, 'data', 'works.js')

def slugify(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode()
    s = re.sub(r'\(.*?\)', '', s.lower())
    s = re.sub(r'[^a-z0-9]+', '-', s).strip('-')
    return '-'.join(s.split('-')[:10])

def esc(s):
    return html.escape(s or '', quote=True)

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
            body.append(f'<a href="{app}"><img src="{esc(page_img)}" alt="{esc(title)} by {esc(maker)}"></a>')
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
        body.append(f'<p class="go"><a href="{app}">Open in The Artchive</a></p>')
        page = f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
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
main{{max-width:760px;margin:0 auto;padding:40px 22px 64px}}
img{{display:block;max-width:100%;max-height:78vh;margin:0 auto 28px;{"max-width:" + str(int(w["imageW"] * 1.5)) + "px;" if w.get("fairUse") and w.get("imageW") else ""}}}
blockquote{{margin:0 0 28px;font-size:1.35rem;line-height:1.5}}
h1{{font-weight:400;font-size:1.5rem;margin:0 0 6px}}
.label{{font-family:-apple-system,Helvetica,Arial,sans-serif;font-size:.82rem;color:#8a8780;margin:0 0 4px}}
.note{{margin:22px 0 0;color:#cfccc5}}
.go{{margin-top:30px;font-family:-apple-system,Helvetica,Arial,sans-serif;font-size:.85rem}}
a{{color:#eae8e3}}
</style></head>
<body><main>
{chr(10).join(body)}
</main></body></html>
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
    DROP = {'noteSource', 'isSeed', 'noteRev', 'olderAuditNote', 'mediumUnchecked', 'license', 'craftSpec', 'grow',
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
    ver = hashlib.sha1((site_js + texts_json).encode('utf-8')).hexdigest()[:10]
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
