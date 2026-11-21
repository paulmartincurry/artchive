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

# 2. Hooks: the new tools filter, arrange and report through three window functions.
s = sub_once("        if (state.tone !== 'ALL' && w.colorFamily !== state.tone) return false;",
             "        if (state.tone !== 'ALL' && w.colorFamily !== state.tone) return false;\n"
             "        if (window.pvPass && !window.pvPass(w)) return false;", s, 'filter hook')
s = sub_once("      state.currentList = filtered;\n",
             "      state.currentList = window.pvArrange ? window.pvArrange(filtered, searchRanked) : filtered;\n", s, 'arrange hook')
s = sub_once("state.tone !== 'ALL' || state.pigmentHex !== ''",
             "state.tone !== 'ALL' || (window.pvActive && window.pvActive()) || state.pigmentHex !== ''", s, 'has filters')

# 3. Placeholder.
s = sub_once('placeholder="Search artist, mood, era or line…"',
             'placeholder="Search an artist, a mood, a line…"', s, 'placeholder')

# 4. The tool row, right under the top bar inside the sticky header.
TOOLROW = '''
    <div class="pv-toolrow" id="pvToolRow">
      <div class="pv-show" role="group" aria-label="Show">
        <button type="button" class="pv-seg is-on" data-pv-show="both">All</button>
        <button type="button" class="pv-seg" data-pv-show="art">Art</button>
        <button type="button" class="pv-seg" data-pv-show="writing">Writing</button>
      </div>
      <span class="pv-rule" aria-hidden="true"></span>
      <div class="pv-tools" id="pvTools"></div>
      <button type="button" class="pv-room" id="pvRoom">Reading Room</button>
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
    .pv-show { display: flex; gap: 20px; margin-right: 12px; flex: 0 0 auto; }
    .pv-seg { background: none; border: 0; padding: 12px 0; font: inherit; font-size: 0.92rem; color: var(--text-muted); cursor: pointer; border-bottom: 1px solid transparent; }
    .pv-seg:hover { color: var(--text); }
    .pv-seg.is-on { color: var(--text); border-bottom-color: var(--text); }
    .pv-room { margin-left: auto; flex: 0 0 auto; background: none; border: 0; font: inherit; font-size: 0.86rem; color: var(--text-muted); cursor: pointer; padding: 12px 0 12px 16px; }
    .pv-room:hover, .pv-room.is-on { color: var(--text); }
    .pv-tool.is-arr { border-style: dashed; }
    .pv-done { margin-top: 14px; padding-top: 12px; border-top: 1px solid var(--border); display: flex; justify-content: space-between; align-items: center; font-size: 0.82rem; color: var(--text-muted); }
    .pv-done button { background: none; border: 0; color: var(--text-muted); font: inherit; cursor: pointer; padding: 6px 0; }
    .pv-done button:hover { color: var(--text); }
    /* The read-back line, left of Shuffle / Captions */
    .wall-controls-bar { justify-content: flex-end; }
    .pv-read { margin-right: auto; display: flex; flex-wrap: wrap; align-items: center; gap: 6px 4px; font-size: 0.88rem; color: var(--text-muted); min-height: 32px; }
    .pv-read:empty { display: none; }
    .pv-chip { background: none; border: 0; font: inherit; color: var(--text); cursor: pointer; padding: 4px 2px; }
    .pv-chip:hover { text-decoration: line-through; text-decoration-color: var(--text-muted); }
    .pv-sep { color: var(--text-muted); opacity: .6; padding: 0 2px; }
    .pv-count { margin-left: 8px; }
    .pv-clear { background: none; border: 0; font: inherit; color: var(--text-muted); cursor: pointer; margin-left: 12px; text-decoration: underline; text-underline-offset: 3px; }
    .pv-clear:hover { color: var(--text); }
    #visibleCount { display: none !important; }
    .art-piece.pv-in { animation: pvIn 380ms ease-out both; }
    @keyframes pvIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: none; } }
    @media (prefers-reduced-motion: reduce) { .art-piece.pv-in { animation: none; } }
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

    .pv-done { gap: 16px; }
    .pv-done span { margin-right: auto; }
    .pv-dot { box-shadow: inset 0 0 0 1px rgba(255,255,255,.22); }
    .pv-pig { display: flex; flex-wrap: wrap; gap: 8px; align-items: center; }
    .pv-sw { width: 28px; height: 28px; border-radius: 14px; border: 1px solid rgba(255,255,255,.18); cursor: pointer; padding: 0; }
    .pv-sw:hover { transform: scale(1.12); }
    .pv-sw.is-on { outline: 2px solid var(--text); outline-offset: 2px; }
    .pv-any { display: inline-flex; align-items: center; gap: 8px; margin-left: 4px; font-size: 0.82rem; color: var(--text-muted); cursor: pointer; }
    .pv-any input { width: 30px; height: 30px; border: 0; padding: 0; background: none; cursor: pointer; }
    #lbPalette .swatch-dot { cursor: pointer; }
    .pv-like:empty { display: none; }
    .pv-like { margin: 22px 0 6px; }
    .pv-like-h { font-size: 0.68rem; letter-spacing: 0.16em; text-transform: uppercase; color: var(--text-muted); margin-bottom: 10px; }
    .pv-like-row { display: flex; flex-wrap: wrap; gap: 8px; }
    .pv-like-row button { border: 0; padding: 0; background: none; cursor: pointer; height: 72px; opacity: .85; }
    .pv-like-row button:hover { opacity: 1; }
    .pv-like-row img { height: 72px; width: auto; max-width: 140px; object-fit: cover; display: block; }
    .pv-like-word { height: 72px; max-width: 140px; padding: 8px !important; font-size: 0.72rem; line-height: 1.25; color: var(--text-muted); border: 1px solid var(--border) !important; text-align: left; font-style: italic; overflow: hidden; }
    .pv-like-lines { display: flex; flex-direction: column; gap: 10px; }
    .pv-like-lines button { background: none; border: 0; padding: 0; text-align: left; cursor: pointer; color: var(--text); font: inherit; font-size: 0.92rem; line-height: 1.4; }
    .pv-like-lines button em { display: block; font-style: normal; font-size: 0.74rem; color: var(--text-muted); margin-top: 2px; }
    .pv-like-lines button:hover span { text-decoration: underline; text-underline-offset: 3px; text-decoration-color: var(--text-muted); }
    @media (max-width: 760px) {
      header { padding: 10px 14px 0 !important; }
      .nav-primary { flex-wrap: wrap !important; row-gap: 8px !important; }
      .header-search-cluster, .header-search-cluster:focus-within,
      header.is-scrolled .header-search-cluster { order: 3 !important; flex: 1 1 100% !important; max-width: none !important; }
      .pv-toolrow { margin-top: 4px; }
      .pv-show { gap: 14px; margin-right: 4px; }
      .pv-room { display: none; }
      .wall-controls-bar { flex-wrap: wrap; }
      .pv-read { flex: 1 1 100%; margin-bottom: 6px; }
      .pv-rule { display: none; }
      .pv-pop { left: 0 !important; right: 0; width: auto; }
    }
  </style>
'''
s = sub_once('</head>', CSS + '</head>', s, '</head>')

# 6. Script, last in <body>.
JS = '\n<script id="pvScript">\n' + (ROOT / 'tools' / 'preview_tools.js').read_text() + '</script>\n'
idx = s.rfind('</body>')
s = s[:idx] + JS + s[idx:]

(ROOT / 'preview.html').write_text(s)
print('preview.html written', len(s))
