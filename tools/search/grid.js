// Paste once per tab. Then: await pvGrid(k) shows page k (18 images, 6 x 3) full screen; returns load status.
window.pvList = window.pvList || await fetch('tools/shotlist.json?' + Date.now()).then(r => r.json());
window.pvGrid = async function (k) {
  let ov = document.getElementById('pvShot');
  if (!ov) {
    ov = document.createElement('div'); ov.id = 'pvShot';
    ov.style.cssText = 'position:fixed;inset:0;z-index:2147483647;background:#000;display:grid;grid-template-columns:repeat(6,1fr);grid-template-rows:repeat(3,1fr);gap:0;margin:0;padding:0;';
    document.body.appendChild(ov); document.documentElement.style.overflow = 'hidden';
  }
  ov.innerHTML = '';
  const items = pvList.slice(k * 18, k * 18 + 18);
  const res = await Promise.all(items.map(([id, u]) => new Promise(done => {
    const cell = document.createElement('div');
    cell.style.cssText = 'position:relative;overflow:hidden;background:#000;';
    const im = new Image(); im.decoding = 'sync';
    im.style.cssText = 'position:absolute;inset:6px;width:calc(100% - 12px);height:calc(100% - 12px);object-fit:contain;';
    const t = setTimeout(() => done(id + ':timeout'), 20000);
    im.onload = () => { clearTimeout(t); done(id + ':ok'); };
    im.onerror = () => { clearTimeout(t); done(id + ':err'); };
    im.src = u; cell.appendChild(im); ov.appendChild(cell);
  })));
  await new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r)));
  return { k, w: innerWidth, h: innerHeight, bad: res.filter(x => !x.endsWith(':ok')) };
};
window.pvDone = () => { const ov = document.getElementById('pvShot'); if (ov) ov.remove(); document.documentElement.style.overflow = ''; };
({ pages: Math.ceil(pvList.length / 18), n: pvList.length })
