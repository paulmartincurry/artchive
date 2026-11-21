import { AutoProcessor, CLIPVisionModelWithProjection, RawImage, env } from '@huggingface/transformers';
import fs from 'fs';
env.cacheDir = './models';
const id='Xenova/clip-vit-base-patch16';
const proc = await AutoProcessor.from_pretrained(id);
const model = await CLIPVisionModelWithProjection.from_pretrained(id, { dtype: 'fp32' });
const out = fs.existsSync('emb.json') ? JSON.parse(fs.readFileSync('emb.json')) : {};
const files = fs.readdirSync('img').filter(f=>f.endsWith('.jpg'));
let n=0;
for (const f of files){ const k=f.slice(0,-4); if (out[k]) continue;
  try { const im=await RawImage.read('img/'+f); const {image_embeds}=await model(await proc(im));
    const v=Array.from(image_embeds.data); const nrm=Math.hypot(...v); out[k]=v.map(x=>+(x/nrm).toFixed(5)); } catch(e){ console.error('fail',k,e.message); }
  if (++n % 200 === 0) { fs.writeFileSync('emb.json', JSON.stringify(out)); console.log(n); } }
fs.writeFileSync('emb.json', JSON.stringify(out)); console.log('done', Object.keys(out).length);
