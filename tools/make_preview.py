"""Build preview.html: index.html with the new arrival design (option E, 20 Nov 2026).

The live site is untouched. preview.html is index.html plus:
  - a mood filter in the state and the filter function,
  - one bar on top (logo, search, Saved, theme icon),
  - a tool row under it: Art · Writing · Timeline, then Colour, Mood, Era,
    Region, Medium and More, each opening a small panel of choices.
The old controls stay in the page, hidden, so every existing handler keeps
working; the new buttons drive the same state.

Run: python3 tools/make_preview.py   (rerun after any change to index.html)
"""
import pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
src = (ROOT / 'index.html').read_text()


def sub_once(old, new, text, label):
    if text.count(old) < 1:
        sys.exit(f'make_preview: anchor not found: {label}')
    return text.replace(old, new, 1)


s = src

# 1. Not for search engines.
s = sub_once('<head>', '<head>\n  <meta name="robots" content="noindex">', s, 'head')

# 2. Mood filter: state, filter, reset, "has filters" check.
s = sub_once("      tone: 'ALL',", "      tone: 'ALL',\n      mood: 'ALL',", s, 'state.tone')
s = sub_once("        if (state.tone !== 'ALL' && w.colorFamily !== state.tone) return false;",
             "        if (state.tone !== 'ALL' && w.colorFamily !== state.tone) return false;\n"
             "        if (state.mood && state.mood !== 'ALL' && w.emotionShort !== state.mood) return false;",
             s, 'filter tone')
s = sub_once("      state.tone = 'ALL';\n      state.pigmentHex = '';",
             "      state.tone = 'ALL';\n      state.mood = 'ALL';\n      state.pigmentHex = '';", s, 'reset tone')
s = sub_once("state.tone !== 'ALL' || state.pigmentHex !== ''",
             "state.tone !== 'ALL' || (state.mood && state.mood !== 'ALL') || state.pigmentHex !== ''", s, 'has filters')

# 3. Placeholder.
s = sub_once('placeholder="Search artist, mood, era or line…"',
             'placeholder="Search an artist, a mood, a line…"', s, 'placeholder')

# 4. The tool row, right under the top bar inside the sticky header.
TOOLROW = '''
    <div class="pv-toolrow" id="pvToolRow">
      <nav class="pv-tabs" aria-label="Sections">
        <button type="button" class="pv-tab is-on" data-pv-view="wall">Art</button>
        <button type="button" class="pv-tab" data-pv-view="reading">Writing</button>
        <button type="button" class="pv-tab" data-pv-view="timeline">Timeline</button>
      </nav>
      <span class="pv-rule" aria-hidden="true"></span>
      <div class="pv-tools" id="pvTools"></div>
      <div class="pv-pop" id="pvPop" role="dialog" aria-label="Choices" hidden></div>
    </div>
'''
s = sub_once('    <!-- Whisper-Quiet View Switcher', TOOLROW + '\n    <!-- Whisper-Quiet View Switcher', s, 'toolrow anchor')

