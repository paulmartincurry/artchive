#!/usr/bin/env python3
"""Placards for work that is deliberately not on the wall (25 Nov 2026).

Reads data/look-archive.json (the 247 works cut on 23 Nov 2026) and writes
data/placards.json: the searches that should show one blank wall label as the
first tile of the results. Run from the repo root:

    python3 tools/placards.py            # print what would trigger, write nothing
    python3 tools/placards.py --apply    # write data/placards.json

Rules (Paul, 25 Nov 2026): a placard shows only when the search is plainly for
that work or that maker. Never on the wall, never for a theme, one per search.

  - a work: its title typed exactly (two words or more, not also a title on the
    site, not a phrase in the search lexicon, not in DENY_TITLES), or one of
    ONE_WORD (single-word titles nobody types by accident), or a nickname in
    the work's `aliases` or NICKNAMES, or the title with the maker's name
    before or after it. A bracketed gloss in a title ("after Hokusai",
    "Dead Sea") is never a trigger on its own; add it to NICKNAMES if it
    should be
  - a film: the same, on the film's title (the part before ", Still …")
  - a maker: the full name, or a surname in SURNAMES

Matching is on a normalised string (accents off, lower case, anything that is
not a letter or digit becomes a space). index.html does the same in pNorm().
Edit the lists below by hand; print the result before applying.
"""
import json, os, re, sys, unicodedata
from urllib.parse import urlparse, quote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARCHIVE = os.path.join(ROOT, 'data', 'look-archive.json')
WORKS = os.path.join(ROOT, 'data', 'works.js')
LEXICON = os.path.join(ROOT, 'data', 'lexicon.json')
OUT = os.path.join(ROOT, 'data', 'placards.json')

# Single-word titles that are safe to match alone. Everything else with one
# word (Flag, Jazz, Gas, Mao, Mural, Vertigo, Psycho, Dracula, M …) needs the
# maker's name beside it.
ONE_WORD = {'guernica', 'golconda', 'tuttomondo', 'abaporu', 'whaam', 'automat',
            'rashomon', 'vampyr', 'godzilla', 'akira', 'maman'}

# Titles of two words or more that read as a theme or a person, not as a hunt
# for this work.
DENY_TITLES = {
    'self portrait', 'morning sun', 'weeping woman', 'human condition', 'face of war', 'song of love',
    'eclipse of the sun', 'mountains and sea', 'calla lily', 'unfinished painting', 'flower power',
    'temptation of st anthony', 'modern times', 'lovers', 'street', 'critic', 'jungle', 'gates',
    'elephants', 'snail', 'sir winston churchill', 'vladimir mayakovsky', 'president barack obama',
    'dinner party', 'sunflower seeds', 'my bed', 'big electric chair', 'kiss on the sidewalk',
    'new york movie', 'early sunday morning', 'many mansions', 'blue nude ii', 'black on maroon',
    'orange red yellow', 'death dealer', 'weather project', 'wounded deer', 'broken column',
    'red ceiling', 'burning monk', 'terror of war', 'falling soldier', 'drowning girl', 'le reve',
    'three musicians', 'drawing hands', 'still life reviving', 'tenement fire harlem',
    'their first murder', 'invisible man', 'subtlety', 'migration series', 'king kong',
    'bicycle thieves', 'tokyo story', 'days of heaven', 'godfather', 'son of man', 'nuclear energy',
    'freedom from want', 'la dolce vita', 'seventh seal', 'wizard of oz', 'lawrence of arabia',
    'hyeres france', 'no i z', 'larmes', 'jazz', 'memphis', 'for the love of god',
    'portrait of an artist', 'in the mood for love', 'order of the angels',
    'midnight ride of paul revere', 'no 61',
}

# Nicknames in the archive that read as a place or a theme.
ALIAS_DENY = {'tiananmen'}

