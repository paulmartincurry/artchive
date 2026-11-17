# Brief 13: the big addition — one round, start to finish

You are adding artworks (or writing) to The Artchive, Paul's site of iconic art and short, powerful writing for creative people. Live: https://paulmartincurry.github.io/artchive/. Read `/home/claude/artchive/CLAUDE.md` (the brief) and `/home/claude/artchive/PLAN.md` (this session's plan) first. Your message names your round, your list, your batch name and your output folder.

**You do not edit the site.** Never touch `/home/claude/artchive/data/works.js`, `index.html` or `w/`. You produce records in a file; the coordinator merges, tests and pushes. The only files you may add inside the repo are images in `/home/claude/artchive/images/fairuse/` or `/home/claude/artchive/images/film/`, named `<batch>-<nn>.jpg`.

Paul is away and has said to go deep and keep going. Make the small calls yourself and write them in your report. A wrong fact, a fake quote, an image that does not show what its title says, or a work that feels AI-made are what would embarrass him most.

## The two tests

Every work must be something people search for or a strong deep cut, **and** on theme: drama, intensity, death, the visionary, raw material for makers. Famous first. Your list is the finish line; if a listed work is impossible (no usable image or record), substitute the nearest real work that passes both tests and say so. Do not go past the list size by more than a few.

## Do not duplicate

`/home/claude/big/existing.json` lists everything on the site (title, artist, a normalised `key` = letters and digits of title and artist with brackets removed, image URL, source URL). Check every candidate against it: same key, same image, or obviously the same object under another title (Saturn Devouring His Son vs. Saturn) means skip. Use the existing title spelling to check by eye too. Also do not duplicate inside your own batch (two impressions of one print: keep one).

## Where to get things (tested from this sandbox, 16 Nov 2026)