# 5. Styles, last in <head> so they win.
CSS = r'''
  <style id="pvStyles">
    /* Preview: option E. Top bar = logo, search, Saved, theme. */
    header { padding: 14px 40px 0 !important; }
    header.is-scrolled { margin-bottom: 0 !important; }
    .nav-primary { flex-wrap: nowrap !important; gap: 28px !important; row-gap: 0 !important; }
    .header-search-cluster, .header-search-cluster:focus-within,
    header.is-scrolled .header-search-cluster, header.is-scrolled .header-search-cluster:focus-within {
      order: 0 !important; flex: 1 1 520px !important; max-width: 760px !important; width: auto !important;
      margin: 0 auto !important;
    }
    .header-search-box, header.is-scrolled .header-search-box { height: 46px !important; padding: 0 12px 0 18px !important; animation: none !important; }
    .header-search-input, header.is-scrolled .header-search-input { font-size: 1.15rem !important; }
    #searchSlashHint { display: none !important; }
    #toggleViewsBtn, #toggleDrawerBtn, #wallThemeBtn { display: none !important; }
    #spatialViewsDrawer { display: none !important; }
    .nav-actions { gap: 6px !important; }
    #savedFilterBtn { display: inline-flex !important; align-items: center; gap: 7px; font-size: 0.92rem !important; color: var(--text) !important; min-height: 44px; padding: 0 8px !important; }
    #savedFilterBtn::before { content: ''; width: 11px; height: 14px; border: 1.5px solid currentColor; border-bottom: 0;
      clip-path: polygon(0 0, 100% 0, 100% 100%, 50% 72%, 0 100%); background: transparent; box-sizing: border-box; }
    #savedFilterBtn.active::before { background: currentColor; }
    #savedCount { color: var(--text-muted); }
    .pv-theme { width: 44px; height: 44px; border: 0; background: none; color: var(--text-muted); cursor: pointer; display: inline-flex; align-items: center; justify-content: center; }
    .pv-theme:hover { color: var(--text); }

    /* Tool row */
    .pv-toolrow { max-width: 1744px; margin: 12px auto 0; height: 56px; display: flex; align-items: center; gap: 8px; position: relative; }
    .pv-tabs { display: flex; gap: 22px; margin-right: 14px; }
    .pv-tab { background: none; border: 0; padding: 12px 0; font: inherit; font-size: 0.92rem; color: var(--text-muted); cursor: pointer; border-bottom: 1px solid transparent; }
    .pv-tab:hover { color: var(--text); }
    .pv-tab.is-on { color: var(--text); border-bottom-color: var(--text); }
    .pv-rule { width: 1px; height: 22px; background: var(--border); margin-right: 8px; flex: 0 0 1px; }
    .pv-tools { display: flex; gap: 8px; align-items: center; overflow-x: auto; scrollbar-width: none; }
    .pv-tools::-webkit-scrollbar { display: none; }
    .pv-tool { flex: 0 0 auto; height: 36px; padding: 0 14px; border-radius: 18px; border: 1px solid var(--border-active, #3a3835); background: transparent; color: var(--text); font: inherit; font-size: 0.86rem; cursor: pointer; display: inline-flex; align-items: center; gap: 8px; white-space: nowrap; }
    .pv-tool:hover { border-color: var(--text-muted); }
    .pv-tool.is-open { background: var(--text); color: var(--bg); border-color: var(--text); }
    .pv-tool.is-set { border-color: var(--text); }
    .pv-tool .pv-dot { width: 12px; height: 12px; border-radius: 6px; }
    .pv-tool .pv-x { color: var(--text-muted); margin-left: 2px; }
    .pv-pop { position: absolute; top: 54px; z-index: 60; width: 380px; max-width: calc(100vw - 32px); box-sizing: border-box; background: var(--bg-elevated, #141413); border: 1px solid var(--border); border-radius: 16px; padding: 18px; box-shadow: 0 30px 80px rgba(0,0,0,0.55); }
    .pv-pop h3 { margin: 0 0 12px; font-size: 0.68rem; letter-spacing: 0.16em; font-weight: 500; color: var(--text-muted); text-transform: uppercase; }
    .pv-opts { display: flex; flex-wrap: wrap; gap: 8px; }
    .pv-opt { height: 36px; padding: 0 14px; border-radius: 18px; border: 1px solid var(--border-active, #3a3835); background: transparent; color: var(--text); font: inherit; font-size: 0.86rem; cursor: pointer; display: inline-flex; align-items: center; gap: 8px; }
    .pv-opt:hover { border-color: var(--text-muted); }
    .pv-opt.is-on { background: var(--text); color: var(--bg); border-color: var(--text); }
    .pv-opt .pv-dot { width: 14px; height: 14px; border-radius: 7px; }
    .pv-more { margin-top: 14px; padding-top: 12px; border-top: 1px solid var(--border); display: flex; justify-content: space-between; font-size: 0.82rem; }
    .pv-more button { background: none; border: 0; color: var(--text-muted); font: inherit; cursor: pointer; padding: 6px 0; }
    .pv-more button:hover { color: var(--text); }
    .wall-controls-bar { opacity: 1 !important; }
    .wall-micro-btn { color: var(--text-muted) !important; }
    .wall-micro-btn:hover { color: var(--text) !important; }

    @media (max-width: 760px) {
      header { padding: 10px 14px 0 !important; }
      .nav-primary { flex-wrap: wrap !important; row-gap: 8px !important; }
      .header-search-cluster, .header-search-cluster:focus-within,
      header.is-scrolled .header-search-cluster { order: 3 !important; flex: 1 1 100% !important; max-width: none !important; }
      .pv-toolrow { margin-top: 4px; }
      .pv-tabs { gap: 16px; margin-right: 6px; }
      .pv-rule { display: none; }
      .pv-pop { left: 0 !important; right: 0; width: auto; }
    }
  </style>
'''
s = sub_once('</head>', CSS + '</head>', s, '</head>')

