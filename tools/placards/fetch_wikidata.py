#!/usr/bin/env python3
"""Pull the raw material for the wide placards from Wikidata (25 Nov 2026).

Well-known makers (artists, photographers, film directors, writers), artworks, films
and poems, each with how many Wikipedia editions have an article on it (n), which is
the measure of "would a stranger search for this". Writes tools/placards/wikidata.json;
tools/placards.py decides what becomes a placard. Run from the repo root, a few minutes:

    python3 tools/placards/fetch_wikidata.py

Wikidata now files many labels under "mul" (all languages) with no English one, so the
name is the English label, else the mul label, else the English Wikipedia title without
its bracket. An earlier pull that asked for the English label alone lost Christopher
Nolan and most of the best-known films.
"""
import json, os, re, sys, time, urllib.parse, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
UA = 'ArtchiveBuild/1.0 (https://www.paulmartincurry.com/artchive/; placards list)'


def q(sparql, tries=4):
    url = 'https://query.wikidata.org/sparql?' + urllib.parse.urlencode({'query': sparql})
    for t in range(tries):
        try:
            r = urllib.request.Request(url, headers={'Accept': 'application/sparql-results+json', 'User-Agent': UA})
            d = json.load(urllib.request.urlopen(r, timeout=150))
            return [{k: v['value'] for k, v in b.items()} for b in d['results']['bindings']]
        except Exception as e:
            print('  retry', t, str(e)[:90], file=sys.stderr)
            time.sleep(20 * (t + 1))
    raise SystemExit('Wikidata did not answer')


def name_of(v):   # label pattern for ?v -> ?vN
    return (f'OPTIONAL{{?{v} rdfs:label ?{v}1. FILTER(LANG(?{v}1)="en")}} OPTIONAL{{?{v} rdfs:label ?{v}2. FILTER(LANG(?{v}2)="mul")}} '
            f'OPTIONAL{{?{v}a schema:about ?{v}; schema:isPartOf <https://en.wikipedia.org/>; schema:name ?{v}3.}}')


WIKI = '?a schema:about ?i; schema:isPartOf <https://en.wikipedia.org/>; schema:name ?wiki.'
LAB = 'OPTIONAL{?i rdfs:label ?l1. FILTER(LANG(?l1)="en")} OPTIONAL{?i rdfs:label ?l2. FILTER(LANG(?l2)="mul")}'


def pick(*names):
    for n in names:
        if n:
            return re.sub(r'\s*\([^)]*\)$', '', n).strip()
    return None


def makers(occ, floor):
    rows = q(f'''SELECT ?i ?wiki ?n (SAMPLE(?l1) AS ?en) (SAMPLE(?l2) AS ?mul) (MIN(YEAR(?b)) AS ?born) (MIN(YEAR(?d)) AS ?died)
      (GROUP_CONCAT(DISTINCT ?o;separator="|") AS ?occ) (GROUP_CONCAT(DISTINCT ?al;separator="|") AS ?aka) WHERE {{
      ?i wdt:P31 wd:Q5; wdt:P106 wd:{occ}; wikibase:sitelinks ?n. FILTER(?n>={floor}) {WIKI} {LAB}
      OPTIONAL{{?i wdt:P569 ?b}} OPTIONAL{{?i wdt:P570 ?d}} OPTIONAL{{?i wdt:P106 ?oo. BIND(STRAFTER(STR(?oo),"entity/") AS ?o)}}
      OPTIONAL{{?i skos:altLabel ?al. FILTER(LANG(?al)="en")}} }} GROUP BY ?i ?wiki ?n''')
    return rows


def works(cls, floor, by_form=False):
    kind = f'?i wdt:P7937 wd:{cls}' if by_form else f'?i wdt:P31 wd:{cls}'
    return q(f'''SELECT ?i ?wiki ?n (SAMPLE(?l1) AS ?en) (SAMPLE(?l2) AS ?mul) (MIN(YEAR(?t)) AS ?year) (MIN(YEAR(?t2)) AS ?year2)
      (SAMPLE(?c1) AS ?m1) (SAMPLE(?c2) AS ?m2) (SAMPLE(?c3) AS ?m3) (MIN(YEAR(?cd)) AS ?makerDied) (SAMPLE(?hn) AS ?holder) (SAMPLE(?pd) AS ?status)
      (GROUP_CONCAT(DISTINCT ?al;separator="|") AS ?aka) WHERE {{
      {kind}; wikibase:sitelinks ?n. FILTER(?n>={floor}) {WIKI} {LAB}
      OPTIONAL{{?i wdt:P571 ?t}} OPTIONAL{{?i wdt:P577 ?t2}}
      OPTIONAL{{?i wdt:P170|wdt:P50 ?c. {name_of('c')} OPTIONAL{{?c wdt:P570 ?cd}} }}
      OPTIONAL{{?i wdt:P195 ?h. ?h rdfs:label ?hn. FILTER(LANG(?hn)="en")}} OPTIONAL{{?i wdt:P6216 ?p. BIND(STRAFTER(STR(?p),"entity/") AS ?pd)}}
      OPTIONAL{{?i skos:altLabel ?al. FILTER(LANG(?al)="en")}} }} GROUP BY ?i ?wiki ?n''')


