"""One way in to the open collections the site draws on.

Every function returns records in the same shape:
    dict(source, id, title, maker, date, year, medium, dimensions, holder, credit,
         description, provenance, imageUrl, highResUrl, sourceUrl, rights, open)
`open` is True only when the holder itself marks the image as free to reuse.
Nothing here writes to the site; tools that add works call these and then decide.

Sources (tested from the work sandbox, 16 Nov 2026):
  nga()    National Gallery of Art, Washington. Bulk CSVs from its GitHub open-data
           repo, cached in ~/src/nga (about 220 MB). `openaccess=1` is CC0.
  rijks()  Rijksmuseum. Linked Art API at data.rijksmuseum.nl, no key. Public-domain
           images are free to reuse; titles are often Dutch only.
  vam()    Victoria and Albert Museum. api.vam.ac.uk v2, no key. Images are under the
           V&A's own terms (free for non-commercial use), so `open` is False: use the
           record, and the image only with care.
  loc()    Library of Congress Prints & Photographs, loc.gov/pictures JSON. Only items
           marked "No known restrictions" count as open.
  si()     Smithsonian Open Access (all Smithsonian museums: Cooper Hewitt, the Freer
           and Sackler, American Art, Portrait Gallery, African Art...). Needs Paul's
           api.data.gov key, read from $SI_API_KEY or ~/.config/artchive/si_key. The key
           must never go into this repo: the repo is public. Images marked CC0 are open.
  met(), aic(), cma() for the three museums the site started with live in
  ~/grow/harvest.py.
"""
import csv, json, os, re, subprocess, urllib.parse

UA = 'ArtchiveSourcing/1.0 (personal art site; github paulmartincurry/artchive)'

def get(url, accept=None, timeout=40):
    cmd = ['curl', '-s', '-L', '-m', str(timeout), '-A', UA]
    if accept:
        cmd += ['-H', f'Accept: {accept}']
    out = subprocess.run(cmd + [url], capture_output=True, text=True).stdout
    try:
        return json.loads(out)
    except Exception:
        return None

def year_of(s):
    m = re.search(r'(\d{3,4})', s or '')
    return int(m.group(1)) if m else None

# ---------------------------------------------------------------- NGA
NGA_DIR = os.path.expanduser('~/src/nga')
_nga = None

def _nga_load():
    global _nga
    if _nga:
        return _nga
    os.makedirs(NGA_DIR, exist_ok=True)
    for f in ('objects', 'published_images'):
        p = os.path.join(NGA_DIR, f + '.csv')
        if not os.path.exists(p):
            subprocess.run(['curl', '-s', '-o', p, f'https://raw.githubusercontent.com/NationalGalleryOfArt/opendata/main/data/{f}.csv'])
    csv.field_size_limit(10 ** 9)
    objs = {r['objectid']: r for r in csv.DictReader(open(os.path.join(NGA_DIR, 'objects.csv'), encoding='utf-8'))}
    imgs = {}
    for r in csv.DictReader(open(os.path.join(NGA_DIR, 'published_images.csv'), encoding='utf-8')):
        if r['viewtype'] == 'primary':
            imgs[r['depictstmsobjectid']] = r
    _nga = (objs, imgs)
    return _nga

def _nga_rec(o, im):
    base = im['iiifurl'] if im else ''
    w = int(im['width']) if im and im['width'] else 0
    return dict(source='nga', id=o['objectid'], title=o['title'], maker=o['attribution'], date=o['displaydate'],
                year=int(o['beginyear']) if o['beginyear'] else year_of(o['displaydate']), medium=o['medium'],
                dimensions=o['dimensions'], holder='National Gallery of Art, Washington', credit=o['creditline'],
                description=o['inscription'], provenance=o['provenancetext'],
                imageUrl=f'{base}/full/{min(w, 960) if w else 960},/0/default.jpg' if base else '',
                highResUrl=f'{base}/full/max/0/default.jpg' if base else '',
                sourceUrl=f'https://www.nga.gov/collection/art-object-page.{o["objectid"]}.html',
                rights='CC0' if im and im['openaccess'] == '1' else '', open=bool(im and im['openaccess'] == '1'),
                accession=o['accessionnum'], classification=o['classification'])

def nga(maker=None, title=None, open_only=True, limit=200):
    objs, imgs = _nga_load()
    out = []
    for o in objs.values():
        if maker and maker.lower() not in (o['attribution'] + ' ' + o['attributioninverted']).lower():
            continue
        if title and title.lower() not in o['title'].lower():
            continue
        im = imgs.get(o['objectid'])
        if open_only and not (im and im['openaccess'] == '1'):
            continue
        out.append(_nga_rec(o, im))
        if len(out) >= limit:
            break
    return out