- Helpers: `/home/claude/artchive/tools/sources.py` (`nga()`, `rijks()`/`rijks_record()`, `loc()`/`loc_item()`, `si()`, `vam()`), `/home/claude/grow/harvest.py` (`met()`, `aic()`, `cma()`), `/home/claude/grow/rawfetch.py` (`raw(title)`, `clean(text)`: Wikipedia wikitext), `/home/claude/grow/trim.py` (`trim()`). Read them before using them.
- **Museum APIs first** (verified record, size, rights flag in one call): Met `https://collectionapi.metmuseum.org/public/collection/v1.1/search?q=...&hasImages=true` then `/public/collection/v1/objects/<id>` (`isPublicDomain`, `primaryImage`, use `web-large` path for imageUrl: replace `/original/` with `/web-large/`); Chicago `https://api.artic.edu/api/v1/artworks/search?q=...&fields=id,title,artist_display,date_display,medium_display,dimensions,is_public_domain,image_id,credit_line` (image `https://www.artic.edu/iiif/2/<image_id>/full/843,/0/default.jpg`; it gave a 500 once, retry); Cleveland `https://openaccess-api.clevelandart.org/api/artworks/?q=...&cc0=1&has_image=1` (use `images.web.url`); NGA via `nga()`; Rijksmuseum via `rijks()`; Smithsonian via `si()`; LoC via `loc()` (images on tile.loc.gov, never cdn.loc.gov).
- **Keys** live in `/root/.config/artchive/`: `si_key`, `bhl_key` (Biodiversity Heritage Library API v3: `https://www.biodiversitylibrary.org/api3?op=...&format=json&apikey=KEY`), `nypl_token` (header `Authorization: Token token="TOKEN"`, `https://api.repo.nypl.org/api/v2/items/search?q=...&publicDomainOnly=true`). Never print a key into a file inside the repo or into your report.
- **Wellcome**: `https://api.wellcomecollection.org/catalogue/v2/works?query=...&include=items` and IIIF images (CC BY 4.0 mostly: `photoCredit` "Wellcome Collection, CC BY 4.0"; check each item's licence).
- **NASA**: `https://images-api.nasa.gov/search?q=...&media_type=image`, then the asset manifest `https://images-api.nasa.gov/asset/<nasa_id>`. Public domain; NASA asks for credit, so `photoCredit` "NASA" (or the credit the record gives).
- **Wikimedia Commons** for works with no open museum API (Prado, Louvre, Uffizi, Tokyo National Museum, Paris Musées): category pages `https://commons.wikimedia.org/wiki/Category:<name>` list files (grep `href="/wiki/File:`); a file's licence and author come from `https://commons.wikimedia.org/w/index.php?title=File:<name>&action=raw`; the 960px thumb is `https://upload.wikimedia.org/wikipedia/commons/thumb/<a>/<ab>/<File>/960px-<File>` where `<a>/<ab>` are the first 1 and 2 hex chars of md5(filename with underscores); the original is the same path without `/thumb` and the size part. The API (`w/api.php`) works but returns 429 under load: one request a second at most, a descriptive User-Agent (`ArtchiveSourcing/1.0 (personal art site; github paulmartincurry/artchive)`), back off 30 seconds on 429. Other agents share this IP. Prefer Commons files that come from the holder (LACMA, Met, Rijks uploads, Google Art Project) over visitor photos; never a photo of a screen, a print in a shop, a reproduction or a frame with a wall around it unless the work is a building or a sculpture.
- **Wikipedia** for note sources: `raw(title)` from rawfetch (about one a second; wait on errors).
- **Wikidata SPARQL** `https://query.wikidata.org/sparql` works for bulk finding, but its dates and holders are wrong about one time in five: never take them unread.

## Picking by eye

Make contact sheets (PIL, about 200 px tiles with an index number and a short title) and **look at them with the Read tool**. Keep only images that show what the title names, are sharp enough, are the whole work (not a crop, unless the record says detail and you title it as a detail), are not hole-punched, watermarked, or photographed at an angle with a wall around a flat work. Look at the final choice for every work before you write its record.

## Rights tier (CLAUDE.md, "Rights: two tiers")

- `free`: public domain in the US (published before 1931; made by a US federal employee; a US work whose copyright was not renewed, with a named source that says so) or CC0 from the holder. Hotlink the holder's web-size image as `imageUrl` and a larger file as `highResUrl`.
- When the image's own licence asks for attribution (CC BY, CC BY-SA, KOGL, Wellcome, NASA credit), set `photoCredit` to "Name, Licence" exactly like "Carole Raddato, CC BY-SA 2.0". Read the author from the file page; never "unknown" if the page names someone.
- `look`: in copyright. `fairUse: true`, `rightsTier: 'look'`, `rights: 'In copyright. Look and learn: shown for study, not for download.'`, `highResUrl: ''`. Download one screen-size image (at most 1,000 px on the long side; English Wikipedia's non-free file for the work is the usual source, at `https://upload.wikimedia.org/wikipedia/en/<a>/<ab>/<File>`) into `/home/claude/artchive/images/fairuse/<batch>-<nn>.jpg` (re-save as JPEG quality 85, long side ≤1000), set `imageUrl` to `images/fairuse/<batch>-<nn>.jpg`, and `imageW`/`imageH` to its pixel size. A look-tier work must have a note.

## The record (one JSON object per work)

```
title, artist, dateLabel, yearNum (int), eraBucket, graphicForm, craftSpec "", region, medium, dimensions,
subjectShort, emotionShort, macroRegion, macroMedium, imageUrl, highResUrl, sourceUrl, museum,
note, noteSource, noteRev 4, palette, colorFamily, iconicScore, isPantheon true, searchTags, isSeed true,
audit "verified", auditNote, grow, rightsTier, [photoCredit], [rights], [fairUse, imageW, imageH], [noHolder true], [labelOnly true], itemType "art", pid
```

- Allowed tag values: `/home/claude/big/vocab.json`. eraBucket from the year: <1400 Ancient & Medieval, <1650 1400–1650, <1800 1650–1800, ≤1920 1800–1920, else 1920–Now. macroMedium: prints → Print & Woodcut; photographs and film → Photograph & Film; drawings, manuscripts, scrolls, books → Scroll & Paper; maps, diagrams, natural-history plates, textiles → Diagram, Cyanotype & Textile; paintings → Painting; sculpture/objects/buildings → Sculpture & Metalwork; posters, lettering, ephemera → Letterform, Score & Ephemera.
- `title`: the holder's title, in the English the holder uses, title case. Long captions may be shortened, but put the holder's full title in `auditNote` ("Shortened from the holder's title: …"). Never invent a title. Prints from a series: "The Sleep of Reason Produces Monsters (Los Caprichos, plate 43)".
- `artist`: the holder's maker in normal order ("Francisco de Goya" style; match the spelling already on the site in existing.json for artists we have, e.g. "Francisco de Goya y Lucientes" if that is how the site has him). Anonymous: "Maker unknown".
- `dateLabel` as the holder states it, tidied (1799, c. 1820–23, 1863, published 1863). `dimensions` as the holder gives it, short ("21.6 × 15.2 cm"); leave out if unknown.
- `museum`: the real holder ("Museo del Prado, Madrid"). Buildings, sites, book plates with no identified copy: `museum: ''`, `noHolder: true`.
- `sourceUrl`: the holder's object page (or the Commons file page if there is no holder page). `noteSource`: the main page the note's facts came from.
- `iconicScore`: 260 for works people search for by name, 230 for strong works, 200 for deep cuts.
- `searchTags`: the words people type (the work's popular name, series, the artist's short name, subject words), lower case, space separated.
- `grow`: your round's tag (given in your message).
- `auditNote`: one or two sentences: where the title, maker, date, medium and image came from, the holder's id/accession, the licence, and the date fetched (16 Nov 2026 or 17 Nov 2026).
- `pid`: `<batch>-<nn>` (two or three digits), the same id you use for the source file and the note.

## Notes (the curator's line)

Follow `/home/claude/out/BRIEF10.md` exactly: the voice, nothing from memory, `save_line(batch, pid, note, evidence, derived)`. Build each source file yourself at `/home/claude/grow/wp/<pid>.txt`: first line `SOURCE: <url>`, then the holder's record as `Field: value` lines (everything the API gives: title, maker, dates, medium, dimensions, credit line, accession, description, provenance, exhibition history, inscriptions), then `SOURCE2: <wikipedia url>` and the cleaned Wikipedia text on the work and/or the maker (use `trim()` to keep it under about 15,000 characters, but keep the sections about the work's making and history). Then read the file and write the note. For a series (twelve Disasters of War plates, sixteen Carceri), the series article supplies facts: tell different facts on each card (plate numbers, when the series was printed, how many impressions, what happened to the plates, the artist's age), and use label only when you run out rather than repeating. One card in a series can carry the series' big facts; the others carry their own.

After notes, put each note into its record from `/home/claude/out/line_<batch>.json` (`note` field). Works with no note: `labelOnly: true`, `note: ''` (not allowed for look tier: drop those instead).

## Palette and colour

```python
import sys,os; sys.path.insert(0,'/home/claude/grow'); import pal
os.chdir('/home/claude/grow')
R = pal.do([{'pid':..., 'imageUrl':..., 'local': '/abs/path/if/downloaded.jpg'}], 'pid', 'pal_<batch>.json')
```
Copy `palette` and `colorFamily` into each record. Chicago and Smithsonian image servers refuse headless browsers but plain HTTP with a UA works for palettes.

## Output

In your folder (`/home/claude/big/<round>/`):
- `records.json`: the list of records, ready to merge.
- `sheet*.jpg`: the contact sheets of what you kept.
- `report.md`: counts; the list as asked against what you delivered; substitutions and why; works dropped and why; any place a source disagreed with a title, maker or date; label-only works; anything the coordinator must check by eye in Paul's browser (Chicago or Smithsonian images you could not see).

Then reply in a few lines: how many records, where the file is, and the three most important things the coordinator should know. Do not paste records or notes.
