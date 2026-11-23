# Write tools/search/aliases.json into data/works.js as `aliases` (hidden; searched like the title).
import json, os
R = os.path.join(os.path.dirname(__file__), '..', '..')
al = {k: v for k, v in json.load(open(os.path.join(R, 'tools/search/aliases.json'))).items() if not k.startswith('_')}
p = os.path.join(R, 'data/works.js'); s = open(p).read(); i = s.index('['); j = s.rindex(']') + 1
a = json.loads(s[i:j]); ids = {w['id'] for w in a}
missing = [k for k in al if k not in ids]
for w in a:
    if w['id'] in al: w['aliases'] = al[w['id']]
    elif 'aliases' in w: del w['aliases']
open(p, 'w').write(s[:i] + json.dumps(a, ensure_ascii=False, separators=(',', ':')) + s[j:])
print('aliases', len(al) - len(missing), 'missing ids', missing)