# ---------------------------------------------------------------- Rijksmuseum
def _la_name(obj, prefer_en=True):
    names = [n for n in obj.get('identified_by', []) if n.get('type') == 'Name']
    en = [n for n in names if any('300388277' in (l.get('id') or '') for l in n.get('language', []))]
    pick = (en or names or [{}])[0]
    return pick.get('content', '')

def rijks_record(uri):
    j = get(uri, 'application/ld+json')
    if not j:
        return None
    prod = j.get('produced_by') or {}
    parts = prod.get('part') or [prod]
    makers = []
    for p in parts:
        for c in p.get('carried_out_by', []):
            n = [x['@value'] for x in c.get('notation', []) if x.get('@language') == 'en'] or [x['@value'] for x in c.get('notation', [])]
            if n:
                makers.append(n[0])
    ts = prod.get('timespan') or {}
    date = ''
    for x in ts.get('identified_by', []):
        date = x.get('content', '') or date
    dims = []
    for d in j.get('dimension', []):
        lab = [x['@value'] for x in (d.get('classified_as') or [{}])[0].get('notation', []) if x.get('@language') == 'en']
        dims.append(f"{lab[0] if lab else ''} {d.get('value')}")
    mats = []
    for m in j.get('made_of', []):
        en = [x['@value'] for x in m.get('notation', []) if x.get('@language') == 'en']
        if en:
            mats.append(en[0])
    texts = [r.get('content', '') for r in j.get('referred_to_by', []) if r.get('content')]
    img = ''
    for v in j.get('shows', []):
        vi = get(v['id'], 'application/ld+json') or {}
        for do in vi.get('digitally_shown_by', []):
            dj = get(do['id'], 'application/ld+json') or {}
            for ap in dj.get('access_point', []):
                img = ap.get('id', '')
    acc = next((n.get('content') for n in j.get('identified_by', []) if n.get('type') == 'Identifier'), '')
    return dict(source='rijks', id=uri.rsplit('/', 1)[-1], title=_la_name(j), maker=', '.join(makers), date=date,
                year=year_of(date), medium=' on '.join(reversed(mats)) if len(mats) == 2 else ', '.join(mats), dimensions='; '.join(dims), holder='Rijksmuseum, Amsterdam',
                credit=next((t for t in texts if t.startswith('Purchased') or t.startswith('Gift') or t.startswith('Bequest')), ''),
                description=' | '.join(texts), provenance='',
                imageUrl=img.replace('/full/max/', '/full/960,/') if img else '', highResUrl=img,
                sourceUrl=f'https://www.rijksmuseum.nl/en/collection/{acc}' if acc else uri,
                rights='Public domain (Rijksmuseum)' if img else '', open=bool(img), accession=acc)

def rijks(creator=None, title=None, limit=20):
    q = {'imageAvailable': 'true'}
    if creator:
        q['creator'] = creator
    if title:
        q['title'] = title
    j = get('https://data.rijksmuseum.nl/search/collection?' + urllib.parse.urlencode(q)) or {}
    ids = [x['id'] for x in j.get('orderedItems', [])][:limit]
    return [r for r in (rijks_record(i) for i in ids) if r]

# ---------------------------------------------------------------- V&A
def vam(q, limit=20):
    j = get('https://api.vam.ac.uk/v2/objects/search?' + urllib.parse.urlencode({'q': q, 'images_exist': 1, 'page_size': limit})) or {}
    out = []
    for r in j.get('records', []):
        rec = (get(f'https://api.vam.ac.uk/v2/object/{r["systemNumber"]}') or {}).get('record') or {}
        img = (r.get('_images') or {}).get('_iiif_image_base_url', '')
        dates = rec.get('productionDates') or [{}]
        out.append(dict(source='vam', id=r['systemNumber'], title=(rec.get('titles') or [{}])[0].get('title') or r.get('_primaryTitle', ''),
                        maker=', '.join(p['name']['text'] for p in rec.get('artistMakerPerson', [])), date=dates[0].get('date', {}).get('text', ''),
                        year=year_of(dates[0].get('date', {}).get('text', '')), medium=rec.get('materialsAndTechniques', ''),
                        dimensions='; '.join(f"{d['dimension']} {d['value']} {d['unit']}" for d in rec.get('dimensions', [])),
                        holder='Victoria and Albert Museum, London', credit=rec.get('creditLine', ''),
                        description=' | '.join(x for x in [rec.get('briefDescription'), rec.get('summaryDescription'), rec.get('physicalDescription')] if x),
                        provenance=rec.get('objectHistory', ''), imageUrl=f'{img}full/!960,960/0/default.jpg' if img else '',
                        highResUrl=f'{img}full/full/0/default.jpg' if img else '',
                        sourceUrl=f'https://collections.vam.ac.uk/item/{r["systemNumber"]}/', rights='V&A image terms (non-commercial)',
                        open=False, accession=rec.get('accessionNumber', '')))
    return out

