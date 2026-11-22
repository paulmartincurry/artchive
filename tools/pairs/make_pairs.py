"""Pictures near these words (and words near this picture). From the meaning vectors in data/vec.bin
(bge-small, the same ones search uses): for each writing piece, up to four artworks whose text sits closest
to it; for each artwork, up to three lines. One per maker. Only pairs above FLOOR are kept, so a weak match
shows nothing rather than something random. Writes data/pairs.json. Run after vectors.mjs."""
import json, numpy as np
FLOOR = 0.668   # about the top quarter of best matches; checked by eye on 21 Nov 2026
ids = json.load(open('data/similar.json'))['ids']
V = np.frombuffer(open('data/vec.bin', 'rb').read(), dtype=np.int8).reshape(len(ids), -1).astype(np.float32)
V /= np.linalg.norm(V, axis=1, keepdims=True) + 1e-9
src = open('data/works.js', encoding='utf-8').read()
W = {w['id']: w for w in json.loads(src[src.index('['):src.rindex(']') + 1])}
lit = np.array([bool(W.get(i, {}).get('shelf')) for i in ids])
li, ai = np.where(lit)[0], np.where(~lit)[0]
S = V[li] @ V[ai].T

def pick(row, pool, k):
    out, seen = [], set()
    for j in np.argsort(-row):
        if row[j] < FLOOR: break
        w = W.get(ids[pool[j]], {}); a = w.get('artist', '?')
        if a in seen: continue
        seen.add(a); out.append(ids[pool[j]])
        if len(out) >= k: break
    return out

pairs = {}
for r, i in enumerate(li):
    p = pick(S[r], ai, 4)
    if p: pairs[ids[i]] = p
for r, i in enumerate(ai):
    p = pick(S.T[r], li, 3)
    if p: pairs[ids[i]] = p
json.dump(pairs, open('data/pairs.json', 'w'), separators=(',', ':'))
print(len(pairs), 'works with pairs;', sum(1 for k in pairs if W[k].get('shelf')), 'writing,', sum(1 for k in pairs if not W[k].get('shelf')), 'art')
