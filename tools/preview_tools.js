// Preview tools (option E, 20 Nov 2026). One collection, rearranged by what you ask for.
// Everything stacks: Show (All / Art / Writing), Colour, Mood, Era, Region, Medium (several values each),
// search, and Arrange (the daily wall, by date, by colour, by mood). The wall animates between states.
(function () {
  const LIT = 'Literature & Verse';
  const FACETS = [
    { id: 'tone', label: 'Colour', field: 'colourStrength', opts: [
      ['Red', 'Red', '#b3261e'], ['Orange', 'Orange', '#d9752b'], ['Gold', 'Gold', '#c9a227'], ['Green', 'Green', '#3f7a4d'],
      ['Blue', 'Blue', '#2a4f9c'], ['Brown', 'Brown', '#6b4a2b'], ['Black', 'Black', '#151515'], ['Grey', 'Grey', '#8a8a8a'],
      ['Cream', 'Cream', '#e8dfc8'] ] },
    { id: 'mood', label: 'Mood', field: 'emotionShort', opts: ['Dread', 'Fury', 'Melancholy', 'Yearning', 'Sublime', 'Resolve', 'Dark Humor'].map(m => [m, m]) },
    { id: 'era', label: 'Era', field: 'eraBucket', opts: [
      ['Ancient & Medieval', 'Before 1400'], ['1400–1650', '1400–1650'], ['1650–1800', '1650–1800'], ['1800–1920', '1800–1920'], ['1920–Now', '1920–now'] ] },
    { id: 'region', label: 'Region', field: 'macroRegion', opts: [
      ['Europe', 'Europe'], ['Americas', 'Americas'], ['East & Inner Asia', 'East & Inner Asia'],
      ['Near East & South Asia', 'Near East & South Asia'], ['Africa, Oceania & Indigenous Americas', 'Africa, Oceania & Indigenous Americas'] ] },
    { id: 'medium', label: 'Medium', field: 'macroMedium', opts: [
      ['Painting', 'Painting'], ['Print & Woodcut', 'Print & Woodcut'], ['Photograph & Film', 'Photograph & Film'],
      ['Sculpture & Metalwork', 'Sculpture & Metalwork'], ['Scroll & Paper', 'Scroll & Paper'],
      ['Diagram, Cyanotype & Textile', 'Diagram, Cyanotype & Textile'], ['Letterform, Score & Ephemera', 'Letterform, Score & Ephemera'] ] }
  ];
  const ARRANGE = [['wall', 'The wall'], ['date', 'By date'], ['colour', 'By colour'], ['mood', 'By mood']];
  const MOOD_ORDER = FACETS[1].opts.map(o => o[0]);

  const sel = {}; FACETS.forEach(f => sel[f.id] = new Set());
  // ---- colour: names by measured strength, or one exact shade (21 Nov 2026) ----
  const CNAMES = ['Red', 'Orange', 'Gold', 'Green', 'Blue', 'Brown', 'Black', 'Grey', 'Cream'];
  const CFLOOR = 6;                                  // a named colour must carry at least this much of the picture (0-100)
  const PIGMENTS = [['Vermilion', '#E34234'], ['Oxblood', '#4A0E0E'], ['Rose madder', '#E32636'], ['Tyrian purple', '#66023C'],
    ['Ultramarine', '#120A8F'], ['Klein blue', '#002FA7'], ['Prussian blue', '#003153'], ['Verdigris', '#43B3AE'],
    ['Viridian', '#40826D'], ['Sap green', '#507D2A'], ['Naples yellow', '#FADA5E'], ['Ochre', '#CC7722'],
    ['Burnt sienna', '#E97451'], ['Raw umber', '#826644']];
  let shade = null;                                  // {hex, label}
  let shadeScore = null, shadeTop = 0, shadeCut = 0, CDATA = null, cdataP = null;
  const strength = (w, n) => (Array.isArray(w.colourStrength) ? w.colourStrength[CNAMES.indexOf(n)] || 0 : 0);
  function hexToOk(hex) {
    const n = parseInt(hex.slice(1), 16), lin = v => { v /= 255; return v > 0.04045 ? Math.pow((v + 0.055) / 1.055, 2.4) : v / 12.92; };
    const r = lin(n >> 16), g = lin(n >> 8 & 255), b = lin(n & 255);
    const l = Math.cbrt(0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b);
    const m = Math.cbrt(0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b);
    const q = Math.cbrt(0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b);
    return [0.2104542553 * l + 0.7936177850 * m - 0.0040720468 * q, 1.9779984951 * l - 2.4285922050 * m + 0.4505937099 * q,
      0.0259040371 * l + 0.7827717662 * m - 0.8086757660 * q];
  }
  function loadColour() {
    const BASEc = location.pathname.replace(/[^/]*$/, '');
    const verc = ((document.querySelector('script[src*="data/site.js"]') || {}).src || '').split('?')[1] || '';
    return cdataP || (cdataP = fetch(BASEc + 'data/colour.json?' + verc).then(r => r.json()).then(j => (CDATA = j)).catch(() => null));
  }
  function scoreShade() {
    shadeScore = new Map(); shadeTop = 0;
    if (!shade || !CDATA) return;
    const [qL, qa, qb] = hexToOk(shade.hex), SIG = 0.075;
    CDATA.ids.forEach((id, i) => {
      let sc = 0;
      for (const c of CDATA.cl[i]) {
        const d2 = (c[0] / 100 - qL) ** 2 + (c[1] / 500 - qa) ** 2 + (c[2] / 500 - qb) ** 2;
        sc += (c[3] / 1000) * Math.exp(-d2 / (SIG * SIG));
      }
      shadeScore.set(id, sc); if (sc > shadeTop) shadeTop = sc;
    });
    // Keep everything within a quarter of the best match, and never fewer than the 60 closest.
    const sorted = [...shadeScore.values()].sort((a, b) => b - a);
    shadeCut = Math.max(0.0015, Math.min(shadeTop * 0.25, sorted[59] || 0));
  }
  function colourRank(w) {
    if (shade) return shadeScore ? (shadeScore.get(w.id) || 0) : 0;
    const names = [...sel.tone]; if (!names.length) return 0;
    return Math.min(...names.map(n => strength(w, n)));
  }
  function colourOn() { return !!shade || sel.tone.size > 0; }
  async function setShade(hex, label) {
    shade = hex ? { hex: hex.toUpperCase(), label: label || hex.toUpperCase() } : null;
    if (shade) { sel.tone.clear(); await loadColour(); }
    scoreShade(); refresh(); if (openId) drawPop();
  }
  // Variety on the first screens: at most two per artist and eight per medium in each run of 24.
  function vary(list) {
    const head = list.slice(0, 240), rest = list.slice(240), out = [], held = [];
    let ca = {}, cm = {};
    for (const w of head) {
      if (out.length % 24 === 0) { ca = {}; cm = {}; }
      const a = w.artist || '?', m = w.macroMedium || '?';
      if ((ca[a] || 0) >= 2 || (cm[m] || 0) >= 8) { held.push(w); continue; }
      ca[a] = (ca[a] || 0) + 1; cm[m] = (cm[m] || 0) + 1; out.push(w);
    }
    return out.concat(held, rest);
  }
  let show = 'both', arrange = 'wall', openId = '';
  try { show = localStorage.getItem('pvShow') || 'both'; } catch (e) {}
  if (!['both', 'art', 'writing'].includes(show)) show = 'both';

  const toolsEl = document.getElementById('pvTools');
  const pop = document.getElementById('pvPop');
  const row = document.getElementById('pvToolRow');
  const esc = x => String(x).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/"/g, '&quot;');
  const isLit = w => w.itemType === 'literature' || w.macroMedium === LIT;

  // ---- hooks read by filterWorks ----
  window.pvPass = function (w) {
    if (show === 'art' && isLit(w)) return false;
    if (show === 'writing' && !isLit(w)) return false;
    for (const f of FACETS) {
      const s = sel[f.id];
      if (!s.size) continue;
      let v = w[f.field];
      if (f.id === 'tone') { if (isLit(w)) return false; const fl = s.size > 1 ? 4 : CFLOOR; for (const n of s) if (strength(w, n) < fl) return false; continue; }
      if (f.id === 'medium') {
        if (isLit(w)) return false;   // a medium choice means art
        if (v === 'Diagram' || v === 'Cyanotype & Textile') v = 'Diagram, Cyanotype & Textile';
        if (v === 'Letterform' || v === 'Score & Ephemera') v = 'Letterform, Score & Ephemera';
      }
      if (!s.has(v)) return false;
    }
    if (shade) {
      if (isLit(w) || !shadeScore) return false;
      const sc = shadeScore.get(w.id) || 0;
      if (sc < shadeCut) return false;
    }
    return true;
  };
  window.pvActive = () => show !== 'both' || arrange !== 'wall' || !!shade || FACETS.some(f => sel[f.id].size);

  function hsl(hex) {
    const m = /^#?([0-9a-f]{6})$/i.exec(hex || ''); if (!m) return null;
    const n = parseInt(m[1], 16), r = (n >> 16) / 255, g = (n >> 8 & 255) / 255, b = (n & 255) / 255;
    const mx = Math.max(r, g, b), mn = Math.min(r, g, b), l = (mx + mn) / 2, d = mx - mn;
    if (!d) return [0, 0, l];
    const s = d / (1 - Math.abs(2 * l - 1));
    let h = mx === r ? ((g - b) / d) % 6 : mx === g ? (b - r) / d + 2 : (r - g) / d + 4;
    return [(h * 60 + 360) % 360, s, l];
  }
  function colourKey(w) {
    // The most colourful of the first three palette swatches decides the place in the spectrum;
    // greys, blacks and creams go after the colours, dark to light. Writing goes last.
    const pal = (w.palette || []).slice(0, 3).map(hsl).filter(Boolean);
    if (!pal.length || isLit(w)) return 2000;
    const best = pal.reduce((a, b) => (b[1] * (1 - Math.abs(2 * b[2] - 1)) > a[1] * (1 - Math.abs(2 * a[2] - 1)) ? b : a));
    const chroma = best[1] * (1 - Math.abs(2 * best[2] - 1));
    if (chroma < 0.12) return 1000 + pal[0][2] * 100;
    return ((best[0] + 345) % 360) + best[2] * 0.5;   // start the wheel at deep red
  }
  const yr = w => (typeof w.yearNum === 'number' ? w.yearNum : 99999);
  window.pvArrange = function (list, searchRanked) {
    if (arrange === 'wall') {
      // Colour alone: strongest first, with variety. With a search, the search order leads and colour only filters.
      if (colourOn() && !(state.query || '').trim()) {
        const k = new Map(list.map(w => [w.id, colourRank(w)]));
        return vary(list.slice().sort((x, y) => k.get(y.id) - k.get(x.id)));
      }
      return list;
    }
    const a = list.slice();
    if (arrange === 'date') a.sort((x, y) => yr(x) - yr(y));
    if (arrange === 'colour') { const k = new Map(a.map(w => [w.id, colourKey(w)])); a.sort((x, y) => k.get(x.id) - k.get(y.id)); }
    if (arrange === 'mood') a.sort((x, y) => (MOOD_ORDER.indexOf(x.emotionShort) - MOOD_ORDER.indexOf(y.emotionShort)) || (yr(x) - yr(y)));
    return a;
  };

  // ---- the wall moves rather than blinks ----
  const reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  function snap() {
    const m = new Map();
    document.querySelectorAll('#galleryGrid .art-piece').forEach(el => {
      const r = el.getBoundingClientRect();
      if (r.bottom > -100 && r.top < innerHeight + 100 && el.dataset.wid) m.set(el.dataset.wid, r);
    });
    return m;
  }
  function play(before) {
    if (reduce) return;
    let n = 0;
    document.querySelectorAll('#galleryGrid .art-piece').forEach(el => {
      const r = el.getBoundingClientRect();
      if (r.bottom < 0 || r.top > innerHeight) return;
      const b = before.get(el.dataset.wid);
      if (b) {
        el.style.transition = 'none';
        el.style.transform = `translate(${b.left - r.left}px, ${b.top - r.top}px)`;
        requestAnimationFrame(() => requestAnimationFrame(() => {
          el.style.transition = 'transform 460ms cubic-bezier(.2,.7,.2,1)';
          el.style.transform = '';
          setTimeout(() => { el.style.transition = ''; }, 500);
        }));
      } else {
        el.style.animationDelay = Math.min(n++ * 22, 260) + 'ms';
        el.classList.add('pv-in');
        setTimeout(() => { el.classList.remove('pv-in'); el.style.animationDelay = ''; }, 800);
      }
    });
  }
  if (typeof createCardElement === 'function') {
    const origCard = createCardElement;
    createCardElement = function (w, idx) { const el = origCard(w, idx); if (el && w) el.dataset.wid = w.id; return el; };
  }
  function refresh() {
    if (state.spatialView && !['wall', 'timeline', 'chromatic'].includes(state.spatialView)) setSpatialView('wall');
    const before = snap();
    filterWorks(false);
    play(before);
    drawTools(); drawRead(); syncShow();
  }

  // ---- tool row ----
  function facetLabel(f) {
    if (f.id === 'tone' && shade) return `<span class="pv-dot" style="background:${shade.hex}"></span>${esc(shade.label)}<span class="pv-x" aria-hidden="true">×</span>`;
    const s = [...sel[f.id]];
    if (!s.length) return `${esc(f.label)} ▾`;
    const o = f.opts.filter(x => sel[f.id].has(x[0]));
    const dots = f.id === 'tone' ? o.map(x => `<span class="pv-dot" style="background:${x[2]}"></span>`).join('') : '';
    const words = o.length <= 2 ? o.map(x => esc(x[1])).join(' + ') : `${esc(f.label)} · ${o.length}`;
    return `${dots}${words}<span class="pv-x" aria-hidden="true">×</span>`;
  }
  function drawTools() {
    const arrLbl = arrange === 'wall' ? 'Arrange ▾' : `${esc(ARRANGE.find(a => a[0] === arrange)[1])}<span class="pv-x" aria-hidden="true">×</span>`;
    toolsEl.innerHTML = FACETS.map(f => {
      const set = sel[f.id].size > 0 || (f.id === 'tone' && !!shade);
      return `<button type="button" class="pv-tool${openId === f.id ? ' is-open' : ''}${set ? ' is-set' : ''}" data-pv-tool="${f.id}" aria-expanded="${openId === f.id}" aria-label="${esc(f.label)}">${facetLabel(f)}</button>`;
    }).join('') +
      `<button type="button" class="pv-tool is-arr${openId === 'arrange' ? ' is-open' : ''}${arrange !== 'wall' ? ' is-set' : ''}" data-pv-tool="arrange" aria-expanded="${openId === 'arrange'}">${arrLbl}</button>` +
      `<button type="button" class="pv-tool${openId === 'more' ? ' is-open' : ''}" data-pv-tool="more" aria-expanded="${openId === 'more'}">More ▾</button>`;
  }
  function drawPop() {
    if (!openId) { pop.hidden = true; return; }
    const btn = toolsEl.querySelector(`[data-pv-tool="${openId}"]`);
    if (openId === 'more') {
      pop.innerHTML = `<h3>More</h3><div class="pv-opts">
        <button type="button" class="pv-opt" data-pv-more="timeline">Timeline view</button>
        <button type="button" class="pv-opt" data-pv-more="reading">Reading Room</button>
        <button type="button" class="pv-opt" data-pv-more="drawer">Collection, form and sort</button>
        <button type="button" class="pv-opt" data-pv-more="theme">Light or dark wall</button></div>`;
    } else if (openId === 'arrange') {
      pop.innerHTML = `<h3>Arrange what you see</h3><div class="pv-opts">` + ARRANGE.map(a =>
        `<button type="button" class="pv-opt${arrange === a[0] ? ' is-on' : ''}" data-pv-arr="${a[0]}">${esc(a[1])}</button>`).join('') + `</div>`;
    } else if (openId === 'tone') {
      const f = FACETS[0];
      pop.innerHTML = `<h3>Colour <span style="letter-spacing:0;text-transform:none;opacity:.7">· pick one, or two to have both</span></h3><div class="pv-opts">` + f.opts.map(o =>
        `<button type="button" class="pv-opt${sel.tone.has(o[0]) ? ' is-on' : ''}" data-pv-opt="${esc(o[0])}" aria-pressed="${sel.tone.has(o[0])}"><span class="pv-dot" style="background:${o[2]}"></span>${esc(o[1])}</button>`
      ).join('') + `</div><h3 style="margin-top:16px">Or a shade</h3><div class="pv-pig">` + PIGMENTS.map(p =>
        `<button type="button" class="pv-sw${shade && shade.hex === p[1].toUpperCase() ? ' is-on' : ''}" data-pv-shade="${p[1]}" data-label="${esc(p[0])}" title="${esc(p[0])}" aria-label="${esc(p[0])}" style="background:${p[1]}"></button>`
      ).join('') + `<label class="pv-any" title="Any colour"><input type="color" id="pvPick" value="${shade ? shade.hex : '#8a2b1f'}"><span>Any colour</span></label></div>` +
        `<div class="pv-done"><span>${shade ? esc(shade.label) + ' · ' : ''}${state.currentList.length.toLocaleString()} works</span>` +
        (colourOn() ? `<button type="button" data-pv-clear="1">Clear colour</button>` : '') + `<button type="button" data-pv-close="1">Done</button></div>`;
      const pk = pop.querySelector('#pvPick');
      if (pk) pk.addEventListener('change', () => setShade(pk.value, pk.value.toUpperCase()));
    } else {
      const f = FACETS.find(x => x.id === openId);
      pop.innerHTML = `<h3>${esc(f.label)} <span style="letter-spacing:0;text-transform:none;opacity:.7">· pick one or more</span></h3><div class="pv-opts">` + f.opts.map(o =>
        `<button type="button" class="pv-opt${sel[f.id].has(o[0]) ? ' is-on' : ''}" data-pv-opt="${esc(o[0])}" aria-pressed="${sel[f.id].has(o[0])}">${o[2] ? `<span class="pv-dot" style="background:${o[2]}"></span>` : ''}${esc(o[1])}</button>`
      ).join('') + `</div><div class="pv-done"><span>${state.currentList.length.toLocaleString()} works</span>` +
        (sel[f.id].size ? `<button type="button" data-pv-clear="1">Clear ${esc(f.label.toLowerCase())}</button>` : '') +
        `<button type="button" data-pv-close="1">Done</button></div>`;
    }
    const r = btn.getBoundingClientRect(), rr = row.getBoundingClientRect();
    pop.style.left = Math.max(0, Math.min(r.left - rr.left, rr.width - 380)) + 'px';
    pop.hidden = false;
  }
  function close() { openId = ''; drawTools(); drawPop(); }

  toolsEl.addEventListener('click', (e) => {
    const b = e.target.closest('[data-pv-tool]'); if (!b) return;
    const id = b.dataset.pvTool;
    if (e.target.classList.contains('pv-x')) {
      if (id === 'arrange') arrange = 'wall'; else if (sel[id]) sel[id].clear();
      if (id === 'tone') { shade = null; scoreShade(); }
      openId = ''; refresh(); drawPop(); return;
    }
    openId = openId === id ? '' : id;
    drawTools(); drawPop();
  });
  pop.addEventListener('click', (e) => {
    const o = e.target.closest('[data-pv-opt]');
    const sw = e.target.closest('[data-pv-shade]');
    if (sw) { const same = shade && shade.hex === sw.dataset.pvShade.toUpperCase(); setShade(same ? null : sw.dataset.pvShade, sw.dataset.label); return; }
    if (o) {   // several values per facet: toggle and keep the panel open
      if (openId === 'tone' && shade) { shade = null; scoreShade(); }
      const s = sel[openId], v = o.dataset.pvOpt;
      s.has(v) ? s.delete(v) : s.add(v);
      refresh(); drawPop(); return;
    }
    if (e.target.closest('[data-pv-clear]')) { sel[openId].clear(); if (openId === 'tone') { shade = null; scoreShade(); } refresh(); drawPop(); return; }
    if (e.target.closest('[data-pv-close]')) { close(); return; }
    const a = e.target.closest('[data-pv-arr]');
    if (a) { arrange = a.dataset.pvArr; openId = ''; refresh(); drawPop(); window.scrollTo({ top: 0 }); return; }
    const m = e.target.closest('[data-pv-more]'); if (!m) return;
    const k = m.dataset.pvMore; close();
    if (k === 'drawer') document.getElementById('toggleDrawerBtn').click();
    if (k === 'timeline' || k === 'chromatic' || k === 'reading') { setSpatialView(k); syncShow(); }
    if (k === 'theme') document.getElementById('wallThemeBtn').click();
  });
  document.addEventListener('click', (e) => {
    if (!openId) return;
    if (e.composedPath().some(n => n === pop || n === toolsEl)) return;
    close();
  });
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && openId) close(); });

  // ---- Show: All / Art / Writing ----
  function syncShow() {
    const inRoom = state.spatialView === 'reading';
    document.querySelectorAll('.pv-seg').forEach(b => b.classList.toggle('is-on', !inRoom && b.dataset.pvShow === show));
    document.getElementById('pvRoom').classList.toggle('is-on', inRoom);
  }
  document.querySelectorAll('.pv-seg').forEach(b => b.addEventListener('click', () => {
    show = b.dataset.pvShow;
    try { localStorage.setItem('pvShow', show); } catch (e) {}
    refresh();
  }));
  document.getElementById('pvRoom').addEventListener('click', () => { setSpatialView('reading'); syncShow(); });
  if (typeof setSpatialView === 'function') {
    const orig = setSpatialView;
    setSpatialView = function (v) { const r = orig(v); syncShow(); return r; };
  }

  // ---- the read-back line: what you asked for, and how many works it found ----
  const bar = document.getElementById('wallControlsBar');
  const read = document.createElement('div'); read.className = 'pv-read'; read.id = 'pvRead';
  if (bar) bar.insertBefore(read, bar.firstChild);
  function drawRead() {
    const parts = [];
    if (show !== 'both') parts.push(['show', '', show === 'art' ? 'Art only' : 'Writing only']);
    if (shade) parts.push(['shade', '', shade.label]);
    const tones = FACETS[0].opts.filter(o => sel.tone.has(o[0]));
    if (tones.length) parts.push(['tone', '', tones.map(o => o[1]).join(' with ')]);
    FACETS.slice(1).forEach(f => f.opts.forEach(o => { if (sel[f.id].has(o[0])) parts.push([f.id, o[0], o[1]]); }));
    const q = (state.query || '').trim();
    if (q) parts.push(['q', '', `“${q}”`]);
    if (arrange !== 'wall') parts.push(['arr', '', ARRANGE.find(a => a[0] === arrange)[1].toLowerCase()]);
    if (!parts.length) { read.innerHTML = ''; return; }
    const n = state.currentList.length;
    read.innerHTML = parts.map(p => `<button type="button" class="pv-chip" data-k="${p[0]}" data-v="${esc(p[1])}" title="Remove">${p[0] === 'shade' ? `<span class="pv-dot" style="background:${shade.hex};display:inline-block;width:10px;height:10px;border-radius:5px;margin-right:6px"></span>` : ''}${esc(p[2])}</button>`).join('<span class="pv-sep">·</span>') +
      `<span class="pv-count">— ${n.toLocaleString()} ${n === 1 ? 'work' : 'works'}</span><button type="button" class="pv-clear" data-k="all">Clear</button>`;
  }
  read.addEventListener('click', (e) => {
    const b = e.target.closest('[data-k]'); if (!b) return;
    const k = b.dataset.k, v = b.dataset.v;
    if (k === 'all') { clearAll(); return; }
    if (k === 'show') { show = 'both'; try { localStorage.setItem('pvShow', show); } catch (er) {} }
    else if (k === 'arr') arrange = 'wall';
    else if (k === 'q') { state.query = ''; const inp = document.querySelector('.header-search-input'); if (inp) inp.value = ''; }
    else if (k === 'shade') { shade = null; scoreShade(); }
    else if (k === 'tone') sel.tone.clear();
    else sel[k].delete(v);
    refresh();
  });
  function clearAll() {
    FACETS.forEach(f => sel[f.id].clear()); arrange = 'wall'; show = 'both'; shade = null; scoreShade();
    try { localStorage.setItem('pvShow', show); } catch (e) {}
    state.query = ''; const inp = document.querySelector('.header-search-input'); if (inp) inp.value = '';
    refresh();
  }
  // Searching from the box updates the read-back too.
  if (typeof updateCountDisplay === 'function') {
    const origCount = updateCountDisplay;
    updateCountDisplay = function () { const r = origCount.apply(this, arguments); drawRead(); return r; };
  }
  // The logo and the old Reset go back to the front of house: filters off, the woven wall.
  ['resetAllBtn', 'emptyResetBtn', 'clearFiltersBtn'].forEach(id => {
    const el = document.getElementById(id);
    if (el) el.addEventListener('click', () => { FACETS.forEach(f => sel[f.id].clear()); arrange = 'wall'; shade = null; scoreShade(); setTimeout(() => {
      if (id === 'resetAllBtn' && state.spatialView !== 'wall') setSpatialView('wall'); filterWorks(false); drawTools(); drawRead(); syncShow(); }, 0); });
  });
  // Shuffle leaves any arrangement and animates too.
  const sh = document.getElementById('shuffleBtn');
  if (sh) sh.addEventListener('click', () => { const before = snap(); arrange = 'wall'; setTimeout(() => { play(before); drawTools(); drawRead(); }, 0); }, true);

  // ---- top bar extras ----
  const sb = document.getElementById('savedFilterBtn');
  if (sb) sb.childNodes.forEach(n => { if (n.nodeType === 3) n.nodeValue = n.nodeValue.replace('Saved (', 'Saved ').replace(')', ''); });
  const acts = document.querySelector('.nav-actions');
  if (acts) {
    const tb = document.createElement('button');
    tb.type = 'button'; tb.className = 'pv-theme'; tb.setAttribute('aria-label', 'Switch between dark and light wall');
    tb.innerHTML = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="4.5"></circle><path d="M12 2v2.5M12 19.5V22M2 12h2.5M19.5 12H22M4.9 4.9l1.8 1.8M17.3 17.3l1.8 1.8M4.9 19.1l1.8-1.8M17.3 6.7l1.8-1.8"></path></svg>';
    tb.addEventListener('click', () => document.getElementById('wallThemeBtn').click());
    acts.appendChild(tb);
  }

  // ---- data that loads after the wall is up: neighbours, meaning vectors, picture descriptions ----
  const BASE = location.pathname.replace(/[^/]*$/, '');
  const V = (document.querySelector('script[src*="data/site.js"]') || {}).src || '';
  const ver = (V.split('?')[1] || '');
  let SIM = null, simP = null;
  function loadSim() {
    return simP || (simP = fetch(BASE + 'data/similar.json?' + ver).then(r => r.json()).then(j => {
      const ids = j.ids; SIM = new Map(ids.map((id, i) => [id, j.nb[i].map(k => ids[k])])); return SIM;
    }).catch(() => null));
  }
  // Hidden picture descriptions: searchable, never shown.
  function loadSee() {
    return fetch(BASE + 'data/see.json?' + ver).then(r => r.json()).then(j => {
      const by = new Map(WORKS.map(w => [w.id, w]));
      for (const id in j) { const w = by.get(id); if (w) { w.searchTags = ((w.searchTags || '') + ' ' + j[id]).trim(); w._searchIdx = null; } }
      if ((state.query || '').trim()) filterWorks(true);
    }).catch(() => {});
  }
  (window.requestIdleCallback || (f => setTimeout(f, 2500)))(() => { loadSee(); });

  // More like this, under the note in the lightbox.
  const lbNote = document.getElementById('lbNote');
  const more = document.createElement('div'); more.className = 'pv-like'; more.id = 'pvLike';
  const lbAnchor = document.querySelector('.lb-palette-row') || lbNote;
  if (lbAnchor) lbAnchor.parentNode.insertBefore(more, lbAnchor.nextSibling);
  function thumbUrl(w) {
    const u = w.imageUrl || '';
    if (/upload\.wikimedia\.org\/.*\/thumb\//.test(u)) return u.replace(/\/\d+px-/, '/330px-');
    if (/artic\.edu\/iiif/.test(u)) return u.replace(/\/full\/[^/]+\//, '/full/200,/');
    return u;
  }
  async function showLike(w) {
    more.innerHTML = '';
    if (!w) return;
    const sim = await loadSim(); if (!sim) return;
    const by = new Map(WORKS.map(x => [x.id, x]));
    const nb = (sim.get(w.id) || []).map(id => by.get(id)).filter(x => x && !x._broken);
    if (!nb.length || state.currentList[state.activeWorkIndex] !== w) return;
    const lit = isLit(w);
    more.innerHTML = `<div class="pv-like-h">More like this</div>` + (lit
      ? `<div class="pv-like-lines">` + nb.slice(0, 4).map(x => `<button type="button" data-id="${x.id}"><span>“${esc((x.hook || '').slice(0, 90))}${(x.hook || '').length > 90 ? '…' : ''}”</span><em>${esc(x.artist || '')}</em></button>`).join('') + `</div>`
      : `<div class="pv-like-row">` + nb.slice(0, 8).map(x => isLit(x)
          ? `<button type="button" class="pv-like-word" data-id="${x.id}" title="${esc(x.title)}">“${esc((x.hook || '').slice(0, 40))}…”</button>`
          : `<button type="button" data-id="${x.id}" title="${esc(x.title)} · ${esc(x.artist || '')}"><img loading="lazy" alt="${esc(x.title)}" src="${esc(thumbUrl(x))}"></button>`).join('') + `</div>`);
    more.querySelectorAll('img').forEach(im => im.addEventListener('error', () => { im.closest('button').remove(); }));
  }
  // A colour in the lightbox's palette is a way in: tap it to see that shade across the collection.
  const lbPal = document.getElementById('lbPalette');
  if (lbPal) {
    lbPal.addEventListener('click', (e) => {
      const d = e.target.closest('.swatch-dot'); if (!d) return;
      e.stopImmediatePropagation(); e.preventDefault();
      const w = state.currentList[state.activeWorkIndex];
      closeLightbox();
      if (show === 'writing') { show = 'both'; try { localStorage.setItem('pvShow', show); } catch (er) {} }
      setShade(d.dataset.hex, 'Colour from ' + (w ? (w.title.length > 34 ? w.title.slice(0, 32) + '…' : w.title) : 'this work'));
      window.scrollTo({ top: 0 });
    }, true);
    new MutationObserver(() => lbPal.querySelectorAll('.swatch-dot').forEach(d => { d.title = 'More in this colour'; }))
      .observe(lbPal, { childList: true });
  }
  if (location.hash.startsWith('#w/')) setTimeout(() => showLike(state.currentList[state.activeWorkIndex]), 0);
  more.addEventListener('click', (e) => { const b = e.target.closest('[data-id]'); if (b) openWorkById(b.dataset.id); });
  if (typeof openLightbox === 'function') {
    const origOpenLb = openLightbox;
    openLightbox = function (index) { const r = origOpenLb(index); showLike(state.currentList[index]); return r; };
  }

  // Search by meaning. Word matches still come first (names, titles, quotes); works that match the
  // meaning of the search follow. The small model loads on the first search and is cached by the browser.
  let VEC = null, VIDX = null, D = 384, vecP = null, ex = null, exP = null; const qVec = new Map();
  function loadVec() {
    return vecP || (vecP = Promise.all([
      fetch(BASE + 'data/vec.bin?' + ver).then(r => r.arrayBuffer()),
      loadSim()
    ]).then(([buf]) => fetch(BASE + 'data/similar.json?' + ver).then(r => r.json()).then(j => {
      VEC = new Int8Array(buf); D = VEC.length / j.ids.length; VIDX = new Map(j.ids.map((id, i) => [id, i]));
    })).catch(() => null));
  }
  function loadModel() {
    return exP || (exP = import('https://cdn.jsdelivr.net/npm/@huggingface/transformers@3.8.1').then(async m => {
      m.env.allowLocalModels = false;
      ex = await m.pipeline('feature-extraction', 'Xenova/bge-small-en-v1.5', { dtype: 'q8' });
      return ex;
    }).catch(() => null));
  }
  const normQ = q => q.trim().toLowerCase().replace(/\s+/g, ' ');
  let semTimer = null;
  async function embedQuery(q) {
    const k = normQ(q); if (k.length < 3 || qVec.has(k)) return;
    await Promise.all([loadModel(), loadVec()]); if (!ex || !VEC) return;
    const out = await ex('Represent this sentence for searching relevant passages: ' + k, { pooling: 'cls', normalize: true });
    qVec.set(k, out.data);
    if (normQ(state.query || '') === k) { const before = snap(); filterWorks(false); play(before); drawRead(); }
  }
  const inp = document.querySelector('.header-search-input');
  if (inp) {
    inp.addEventListener('focus', () => { loadModel(); loadVec(); }, { once: true });
    inp.addEventListener('input', () => { clearTimeout(semTimer); const q = inp.value; semTimer = setTimeout(() => embedQuery(q), 380); });
  }
  if (typeof runFiveStageArchiveSearch === 'function') {
    const origSearch = runFiveStageArchiveSearch;
    runFiveStageArchiveSearch = function (pool, raw) {
      const r = origSearch(pool, raw);
      const v = qVec.get(normQ(raw || ''));
      if (!v || !VEC) return r;
      // One score: meaning, plus a boost when the words appear whole in the title, maker, mood or subject,
      // and a small one for whole words in the note, text or picture description. Word fragments don't count.
      const toks = normalizeSearchStr(raw).split(' ').filter(t => t && !SEARCH_STOP_WORDS.has(t));
      const phrase = toks.join(' ');
      const has = (set, t) => set.has(t) || set.has(t + 's') || set.has(t + 'es') || (t.endsWith('s') && set.has(t.slice(0, -1)));
      const floor = window.pvSemFloor || 0.56, band = window.pvSemBand || 0.12;
      const scored = [];
      let top = 0;
      for (const w of pool) {
        const i = VIDX.get(w.id); if (i === undefined) continue;
        let sem = 0; const o = i * D; for (let d = 0; d < D; d++) sem += VEC[o + d] * v[d]; sem /= 127;
        const idx = getWorkSearchIndex(w);
        if (!idx._hi) { idx._hi = new Set(idx.highWords); idx._lo = new Set((idx.mid + ' ' + idx.low).split(' ')); }
        let kw = 0;
        if (toks.length) {
          if (toks.length > 1 && (' ' + idx.high + ' ').includes(' ' + phrase + ' ')) kw = 0.3;
          else if (toks.every(t => has(idx._hi, t))) kw = 0.2;
          else if (toks.every(t => has(idx._hi, t) || has(idx._lo, t))) kw = 0.06;
        }
        if (sem > top) top = sem;
        scored.push([w, sem, kw]);
      }
      const cut = Math.max(floor, top - band);
      const items = scored.filter(x => x[2] >= 0.2 || x[1] >= cut || (x[2] > 0 && x[1] + x[2] >= cut))
        .sort((a, b) => (b[1] + b[2]) - (a[1] + a[2])).slice(0, 400).map(x => x[0]);
      // Typos and odd names: if none of the words occur anywhere, the old search's typo matching knows better.
      if (r.items.length && !r.relaxed && !scored.some(x => x[2] > 0)) return r;
      if (items.length < 4 && r.items.length) return r;
      const relaxEl = document.getElementById('relaxedSearchBadge'); if (relaxEl) { relaxEl.textContent = ''; relaxEl.classList.remove('visible'); }
      return { items, relaxed: false, matchedTokens: r.totalTokens, totalTokens: r.totalTokens };
    };
  }
  window.pvSem = { qVec, embedQuery, loadVec, loadModel };

  if (show !== 'both') filterWorks(false);
  drawTools(); drawRead(); syncShow();
})();