# 6. Script, last in <body>.
JS = r'''
<script id="pvScript">
(function () {
  const TOOLS = [
    { id: 'colour', label: 'Colour', key: 'tone', opts: [
      ['Obsidian & Ink', 'Black', '#1c1c1e'], ['Crimson & Rust', 'Red', '#9e2f24'], ['Ochre & Gold', 'Gold', '#c89d3c'],
      ['Indigo & Prussian', 'Blue', '#24486b'], ['Verdigris & Forest', 'Green', '#3b6352'], ['Parchment & Bone', 'Cream', '#d8ceb8'] ] },
    { id: 'mood', label: 'Mood', key: 'mood', opts: ['Dread', 'Sublime', 'Melancholy', 'Fury', 'Yearning', 'Resolve', 'Dark Humor'].map(m => [m, m]) },
    { id: 'era', label: 'Era', key: 'era', select: 'eraSelect', opts: [
      ['Ancient & Medieval', 'Before 1400'], ['1400–1650', '1400–1650'], ['1650–1800', '1650–1800'], ['1800–1920', '1800–1920'], ['1920–Now', '1920–now'] ] },
    { id: 'region', label: 'Region', key: 'region', select: 'regionSelect', opts: [
      ['Europe', 'Europe'], ['Americas', 'Americas'], ['East & Inner Asia', 'East & Inner Asia'],
      ['Near East & South Asia', 'Near East & South Asia'], ['Africa, Oceania & Indigenous Americas', 'Africa, Oceania & Indigenous Americas'] ] },
    { id: 'medium', label: 'Medium', key: 'medium', select: 'mediumSelect', opts: [
      ['Painting', 'Painting'], ['Print & Woodcut', 'Print & Woodcut'], ['Photograph & Film', 'Photograph & Film'],
      ['Sculpture & Metalwork', 'Sculpture & Metalwork'], ['Scroll & Paper', 'Scroll & Paper'],
      ['Diagram, Cyanotype & Textile', 'Diagram, Cyanotype & Textile'], ['Letterform, Score & Ephemera', 'Letterform, Score & Ephemera'],
      ['Literature & Verse', 'Writing'] ] }
  ];
  const toolsEl = document.getElementById('pvTools');
  const pop = document.getElementById('pvPop');
  const row = document.getElementById('pvToolRow');
  let openId = '';

  function cur(t) { return (typeof state !== 'undefined' && state[t.key]) || 'ALL'; }
  function esc(x) { return String(x).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/"/g, '&quot;'); }

  function setVal(t, val) {
    if (t.key === 'tone' && typeof setToneFilter === 'function') { setToneFilter(val); }
    else {
      state[t.key] = val;
      if (t.select) { const el = document.getElementById(t.select); if (el) el.value = val; }
      if (typeof filterWorks === 'function') filterWorks(false);
    }
    drawTools();
  }

  function drawTools() {
    toolsEl.innerHTML = TOOLS.map(t => {
      const v = cur(t);
      const o = t.opts.find(x => x[0] === v);
      const set = v !== 'ALL' && o;
      const dot = set && o[2] ? `<span class="pv-dot" style="background:${o[2]}"></span>` : '';
      const lbl = set ? `${dot}${esc(o[1])}<span class="pv-x" aria-hidden="true">×</span>` : `${esc(t.label)} ▾`;
      return `<button type="button" class="pv-tool${openId === t.id ? ' is-open' : ''}${set ? ' is-set' : ''}" data-pv-tool="${t.id}" aria-expanded="${openId === t.id}" aria-label="${esc(t.label)}${set ? ': ' + esc(o[1]) : ''}">${lbl}</button>`;
    }).join('') + `<button type="button" class="pv-tool${openId === 'more' ? ' is-open' : ''}" data-pv-tool="more" aria-expanded="${openId === 'more'}">More ▾</button>`;
  }

  function drawPop() {
    if (!openId) { pop.hidden = true; return; }
    const btn = toolsEl.querySelector(`[data-pv-tool="${openId}"]`);
    if (openId === 'more') {
      pop.innerHTML = `<h3>More</h3><div class="pv-opts">
        <button type="button" class="pv-opt" data-pv-more="drawer">Collection, form and sort</button>
        <button type="button" class="pv-opt" data-pv-more="chromatic">Colour view</button>
        <button type="button" class="pv-opt" data-pv-more="theme">Light or dark wall</button>
        <button type="button" class="pv-opt" data-pv-more="reset">Clear every filter</button></div>`;
    } else {
      const t = TOOLS.find(x => x.id === openId);
      const v = cur(t);
      pop.innerHTML = `<h3>${esc(t.label)}</h3><div class="pv-opts">` + t.opts.map(o =>
        `<button type="button" class="pv-opt${v === o[0] ? ' is-on' : ''}" data-pv-opt="${esc(o[0])}">${o[2] ? `<span class="pv-dot" style="background:${o[2]}"></span>` : ''}${esc(o[1])}</button>`
      ).join('') + `</div>` + (v !== 'ALL' ? `<div class="pv-more"><button type="button" data-pv-clear="1">Clear ${esc(t.label.toLowerCase())}</button></div>` : '');
    }
    const r = btn.getBoundingClientRect(), rr = row.getBoundingClientRect();
    pop.style.left = Math.max(0, Math.min(r.left - rr.left, rr.width - 380)) + 'px';
    pop.hidden = false;
  }

  toolsEl.addEventListener('click', (e) => {
    const b = e.target.closest('[data-pv-tool]'); if (!b) return;
    const id = b.dataset.pvTool;
    const t = TOOLS.find(x => x.id === id);
    // A tool that is set: clicking its × area clears it; clicking elsewhere opens it.
    if (t && cur(t) !== 'ALL' && e.target.classList.contains('pv-x')) { openId = ''; setVal(t, 'ALL'); drawPop(); return; }
    openId = openId === id ? '' : id;
    drawTools(); drawPop();
  });
  pop.addEventListener('click', (e) => {
    const t = TOOLS.find(x => x.id === openId);
    const o = e.target.closest('[data-pv-opt]');
    if (o && t) { const v = o.dataset.pvOpt; openId = ''; setVal(t, cur(t) === v ? 'ALL' : v); drawPop(); return; }
    if (e.target.closest('[data-pv-clear]') && t) { openId = ''; setVal(t, 'ALL'); drawPop(); return; }
    const m = e.target.closest('[data-pv-more]'); if (!m) return;
    const k = m.dataset.pvMore; openId = ''; drawTools(); drawPop();
    if (k === 'drawer') document.getElementById('toggleDrawerBtn').click();
    if (k === 'chromatic') setSpatialView('chromatic');
    if (k === 'theme') document.getElementById('wallThemeBtn').click();
    if (k === 'reset') { const c = document.getElementById('clearFiltersBtn'); if (c) c.click(); else if (typeof resetAll === 'function') resetAll(); drawTools(); }
  });
  document.addEventListener('click', (e) => {
    if (!openId) return;
    if (e.composedPath().some(n => n === pop || n === toolsEl)) return;
    openId = ''; drawTools(); drawPop();
  });
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && openId) { openId = ''; drawTools(); drawPop(); } });

  // Section tabs drive the existing views.
  function syncTabs() {
    const v = (typeof state !== 'undefined' && state.spatialView) || 'wall';
    document.querySelectorAll('.pv-tab').forEach(b => b.classList.toggle('is-on', b.dataset.pvView === v));
  }
  document.querySelectorAll('.pv-tab').forEach(b => b.addEventListener('click', () => { setSpatialView(b.dataset.pvView); syncTabs(); }));
  if (typeof setSpatialView === 'function') {
    const orig = setSpatialView;
    setSpatialView = function (v) { const r = orig(v); syncTabs(); return r; };
  }

  // Saved: "Saved 3", always shown.
  const sb = document.getElementById('savedFilterBtn');
  if (sb) sb.childNodes.forEach(n => { if (n.nodeType === 3) n.nodeValue = n.nodeValue.replace('Saved (', 'Saved ').replace(')', ''); });

  // Theme as a small icon.
  const acts = document.querySelector('.nav-actions');
  if (acts) {
    const tb = document.createElement('button');
    tb.type = 'button'; tb.className = 'pv-theme'; tb.setAttribute('aria-label', 'Switch between dark and light wall');
    tb.innerHTML = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="4.5"></circle><path d="M12 2v2.5M12 19.5V22M2 12h2.5M19.5 12H22M4.9 4.9l1.8 1.8M17.3 17.3l1.8 1.8M4.9 19.1l1.8-1.8M17.3 6.7l1.8-1.8"></path></svg>';
    tb.addEventListener('click', () => document.getElementById('wallThemeBtn').click());
    acts.appendChild(tb);
  }

  // Keep the tool labels in step when the old controls (Reset, pigment chips) change state.
  const clr = document.getElementById('clearFiltersBtn'); if (clr) clr.addEventListener('click', () => setTimeout(drawTools, 0));
  const brand = document.getElementById('resetAllBtn'); if (brand) brand.addEventListener('click', () => setTimeout(() => { drawTools(); syncTabs(); }, 0));

  drawTools(); syncTabs();
})();
</script>
'''
idx = s.rfind('</body>')
s = s[:idx] + JS + s[idx:]

(ROOT / 'preview.html').write_text(s)
print('preview.html written', len(s))