def films(floor):
    return q(f'''SELECT ?i ?wiki ?n (SAMPLE(?l1) AS ?en) (SAMPLE(?l2) AS ?mul) (MIN(YEAR(?t)) AS ?year)
      (SAMPLE(?c1) AS ?m1) (SAMPLE(?c2) AS ?m2) (SAMPLE(?c3) AS ?m3) (SAMPLE(?pd) AS ?status) WHERE {{
      ?i wdt:P57 ?c; wikibase:sitelinks ?n. FILTER(?n>={floor}) {WIKI} {LAB}
      OPTIONAL{{?i wdt:P577 ?t}} {name_of('c')}
      OPTIONAL{{?i wdt:P6216 ?p. BIND(STRAFTER(STR(?p),"entity/") AS ?pd)}} }} GROUP BY ?i ?wiki ?n''')


MAKERS = [('painter', 'Q1028181', 40), ('photographer', 'Q33231', 40), ('sculptor', 'Q1281618', 40), ('illustrator', 'Q644687', 40),
          ('printmaker', 'Q11569986', 40), ('graphic designer', 'Q627325', 35), ('visual artist', 'Q3391743', 35), ('graffiti artist', 'Q15095148', 15),
          ('comics artist', 'Q715301', 45), ('installation artist', 'Q18074503', 30), ('performance artist', 'Q10774753', 35),
          ('film director', 'Q2526255', 70), ('animator', 'Q266569', 50), ('artist', 'Q483501', 45), ('architect', 'Q42973', 70),
          ('poet', 'Q49757', 80), ('novelist', 'Q6625963', 80), ('playwright', 'Q214917', 80), ('writer', 'Q36180', 110)]
WORKS = [('painting', 'Q3305213', 14), ('photo', 'Q125191', 8), ('sculpture', 'Q860861', 16), ('print', 'Q11060274', 10),
         ('install', 'Q20437094', 8), ('mural', 'Q219423', 10)]


def main():
    out = {'_about': 'Pulled from Wikidata by tools/placards/fetch_wikidata.py on %s: makers, works, films and poems ranked by how many Wikipedia '
                     'editions have an article (n). The raw material for the wide placards; tools/placards.py decides what becomes one.' % time.strftime('%d %b %Y'),
           'makers': [], 'works': [], 'films': [], 'poems': []}
    M = {}
    for label, occ, floor in MAKERS:
        rows = makers(occ, floor)
        print(label, len(rows)); time.sleep(4)
        for x in rows:
            e = M.setdefault(x['i'], x)
            e.setdefault('lists', []).append(label)
    occs = sorted({o for m in M.values() for o in (m.get('occ') or '').split('|') if o})
    lab = {}
    for i in range(0, len(occs), 150):
        for b in q('SELECT ?o ?l WHERE { VALUES ?o { %s } ?o rdfs:label ?l. FILTER(LANG(?l)="en") }' % ' '.join('wd:' + o for o in occs[i:i + 150])):
            lab[b['o'].split('/')[-1]] = b['l']
        time.sleep(2)
    for m in M.values():
        name = pick(m.get('en'), m.get('mul'), m['wiki'])
        out['makers'].append({'id': m['i'].split('/')[-1], 'name': name, 'wiki': m['wiki'], 'n': int(m['n']),
                              'born': int(m['born']) if m.get('born') else None, 'died': int(m['died']) if m.get('died') else None,
                              'occ': sorted({lab.get(o, o) for o in (m.get('occ') or '').split('|') if o}),
                              'aka': [a for a in (m.get('aka') or '').split('|') if a][:12], 'lists': m['lists']})
    for kind, cls, floor in WORKS:
        rows = works(cls, floor)
        print(kind, len(rows)); time.sleep(4)
        for x in rows:
            y = x.get('year') or x.get('year2')
            out['works'].append({'id': x['i'].split('/')[-1], 'kind': kind, 'name': pick(x.get('en'), x.get('mul'), x['wiki']), 'wiki': x['wiki'], 'n': int(x['n']),
                                 'year': int(y) if y else None, 'maker': pick(x.get('m1'), x.get('m2'), x.get('m3')), 'holder': x.get('holder'),
                                 'pd': x.get('status') == 'Q19652', 'aka': [a for a in (x.get('aka') or '').split('|') if a][:10]})
    rows = films(55)
    print('films', len(rows)); time.sleep(4)
    for x in rows:
        out['films'].append({'id': x['i'].split('/')[-1], 'name': pick(x.get('en'), x.get('mul'), x['wiki']), 'wiki': x['wiki'], 'n': int(x['n']),
                             'year': int(x['year']) if x.get('year') else None, 'maker': pick(x.get('m1'), x.get('m2'), x.get('m3')), 'pd': x.get('status') == 'Q19652'})
    rows = works('Q5185279', 8, by_form=True)
    print('poems', len(rows))
    for x in rows:
        y = x.get('year2') or x.get('year')
        out['poems'].append({'id': x['i'].split('/')[-1], 'name': pick(x.get('en'), x.get('mul'), x['wiki']), 'wiki': x['wiki'], 'n': int(x['n']),
                             'year': int(y) if y else None, 'maker': pick(x.get('m1'), x.get('m2'), x.get('m3')),
                             'makerDied': int(x['makerDied']) if x.get('makerDied') else None, 'pd': x.get('status') == 'Q19652'})
    for k in ('makers', 'works', 'films', 'poems'):
        out[k].sort(key=lambda e: (-e['n'], e['name'] or ''))
    json.dump(out, open(os.path.join(HERE, 'wikidata.json'), 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
    print({k: len(v) for k, v in out.items() if k != '_about'}, os.path.getsize(os.path.join(HERE, 'wikidata.json')) // 1024, 'KB')


if __name__ == '__main__':
    main()