# ---------------------------------------------------------------- Library of Congress
def loc_item(url):
    j = get(url.rstrip('/') + '/?fo=json') or {}
    it = j.get('item') or {}
    res = j.get('resources') or []
    # Prefer the scan of the original over a film copy; use the 1024 px 'large' JPEG, never the TIFF master.
    res = sorted(res, key=lambda r: (0 if (r.get('large') and 'notdig' not in r.get('large')) else 1, 0 if 'original' in (r.get('note') or '') else 1))
    big = small = ''
    ok = lambda u: u and 'notdig' not in u
    for r in res:
        pick = next((u for u in (r.get('large'), r.get('medium')) if ok(u)), '')
        if pick:
            big = small = pick
            break
    rights = it.get('rights_information') or ''
    notes = ' | '.join(n.get('note', '') for n in it.get('notes', []) if isinstance(n, dict))
    return dict(source='loc', id=url.rstrip('/').rsplit('/', 1)[-1], title=it.get('title', ''),
                maker='; '.join(c.get('title', '') for c in it.get('creators', [])), date=it.get('created_published_date', ''),
                year=year_of(it.get('created_published_date', '')), medium=it.get('medium') or '',
                dimensions='', holder='Library of Congress, Prints and Photographs Division', credit='',
                description=notes + (' | ' + it['summary'] if it.get('summary') else ''), provenance='',
                imageUrl=('https:' + small if small.startswith('//') else small), highResUrl=('https:' + big if big.startswith('//') else big),
                sourceUrl=url, rights=rights.strip(), open=rights.lower().startswith('no known restrictions'),
                call_number=it.get('call_number', ''))

def loc(q, limit=20):
    j = get('https://www.loc.gov/pictures/search/?' + urllib.parse.urlencode({'q': q, 'fo': 'json', 'c': limit})) or {}
    return [loc_item(r['links']['item']) for r in j.get('results', [])[:limit] if r.get('links', {}).get('item')]

# ---------------------------------------------------------------- Smithsonian
def _si_key():
    k = os.environ.get('SI_API_KEY')
    if k:
        return k.strip()
    p = os.path.expanduser('~/.config/artchive/si_key')
    return open(p).read().strip() if os.path.exists(p) else ''

def _si_free(c, label):
    return ' | '.join(x.get('content', '') for x in (c.get('freetext') or {}).get(label, []))

def _si_free_named(c, label, name):
    return ' | '.join(x.get('content', '') for x in (c.get('freetext') or {}).get(label, []) if (x.get('label') or '').lower() == name.lower())

def si(q, limit=20, images_only=True):
    key = _si_key()
    if not key:
        raise RuntimeError('No Smithsonian key: set SI_API_KEY or ~/.config/artchive/si_key')
    qq = q + (' AND online_media_type:Images' if images_only else '')
    j = get('https://api.si.edu/openaccess/api/v1.0/search?' + urllib.parse.urlencode({'q': qq, 'rows': limit, 'api_key': key})) or {}
    out = []
    for x in (j.get('response') or {}).get('rows', []):
        c = x.get('content') or {}
        d = c.get('descriptiveNonRepeating') or {}
        media = [m for m in ((d.get('online_media') or {}).get('media') or []) if m.get('type') == 'Images']
        m = media[0] if media else {}
        cc0 = (m.get('usage') or {}).get('access') == 'CC0'
        base = m.get('content', '')
        out.append(dict(source='si', id=d.get('record_ID', x.get('id')), title=(d.get('title') or {}).get('content') or x.get('title', ''),
                        maker='; '.join(n.get('content', '') for n in (c.get('freetext') or {}).get('name', [])), date=_si_free(c, 'date'),
                        year=year_of(_si_free(c, 'date')), medium=_si_free_named(c, 'physicalDescription', 'Medium') or _si_free(c, 'physicalDescription'),
                        dimensions=_si_free_named(c, 'physicalDescription', 'Dimensions'), holder=d.get('data_source', ''),
                        credit=_si_free(c, 'creditLine'), description=_si_free(c, 'notes'), provenance=_si_free_named(c, 'notes', 'Provenance'),
                        imageUrl=f'{base}&max=960' if base else '', highResUrl=base, sourceUrl=d.get('record_link') or d.get('guid', ''),
                        rights='CC0' if cc0 else ((m.get('usage') or {}).get('access') or ''), open=cc0, unit=d.get('unit_code', ''),
                        accession=_si_free_named(c, 'identifier', 'Object number') or _si_free(c, 'identifier')))
    return out
