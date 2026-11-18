# The big addition — session plan

Written 16 Nov 2026, approved in outline by Paul ("all of those sound good"). Not started. Run it as one long session, round by round, pushing after each round so the site is never half-done.

## The point

Every round has to pass two tests at once: **people search for it** and **it is on theme** (drama, intensity, death, the visionary, raw material to steal). Famous first inside each round, deep cuts after. Pull from the collections we have barely touched. On 16 Nov, 460 of the 1,112 artworks came from four holders (Cleveland, Chicago, the Met, Cooper Hewitt) and Europe was 56% of the art.

**Size:** about 560 artworks and 60 writing pieces across nine rounds. That takes the site from 1,864 to about 2,480. Each round has a fixed list and a finish line. When a round's list is done, stop it, even if more good material turns up; park extras in `out/parked.json`.

## Before starting (round 0)

1. **Read** CLAUDE.md, this file, AUDIT.md's last two sections.
2. **Access check.** Tested from the sandbox on 16 Nov:
   - Work: Wellcome catalogue API, NASA Images API, David Rumsey (LUNA search), Library of Congress, Rijksmuseum Linked Art, Commons file pages (`index.php?action=raw`), Met v1.1 search.
   - Need a free key: Biodiversity Heritage Library (401), NYPL Digital Collections (401), Paris Musées (503 without key). BHL and NYPL keys are in hand (see Paul's answers below); Paris Musées is not, stored like the Smithsonian key in `~/.config/artchive/` and never committed. If he would rather not sign up: BHL books are mirrored on archive.org (use `advancedsearch.php`, collection `biodiversity`), and most Paris Musées and NYPL highlights are on Commons.
   - Getty: the search URL tried was wrong (404). Use its SPARQL endpoint `https://data.getty.edu/museum/collection/sparql` or the Commons copies of Getty open-content images.
   - Chicago's API gave a 500 once; retry before assuming it is down.
3. **Tools to add to `tools/sources.py`:** `wellcome()`, `nasa()`, `rumsey()`, `commons_cat(category)` (lists files in a Commons category with licence and author, using the raw file page), `ia_scan(id)` (archive.org page images for plates). Same record shape as the others.
4. **Dedupe list.** Before each round, build the set of existing title + artist (brackets stripped, as the app does) and the set of image URLs, and refuse any candidate that matches.
5. **Write `out/BRIEF13.md`** for note-writing agents: the voice (CLAUDE.md rule 1), `save_line`, the source files, the banned words, the per-round notes below. Agents get one round's list each, at most 20 running.

## The pipeline (every round, every work)

1. Candidates from the holder's API or Commons category, saved to `~/grow/r<N>/cands.json`.
2. **Contact sheet, picked by eye.** The image must show what the title names. No killed negatives, no ads, no medical or specimen material, no sideshow.
3. Record from the holder: title, maker, date, medium, **size**, holder, credit, rights. Holder's title kept; long titles shortened with the full one in `auditNote`.
4. Licence read for every image. Set `rightsTier`. `photoCredit` whenever the licence asks for attribution.
5. Source file per work in `~/grow/wp/` (holder record plus Wikipedia on the work and the maker), notes through `save_line`, batch named for the round.
6. Tags (subject, emotion, era, region, macro medium, `grow`), palette via `pal.py`, `searchTags` with the names people type.
7. Merge, `build_pages.py`, pre-push tests, push, check a sample live in Paul's Chrome (Chicago, Smithsonian and Wikimedia images only load there).
8. AUDIT.md section per round: what came in, what was dropped and why.

## Rounds

### 1. The dark masters, properly — about 110, free tier
Where: Rijksmuseum, National Gallery of Art, Prado and Louvre via Commons (PD-Art), British Museum via Commons, Met for prints we lack.
Already have: Goya 11, Rembrandt 8, Caravaggio 9, Bosch 5, Bruegel 9, Piranesi 3, Fuseli 1, Géricault 1, Holbein 2, Gentileschi 3, Böcklin 3, Ensor 2, Doré 1.
Must-haves people search for:
- Goya: the Black Paintings set (Saturn is likely in; add the rest), Caprichos (The Sleep of Reason and 10 more), Disasters of War (12), The Third of May if missing.
- Rembrandt: etchings (Three Crosses, Hundred Guilder Print, self-portrait etchings), The Anatomy Lesson, Jewish Bride.
- Bosch: Garden of Earthly Delights panels and details, The Haywain, Seven Deadly Sins, Ship of Fools.
- Caravaggio: Judith Beheading Holofernes, David with the Head of Goliath, Medusa, Calling of St Matthew (check which we have).
- Fuseli: The Nightmare and its versions. Géricault: Raft of the Medusa, severed heads studies. Piranesi: the Carceri (all 16 plates are the finish line).
- Gentileschi's Judith Slaying Holofernes, Holbein's Ambassadors and Dead Christ, Grünewald's Isenheim Altarpiece, Doré's Inferno and Paradise Lost plates (10), Callot's Miseries of War, Mantegna's Lamentation, Bocklin's Isle of the Dead versions.
Note: Prado and Louvre have no open API; take Commons PD-Art files and name the holder from the holder's own page.

### 2. Night, magic and the occult — about 60, free tier
Where: Wellcome (CC BY, so `photoCredit` "Wellcome Collection, CC BY 4.0"), Getty, Paris Musées, Commons, Rijksmuseum, LoC.
Must-haves: the Codex Gigas devil page, Splendor Solis, Ripley Scroll, Mutus Liber, Robert Fludd's cosmic diagrams, the Visconti-Sforza and Marseille tarot (key cards), Dürer's Melencolia I if missing, Goya's Witches' Sabbath, Hans Baldung Grien's witches, Kircher's diagrams, the Compendium Rarissimum demons, Redon and Moreau from the Paris city museums, Hilma af Klint's paintings for the Temple (PD).
**Wellcome filter is strict:** anatomy, surgery, disease, specimens and medical photographs stay out (Paul's line). Alchemy, astrology, magic, divination and religion are in.

### 3. Nature as raw material — about 70, free tier
Where: Biodiversity Heritage Library (key or archive.org mirror), NYPL, Smithsonian Libraries via `si()`, Commons.
Must-haves: Haeckel's Art Forms in Nature (the best 20 plates is the finish line), Audubon's Birds of America (15), Maria Sibylla Merian's Surinam plates (add to our 4), Blossfeldt's plant photographs (PD in the US if published before 1931: Urformen der Kunst, 1928), Seba's Thesaurus, Besler's Hortus Eystettensis, Anna Atkins's cyanotypes (check what we have), Japanese bird-and-flower prints, shell and insect plates.
Note: one plate equals one work; title it with the book and plate number from the scan, never a made-up caption.

### 4. Maps, stars and diagrams — about 50, free tier
Where: David Rumsey (licence per item; most are CC BY-NC-SA, so check, and prefer Commons or LoC copies that are PD), LoC Geography and Map, NASA Images API (public domain, credit NASA), Commons.
Must-haves: Carta Marina sea monsters, Cellarius's Harmonia Macrocosmica plates, the Hereford Mappa Mundi, Ortelius, Burritt's star atlas, Apollo photographs (Earthrise is in; add the Blue Marble, Aldrin's bootprint, Buzz on the Moon, the Pale Blue Dot), Hubble deep fields, Mars rover panoramas, early solar eclipse photographs.

### 5. Japan beyond Hokusai — about 70, free tier
Where: Met, Rijksmuseum, Chicago, Cleveland (prints we have not used), Tokyo National Museum and Commons, MFA Boston via Commons.
Already have: Kuniyoshi 3, Yoshitoshi 1, Hiroshige 3, Kyōsai 0.
Must-haves: Yoshitoshi's One Hundred Aspects of the Moon (15) and his New Forms of Thirty-Six Ghosts (8), Kuniyoshi's Takiyasha the Witch and the Skeleton Spectre, cats, warrior prints (10), Kawanabe Kyōsai's demons and skeletons (8), Hiroshige's One Hundred Famous Views of Edo highlights, Hokusai's ghost prints from One Hundred Ghost Stories, Tsukioka's Kabuki ghosts, Shin-hanga before 1931 (Hasui, Yoshida), katagami we lack, Japanese ghost scrolls (Maruyama Ōkyo's yūrei).

### 6. Look and learn: the modern canon — about 80, look tier
Where: English Wikipedia's non-free files and museum web images, hosted in `images/fairuse/`, up to about 1,000 px, `fairUse: true`, a `rights` line, a sourced note on every one, no download.
Painters (one to three each, the works people search for): Hopper (more), Francis Bacon, Basquiat (more), Haring, Kusama, Hockney, Warhol (more), Rothko (more), de Kooning, Kahlo (more), Dalí (more), Magritte (more), O'Keeffe after 1930, Lucian Freud, Picasso after 1930, Matisse cut-outs, Jean Dubuffet, Louise Bourgeois's Maman, Kerry James Marshall, Jacob Lawrence, Faith Ringgold, Romare Bearden, Leonora Carrington, Remedios Varo.
Photographers: Cartier-Bresson, Capa, Weegee, Arbus, Avedon, Gordon Parks after the FSA, Robert Frank, Vivian Maier, Eggleston, Mapplethorpe flowers, Nan Goldin (check fit), Sebastião Salgado, Steve McCurry's Afghan Girl, Eddie Adams, Nick Ut. The war and news photographs are on theme and searched; each needs a note and the look-and-learn line.
Cap: no cap per artist (Paul), but the list is the finish line.

### 7. Film after 1931 — about 45 stills, mixed tier
Free tier first: films in the US public domain because they were never renewed or never registered: Night of the Living Dead (1968), Carnival of Souls (1962), Detour (1945), His Girl Friday (1940), Charade (1963), The Little Shop of Horrors (1960), Plan 9 from Outer Space, Reefer Madness, The Last Man on Earth (1964), Dementia 13. Grab frames from archive.org copies made from prints (never Blu-ray rips), contact sheet, pick by eye, same title format as the silent stills. Check each film's PD status against a named source (the film's Wikipedia article states it).
Look tier: Citizen Kane, Psycho, Vertigo, Rear Window, 2001, Seven Samurai, Rashomon, Persona, The Seventh Seal, La Dolce Vita, 8½, Breathless, Taxi Driver, The Shining, Apocalypse Now, Blade Runner, In the Mood for Love. Use only the stills English Wikipedia carries under fair use, or the studio's own publicity stills, never frames from bootleg uploads. One or two per film.

### 8. Writing — about 60 pieces
Where: Gutenberg, archive.org, LoC sheet music, Standard Ebooks. Same edition method as before (`save_new`, letters-only match, start and end phrases).
Already have: Lincoln 3, Douglass 2, Chief Joseph 2, Kabir 2, Mirabai 2, Eckhart 1, Julian 1, Marinetti 1, Blake 8.
New:
- Manifestos before 1931: Tzara's Dada manifesto, Breton's first Surrealist manifesto (1924; original French, plus an English translation only if one is public domain or openly offered), Vorticist BLAST, Mayakovsky's Slap in the Face of Public Taste, Malevich, Loos's Ornament and Crime.
- Blues and spirituals in published sheet music before 1929: W. C. Handy (St. Louis Blues, Memphis Blues), Ma Rainey and Bessie Smith titles where a published score exists, spirituals from the Fisk and Hampton collections. A lyric goes in only from a scan of the published score or songbook.
- Speeches: Sojourner Truth from the 1851 Marius Robinson report (not the later dialect version), Emmeline Pankhurst's Freedom or Death, Patrick Henry, Pericles' funeral oration (Jowett), Socrates' Apology.
- Notebooks and letters of artists: Delacroix's journal, Leonardo's notebooks (more), Gauguin's Noa Noa, Rilke's Letters to a Young Poet (Herter Norton is in copyright, so one line only; full text needs a PD translation).
- Mystics: Rumi beyond what we have, Hafiz, Kabir via Tagore, Hildegard, Meister Eckhart, the Cloud of Unknowing, Teresa of Ávila.

### 9. Size on the label — UI, small
Paul asked for size. Most new records carry dimensions; Met, Chicago, Cleveland, NGA and LoC records have it too. Add `dimensions` to the lightbox label line and to the static pages, backfill from the holders' APIs for the museum works already on the site, and leave it blank where no holder states it. Do this at the start of the session so every round fills it.

## Order and checkpoints

0 setup and 9 (size) → 1 dark masters → 5 Japan → 6 look-and-learn modern → 7 film → 2 occult → 3 nature → 4 maps and stars → 8 writing.
Push after each round. After rounds 1, 6 and 7, send Paul a contact sheet of what went in before moving on.

## Red lines (unchanged)

- Real texts only; notes from fetched sources only, through `save_line`.
- No advertising, no medical or specimen material, no sideshow material.
- Look tier: screen-size images, no full-size link, a note on every one, take down on request.
- Writing in copyright: one prose sentence under fifteen words, confirmed in a scan; never a line of a poem in copyright.
- Ask Paul before cutting anything that is already on the site.

## Paul's answers (16 Nov 2026)

1. Keys: BHL and NYPL keys received and working (stored in `~/.config/artchive/bhl_key` and `nypl_token`, never committed; if a new session lacks them, ask Paul again). Paris Musées: no key yet, so route around it through Commons.
2. War and news photographs (Adams, Ut, Capa): in.
3. Kills or must-haves: none named yet. Ask once more at the start of the session.

## Round 10: the world and the gaps (17 Nov 2026)

Paul: "yep go for it, and make your own calls on anything outstanding." Art is 56% European and writing from Africa, Oceania and Indigenous sources is 23 pieces, so most of this round goes there. Same pipeline (tools/BRIEF13.md for art, out/BRIEF6.md plus save_line notes for writing). New `grow` values: world, illus, avant.

| Round | What | Size | Tier |
|---|---|---|---|
| n1 | Persian, Mughal, Ottoman and Islamic painting and calligraphy: Shahnama of Shah Tahmasp, Hamzanama, Khamsa, Jahangir and Shah Jahan album leaves, Siyah Qalam, Wonders of Creation, the tughra, Blue Qur'an, Kufic leaves | ~60 | free |
| n2 | South and Southeast Asia and Tibet: Chola bronzes, Kali and Durga, Rajput and Pahari painting, Kota hunts, thangkas (Mahakala, Chitipati, the Wheel of Life), Khmer and Javanese sculpture | ~55 | free |
| n3 | China and Korea: ink landscapes (Guo Xi, Ma Yuan, Wang Ximeng, Along the River), Bada Shanren, Shitao, Chen Rong's Nine Dragons, the Ten Kings of Hell, calligraphy, Jeong Seon, Kim Hong-do, minhwa tigers | ~60 | free |
| n4 | Africa, Oceania and the Indigenous Americas: Benin, Ife, Fang, Kongo, Yoruba, Ethiopian manuscripts, Lalibela, Asmat bisj poles, Kū, Rapa Nui, Māori carving, codices (Borgia, Mendoza, Florentine, Zouche-Nuttall), Maya lintels, Moche, Northwest Coast masks, ledger drawings | ~65 | free |
| n5 | Golden-age illustration and early comics: Rackham, Dulac, Nielsen, Harry Clarke, John Bauer, Bilibin, Sime, more Beardsley, Mucha's decorative panels, Little Nemo, Rarebit Fiend, Krazy Kat, Kin-der-Kids | ~55 | free (pre-1931) |
| n6 | Avant-garde, Weimar and early photography, plus the four missing famous works: Rodchenko, Lissitzky, Klutsis, Stenberg, Dix's Der Krieg, Grosz, Beckmann, Kollwitz-era prints, Riis, Strand, Atget, Sander, Blossfeldt, Man Ray; Rodin's The Kiss, Chartres, the Alhambra, the Sagrada Família | ~55 | mostly free |
| n7 | Silent film, second reel: Greed, The Wind, Pandora's Box, The Unknown, The Last Laugh, Napoléon, Spies, Woman in the Moon, The Crowd, Destiny, The Phantom Carriage, The Man Who Laughs, Steamboat Bill Jr., The Cameraman, Gertie the Dinosaur, Strike, Earth, Ballet Mécanique, Salomé | ~30 frames | free |
| w10a | Writing from Africa, Oceania and the Indigenous Americas in pre-1931 translations: Brinton's Nahuatl poems, Navajo Night Chant, Densmore's Chippewa songs, Ghost Dance songs, Chief Joseph, the Kumulipo (Liliʻuokalani), Grey's Polynesian Mythology, Kebra Nagast, Book of the Dead, Hymn to the Aten, Ollantay | ~30 | free |
| w10b | East Asia, Greek tragedy and the blues: Waley (170 Chinese Poems, Genji, the Pillow Book), Pound's Cathay, Sansom's Essays in Idleness, Hōjōki, Giles's Zhuangzi, Legge's Laozi, Murray's Euripides and Aeschylus, Jebb's Sophocles, Handy's Blues: An Anthology (1926) | ~40 | free |

Calls made (Paul said to make them):
- **The blues: in.** Lyrics printed before 1929 are public domain. A lyric goes on the site only when its words are in the OCR text of a pre-1929 printing and each line is confirmed by eye against the page image; the kit still checks every line against the OCR source file, with corrections recorded in `auditNote`.
- **I Know Moon-Rise stays as Higginson printed it** (rule 4: no standard-spelling edition exists, so keep the public-domain text and say so). Recorded in AUDIT.md.
- **VAULT-116 and VAULT-061 are cut.** Their holder withdrew the images, no free copy exists, and both artists are on the site through other works.
- **Commons-only sizes stay held back** (a spot check found errors).
- **No images of the Prophet Muhammad, no human remains, no objects a community restricts as secret or sacred.** Respect, and Paul's line on specimen material.
- **Film posters are in** when they advertise a film (the same footing as the Federal Theatre posters); posters that sell a product stay out.
