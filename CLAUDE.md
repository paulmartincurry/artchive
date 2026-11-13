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

1. **Real texts only.** Nothing presented as the work is written by an AI. No paraphrases, no retellings, no invented titles. AI chooses and tags; it never authors the work.
   - **The one exception is the context note** (`note`). Claude writes these. Paul credits that elsewhere on the site, so no per-note label. A note is a museum card with a bit more history or a bit about the maker, in a plain, friendly voice. Paul's instruction: keep it factual, don't get cute or clever. Facts only, no interpretation or mood-setting, no punchlines or asides to the reader, two to four short sentences, nothing that can't be checked against the museum record or the cited edition. If a fact is shaky, leave it out. Never quote the work or anyone else in a note.
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
- Artworks carry `audit` and `auditNote` too (13 Nov 2026). `verified` means the title, maker and date were checked against the museum's own record (the 129 Met, Chicago, Cleveland and SMK works, which also had their medium checked) or against the Wikipedia and Wikidata records for that work. `unconfirmed` means the source is a general article or nothing was checked; the lightbox says "details not yet verified" on those. `museum` is the real holder or empty: never a placeholder. Where a medium could not be checked it was moved to `mediumUnchecked` and `medium` left empty or filled from Wikidata. Anonymous works are credited "Maker unknown", not to an invented workshop. The site no longer claims CC0 or public domain for anything.
- Wikipedia and Wikidata rate-limit the sandbox hard. Use the batch APIs (`action=query` with 20 titles, `wbgetentities` with 45 ids), a descriptive User-Agent, and pauses.
- Artworks no longer carry a stored `quote`. The lightbox can still pair an artwork with a line from the writing library on click (`matchCanonicalVerse`), which draws on audited pieces.
- Search: an exact phrase in a title, artist, pull quote or full text always outranks loose word matches.
- The app de-duplicates on title + artist with anything in parentheses stripped, so two pieces by one author need titles that differ outside the brackets.
- `AUDIT.md` and `audit.csv` — record of the November 2026 audit of the writing.

## Before pushing

Load the page in a headless browser, switch through every view, open a book and page through it, run a search, and confirm there are no script errors and the Reading Room count matches the number of writing pieces in `data/works.js` (446 as of 12 Nov 2026).

## Next up

1. Finish the last 16 `loose` texts (listed in AUDIT.md). Likely sources: Haft Paikar (Wilson, 1924), Tukaram (Fraser and Marathe), Tirukkural (Pope), the German Classics series for Hölderlin and Droste, Blackwell's Some Spanish-American Poets for Agustini, Chamberlain's Japanese Poetry for Shiki, the Blunts' Seven Golden Odes for ʿAntara, and any 1928 printing for Larsen's Quicksand. Then look again at the "Cut, wanted back" list in AUDIT.md (Ghalib, Hagakure, Kleist, Sōseki, Ibn Khaldun, Lautréamont): a short verified quote each would restore them. The loose-text pass on 12 Nov 2026 re-sourced 101, cut 70 and left 16. Walsh's per-poem translator credits (Silva, Rosalía de Castro, Mistral) and the Martí translator still need confirming. The 33 `modern-translation` pieces are closed out (12 Nov 2026, see AUDIT.md): 25 re-sourced, 3 kept as short credited quotes, 5 cut. Good replacements for the cuts would be other work by Akka Mahadevi, Jarry or a Zen death poem, if a usable text turns up. Kline's and Wyllie's texts are free for non-commercial use only, so revisit them if the site ever makes money.
2. The public test, continued. First pass on 12 Nov 2026 added 21 famous writings (see AUDIT.md for what is still missing). **Art is the gap:** half of the 72 most-searched artworks are absent (Mona Lisa, Starry Night, Birth of Venus, Night Watch…). They could not be added because the sandbox cannot reach Wikimedia to verify image links. Options: add from museum open-access APIs (Met, Art Institute of Chicago, Cleveland, Rijksmuseum, National Gallery of Art) instead of Wikimedia, or have Paul confirm links in a browser.
   - **Notes rewrite: done (13 Nov 2026).** All 946 pieces have a Claude-written `note` to the standard in rule 1 (`noteRev: 2` on every record; a new piece without it has no checked note). They were written from well-documented facts, not looked up one by one, so treat a note as a first pass and correct it when a record is audited. Paul has floated a second, longer layer behind a click: not built. If it is built, only for pieces with a real story, and each one checked against a source. The AI-written `craftSpec` is no longer shown (the Craft / Process row was removed from the specs drawer); the field is still in the data and still searched, and should be dropped or replaced with the museum's medium line during the art audit. Things the notes pass turned up are listed in AUDIT.md under "Context notes".
3. Art audit, in progress (13 Nov 2026): 494 of 500 records verified for identity, maker and date. Six are `unconfirmed`: VAULT-117 (Bonheur, Sheep), 168 (Ouyang Xiu letter, authenticity doubted on its own file page), 174 (celadon vase, a visitor's photo with no object record), 208 (Harunobu, scanned from a postcard, title unknown), 430 and 485 (file records not yet read). The Wikimedia Commons file record for each image (`action=query&prop=imageinfo&iiprop=extmetadata`) names the object and its holder and is the fastest way to check a record. Notes: the dates in 48 of the Wikipedia-sourced notes were checked against the full article text and none was wrong; 59 more such pages and all the museum-sourced and writing notes still need the same pass (script and cache in the work sandbox are not kept, so redo it). Still to do: resolve the six; check the medium on the 312 Wikipedia-sourced works (208 are blank, the rest are from Wikidata); fill `museum` on the roughly 100 objects that have a holder but no value yet (buildings and sites have none); re-read every note against its source, since so far only the notes that the museum records contradicted were corrected; `craftSpec` is still in the data, unshown.
4. Decide the fate of the parked views (Global Map, Weather) and the maker tools.
