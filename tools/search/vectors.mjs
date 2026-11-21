// Build data/vec.bin (meaning vectors, int8, one row per work in the order of data/similar.json ids)
// and data/similar.json ("More like this": picture neighbours for art, meaning neighbours for writing).
// Needs @huggingface/transformers (npm i in this folder; node_modules is not committed) and the picture
// embeddings in <vis>/emb.json from embed.mjs.   Run: node tools/search/vectors.mjs [/home/claude/vis]
import { pipeline, env } from '@huggingface/transformers';
import fs from 'fs'; import path from 'path'; import { fileURLToPath } from 'url';
const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../..');
const VIS = process.argv[2] || '/home/claude/vis';
env.cacheDir = path.join(VIS, 'models');
const raw = fs.readFileSync(path.join(ROOT, 'data/works.js'), 'utf8');
const works = JSON.parse(raw.slice(raw.indexOf('['), raw.lastIndexOf(']') + 1));
const isLit = w => w.itemType === 'literature';
const clean = s => String(s || '').replace(/\s+/g, ' ').trim();
const docText = w => isLit(w)
  ? [w.title, w.artist, w.emotionShort, w.shelf, w.hook, w.note, clean(w.fullText).slice(0, 700)].filter(Boolean).join('. ')
  : [w.title, w.artist, w.medium || w.macroMedium, w.emotionShort, w.seeText, w.note].filter(Boolean).join('. ');
const ex = await pipeline('feature-extraction', 'Xenova/bge-small-en-v1.5', { dtype: 'q8' });
const ids = works.map(w => w.id); const N = ids.length; let D = 384;
const T = new Float32Array(N * D);
for (let i = 0; i < N; i += 32) {
  const batch = works.slice(i, i + 32).map(docText);
  const out = await ex(batch, { pooling: 'cls', normalize: true });
  T.set(out.data, i * D);
  if (i % 640 === 0) console.log('text', i);
}
const q = new Int8Array(N * D); for (let k = 0; k < q.length; k++) q[k] = Math.max(-127, Math.min(127, Math.round(T[k] * 127)));
fs.writeFileSync(path.join(ROOT, 'data/vec.bin'), Buffer.from(q.buffer));
// neighbours
const emb = JSON.parse(fs.readFileSync(path.join(VIS, 'emb.json'), 'utf8'));
const dot = (A, ao, B, bo, d) => { let s = 0; for (let k = 0; k < d; k++) s += A[ao + k] * B[bo + k]; return s; };
const artIdx = [], litIdx = []; works.forEach((w, i) => (isLit(w) ? litIdx : artIdx).push(i));
const C = new Float32Array(N * 512); const hasC = new Uint8Array(N);
works.forEach((w, i) => { const e = emb[w.id]; if (e) { C.set(e, i * 512); hasC[i] = 1; } });
const pick = (i, pool, score, k, perArtist) => {
  const cand = []; for (const j of pool) if (j !== i) cand.push([j, score(j)]);
  cand.sort((a, b) => b[1] - a[1]);
  const out = [], count = {};
  for (const [j, s] of cand) {
    if (s > 0.985) continue;                         // the same image twice
    const a = works[j].artist || ''; if ((count[a] || 0) >= perArtist) continue;
    count[a] = (count[a] || 0) + 1; out.push(j); if (out.length >= k) break;
  }
  return out;
};
const nb = new Array(N);
for (const i of artIdx) {
  nb[i] = hasC[i]
    ? pick(i, artIdx.filter(j => hasC[j]), j => dot(C, i * 512, C, j * 512, 512), 8, 2)
    : pick(i, artIdx, j => dot(T, i * D, T, j * D, D), 8, 2);
}
for (const i of litIdx) nb[i] = pick(i, litIdx, j => dot(T, i * D, T, j * D, D), 6, 1);
fs.writeFileSync(path.join(ROOT, 'data/similar.json'), JSON.stringify({ ids, nb }));
console.log('done', N, 'with pictures', hasC.reduce((a, b) => a + b, 0));
