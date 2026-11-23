// Hubness: some works sit close to almost any search (a short, abstract poem about sorrow). Measure each work's
// mean meaning-closeness to a broad set of probe searches and write it to data/hub.json; the site subtracts a share.
import { pipeline, env } from '@huggingface/transformers';
import fs from 'fs'; import path from 'path'; import { fileURLToPath } from 'url';
const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../..');
env.cacheDir = '/home/claude/vis/models';
const lex = Object.keys(JSON.parse(fs.readFileSync(path.join(ROOT, 'data/lexicon.json'), 'utf8'))).filter(k => !k.startsWith('_'));
const extra = fs.readFileSync(path.join(ROOT, 'tools/search/probes.txt'), 'utf8').split('\n').map(s => s.trim()).filter(Boolean);
const probes = [...new Set([...lex, ...extra])];
const ex = await pipeline('feature-extraction', 'Xenova/bge-small-en-v1.5', { dtype: 'q8' });
const P = [];
for (let i = 0; i < probes.length; i += 32) {
  const out = await ex(probes.slice(i, i + 32).map(p => 'Represent this sentence for searching relevant passages: ' + p), { pooling: 'cls', normalize: true });
  for (let k = 0; k < out.dims[0]; k++) P.push(out.data.slice(k * 384, (k + 1) * 384));
}
const ids = JSON.parse(fs.readFileSync(path.join(ROOT, 'data/similar.json'), 'utf8')).ids;
const V = new Int8Array(fs.readFileSync(path.join(ROOT, 'data/vec.bin')).buffer.slice(0));
const hub = ids.map((id, i) => { let s = 0; for (const p of P) { let d = 0; for (let k = 0; k < 384; k++) d += V[i * 384 + k] * p[k]; s += d / 127; } return s / P.length; });
const sorted = [...hub].sort((a, b) => a - b), med = sorted[Math.floor(sorted.length / 2)];
fs.writeFileSync(path.join(ROOT, 'data/hub.json'), JSON.stringify({ med: +med.toFixed(4), hub: hub.map(h => +h.toFixed(4)) }));
console.log('probes', probes.length, 'median', med.toFixed(4), 'max', sorted[sorted.length - 1].toFixed(4));