# Nicknames, exact phrase only. The archive's own `aliases` are added to these.
NICKNAMES = {
    "Campbell's Soup Cans": ['soup cans', 'campbells soup', 'warhol soup cans', 'warhol soup'],
    'Marilyn Diptych': ['warhol marilyn', 'marilyn warhol'],
    'Tank Man': ['tank man', 'tiananmen tank man'],
    'The Terror of War': ['napalm girl'],
    'V-J Day in Times Square': ['times square kiss', 'the kiss in times square', 'vj day kiss', 'v j day kiss'],
    'Raising the Flag on Iwo Jima': ['iwo jima flag', 'iwo jima photo', 'flag raising iwo jima'],
    'Guerrillero Heroico': ['che guevara photo', 'che guevara portrait'],
    'The Persistence of Memory': ['dali melting clocks'],
    'The Treachery of Images': ['magritte pipe'],
    'The Son of Man': ['magritte apple', 'man with apple face'],
    'Girl with Balloon': ['balloon girl', 'banksy balloon'],
    'Christina\'s World': ['christinas world'],
    'The Physical Impossibility of Death in the Mind of Someone Living': ['hirst shark', 'damien hirst shark', 'shark in formaldehyde'],
    'Cloud Gate': ['the bean chicago', 'chicago bean'],
    'Balloon Dog (Blue)': ['balloon dog', 'koons balloon dog'],
    'Comedian': ['banana taped to a wall', 'banana duct tape', 'cattelan banana'],
    'Lunch atop a Skyscraper': ['men on a beam', 'lunch on a skyscraper'],
    'The Two Fridas': ['two fridas', 'las dos fridas'],
    'L.H.O.O.Q.': ['lhooq', 'mona lisa with moustache', 'mona lisa with mustache'],
    '2001: A Space Odyssey': ['2001 space odyssey', 'space odyssey'],
    'The Shining': ['the shining'],
    'The 400 Blows': ['400 blows'],
    'Dr. Strangelove': ['strangelove'],
    'The Night of the Hunter': ['night of the hunter'],
    'Rhein II': ['gursky rhine', 'rhein 2'],
    'Celebes (The Elephant Celebes)': ['the elephant celebes', 'elephant celebes'],
    'Time Transfixed (La durée poignardée)': ['la duree poignardee'],
    'Not to Be Reproduced (La reproduction interdite)': ['la reproduction interdite'],
    'Still Life Reviving (Naturaleza muerta resucitando)': ['naturaleza muerta resucitando'],
    'Autoportrait (Tamara in a Green Bugatti)': ['tamara in a green bugatti', 'tamara in the green bugatti'],
    'Le Rêve (The Dream)': ['picasso the dream', 'picasso le reve'],
    '8½': ['8 1 2', 'eight and a half', 'fellini 8 1 2', '8 1 2 fellini'],
    'American Collection #5: Bessie\'s Blues': ['bessies blues'],
}

# Surnames that may stand alone. A surname is used only if exactly one maker in
# the archive ends with it. Left out on purpose: Wood, Frank, Wall, Parks,
# Bacon, Penn, Ray, Adams, Freud, Chicago, Bourgeois, Tanning, Sherman, Smith,
# Moore, Scott, Lean, Lang, Wilder, Whale, Newman, Johns, Nash, Lam, Honda.
SURNAMES = {
    'picasso', 'dali', 'kahlo', 'magritte', 'warhol', 'hopper', 'pollock', 'rothko', 'basquiat',
    'lichtenstein', 'escher', 'banksy', 'matisse', 'haring', 'kusama', 'hockney', 'de kooning',
    'wyeth', 'hirst', 'koons', 'kapoor', 'eliasson', 'abramovic', 'duchamp', 'rodchenko', 'grosz',
    'nolde', 'kertesz', 'brassai', 'doisneau', 'sugimoto', 'eggleston', 'karsh', 'crewdson',
    'leibovitz', 'gursky', 'korda', 'giacometti', 'rauschenberg', 'twombly', 'orozco', 'kiefer',
    'calder', 'giger', 'frazetta', 'chagall', 'miro', 'lempicka', 'frankenthaler', 'rockwell',
    'beuys', 'de chirico', 'mapplethorpe', 'capa', 'cartier bresson', 'arbus', 'avedon',
    'eisenstaedt', 'salgado', 'mccurry', 'af klint', 'o keeffe', 'okeeffe', 'varo', 'bearden',
    'ringgold', 'dubuffet', 'kubrick', 'hitchcock', 'kurosawa', 'fellini', 'godard', 'truffaut',
    'welles', 'coppola', 'ozu', 'malick', 'weegee', 'rivera', 'ai weiwei', 'emin', 'gormley',
    'cattelan', 'catlett', 'wifredo lam', 'tarsila',
}

# Makers who answer to a name that is not the end of their full name.
MAKER_KEYS = {'Christo and Jeanne-Claude': ['christo'], 'Tarsila do Amaral': ['tarsila'],
              'Margaret Bourke-White': ['bourke white']}

# Records that get no placard: the work is public domain and only this
# photograph of it was not free, so "not free to use" would mislead.
SKIP_IDS = {'VAULT-1794'}   # Sagrada Família, Interior Vaults
SKIP_MAKERS = {'Antoni Gaudí (design)'}

