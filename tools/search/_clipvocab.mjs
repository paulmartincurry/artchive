import { AutoTokenizer, CLIPTextModelWithProjection, env } from '@huggingface/transformers';
import fs from 'fs';
env.cacheDir = '/home/claude/vis/models';
const V = JSON.parse(fs.readFileSync('/home/claude/sq/vocab.json', 'utf8'));
const tok = await AutoTokenizer.from_pretrained('Xenova/clip-vit-base-patch16');
const model = await CLIPTextModelWithProjection.from_pretrained('Xenova/clip-vit-base-patch16', { dtype: 'q8' });
const out = [];
for (let i = 0; i < V.length; i += 32) {
  const t = tok(V.slice(i, i + 32).map(v => 'a picture of ' + v[1]), { padding: true, truncation: true });
  const { text_embeds } = await model(t);
  const d = text_embeds.dims[1];
  for (let k = 0; k < text_embeds.dims[0]; k++) { const v = Array.from(text_embeds.data.slice(k * d, (k + 1) * d)); const n = Math.hypot(...v); out.push(v.map(x => x / n)); }
}
fs.writeFileSync('/home/claude/sq/vocab_emb.json', JSON.stringify(out));
console.log('done', out.length);
