# The Artchive — project brief

Paul's site: iconic art and short, powerful writing for creative people.
Live at https://paulmartincurry.github.io/artchive/ (GitHub Pages, deploys from `main`).

## What it is

- **Audience:** starts as Paul's own tool, then creative friends, then any creative person. Also a portfolio piece. Build for strangers.
- **The job:** spark an idea and hand over raw material. Get in, get hit by something, go make work. Lingering is a bonus, not the goal.
- **Art leads.** It is a visual experience first. Writing takes less room but gets equal care. Art-and-text pairings are a future experiment, not the spine.
- **Point of view:** drama, intensity, life, poetry. A personal canon with a bias, not a neutral survey.
- **Famous first, deep cuts inside.** The works people will search for must be there, or it fails the public test. Over time, lean further into the overlooked.
- **Scale:** tens of thousands eventually, behind a curated front of house.

## Rules for content

1. **Real texts only.** Nothing on the page is written by an AI. No paraphrases, no retellings, no invented titles. AI chooses and tags; it never authors.
2. **Text comes from sources**, not memory: Project Gutenberg, Wikisource, PoetryDB, museum collection APIs. Record where each piece came from.
3. **The pull quote is the unit.** Every writing piece has a short, strong excerpt (`hook`) that works on its own. For many visitors that is the whole point. The longer passage (`fullText`) is optional depth, one tap away. Never lose the short form, and the quote must be the source's exact words.
4. **Public-domain wording first; openly offered translations second.** Old poem, modern translator = not ours to use, unless the translator has published it for free reuse (A. S. Kline's poetryintranslation.com, Project Gutenberg's licensed texts, open-access scholarly editions). Prefer a named, checkable translator over an anonymous one. Always credit the translator and record the terms in `license`. Claude does not translate. Cut if no usable text exists.
5. **Don't force balance.** Tag a piece for what it is. Fix thin shelves by adding pieces, not by re-labelling.

## Design principles

- Minimal, dark, quiet. Show the work, hide the UI. Less is more everywhere.
- One big search bar. Search returns the works themselves, not an organising layer.
- Captions off by default on the Wall; title on hover.
- Maker tools (stencil, duotone, loupe, export) stay, but out of the way.

## How it's built

- `index.html` — the whole app (CSS + JS inline). Edit in place; never regenerate.
- `data/works.js` — the library: 500 artworks + 500 writing pieces, one JSON array.
- Writing pieces carry `shelf` (Love, God, Earth, Death, War, Art), `emotionShort` (mood), `audit` (verified / loose / modern-translation / unconfirmed / attribution) and `auditNote`.
- Re-sourced pieces also carry `translator` (shown in the reader's credit line), `license` (only when the text is not public domain) and a `sourceUrl` pointing at the edition the text was taken from; `auditNote` names the edition.
- Sourcing from the work sandbox: Project Gutenberg, archive.org and poetryintranslation.com can be fetched directly; Wikisource refuses. Archive.org scans are OCR, so check them against a second scan.
- Reading Room: a book is one shelf in one mood. Titles are in `RR_BOOK_TITLES` in `index.html`.
- The app de-duplicates on title + artist with anything in parentheses stripped, so two pieces by one author need titles that differ outside the brackets.
- `AUDIT.md` and `audit.csv` — record of the November 2026 audit of the writing.

## Before pushing

Load the page in a headless browser, switch through every view, open a book and page through it, run a search, and confirm there are no script errors and the Reading Room still counts 500 pieces.

## Next up

1. Replace the 187 `loose` texts with sourced wording (rule 4); cut what can't be sourced. Keep or re-pick a strong pull quote for each. Of the original 33 `modern-translation` pieces, 24 were re-sourced on 12 Nov 2026 (see AUDIT.md). The 9 left (LIT-020 Musashi, 132 Kozan Ichikyo, 149 Thunder Perfect Mind, 286 and 457 Akka Mahadevi, 375 Jarry, 426 Lu Xun, 462 Shaka, 498 Andrade) have no public-domain or openly offered English that could be found and are waiting on Paul: cut, or keep looking. Kline's and Wyllie's texts are free for non-commercial use only, so revisit them if the site ever makes money.
2. The public test: list the ~100 works people will search for first, find what's missing, add it.
3. Audit the 500 artworks the same way the writing was audited (titles, credits, dates).
4. Decide the fate of the parked views (Global Map, Weather) and the maker tools.