FILM_RX = re.compile(r',\s*(?:Still|Publicity|Trailer|Frame|Press|Production|the Match Cut|the Final Frame|'
                     r'Welles and|Anthony Perkins)\b')


def norm(s):
    s = unicodedata.normalize('NFD', str(s or ''))
    s = ''.join(c for c in s if not ('̀' <= c <= 'ͯ')).lower()
    return re.sub(r'[^a-z0-9]+', ' ', s).strip()


def _apos(s):
    """Christina's World is also typed Christinas World."""
    return {s, re.sub(r"[\u2019']", '', s)}


def title_forms(title):
    """The title as typed: whole, without a bracketed gloss, without the apostrophe, without a leading The."""
    out = set()
    bare = re.sub(r'\s*\([^)]*\)', '', title).strip()
    for t in (title, bare):
        for v in _apos(t):
            out.add(norm(v))
    more = {t[4:] for t in out if t.startswith('the ') and len(t.split()) >= 3}
    return {t for t in out | more if t}


def denied(t):
    return re.sub(r'^(?:the|a) ', '', t) in DENY_TITLES or t.startswith('untitled')


def maker_forms(maker):
    """Full names a maker answers to, and the endings that could be a surname."""
    names = [re.sub(r'\s*\([^)]*\)', '', maker).strip()]
    for m in re.findall(r'\(([^)]*)\)', maker):
        if not re.search(r'attribution|design', m, re.I):
            names.append(m)                               # Weegee (Arthur Fellig)
    full, last = set(), set()
    for n in names:
        for v in _apos(n):
            toks = norm(v).split()
            if not toks:
                continue
            full.add(' '.join(toks))
            lead = 0
            while lead < len(toks) - 1 and len(toks[lead]) == 1:
                lead += 1
            if lead:                                      # M. C. Escher: mc escher
                full.add(''.join(toks[:lead]) + ' ' + ' '.join(toks[lead:]))
                if len(toks) - lead >= 2:                 # W. Eugene Smith: eugene smith
                    full.add(' '.join(toks[lead:]))
            mid = [t for i, t in enumerate(toks) if len(t) > 1 or i == 0 or i == len(toks) - 1]
            if lead == 0 and len(mid) >= 2:               # Charles C. Ebbets: charles ebbets
                full.add(' '.join(mid))
            for k in (1, 2):
                if len(toks) >= k:
                    last.add(' '.join(toks[-k:]))
    return full, last


