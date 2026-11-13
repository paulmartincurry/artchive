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
   - **Must-haves only:** a work people will expect to find, with no usable translation, may stay as a one-or-two-line quote from the standard translation, credited to translator and book (`audit: quoted`). No longer passage. Keep this list short.
   - **Steer toward what we can use.** When adding or featuring work, favour authors and pieces with public-domain or openly offered texts. If an author's famous piece is locked up, look for another piece by them that isn't. Don't announce it; just curate that way.
5. **Don't force balance.** Tag a piece for what it is. Fix thin shelves by adding pieces, not by re-labelling.

## Design principles

- Minimal, dark, quiet. Show the work, hide the UI. Less is more everywhere.
- One big search bar. Search returns the works themselves, not an organising layer.
- Captions off by default on the Wall; title on hover.
- Maker tools (stencil, duotone, loupe, export) stay, but out of the way.

## How it's built

- `index.html` — the whole app (CSS + JS inline). Edit in place; never regenerate.
- `data/works.js` — the library: 500 artworks + 446 writing pieces, one JSON array.
- Writing pieces carry `shelf` (Love, God, Earth, Death, War, Art), `emotionShort` (mood), `audit` (verified / loose / modern-translation / unconfirmed / attribution / quoted) and `auditNote`.
- Re-sourced pieces also carry `translator` (shown in the reader's credit line), `license` (only when the text is not public domain) and a `sourceUrl` pointing at the edition the text was taken from; `auditNote` names the edition.
- Sourcing from the work sandbox: Project Gutenberg, archive.org and poetryintranslation.com can be fetched directly; Wikisource refuses. Archive.org scans are OCR, so check them against a second scan and say in `auditNote` when errors were corrected by eye.
- Reading Room: a book is one shelf in one mood. Titles are in `RR_BOOK_TITLES` in `index.html`. A mood with fewer than four pieces on a shelf joins the nearest mood's book on that shelf (`RR_NEAREST`); the pieces keep their own tags. There are no catch-all books.
- Artwork images: 372 come from Wikimedia Commons. `imageUrl` is the 960px thumbnail and `highResUrl` the original file (some originals are hundreds of MB, so never put an original in `imageUrl`). All 372 files were confirmed to exist on 12 Nov 2026 via the Commons API from Paul's browser; the sandbox itself cannot reach Wikimedia. 60 images narrower than 960px use the original.
- Artworks no longer carry a stored `quote`. The lightbox can still pair an artwork with a line from the writing library on click (`matchCanonicalVerse`), which draws on audited pieces.
- Search: an exact phrase in a title, artist, pull quote or full text always outranks loose word matches.
- The app de-duplicates on title + artist with anything in parentheses stripped, so two pieces by one author need titles that differ outside the brackets.
- `AUDIT.md` and `audit.csv` — record of the November 2026 audit of the writing.

## Before pushing

Load the page in a headless browser, switch through every view, open a book and page through it, run a search, and confirm there are no script errors and the Reading Room count matches the number of writing pieces in `data/works.js` (446 as of 12 Nov 2026).

## Next up

1. Finish the last 16 `loose` texts (listed in AUDIT.md). Likely sources: Haft Paikar (Wilson, 1924), Tukaram (Fraser and Marathe), Tirukkural (Pope), the German Classics series for Hölderlin and Droste, Blackwell's Some Spanish-American Poets for Agustini, Chamberlain's Japanese Poetry for Shiki, the Blunts' Seven Golden Odes for ʿAntara, and any 1928 printing for Larsen's Quicksand. Then look again at the "Cut, wanted back" list in AUDIT.md (Ghalib, Hagakure, Kleist, Sōseki, Ibn Khaldun, Lautréamont): a short verified quote each would restore them. The loose-text pass on 12 Nov 2026 re-sourced 101, cut 70 and left 16. Walsh's per-poem translator credits (Silva, Rosalía de Castro, Mistral) and the Martí translator still need confirming. The 33 `modern-translation` pieces are closed out (12 Nov 2026, see AUDIT.md): 25 re-sourced, 3 kept as short credited quotes, 5 cut. Good replacements for the cuts would be other work by Akka Mahadevi, Jarry or a Zen death poem, if a usable text turns up. Kline's and Wyllie's texts are free for non-commercial use only, so revisit them if the site ever makes money.
2. The public test, continued. First pass on 12 Nov 2026 added 21 famous writings (see AUDIT.md for what is still missing). **Art is the gap:** half of the 72 most-searched artworks are absent (Mona Lisa, Starry Night, Birth of Venus, Night Watch…). They could not be added because the sandbox cannot reach Wikimedia to verify image links. Options: add from museum open-access APIs (Met, Art Institute of Chicago, Cleveland, Rijksmuseum, National Gallery of Art) instead of Wikimedia, or have Paul confirm links in a browser.
   - **Rule 1 problem to settle (talking it through with Paul):** every older piece carries an AI-written `note`, and artworks an AI-written `craftSpec`. Paul wants every work to have context and is open to Claude writing it. Nothing has been changed yet. The unchecked paired quotes on artworks were removed on 12 Nov 2026.
3. Audit the 500 artworks the same way the writing was audited (titles, credits, dates).
4. Decide the fate of the parked views (Global Map, Weather) and the maker tools.