def main():
    apply = '--apply' in sys.argv
    arch = json.load(open(ARCHIVE, encoding='utf-8'))['works']
    raw = open(WORKS, encoding='utf-8').read()
    site = json.loads(raw[raw.index('['):raw.rindex(']') + 1])
    lex = {norm(k) for k in json.load(open(LEXICON, encoding='utf-8')) if not k.startswith('_')}

    site_titles, site_pairs = set(), set()
    for w in site:
        for t in title_forms(w.get('title', '')) | {norm(a) for a in str(w.get('aliases') or '').split(',')}:
            site_titles.add(t)
            site_pairs.add((t, norm(w.get('artist'))))
        ft = norm(re.split(r',\s*frame at', w.get('title', ''))[0])
        site_titles.add(ft)

    items, keys, notes = [], {}, []

    def put(key, idx, why):
        key = norm(key)
        if not key or len(key) < 3:
            return
        if key in keys and keys[key] != idx:
            notes.append(f'  clash, kept first: "{key}" ({items[keys[key]].get("t") or items[keys[key]]["a"]}) vs ({items[idx].get("t") or items[idx]["a"]})')
            return
        keys[key] = idx

    # how many makers end with each surname
    surname_owner = {}
    makers = sorted({w['artist'] for w in arch if w.get('artist') and w['id'] not in SKIP_IDS and w['artist'] not in SKIP_MAKERS})
    for m in makers:
        _, last = maker_forms(m)
        for s in last:
            surname_owner.setdefault(s, set()).add(m)

    nick = {norm(k): v for k, v in NICKNAMES.items()}
    seen_film = {}
    for w in arch:
        if w['id'] in SKIP_IDS:
            continue
        title, maker = w.get('title', ''), w.get('artist', '')
        film = bool(FILM_RX.search(title))
        shown = FILM_RX.split(title)[0].strip() if film else title
        if film and norm(shown) in seen_film:
            continue
        if any((t, norm(maker)) in site_pairs for t in title_forms(shown)):
            notes.append(f'  skipped, same title and maker is on the site: {shown} / {maker}')
            continue
        idx = len(items)
        it = {'t': shown, 'a': maker_clean(maker), 'd': w.get('dateLabel') or ''}
        if w.get('museum'):
            it['h'] = w['museum']
        # One click to where the work can be seen (Paul, 25 Nov 2026). `k` says what the link is, so the label is honest:
        # hold = the holder's own page, wiki = its Wikipedia article, find = a Wikipedia search (no page of its own on file).
        src = w.get('sourceUrl') or ''
        host = urlparse(src).netloc.replace('www.', '')
        if film:
            it['f'] = 1
            year = re.search(r'\d{4}', str(w.get('dateLabel') or ''))
            it['u'], it['k'] = wiki_find(f'{shown} {year.group(0) if year else ""} film'), 'find'   # the source was the still's file page
            seen_film[norm(shown)] = idx
        elif host.endswith('wikipedia.org'):
            it['u'], it['k'] = src, 'wiki'
        elif host and w.get('museum') and not host.endswith(('wikimedia.org', 'wikidata.org')):
            it['u'], it['k'] = src, 'hold'
        else:
            it['u'], it['k'] = wiki_find(f'{shown} {maker_clean(maker)}'), 'find'
        items.append(it)

        forms = title_forms(shown)
        full, _ = maker_forms(maker)
        sur = {s for s in SURNAMES if surname_owner.get(s) == {maker}}
        for t in forms:
            alone = (len(t.split()) >= 2 and not denied(t) and t not in site_titles and t not in lex) or t in ONE_WORD
            if alone:
                put(t, idx, 'title')
            for m in full | sur:
                put(f'{m} {t}', idx, 'maker+title')
                put(f'{t} {m}', idx, 'title+maker')
                put(f'{t} by {m}', idx, 'title by maker')
        own = [a for a in str(w.get('aliases') or '').split(',') if len(norm(a).split()) >= 2 and norm(a) not in ALIAS_DENY]
        for a in own + nick.get(norm(shown), []) + nick.get(norm(title), []):
            if norm(a) and norm(a) not in site_titles and norm(a) not in lex:
                put(a, idx, 'nickname')

    for m in makers:
        cut = sum(1 for w in arch if w.get('artist') == m and w['id'] not in SKIP_IDS)
        idx = len(items)
        items.append({'a': maker_clean(m), 'n': cut, 'x': 1, 'u': wiki_find(maker_clean(m)), 'k': 'find'})
        full, _ = maker_forms(m)
        for k in full:
            if len(k.split()) >= 2 or k in SURNAMES or len(full) == 1:
                put(k, idx, 'maker')
        for s in SURNAMES:
            if surname_owner.get(s) == {m}:
                put(s, idx, 'surname')
        for k in MAKER_KEYS.get(m, []):
            put(k, idx, 'maker')

    by = {}
    for k, i in keys.items():
        by.setdefault(i, []).append(k)
    print(f'{len(items)} placards ({sum(1 for i in items if i.get("x"))} makers, {sum(1 for i in items if i.get("f"))} films), {len(keys)} searches')
    for i, it in enumerate(items):
        ks = sorted(by.get(i, []), key=lambda s: (len(s.split()), s))
        mk = set() if it.get('x') else {m for m in maker_forms(next(w['artist'] for w in arch if maker_clean(w['artist']) == it['a']))[0]} | SURNAMES
        alone = [k for k in ks if it.get('x') or not any(k.startswith(m + ' ') or k.endswith(' ' + m) for m in mk)]
        label = it.get('t') or it['a']
        print(f'- {label}{"" if it.get("x") else " / " + it["a"]}: {" | ".join(alone) or "(with the maker only)"}')
    for n in notes:
        print(n)
    if apply:
        json.dump({'_about': 'Blank wall labels for work that is not on the site. Made by tools/placards.py from data/look-archive.json; do not edit by hand.',
                   'items': items, 'keys': dict(sorted(keys.items()))}, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
        print('wrote', OUT, os.path.getsize(OUT), 'bytes')


def wiki_find(q):
    """A Wikipedia search: an exact title goes straight to the article, anything else to the results."""
    return 'https://en.wikipedia.org/wiki/Special:Search?search=' + quote(' '.join(q.split()))


def maker_clean(m):
    return re.sub(r'\s*\((?:attribution[^)]*|design)\)', '', m).strip()


if __name__ == '__main__':
    main()
