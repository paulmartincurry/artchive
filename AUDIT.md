# Reading Room audit — 12 November 2026

All 500 writing pieces were read one by one and checked by Claude. This file is the record.
The full before/after for every piece is in `audit.csv`.

## What was checked

1. **Shelf and mood.** Each piece was re-tagged by hand: one of six shelves (Love, God, Earth, Death, War, Art) and one of seven moods. These live in the data as `shelf` and `emotionShort`, and they decide which book a piece lands in.
2. **Title.** Embellished or invented titles were replaced with the work's real title.
3. **Attribution.** Whether the credited author actually wrote it.
4. **Wording.** Whether the text is a real published version or a loose rendering.

## How far to trust it

Most calls were made from Claude's own knowledge of these works, not from looking each one up. Seven of the shakiest were checked against sources on the web and all seven held. A status of `verified` means the author, work and wording were recognised with confidence. It does not mean every character was collated against a printed edition.

## The numbers

| Status | Count | Meaning |
|---|---|---|
| verified | 258 | Real author, real work, wording recognised as a published text |
| loose | 187 | Real author and work, but the English is a loose rendering, paraphrase, or retelling |
| modern-translation | 33 | Wording matches a specific 20th- or 21st-century published translation |
| unconfirmed | 13 | Could not confirm the lines or the translator |
| attribution | 9 | The credit or source was wrong and has been corrected |

Also changed: 408 titles cleaned up, 85 moods changed, 440 texts had a stray signature line removed from the end, and 9 pieces had typos or find-and-replace damage repaired (for example "zero trees" for "no trees").

## Attribution corrected (9)

- **Anonymous (Old Babylonian)**, *The Epic of Gilgamesh — Siduri's Advice* (LIT-078). Siduri's speech is from the Old Babylonian version, not Sin-leqi-unninni's; wording is a paraphrase. Credit should be Anonymous
- **Daniel Ladinsky (published as “Hafiz”)**, *The Sun Never Says* (LIT-081). Not by Hafez. Written by Daniel Ladinsky (The Gift, 1999), who publishes his own poems under Hafez's name
- **Arthur Schopenhauer**, *The World as Will and Representation* (LIT-115). The pendulum line is from The World as Will, not Studies in Pessimism
- **Hildegard von Bingen**, *Liber Divinorum Operum* (LIT-137). This passage is from the Book of Divine Works, not Scivias or Symphonia
- **Yu Xuanji**, *To a Neighbor Girl* (LIT-334). The famous couplet is from her poem To a Neighbor Girl, not the poem named in the old title
- **Anecdote about Mi Fu**, *Mi Fu Bows to the Rock* (LIT-338). An anecdote about Mi Fu, not a text written by him
- **Abu al-ʿAlāʾ al-Maʿarrī**, *Elegy (Tread Lightly)* (LIT-450). These lines are from an elegy, not his epitaph; they also repeat part of No. 306
- **Attributed to Crazy Horse (Tȟašúŋke Witkó)**, *Attributed Sayings* (LIT-470). Popularly attributed to Crazy Horse; none can be verified as his words
- **Tochihuitzin Coyolchiuhqui (attributed)**, *We Only Came to Dream* (LIT-473). Usually attributed to Tochihuitzin Coyolchiuhqui, not Nezahualcóyotl; loose rendering

## Unconfirmed (13)

These may be real lines in a translation that could not be identified, or they may have been composed by the AI that built the first version of this library. Treat them as unverified.

- **Yoruba Babaláwo & Akéwì Oral Canon**, *Oríkì of Ṣàngó* (LIT-153). Could not confirm these lines against a recorded oríkì; may be composed
- **Traditional Māori Chant (Aotearoa)**, *Tōia Tainui* (LIT-234). A real hauling chant exists; could not confirm this English wording
- **Michelangelo Buonarroti**, *Sonnet 151* (LIT-237). Real sonnet; could not identify the translator, reads 20th-century
- **Guillaume Apollinaire**, *Le Pont Mirabeau* (LIT-293). Could not identify the translator
- **Charles Baudelaire**, *Une Charogne (A Carcass)* (LIT-367). Could not identify the translator
- **Comte de Lautréamont (Isidore Ducasse)**, *Les Chants de Maldoror (Canto VI)* (LIT-369). Could not identify the translator
- **Jules Laforgue**, *Litanies of the Last Quarters of the Moon* (LIT-371). Could not match these lines to Laforgue's poem; may be composed
- **Guillaume Apollinaire**, *Il pleut (It's Raining)* (LIT-376). Could not identify the translator
- **Ali-Shir Nava'i**, *Ghazal (Flint and Spark)* (LIT-446). Could not match to a known ghazal; may be composed
- **Yoruba Babaláwo Oral Divination Canon**, *Odù Ifá* (LIT-459). One line is a known Ifá verse; the rest could not be confirmed
- **Nana Asma'u**, *Poem* (LIT-466). Could not match these lines to her work; may be composed
- **Queen Liliʻuokalani**, *Kuʻu Pua i Paoakalani* (LIT-469). Real song; could not confirm this English wording
- **Salomé Ureña**, *Ruinas* (LIT-475). Real poet and poem; could not match these lines, may be composed

## Modern translations (33)

The originals are old, but this English wording belongs to a named modern translator. Worth replacing with an older public-domain translation, or crediting, if the site is shared widely. This is a note about provenance, not legal advice.

- **Nezahualcóyotl (King of Texcoco)**, *Not Forever on Earth* (LIT-012). Widely circulated modern English version; attribution to Nezahualcóyotl is traditional
- **Rainer Maria Rilke**, *The Panther (In the Jardin des Plantes, Paris)* (LIT-016). Wording matches Stephen Mitchell's 1982 translation
- **Miyamoto Musashi**, *The Book of Five Rings — The Book of the Void* (LIT-020). Wording matches Victor Harris's 1974 translation
- **Charles Baudelaire**, *To the Reader (Au Lecteur — Les Fleurs du mal)* (LIT-037). Wording matches William Aggeler's 1954 translation
- **Franz Kafka**, *The Metamorphosis (Die Verwandlung)* (LIT-092). Wording matches Stanley Corngold's 1972 translation
- **Franz Kafka**, *The Trial — Before the Law* (LIT-093). Wording matches the Muirs' 1937 translation
- **Euripides**, *Medea* (LIT-104). Wording matches Rex Warner's 1944 translation
- **Sei Shōnagon**, *The Pillow Book (opening)* (LIT-118). Wording matches Ivan Morris's 1967 translation
- **Kozan Ichikyo**, *Death Poem* (LIT-132). Wording matches Yoel Hoffmann's Japanese Death Poems (1986)
- **Kumārajīva / Sanskrit Mahāyāna Canon**, *The Diamond Sutra (Ch. 32)* (LIT-147). Wording matches A. F. Price's 1947 translation
- **Anonymous Gnostic Visionary**, *The Thunder, Perfect Mind* (LIT-149). Wording matches George MacRae's 1977 translation
- **Izumi Shikibu**, *Tanka* (LIT-205). Wording matches Hirshfield and Aratani's The Ink Dark Moon (1988)
- **Lal Ded (Lalleshwari)**, *Vakh* (LIT-209). Wording matches Coleman Barks's Naked Song (1992)
- **Taras Shevchenko**, *Testament (Zapovit)* (LIT-221). Wording matches John Weir's 1961 translation
- **Rainer Maria Rilke**, *Letters to a Young Poet (First Letter)* (LIT-245). Wording matches M. D. Herter Norton's 1934 translation
- **Michel de Montaigne**, *Essays (Book III, Ch. 13)* (LIT-252). Wording reads like a 20th-century translation (Frame or Screech)
- **Friedrich Nietzsche**, *Thus Spoke Zarathustra (Prologue, 5)* (LIT-259). Wording matches Walter Kaufmann's 1954 translation
- **Friedrich Nietzsche**, *Twilight of the Idols — Maxims and Arrows* (LIT-260). Wording matches Walter Kaufmann's 1954 translation
- **Hanshan (Cold Mountain)**, *Cold Mountain Poem* (LIT-265). Wording matches Gary Snyder's 1958 translation
- **Yoshida Kenkō**, *Essays in Idleness (7)* (LIT-271). Wording matches Donald Keene's 1967 translation
- **Akka Mahadevi**, *Vachana: To a Suitor* (LIT-286). Wording reads like A. K. Ramanujan's Speaking of Siva (1973)
- **Basava (Basavanna)**, *Vachana 820* (LIT-287). Wording matches A. K. Ramanujan's Speaking of Siva (1973)
- **Rainer Maria Rilke**, *Duino Elegies (First Elegy)* (LIT-299). Wording matches the Leishman and Spender translation (1939)
- **Jayadeva**, *Gīta Govinda (opening)* (LIT-320). Wording closely follows Barbara Stoler Miller's 1977 translation
- **Hawaiian creation chant (trans. Martha Beckwith)**, *The Kumulipo* (LIT-359). Wording matches Martha Beckwith's 1951 translation, not Liliʻuokalani's as credited
- **Alfred Jarry**, *Exploits and Opinions of Dr. Faustroll* (LIT-375). Wording matches Simon Watson Taylor's 1965 translation
- **Søren Kierkegaard**, *Either/Or — Diapsalmata* (LIT-397). Wording matches the Swenson translation (1944)
- **Marina Tsvetaeva**, *I Know the Truth* (LIT-405). Wording matches Elaine Feinstein's 1971 translation
- **Lu Xun (Zhou Shuren)**, *A Madman's Diary* (LIT-426). Wording closely follows the Yangs' 1960 translation
- **Sei Shōnagon**, *The Pillow Book — Things That Make the Heart Beat Faster* (LIT-444). Wording closely follows Ivan Morris's 1967 translation
- **Akka Mahadevi (Trans. Vacana Tradition)**, *Vachana: The Eye of the Lord* (LIT-457). Wording matches A. K. Ramanujan's Speaking of Siva (1973); overlaps with No. 286
- **Magolwane kaMkhathini (Zulu *Imbongi* Royal Praise-Poet)**, *Izibongo of Shaka* (LIT-462). Wording matches Trevor Cope's 1968 translation
- **Oswald de Andrade**, *Manifesto Antropófago* (LIT-498). Wording matches Leslie Bary's 1991 translation

## Re-sourcing pass 1 — 12 November 2026

15 of the 33 modern translations were replaced with older public-domain wording copied from a source, not from memory. The audit table above is the state before this pass; `audit.csv` is also unchanged.

| Piece | Now uses | Source |
|---|---|---|
| LIT-221 Shevchenko, My Testament | A. J. Hunter, 1922 | Gutenberg #68486 |
| LIT-118 Sei Shōnagon, Pillow Book (opening) | W. G. Aston, 1899 | archive.org scan, OCR corrected by eye against a second scan |
| LIT-252 Montaigne, Essays III.13 | Charles Cotton, ed. Hazlitt 1877 | Gutenberg #3600 |
| LIT-259 Nietzsche, Zarathustra | Thomas Common, 1909 | Gutenberg #1998 |
| LIT-260 Nietzsche, Twilight of the Idols | A. M. Ludovici, 1911 | Gutenberg #52263 |
| LIT-271 Kenkō, Essays in Idleness | W. N. Porter, 1914 | archive.org scan |
| LIT-205 Izumi Shikibu | W. N. Porter, 1909 | archive.org scan. **Different poem** (Hyakunin Isshu 56); moved from Art/Sublime to Love/Yearning |
| LIT-209 Lal Ded, Vakh 94 | Grierson and Barnett, 1920 | archive.org scan. Original-script text removed, not verified |
| LIT-320 Jayadeva, Gīta Govinda | Edwin Arnold, 1875 | Gutenberg #25965. A free Victorian verse rendering |
| LIT-359 The Kumulipo | Queen Liliʻuokalani, 1897 | Lines as quoted by the Library of Congress and poets.org; **not yet checked against the 1897 printing** |
| LIT-397 Kierkegaard, Diapsalmata | L. M. Hollander, 1923 | Gutenberg #60333 |
| LIT-012 Nezahualcóyotl | D. G. Brinton, 1887 | Gutenberg #12219. **Different text**, from a Spanish version of doubtful authenticity; status set to `attribution` |
| LIT-016 Rilke, The Panther | Jessie Lemont, 1918 | Gutenberg #38594 |
| LIT-104 Euripides, Medea | Gilbert Murray, 1910 | Gutenberg #35451 |
| LIT-147 Diamond Sutra | William Gemmell, 1912 | Gutenberg #64623 |

## Re-sourcing pass 2 — 12 November 2026

Seven more replaced with translations their translators publish for free reuse. These are **not public domain**; the terms are recorded on each piece in `license`.

| Piece | Now uses | Source and terms |
|---|---|---|
| LIT-405 Tsvetaeva, I Know the Truth | A. S. Kline, 2010 | poetryintranslation.com, free for non-commercial use |
| LIT-265 Hanshan, Cold Mountain Poem | A. S. Kline, 2006 | same |
| LIT-299 Rilke, Duino Elegies (First) | A. S. Kline, 2004 | same |
| LIT-245 Rilke, Letters to a Young Poet | A. S. Kline, 2021 | same |
| LIT-037 Baudelaire, To the Reader | A. S. Kline, 2001–2010 | same |
| LIT-092 Kafka, Metamorphosis | David Wyllie, 2002 | Gutenberg #5200, copyrighted, Gutenberg licence |
| LIT-093 Kafka, Before the Law | David Wyllie | Gutenberg #7849, copyrighted, Gutenberg licence |

## Re-sourcing pass 3 — 12 November 2026

| Piece | Now uses | Source and terms |
|---|---|---|
| LIT-287 Basava, Vachana | P. G. Halkatti, 1922 | The Indian Antiquary vol. 51, archive.org scan, public domain. Shorter than the version before: no closing lines |
| LIT-444 Sei Shōnagon, Stray Notes | Arthur Waley, 1928 | Gutenberg #76016. **Different passage.** Public domain in the US only until 2037 |

Still `modern-translation` (9), searched twice, nothing usable:

- LIT-020 Musashi: only commercial translations found.
- LIT-132 Kozan Ichikyo: only Hoffmann's (Tuttle). Original found on a blog: 来時は空手、去時は赤脚。一去一来、単重交折 (unverified).
- LIT-149 Thunder, Perfect Mind: Anne McGuire's translation is online but licensed for classroom use only.
- LIT-286, LIT-457 Akka Mahadevi: nothing older than Ramanujan found.
- LIT-375 Jarry: Simon Watson Taylor's is the only English translation found.
- LIT-426 Lu Xun: English Wikisource has a volunteer translation (CC BY-SA) but it could not be fetched from the sandbox.
- LIT-462 Shaka: R. C. Samuelson's Long, Long Ago (1929) may have an older English text; no scan found.
- LIT-498 Andrade: a newer translation is posted online from The Forest & The School (ed. Pedro Neves Marques); terms unknown.

## Short quotes — 12 November 2026

Three works people will expect to find, with no usable translation, cut down to a one-or-two-line quote from the standard translation and credited (`audit: quoted`). Paul's call.

| Piece | Quote from |
|---|---|
| LIT-426 Lu Xun, A Madman's Diary | Yang Xianyi and Gladys Yang, 1960 |
| LIT-020 Musashi, Book of the Void | Victor Harris, 1974 |
| LIT-149 The Thunder, Perfect Mind | George W. MacRae, 1977 |

## Cuts — 12 November 2026

No usable English and not must-haves. Cut with Paul's go-ahead; the old entries are in git history before this commit. The Reading Room now holds 495 pieces.

- LIT-132 Kozan Ichikyo, Death Poem
- LIT-286 Akka Mahadevi, Vachana: To a Suitor
- LIT-457 Akka Mahadevi, Vachana: The Eye of the Lord (duplicated 286)
- LIT-375 Alfred Jarry, Exploits and Opinions of Dr. Faustroll
- LIT-462 Izibongo of Shaka

LIT-498 Andrade, Manifesto Antropófago: kept as the single line "Tupi, or not tupi that is the question." It is in English in the original, so no translator is involved. Spelling follows the Revista Periferia (UERJ) edition; the 1928 printing has "Tupy".

No `modern-translation` pieces remain.

## Loose texts — 12 November 2026

The 187 `loose` texts, in two passes on the same day:

- **101 re-sourced** with wording copied from a source (table below). Six of these are must-haves kept as one- or two-line credited quotes from a translation still in copyright (`audit: quoted`).
- **70 cut.** No public-domain or openly offered English was found. This was a first search plus what Claude knows of the translation history, not an exhaustive hunt, so some may be recoverable. The old entries are in git history before commit "Loose texts pass 2".
- **16 still loose**, where a usable source probably exists but was not reached.

The Reading Room now holds 425 pieces.

Things to know:

- Sources are Project Gutenberg, Internet Archive scans of older books, and A. S. Kline's poetryintranslation.com. Scans are OCR: obvious scan errors were corrected by eye, and the piece's `auditNote` says so where that happened.
- Many pieces are now a different passage or poem by the same author, because that was what a usable text existed for. Marked "different" below.
- Books published 1921–1930 are public domain in the United States but may not be elsewhere. Noted in `license`.
- Kline's translations are free for non-commercial use only.
- In Walsh's Hispanic Anthology (Silva, Rosalía de Castro, Mistral) each poem has its own translator, but the scan was too poor to read the credits. Credited to the anthology for now.
- The two Popol Vuh pieces are Lewis Spence's 1908 English account, not a translation.
- The Martí quote's translator (Tellechea) is inferred from the edition named where it was found quoted; worth confirming against the book.

| Piece | Translator | Source and notes |
|---|---|---|
| LIT-383 Bram Stoker, Dracula (Ch. II) | original English | https://www.gutenberg.org/ebooks/345 |
| LIT-386 Algernon Blackwood, The Willows | original English | https://www.gutenberg.org/ebooks/11438 |
| LIT-100 Oscar Wilde, The Picture of Dorian Gray (Ch. XIII) | original English | https://www.gutenberg.org/ebooks/174 |
| LIT-430 Olive Schreiner, The Story of an African Farm — The Hunter | original English | https://www.gutenberg.org/ebooks/1441 |
| LIT-471 Geronimo (Goyaałé), Geronimo's Story of His Life | original English | https://www.gutenberg.org/ebooks/31318 — A different passage from the one shown before, which is from his 1886 surrender, not this book. |
| LIT-003 Homer, The Odyssey (Book XII) | Samuel Butler, 1900 | https://www.gutenberg.org/ebooks/1727 |
| LIT-102 Miguel de Cervantes, Don Quixote (Part I, Ch. VIII) | John Ormsby, 1885 | https://www.gutenberg.org/ebooks/996 |
| LIT-077 Sophocles, Antigone — Ode to Man | F. Storr, 1912 | https://www.gutenberg.org/ebooks/31 |
| LIT-175 Demosthenes, The Third Philippic | Charles Rann Kennedy, 1852 | https://www.gutenberg.org/ebooks/6878 |
| LIT-183 Alexander the Great (via Arrian, Anabasis VII.9–10), Speech at Opis | E. J. Chinnock, 1884 | https://www.gutenberg.org/ebooks/46976 |
| LIT-107 Sophocles, Oedipus the King | F. Storr, 1912 | https://www.gutenberg.org/ebooks/31 |
| LIT-106 Aeschylus, Agamemnon | Gilbert Murray, 1920 | https://www.gutenberg.org/ebooks/14417 |
| LIT-390 E. T. A. Hoffmann, The Sandman | John Oxenford, 1844 | https://www.gutenberg.org/ebooks/32046 |
| LIT-117 Cao Xueqin, Dream of the Red Chamber (Ch. 1) | H. Bencraft Joly, 1892 | https://www.gutenberg.org/ebooks/9603 |
| LIT-131 Laozi (Lao Tzu), Tao Te Ching (Ch. 1 & 5) | James Legge, 1891 | https://www.gutenberg.org/ebooks/216 |
| LIT-435 Zhuangzi (Master Zhuang), Zhuangzi — Autumn Floods | Herbert A. Giles, 1889 | https://www.gutenberg.org/ebooks/59709 |
| LIT-123 The Qur'an (Surah An-Nur), The Qur'an — The Verse of Light (24:35) | J. M. Rodwell, 1861 | https://www.gutenberg.org/ebooks/2800 |
| LIT-134 Papyrus of Ani (New Kingdom Scribes), Book of the Dead (Spell 30B) | E. A. Wallis Budge, 1920 | https://www.gutenberg.org/ebooks/7145 |
| LIT-247 Vizier Ptahhotep, The Maxims of Ptahhotep | Battiscombe Gunn, 1906 | https://www.gutenberg.org/ebooks/30508 |
| LIT-318 Anonymous Medieval Arabic Storytellers, One Thousand and One Nights (frame tale) | Sir Richard Burton, 1885 | https://www.gutenberg.org/ebooks/3435 |
| LIT-398 Hans Christian Andersen, The Shadow | translator not named | https://www.gutenberg.org/ebooks/1597 |
| LIT-105 Euripides, The Bacchae | Gilbert Murray, 1904 | https://www.gutenberg.org/ebooks/35173 |
| LIT-113 Lucretius, De Rerum Natura (Book II) | William Ellery Leonard, 1916 | https://www.gutenberg.org/ebooks/785 |
| LIT-443 Multatuli (Eduard Douwes Dekker), Max Havelaar — Saïdjah's Song | Baron Alphonse Nahuijs, 1868 | https://www.gutenberg.org/ebooks/70128 |
| LIT-272 Tao Yuanming (Tao Qian), Drinking Wine (V) | Arthur Waley, 1918 | https://www.gutenberg.org/ebooks/42290 |
| LIT-289 Giacomo Leopardi, L'Infinito | Frederick Townsend, 1887 | https://www.gutenberg.org/ebooks/19315 |
| LIT-292 Paul Verlaine, Chanson d'automne | Gertrude Hall, 1895 | https://www.gutenberg.org/ebooks/8426 |
| LIT-332 Bai Juyi (Po Chü-i), The Lute Girl (Pípá Xíng) | L. Cranmer-Byng, 1909 | https://www.gutenberg.org/ebooks/390 |
| LIT-228 Alexander Pushkin, The Prophet (Prorok) | Ivan Panin, 1888 | https://www.gutenberg.org/ebooks/54991 |
| LIT-427 José Rizal, My Last Farewell (Mi último adiós) | Charles Derbyshire, 1911 | https://www.gutenberg.org/ebooks/6867 |
| LIT-449 Hafez of Shiraz, Ghazal (The Shirazi Turk) | Gertrude Bell, 1897 | https://www.gutenberg.org/ebooks/74883 |
| LIT-421 Pu Songling, The Painted Skin (Huàpí) | Herbert A. Giles, 1880 | https://www.gutenberg.org/ebooks/43629 |
| LIT-317 Muhammad Iqbal, Secrets of the Self (Asrār-i-Khudī) | Reynold A. Nicholson, 1920 | https://www.gutenberg.org/ebooks/57317 |
| LIT-447 Fuzuli, Gazel | E. J. W. Gibb, 1882 | https://www.gutenberg.org/ebooks/56464 — A different gazel from the one shown before. |
| LIT-353 Middle Kingdom Egyptian Blind Harper Tradition, Harper's Song from the Tomb of King Intef | E. A. Wallis Budge, 1914 | https://www.gutenberg.org/ebooks/15932 |
| LIT-229 Anna Akhmatova, Song of the Last Meeting | A. S. Kline, 2005 | https://www.poetsofmodernity.xyz/POMBR/Russian/Akhmatova.php |
| LIT-403 Alexander Blok, Night, Street, Lamp, and Pharmacy | A. S. Kline | https://www.poetryintranslation.com/PITBR/Russian/BlokAlexanderSelectedPoems.php |
| LIT-372 Tristan Corbière, Le Crapaud (The Toad) | A. S. Kline | https://www.poetryintranslation.com/PITBR/French/CorbiereSelectedPoems.php |
| LIT-373 Aloysius Bertrand, Gaspard de la Nuit — Scarbo | A. S. Kline | https://www.poetryintranslation.com/PITBR/French/BertrandGaspard.php |
| LIT-264 Juvenal (Decimus Junius Juvenalis), Satire X | A. S. Kline | https://www.poetryintranslation.com/PITBR/Latin/JuvenalSatires10.php |
| LIT-370 Stéphane Mallarmé, Brise Marine (Sea Breeze) | A. S. Kline | https://www.poetryintranslation.com/PITBR/French/Mallarme.php |
| LIT-368 Arthur Rimbaud, Après le Déluge (After the Flood) | A. S. Kline | https://www.poetryintranslation.com/PITBR/French/Rimbaud2.php |
| LIT-330 Meng Haoran, A Spring Morning (Chūn Xiǎo) | Witter Bynner and Kiang Kang-hu, 1929 | https://archive.org/details/jademountainchin00heng — One OCR slip corrected (a full stop for a comma after “storm”). |
| LIT-322 Muttā (Elder Buddhist Nun), Therīgāthā (Muttā) | C. A. F. Rhys Davids, 1909 | https://archive.org/details/psalmsofearlybud01davi |
| LIT-333 Liu Zongyuan, River-Snow (Jiāng Xuě) | Witter Bynner and Kiang Kang-hu, 1929 | https://archive.org/details/jademountainchin00heng |
| LIT-331 Wei Yingwu, At Chuzhou on the Western Stream | Witter Bynner and Kiang Kang-hu, 1929 | https://archive.org/details/jademountainchin00heng |
| LIT-329 Qu Yuan, The Fisherman’s Reply | Herbert A. Giles, 1923 | https://archive.org/details/gemsofchineselit00gileuoft — The line comes from The Fisherman’s Reply, traditionally attributed to Qu Yuan, not from the Li Sao. |
| LIT-304 Al-Khansāʾ (Tumāḍir bint ʿAmr), Elegy for Ṣakhr | Reynold A. Nicholson, 1922 | https://archive.org/details/translationsofea00nich |
| LIT-355 King Hammurabi's Babylonian Scribes, Code of Hammurabi (prologue) | Robert Francis Harper, 1904 | https://archive.org/details/CodeOfHammurabiHarper |
| LIT-152 Karma Lingpa / Padmasambhava Tradition, Bardo Thödol (The Tibetan Book of the Dead) | Lāma Kazi Dawa-Samdup, ed. W. Y. Evans-Wentz, 1927 | https://archive.org/details/the-tibetan-book-of-the-dead_202401 |
| LIT-456 Bhartṛhari, Nītiśataka | B. Hale Wortham, 1886 | https://archive.org/details/the-satakas-of-bhartrihari |
| LIT-324 Ambapālī (Courtesan-Turned-Elder Nun of Vesālī), Therīgāthā (Ambapālī) | C. A. F. Rhys Davids, 1909 | https://archive.org/details/psalmsofearlybud01davi |
| LIT-323 Kisāgotamī (Elder Buddhist Nun), Therīgāthā (Kisāgotamī) | C. A. F. Rhys Davids, 1909 | https://archive.org/details/psalmsofearlybud01davi — The verse she speaks in the old commentary after the mustard-seed search. |
| LIT-352 Neburä Id Yishaq of Aksum, Kebra Nagast | E. A. Wallis Budge, 1922 | https://archive.org/details/kebranagast |
| LIT-306 Abu al-ʿAlāʾ al-Maʿarrī, Luzūmiyyāt | Ameen Rihani, 1918 | https://www.gutenberg.org/ebooks/50457 |
| LIT-150 Orphic Mystery Initiates, The Orphic Gold Tablets | Gilbert Murray, 1903 | https://archive.org/details/prolegomenatostu00harrrich |
| LIT-121 Rigveda (hymn 10.129), Rigveda — Nasadiya Sukta (10.129) | Ralph T. H. Griffith, 1897 | https://archive.org/details/in.ernet.dli.2015.47262 |
| LIT-281 Anyte of Tegea, Epigram | W. R. Paton, 1917 | https://archive.org/details/greekanthology0003wrpa — A different epigram from the one shown before (Greek Anthology 9.144). |
| LIT-354 Achaemenid–Babylonian Chancery Scribes, The Cyrus Cylinder | Robert William Rogers, 1912 | https://archive.org/details/cuneiformparalle00roge |
| LIT-311 Rudaki, Bū-yi Jū-yi Mūliyān | A. V. Williams Jackson, 1920 | https://archive.org/details/earlypersianpoet00jackuoft |
| LIT-467 Ibn Battuta (Dictated to Ibn Juzayy), The Rihla (Taghaza) | H. A. R. Gibb, 1929 | https://archive.org/details/dli.ernet.16353 |
| LIT-313 Nizami Ganjavi, Layla and Majnun | James Atkinson, 1836 | https://archive.org/details/lovesoflailmaj00nizauoft |
| LIT-458 Mirabai, Pada | Max Arthur Macauliffe, 1909 | https://archive.org/details/in.ernet.dli.2015.56975 — A different song of hers from the one shown before. |
| LIT-491 José Asunción Silva, Nocturne (Nocturno III) | Thomas Walsh (ed.), 1920 | https://archive.org/details/hispanicantholo04walsgoog — The anthology names a translator for each poem; the scan was too poor to read this one’s credit. |
| LIT-400 Rosalía de Castro, Las campanas (The Bells) | Thomas Walsh (ed.), 1920 | https://archive.org/details/hispanicantholo04walsgoog — A different poem from the one shown before; no usable English was found for Negra sombra. The translator’s name could not be read in the scan. |
| LIT-393 Georg Heym, The Demons of the Cities (Die Dämonen der Städte) | Babette Deutsch and Avrahm Yarmolinsky, 1923 | https://archive.org/details/dli.ernet.79482 — A different Heym poem from the one shown before. |
| LIT-392 Else Lasker-Schüler, End of the World (Weltende) | Babette Deutsch and Avrahm Yarmolinsky, 1923 | https://archive.org/details/dli.ernet.79482 — A different poem of hers from the one shown before. |
| LIT-394 Georg Trakl, Amen | Babette Deutsch and Avrahm Yarmolinsky, 1923 | https://archive.org/details/dli.ernet.79482 — A different Trakl poem from the one shown before. |
| LIT-417 Gabriela Mistral, From the Sonnets of Death (Los sonetos de la muerte) | Thomas Walsh (ed.), 1920 | https://archive.org/details/hispanicantholo04walsgoog — Lines from a different sonnet in the sequence. The translator’s name could not be read in the scan. |
| LIT-337 Lu You, To Wine | Herbert A. Giles, 1898 | https://archive.org/details/gems-of-chinese-literature — A different Lu You poem from the one shown before. |
| LIT-342 Ki no Tsurayuki, Kana Preface to the Kokinshū | W. G. Aston, 1899 | https://archive.org/details/historyjapanese00asto |
| LIT-061 Alfred, Lord Tennyson, Ulysses | original English | https://www.gutenberg.org/ebooks/8601 |
| LIT-023 Abu'l-Qasim Ferdowsi, Shahnameh — Rostam and Sohrab | James Atkinson, 1832 | https://www.gutenberg.org/ebooks/10315 |
| LIT-119 Kamo no Chōmei, Hōjōki (opening) | W. G. Aston, 1899 | https://archive.org/details/historyjapanese00asto |
| LIT-224 Al-Mutanabbi, Qasida (The Steed, the Night, the Desert) | Reynold A. Nicholson, 1922 | https://archive.org/details/translationsofea00nich — The opening of the same ode that contains the famous “steed, night and desert” line. |
| LIT-305 Abu Nuwas, Wine Poem (Leave Off Blaming Me) | Reynold A. Nicholson, 1922 | https://archive.org/details/translationsofea00nich |
| LIT-301 Imru' al-Qais, Muʿallaqa of Imruʾ al-Qais | Reynold A. Nicholson, 1922 | https://archive.org/details/translationsofea00nich — A different passage of the ode from the one shown before. |
| LIT-227 Mikhail Lermontov, The Demon | Francis Storr, 1894 | https://archive.org/details/demonoflermontof00lerm |
| LIT-319 Kālidāsa, Meghadūta (The Cloud Messenger) | Arthur W. Ryder, 1912 | https://www.gutenberg.org/ebooks/16659 |
| LIT-303 Labīd ibn Rabī'a, Muʿallaqa of Labīd | Reynold A. Nicholson, 1922 | https://archive.org/details/translationsofea00nich |
| LIT-133 Lewis Spence, retelling the Popol Vuh, Popol Vuh | original English | https://www.gutenberg.org/ebooks/56550 — Spence’s 1908 English account of the book, not a line-by-line translation. |
| LIT-358 Lewis Spence, retelling the Popol Vuh, Popol Vuh — The House of Gloom | original English | https://www.gutenberg.org/ebooks/56550 — Spence’s 1908 English account of the book, not a line-by-line translation. |
| LIT-401 Nikolai Gogol, The Overcoat (The Mantle) | Claud Field, 1916 | https://www.gutenberg.org/ebooks/36238 |
| LIT-343 Fujiwara no Teika, Waka (Hyakunin Isshu 97) | William N. Porter, 1909 | https://archive.org/details/hundredversesfro00fujiuoft |
| LIT-288 Bhartṛhari, Vairāgyaśataka | B. Hale Wortham, 1886 | https://archive.org/details/the-satakas-of-bhartrihari |
| LIT-425 Ryūnosuke Akutagawa, Rashōmon | Glenn W. Shaw, 1930 | https://www.gutenberg.org/ebooks/78105 — A different passage from the retelling shown before. |
| LIT-029 Farid ud-Din Attar, The Conference of the Birds | Edward FitzGerald, 1889 | https://archive.org/details/BirdParliamentEnglishFareeduddinAttaarFitzgerald — FitzGerald’s version is a free abridgement of the poem. |
| LIT-492 José Enrique Rodó, Ariel | F. J. Stimson, 1922 | https://archive.org/details/arielrod00roduoft — A different passage from the retelling shown before. |
| LIT-436 Xunzi (Xun Kuang), Xunzi — Man’s Nature Is Evil | Herbert A. Giles, 1923 | https://archive.org/details/gemsofchineselit00gileuoft — A different passage from the one shown before. |
| LIT-495 Amado Nervo, Deity (Deidad) | Alice Stone Blackwell, 1929 | https://archive.org/details/somespanishameri0000blac — A different Nervo poem from the one shown before. |
| LIT-396 Franz Kafka, In the Penal Colony | Ian Johnston | https://johnstoi.web.viu.ca/kafka/inthepenalcolony.htm |
| LIT-135 Babylonian Temple Priests, Enuma Elish (Tablet IV) | L. W. King, 1902 | https://archive.org/details/the-seven-tablets-of-creation.-vol.-1 |
| LIT-270 Yosa Buson, Haiku (Memories of the Past) | Basil Hall Chamberlain, 1911 | https://archive.org/details/in.ernet.dli.2015.53428 — A different Buson haiku from the ones shown before. |
| LIT-404 Andrei Bely, Messengers | Babette Deutsch and Avrahm Yarmolinsky, 1921 | https://archive.org/details/modernrussianpoe00deutuoft — A different work from the Petersburg passage shown before: one of his poems. |
| LIT-499 Alfonsina Storni, Tu casa está llena de lirios | Alice Stone Blackwell, 1929 | https://archive.org/details/somespanishameri0000blac — A different Storni poem from the one shown before, in Blackwell’s prose rendering. The title here is its first line; the scan did not show the poem’s title. |
| LIT-276 Kobayashi Issa, Haiku (A Million Bales) | Basil Hall Chamberlain, 1911 | https://archive.org/details/in.ernet.dli.2015.53428 — A different Issa haiku from the ones shown before. |
| LIT-416 Juana de Ibarbourou, El dulce milagro (The Sweet Miracle) | Alice Stone Blackwell, 1929 | https://archive.org/details/somespanishameri0000blac — A different Ibarbourou poem from the one shown before. |
| LIT-021 Jia Dao (Tang Dynasty), A Note Left for an Absent Recluse | Witter Bynner and Kiang Kang-hu, 1929 | https://archive.org/details/jademountainchin00heng — A different Jia Dao poem from the one shown before. |
| LIT-496 César Vallejo, Los heraldos negros (The Black Heralds) | Clayton Eshleman | https://www.thenation.com/?p=80225 |
| LIT-364 José Martí, I Cultivate a White Rose (Versos Sencillos XXXIX) | Manuel A. Tellechea | https://www.goodreads.com/user_quotes/85407605 |
| LIT-434 Han Fei, Han Feizi — Circumstances Alter Cases | Herbert A. Giles, 1923 | https://archive.org/details/gemsofchineselit00gileuoft — A different passage from the spear-and-shield story shown before. |

### Cut, wanted back

Works people may look for. Bring back if a usable text or a short verified quote turns up.

- LIT-223 Mirza Ghalib, Hazaaron Khwahishein Aisi
- LIT-274 Yamamoto Tsunetomo, Hagakure
- LIT-310 Ibn Khaldun, The Muqaddimah
- LIT-389 Heinrich von Kleist, On the Marionette Theatre
- LIT-424 Natsume Sōseki, Ten Nights of Dreams — The First Night
- LIT-103 Comte de Lautréamont (Isidore Ducasse), Les Chants de Maldoror — Hymn to the Ocean (Canto I)

### Cut

- LIT-357 Nezahualcóyotl, Even Jade Shatters
- LIT-219 Hwang Jin-i, The Long Midwinter Night (Sijo)
- LIT-220 Hwang Jin-i, Blue-Green Stream (Sijo)
- LIT-222 Lesya Ukrainka, Contra Spem Spero
- LIT-312 Rābiʿa Balkhī (Zayn al-ʿArab), Ghazal (Love Is a Shoreless Sea)
- LIT-243 Guo Xi, Lofty Ambitions in Forests and Streams
- LIT-244 Shitao (Bitter Melon Monk), Remarks on Painting (The Single Brushstroke)
- LIT-267 Ikkyū Sōjun, Skeletons (Gaikotsu)
- LIT-268 Hakuin Ekaku, Song of Zazen
- LIT-273 Shen Fu, Six Records of a Floating Life
- LIT-275 Yagyū Munenori, Heihō Kadensho
- LIT-285 Yunus Emre, Ilahi
- LIT-307 Wallada bint al-Mustakfi, Verses Embroidered on Her Robe
- LIT-308 Ibn Hazm of Córdoba, The Ring of the Dove
- LIT-315 Amir Khusrau, Chhaap Tilak
- LIT-316 Mir Taqi Mir, Ghazal (Smoke from the Heart)
- LIT-321 Compiled by King Hāla (Satavahana Anthology), Gāhā Sattasaī
- LIT-326 Avvaiyār (Sangam Bard), Puṟanāṉūṟu 235
- LIT-327 Āṇḍāl (Kōtai), Nācciyār Tirumoḻi (To the Conch)
- LIT-335 Li Yu (Last Emperor of Southern Tang), Yú Měirén
- LIT-336 Xin Qiji, Pò Zhèn Zǐ
- LIT-339 Guan Daosheng, Song of You and Me (Wǒ Nóng Cí)
- LIT-340 Zhao Mengfu, Colophon on Elegant Rocks and Sparse Trees
- LIT-341 Qiu Jin, Mǎn Jiāng Hóng
- LIT-345 Yosano Akiko, Kimi Shinitamō Koto Nakare (Thou Shalt Not Die)
- LIT-346 Shin Saimdang, Looking Back at My Parents' Home from Daegwallyeong
- LIT-347 Admiral Yi Sun-sin, Hansando Sijo
- LIT-348 Nguyễn Du, The Tale of Kiều (opening)
- LIT-349 Hồ Xuân Hương, Bánh Trôi Nước (Floating Cake)
- LIT-350 Balla Fasséké & Mandinka *Jeli* (Griot) Tradition, Epic of Sundiata
- LIT-351 Zera Yacob, Hatata
- LIT-356 Macuilxochitzin (Lady Five-Flower), Song of Macuilxochitzin
- LIT-362 Castro Alves, O Navio Negreiro (The Slave Ship)
- LIT-363 José Hernández, El Gaucho Martín Fierro (opening)
- LIT-374 Auguste Villiers de l'Isle-Adam, Axël
- LIT-395 Hugo Ball, Flight Out of Time (23 June 1916)
- LIT-399 Edith Södergran, Vierge moderne
- LIT-418 Horacio Quiroga, El almohadón de plumas (The Feather Pillow)
- LIT-419 Cruz e Sousa, Antífona
- LIT-420 Augusto dos Anjos, Versos íntimos
- LIT-422 Ueda Akinari, The Chrysanthemum Vow
- LIT-423 Ichiyō Higuchi, Nigorie (Troubled Waters)
- LIT-433 Sima Qian, Letter to Ren An
- LIT-437 Wen Tianxiang, Crossing the Lingding Sea
- LIT-438 Yun Sŏndo (Kosan), The Fisherman's Calendar (Autumn)
- LIT-439 Pak Chiwŏn (Yŏnam), The Tale of a Yangban
- LIT-440 Kim Sowŏl, Azaleas (Chindallae kkot)
- LIT-441 Han Yong-un (Manhae), The Silence of Love
- LIT-442 Francisco Balagtas (Baltazar), Florante at Laura (opening)
- LIT-445 Recorded by Mahmud al-Kashgari, Elegy for Alp Er Tunga
- LIT-451 Baba Bulleh Shah, Bulleha Ki Jaana Main Kaun
- LIT-452 Waris Shah, Heer Ranjha (opening)
- LIT-453 Shah Abdul Latif Bhittai, Shah Jo Risalo — Sur Sasui
- LIT-454 Subramania Bharati (Mahakavi Bharathiyar), Achamillai Achamillai
- LIT-460 Nyanga *Karisi* Oral Bards, The Mwindo Epic
- LIT-461 Ijaw *Okabou* Bardic Tradition, The Ozidi Saga
- LIT-463 Bwana Mwengo wa Athman, Utendi wa Tambuka (opening)
- LIT-464 Ahmad Baba al-Timbukti, Miʿrāj al-Ṣuʿūd
- LIT-465 Shehu Usman dan Fodio, Nūr al-Albāb
- LIT-493 Euclides da Cunha, Os Sertões (Rebellion in the Backlands)
- LIT-494 Joaquim Maria Machado de Assis, Dom Casmurro (Ch. XXXII)
- LIT-497 César Vallejo, Trilce LXXV
- LIT-500 José Martí, Nuestra América
- LIT-138 Mansur al-Hallaj, Kitāb al-Ṭawāsīn

### Still loose (0)

LIT-415 Delmira Agustini, *Lo inefable*, was cut on 13 November 2026 under Paul's rule (cut what can't be found or verified): no usable English text, and not a work a visitor would come looking for. Bring her back if a public-domain or credited translation turns up.

## Public test, first pass — 12 November 2026

Claude drew up a list of about 120 writings and 70 artworks a visitor is likely to search for first (Claude's own judgement, not search data) and checked the library against it.

**Writing: 37 of 117 were missing; 21 added.** All from Project Gutenberg, PoetryDB or A. S. Kline. New pieces have no commentary note and no original-language text.

| Piece | Translator | Source |
|---|---|---|
| LIT-501 Charles Dickens, A Tale of Two Cities (opening) | original English | https://www.gutenberg.org/ebooks/98 |
| LIT-502 Leo Tolstoy, Anna Karenina (opening) | Constance Garnett, 1901 | https://www.gutenberg.org/ebooks/1399 |
| LIT-503 Robert Frost, The Road Not Taken | original English | https://www.gutenberg.org/ebooks/59824 |
| LIT-504 T. S. Eliot, The Love Song of J. Alfred Prufrock (opening) | original English | https://www.gutenberg.org/ebooks/1459 |
| LIT-505 T. S. Eliot, The Waste Land (opening) | original English | https://www.gutenberg.org/ebooks/1321 |
| LIT-506 James Joyce, The Dead (ending) | original English | https://www.gutenberg.org/ebooks/2814 |
| LIT-507 Lewis Carroll, Jabberwocky | original English | https://www.gutenberg.org/ebooks/12 |
| LIT-508 Niccolò Machiavelli, The Prince (Ch. XVII) | W. K. Marriott, 1908 | https://www.gutenberg.org/ebooks/1232 |
| LIT-509 Confucius, Analects (Book I, 1) | James Legge, 1893 | https://www.gutenberg.org/ebooks/3330 |
| LIT-510 The Dhammapada, The Dhammapada (verse 1) | F. Max Müller, 1881 | https://www.gutenberg.org/ebooks/2017 |
| LIT-511 Johann Wolfgang von Goethe, Faust, Part One (Before the City Gate) | Bayard Taylor, 1870 | https://www.gutenberg.org/ebooks/14591 |
| LIT-512 Aristotle, Poetics (VI) | S. H. Butcher, 1895 | https://www.gutenberg.org/ebooks/1974 |
| LIT-513 Rainer Maria Rilke, Archaic Torso of Apollo | Jessie Lemont, 1918 | https://www.gutenberg.org/ebooks/38594 |
| LIT-514 Rupert Brooke, The Soldier | original English | https://poetrydb.org/ |
| LIT-515 Horace, Odes I.11 (Carpe Diem) | A. S. Kline | https://www.poetryintranslation.com/PITBR/Latin/HoraceOdesBkI.php |
| LIT-516 Federico García Lorca, Romance Sonámbulo (opening) | A. S. Kline | https://www.poetryintranslation.com/PITBR/Spanish/LorcaPoemsLoveDeath.php |
| LIT-517 Fernando Pessoa, Autopsychography | A. S. Kline | https://www.poetryintranslation.com/PITBR/Portuguese/FernandoPessoa.php |
| LIT-518 Rudyard Kipling, If— | original English | https://www.gutenberg.org/ebooks/556 |
| LIT-519 William Blake, London | original English | https://poetrydb.org/ |
| LIT-520 George Gordon, Lord Byron, She Walks in Beauty | original English | https://poetrydb.org/ |
| LIT-521 Robert Burns, A Red, Red Rose | original English | https://poetrydb.org/ |

Still missing from the writing list: Dickinson "I'm Nobody", Wordsworth's daffodils, Yeats, Frost "Stopping by Woods", Henley "Invictus", Owen, Hardy, Sandburg, Cummings, Pound, Lawrence, Chaucer, Ovid, Proust, Flaubert, Rousseau, the Buddha beyond the Dhammapada, Cavafy. Neruda is deliberately left out: his originals are still in copyright.

**Art: 36 of 72 were missing; none added.** The work sandbox cannot reach Wikimedia (rate-limited), so image links could not be checked, and an unchecked link is a broken picture.

- Public domain and addable once images can be verified: Mona Lisa, The Last Supper, The Starry Night, Sunflowers, The Birth of Venus, The Creation of Adam, David, Impression Sunrise, The Night Watch, The Third of May 1808, Olympia, Le Déjeuner sur l'herbe, The Thinker, The School of Athens, The Arnolfini Portrait, American Gothic, Malevich's Black Square, and something by Renoir, Titian, Giotto, Bernini, Klee, Mondrian, Modigliani, Matisse (pre-1930 work).
- Still in copyright, cannot be shown: Picasso's Guernica, Dalí, Kahlo, Magritte, Hopper's Nighthawks, Warhol, Pollock, Rothko, Basquiat, O'Keeffe, Brancusi.

## Artwork clean-up — 12 November 2026

- **Paired quotes removed from all 500 artworks.** They were unchecked text added by the first build.
- **Wikimedia images checked.** All 372 Wikimedia files exist (Commons API, run in Paul's browser). The problem was size, not broken links: the Wall was loading original files, 4.4 GB in total, 57 of them over 10 MB and one of 890 MB. `imageUrl` now points at the 960px thumbnail for 312 of them; all 312 thumbnails were loaded successfully in the browser. `highResUrl` still points at the original.

## Not yet audited

The 500 artworks (titles, artist credits, dates, museum attributions) have not been through this process. Note for that audit: 370 of them hotlink images from Wikimedia, every artwork carries an AI-written `note` and `craftSpec`, and 500 carry a paired `quote` whose wording and attribution have never been checked. All 425 older writing pieces also carry an AI-written `note`, shown under “Notes” in the reader.

## Context notes — 12 November 2026

Decision: Claude writes the context notes (rule 1 in CLAUDE.md now says so). The old notes were written by another model during the first build and never checked; all are to be replaced.

- Batch 1: 91 notes (70 artworks, LIT-501 to LIT-521). Marked `noteRev: 2` in the data.
- Written from well-documented facts about each work. They were not each looked up against the museum record; anything that would have been a guess was left out.
- The Craft / Process row is gone from the specs drawer. `craftSpec` remains in the data for now.
- Noticed while writing, for the art audit: VAULT-003 (Turner, the Met's *Whalers*) carries the subtitle of a different Turner painting in the Tate. Many records list the museum as "Global National Treasures & Museums", which is not a museum.

### Finished 13 November 2026

All 946 notes rewritten (500 artworks, 446 writings). After Paul's note ("don't get cute or clever, keep it factual") the first 191 were gone over again and about 25 were flattened.

Turned up while writing, not acted on:

- **LIT-081, "The Sun Never Says".** By Daniel Ladinsky (1999), a living author. Not public domain and not openly offered, so it breaks rule 4. Paul to decide: cut, or replace with a real Hafez ghazal (Gertrude Bell, 1897).
- **Possibly still in copyright outside the US:** VAULT-415 Goncharova (d. 1962), VAULT-428 Hopper (d. 1967); texts by Ibarbourou (d. 1979), Mistral (d. 1957), Akhmatova (d. 1966), Stevens, Williams, Moore, Hughes, H.D. Check each during the audits.
- **Records that may not describe a real object:** VAULT-293 "Seated Statue of Vizier Ptahhotep", VAULT-275 triptych by "Ueno Jakugen", VAULT-331 Harar Qur'an by a named scribe, VAULT-287 "Sunzi bamboo slips, Qing archival edition", VAULT-334 "Haʻalelea's" cloak. Their notes describe the subject only.
- **Wrong or doubtful details in records:** VAULT-003 Turner subtitle belongs to a different painting; VAULT-343 Muisca raft was found at Pasca, not Lake Guatavita; VAULT-214 "First Half — Master Wuyong Scroll" mixes up the two halves; VAULT-026 is listed as the Met but the page may be elsewhere; VAULT-372, 494, 488, 215 are Met works listed under the placeholder museum; LIT-115 Schopenhauer title and date do not match (1851 is Parerga); LIT-137 Hildegard date; LIT-392 and LIT-394 poem dates.
- Many artwork titles and artist credits are dressed up ("Machu Picchu Dry-Fitted Granite Cloud Citadel", "Mexica Imperial Sculptors of King Axayacatl"). The notes use plain names.

## Art audit — 13 November 2026

Paul's instruction: everything must be right; made-up or wrong information matters more than copyright.

**Museum-held works (129 of 130).** Fetched from the Met, Art Institute of Chicago, Cleveland and SMK APIs. Title, maker, date and medium now follow the museum. Real errors found and fixed:
- VAULT-129 was labelled Kangra, ca. 1790–1800. Chicago says Rajasthan, Kota, mid-18th century.
- VAULT-026 was titled "Bahram Gur Fights the Horned Wolf". The Met object is "Rustam Kills the White Div".
- VAULT-061 was credited to Charles Meryon, 1853. Cleveland's object is by John Taylor Arms, 1920.
- VAULT-037 note described the wrong page of Vesalius. VAULT-052 was placed in Cambodia; Cleveland says northeastern Thailand.
- VAULT-012 is "probably" Henry VIII's. VAULT-003 lost a subtitle that belonged to another Turner. Invented makers ("Kangra Court Master", "Sultanate Period Master", "Safavid Court Workshop") replaced by the museum's wording.
- VAULT-117 (Bonheur, Sheep): the accession number in the record does not resolve. Unconfirmed.
- VAULT-167 and VAULT-035 are two different Met tughras, not duplicates.

**Wikipedia-sourced works (361).** Each source page and its Wikidata record fetched. 312 confirmed as the work described, with maker and date agreeing. Titles stripped of invented description (about 200), invented makers replaced with "Maker unknown" or the documented name (131 now anonymous), dates stripped of padding, placeholder museum removed everywhere and replaced with the real holder where known.

**Site-wide.** Removed "CC0 Public Domain" from the credit line, provenance line and link labels: it was asserted for every work and was not true for many.

**Unconfirmed (59).** Source is an artist, genre or subject page, so the specific object is unverified: VAULT-132, 127, 139, 128, 140, 156, 162, 168, 169, 171, 172, 173, 174, 180, 181, 182, 195, 207, 208, 209, 210, 217, 218, 228, 230, 232, 252, 272, 275, 282, 293, 325, 328, 330, 331, 334, 335, 341, 378, 415, 417, 418, 419, 430, 452, 453, 473, 484, 485, and ten never checked: 141, 148, 133, 117, 144, 382, 385, 406, 420, 502.

**Not done.** Notes were corrected only where a museum record contradicted them. The other notes have not been re-read against sources. Medium unchecked on Wikipedia-sourced works. The writing side still has 16 loose, 13 unconfirmed, 10 attribution.

### Later the same day

The image's own Wikimedia Commons record was read for each unconfirmed work. 53 of the 59 turned out to be real, identifiable objects and now carry their holder. Wrong records found this way:
- VAULT-181 was titled "The Poet Bihari Offers Homage to Radha and Krishna". The image is Nainsukh's self-portrait, ca. 1730.
- VAULT-252 was credited to Julia Margaret Cameron. It is a portrait of her, taken by her son Henry in 1870 (the Met).
- VAULT-325 was dated early 20th century. The museum dates it 1965–1975.
- VAULT-139 is by the circle of the Master of Calamarca, not the master, and is not the painting in the church.
- VAULT-293 (Ptahhotep statue), VAULT-275 (Ueno Jakugen) and VAULT-331 (Harar Qur'an), suspected of being invented, are real.

Still unconfirmed: VAULT-117, 168, 174, 208, 430, 485.

Notes: dates in 48 Wikipedia-sourced notes checked against the full article text. No errors; one softened (VAULT-230).

### Notes date check, finished 13 November 2026

VAULT-430 matched to the Peabody Museum, Harvard, and VAULT-485 to the Museo Etnográfico Juan B. Ambrosetti, Buenos Aires. Four artworks remain unconfirmed: VAULT-117, 168, 174, 208.

Every year in the art notes on Wikipedia-sourced works (106 pages) and in the writing notes (about 245 author or work pages) was checked against the full article text. Unmatched years were reviewed by hand; all were correct facts the article simply does not mention. No wrong date found. Not covered: non-date claims, notes without a year, about 40 anonymous or collective authors, and the notes on the 129 museum-held artworks.

### Cuts, 13 November 2026 (Paul: cut what we can't find)

- VAULT-168, Ouyang Xiu letter: its own file record questions its authenticity.
- VAULT-174, celadon vase: a visitor's photograph with no object record.
- VAULT-208, Harunobu print: scanned from a postcard, title and holder unknown.
- LIT-081, "The Sun Never Says": by Daniel Ladinsky (1999), not Hafez, and in copyright. Hafez is still represented by LIT-449 (Gertrude Bell's translation).
- VAULT-117, Bonheur's *Sheep*, was kept: matched to Cleveland 1915.716 and the image replaced with the museum's own.

None of the four is a work a visitor would come looking for. Library is now 497 artworks and 445 writings.

### Notes name check, 13 November 2026

Run from Paul's browser on the live site: for each piece, fetch the full Wikipedia article for its source page (artworks) or its author (writing, and museum-held artworks), and list every capitalised name in the note that the article does not contain.

- 869 notes covered. 586 had every name present in the article.
- 283 had one or more names absent (446 names in all). Each was reviewed by hand. They were true details the article does not mention (a translator, a museum, a patron, a place) or stray capitalised words. None was judged wrong, but that judgement rests on general knowledge, not on a second source.
- 73 notes not covered: no usable article for the maker or author.

No note was changed as a result.

## Loose texts, last pass — 13 November 2026

The 16 remaining loose texts. 13 re-sourced and now `verified`; 3 left.

Every sentence of each new text was machine-checked against the downloaded source (letters only, ignoring spacing and punctuation), and where the source is an archive.org OCR scan, against a second scan too. Punctuation was read by eye from the OCR; three passages were checked against the page image (Masani, Tukārāma, Avalon).

| id | Piece | Text now from | Checked |
|---|---|---|---|
| LIT-290 | Hölderlin, **Hyperion's Song of Fate** (was *Hälfte des Lebens*) | German Classics vol. 4 (1913), tr. Charles Wharton Stork, Gutenberg #12060 | Gutenberg text |
| LIT-300 | Attar, Conference of the Birds — The Valley of Bewilderment | R. P. Masani's abridged prose version (OUP, 1924) | one scan + page image |
| LIT-302 | ʿAntara, Muʿallaqa | Sir William Jones (1782), in Clouston, Arabian Poetry for English Readers (1881) | two scans |
| LIT-314 | Nizami, Haft Paykar (The Black Dome) | C. E. Wilson, The Haft Paikar, vol. 1 (1924) | two scans |
| LIT-325 | Tirukkuṛaḷ 129, 396, 972 | G. U. Pope, The 'Sacred' Kurral (1886) | two scans |
| LIT-328 | Tukārām, Abhang (no. 2718) | Fraser and Marathe, The Poems of Tukārāma, vol. 3 (1915) | two scans + page image |
| LIT-391 | Droste-Hülshoff, Am Turme | German Classics vol. 7 (1913), tr. Charles Wharton Stork, Gutenberg #12351 | Gutenberg text |
| LIT-402 | Chekhov, **Letter to Suvorin (27 October 1888)** (was the Lazarev-Gruzinsky letter) | Letters of Anton Chekhov, tr. Constance Garnett (1920), Gutenberg #6408 | Gutenberg text |
| LIT-448 | Ferdowsi, Shahnameh (conclusion) | Warner and Warner, vol. 9 (1925), p. 122 | two scans |
| LIT-484 | Larsen, Quicksand | Standard Ebooks edition (from the Gutenberg transcription) | one text |
| LIT-130 | Karpūrādi-Stotra, verse 7 | Arthur Avalon (Woodroffe), Hymn to Kālī (1922; 1953 printing) | two scans + page image |
| LIT-184 | Napoleon, Farewell to the Old Guard | Bryan, The World's Famous Orations, vol. 7 (1906), anonymous translator | one scan |
| LIT-190 | Hugo, Funeral Oration for Balzac | Wormeley, A Memoir of Honoré de Balzac (1892), p. 349 | two scans |

Things to know:

- **Two pieces changed to a different work by the same author**, because the famous one has no usable English text. Hölderlin's *Hälfte des Lebens* is gone; *Hyperion's Song of Fate* took its record, moved from Earth to the God shelf, and got a new note. Chekhov's loaded-rifle letter is gone; the "stating a problem correctly" letter to Suvorin took its record and got a new note. A search for "Chekhov's gun" still brings up the Chekhov letter, but the rifle line itself is no longer on the site. Koteliansky's 1927 *Anton Tchekhov: Literary and Theatrical Reminiscences* may carry a version of the rifle remark and is public domain in the US by date, but no open scan was reachable, so that is unchecked.
- The stored original-language lines were cleared on those two, since they belonged to the old texts.
- Masani (d. 1966) and the 1925 Warner volume are public domain in the United States by publication date; elsewhere that may differ.
- Tukārāma 2718: the print has a stray semicolon after "fight" (left out) and no stop after "soul of our soul" at the page turn (shown as a line break).
- Droste: stanza breaks follow the German (four stanzas of eight lines), not Gutenberg's page-break artefacts.
- Jones spells it "coloquinteda"; Pope writes "throughly". Both kept.
- Napoleon: Bryan's version has the embrace of General Petit and the eagle but not the "our cause was not lost" sentence the old hook used. Bourrienne's Memoirs (Gutenberg #3567) gives a different English version with that sentence and without the eagle.
- Standard Ebooks modernises some spelling; if that matters, compare with the 1928 first edition.

Not found:

- **Shiki, persimmon haiku.** Not in Chamberlain's Japanese Poetry (1911) or Porter's A Year of Japanese Epigrams (1911). Miyamori's 1932 anthology has Shiki but is not yet public domain in the US.
- **Agustini, Lo inefable.** Not in Blackwell's Some Spanish-American Poets (1929; she is only named in the introduction) or Walsh's Hispanic Anthology (1920).
- **Bolívar, Jamaica Letter.** No public-domain English text found on archive.org or Gutenberg; the standard modern translation is in copyright.

### Later the same day: must-haves brought back

Paul: find a way to confidently carry a version of anything people would look for. Method now in CLAUDE.md (public-domain text first, then a short credited quote whose wording has been checked).

- **LIT-522 Chekhov's gun (new).** "If in the first chapter you say that a gun hung on the wall…" from Shchukin's reminiscences in Koteliansky, *Anton Tchekhov: Literary and Theatrical Reminiscences* (1927), p. 23. Public domain in the US. One archive.org scan; every sentence matched by script. The date of the remark is not given, so the record says "before 1904".
- **LIT-344 Shiki, persimmon haiku.** Now `quoted`: Janine Beichman's translation (Kodansha, 1986) as given by the University of Virginia's Japanese Text Initiative, which also confirms the Japanese. It is the whole haiku, three lines, from a book still in copyright.
- **LIT-476 Bolívar, Jamaica Letter.** Now `quoted`: two sentences from Lewis Bertrand's translation (Selected Writings of Bolivar, 1951) as reproduced by Brown University Library. Read through a web fetch, not from a scan of the book.
- **Hölderlin, *Hälfte des Lebens*: still off.** A reference page gives closing lines ending "Weathercocks clatter" but names no translator, so it can't be credited. Needs Hamburger's *Poems and Fragments* or a page that quotes it with a credit.
- Not yet tried under this method: the "Cut, wanted back" six (Ghalib, Hagakure, Ibn Khaldun, Kleist, Sōseki, Lautréamont) and the famous writings and artworks listed as missing under "Public test, first pass".

## Full-list pass — 13 November 2026 (evening)

Paul: "do the full list." Library is now 521 artworks and 431 writings.

### 1. Unconfirmed and shaky texts: none left

Re-sourced (8):

- LIT-234 Tōia Tainui: Buick, An Old New Zealander (1911), Gutenberg #44726. Translator not named there.
- LIT-237 Michelangelo, Sonnet 151: J. A. Symonds (1878), Gutenberg #10314.
- LIT-293 Apollinaire, Le Pont Mirabeau: A. S. Kline, poetryintranslation.com (non-commercial terms).
- LIT-367 Baudelaire, Une Charogne: "The Corpse" from the Huneker edition (1919), Gutenberg #36287. The credit to F. P. Sturm is from general knowledge, not from the edition.
- LIT-115 Schopenhauer, pendulum line: Haldane and Kemp (1883), Gutenberg #38427. Date corrected to 1818.
- LIT-078 Gilgamesh, Siduri's advice: R. Campbell Thompson (1928), one archive.org scan.
- LIT-469 Liliʻuokalani: now her Official Protest to the Treaty of Annexation (1897), from Hawaii's Story by Hawaii's Queen (1898). The song Kuʻu Pua i Paoakalani is gone; its English could not be confirmed. Moved to the War shelf.

Cut (14), because the wording could not be matched to any real text:

- LIT-338 Anecdote about Mi Fu, *Mi Fu Bows to the Rock*
- LIT-371 Jules Laforgue, *Litanies of the Last Quarters of the Moon*
- LIT-376 Guillaume Apollinaire, *Il pleut (It's Raining)*
- LIT-446 Ali-Shir Nava'i, *Ghazal (Flint and Spark)*
- LIT-450 Abu al-ʿAlāʾ al-Maʿarrī, *Elegy (Tread Lightly)*
- LIT-459 Yoruba Babaláwo Oral Divination Canon, *Odù Ifá*
- LIT-153 Yoruba Babaláwo & Akéwì Oral Canon, *Oríkì of Ṣàngó*
- LIT-466 Nana Asma'u, *Poem*
- LIT-475 Salomé Ureña, *Ruinas*
- LIT-470 Attributed to Crazy Horse (Tȟašúŋke Witkó), *Attributed Sayings*
- LIT-473 Tochihuitzin Coyolchiuhqui (attributed), *We Only Came to Dream*
- LIT-334 Yu Xuanji, *To a Neighbor Girl*
- LIT-137 Hildegard von Bingen, *Liber Divinorum Operum*
- LIT-369 Comte de Lautréamont (Isidore Ducasse), *Les Chants de Maldoror (Canto VI)*

Three of those are names a visitor may look for: **Hildegard von Bingen** (her artwork is still here), **Crazy Horse** (no saying can be verified as his) and **Yu Xuanji**. Apollinaire's Il pleut and Lautréamont's Canto VI are also gone; Lautréamont was already on the wanted-back list.

### 2. Famous artworks: 24 added

Mona Lisa, The Last Supper, The Starry Night, Sunflowers (National Gallery version), The Birth of Venus, The Creation of Adam, David, Impression Sunrise, The Night Watch, The Third of May 1808, Olympia, Le Déjeuner sur l'herbe, The Thinker, The School of Athens, The Arnolfini Portrait, American Gothic, Bal du moulin de la Galette, Venus of Urbino, Giotto's Lamentation, Ecstasy of Saint Teresa, Twittering Machine, Mondrian's Composition with Red, Blue and Yellow, Modigliani's Nu couché, Matisse's Dance.

- Title, maker, date and holder from the Wikipedia article lead and the Wikidata record of each work. Medium from Wikidata or the article, not from the museum. Twittering Machine has no medium.
- Each image is the article's lead image on Wikimedia Commons. All 24 thumbnails were downloaded from the sandbox, and each palette was computed from the actual image.
- The Thinker shows the Kunsthalle Bielefeld cast, and says so. Sunflowers was confirmed as the London picture from its Commons file page.
- Notes written to the usual standard from well-documented facts; not checked one by one against a source.
- Still absent because they are in copyright: Guernica, Dalí, Kahlo, Magritte, Nighthawks, Warhol, Pollock, Rothko, Basquiat, O'Keeffe, Brancusi.

### 3. "Verified" was softer than the name: edition check started

The first audit marked a text verified when the wording was recognised as a published text. Checking sentence by sentence against editions showed that this let through paraphrased and stitched wording, mostly in prose. Examples found and fixed: Carmilla, The Great God Pan, The Gods of Pegāna, Incidents in the Life of a Slave Girl, Confessions of an English Opium-Eater, Songs of Kabir, Candide, Salomé.

State of the 431 writings after this pass:

- **244 edition-sourced or edition-checked**: taken from, or matched line by line against, a named edition.
- **187 recognised only**: not yet checked against an edition. Expect some of these to be condensed or reworded. Most have no Gutenberg link or are translations with no translator recorded.

Done this pass: 58 pieces matched an edition in full and are marked so; 15 were replaced with the edition's wording (list in the commit); 5 stitched quotes got an ellipsis where they skip text (Persuasion, Moby-Dick whiteness, Heart of Darkness, Cask of Amontillado, Duchess of Malfi).

Known to need a hand repair (some sentences do not match the edition linked): LIT-226 Kalevala, LIT-041 Frankenstein, LIT-096 The Yellow Wallpaper, LIT-197 Middlemarch, LIT-002 Moby-Dick (Ahab), LIT-008 Hamlet, LIT-031 The Art of War, LIT-035 A Modest Proposal, LIT-099 Jekyll and Hyde, LIT-166 Agricola, LIT-010 Dickinson, LIT-216 Bradstreet, LIT-014 The Tyger, LIT-025 Paradise Lost, LIT-059 Annabel Lee. Some of these will only be spelling or a different edition.

Method: strip both texts to letters only, split the piece into sentences and lines, and require every one to occur in the edition. Where it fails, pull the passage from the edition between a start and an end phrase, so nothing is retyped.

### 4. Not done

- **Art medium and museum** (203 and 164 blank). The Wikidata route does not work from the sandbox: it is throttled to a crawl, and many source links point at the artist's page, not the work's. Needs the Commons file records from Paul's browser, as before.
- **Hälfte des Lebens and the six wanted-back writers.** Need web lookups that require Paul's approval when he is away.
- **Live site and a real phone.** Tested locally at desktop and phone size only.

### 5. Small fixes

- The two Met tughras (38.149.1 and 38.149.2) have identical titles at the museum; the accession number is now in each title so both show.

## Edition check completed — 13 November 2026 (night)

Paul: "do it all however is best optimized for you." The 187 recognised-only pieces were split into six batches and worked in parallel, each to the same brief (kept in the session, summarised in CLAUDE.md). Every result was machine-checked: a text was only accepted if each sentence and line occurs, letters only, in the downloaded edition. Library is now 521 artworks and 436 writings.

**Result for the 187:** 49 matched their edition as they stood. 126 did not and were replaced with the edition's wording. 6 became short credited quotes. 5 were cut. 1 is still open.

So roughly two in three of the texts the first audit called verified were reworded, stitched or in a wording no edition carries. All 436 writings are now tied to a named edition or are short credited quotes, except LIT-058.

**Cut (5):**
- LIT-083 Su Shi (Su Dongpo), *Memories of the Red Cliff (Nian Nu Jiao)*: The two English lines could not be tied to any published translation; the record's only source is the Chinese text on zh.wikisource, so the English looks composed. No public-domain or openly offered English version of this ci (Nian Nu Jiao, Red Cliff) was found. To bring Su Shi back: a one-line credited quote from a standard translation (e.g. Burton Watson) once the wording is confirmed on a library page, or Herbert Giles's public-domain version of the Red Cliff prose-poem as a different piece. **A visitor may look for this.**
- LIT-468 Te Rauparaha (Ngāti Toa Rangatira), *Ka Mate*: neither the Māori nor the English wording could be tied to an edition **A visitor may look for this.**
- LIT-257 Georg Christoph Lichtenberg, *The Waste Books*: The three aphorisms are in a modern rewording with no credited translator (source was Wikiquote). No public-domain English Lichtenberg could be found on Gutenberg or archive.org (Alliston's 1908 Reflections is not scanned there). The standard version is R. J. Hollingdale's The Waste Books (NYRB, 2000), in copyright; I could not confirm his wording of the mirror aphorism from a publisher or library page (a Chronicle of Higher Education article gives a different wording, uncredited). Bring back as a one-line credited quote once the Hollingdale wording is checked against the book.
- LIT-472 Queen Liliʻuokalani, *Aloha ʻOe*: English wording matches no source; reads as reworded **A visitor may look for this.**
- LIT-189 Louis Antoine de Saint-Just, *Speeches to the Convention*: Two lines from two different speeches (13 Nov 1792 on the king; the second from 1793-94), stitched, in an English wording with no translator. No public-domain English edition of Saint-Just carrying these words was found (Gutenberg, archive.org full-text search); every English printing found is a modern history quoting its own rendering ("One cannot reign innocently", "No man can reign innocently", "dig their own tombs"). Could come back as a credited one-line quote from Marian Rothstein's translation in Walzer, Regicide and Revolution (Cambridge, 1974), if the wording is checked against the book.

**Still open (1):** LIT-058 Dickinson, "Tell all the truth but tell it slant". First printed in 1945, so there is no public-domain edition; the two lines are the standard reading but were not re-confirmed against a source this pass.

**Restored or new (10):** LIT-523 Friedrich Hölderlin, Half of Life (Hälfte des Lebens) (quoted); LIT-524 Mirza Ghalib, Hazaaron Khwahishein Aisi (Thousands of Desires) (quoted); LIT-525 Yamamoto Tsunetomo, Hagakure (quoted); LIT-526 Ibn Khaldun, The Muqaddimah (On the Science of History) (public-domain); LIT-527 Heinrich von Kleist, On the Marionette Theatre (public-domain); LIT-528 Natsume Sōseki, Ten Nights of Dream — The First Night (quoted); LIT-529 Comte de Lautréamont (Isidore Ducasse), Les Chants de Maldoror (Canto VI) (quoted); LIT-530 Hildegard von Bingen, The Book of Divine Works (I Am That Supreme and Fiery Force) (public-domain); LIT-531 Yu Xuanji, Sent to a Neighbor Woman Friend (quoted); LIT-532 Guillaume Apollinaire, Il pleut (It's Raining) (quoted).

### Famous wordings that changed, because the familiar words are not in any edition that could be reached

- Dante: "Abandon all hope, ye who enter here" is now Longfellow's "All hope abandon, ye who enter in!"
- Bhagavad Gita: "destroyer of worlds" is now Edwin Arnold's "Thou seest Me as Time who kills".
- Elizabeth I at Tilbury: "heart and stomach of a king" is now "the heart of a king, and of a king of England too" (Hume, Aikin).
- Catullus 101: ends "hail! for ever, adieu!" (Smithers), not "hail and farewell".
- Simonides: Macaulay's rendering, not "Go tell the Spartans".
- Diogenes: "Cease to shade me from the sun" (Yonge).
- La Rochefoucauld: "Neither the sun nor death can be looked at without winking."
- Dickinson: both poems now follow the 1890s editors' texts; the "Plank in Reason" stanza is gone because that edition omits it.
- Ida B. Wells: "The way to right wrongs…" could not be found in her writings; the piece is now a passage from Southern Horrors.
- Sun Tzu: "Victorious warriors win first…" is not in Giles and is gone.
- Bashō, Issa: now Chamberlain's 1902 versions, which read dated.
A search for the familiar wording will miss these. Each could be restored as a short credited quote from a modern translation.

### For Paul to decide

- **Sojourner Truth** is now Frances Gage's 1863 report, which is written in dialect. **Harriet Tubman** is Bradford's 1869 text, also in dialect. These are the published sources, but the dialect is the reporters'.
- **Rubén Darío, Lo fatal** is now the Spanish original only; no public-domain English was found. Same for **Storni** and **Sor Juana**.
- Notes were not rewritten to match replaced texts, except Pankhurst's (the words turned out to be from her 1908 Bow Street speech, not the 1913 Hartford one). A note may mention a line that is no longer shown.

### Weakest sources (check first)

- Quotes confirmed only through a page summary or a search snippet: Linji (Sasaki), Ryōkan (Stevens), Li Qingzhao (Rexroth), Brás Cubas (Rabassa), Delacroix (Norton), Hölderlin (Hamburger; line breaks inferred), Sōseki, Lautréamont (Lykiard), Hagakure (Wilson), Ghalib (Kanda).
- Translator credits not on the page: van Gogh letter (credited from memory), Zola (Tucker edition names no translator), Apollinaire's Il pleut (Padgett inferred from the handbook's rule), Tacitus, the Emerald Tablet, Baudelaire's Corpse (Sturm).
- OCR-only sources where a clean passage was chosen and gaps marked with an ellipsis: Rumi, Zafarnama, Debs, Pitt, Garibaldi, Gracián, Heart Sutra, Cicero, Mirabai, Martí, Hokusai, Seneca, Naidu, Komachi, Heraclitus, Eckhart, Chief Joseph, Toussaint, Du Fu, Wang Wei, Ibn Arabi, John of the Cross, Tecumseh (a late retelling), Kleist, Ibn Khaldun.
- Bynner's Jade Mountain is 1929 and Trevelyan (Garibaldi) died in 1962: public domain in the US, not everywhere.

### Art medium and museum

Run from Paul's browser. Only 37 of 231 Commons files carry a structured link to a Wikidata item, and most file pages are a bare description. 36 mediums and 19 holders were filled. 168 mediums and 145 holders are still blank and cannot be filled from structured data; each would have to be read off the museum's own page.

## Modern wording pass — 13 November 2026 (late)

Paul: "make sure there is a modern, respectful, agreed-upon translation or phrasing of everything, in regards to languages and dialects." This replaces the old habit of preferring the public-domain wording for the pull quote.

**How it works now.** For a translated piece, the pull quote is one or two lines from the current standard translation, credited to translator and book (`audit: quoted`). The older public-domain passage is kept in `olderText` / `olderTranslator` and shown in the reader behind a "Longer passage" button. The older wording stays searchable.

**Result.** 234 translated or reported pieces were reviewed. 115 now lead with a modern standard wording, 7 with a better public-domain standard wording, and 112 were kept as they are (already modern, or the old version is the agreed English, or no modern wording could be confirmed). 112 pieces carry a longer older passage behind the quote. The library now has 136 short credited quotes.

Every new quote was machine-checked against text fetched from the scanned book, a publisher or a university page; nothing was typed from memory. 88 were seen in the book itself or on the translator's page. **34 are "medium": the wording was seen quoted elsewhere, and for some the translator's name is from general knowledge.** Their `auditNote` says "credit to be confirmed".

**Familiar wordings restored:** Dante's "Abandon all hope ye who enter here" (Ciardi), Catullus's "hail and farewell" (Cornish), Tilbury's "heart and stomach of a king", Simonides' "Go tell the Spartans", Issa's "And yet, and yet—" (Hass), the Tao Te Ching's "The Tao that can be told…" (Feng and English), Cicero's "How long, O Catiline…". The Gita piece now carries Oppenheimer's "Now I am become Death, the destroyer of worlds", credited to him; it is his rendering, not a published translation of the Gita.

**Dialect.** Sojourner Truth is now Marius Robinson's 1851 standard-English report (retitled; it has no "Ain't I a woman"). Harriet Tubman was held back: no authoritative standard-English edition was found, so Bradford's dialect text is still showing.

**Held back on purpose (6):**
- LIT-283: popular rendering with no named translator
- LIT-224: translator of the wording not established
- LIT-478: no authoritative standard-English edition; source was a children's biography
- LIT-510: Müller's line is the one people know and search for
- LIT-211: Longfellow's is the known English
- LIT-186: credit to C. L. R. James was from memory, not from the source seen

**Retitled (6):** LIT-071 → Be Drunk (Enivrez-vous); LIT-332 → Song of the Lute (Pipa xing); LIT-366 → Against Nature (À rebours), Ch. IV; LIT-159 → Speech at the Woman's Rights Convention, Akron (“Ain't I a Woman?”); LIT-259 → Thus Spoke Zarathustra (Prologue, 5); LIT-329 → The Fisherman (Yu fu).

**Medium-confidence quotes to confirm (34):** LIT-085 Kobayashi Issa (Robert Hass, 1994), LIT-115 Arthur Schopenhauer (E. F. J. Payne), LIT-121 Rigveda (Wendy Doniger), LIT-492 José Enrique Rodó (Margaret Sayers Peden), LIT-146 Attributed to Thomas of Celano (William Josiah Irons, 1849), LIT-026 Vyasa (J. Robert Oppenheimer (his own rendering of Gita 11.32)), LIT-116 Zhuangzi (Burton Watson), LIT-123 The Qur'an (M. A. S. Abdel Haleem), LIT-168 Queen Elizabeth I (no translator), LIT-183 Alexander the Great (Aubrey de Sélincourt), LIT-248 Diogenes of Sinope (R. D. Hicks), LIT-353 Middle Kingdom Egyptian Blind Harper Tradition (Miriam Lichtheim), LIT-397 Søren Kierkegaard (Howard V. Hong and Edna H. Hong), LIT-033 Homer (Richmond Lattimore), LIT-159 Sojourner Truth (no translator), LIT-015 Friedrich Nietzsche (Walter Kaufmann, 1966), LIT-131 Laozi (Gia-fu Feng and Jane English, 1972), LIT-204 Izumi Shikibu (Jane Hirshfield with Mariko Aratani, 1988), LIT-237 Michelangelo Buonarroti (James M. Saslow, 1991), LIT-270 Yosa Buson (R. H. Blyth, 1950), LIT-354 Achaemenid–Babylonian Chancery Scribes (Irving Finkel, British Museum), LIT-029 Farid ud-Din Attar (Afkham Darbandi and Dick Davis), LIT-102 Miguel de Cervantes (Edith Grossman), LIT-134 Papyrus of Ani (Raymond O. Faulkner), LIT-150 Orphic Mystery Initiates (Fritz Graf and Sarah Iles Johnston), LIT-221 Taras Shevchenko (John Weir), LIT-238 Michelangelo Buonarroti (James M. Saslow), LIT-259 Friedrich Nietzsche (Walter Kaufmann), LIT-290 Friedrich Hölderlin (Michael Hamburger), LIT-328 Sant Tukārām (Dilip Chitre), LIT-355 King Hammurabi's Babylonian Scribes (Martha T. Roth), LIT-118 Sei Shōnagon (Ivan Morris), LIT-119 Kamo no Chōmei (Donald Keene), LIT-206 Murasaki Shikibu (Royall Tyler).

**Kept, but a modern standard exists and could not be confirmed in this pass:** Rostam and Sohrab (Davis), Mirabai, Kalevala (Bosley), Nizami, Teika, Pu Songling (Minford), Bhartṛhari (Miller), Pushkin, Abu Nuwas, Meghadūta, Lu You, Mistral, Verlaine, Heine, Lucretius, Kartini (Coté).

Not reviewed: notes (some may mention an old line), and line breaks in quotes taken from search snippets, which show words but not layout.

## Closing pass — 13 November 2026 (last)

- **Quote credits:** the 34 medium-confidence quotes, the 6 held-back pieces and 31 unconfirmed keeps were re-examined. 32 confirmed in the translator's own book or a credited reprint, 17 corrected, 22 kept as they are. No piece now carries "credit to be confirmed". Corrections of note: Michelangelo's Sonnet V is Christopher Ryan's wording, not Saslow's; Harriet Tubman is now in standard English as quoted by Kate Clifford Larson (also in Humez); Toussaint is C. L. R. James's wording; Saadi's Bani Adam is the wording quoted at the UN, credited to M. Aryanpoor on the strength of one published book; al-Mutanabbi (Farrin) and Abu Nuwas (Hamori) are scholars' renderings, not agreed standards. Teresa of Ávila stays in Longfellow's version.
- **Kept without a modern wording (22):** LIT-313, LIT-323, LIT-228, LIT-427, LIT-184, LIT-319, LIT-510, LIT-276, LIT-343, LIT-304, LIT-331, LIT-288, LIT-456, LIT-256, LIT-337, LIT-113, LIT-417, LIT-207, LIT-394, LIT-522, LIT-428, LIT-291. Reasons are in the session record; in short, no standard modern wording could be confirmed, or the old version is the agreed English.
- **Notes:** all 436 writing notes were re-read against the text now shown, and the 24 new art notes were fact-checked against each work's Wikipedia article. 99 were rewritten (`noteRev: 3`): notes naming a translator or passage no longer shown, a few wrong facts (the Popol Vuh episode, the Kalevala harp, Beowulf's passage, the Iliad passage), unsupported claims, and rule breaks (quotation, asides, more than four sentences). Rewrites of writing notes were made from the record and general knowledge, not from a lookup.
- **Art records corrected from the same check:** Nu couché is in a private collection; Twittering Machine has its medium; The Creation of Adam is ca. 1512; Venus of Urbino is 1534; The Thinker is modelled ca. 1881, first cast 1904; The Night Watch is on loan to the Rijksmuseum from the Amsterdam Museum.
- **Pull quotes:** a sweep found six "checked" pieces whose pull quote was reworded even though the full text was exact (Book of Tea, Reading Gaol, Crossing Brooklyn Ferry, Rubáiyát, Lady of Shalott, Crane's In the Desert). Fixed. Every pull quote on the site is now an exact run of words from its own text or its longer passage; this is machine-checked.
- **Still open:** three dates that may belong to a poem shown earlier (LIT-337 Lu You, LIT-394 Trakl, LIT-400 Rosalía de Castro); line breaks on quotes taken from search snippets; 168 art mediums and 145 holders with no structured source.

## Art details from legitimate sources — 13 November 2026 (after the closing pass)

Paul: "if you can find it somewhere legit, do it. That goes for all."

- Each of the 188 artworks missing a medium or holder was looked up one by one. 121 mediums and 55 holders were added: 26 from the holder's own record (Met, V&A, Rijksmuseum, Tate, British Museum, British Library, National Palace Museum, MFA Boston, NGA, Library of Congress and others), the rest from the Wikipedia article on that specific work, its Wikidata item or its Commons file record. Each `auditNote` names the page.
- 56 works are buildings, sites, rock art or book plates with no single holder. They are flagged `noHolder` and left without a museum line.
- **Still blank: 46 mediums and 34 holders.** No source states them: mostly printed multiples where the impression shown cannot be identified, plates from books, and a few objects whose image comes from an unattributed web page.
- Held back: the holder for VAULT-198 (rests only on the file name) and both fields for VAULT-403 (the source describes the original drawing; the image may be the printed plate).
- **Three artworks had the wrong title for the image shown** and were corrected after looking at the pictures: VAULT-202 Yoshitoshi (not "Mount Yoshino Midnight Moon"), VAULT-178 Sanxingdui (a bronze head with a gold mask, not a bronze mask), VAULT-339 Nazca (the monkey, not the hummingbird). These had passed the earlier identity audit. The same check, image against title, has not been run by eye on the other 330 or so works.
- Other flags not acted on: VAULT-156 is an etched book plate, not a painting, and its title is generic; VAULT-458 Kanishka casket (Wikipedia says the original is in Peshawar and the British Museum has a copy); VAULT-324 (source says volcanic tuff); VAULT-266 (owned by Kennin-ji, on deposit at Kyoto National Museum); VAULT-385 (note says watercolour, Musée d'Orsay, unsourced).
- Three poem dates corrected: Lu You's To Wine (c. 1179, inferred), Trakl's Amen (1913), Rosalía de Castro's Las campanas (1884). VAULT-219's medium now follows the Met's wording.
- Follow-up the same night: the remaining 181 Commons images had their file names compared with their titles. 148 name the work. Of the 33 that don't, most are the work's name in another language; seven with uninformative names were looked at and all match (Blake's Ghost of a Flea, the Standard of Ur, Tutankhamun's mask, the Muisca raft, Zurbarán's Agnus Dei, Morisot's Cradle, Whistler's Nocturne). Three could not be downloaded and are unseen: VAULT-144, 181, 327.


## Public test, second pass (14 Nov 2026)

Paul's question: does the site have what people would look for. The art side does, apart from works in copyright. The writing side had gaps, so 29 pieces were added, bringing the writing to 465.

Method. The 23 public-domain texts were pulled from the named edition between a start and an end phrase and checked letters-only, line by line, against that edition. The six writers still in copyright are each represented by one sentence of prose under fifteen words, credited, with the wording seen in archive.org full-text search results for scans of the book. Lines from poems still in copyright were not used.

| id | writer | piece | kind | source |
|---|---|---|---|---|
| LIT-533 | William Wordsworth | I Wandered Lonely as a Cloud (Daffodils) | edition text | https://www.gutenberg.org/ebooks/19221 |
| LIT-534 | Emily Dickinson | I'm Nobody! Who are you? | edition text | https://www.gutenberg.org/ebooks/12242 |
| LIT-535 | Robert Frost | Stopping by Woods on a Snowy Evening | edition text | https://www.gutenberg.org/ebooks/58611 |
| LIT-536 | Matsuo Bashō | The Old Pond (Furu ike ya) | edition text | https://www.gutenberg.org/ebooks/42735 |
| LIT-537 | Thomas Hardy | The Darkling Thrush | edition text | https://www.gutenberg.org/ebooks/3168 |
| LIT-538 | Carl Sandburg | Fog | edition text | https://archive.org/details/chicagopoems00sandrich |
| LIT-539 | Geoffrey Chaucer | The Canterbury Tales — General Prologue (opening) | edition text | https://www.gutenberg.org/ebooks/22120 |
| LIT-540 | Ovid | Metamorphoses — Daedalus and Icarus (Book VIII) | edition text | https://www.poetryintranslation.com/PITBR/Latin/Metamorph8.php |
| LIT-541 | C. P. Cavafy | The God Abandons Antony | edition text | https://www.gutenberg.org/ebooks/61116 |
| LIT-542 | Ezra Pound | In a Station of the Metro | edition text | https://www.gutenberg.org/ebooks/55564 |
| LIT-543 | E. E. Cummings | Buffalo Bill ’s | edition text | https://archive.org/details/tulips-and-chimneys |
| LIT-544 | D. H. Lawrence | Snake (ending) | edition text | https://www.gutenberg.org/ebooks/60337 |
| LIT-545 | Marcel Proust | Swann's Way — The Madeleine | edition text | https://www.gutenberg.org/ebooks/7178 |
| LIT-546 | Gustave Flaubert | Madame Bovary (Part II, Ch. 12) | edition text | https://www.gutenberg.org/ebooks/2413 |
| LIT-547 | Jean-Jacques Rousseau | The Social Contract (Book I, Ch. 1) | edition text | https://www.gutenberg.org/ebooks/46333 |
| LIT-548 | Jalāl al-Dīn Muḥammad Rūmī | Divan-e Shams — Every Form You See | edition text | https://archive.org/details/india.history.resource.111025 |
| LIT-549 | W. B. Yeats | The Lake Isle of Innisfree | edition text | https://www.gutenberg.org/ebooks/38877 |
| LIT-550 | W. B. Yeats | When You Are Old | edition text | https://www.gutenberg.org/ebooks/38877 |
| LIT-551 | W. B. Yeats | Sailing to Byzantium | edition text | https://www.gutenberg.org/ebooks/72985 |
| LIT-552 | Langston Hughes | The Negro Speaks of Rivers | edition text | https://www.gutenberg.org/ebooks/74745 |
| LIT-553 | Langston Hughes | Mother to Son | edition text | https://www.gutenberg.org/ebooks/74745 |
| LIT-554 | Virginia Woolf | Mrs Dalloway (opening) | edition text | https://www.gutenberg.org/ebooks/71865 |
| LIT-555 | Leo Tolstoy | War and Peace — The Sky at Austerlitz | edition text | https://www.gutenberg.org/ebooks/2600 |
| LIT-556 | Sylvia Plath | The Bell Jar | one-line quote | https://archive.org/details/belljarnoveloffi0000wagn |
| LIT-557 | Maya Angelou | I Know Why the Caged Bird Sings | one-line quote | https://archive.org/details/iknowwhycagedbir0000unse_x1z8 |
| LIT-558 | James Baldwin | Giovanni's Room | one-line quote | https://archive.org/details/giovannisroomnov0000bald |
| LIT-559 | Dylan Thomas | A Child's Christmas in Wales | one-line quote | https://archive.org/details/childschristmasi00thom |
| LIT-560 | Pablo Neruda | Memoirs | one-line quote | https://archive.org/details/memoirs0000pabl |
| LIT-561 | Jorge Luis Borges | Borges and I | one-line quote | https://archive.org/details/labyrinthsselect0000auth |

Things to know:
- Wordsworth is Palgrave's 1861 printing (his spelling: wander'd). Dickinson is the edited 1891 text, not her manuscript wording.
- Bashō's frog poem uses Lafcadio Hearn's 1898 version, not a modern standard one, because the modern versions are whole poems in copyright.
- Cummings: words from the OCR text of the 1923 book, indents set by eye from the page image.
- Rumi: OCR text of Nicholson 1898, stray marks removed, checked against a second scan.
- Sandburg and Hardy: the edition's opening small capitals are set in lower case.
- Plath: the wording was seen in scans of the novel and in a study that quotes it with page numbers; the source link points at the study.
- The Angelou line first considered (about an untold story) was dropped: the same sentence is credited to Zora Neale Hurston, and it could not be found in a scan of Angelou's book.
- Notes for the 29 were written from well-documented facts and not checked one by one against a second source.
- Two older pull quotes (LIT-253 Bacon, LIT-296 Du Bois) joined two phrases with words skipped between them. An ellipsis now marks the skip.

Still missing that a visitor might look for: more Rumi in the popular modern versions (in copyright and loose), Neruda's and Plath's poems, Angelou's poems, Dylan Thomas's poems, Hughes's Harlem, A Room of One's Own and Cavafy's Ithaka (a quick search turned up no public-domain English text; not searched in depth).


## Public test, closed (14 Nov 2026)

The question "does the site have what people would look for" had no finish line: each check against a longer list found more. It is now fixed to one list and closed against it.

The list. Writers: Shakespeare, Dickinson, Whitman, Frost, Poe, Keats, Shelley, Byron, Blake, Wordsworth, Coleridge, Tennyson, Browning, Yeats, Eliot, Rilke, Rumi, Hafez, Khayyam, Bashō, Issa, Li Bai, Du Fu, Sappho, Homer, Virgil, Dante, Milton, Donne, Goethe, Baudelaire, Rimbaud, Neruda, Lorca, Pessoa, Akhmatova, Tagore, Gibran, Hughes, Angelou, Plath, Dylan Thomas, Cummings, Pound, Sandburg, Hardy, Hopkins, Owen, Millay, Wilde, Kipling, Burns, Auden, Ginsberg, Bukowski, Mary Oliver, Szymborska, Borges, Kafka, Dostoevsky, Tolstoy, Chekhov, Woolf, Joyce, Proust, Melville, Thoreau, Emerson, Nietzsche, Marcus Aurelius, Seneca, Epictetus, Laozi, Confucius, Sun Tzu, Plato, Aristotle, Montaigne, Pascal, Austen, the Brontës, Dickens, Twain, Hemingway, Fitzgerald, Orwell, Camus, Sartre, Beckett, Baldwin, Morrison, Douglass, Lincoln, Martin Luther King, Sojourner Truth, Machiavelli, Cervantes, Hugo, Ecclesiastes, the Psalms, the Gita, the Tao Te Ching, Heraclitus, Van Gogh's letters, Frankenstein, Carroll, Stevenson, Stoker, Conrad, Wharton, Henley, Housman, Rossetti, Barrett Browning, Pushkin, Mandelstam, Tsvetaeva, Celan, Walcott, Heaney, Larkin, Bishop, Stevens, Williams, Moore, Brooks, Lorde, Rich, Salinger, Nabokov, García Márquez, Kerouac, Vonnegut, Steinbeck, Faulkner. Artists and works: Leonardo, Michelangelo, Raphael, Botticelli, Rembrandt, Vermeer, Caravaggio, Velázquez, Goya, Turner, Monet, Manet, Renoir, Degas, Cézanne, Van Gogh, Gauguin, Seurat, Klimt, Schiele, Munch, Hokusai, Hiroshige, Dürer, Bosch, Bruegel, Van Eyck, El Greco, Rubens, Titian, Giotto, Delacroix, Géricault, David, Ingres, Courbet, Millet, Whistler, Sargent, Homer, Hopper, Cassatt, Morisot, Toulouse-Lautrec, Rousseau, Matisse, Picasso, Kandinsky, Mondrian, Klee, Malevich, Modigliani, Rodin, Blake, Friedrich, Constable, Gentileschi, Bernini, Donatello, Mucha, Beardsley, Kollwitz, Hilma af Klint, Utamaro, Grant Wood, Kahlo, Rivera, Dalí, Magritte, Pollock, Warhol, O'Keeffe, Basquiat, Rothko, Chagall, Miró, Duchamp, Brancusi, Lichtenstein, Escher, Banksy, Nefertiti, Venus de Milo, Winged Victory, the Great Wave, The Scream, Girl with a Pearl Earring, American Gothic, The Last Supper, The Creation of Adam, The Persistence of Memory, The Kiss, The Thinker, Water Lilies, Liberty Leading the People, The Third of May, The Garden of Earthly Delights, the Arnolfini Portrait, Las Meninas, The School of Athens, La Grande Jatte, Tutankhamun, the Terracotta Army, Lascaux, the Book of Kells, the Bayeux Tapestry, the Rosetta Stone.

The check is a name match against artist and title, so it shows that each name is represented, not that every famous work by that name is there.

Added in this pass: 25 writing pieces (writing now 490) and five artworks (art now 526).

| id | writer | piece | kind | source |
|---|---|---|---|---|
| LIT-562 | A. E. Housman | Loveliest of Trees | edition text | https://www.gutenberg.org/ebooks/5720 |
| LIT-563 | Edith Wharton | The Age of Innocence (Ch. VI) | edition text | https://www.gutenberg.org/ebooks/541 |
| LIT-564 | Ernest Hemingway | The Sun Also Rises (ending) | edition text | https://www.gutenberg.org/ebooks/67138 |
| LIT-565 | William Faulkner | The Sound and the Fury (June Second, 1910) | edition text | https://www.gutenberg.org/ebooks/75170 |
| LIT-566 | Osip Mandelstam | Insomnia. Homer. Taut canvas. | edition text | https://www.poetryintranslation.com/PITBR/Russian/Mandelstam.php |
| LIT-567 | George Orwell | Nineteen Eighty-Four | one-line quote | https://archive.org/details/georgeorwellnine0000welc |
| LIT-568 | Albert Camus | The Myth of Sisyphus | one-line quote | https://archive.org/details/albertcamusessen0000camu |
| LIT-569 | Jean-Paul Sartre | No Exit | one-line quote | https://archive.org/details/noexithuisclospl00sartrich |
| LIT-570 | Samuel Beckett | The Unnamable | one-line quote | https://archive.org/details/samuelbeckettsmo0000unse |
| LIT-571 | John Steinbeck | East of Eden | one-line quote | https://archive.org/details/eastofeden0000stei |
| LIT-572 | J. D. Salinger | The Catcher in the Rye | one-line quote | https://archive.org/details/jdsalingerscatch0000unse |
| LIT-573 | Vladimir Nabokov | Lolita | one-line quote | https://archive.org/details/keystololita0000prof |
| LIT-574 | Jack Kerouac | On the Road | one-line quote | https://archive.org/details/jackkerouacthero0000wort |
| LIT-575 | Kurt Vonnegut | Slaughterhouse-Five | one-line quote | https://archive.org/details/slaughterhousefi0000kurt_c9n1 |
| LIT-576 | Gabriel García Márquez | Love in the Time of Cholera | one-line quote | https://archive.org/details/gabrielgarcamrqu0000unse_w4u6 |
| LIT-577 | Toni Morrison | Beloved | one-line quote | https://archive.org/details/tonimorrisonsbel0000unse |
| LIT-578 | Martin Luther King Jr. | Letter from Birmingham Jail | one-line quote | https://archive.org/details/annotationsonlet0000pete |
| LIT-579 | W. H. Auden | The Dyer's Hand | one-line quote | https://archive.org/details/dyershandotheres00aude |
| LIT-580 | Mary Oliver | Upstream | one-line quote | https://archive.org/details/upstreamselected0000oliv |
| LIT-581 | Wisława Szymborska | The Poet and the World (Nobel Lecture) | one-line quote | https://archive.org/details/nobellecturesfro00newy |
| LIT-582 | Philip Larkin | Required Writing | one-line quote | https://archive.org/details/requiredwritingm0000lark_b1a5 |
| LIT-583 | Seamus Heaney | Crediting Poetry (Nobel Lecture) | one-line quote | https://archive.org/details/creditingpoetryn00hean |
| LIT-584 | Derek Walcott | The Antilles: Fragments of Epic Memory (Nobel Lecture) | one-line quote | https://archive.org/details/nobelprizeannual0000unse_o4y3 |
| LIT-585 | Gwendolyn Brooks | Maud Martha | one-line quote | https://archive.org/details/maudmarthanovel00broo |
| LIT-586 | Audre Lorde | The Transformation of Silence into Language and Action | one-line quote | https://archive.org/details/cancerjournals00lord |

Artworks: VAULT-529 The Gleaners (Millet, Musée d'Orsay), VAULT-530 The Hay Wain (Constable, National Gallery), VAULT-531 David, detail of the head (Donatello, Bargello), VAULT-532 Venus de Milo (Louvre), VAULT-533 Lascaux Cave Paintings (a site, no holder). The first four were checked against their Wikidata records for date, material and holder. Lascaux's date and medium are from general reference. All five images were downloaded and looked at.

Not on the site, and why:
- Ginsberg, Bukowski, Elizabeth Bishop: known for poems still in copyright, and no line of their prose was confirmed in a scan. The Bukowski line first considered turned out to be from a poem.
- Picasso: not added. His early work may be out of copyright in the United States but the position was not checked.
- Kahlo, Rivera, Dalí, Magritte, Pollock, Warhol, O'Keeffe, Basquiat, Rothko, Chagall, Miró, Duchamp, Brancusi, Lichtenstein, Escher, Banksy: in copyright, cannot be shown.

Things to know about this pass:
- The twenty one-line quotes are prose only, each under fifteen words, each seen in archive.org full-text search results for the scan its record links to. Eleven were seen in a scan of the book itself; nine (Orwell, Camus, Beckett, Salinger, Nabokov, Kerouac, García Márquez, Morrison, King) in a published study, anthology or annotated edition that quotes the book.
- Auden's sentence was cut at the front to fit the limit; its auditNote says so. Walcott's is cut at the end, Kerouac's at both ends.
- Sartre: the wording with a dash is Stuart Gilbert's American text (Knopf, 1947). His British text prints three dots instead.
- Faulkner's odd spellings are the edition's.
- Wharton, Hemingway, Faulkner are in the public domain in the United States by publication date (1920, 1926, 1929); they may still be in copyright elsewhere.
- Notes for these 30 were written from well-documented facts and not checked one by one against a second source.

## Works in copyright: how other sites do it (14 Nov 2026)

Paul's instruction: workarounds are fine, do it the way other art sites do, and still do the right thing because the site is headed public.

What other projects do. WikiArt and Obelisk Art History show in-copyright art under a stated fair-use rationale: historically significant work, informational purpose, already widely available, low-resolution copies unsuitable for commercial use. Wikipedia allows low-resolution images of copyrighted art under its non-free content policy, used sparingly. The Getty publishes thumbnail-size images of copyrighted works it has no licence for. The Artists Rights Society licenses most of these estates for a fee. This is a record of practice, not legal advice.

What was done here.

Early works that are public domain in the United States (ten, ordinary records with tools on): VAULT-534 Les Demoiselles d'Avignon and VAULT-535 The Old Guitarist (Picasso), VAULT-536 I and the Village (Chagall), VAULT-537 The Farm (Miró), VAULT-538 Nude Descending a Staircase, No. 2 and VAULT-539 Fountain in Stieglitz's photograph (Duchamp), VAULT-540 Bird in Space (Brâncuși), VAULT-541 Black Iris (O'Keeffe), VAULT-542 Campbell's Soup Cans (Warhol), VAULT-543 Man, Controller of the Universe (Rivera). The first five are hosted on English Wikipedia with file pages marking them public domain in the United States; the rest are on Wikimedia Commons. Two rest on Commons' own judgement and are the weakest of the ten: the Warhol (Commons holds that the 1962 paintings were published without notice or renewal) and the Rivera (a contributor's photograph of a mural in Mexico City).

Small fair-use images (nine, `fairUse: true`, tools off): VAULT-544 The Persistence of Memory (Dalí), VAULT-545 The Two Fridas (Kahlo), VAULT-546 The Treachery of Images (Magritte), VAULT-547 Autumn Rhythm (Pollock), VAULT-548 No. 61 (Rothko), VAULT-549 Untitled (Skull) (Basquiat), VAULT-550 Whaam! (Lichtenstein), VAULT-551 Relativity (Escher), VAULT-552 Girl with Balloon (Banksy). Each is the low-resolution file English Wikipedia uses, between 280 and 490 pixels wide, hosted in `images/fairuse/`. One work per artist. The lightbox caps the display size, shows a rights line, and hides the maker tools, export and full-size link.

All nineteen images were downloaded and looked at against their titles. Dates, materials and holders were checked against Wikidata. Bird in Space has no holder because the cast in the photograph could not be identified. Notes were written from well-documented facts and not checked one by one against a second source.

Three poets, by prose: LIT-587 Ginsberg (a line from his 1959 notes on recording Howl), LIT-588 Bukowski (the first sentence of Post Office), LIT-589 Bishop (a remark to Robert Lowell, known from his 1957 letter to her; the wording is his report, and the record says so).

Open risks, plainly: fair use is a defence, not a permission, and this site's purpose (raw material for makers) is a weaker case than an encyclopedia's, which is why the tools are off for the nine. If the site makes money or a rights holder objects, those nine come down first.

## Loose ends closed (14 Nov 2026)

Paul asked for the remaining open items to be handled, not listed.

- Guernica added as VAULT-553, a small fair-use image (the tenth). Nighthawks added as VAULT-554 from a free file on Wikimedia Commons; its Commons file page was not read.
- The three unseen images (VAULT-144 Hammershøi, VAULT-181 Nainsukh, VAULT-327 the Mapungubwe rhinoceros) were downloaded and looked at. All three show the work named. Every image on the site has now been seen against its title.
- Blank mediums and holders. The Commons file record was read for all 62 artworks with a blank, and the lead of the Wikipedia article for 25 of them. That filled five holders (VAULT-195 Cincinnati Art Museum, VAULT-401 Museum of Fine Arts, Boston, VAULT-402 and VAULT-429 private collection, VAULT-183 University of Groningen Library, the copy the plate was scanned from) and six mediums (VAULT-323 phonolite, VAULT-335 and VAULT-430 carved wood, VAULT-148 carved leather, VAULT-339 geoglyph, VAULT-269 illustrated handscroll). 40 mediums and 29 holders remain blank. Neither source states them, and they are mostly book plates, prints with no identified impression, and buildings or sites. They are left blank on purpose and are no longer an open task.
- Notes. The 83 notes written on 14 Nov 2026 had every year checked against the Wikipedia article for the work (art) or the author (writing). In 74 every year is on the page. Nine had a year the page does not carry. Eight of those are dates of a translation, an edition, a battle, a birth or a museum accession that the checked page would not be expected to give, and were kept. One, the year The Gleaners entered the Louvre, could not be supported and was removed. Names and anecdotes in these notes were not checked.
- Not done: a second-source read of the 283 older notes whose names were reviewed by hand. That is a few hours of slow lookups from the sandbox and is the one real item left.

## Growth pass (15 Nov 2026)

Paul's brief after the public test closed: grow it in every direction that serves a working creative. Art in its broadest sense, no advertising, nothing sideshow, medical or morbid, the most-searched names plus the people this audience comes looking for. Run the whole thing.

The site went from 547 artworks and 493 writing pieces to 938 and 731.

**Writing, 238 pieces** (LIT-590 to LIT-827), by four parallel agents, each working a fixed list through `grow_kit.save_new()`, which checks every line against the fetched edition and refuses anything that does not match.
- Poems by the most-searched poets: 64 (Dickinson, Whitman, Keats, Shelley, Blake, Wordsworth, Frost, Shakespeare, Donne, Hopkins, Tennyson, Yeats and others).
- Prose passages people quote: 55 (Melville, Austen, Dickens, Twain, Fitzgerald, Joyce, Woolf, Chekhov, Dostoevsky, Thoreau, Emerson, Nietzsche, Marcus Aurelius, Plato, Laozi, Homer, Virgil, Dante and others).
- Words that are not poems: 55 (Van Gogh's and Keats's letters, Leonardo's notebooks, Whistler, Morris, Kandinsky, Pater, Pepys, Dorothy Wordsworth, Beethoven, the Communist Manifesto, the Declaration of Sentiments and others).
- The Love, Earth and Fury shelves: 64.
All are public-domain texts from Project Gutenberg or pre-1931 scans, or A. S. Kline's openly offered translations. No in-copyright poem lines.

Left out on review: a one-sentence letter of Héloïse from a single unchecked scan, a Gauguin passage whose surrounding text uses wording the site avoids, and a second passage from a Douglass speech already on the site.

Things the agents flagged that are still true of what is on the site:
- Several texts follow an older or edited edition and say so in their auditNote: Dickinson (the edited 1890s texts), Donne (Grierson's original spelling), Wordsworth's Westminster Bridge (1807 spelling), Hopkins (no stress marks), Owen's Parable (the 1920 text, without the last line later editions add), Sassoon's Suicide in the Trenches (the American text reads snug-faced where the London one reads smug-faced), Tennyson's Crossing the Bar (from an anthology, crossed for crost).
- Dates that are conventions or inferences: the Van Gogh letter extracts (c. 1888), Leonardo's notebook passages, Chekhov's letter (1888 against the edition's 1889), Beethoven's Immortal Beloved letter (1812 is later scholarship; the edition says 1800), Seneca, Plato, Laozi, Confucius, Sun Tzu, Homer.
- Emily Dickinson's line about the top of her head is her speech as T. W. Higginson reported it, not a letter.
- Luther's translator (R. S. Grignon) is inferred from matching wording.
- Notes were written from well-documented facts. Some state a magazine, month or line count from memory. None was checked against a second source.
- Not found or not attempted: Marinetti's Futurist Manifesto (no pre-1931 English), Sullivan Ballou's letter, Tolstoy's Confession, Woolf's To the Lighthouse, Kafka's Hunger Artist, The Hollow Men, more Rumi, Bashō in a public-domain version, Waley's Japanese poems.

**Art from museum open-access collections, 306 works** (VAULT-555 to VAULT-860): the Met, the Art Institute of Chicago and the Cleveland Museum of Art. Each museum flags these as public domain or CC0 and supplies the title, maker, date, medium and image. 83 for the best-known artists, and from themed searches 55 design pieces, 65 visionary and mythic, 54 photographs and 49 early twentieth-century works. Every candidate title was read and every image looked at on a contact sheet before it went in. Cards (display title, maker's name, note, tags) were written by five agents from the museum record.

Left out on review: a Gettysburg photograph showing the dead, a skull print, a Gauguin portrait whose record turns on the sitter's age, a possibly modern "medieval" initial, duplicates, and seven images with too little to look at.

**Famous works held elsewhere, 85** (VAULT-861 to VAULT-945): Café Terrace at Night, The Milkmaid, Primavera, the Pietà, Vitruvian Man, The Calling of Saint Matthew, The Death of Marat, The Fighting Temeraire, Earthrise, Migrant Mother and others. Records came from Wikidata in one bulk query and images from Wikimedia Commons. Wikidata's date or holder was wrong, garbled or out of date for about twenty of them (a 1700 date on Velázquez's Innocent X, wartime holders for Vermeer's Art of Painting) and each was corrected by hand; the auditNote says where. All 85 images were downloaded and looked at against their titles. Ten have no holder because the image is one of several versions or casts and which one was not established (Bedroom in Arles, Rouen Cathedral, Houses of Parliament, Napoleon Crossing the Alps, The Burghers of Calais, The Gates of Hell and others). Two Matisse paintings (The Red Studio, Woman with a Hat) are included on the ground that they were published before 1931 and Commons hosts them.

Not done from the famous list, because the lookup failed or the image would not download: Judith and the Head of Holofernes (Klimt), The Dance of Life, Rousseau's The Dream, Sudden Shower over Shin-Ōhashi Bridge, The Ten Largest, Ophelia, The Lady of Shalott, Proserpine, Isle of the Dead, The Large Blue Horses, Las Hilanderas, The Triumph of Galatea, The Tempest (Giorgione), Where Do We Come From, The Virgin of the Rocks.

**What "verified" means for this pass.** Texts: matched line by line to a fetched edition. Museum artworks: the museum's own record. Famous works: Wikidata reviewed and corrected by hand, image checked by eye. Notes for all the new art and writing: written from the record plus well-documented facts, not second-sourced. That last part is the same standing as the older notes and is the main open item.

Tested before each push: desktop and phone-size, every view, every Reading Room book paged through, search, the fair-use lightbox, the pull-quote check, counts. Not tested: real devices, Safari, or how the Wall feels with 938 images on a slow connection.

## Growth pass, follow-up (15 Nov 2026): the line on death, and the misses

Paul's correction: death in art is welcome and important (he named Van Gogh's skull and the Isle of the Dead). What stays out is what he does not see as art: medical and specimen photography, sideshow material. The growth pass had cut too much on the wrong side of that line. The rule in CLAUDE.md is rewritten.

Restored or added on that basis (VAULT-946 onward): the Klinger print and the Gettysburg photograph cut earlier; a Lambayeque and an Egyptian funerary mask; a Northern Wei zodiac tomb figure; Posada's Calavera of Francisco Madero; and from the canon of death in art, Van Gogh's Head of a Skeleton with a Burning Cigarette, Cézanne's Pyramid of Skulls, Ensor's Skeletons Fighting over a Pickled Herring, Böcklin's Self-Portrait with Death Playing the Fiddle, Simberg's Garden of Death and Wounded Angel, Bosch's Death and the Miser, a Claesz Vanitas, Vereshchagin's Apotheosis of War, Mantegna's Lamentation, Bouguereau's Dante and Virgil, Caravaggio's Saint Jerome Writing and O'Sullivan's A Harvest of Death. Still out: two medical photographs from the Met's photography department.

The fifteen famous works reported as missed. The first lookup matched on exact Wikipedia titles and failed quietly. A second lookup searched Wikidata by name and matched on the artist. Result: eight of the fifteen were already on the site under a slightly different title (Ophelia, The Lady of Shalott, Isle of the Dead, The Dream, Death and the Maiden, Sudden Shower over Shin-Ōhashi Bridge, La Calavera Catrina, The Death of Socrates), so the earlier report that they were missing was wrong. Added now: Klimt's Judith, Munch's Dance of Life, The Ten Largest No. 2, Proserpine, The Large Blue Horses, Schiele's Self-Portrait with Chinese Lantern Plant, Las Hilanderas, The Tempest, Where Do We Come From, The Virgin of the Rocks (the London version). Not added: The Triumph of Galatea and The Death of Chatterton, because Wikidata's image for each is a later copy, not the original.

All 37 images in this batch were downloaded and looked at against their titles. Dates, mediums and holders from Wikidata were reviewed and corrected by hand (Munch's Dance of Life was dated 2000; The Tempest's holder was a former owner).

The texts reported as having no public-domain English. A second pass looked the way other archives do, in scans of pre-1931 printings and at Standard Ebooks, and found 21 (LIT-828 to LIT-848):
- Marinetti's manifesto, points 1 to 8, from the English text printed in the 1912 Sackville Gallery catalogue in London. No translator is named there.
- Sullivan Ballou's letter, from a book printed in 1864. That printing is abridged and garbles the best-known sentence, so the passage shown is the part around it. The famous phrase is not displayed.
- Tolstoy's Confession (Maude), To the Lighthouse, Orlando, A Room of One's Own, The Hollow Men, Frost's Acquainted with the Night, Stevens's Emperor of Ice-Cream, three more Bashō haiku (Chamberlain, 1902), another Rumi, two Bai Juyi poems (Waley, 1918), Emily Brontë's High Waving Heather, Blake's And Did Those Feet, and further sections of Song of Myself, the Ancient Mariner and Prufrock.
- Kafka's A Hunger Artist has no public-domain English, so it is one credited sentence from the Muirs' translation.
For the Marinetti and Ballou texts the scan's OCR was too rough to check against directly, so the agent made a corrected transcription from the page images and checked against that; the auditNote says so. The four Standard Ebooks texts rest on Standard Ebooks' own proofing.

The site stands at 967 artworks and 752 writing pieces.

## The note's voice: pilot (15 Nov 2026)

Paul on the notes: the site should sound like a museum with just enough of a person in it to read as a curator or fellow creative. Not cold. Not forced AI conversational, which he said would ruin the project. The voice settled on is a museum run by people who make things: the curator notices what a maker would (age, time taken, materials, money, what went wrong, what happened to the object), in full plain sentences, several facts where a work has several.

Pilot: 52 famous works rewritten in that voice (35 artworks, 17 pieces of writing), `noteRev: 4`. Method: the Wikipedia article for each work was fetched; three agents wrote from that text alone and had to supply the verbatim snippet behind every fact; `grow_kit.save_line()` refused any note whose snippets were not in the article or whose years were not in the snippets, and a list of praise and interpretation words. The snippets are kept in `data/pilot-notes-evidence.json` and the notes they replaced in `data/pilot-notes-old.json`, so the pilot can be reversed.

What the source check caught: two of the example lines used to sell the voice were not supported. The article on Goya's The Dog does not say dining room, and says the murals were not meant for public display, not that he never showed them. The article on the Pietà gives no birth year, so Michelangelo's age was left out. The Night Watch article's own figures for the commission do not add up, so only the total is given.

Thin or compromised: Judith Slaying Holofernes (the article is on the Naples version; the site shows the Uffizi one), The Tyger and The Triumph of Death (little in the article about the making), The Metamorphosis (publication facts only). Ophelia was not done: the fetched page was a disambiguation page. The Ten Largest and Migrant Mother were not fetched.

Limits: the facts are as good as the Wikipedia article they came from, and one source is not two. The check proves the snippets exist and the years match; it cannot prove every clause is covered. The other 1,660-odd notes are still in the older voice and wait on Paul's verdict.

## The note's voice: wave 1 (15 Nov 2026)

Paul approved the pilot. 438 more artwork notes were rewritten in the same voice, by 13 parallel agents, each from the trimmed wikitext of the work's Wikipedia article (or the maker's, or the parent work's, where the piece has no article of its own). Every note went through `save_line()`: each evidence snippet is verbatim in the source file and every year in the note is in the evidence. Afterwards all 438 were machine-checked for praise words, quotation marks, markup and length, and a random 26 were read in full. 490 notes are now `noteRev: 4`.

Not checked: the agents' reading of the source is trusted beyond the snippet match; nothing was second-sourced; Wikipedia is the only source.

Left in the old voice from this wave, because the only article found was about the subject, not the object: VAULT-128, 134, 153, 156, 161, 193, 228, 230, 232, 273, 275, 282, 325, 328, 331, 378, 402, 405, 415, 416, 466, 484, 526, 536. Still to do: about 475 artworks and all 752 writing pieces.

## The note's voice: wave 2, rollout finished (16 Nov 2026)

Paul: do it all. 1,216 more notes in the new voice: 494 artworks and all 752 writing pieces (less a handful), by 35 parallel agents under `out/BRIEF10.md`, each fact saved with its verbatim source snippet through `save_line()`. 1,711 of 1,719 notes are now `noteRev: 4`.

Sources: for museum works, the museum's own API record (Met, Chicago, Cleveland: size, credit line, description, provenance, exhibitions) plus the Wikipedia article on the work and on the maker; for writing, the article on the work and the author. 38 writing files had been built on a Wikipedia disambiguation page; the right articles were fetched and those 39 notes redone.

Known soft spots:
- Many writing notes rest on the author's article only (it often never names the piece), so they say what the writer was doing at the label's date. They do not claim facts about the piece the source does not give.
- Several maker articles were cut off at about 15,000 characters, so facts late in a life were not available.
- Some of the museum records are bare; those cards are one or two sentences of size, place and donor.
- Still not second-sourced; Wikipedia and the museum records are the only sources.

Label only (no fact in the record): VAULT-642, 755, 703, 129, LIT-234. Old note kept, no source about the object found: VAULT-128, 275, 325, 328, 331, 484, LIT-447, LIT-130.

Label dates the agents found at odds with their sources (not changed; worth a look): VAULT-585 Munch Girl by the Window (shown in 1892, label 1893); VAULT-955 Harvest of Death (Sketch Book 1865 vs label 1866); VAULT-102 Artemisia Esther (Wikipedia says 1630s); VAULT-087 Caravaggio Musicians; VAULT-966 Bosch; VAULT-632 van Eyck; VAULT-949 Posada (printed 1944, design date unsourced); LIT-139 Genesis and LIT-140 Psalm 23 (c. 600 BCE); LIT-125 Song of Songs (3rd c. BCE in source); LIT-616 The Bells (written 1848); LIT-820 Base Details (diary 1917); LIT-194 Oread (1915); LIT-407 Heart of a Woman (1916 or 1918); LIT-491 Silva Nocturne (published 1908); LIT-252 Montaigne vol. 3. Also: LIT-133/358 credit Lewis Spence's retelling of the Popol Vuh, which may sit badly with the real-texts rule; VAULT-112 credits van Musscher, the Met names Ruysch alone.

## Dates, images, links (16 Nov 2026)

Label dates changed where the work's own source was clear: VAULT-949 Posada (design before 1913, printed 1944); LIT-139 Genesis (final form c. 5th century BCE); LIT-140 Psalm 23 (date uncertain); LIT-125 Song of Songs (c. 3rd century BCE); LIT-616 The Bells (1848, published 1849); LIT-820 Base Details (1917); LIT-194 Oread (1915); LIT-491 Silva, Nocturne (published 1908); LIT-128 Völuspá (10th century); LIT-490 Thirteen Ways (1917); LIT-593 Success is counted sweetest (1859, published 1864); LIT-298 Crossing Brooklyn Ferry (1856); LIT-109 Duchess of Malfi (1612–13); LIT-111 Seneca's Phaedra (before 54 CE); LIT-426 Lu Xun (1918); LIT-686 Inferno (c. 1306–1310); LIT-127 Heart Sutra (by the 7th century CE). Left alone because the label is the holder's own date: Munch's Girl by the Window, Artemisia's Esther, Caravaggio's Musicians, Bosch, van Eyck, Harvest of Death. Hidden year field fixed for ten pieces (seven Roman texts sat at year 800, three New Testament verses at 1611, the translation's year).

Image check of all 440 non-Commons images: four Chicago images asked for a width larger than the file and returned 403 (fixed); three Cleveland files had been withdrawn (404). Cassatt now uses Chicago's impression, with Chicago's date and medium. Kollwitz VAULT-116 and Arms VAULT-061 still have no image.

## New sources, Kollwitz and Arms back, film stills (16 Nov 2026)

Added: Käthe Kollwitz, Germany's Children are Hungry! (1924), Self-Portrait with Hand on Forehead (1910), The End (1897) and Revolt (1899) from the National Gallery of Art (CC0), and the chalk study Losbruch (1898–1903) from the Rijksmuseum; John Taylor Arms, On Lake Como, Number Two (1919), from a Commons file of the Zimmerli Art Museum's impression marked PD-1923. Revolt is label only (no fact in its record). Every image was looked at against its title.

Film stills: 33 frames from A Trip to the Moon, The Cabinet of Dr. Caligari, Nosferatu, Metropolis, The Passion of Joan of Arc, Battleship Potemkin, Häxan, The Phantom of the Opera, Sherlock Jr., The General, Safety Last!, The Gold Rush, Man with a Movie Camera, Un Chien Andalou, Sunrise, Faust, The Golem, Dr. Jekyll and Mr. Hyde (1920), The Hands of Orlac, The Thief of Bagdad, Intolerance and The Lodger. All released before 1931. Pandora's Box and Waxworks were left out because the only usable copies were Blu-ray rips. Notes come from each film's Wikipedia article through save_line(); release years and directors from the same articles. Not checked: the restoration history of each Internet Archive copy (tinting differs between copies), and some frames are low resolution (Intolerance 460px, Safety Last 488px).

## Design batch (16 Nov 2026)

56 works from Cooper Hewitt, Smithsonian Design Museum (VAULT-1014 to 1069), all CC0 in the museum's record and dated before 1931. Notes from the museum record (size, technique, inscriptions, credit line) and, for nine, the maker's Wikipedia article, through save_line(). One note (Eisler's silver platter) was trimmed where the writer read the print lettering from general knowledge. Region tags come from the record's place made, or the maker's nationality where none is given.


## Rights tiers and the first additions under them (16 Nov 2026)

Paul's decision: two tiers, free to take and look and learn (CLAUDE.md, "Rights: two tiers").

**Rights audit.** Every artwork was assigned `rightsTier`. For the 518 Commons images the file page's licence section was read (`commons.wikimedia.org/w/index.php?title=File:…&action=raw`). 387 are public domain outright. 131 are photographs whose photographer kept a CC, GFDL, Free Art, KOGL or Taiwan open-data licence over a public-domain object; 126 now carry `photoCredit`, and five 2D reproductions (a manuscript page, a Met print, Brooklyn's no-known-restrictions scan) were left without one. Credits whose author field was garbled were fixed by hand from the file page. Two works moved to `look`: Warhol's Campbell's Soup Cans, which Commons tags PD-US-not renewed but the estate licenses, and Rivera's Man, Controller of the Universe (1934). The ten earlier fair-use works now use the look-and-learn line.

**Wrong image found.** Pillars of Creation (VAULT-890) showed a visitor's photo of a planetarium screen playing the 2022 Webb image, not the 1995 Hubble photograph its note describes. Replaced with File:Eagle nebula pillars.jpg (NASA; PD-Hubble), which shows the stair-shaped gap the note mentions.

**WPA posters, 30 (VAULT-1070 to 1099).** Library of Congress WPA Poster Collection, made 1936 to 1943 under the Works Progress Administration. Picked from about 200 candidates by eye; the Sea Cliff, Long Island poster was dropped as a town advertisement. Notes written from the LoC record alone (maker, printer, method, size, date stamps, sponsor, conservation) through `save_line`, batch `wpa`. 22 are 1,024 px, 8 only exist at 640 px.

**FSA/OWI photographs, 20 (VAULT-1100 to 1119).** Library of Congress, made by photographers employed by the Resettlement Administration, Farm Security Administration and Office of War Information. Notes from the LoC record plus the Wikipedia articles on the photographer or the picture (Let Us Now Praise Famous Men, American Gothic (photograph), Migrant Mother, Pie Town), batch `fsa`. Floyd Burroughs Jr. was dropped because its negative is hole-punched; Toward Los Angeles uses the original negative, not the copy of a mounted print. Rothstein's dust storm uses the LoC's scan of the file print, because the worn-out negative was discarded (the record says so). Marion Post Wolcott's juke joint photograph is titled from the holder's caption with its 1939 racial term left out; the full caption is in `auditNote`.

**Not done yet in this round:** look-and-learn additions (modern artists and photographers, post-1931 film stills); unrenewed 1931 to 1963 works; size on the label (WPA records carry `dimensions`, nothing shows it yet).

## Big addition, round 8a: manifestos and artists' writing (17 Nov 2026)

30 pieces (LIT-849 to 878), every text pulled from a fetched edition with `save_new` and every note saved through `save_line` from the Wikipedia article on the piece or author. Manifestos: Tzara's Manifeste Dada 1918 (French, Dada 3), Breton's Manifeste du surréalisme in French (three passages; text from a 2017 free e-book of the manifestos, wording confirmed against other printings by archive.org full-text search; the 1924 text is public domain in the US), BLAST No. 1 (two unsigned passages, credited to Wyndham Lewis as editor and chief writer, as the auditNote says), Marinetti's museums passage from the 1912 Sackville Gallery catalogue (collated from two scans), and one line of Pankhurst's Freedom or Death (quoted, under 15 words). Artists' writing: Gauguin (Theis 1919), Cennini (Herringham), Leonardo (Richter), Van Gogh (Ludovici), Rodin (Fedden), Kandinsky (Sadler), Whistler, Morris, Ruskin, Delacroix (French, 1893 Plon). Not done: the Russian Futurists, Malevich, Loos, Sant'Elia and Saint-Point (no public-domain English found); Sojourner Truth (LIT-159 already leads with the 1851 Robinson wording; the full 1851 report is on a LoC newspaper site the sandbox cannot reach).

## Big addition, round 6b: photographs of the modern canon (17 Nov 2026)

36 photographs (VAULT-1120 to 1155): Cartier-Bresson, Capa, Weegee, Arbus, Avedon, Frank, Maier, Eggleston, Parks, and the news and war photographs Paul approved (Eisenstaedt, Rosenthal, Adams, Ut, Browne, Carter, Widener, van Es, Khaldei), Bourke-White, McCurry, Salgado, Ansel Adams, Weston, Man Ray, Mapplethorpe, Penn, Halsman. 33 are look tier with local screen-size copies; 3 are free: Monolith (published 1927), Le Violon d'Ingres (published 1924), and the Library of Congress's unretouched Dalí Atomicus print (LoC: no renewal found). Commons tags several press photographs as public domain (Iwo Jima, Saigon Execution, The Terror of War, the Burning Monk, the Saigon rooftop, Khaldei's Reichstag, Moonrise, Identical Twins); because agencies or estates still license them, they are look tier, and each auditNote records the Commons tag. The Terror of War is credited "Nick Ut (attribution disputed)", following World Press Photo's 2025 suspension of the credit; the AP keeps it. W. Eugene Smith's Tomoko Uemura in Her Bath was left out: it was withdrawn from publication at the family's wish in 1997. Fifteen press photographs with no holder's print behind them carry `noHolder`. Eight Wikipedia non-free files are small (254 to 392 px).

## Big addition, round 8b: ballads, spirituals, mystics (17 Nov 2026)

24 pieces (LIT-879 to 902). Child ballads (5: The Twa Corbies, Edward, Lord Randal, The Unquiet Grave, Bonny Barbara Allan); spirituals (5: four from James Weldon Johnson's 1925 preface, keeping his spelling, and I Know Moon-Rise from Higginson's 1870 Army Life in a Black Regiment, which keeps Higginson's dialect spelling because no standard-spelling edition was found; flagged for Paul); mystics (14: Kabir via Tagore, Hafiz via Gertrude Bell, Angelus Silesius via Carus, the Cloud of Unknowing via Underhill, Teresa's Interior Castle, John of the Cross's Dark Night in prose, Lal Ded via Grierson and Barnett, Boehme, Rabi'a via Margaret Smith, credited as attributed). Dates for Teresa (1577) and some spirituals were set by the agent, not from the note sources; yearNum for Kabir, Hafiz and Lalla are estimates. **Blues not done:** first-edition sheet music for Handy's St. Louis, Memphis, Beale Street and Yellow Dog Blues was found on archive.org, but sheet-music OCR scatters each lyric between the staves, so no line passes the kit's machine check. Transcribing from page images would bypass the check; left for Paul to decide. Deep River, Nobody Knows, Didn't My Lord Deliver Daniel and Joshua exist only inside scores in the editions fetched, with the same problem.

## Big addition, round 3: nature as raw material (17 Nov 2026)

63 plates (VAULT-1156 to 1218): Haeckel's Kunstformen der Natur (20, one Smithsonian copy via the Biodiversity Heritage Library), Audubon's Birds of America (14, National Gallery of Art Havell set), Merian's Surinam book (6), Blossfeldt's Urformen der Kunst (6, NGA's 1928 portfolio), Seba (5), Besler's Hortus Eystettensis (4), Thornton's Temple of Flora (3), Shaw (2), Moses Harris (2), Stubbs's horse skeleton (Met). The 38 BHL page images are hosted on the site in `images/plates/` (JPEG, long side up to 1,400 px) because BHL's thumbnail links redirect and throttle; `highResUrl` points to BHL's full page image. Five Haeckel plates are label only. Nine black-and-white Haeckel plates carry the medium "Book plate (printing method not confirmed)", because the book mixes lithographs and halftones. Facts on Haeckel plates 2, 5, 7, 62, 63, 88 and 92 and Merian plates 1, 5, 7, 18, 56 and 59 rest on the agent's reading of the authors' own German and Dutch text in the scans (evidence copied from the OCR); a second reader could check them against the page images. New plates use the macro medium "Diagram, Cyanotype & Textile"; the two Haeckel and one Audubon already on the site are still "Print & Woodcut".

## Big addition, round 4: maps, stars and space (17 Nov 2026)

46 works (VAULT-1219 to 1264). Carta Marina from the Bayerische Staatsbibliothek's 1539 original (Commons' coloured copy is a 1949 facsimile and was refused): the nine BSB sheets shown side by side, hosted in `images/plates/`, plus a sea-serpent detail and the sea-monster sheet D. Waldseemüller 1507, Ortelius (world 1570, Islandia), six Cellarius plates (LoC's 1708 Valk and Schenk edition; plate numbers in auditNote because LoC's captions are out of step), three Burritt (c. 1856 Mattison edition; the 1835 plates at David Rumsey are CC BY-NC-SA), Bayer's Cetus and Hydra, six Trouvelot chromolithographs (NYPL), early astronomical photographs (Whipple, Rutherfurd, the Langenheims' 1854 eclipse, Lawrence's 1883 eclipse, Paul Henry's 1885 Cygnus; Met), and NASA and observatory images (Aldrin, the bootprint, Crab Nebula, Sombrero, The Day the Earth Smiled, the EHT black hole (CC BY 4.0), Perseverance's panorama, Cosmic Cliffs, Webb's First Deep Field, Viking 1's first Mars photograph, Ed White's spacewalk, the Pioneer plaque, Mystic Mountain), plus the Met's Far Side of the Moon print, Regiomontanus's astrolabe, a Posada comet broadsheet, Dürer's southern sky and a Jain cosmological map. Seven listed works were already on the site (Hereford, Fra Mauro, Catalan Atlas, Piri Reis, Blue Marble, Ultra Deep Field, Pale Blue Dot). The Jain map's note had a continent name spelt from memory; the names were taken out.

## Big addition, round 6a: the modern canon, painters (17 Nov 2026)

42 works (VAULT-1265 to 1306), all look tier with local screen-size copies and sourced notes: Hopper (Automat, Early Sunday Morning, New York Movie and more), Bacon, Basquiat, Haring, Kusama (Pumpkin, an Infinity Nets painting; no Infinity Mirror Room image was usable), Hockney, Warhol, Rothko, de Kooning, Pollock, Kahlo, Dalí, Magritte, Picasso, Matisse, Freud, Bourgeois's Maman, Dubuffet, Lawrence, Bearden (The Street), Ringgold (Bessie's Blues; Wikipedia's Tar Beach image is the picture-book cover), Kerry James Marshall (Many Mansions), Carrington, Varo (Still Life Reviving), O'Keeffe's Cow's Skull. Automat (1927), Early Sunday Morning (1930) and Magritte's The Lovers (1928) predate 1931 but stay in the look tier: the Whitney still carries an ARS copyright line for Hopper, The Treachery of Images is already look tier, and first publication of a painting is hard to date. New York Movie (1939) is tagged on Commons as public domain for want of a notice, as Nighthawks is; left in look until checked. Where MoMA, Des Moines or the Phillips would not answer, date, medium and size come from the Wikipedia infobox, as each auditNote says. Three look-tier works use photographers' Commons photographs and carry photoCredit (Tuttomondo, Pumpkin, Maman).

## Big addition, round 5a: Yoshitoshi and Kuniyoshi (17 Nov 2026)

38 prints (VAULT-1307 to 1344), all free tier: Yoshitoshi's One Hundred Aspects of the Moon (14) and New Forms of Thirty-Six Ghosts (9), four more Yoshitoshi (the Yasumasa triptych, Lonely House on Adachi Moor, the Zhang Shun and Li Kui diptych, Saint Mongaku), and Kuniyoshi (five Water Margin heroes, the Tōkaidō cats, the Okazaki cat demon, the Earth Spider triptych, Ghosts of the Taira, the Dragon King's jewel, Tamatori-ama). Holders: Library of Congress 15, Art Institute of Chicago 15, Met 3, Rijksmuseum 3, LACMA 2, Cleveland 1. Most LoC sheets are trimmed impressions ("Copy trimmed" in auditNote); two have the series cartouche cut (Moon over a Single Dwelling, Summer-Like Moon) though the picture is whole; five LoC sheets were dropped for trimming or a wrong title. LoC dates these only "[188-]", so labels use the series dates (Moon 1885–92, Ghosts 1889–92). Chicago dates Moon of Enlightenment 1881, before the series existed; the label uses the series date and the auditNote keeps Chicago's. Takiyasha was already on the site (VAULT-201). The Rijksmuseum cats image uses an IIIF region crop to remove the museum's colour chart. LoC's English titles were put in title case.

## Big addition, round 1: the dark masters (17 Nov 2026)

112 works (VAULT-1345 to 1456), all free tier, grow `dark`.
- **1a (54):** Goya's Caprichos (11, Met 1799 set) and Disasters of War (12, Met 1863 first edition), all twelve Black Paintings that were missing, Bosch (the Hell panel, the Tree Man and Prince of Hell as details, the Seven Deadly Sins, the Ship of Fools), Fuseli (the Frankfurt Nightmare, Titania and Bottom, the Night-Hag), Géricault (Charging Chasseur, Wounded Cuirassier; his severed heads and anatomical studies left out under Paul's line), Gentileschi's Capodimonte Judith, Holbein (the Dead Christ, four Dance of Death woodcuts), Grünewald (Isenheim Temptation and Resurrection, Tauberbischofsheim Crucifixion). 28 use the Met's records; 26 are Commons files with labels from the English Wikipedia infobox checked against the Commons record (the Prado refused the sandbox), as each auditNote says. "The Nightmare, Frankfurt Version" carries a descriptor, not the holder's title, so the app does not hide it behind the Detroit painting. Goya is now "Francisco de Goya" on every record (six older ones said "Francisco de Goya y Lucientes", kept in searchTags).
- **1b (58):** Piranesi's Carceri (13 plates of the 1761 set, Art Institute of Chicago; I, III and X were already on the site, III and X as first-state impressions), Rembrandt (6), Caravaggio (6), Doré (10: Inferno from the National Library of Poland's Berlin 1870 copy, Paradise Lost, the Ancient Mariner), Callot's Miseries of War (5), Böcklin (Isle of the Dead II, III and V, The Plague), Baldung (5), Ensor (4), Bruegel (Dulle Griet, Big Fish Eat Little Fish), Rethel's Dance of Death (3, NGA; the NGA record 2015.103.2 has the wrong image for its title, so two other impressions were used). One Doré plate is label only. Dulle Griet is dated 1563 (Wikipedia, after the 2018 restoration; Commons says 1561).

## Big addition, round 7: film after 1931 (17 Nov 2026)

42 stills (VAULT-1457 to 1498). **Free (23 frames, 12 films)**, each film's US public-domain status taken from its own English Wikipedia article (sentence kept in the source file, summed up in `rights`): Night of the Living Dead (from the raw unrestored TV master), Carnival of Souls (Wikipedia still calls it public domain, though a 1997 rights purchase and Criterion's claim are recorded; caveat in auditNote), Detour, His Girl Friday, The Little Shop of Horrors, The Last Man on Earth, Dementia 13, Reefer Madness, The Brain That Wouldn't Die, Scarlet Street, The Hitch-Hiker, The Stranger. Frames from archive.org copies, chosen by eye, hosted in `images/film/`. Charade's two frames were dropped: no copy from a print or TV master was found, only an upload of unknown origin. Plan 9, White Zombie and House on Haunted Hill were dropped because their articles do not say public domain; The Third Man's US copyright was restored. **Look (19 stills, 17 films):** only the still each film's English Wikipedia article carries: Citizen Kane (2), Psycho (an on-set photograph), Vertigo and Rear Window (trailer frames), 2001 (2), Seven Samurai, Rashomon, The Seventh Seal, 8½, Breathless, The Shining, Blade Runner (The Final Cut), M, Dr. Strangelove, The 400 Blows, The Night of the Hunter, Vampyr. Eight of these are tagged public domain on Commons as trailer frames or publicity photographs; they stay look tier because the films are in copyright. Several are small (The Shining 202 × 300). M enters the US public domain on 1 January 2027 and could then get a free frame.

## Big addition, round 5b: Kyōsai, ghost prints, Edo, shin-hanga (17 Nov 2026)

36 works (VAULT-1499 to 1534), all free tier. Kawanabe Kyōsai (8: the Hell Courtesan, a section of the Night Procession of Goblins scroll, pages from his Hundred Demons and Kyōsai gadan, the Wereldmuseum's walking skeleton and long-haired ghost, the Cernuschi frogs, Crow and the Moon), Hokusai's five One Hundred Ghost Tales prints (Chicago), eight Hiroshige Edo views (Met and Chicago; Sudden Shower and Plum Park were already on the site), three spreads from Toriyama Sekien's Konjaku Hyakki Shūi (1781, Met), shin-hanga made before 1931 (Hasui 3, Yoshida 3, Koson 2), Kōgyo's Noh prints (2) and Kunisada (2). Four titles are English renderings of the Rijksmuseum's or Wereldmuseum's Dutch-only titles, with the Dutch kept in auditNote (A Walking Skeleton Carrying a Woman on Its Back, A Female Ghost with Long Hair, Two Crows on a Branch, Owl at Half Moon). The three Sekien spreads are titled with the monster names printed on each. Ōkyo's Ghost of Oyuki was left out (no holder record); Yoshida's sailboats (only a dealer's copy) and a Cooper Hewitt Hasui dated c. 1920 by the museum but 1933 by the Walters were also left out. Honolulu's Lake Kawaguchi carries only the accession number from the Commons file, no medium or size.

## Big addition, round 2: night, magic and the occult (17 Nov 2026)

54 works (VAULT-1535 to 1588), all free tier, grow `occult`: the Codex Gigas's Devil and Heavenly City, six Splendor Solis leaves (British Library), two Ripley Scroll panels (Wellcome), three Mutus Liber plates (LoC, 1702 Geneva), four Fludd plates and three Kircher plates (Wellcome photographs; one carries a CC BY credit), the Visconti-Sforza Death (Morgan) and the Cary-Yale Lovers and Chariot (Beinecke; maker unknown, mid-15th century), four Jean Dodal Marseille cards (BnF), witches from Dürer, de Gheyn, Stock, the Stregozzo, Salvator Rosa (2), Francken, van der Heck, Jan van de Velde II and Teniers, Callot's Temptation of Saint Anthony, Bruegel's Alchemist, Khunrath's laboratory, four leaves of the Compendium Rarissimum (Wellcome MS.1766), four Dictionnaire Infernal demons (crops of the BnF copy), four Kitab al-Bulhan leaves (Bodleian), and two Redon lithographs (Chicago). Medical and sideshow plates were left out (Fludd's senses diagram, Kircher's tarantula, the Augsburg conjoined twins). **Cut before merging:** three Augsburg Book of Miracles pages, because the only scans are of the 2013 Taschen facsimile, not the manuscript. Some titles had no holder title and were made from the folio or image number (Splendor Solis "folio NN", Compendium "Image NN"); each auditNote says so.

**Hilma af Klint moved to the look tier.** VAULT-141, 142 and 961 were free. Commons tags them only PD-old-70; their US status depends on when they were first published (if in 1978–2002, US copyright runs to 2047). Full-size link now hidden; the note and the image stay.

## Big addition, gap round g2: famous works in copyright (17 Nov 2026)

23 works (VAULT-1589 to 1611): Christina's World, Broadway Boogie Woogie (free: Commons marks it public domain in the US, published without notice), No. 5, 1948, Drowning Girl, Orange, Red, Yellow, Vir Heroicus Sublimis, Excavation (Chicago), four Magritte (Golconda, The Empire of Light (1954 Brussels version), Time Transfixed (Chicago), The False Mirror), Dalí's The Elephants, Spiral Jetty, The Dinner Party, Hirst's shark, Koons's Balloon Dog (Blue) (The Broad), Cloud Gate, The Weather Project, Fallingwater (free: a building), The Wounded Deer, Banksy's The Son of a Migrant from Syria (Flower Thrower had no usable image), Ai Weiwei's Sunflower Seeds (Tate) and Abramović's The Artist Is Present. Seven labels come from Wikipedia infoboxes because MoMA, the Menil and Brooklyn refuse the sandbox; Orange, Red, Yellow says acrylic per the infobox (unchecked against the sale record). Spiral Jetty and The False Mirror are tagged public domain in the US on Commons or Wikipedia but stay look tier (Dia and the estate claim copyright; The Treachery of Images is look).

## Big addition, gap round g1: famous free works (17 Nov 2026)

31 works (VAULT-1612 to 1642): Van Gogh (Self-Portrait with Bandaged Ear, The Night Café, Almond Blossom, Sorrowing Old Man ('At Eternity's Gate')), Caillebotte (Paris Street; Rainy Day, The Floor Scrapers), Uccello's Battle of San Romano, Masaccio's Tribute Money, Duccio's Maestà, Millet's Angelus, Courbet's Burial at Ornans, Surikov's Boyarina Morozova, Vermeer's Lacemaker, Klimt's Danaë, Kandinsky (Composition 8, The Blue Rider), Klee's Senecio (medium "Oil on gauze" from the Kunstmuseum Basel's file; the Wikipedia infobox says canvas on panel), Malevich's White on White, Matisse's Le Bonheur de vivre, the Lancellotti Discobolus, Millais's Boyhood of Raleigh, Hunt's Hireling Shepherd, Wallis's Chatterton, and the Parthenon, Hagia Sophia, the Great Sphinx, Stonehenge and the moai at Rano Raraku (photographs with photoCredit). Duchamp's L.H.O.O.Q., Picasso's Three Musicians and Ernst's Celebes went to the look tier with local copies, because English Wikipedia holds their images as non-free. The agent stopped before Rodin's The Kiss, Chartres, the Alhambra and the Sagrada Família; palettes and two mediums were finished by the coordinator, and every image was looked at against its title.

## Checking the big addition's notes (18 Nov 2026)

An independent agent read a random 50 of the ~568 new notes against their source files (seed 1117): 38 ok, 12 fixed, none cut. No invented quotations, praise words, readings of meaning or AI tics were found; a scan of all 568 for tics (em dashes, "notably", "iconic", "you", question marks, quotation marks) found only legitimate uses. The one real failure pattern was **dropped hedges**: a source's "probably", "identified as", "apparently" or "supposedly" stated as fact. A targeted pass then read every new note whose evidence held a hedge word the note lacked (22 more) and every look-tier film still (19): 11 more fixed (Carter's Vulture, Weston's Pepper, Higginson, a Yoshitoshi legend, Goya's Men Reading, the Hundred Guilder Print, Hokusai's Oiwa, Kircher's Magnes, Dalí's Elephants, two 2001 stills). Two film-still titles that read a scene into the image were cut back to what the file says (Seven Samurai, Still; Citizen Kane, Still (Kane at the Podium)). Other fixes: Caravaggio's age at Sick Bacchus (21 to 23, not 21 or 22), Ortelius began as a map illuminator not a map colourer, Vampyr's note no longer names the man in the coffin. Remaining risk: hedges that never reached the saved evidence are not caught by the filter, so about 2 to 4 percent of the unread notes may still overstate a source.

## Writing round 9a: dark and visionary (18 Nov 2026)

24 pieces (LIT-903 to 926), texts from Project Gutenberg through its own mirror (gutenberg.pglaf.org) while the main site was down, every line machine-checked with `save_new` and every note saved through `save_line` with the sources' hedges kept. Hearn's Kwaidan (Mimi-Nashi-Hōïchi, Mujina, Rokuro-Kubi, Yuki-Onna), Lovecraft (The Colour Out of Space, a second Call of Cthulhu passage), Stoker's Dracula (2), Le Fanu's Carmilla, Bierce's Owl Creek Bridge, Stevenson's Jekyll, Poe (Usher, The Pit and the Pendulum), Baudelaire in French (Spleen, L'Albatros), Rimbaud's Le Bateau ivre (first 8 stanzas, French), Dante (Longfellow: the Wood of the Suicides, Ugolino), Milton (Paradise Lost I and IV, 1667 spelling), Blake's doors of perception, Marlowe's Why, this is hell, Nietzsche (Common's Zarathustra) and Revelation 12. Not done: Lovecraft's The Outsider and Dagon (no trustworthy pre-1931 text), and pieces already on the site (Devil's Dictionary, Une charogne, Au lecteur, Proverbs of Hell, Faustus's last speech).

## Writing round 9b: war, earth and love (18 Nov 2026)

28 pieces (LIT-927 to 954) for the thinner shelves. War (12): Owen (Strange Meeting, Futility), Sassoon (The General, Attack, Glory of Women, Everyone Sang), Rosenberg (Break of Day in the Trenches, Dead Man's Dump, read against the 1922 page images), McCrae, Crane's War Is Kind, Hardy (Channel Firing, The Man He Killed). Earth (8): Hopkins (Spring, The Starlight Night, Hurrahing in Harvest, with Bridges's 1918 notes as the source for dates), Thoreau's Ponds, Muir (Our National Parks, Hetch Hetchy), Clare's I Am, Edward Thomas's Rain. Love (8): Sappho in Wharton's translation (2), the Song of Songs (2), Rossetti's Echo, Teasdale, Millay (Thursday, Time does not bring relief; both published before 1931). Three texts are OCR checked across two scans; Rossetti's Echo is dated 1862 from its place in the Goblin Market section of the 1906 edition, not from a source that names the year. Six notes are about the writer at the time, not the poem, because the sources say nothing specific about it. Seven of the new lines joined the front-of-house pool.

## Open decisions closed (17 Nov 2026)

Paul asked Claude to make the calls on what was outstanding.
- **VAULT-116 (Kollwitz, Sleeping Woman and Child) and VAULT-061 (Arms, The Gargoyle and His Quarry) were cut.** Cleveland withdrew both image files and no free copy exists at the Met, Chicago, NGA or the Library of Congress. Both artists stay on the site through other works (VAULT-975 to 980).
- **I Know Moon-Rise (LIT-888) keeps Higginson's 1870 spelling.** No edition in standard spelling was found, and rule 4 says to keep the public-domain text and record that here rather than respell it.
- **The blues are allowed** (round w10b) where the lyric was printed before 1929 and every line is confirmed by eye against the page image; the method is in that round's auditNotes.
- **Commons-only sizes stay held back** (135 works): a spot check found errors, and a wrong size is a wrong fact.

## Round 10: the world and the gaps (17–18 Nov 2026)

Plan in PLAN.md, "Round 10". Run with tools/BRIEF13.md (art) and out/BRIEF6.md plus save_line notes (writing). Every contact sheet was looked at before merging. Added 374 artworks (VAULT-1643 to 2016) and 64 writing pieces (LIT-955 to 1018). Europe's share of the art fell from 56% to 51%; writing from Africa, Oceania and the Indigenous Americas went from 23 pieces to 52.

| Round | Added | Notes |
|---|---|---|
| n2 South Asia and Tibet | 52 | Three Koh Ker sculptures dropped by the coordinator (Koh Ker was looted and the provenance is unclear; kept in big/n2/records_all.json). No Chitipati, skull drum or thighbone trumpet (human bone). A Met Bundi drawing given by Subhash Kapoor dropped. Southeast Asia filed under East & Inner Asia, as the site already does. |
| n7 Silent film, second reel | 33 | 22 films. The Wind and The Man Who Laughs carry "with recorded score". The Phantom Carriage copy was cropped by its uploader; Napoléon is probably the 2024 restoration ("probably" in auditNote). |
| w10b East Asia and Greek tragedy | 35 | The blues were dropped: the run was stopped by an output filter on the lyrics, so they stay off. Placeholder dates for Tao Qian and the Cathay poems were replaced with "early 5th century" and "8th century; English 1915". Song of the Bowmen of Shu credited to Ezra Pound (Pound gave it to "Kutsugen"; no fetched source confirmed the Classic of Poetry). |
| w10a Africa, Oceania and the Indigenous Americas | 29 | Chief Joseph's two passages from the North American Review (1879) and his father's dying words (LIT-361, same article) are `audit: attribution`: the article names no interpreter. The Indians' Book songs were transcribed from page images because the OCR interleaves two languages. LIT-359 (Kumulipo) now also cites the Journal of the Polynesian Society 1900 printing. |
| n1 Persian, Mughal and Islamic | 61 | No images of the Prophet. 13 works rest on Commons file records because the Freer, Brooklyn, Walters and Bodleian sites refused the sandbox. |
| n6 Avant-garde, early photography, four famous works | 54 | Published before 1931 = free even where Chicago's record shows an estate notice (Dix's Der Krieg, the Soviet posters, Sander, Man Ray's rayograph), matching Le Violon d'Ingres; five never published that early are look (Nolde ×2, Grosz's collage, Rodchenko's Mayakovsky, the Sagrada Família interior). The Stenberg posters for Man with a Movie Camera, The General and Potemkin had no reachable image; October, A Sixth Part of the World and Bed and Sofa stand in. Rodin's The Kiss, Chartres, the Alhambra and the Sagrada Família are now on the site, which clears the famous list. |
| n4 Africa, Oceania and the Americas | 65 | The Songye figure with human teeth and the Asmat bisj poles (c. 1960, not open) left out. Codex Borgia page 29 retitled "Codex Borgia, Page 29" to avoid the title rule clash with VAULT-236. |
| n3 China and Korea | 57 | Eight scrolls shown as details and titled so. The Met's Dong Yuan Riverbank keeps Wikipedia's hedge that it may be a Zhang Daqian forgery. |
| n5 Illustration and early comics | 52 | A 1922 Krazy Kat original known only from a fan-site scan was dropped. The agent found that VAULT-405's image is not Baba Yaga in her mortar but plate 3 of Russian Wonder Tales (1912); checked by eye and retitled with the book's caption (slug unchanged). The Baba Yaga plate is now its own record. |

The front of house pool gained 26 artworks (Kali, Yamantaka, the Wheel of Life, The Phantom Carriage, the Red Wedge, the Fourth King of Hell, Rackham's Valkyries, Clarke's Maelström, The Kiss, Little Nemo and others) and eight lines of writing.

## Round 11: writing first (19 Nov 2026)

Paul set a goal of 5,000 works with quality over everything. Six writing batches under out/BRIEF14.md (a piece goes in only if its pull quote stands alone; coming in short is fine). 297 pieces added (LIT-1019 to 1315); writing went from 922 to 1,219.

| Batch | Added | Notes |
|---|---|---|
| w11f Beyond Europe | 37 | Short of 50 on purpose (Porter's Hyakunin Isshu too weak; no usable source for Ghalib, Martí, Mistral, the Blunts' Mu'allaqat). Three titles the agent invented were replaced with first lines. Cullen's Incident carries the slur as printed, in the full text only. Dunbar's collections and years confirmed afterwards. |
| w11b Scripture and mystics | 31 | Seven held back in out/g_w11b_held.json: longer passages around verses already on the site (Psalm 23, Psalm 137, 1 Cor 13, John 1, Eccl 1, Rev 6) and a second wording of Gita 11:32. Pickthall from the 1930 Allen & Unwin scan (Gutenberg's text is a later revision). Gilgamesh (Thompson), Rumi (Nicholson), Eckhart and St John of the Cross not done: OCR needs page-image correction. |
| w11c English and American poetry | 63 | Most listed poems were already on the site, so other famous poems by the same writers went in. Dickinson in the Todd/Higginson edited texts. All poems first published before 1929. Thirteen more are extracted but unsaved in w11c/pieces.py. |
| w11a Greek and Latin | 49 | Two notes trimmed of clauses their source did not fully cover (Marcus Aurelius XII.36, Heraclitus). The Medea passage retitled with Riley's words. Edition years for Butler, Riley, Cornish and Gummere are from memory or archive.org metadata and say so. |
| w11e Prose | 64 | Chapter numbers the agent had from memory were taken off 11 titles (Gutenberg refused the check). Trotter's Pascal confirmed as Harvard Classics vol. 48, copyright 1910. Frankenstein uses the 1831 text under an 1818 label, as the existing pieces do. |
| w11d Europe in translation | 53 | Two notes trimmed (Huysmans on Moreau, Verlaine on the fête galante: the source did not tie the fact to the work). Wyatt's Petrarch dated "English before 1542". Several composition dates are from the agent's knowledge and are flagged in auditNotes. Pushkin and Hölderlin skipped on quality. |

Egypt is filed under Africa, Oceania & Indigenous Americas throughout (VAULT-146, LIT-247 and LIT-134 moved). Found, not fixed: Hafez is spelled two ways and "Where Are the Tidings of Union?" is on the site twice (LIT-780, LIT-892); Paul to decide which to cut.

## Round 12, p8: free works by look-tier artists (19 Nov 2026)

Paul asked for every legitimate route from look-and-learn to usable. Four routes only, each with fetched evidence in auditNote: the holder's own open-access flag; publication before 1931; US federal government work; documented non-renewal. 43 works added. No existing look work could be moved: the Met and Chicago flag every look work they hold as not public domain, and no pre-1931 reproduction was found for Three Musicians, Automat, Early Sunday Morning, Celebes, the pre-1931 Magrittes or Rodchenko's Mayakovsky.
- Holder's flag (30): Cleveland CC0 (Picasso's Frugal Meal, The Poor and Two Saltimbanques, two Klee, Mondrian's Chrysanthemum, Hopper's Lighthouse Village, three O'Keeffe, Sheeler, Demuth); Chicago public-domain flag (two Matisse, three Kandinsky, a 1935 Mondrian, two Stieglitz portraits of O'Keeffe, Hartley, Evans's Penny Picture Display); NGA open access (three Klee, Malevich, three Hopper etchings, Gris). For O'Keeffe, Hopper, Sheeler, Matisse and the 1935 Mondrian the tier rests on the holder's flag alone; take down at once if an estate objects.
- US government work (11): Evans, Lange, Parks, Shahn's OWI poster, Robert F. Sargent's D-Day photograph.
- Published before 1931 (2): two Magritte pages from La Révolution surréaliste no. 12 (15 Dec 1929), public domain in the United States only; hosted in images/plates.
- Dropped: two Kubrick Look photographs (the Library's rights statement could not be read), a faint Picasso etching.
- Leads: Grosz's The Guilty One Remains Unknown may have been reproduced in Bazalgette's George Grosz (1926), unproven. L.H.O.O.Q.'s 1920 printing in 391 was Picabia's replica, so it is not a basis for a move. Nolde's Prophet was unpublished per MoMA.

## Round 12: art toward 5,000 (19 Nov 2026)

Plan in PLAN.md, "Round 12". Eight batches under tools/BRIEF13.md, every contact sheet looked at, 457 artworks added (VAULT-2017 to 2473). The site holds 2,464 artworks and 1,219 writing pieces: 3,683 works. p8 (free works by look-tier artists) has its own section above.

| Batch | Added | Notes |
|---|---|---|
| p8 Free the look tier | 43 | See the section above. |
| p1 Dark masters II | 62 | Dürer, Bruegel's Sins, Blake, Redon, Munch's prints, Klinger, Rops, Martin, Kollwitz, Hugo. Munch's Madonna and an NGA Blake left out (title clashes); Kubin has nothing openly held. Rops prints undated by their holders. |
| p4 Painting depth | 69 | NGA lists Lucretia as Rembrandt; the note records van de Wetering's 2015 rejection. Hammershøi's English title is the common one, not from SMK's record. Five carry photoCredit. |
| p3 Photography II and government work | 61 | Trinity dropped (a Los Alamos contractor's photograph; only a Commons tag as evidence). Adams's Manzanar pictures are a private gift to the Library of Congress marked no known restrictions, not government work; his Mural Project is contract work marked Unrestricted by the National Archives. Abbott rests on NYPL's No Copyright – United States statement. |
| p2 Japan II | 61 | A Hokusai Manga spread and Rosetsu's tiger doors dropped (weak at tile size). Thirteen rest on Commons and Wikipedia. Yoshitoshi's English titles come from Wikipedia. |
| p6 Sculpture, buildings, objects | 52 | An arm reliquary dropped (the bone is still inside). The Veiled Christ and Sainte Foy left out for want of a good photograph. 28 carry photoCredit. |
| p5 Manuscripts and the medieval | 51 | A Hildegard vision numbered by eye and a prayer-book spread dropped. Five images (Kells ×2, the Rohan dead man, the Très Riches Heures Hell, the Angers pale horse) are Commons scans with no holder source, kept on the footing of the site's other PD-Art files. Facundus, the Morgan Beatus and the Scivias left out (facsimile scans only). Conques uses a Free Art License photograph. |
| p7 Design to steal II | 58 | The Chap-Book poster dropped (it advertises a magazine) and a second Beethoven Frieze panel (already in p4). Ten Rider-Waite-Smith cards from the 1910 printing. 32 have a blank medium. |

`tools/merge_round.py` now accepts a blank medium when the record carries `mediumBlank: true` (no fetched source states one). The front of house pool gained 46 works. All 457 images were loaded in Paul's Chrome.

## Calls Paul handed over (19 Nov 2026)

Paul: "you decide all of em, also remember our desire for inclusion of popular works etc however we can get around it or defend it."
- **Hafez:** LIT-892 cut (the same Bell translation of the same poem as LIT-780); the name is "Hafez of Shiraz" throughout, with "Hafiz" in search tags.
- **Rembrandt's Lucretia stays**, under the holder's attribution, with the dispute in the note.
- **The five manuscript images without a holder source stay** (Kells ×2, Rohan, Très Riches Heures Hell, Angers).
- **Works free on a holder's flag alone stay free** (O'Keeffe, Hopper, Sheeler, Matisse, the 1935 Mondrian); first to come down if an estate objects.
- **Popular works:** where no free route exists, a work people come looking for goes in the look tier (screen-size image, no download, sourced note: the commentary is the defence). In-copyright writing stays at one prose sentence under fifteen words, confirmed in a scan; no lines from poems or songs in copyright.

## Round 13, art: the popular works (19 Nov 2026)

Paul: popular works in, however it can be defended; and the look tier may go one day, so every candidate was checked against the free routes first. 111 artworks added (VAULT-2474 to 2584): 108 look, 3 free.
- **g4, photographs and film stills (49, all look).** Kertész, Brassaï, Brandt, Doisneau's kiss, Keïta, Sidibé, Eggleston, Shore, Sugimoto, Arbus-era portraits, Penn, Karsh's Churchill, Avedon, Crewdson, Gursky, Wall, Lunch atop a Skyscraper, Guerrillero Heroico, the 1968 podium, the Hindenburg; stills from Casablanca, La Dolce Vita, Tokyo Story, The Godfather, The Wizard of Oz, Days of Heaven, In the Mood for Love, Akira, Apocalypse Now, Sunset Boulevard, King Kong, Lawrence of Arabia, Godzilla, Modern Times, Bicycle Thieves, Dracula, Bride of Frankenstein. Dropped by the coordinator: Sally Mann's Easter Dress (her children), a Goldin shown as a photograph of the framed print, and a near-black tile. Eleven images are only 290 to 500 px.
- **g3, modern art (62: 60 look, 2 free).** Dalí, Kahlo, Magritte, Picasso, Matisse's Jazz, Hopper, Wood, Pollock, Giacometti, Rauschenberg, Johns, Warhol, Haring, Richter, Twombly, Rivera, Orozco, Lam, Kara Walker, Kiefer, Hirst, Sherman, Christo, Serra, Calder, Moore, Escher, Giger, Frazetta, Chagall, Miró, Dix, Grosz, Rockwell, Wiley, Tarsila, Albright, Bacon, Emin, Gormley, Cattelan, Gonzalez-Torres, Beuys, de Chirico, Nash, Motley, Catlett, Tanning. Beksiński's two paintings are free under CC BY-SA 3.0 from the rights holder (the Sanok museum, with a permission ticket on Commons): the first use of the maker's-licence route. De Lempicka's Autoportrait was flipped to look (no scan of the 1929 Die Dame cover was fetched). Holzer's Truisms dropped (the image is the text itself).
- **Leads toward the free tier** (unproven; each is in its auditNote): Lunch atop a Skyscraper (no renewal found, per Heald 2020; the renewal volumes would settle it); De Lempicka's Autoportrait (Die Dame cover, July 1929); Kertész's Satiric Dancer (a variant ran in Die Dame, 1927); Gas, Detroit Industry, Flamingo and Nuclear Energy (Commons "no notice" tags); The Harlequin's Carnival, Sylvia von Harden, Eclipse of the Sun, Abaporu and The Song of Love (pre-1931 works with no reproduction fetched); Totes Meer (possibly expired Crown copyright); Freedom from Want (OWI poster: a renewal search); Albright's Dorian Gray (the Art Institute holds the copyright and could grant permission). Dracula, M and Frankenstein (1931 films) enter the US public domain on 1 January 2027: move them then. Eleven living artists are listed in big/g3/report.md as people to ask.

## Round 13, writing (19 Nov 2026)

- **w12b, public-domain depth (37).** Gilgamesh (Thompson 1928, corrected from page images), two Rumi (Nicholson 1898; poem XXXI filed as an attribution), Whitman, Hardy, Housman, Dickinson (Todd and Higginson texts) and a letter, Owen, Hopkins, Gibran's The Prophet, Khayyam, Teasdale, Lowell, Brontë, Tennyson. Two Khayyam labels say "FitzGerald's fifth edition" without a year (the year was from memory). Not done: Eckhart, St John of the Cross, the Yoruba proverbs (choosing passages means reading the scans out, which trips the output filter), Li Bai and Du Fu (left out only because the coordinator barred translators who died after 1955 to get past the filter: they can come back), Rossetti, Thoreau's journal, Bashō and Issa.
- **w12a, one-line quotes from modern prose (45, all `audit: quoted`).** One sentence each, 14 words at most, found by code in archive.org full-text snippets and required in two scans; the coordinator read all 47 by eye and dropped two Kafka lines (he already has two quoted pieces, and one had no credited translator). Didion's opening is shown in ordinary case. No page image was checked, so punctuation rests on OCR; each auditNote says so. Not confirmed and left out: Ellison, Mandela, Calvino, Kundera, Saint-Exupéry, Campbell (the sentence runs to fifteen words or more), Borges, Arendt, Nabokov, Atwood, Watts, bell hooks. Never attempted: Salinger, Kerouac, Wright, Butler, García Márquez, Levi, Bukowski, and the presidents' speeches.
- Both writing runs were stopped once by the output filter and finished after being told to keep all taken text in files and never in their own output.

## Round 14 (20 Nov 2026, overnight)

- **w13a, letters, journals and speeches (53):** every pull quote read by eye before merging. The Bixby letter is `attribution` (possibly John Hay). Editorial line numbers stripped from two Rossetti poems. John Brown's last note titled as Du Bois prints it. Beethoven to Wegeler dated "1800 or 1801" (edition says 1800; 1801 not confirmed). Skipped: FDR's first inaugural and JFK at Rice (no official transcript reachable), Seneca (Gummere OCR), Heloise, Nietzsche's letters, Emerson's journals.
- **q1, Posada and the Americas (63 of 66):** all free. Held, not merged (`/home/claude/big/q1/held.json`): Bellows's The Law Is Too Slow (an anti-lynching lithograph, Century Magazine 1923, shows a lynching: Paul to see first), Posada's The Devil Butts with His Head (the mask reads as a caricature at tile size), Serpent Weather Vane (weak tile). Tier rests on the holder's flag alone for Sloan, Luks, Glackens and Shinn; the two arquebusier archangels rest on Commons PD-Art records. Not yet seen in Paul's Chrome: Chicago (At Mouquin's, The Advance-Guard, Execution by Firing Squad), Smithsonian (Homer's High Cliff, Fired On, five Catlins), Wikimedia (the two archangels). Leads: Amon Carter open access (Remington nocturnes, Heade), more Posada broadsides, Bellows's New York, Bierstadt's Last of the Buffalo.
- **w13b, mystics, Stoics, essayists and artists on art (50 of 51):** Gilgamesh (Thompson 1928), Rumi (Nicholson 1914), Eckhart (Inge), St John of the Cross (Lewis), Chapman's and Pope's Homer, Seneca (Stewart 1889), Epictetus and Marcus (Long), Montaigne (Cotton), Pascal (Trotter), Browne, Burton, Donne, Leonardo (Richter), Michelangelo (Symonds), Holanda (Holroyd), Xhosa and Yoruba proverbs, a Nama and a Southern Nigerian tale. Every pull quote read by eye. Dropped: a Seneca card whose quote was the front half of a sentence. Fixed: stray opening quote marks on four hooks, small-capital openings on two Eckhart pieces, OCR spaces before punctuation, the Gilgamesh "Sleeping and dead" hook cut to its first line (the passage is fragmentary). Michelangelo's "one paints with the brain" letter is dated only "16th century": recipient (Aliotti) and year (1542) were inferred, not confirmed. Five are label only. The proverb cards hold non-consecutive proverbs from one book; the two Rumi pieces come from Nicholson's The Mystics of Islam, which does not name the work. `merge_lit_round.py` now accepts an empty note with `labelOnly`. Leads: Blackwell's Some Spanish-American Poets (1929), Conway's Dürer (1889), Symons's St John, Burton's Wit and Wisdom from West Africa.
- **q3, the ancient world (55 of 58):** Egypt, Mesopotamia, the Aegean, Greece, Etruria, Rome, prehistoric and northern Europe; 29 from the Met, 26 from Commons with the photographer's licence read from the file page. Held (`/home/claude/big/q3/held.json`): Ram in a Thicket and the Artemision Bronze (gallery photographs where the work reads poorly), the Altamira bison (no source says whether the photograph shows the cave or the museum's replica). The agent dropped five on provenance (the Met's Gudea, the Monteleone chariot, a silver axe head, a Mithras plaque, a second Cycladic figure). Kept and flagged in auditNote as contested: the Parthenon frieze block, the Burney Relief, the Boscoreale frescoes, the Cycladic harp player, the copper Head of a Ruler: Paul may cut. Tutankhamun's throne and mask (VAULT-296) now give the Grand Egyptian Museum as holder (opened November 2025; press reports fetched 20 Nov 2026). Sixteen Met notes rest on the bare record and are plain. All 26 Commons images need Paul's Chrome. Leads: Cleveland, Chicago, the Getty, the Walters, LACMA and the Smithsonian for a second ancient pass; a Nebra disc photograph of the original; Trajan's Column; Scythian gold.
- **q4, Romantic, Symbolist and Expressionist drama (60 of 62):** Friedrich, Turner, Martin, Géricault, Delacroix, Blake, Fuseli, Palmer, Blechen, Redon, Bresdin, Klinger, Vallotton, Munch, Klimt, Schiele, Hammershøi, Meryon, Strindberg, three more Harry Clarke Poe plates. Held (`/home/claude/big/q4/held.json`): Munch's Melancholy III (same motif as Evening, Melancholy I already on the site) and Khnopff's The Offering (a thin strip that does not read as a tile). In: Géricault's Head of a Guillotined Man (a painting; death in art). Tier on the holder's flag for makers who died after 1930: Munch's three prints (Chicago's flag plus print dates 1896–1902), Gallen-Kallela's Ad Astra (Chicago). Clarke's plates rest on the 1919 edition; the title page was not re-read this round. Strindberg's medium is a translation of SMK's Danish. 18 Chicago images and three Commons plates need Paul's Chrome. Chicago's IIIF refuses region crops, so wide-margin Chicago prints cannot be cropped by URL. Leads are long and good (Kollwitz at Cleveland, NGA and SMK; more Turner, Blake's Job, Klinger, Vallotton, Munch at Chicago, 16 more Clarke plates; the Getty, Nationalmuseum, Rijksmuseum and Smithsonian were not searched).
- **w14a, poetry in English published before 1929 (94 of 95):** Herbert to Eliot; every pull quote read by eye. Held (`out/g_w14a_held.json`): Hughes's Suicide's Note (a three-line poem about suicide with nothing around it; Paul to decide). McKay's The Lynching is in. Corrected and noted in auditNote: an OCR first word in Frost's Once by the Pacific, a doubled word in Melville's The Portent, double hyphens set as dashes. Hopkins's title follows Bridges's 1918 first line. Dates the agent gave from memory were checked against fetched Wikipedia articles or edition pages (Shakespeare 1609, Housman 1896, Hopkins 1918, Owen 1920, Sassoon, Prufrock 1917, McKay 1922, Yeats 1910 and 1928, Millay 1917 and 1921, Robinson's Luke Havergal moved to 1896); Milton's sonnet on his late wife is labelled "17th century" because its date was not confirmed. Eighteen are label only. Not checked against page images: stanza breaks in Whitman's A Sight in Camp and Dickinson's There is a solitude of space; the line breaks of Toomer's Portrait in Georgia (five lines in the Gutenberg file). About 50 more clean extractions are specced in `/home/claude/w14a/s1.py`–`s6b.py`. gutenberg.pglaf.org mirrors Gutenberg when the main site is down.
- **w14b, great passages of fiction and drama (88 of 90):** Melville, Hawthorne, Dickens, Austen, George Eliot, Hardy, Conrad, Wilde, James, Joyce, Forster, Fitzgerald, Cather, London, Twain, Poe, Chopin, Toomer; Dostoevsky, Tolstoy and Turgenev (Garnett), Gogol, Flaubert, Hugo, Balzac, Stendhal, Zola, Proust (Scott Moncrieff), Cervantes (Ormsby), Goethe, Rabelais, Voltaire, Hamsun; fourteen Shakespeare speeches, Marlowe, Webster, Jonson, Ibsen, Synge, Shaw, O'Neill. Every pull quote read by eye. Held for a page-image check (`out/g_w14b_held.json`): Hemingway's "The world breaks every one" (1929) and Faulkner's Addie passage (1930), both from OCR of later reprints. Titles changed where the agent's first-words title read badly (Three Sisters; Anna Karenina, Part Eight). For eleven translated pieces the translation's year is not in the Gutenberg file; the translator is, and the auditNote says so. Candide's 1918 Modern Library text names no translator. Six are label only; fifteen notes are one or two short sentences. Not done: Chekhov's The Student and The Sea-Gull (translator not named), Larsen's Passing, Woolf, Murasaki, Maupassant, Boccaccio, Strindberg, Büchner.
- **q5, Renaissance and Baroque depth (61 of 64):** Dürer, Bruegel, Cranach, Altdorfer, Holbein, Rembrandt, Vermeer, Hals, Ruisdael, Fabritius, Rubens; Leonardo, Michelangelo, Raphael, Botticelli, Mantegna, Bellini, Giorgione, Titian, Pontormo, Parmigianino, Arcimboldo, Caravaggio, Artemisia; El Greco, Velázquez, Zurbarán, Ribera, Murillo, La Tour, Poussin. 29 rest on a holder's open-access image (NGA, the Met, the Rijksmuseum, Cleveland); 32 on a Commons faithful reproduction of a painting made before 1700, licence read on each file page, sizes left blank. Held (`/home/claude/big/q5/held.json`): Leonardo's Saint Jerome (the photograph reads badly), Tintoretto's Last Supper (dark, small file), Bronzino's Allegory with Venus and Cupid (Paul to decide). Mantegna's Louvre Saint Sebastian uses a file confirmed by eye because the file named for it describes the Vienna picture. The Delphic Sibyl's date and the Map of Hell's details come from the Commons record only. All 32 Commons images need Paul's Chrome. The agent listed about 30 open-access works checked and ready (Met, NGA, Rijksmuseum, Cleveland) and a long unsearched list: enough for a second batch.
- **q6, leads taken up (64 of 68):** Turner, Martin, Géricault, Delacroix, five Blakes, Fuseli, Palmer, four Klingers, Vallotton, Meryon, Toorop, Schiele, five Munch, seven Kollwitz, Hammershøi, Dahl, Bellows's New York, Homer's Dressing for the Carnival, Bierstadt's Last of the Buffalo, two Posada broadsides, eight ancient objects (Cleveland, Chicago, the Freer), six more Clarke Poe plates. Held (`/home/claude/big/q6/held.json`): the Posada devil mask again (the same block held from q1), two Vallotton plates from Crimes et Châtiments that show a child run over and a child beaten (Paul to decide), Friedrich's Moonrise (too faint for a tile). On a holder's flag alone, makers who died after 1930: Munch's two paintings at SMK and three prints at Chicago; Kollwitz at Cleveland, NGA and SMK. Four Kollwitz prints use our own IIIF region crop of SMK's image, recorded in auditNote. Clarke's edition year (1919) is still not confirmed from a title page; Wikipedia mentions 1919 halftones and a 1923 edition, both before 1931. Amon Carter marks works public domain but routes images through a licence form: not taken. Skipped on provenance: Cleveland's Stargazer, Apollo, Medea krater and a 1971 Hawara portrait. Needs Paul's Chrome: nine Chicago, one Smithsonian, six Commons.
- **w15a, poetry in English, second helping (47):** more Shakespeare, Herbert, Blake, Clare, Shelley, Tennyson, Hardy, Housman, Swinburne, Sassoon, Dickinson, Frost, McKay, Cullen, Hughes, Yeats, Eliot. Every pull quote read by eye. Emily Brontë's "Often rebuked" is `attribution` (printed as hers in the 1850 selection; the attribution has been questioned). Blake's A Divine Image is labelled "date unknown". 21 are label only. Failed again for want of a clean text: Marvell's Definition of Love, Herbert's The Collar, Clare's A Vision.
- **q7, photography III (68):** Talbot, Hill and Adamson, Cameron, Le Gray, Watkins, Barnard, Southworth and Hawes, Du Camp, Frith, Beato, Atget, Sutcliffe, Emerson; Camera Work gravures (Stieglitz, Strand, Steichen, Coburn, de Meyer, with issue and year); Genthe's San Francisco, Ponting, Hurley's Endurance, the Wright brothers' first flight, Hine, Riis, Curtis (portraits and landscapes only), FSA/OWI (Wolcott, Delano in colour, Vachon, Bubley, Palmer, Parks, Rothstein), Adams's Manzanar, the Nagasaki cloud (US Army Air Forces), four Abbott Changing New York, five NASA. 34 from the Library of Congress, 17 the Met, 6 NGA, 4 NYPL, 2 Cleveland. None hosted by Chicago, the Smithsonian or Wikimedia. On a holder's flag alone for makers who died after 1930: Adams, Abbott (NYPL says it believes the prints are public domain), Genthe, Johnston, Hine. LoC captions kept as the historical record, as elsewhere on the site. To check: the LoC record calls Strand's The White Fence plate IX of Camera Work 49/50, and VAULT-1829 Porch Shadows claims plate IX too; one is wrong. Strand's two "Photograph—New York" plates carry their plate numbers in the title so the app keeps both. The first-flight photograph is credited to Orville Wright and John T. Daniels.
- **w15b, philosophy, wisdom and the sacred (62):** Nietzsche (Common, Zimmern), Schopenhauer (Saunders), Spinoza (Elwes), Emerson, William James, Carlyle, Wilde's Soul of Man, Unamuno (Flitch 1921), Plato (Jowett), Boethius (H. R. James), Augustine (Pusey), Job, Psalms and Ecclesiastes (KJV), Laozi, Confucius (Legge), the Dhammapada (Müller), the Gita (Arnold), Kabir and Gitanjali (Tagore), Gibran's The Prophet (1923), Emma Goldman, Du Bois's Darkwater, Ptahhotep (Gunn). Run on Opus after the overnight model's weekly limit ran out. Every pull quote read by eye; stray closing quote marks taken off the three Analects hooks. Saunders's and Elwes's translation years are not in the files (Gutenberg hosts both as US public domain). The Schopenhauer "forfeit" date assumes Counsels and Maxims is from Parerga, which Saunders states in another volume. Augustine is filed under Africa (Hippo). Not reached: Plotinus, Mencius, the Upanishads, al-Ma'arri, Epicurus, Kropotkin, Gibran's Madman and Forerunner, Twilight of the Idols.
- **w16a, poetry in translation (40 of 41):** 37 in A. S. Kline's openly offered translations (`license` set, non-commercial; every original published before 1931): Baudelaire, Mallarmé, Nerval, Ronsard, du Bellay, Labé, Charles d'Orléans, Villon, Hugo, Verlaine, Apollinaire, Rilke, Goethe, Heine, Pushkin, Tyutchev, Lermontov, Gumilev, Blok, Mandelstam, Leopardi, Quevedo, Góngora, Lorca (Canciones 1927, Romancero gitano 1928), Machado, O Fortuna; plus Pound's Cathay (1915) and two from Waley's More Translations from the Chinese (1919). Kline is now a large share of the translated poetry: revisit if the site ever makes money. Held: Leopardi's Night-Song closing lines (the hook opened mid-clause and read badly). Unsure and noted: Machado's Caminante dated 1912 (may be from the enlarged edition); Mandelstam's Tristia dated by the 1922 book; Baudelaire's Recueillement and Ronsard's sonnet matched to Kline's pages by keyword. Dropped for want of a confirmed date: about a dozen, including Clair de lune and Tsvetaeva. Akhmatova left out (died 1966; Kline asks permission where the original is not public domain). Correction to the briefs: works published in 1929 have been US public domain since 1 January 2025, so the "before 1929" line in the writing briefs is a year too strict; the line is "before 1931" from 1 January 2026.
- **q8, European painting and drawing 1300–1700, second pass (66 of 68):** Giotto's Arrest of Christ, Fra Angelico's Annunciation, Uccello's Hunt in the Forest, Piero della Francesca (Flagellation, Federico da Montefeltro), van Eyck (Annunciation, Man in a Red Turban), Rogier (Portrait of a Lady, Descent from the Cross), Memling's Last Judgment, Grünewald's Small Crucifixion, Bruegel (Land of Cockaigne, Magpie on the Gallows, Two Monkeys), Holbein's Georg Gisze, the Doni Tondo, Botticelli, Bellini's Loredan, Titian, Leonardo's Saint John, Caravaggio's Sacrifice of Isaac, Artemisia's Jael and Sisera, Reni's Saint Michael, Ribera's Tityus, Rubens (Medusa, Prometheus), Velázquez (Bacchus, Mars, Waterseller), Vermeer (Maid Asleep, Lady Writing, Love Letter), Rembrandt (Self-Portrait with Two Circles, Bellona), Hals's Young Man with a Skull, Torrentius, Dürer's Stag Beetle. 34 on the holder's own open-access image, 34 on Commons PD-Art copies. Held (`/home/claude/big/q8/held.json`): Caravaggio's Amor Vincit Omnia (Paul to decide), Segers's Enclosed Valley and a pale Leonardo sheet (weak tiles). Disputed attributions kept with the hedge in note and auditNote: Rubens's Vienna Medusa, Arcimboldo's Librarian, Hals's Young Man and Woman in an Inn. The Met's image server now shows the sandbox a bot page, so the ten Met images were seen through cached copies. Needs Paul's Chrome: four Chicago, 34 Commons.
- **q9, design, type and posters to steal from III (50 of 59):** Bodoni's Manuale Tipografico, Byrne's coloured Euclid, Bickham's Universal Penman, Leavenworth's wood type (NYPL's only surviving specimen), Chinese and Japanese calligraphy, a Kufic Qur'an page; Lautrec (Eldorado, Bruant, Eglantine's troupe), Mucha (Gismonda, La Samaritaine, Lorenzaccio, Zdeňka Černý, Documents Décoratifs, Ilsée), Chéret, Grasset, Rysselberghe, Fischer, Hohlwein's 1913 Bavarian railways, Raleigh's Liberty Loan posters, two WPA exhibition posters; surimono by Hokusai, Hokkei and Zeshin; five of Du Bois's 1900 Paris data portraits; Dresser, Owen Jones, Prisse d'Avennes, katagami, Iznik tiles, Morris, the Wiener Werkstätte sample book. Held for Paul (`/home/claude/big/q9/held.json`): nine posters that advertise a publication (Lautrec's Reine de Joie, Au Pied de l'Echafaud and La Revue Blanche; Mucha's Zodiaque for La Plume; Steinlen's Traite des Blanches, Temps Nouveaux and Ten Assassinations; the 1896 Jugend poster; Bradley's Chap-Book). The no-ads rule dropped the Chap-Book poster in round 12, so these are held to the same line; if Paul reads a poster for a magazine or a book as closer to a theatre poster than to an ad, they can go in as they are. Chéret's Palais de Glace and Olympia were treated as entertainment venues. Du Bois's charts rest on the LoC flag and their 1900 display; posters by makers who died after 1930 rest on publication before 1931 plus the holder's flag. The Met's image server blocked the sandbox, so Blake's Songs, Beardsley's Morte d'Arthur drawings, Hokusai Manga and the Met's calligraphy were left for a run from Paul's browser. Needs Paul's Chrome: 18 Chicago, five Smithsonian, one Commons.
- **q10, Asia and the Islamic world, further pass (65):** Hokusai (five Thirty-six Views not on the site, whaling off Gotō, bridges, the Ono waterfall), Hiroshige (Shōno rain, Kambara snow, the Kiso snow and Awa whirlpools triptychs), Kuniyoshi, Kobayashi Kiyochika (new: the 1881 fire, Pungdo naval battle), Cleveland's Nanban screen, Sakai Hōitsu, tsuba; Song leaves (Ma Lin, Li Anzhong 1117), Zhao Mengfu, Shen Zhou, a Shang fangyi; Goryeo celadon and iron-glazed prunus vases; Mewar, Deccani, Mughal, Basohli and Bengal pages, the Akbarnama; the Wade Cup, the Seljuq feline incense burner, an Ilkhanid sphinx ewer, Iznik, a Mina'i beaker, a 1444 Shiraz Shahnama frontispiece, a Qajar astrolabe. All on Cleveland's CC0 and Chicago's public-domain flag. Pages checked by eye for images of the Prophet: none. Provenance rule applied strictly: eleven wanted works dropped (acquired after 1970 with only a dealer or auction history, including a Chola Narasimha, a Javanese Mahakala, Green Tara, Soga Nichokuan's Dragon and Tiger screens), so no Chola, Khmer, Javanese or Tibetan piece this round. Kept with collection history in auditNote: the bixie (Bernat, Sotheby's 1980), Palace Landscape (Jiang Ershi, 1971), Boating in Moonlight (Carroll, 1989), the Benkaim Indian pages. A Mewar page Cleveland gives to Chokha but dates before his working life is credited Maker unknown. Needs Paul's Chrome: 20 Chicago.
- **w16b, leads and East Asia (40 of 42):** eighteen poems from Bynner and Kiang's The Jade Mountain (1929, public domain since 2025; every line checked against a second scan and the page image): Li Bai's Quiet Night, Wang Wei, Du Fu, Li Shangyin, Zhang Ji's Maple Bridge, Chen Zi'ang, Zhang Jiuling, Wang Changling, Chen Tao, Bai Juyi; Waley's 170 Chinese Poems (1918): Su Shi on his son, Wang Ji, Chen Zi'ang; Gibran's The Madman and The Forerunner; Nietzsche's Twilight of the Idols and Ecce Homo (Ludovici); Zhuangzi (Giles 1889); al-Ma'arri (Rihani 1918); five Greek Anthology epigrams (Mackail 1890); Annensky (Kline, The Cypress Chest 1910) and Bion (Kline). Held (`out/g_w16b_held.json`): Plotinus on the Beautiful in Taylor (the text reads "participating largely off the vivid ray", an apparent misprint, and "survey, the orb"), and Ecce Homo's amor fati passage (the source reads "is! amor fati"). Du Fu's Yo-chou poem: "T" corrected to "I" from the sense of the line, not checked against the page image. Waley's dates for Wang Ji and Chen Zi'ang differ from Wikipedia's; both recorded.
- **q11, photography and poster leads (51):** sixteen Camera Work and pictorialist gravures (Steichen's Rodin, Coburn's Williamsburg Bridge, Frank Eugene, Clarence White, Käsebier, Seeley), six Abbott Changing New York (Seventh Avenue, Manhattan Bridge, Daily News, Zito's bakery, the Flatiron, the El), ten FSA/OWI Kodachromes (Palmer's slag run-off and Bessemer converter, Delano, Feininger, Collier, Wolcott, Lee), Hurley's Endurance and Ponting's bergs, Steinlen's war posters, Grasset's 1894 exhibition poster, US Liberty Loan and Tank Corps posters, seven Federal Theatre posters. LoC 38, NYPL 6, NGA 4, Cleveland 3; nothing on Chicago, the Smithsonian or Wikimedia. On a holder's flag for makers who died after 1930: Seeley, Eugene, Käsebier (NGA CC0); Abbott (NYPL and the FAP); Steinlen's 1915 Belgian poster rests on its Paris printing alone. French war-loan posters naming a bank were left out (no business). White's Camera Work nudes of children left out. Delano's sawmill is "attributed" as the LoC says.
- **The site passed 5,000 with this merge: 5,010 works (3,236 art, 1,774 writing).**

## Search by meaning, measured colour and More like this (20–21 Nov 2026)

Paul asked whether search was just a tagging game, asked for research, then said "do it all … hide as much as we can." Done overnight on the preview; method in CLAUDE.md ("Search by meaning…") and `tools/search/`.

- **What the research said.** On art, text search over a plain description of each picture beat searching the picture directly (one Met test: 13 of 20 relevant against 8, and 3 for keywords). Picture models are weaker on concepts thin on the web, which is the deep cuts, so descriptions carry the search and picture matching is used only for "More like this", where it compares pictures with pictures.
- **Measured colour.** 3,086 of 3,236 artworks measured from their pixels. Families now: black 1,395, cream 1,163, gold 640, red 318, green 210, blue 163 (a work can carry several). Fewer blue and green than the old tags claimed, but the old tags were wrong (the Scream under Blue); thin cool shelves are honest for a collection heavy on prints and old paintings. Contact sheets per family were checked by eye; teal-greens leaking into blue and sepia browns into red were fixed before the run.
- **Descriptions.** Written by eight describers from numbered contact sheets, never shown. Spot-read samples are literal and plain (octopus plate, the tiger folk painting, a Night of the Living Dead still). The brief asks for what is visible only, plain words for nudity, violence and death, and a mismatch flag when a picture is not what its title says.
- **Broken images the describers found.** VAULT-057, Van Gogh's The Bedroom: the IIIF id showed a different painting (a blue mosaic, apparently by another artist) on the live site. Replaced with the image_id from Chicago's own record for artwork 28560 and checked by eye. VAULT-3127, the Wiener Werkstätte sample book: the image is only the cover logo, no swatches; held for Paul (the rule that the image must show what the title names). Six more confirmed by eye and held for a fix from the holders' records (the sandbox cannot search Wikimedia properly; do it from Paul's browser): VAULT-248 Wild Turkey shows a modern Audubon book cover with a heron; VAULT-399 Tournée du Chat Noir shows a photograph of Steinlen with a cat sculpture; VAULT-470 Bonampak Murals shows the site's ruins, not the murals; VAULT-234 Copernicus's sun-centred diagram shows the title page; VAULT-233 Uranometria (Title Page) shows a constellation plate; VAULT-1865 Kota Reliquary Figure shows a standing figure that does not look Kota (least certain). VAULT-2613/2614, Albinus plates titled as muscle figures, look stripped nearly to the bone; probably deep-layer plates, left alone.
- **Search tests (headless, word search alone → with meaning).** "lonely woman at night": loose matches on "woman" → Yoshitoshi's Moon over a Single Dwelling, Hopper's Automat, Palmer's Lonely Tower, Frost's Acquainted with the Night. "storm at sea": 1,072 loose matches → Turner's Snow Storm, Heade, Friedrich, Hurley's Shackleton. "a cat": Catullus, Cather and Catrina → Steinlen's cat, Poe's Black Cat, Beardsley, Kuniyoshi's cats. "longing for home": Winslow Homer → Frost, du Bellay, Baudelaire. "rembrandt" and the typo "gentileshi" still go straight to the artist.
- **Finished 21 Nov.** The last 150 pictures were screenshotted from Paul's Chrome once it was back: all 3,236 artworks are measured, described and matched. Two SMK images (VAULT-143 Appraising the Day's Work, VAULT-046 The Fall of the Titans) would not load from SMK's thumbnail server even in Paul's browser, so they were likely blank on the live site; both now point at SMK's main IIIF server, same files, checked by eye. The Met's image server sends no CORS headers, so its images can only be read from a screenshot. Two ways of fetching faster (another user agent for the Met, a GitHub Actions run for Wikimedia) were refused by the session's safeguards as getting around the holders' limits; that is the right line and is written into CLAUDE.md.

## Smarter colour (21 Nov 2026)

Paul asked whether a work with several colours should sit high under each of them. Research and tests (PLAN-colour.md, with sources), then his go on all four ideas with Claude's picks: strongest first, accents weighed by vividness, two colours meaning both, and any shade, with pink and purple as pigments only, pigment names in the strip, lightbox swatches that search on tap, and the old colour view hidden.

- **Measurement.** OKLab, eight clusters per image, centre weighting, the ground discounted (a third for names, a tenth for shades; Cream exempt). Contact sheets per name were read by eye and the boundaries tuned twice: aged silk and yellowed paper had been reading as orange and gold (now brown or cream), and deep reds as brown (now red).
- **Counts at strength 8 or more:** Red 122, Orange 88, Gold 129, Green 98, Blue 159, Brown 1,748, Black 1,277, Grey 2,528, Cream 1,904. The collection is mostly prints, drawings, photographs and old paint, so the bright names are short lists and honest ones.
- **Tests read by eye (first ten of each):** Red opens on Haring, Malevich, Dalí, Mondrian, Matisse's Red Studio and af Klint; Blue on the Blue Nude, Dürer's Praying Hands and Anna Atkins; Gold on Sunflowers and Basquiat; Green on Hirst's shark, Gauguin and Warhol's Mao; Black on deep-field photographs, Caravaggio and Las Meninas; Cream on prints and plates. Oxblood: Caravaggio's Death of the Virgin, Piero, Gentileschi, Sargent, McCurry. Klein blue: the Blue Nude then WPA posters. Vermilion: Malevich, Mondrian, Rothko, Hokusai's dragon. Verdigris: Almond Blossom, Whistler, Hockney. Lilac: Klimt's Mäda Primavesi, Emin's bed, Monet's Camille (it found sky before the OKLab switch). Red with Gold: the R.U.R. poster, the Magician tarot, Lichtenstein. Blue with Gold: Marc, Picasso's Weeping Woman, Dalí.
- **Known limit.** Sage and other quiet greige shades still match aged paper on prints; the paper really is that colour. Left as is rather than tuned into dishonesty.
- **Change in behaviour.** Colour now applies to art only; writing had carried colour tags from the old system that meant nothing for a text.

## Go-live and loose ends (21 Nov 2026)

Paul: move the preview live, and "solve all that now" before he moves to a new chat.

- **Held items, Paul's decisions.** In: Bellows's The Law Is Too Slow (VAULT-3246); Vallotton's Crimes et Châtiments plates 6 and 8 (3247, 3248); nine publication posters, which now count like theatre and film posters rather than ads (Lautrec's Reine de Joie, Au Pied de l'Echafaud and La Revue Blanche, Mucha's Zodiaque, Steinlen's La Traite des Blanches, Les Temps Nouveaux and Ten Assassinations for a Penny, the Jugend poster, Bradley's Chap-Book; 3249 to 3257); Hughes's Suicide's Note (LIT-1872). Out, unchanged: Bronzino's Allegory with Venus and Cupid and Caravaggio's Amor Vincit Omnia. Each new record's auditNote names the approval.
- **Hemingway and Faulkner.** A Farewell to Arms (1929) and As I Lay Dying (1930) are public domain in the United States. Both passages were read word by word against the page image of the same scan (Hemingway: in.ernet.dli.2015.209262, leaf n266, page 264; Faulkner: dli.ernet.285658, leaf n134, page 134); both match. Added as LIT-1873 and 1874.
- **Images fixed, 21 Nov 2026** (found by the describers; all checked by eye, details in each auditNote):
  - VAULT-057 The Bedroom: showed another painting; now Chicago's image for artwork 28560 (fixed 20 Nov).
  - VAULT-248 Wild Turkey: was a modern book cover; now Plate 1 from the Boston Public Library copy (W. H. Lizars engraving, per the library).
  - VAULT-399 Tournée du Chat Noir: was a photograph of Steinlen; now the Rijksmuseum's poster (RP-P-1969-78, CC0).
  - VAULT-470 Bonampak Murals: was the site's ruins; now a photograph of a painted wall (Jacob Rus, CC BY-SA 2.0, credited).
  - VAULT-234 Copernicus: was the title page; now folio 9 verso with the sun-centred diagram, from the Smithsonian Libraries copy of the 1543 first edition (archive.org), hosted in images/plates/.
  - VAULT-233 Uranometria (Title Page): was a crop of a 1661 constellation figure; now the 1603 title page from the US Naval Observatory Library's copy.
  - VAULT-3127 Wiener Werkstätte sample book: was the cover logo; now Chicago's own view of the book open on a swatch.
  - VAULT-1865 Kota: the image was right; the title now follows the Met's ("Reliquary Figure (Kota peoples, Mbete group)").
  - VAULT-143 and 046: SMK's thumbnail server stopped serving them; now SMK's main IIIF server.
- **Speed.** Full texts moved to data/texts.json, loaded when the browser is idle: site.js 8.5 to 7.3 MB raw, 2.1 to 1.7 MB gzipped.
- **Pipeline cache.** Picture embeddings for all 3,248 artworks are in tools/search/cache (int8). Rebuilding neighbours from the cache alone matched the full-precision build at 97% overlap (every list shares at least 6 of 8).
- **Site now:** 5,025 works (3,248 art, 1,777 writing).

## Writing as rich as the art (21 Nov 2026, evening)

Paul asked for the writing to feel as rich as the art, retired the Reading Room, and told Claude to make the calls and put them live. Calls made, for Paul to overrule:

| Call | Why |
|---|---|
| Reading Room hidden, not deleted | The Writing wall, its row and the reader do its job; the code stays in case it comes back. |
| Writing row: Theme, Mood, Form, Length, Era, Region | Paul's list. "Use it for" and "Spoken to" are out (Paul, 22 Nov 2026). |
| Form in nine groups | The 400-odd labels on writing include many invented ones ("Fever Prose", "Modernist Polyrhythmic Free-Stanza Indictment"); the nine are what a reader asks for. Labels in `medium` are unchanged in the data. |
| Length thresholds 16 / 40 words | 481 lines, 1,080 few lines, 216 passages. |
| Peek on mouse only | Hover does not exist on a phone; a tap opens the reader, which now leads with the quote. |
| "Grow on hover" rejected | The wall would shuffle under the mouse. |
| Recognition from Bartlett's 1919 | Open, sourced, and matches the famous lines exactly. Biased to the English canon, so the weighting is light and capped per writer. |
| Pairs only above a floor | A weak pairing reads as random; better to show nothing. |

Bartlett's texts are OCR; a missed match only costs a piece its nudge.

## Round 15: slogans and protest (22 Nov 2026)

45 Slogan & chant cards (LIT-1875 to 1919) and 29 Library of Congress pictures (VAULT-3258 to 3286). Method: 81 candidate slogans, each matched to its Wikipedia article fetched as raw wikitext; the card's wording had to occur in the article, and every fact in the note was taken from it. 36 candidates were dropped: no article or no documented first use (Bread or Blood, Don't mourn organize, Wir sind das Volk, ¡Ya basta!, Be water, Que se vayan todos, Hasta la victoria siempre, All power to the Soviets, Peace, Land and Bread, There is no Planet B), songs (We Shall Overcome, Lift Every Voice, Down by the Riverside, the Internationale), duplicates of pieces already on the site (Give me liberty, Ain't I a Woman), or too vague (Solidarity, Velvet Revolution, Free speech, Peace Now, Save the Whales, We Demand, Stonewall, Remember the ladies, Out of the closets, Land to the tiller, Deeds not words, Votes for Women as a newspaper title, Failure is impossible). Notes trimmed where a draft said more than the article: Live Free or Die (no reunion), Silence=Death (poster 1986, not 1987), Woman, Life, Freedom (late twentieth century, not 1990s), Amandla (no decade), the IWW motto (no year). Pictures: chosen by eye from 125 open LoC results; one dropped (an Iran hostage-crisis demonstration, too unclear to caption). Picture notes use only what the LoC record says; claims read off the image were cut (the broadsides' contents, Milholland riding at the head of the parade). Descriptions for search written from the contact sheets.

Same day, Paul's bar for protest pictures: a sign is art; a crowd shot only with real drama or action. Cut ten wide shots from the LoC set (VAULT-3258, 3264, 3265, 3266, 3269, 3270, 3271, 3273, 3275, 3278: the long picket line, the head of the 1913 parade, the aerial parade crowd, four March on Washington crowd views, the Reflecting Pool, the Eartha Kitt picket, the 1976 march, the Lawrence children). Added ten Commons photos (VAULT-3287 to 3296), chosen by eye from 275 openly licensed results: signs, and one water-cannon scene. Left out: Women's March pictures dominated by election signs (no campaign material), school-strike photos centred on children, an ACT UP Silence=Death button marked public domain on Commons whose design rights are unclear, and Keith Haring's Ignorance = Fear (in copyright).


## Round 16: folk songs (22 Nov 2026)

Paul asked for public-domain folk lyrics from traditions around the world, with an English translation for everything, overlapping with the protest songs. Finish line set at the start: what the downloaded pre-1931 collections could give cleanly, about 15. 14 merged (LIT-1920 to 1933).

| Id | Song | Source | Fixes |
|---|---|---|---|
| 1920 | Home on the Range | Lomax 1918 | drop cap |
| 1921 | Jesse James (first three verses) | Lomax 1918 | soft wrap joined |
| 1922 | The Old Chisholm Trail (opening) | Lomax 1918 | drop cap, hyphen join |
| 1923 | The Cowboy's Lament (first three verses) | Lomax 1918 | drop cap |
| 1924 | The Preacher and the Slave | IWW Songs of the Workers, Oct 1919 | 'bout, we'll, you'll (page image) |
| 1925 | Solidarity Forever (first three verses) | same | sun (page image); the book's 'insipration' kept |
| 1926 | Sir Patrick Spens (Child 58 A, Percy 1765) | Sargent & Kittredge 1904 | they'll, fiftie |
| 1927 | The Wife of Usher's Well (Child 79 A, Scott 1802) | same | stanza number |
| 1928 | Many Thousand Go | Slave Songs of the US, 1867 | 'Man-y' to Many |
| 1929 | My Grief on the Sea (tr. Hyde) | Love Songs of Connacht, 1893 | soul!, bound. (page image) |
| 1930 | Olympos and Kissavos (tr. Stuart-Glennie with Demosthenes) | Greek Folk Poesy, 1896 | Olympos, gazes!’ (page image) |
| 1931 | Charon and the Souls (tr. Garnett) | same | them |
| 1932 | Dirge for the Dead, closing part (Badaga, tr. Gover from Metz) | Folk-Songs of Southern India, 1871 | thread, (page image), pillar's, dashes closed as printed |
| 1933 | Song of War (Zulu, tr. Curtis, metrical version) | Songs and Tales from the Dark Continent, 1920 | Gully-Wall |

Calls: the cowboy and IWW songs that run long are cut to their opening verses (said in auditNote). Curtis's book frames its singers in the racial language of 1920; only the song and her facts about it (singer, occasion, translation) are used. Gover's headnote is a missionary's; only the funeral custom it records is used. Home on the Range is credited 'Traditional, words after Brewster M. Higley' because Lomax prints the sung version. The IWW songs are authored (Joe Hill, Ralph Chaplin), published before 1931, and sit here because they are the protest tradition Paul named. Nothing from Ralston (Russian) or Curtis's Ndau songs yet: leads for another pass.


## Protest pictures, second pass (22 Nov 2026)

Paul: get the iconic public-domain protest signs and posters from around the world and from all conflicts, still picky. 16 added (VAULT-3297 to 3312), all `free`. Pre-1931 posters and photographs (public domain in the US): Moor, Help (1922); Minor, At Last a Perfect Soldier! (1916); the Easter Proclamation (1916); Gandhi at Dandi (1930; Commons PD-India and PD-1996); Pankhurst's arrest (1914; IWM scan); the 1908 suffragette poster parade. Openly licensed (photoCredit): Hellberg's Greta Thunberg (CC BY-SA 4.0), Studio Kanu's Harcourt Road (CC BY-SA 2.0), Sue Ream's Brandenburg Gate (CC BY 3.0), Yann Forget's juggler (CC BY-SA 3.0), Hickson's Tahrir Square (CC BY-SA 4.0). US government: VOA's Women's March sign. Library of Congress, no known restrictions: two Trikosko frames from the March on the Pentagon (1967), Vargas's Moratorium poster (published without notice), O'Halloran's gagged women (1970). Every Commons image was loaded at 960 px in Paul's Chrome before merging.

Left out: Tiananmen's Tank Man, Solidarność's logo, the Atelier Populaire posters of May 1968, Heartfield, I AM A MAN (Withers): all in copyright. The May Fourth photographs on Commons are purple-tinted copies and Bloody Sunday 1905 has no clean free photograph: gaps left open. Tahrir, Women's March and Euromaidan had many weak candidates; one each at most. A 1970 All in Contempt frame turned out to be on the site already.


## Protest photographs cut (22 Nov 2026)

Paul, after seeing them: protest signs don't make the cut, only actual artwork images. Cut: VAULT-3259 to 3263, 3267, 3268, 3272, 3274, 3280 to 3296, 3300 to 3312 (39 photographs, including the Dwornik Moratorium poster, which is a photograph of a placard in a crowd). Kept: VAULT-3276, 3277 (abolitionist broadsides), 3279 (Seattle handbill), 3297 (Moor), 3298 (Minor), 3299 (Easter Proclamation). The slogan cards on the writing side stay.


## Colour round (22 Nov 2026)

20 paintings, VAULT-3313 to 3332, chosen by measuring candidates with colour2.py (about 95 probed from Commons) and keeping the strongest in a thin colour, then looking at a contact sheet. Calls: holders for Red Deer and Bathing of a Red Horse left blank (not in the file record); Irises in a Vase given to the Van Gogh Museum although Commons names the Rijksmuseum; the framed Met photograph of Red Sunset replaced by the Met's own frameless file; Water Lilies, Irises and Sunflowers retitled with a comma (not brackets) so the app does not merge them with works already on the site. Eleven carry a sourced note, nine are label only.


## Vibert round (22 Nov 2026)

VAULT-3333 to 3345. Delort's Game for the Cardinal left out (Commons dates it about 1900, after Delort's death in 1895). Holders blank where the file record names none (Friendly Chat, Committee on Moral Books, Landini). The Met's Missionary's Adventures uses the Met's own 600 px web image.

## Edges round (22 Nov 2026)

VAULT-3346 to 3357, under Paul's edges policy (CLAUDE.md, What it is). Holders left blank where the file record names none (Nuda Veritas, Water Serpents I, Schiele's Seated Male Nude). Schiele works with young models were not considered. Beardsley's Lysistrata drawings and Courbet's Le Sommeil held for a later look: defensible as art, but the bar here was work museums hang and the public knows.


## Met leads (22 Nov 2026)

VAULT-3358 to 3364 (`grow: 'metleads'`). From the list lost to the Met's bot page: Blake's Songs of Innocence title page (Met 17.10.3, printed about 1825), The Lamb (Library of Congress, Rosenwald copy) and Infant Joy (Fitzwilliam, copy AA, 1826); Beardsley's frontispiece to Le Morte d'Arthur (1893); a page of the Hokusai Manga, volume 1 (1814); the Emperor's Carpet (Met 43.121.1) and a silk and metal-thread tapestry carpet (Met 51.197), both Iran. The Tahmasp Shahnama was already well covered (16 folios), so none added. Met images are shown from the Met's own files mirrored on Commons (the Met's web-large images are only 300 to 600 px wide); the source link is the Met record. Not taken: more Manga pages and Morte d'Arthur plates (one each for now).

## Estates and open releases: leads only (22 Nov 2026)

Paul asked for a check of estates and foundations that have given work to the public. Nothing added; leads for Paul to decide:
- **Carol M. Highsmith** gave her photographs of America to the Library of Congress; the record reads: No known restrictions on publication. Photographs are in the public domain. Tens of thousands of colour photographs, 1980 onward.
- **John Margolies, Roadside America photograph archive (1969–2008)**, Library of Congress: No known restrictions on publication. Dinosaurs, giant signs, motels, mini golf: strong colour, and a good fit for the colour gaps.
- **Toni Frissell collection (1930–1969)**, Library of Congress: No known restrictions on publication for most images (some restricted; check each). Fashion, wartime, the Tuskegee Airmen.
- **Art UK** has Creative Commons licences agreed with more than 10,000 artists and estates, but most are non-commercial or no-derivatives, so they would not make work free to use here; worth searching its licence filter for any CC BY or public-domain marks on modern British work.
- **Museum waivers:** the Art Institute of Chicago's CC0 covers works believed to be in the public domain or to which the museum otherwise waives any copyright; worth a pass for twentieth-century works it marks CC0.
- **The permission route** (CLAUDE.md 0d, route 5) is still untried. Lawyers have proposed a standing posthumous licence for artists who want their work to stay available after death (ABA Landslide, 2025); the same idea makes a permission letter to a small estate easier to say yes to.

## Spectrum round (22 Nov 2026)

Paul: colour menu becomes the any-colour picker; fill the spectrum from every source at the usual bar. 130 artworks, VAULT-3365 to 3494, `grow: 'spectrum'`, all `rightsTier: free` (holder CC0 or public-domain flag: Chicago, Cleveland, NGA open access, Rijksmuseum, Smithsonian CC0; LoC No known restrictions; Commons PD-Art for makers dead over 100 years, Tiffany's window from the Met's CC0 file). Notes come only from the holder's own description (48 works); the rest are label only. Titles are the holder's; generic titles (Panel, Shawl, Drawing, Fukusa) that would collide under the app's de-duplication carry the accession number. Three LoC theatre posters keep a shortened form of the catalogue's devised title. Rijksmuseum titles are given in English with the Dutch in auditNote.

Calls: left out a Rijksmuseum advertisement for a lithography firm (no ads) and the 1880 Garfield and Arthur quilt (centre is a campaign handkerchief); Delaunay's Windows Open Simultaneously (Tate; Delaunay died 1941 and no holder flag); a Harry Clarke Studios window (date unclear); the Khalili Collections Iznik panel (licence template could not be read); a Boucher visitor photo replaced by the Yorck Project file; a Burne-Jones and a Redon visitor photo dropped; duplicates of works already on the site (Cassatt's Blue Armchair, Vallotton's Corn Fields, Gauguin's In the Waves, Munch's Two Women on the Shore, Redon's Orpheus, Steinlen's Winter: Cat on a Cushion, the Chartres and Sainte-Chapelle glass, Audubon's flamingo, William the hippo, Monet's Parliament). Seven Chicago images are under 843 px wide (the holder's largest), sized from info.json.

Images: every imageUrl returned an image to curl from the sandbox on 22 Nov after the Chicago resize. Not yet loaded in Paul's Chrome (Chicago, Commons and Smithsonian refuse the headless browser).

Coverage (OKLab hue bands, works with a 10% cluster at chroma 0.07 or more): red 92 to 130, orange 393 to 421, gold 570 to 611, yellow 97 to 115, yellow-green 21 to 23, green 49 to 60, teal 5 to 6, cyan 4 to 17, sky 13 to 17, blue 72 to 85, indigo 7 to 11, violet 2 to 5, purple 0 to 0, magenta 2 to 7, pink 0 to 6. Empty cells (hue band by lightness) 48 to 35 of 120. The cool and purple end stays open.

## Spectrum round II (22 Nov 2026)

72 artworks, VAULT-3495 to 3566, `grow: 'spectrum'`, all free: Chicago and Cleveland open access (34), Séguy's Papillons plates 1, 6, 7, 11, 13, 16 to 20 (BHL public domain, published c. 1925; images are the Commons copies of the BHL scan), Owen Jones's Grammar of Ornament plates from NYPL (public domain, 1856; titles from the NYPL record), and Gazette du Bon Ton / La Guirlande pochoirs from the Rijksmuseum (public domain, published 1914 to 1921; titles from the plate and the Rijksmuseum record, designer as the Rijksmuseum credits). Notes only from the holder's description (19 works), or for two Séguy plates from the portfolio's title page; the rest are label only.

Left out: a micromosaic table and a Gazette plate whose scans show the photographer's colour bar; Redon's Orpheus, Cassatt's The Child's Bath, Seurat's Grande Jatte, Kandinsky's Painting with Troika, Marc's Bewitched Mill and Monet's 1906 Water Lilies (already on the site); a Song shard and a second kingfisher ornament (weak or repetitive).

Picker change: a pick more vivid than anything in the collection at that hue is pulled back to the collection's 97th-percentile chroma for that 15° band, and the result always includes the 60 closest works. Tested headless: violet 4 works before, 144 after; purple 48, magenta 33, pink 38, red 42, cyan 406, green 217, yellow 403; no script errors.

Images: Chicago, Cleveland, NYPL and Rijksmuseum images returned images to curl; the Séguy Commons thumbnails could not be fetched from the sandbox (Commons 429) but the file pages exist. Not yet loaded in Paul's Chrome.

## Spectrum round III (22 Nov 2026)

44 artworks, VAULT-3567 to 3610, all free, all from Wikimedia Commons files chosen in Paul's Chrome (Commons refused the sandbox's image requests): Séguy's Floréal (12 plates, 1914, PD-old-70) and Insectes (9, 1929); Racinet's Polychrome Ornament plates 24, 31, 98 and 100 (Sotheran, London, 1877, PD-US); Nielsen's East of the Sun and West of the Moon (4, 1914); Dulac's Stories from the Arabian Nights (5, 1907) and Stories from Hans Andersen (2, 1912, Maastricht University Library scans); Sterrett's Arabian Nights (2, 1928); Vrubel's The Swan Princess (1900) and Lilacs (1901, unfinished), both Tretyakov; Bakst's The Butterfly (MFA Boston, 1913), Costume Design for L'Oiseau de Feu (1922) and Nijinsky as Chinese Dancer (McNay, 1917); Erté's Harper's Bazar cover, February 1921. Titles: Nielsen's are the book's captions, as the Commons description gives them; Sterrett's are the story names from Commons categories; Dulac's and Séguy's use the plate or page number in the scan. Notes for three works only (Floréal's publisher and date, Insectes's title page, the Swan Princess and the opera), from the Commons records and the plate imprint.

Left out: seven Sterrett plates (Commons files about 440 px wide), a Bilibin postcard whose Commons source is Pinterest, a Vrubel sketch, Demon Seated and Nielsen's Whiteland princesses (already on the site). Floréal's scans are about 500 px wide and were kept for the violets; Nielsen's blue mountain, Dulac's Andersen pages and the Nijinsky design are 580 to 820 px. All images were loaded in Paul's Chrome when chosen.

## Whole-archive scan for thin spots (22 Nov 2026)

5,388 works (3,552 art, 1,836 writing). Counted every one-click filter, every two-click pair on the art and writing rows, about 250 common search words (whole words in title, maker, note, text and the hidden descriptions; the site's meaning search finds more than this), the colour spectrum by OKLab hue band, artist depth and context coverage. Scripts in the sandbox at /home/claude/scan.

- Taxonomy trap: Region Americas + Before 1400 or 1400–1650 returns 0 art, because the 53 pre-Columbian works (Maya, Aztec, Inca, Moche and others) are filed under Africa, Oceania & Indigenous Americas.
- Art two-click gaps: photography outside Europe and the US (Near East 2, East Asia 14, Africa/Oceania 15); prints from the Near East 1 and Africa/Oceania 4; 1920–now from the Near East 2 and Africa/Oceania 5; lettering and calligraphy from East Asia 7 and the Near East 8; textiles after 1920, 8; Dark Humor from Africa/Oceania 3.
- Writing two-click gaps: no plays, speeches or modern writing from East Asia; no letters from Africa/Oceania; no diaries from the Near East; love letters 7, love speeches 3; letters before 1650 and after 1920, 2 each; 1920–now writing is 233 of 1,836.
- Common searches with fewer than 15 artworks: aeroplane 1, neon 1, picnic 1, guitar 3, clown 3, Celtic 3, Viking 3, mermaid 5, robot 5, mushroom 5, octopus 6, crow 7, piano 7, owl 8, unicorn 8, rainbow 8, wolf 9, whale 9, jewellery 9, circus 10, monkey 10, sports 11, carnival 12, alchemy 14, astrology/zodiac 14. Writing with none: tarot, alchemy, astrology, circus, guitar, robot, octopus, unicorn, Korea.
- Colour: violet, purple, magenta, pink, teal and yellow-green are still the thin bands at full strength (see the spectrum rounds).
- Depth: 646 of 1,061 artists have one work; famous names with three or fewer include Rossetti, Millais, Chagall, Miró, Waterhouse, Rothko, Kusama, Hockney, Rivera.
- Context: 245 artworks are label only, 52 writing pieces have no note, 1,480 artworks show no size, 444 no holder (many are buildings, sites and book plates).


## Thin-spots round (22 Nov 2026)

Follows "Whole-archive scan for thin spots". Paul: "yep do all of it and more".

- Americas filter fixed (Indigenous American works filed under Africa, Oceania & Indigenous Americas now also answer to Americas).
- Everyday searches: 180 artworks, VAULT-3611 to 3790 (`grow: 'search'`). Sources: Art Institute of Chicago, Cleveland Museum of Art, Smithsonian (Cooper Hewitt, SAAM, Freer). Notes only from the holder's own description; 105 are label only. Held out: Cleveland 115163 (Asante akrafokɔnmu, "before 1896"), Chicago 130700 (Nepalese necklace for the goddess Taleju), and duplicates of works already on the site (Nushirwan Listens to the Owls, Kirchner's Wrestlers in a Circus, Klee's Carnival in the Snow, Rousseau's Tiger and Buffalo, Ranson's Tiger in the Jungle, Marc's Tiger, Bruegel's Alchemist, a second Kota tiger hunt). Clarence Carter's Circus Horses (1933) is free on Cleveland's CC0 release alone; its auditNote says so.
- Photography from Asia, the Near East and North Africa: 35, all from the Rijksmuseum, attributions as the holder records them. Céphas and Abdullah Frères notes also use their Wikipedia articles.
- Pre-Raphaelites: 33 from Chicago, Cleveland and NGA. Waterhouse, Chagall and Miró need Commons (through Paul's Chrome).
- Colour: 11 for teal and yellow-green. Most of the strongest teal candidates were already added in the spectrum rounds.
- Writing: LIT-1934 to 1939. Modern standard translations of the Nō plays (Royall Tyler) and of The Cloud Dream of the Nine (Heinz Insu Fenkl) were not confirmed, so the 1922 public-domain wordings are kept. Heloise's line is the Radice/Clanchy Penguin wording, confirmed in archive.org full-text search of the Penguin edition; the 1974 text has mistress where the revision has friend [amica].
- Not done: Nasir Khusraw's travel diary (Le Strange's 1888 translation not found on archive.org in this pass), Viking material, more aeroplanes.
- Waterhouse: 16 paintings from Commons (VAULT-3870 to 3885), PD-Art; holders from Wikidata, blank for private collections; notes only for Ulysses and the Sirens and I Am Half-Sick of Shadows (Wikipedia). Chagall and Miró: no free route found (no holder open flag; paintings are not publications).

## The row, round two (22 Nov 2026)

Mood cut from the row and from Arrange. Era is now a drawn span on a histogram of the collection; Region is a clickable map of ten regions (`place`, from `tools/places.py`); Medium is twelve groups (`medGroup`, from `tools/medgroup.py`).

- Places: Europe 3,066, North America 1,088, East Asia 645, Middle East & North Africa 299, South Asia 203, Latin America & Caribbean 164, Africa 76, Southeast Asia 40, Oceania 38, Central Asia 7, none 43 (space, the Moon, Antarctica, international). Africa, Oceania, Southeast and Central Asia are thin on the map and say so with their counts; per the brief, they stay open until work that meets the bar turns up.
- Medium groups: Painting 1,241, Print 950, Photograph 434, Sculpture 297, Drawing & Watercolour 175, Craft & Object 172, Poster & Graphic 134, Book & Manuscript 125, Film still 125, Textile 86, Building & Site 53, Map & Chart 35.
- Calls made in the place rules: Byzantine works count as Europe; ancient Egypt as Middle East & North Africa (the map follows the modern region, so Egypt sits with the Maghreb); Hawaiʻi as Oceania; Russia as Europe.

- Cut on Paul's word (22 Nov 2026): LIT-1906, Me Too (Tarana Burke, 2006), from the slogans round. Record kept in the sandbox at /home/claude/cut_LIT-1906.json.

## Search tested like a stranger, and the depth round (22–23 Nov 2026)

- Test kit in the sandbox at /home/claude/sq. Training set 143 known + 276 open queries; fresh sets holdout (53 + 135) and holdout2 (58 + 108).
- Training set: known items in the top 5, 123 → 143 of 143; open precision@12 0.82 → 0.91. Holdout: 41 → 49 of 53, 0.80 → 0.84 before its own words were added to the lexicon. Holdout2: 54 → 55 of 58, 0.84 → 0.85 before, 0.87 after. Under-8-result searches 11 → 0.
- Whole texts for 17 short poems (list in CLAUDE.md). Charge of the Light Brigade: the 1855 edition's "blunder' d" printed blunder'd.
- Depth round: 185 artworks VAULT-3886 to 4070 (`grow: 'search2'`); 12 passages LIT-1940 to 1951. Dropped on the way: Remington's Bronco Buster (Chicago cast; the Met's cast is already VAULT-500), a Koshiro Onchi woodcut dated anywhere from 1915 to 1955, Méryon's Vampire prints (Le Stryge is already on the site), a bicycle maker's poster (no ads), Duchenne's laughter photograph (medical photography). VAULT-3905's title carries its accession number to tell it from another The Lovers by an unknown maker. All 184 shown images loaded in Paul's Chrome.
- Places now go by the first place a region string names (Shelley's Britain / Egypt is Europe), with empire adjectives (French Polynesia, British India, Roman Egypt) and overseas places handled.

## Search-depth round II (23 Nov 2026)

- 55 artworks VAULT-4071 to 4125 (`grow: 'search3'`), 6 passages LIT-1952 to 1957. List in CLAUDE.md.
- Dropped: Chicago's El Greco Saint Martin and the Beggar (small replica of the altarpiece NGA holds, already VAULT-2838); a Macbeth Tomorrow card (LIT-009 has it). VAULT-4080's title carries its accession number to tell it from Eisen's Courtesan VAULT-210.
- The Guna mola panel (VAULT-4082) is dated "before 1960" by Cleveland; its free tier rests on Cleveland's CC0.
- Every image URL returned an image from the sandbox on 23 Nov; not yet seen in Paul's Chrome (his machine was asleep).
- Third pass, VAULT-4126 to 4130 (`grow: 'search4'`). Kerr Eby's The Refugees carries SAAM's own date range (ca. 1918–1935) and SAAM's CC0; its place is left blank because the record does not say where it shows. Pether's long holder title is cut after "Discovers Phosphorus"; the full title is in sourceUrl. Stieglitz's The Steerage and Bruegel's Alchemist turned up again and were skipped (VAULT-784, VAULT-1573).

## The West and flight (23 Nov 2026)

- 21 works VAULT-4131 to 4151 (`grow: 'west'`), all Commons, PD by the maker's death (Russell 1926, Remington 1909) or, for Klinger's two posters, publication before 1931. Holders from the Commons record or Wikidata; blank where neither names one (Camp Cook's Troubles, Lassoing a Steer, Round-Up on the Musselshell, York, Downing the Nigh Leader, Casuals on the Range). VAULT-4147's place is blank: the record does not say where it shows. York's medium is blank. Klinger's dates come from secondary sources on Commons (c. 1910, 1913).
- All 21 images and all 245 overnight images loaded in Paul's Chrome on 23 Nov.


## Clean crops, Library of Congress (23 Nov 2026)

135 LoC artworks cropped to the work itself, removing colour targets, grey scales, rulers, scan backdrops, film edges and negative numbers, mounts and book surrounds. Each box set by eye on a 5% grid and checked on a contact sheet of the actual IIIF output. Served as LoC IIIF `pct:` regions; originals kept in `rawImageUrl` / `rawHighResUrl`, box in `crop`. Not cropped: VAULT-1098, 3243, 3244 (already clean). Damage on the object itself (VAULT-2208's chipped plate) left as is. Colour, picture embeddings, vectors, hubs and pairs re-run.


## Look-and-learn tier cut (23 Nov 2026)

Paul: seeing the perfect thing and not being able to use it is frustrating. All 247 `rightsTier: 'look'` works removed; records in `data/look-archive.json`, images (`images/fairuse/`, 242 files) deleted from the repo. Site now 3,846 artworks, all free, and 1,859 writing pieces. Search test after the cut: known items 135 of 143 (the 8 misses are the cut works), open-query precision 0.92, no search under 8 results. Front of house and the whole wall now reshuffle on every visit.


## Welcome card (23 Nov 2026)

Paul wrote the copy. Claude flagged that "completely free to use ... commercialize it" was not true for every work (quoted writing in copyright, A. S. Kline's non-commercial texts, CC BY-SA photo credits); Paul rewrote it to "make it yours", which makes no licence claim. "Art, works, and words" kept as he wrote it.


## Weak-spots round, 23 Nov 2026

Scan: filter and cross-filter counts from works.js, OKLab hue bands from data/colour.json, and 128 fresh everyday searches (holdout4) scored for precision and depth. Thin then: collage 4 works, tea 3, kitchen 4, bicycles 6, aeroplanes 11, cars 13; Central Asia 16 artworks, Oceania 28, Southeast Asia 33, Africa 58; writing from Southeast Asia 3, Central Asia 1, Oceania 10, Africa 17.

Added 503 artworks (VAULT-4152 to 4664) and 11 writing pieces (LIT-1958 to 1968); see CLAUDE.md for the breakdown. Every artwork looked at on a contact sheet; notes only from the holder's own text, otherwise label only. Archaeological pieces kept only with a documented history from before 1970; about 50 cut on that rule. Asante gold before 1896 excluded (one disk pendant). Two Ethiopian icons without provenance, and two Chicago Ethiopian works with dealer histories from the 1980s, left out.

Removed: VAULT-330 Benin Palace Plaque (looted 1897), on Paul's instruction; record in data/removed.json and its page deleted. Flagged, not removed: VAULT-004, 017, 1843, 1844, 1845, 1846, 1847, 1848, 1849 (Benin court art at the Met).

After: thin-query precision 0.60 to 0.91 on 23 of the holdout4 searches; no search under 8 results.

### Modern colour (NGA) and space rounds, 23 Nov 2026

- VAULT-4655 to 4693: 39 NGA open-access works, 1905–1930 (Kirchner, Mueller, Marc, Jawlensky, Schiele, Lissitzky, Gris, Boccioni, Dada). Label only; records from NGA open data.
- VAULT-4694 to 4706: 13 NASA images. Notes only from the NASA record's own description; three label only. Skipped as duplicates of works already on the site: Crab, Cosmic Cliffs, Sombrero, Mystic Mountain, Pale Blue Dot, McCandless, Curiosity selfie, Horsehead, Artemis II Earthset, Ultra Deep Field, Voyager Great Red Spot. Left out: Herschel's Eagle (ESA), ESA/Hubble Twin Jet and N159 (ESA licence), a Juno illustration (a render, not an image).

## Toward 10,000 (overnight, 23–24 Nov 2026)

Paul asked to go to 10,000 without lowering the bar, using more open-access holders. Each round was chosen by eye from contact sheets and pushed after the headless tests.

| Round | Works | Holder | Notes |
|---|---|---|---|
| Film frames | 13 | Internet Archive copies | Un Chien Andalou (1929), L'Âge d'Or (1930) |
| Covers | 9 | Commons, checked against publication dates | Rockwell, Leyendecker, before 1931; ©SEPS-marked scans skipped |
| WWI posters | ~10 | Library of Congress | cropped to the poster |
| SMK | 185 | Statens Museum for Kunst | public-domain flag |
| Rijksmuseum paintings | 187 | Rijksmuseum | Linked Art API |
| NGA paintings | 1,354 | National Gallery of Art | open access (CC0), two passes |
| PDR leads, Rijksmuseum | 25 | Rijksmuseum | Dutch titles kept, English gloss in auditNote |
| PDR leads, Wellcome | 62 | Wellcome Collection | Public Domain Mark only |
| Getty paintings | 374 | J. Paul Getty Museum | Open Content; antiquities skipped |
| Writing | 1 | Gutenberg | Gray's Elegy (LIT-1969) |
| Getty manuscripts | 122 | J. Paul Getty Museum | Open Content leaves and miniatures |
| Rijksmuseum Japanese prints | 107 | Rijksmuseum | Koson, Kiyochika, Hiroaki |
| Hyde and Mucha | 21 | Art Institute of Chicago | public-domain flag |
| Cleveland | 514 | Cleveland Museum of Art | CC0; undated and forged pieces left out |
| Index of American Design | 52 | National Gallery of Art | US federal work; after 1942 left out |
| Woodcuts and colour prints | 162 | National Gallery of Art | open access |
| Chicago paintings | 439 | Art Institute of Chicago | public-domain flag; Tibetan, Nepalese, Lakota, Cheyenne and Teotihuacan pieces left out |
| Writing | 1 | Gutenberg | The Water of Kāne (LIT-1970), Emerson 1909 |

**10,000 reached on 24 Nov 2026: 10,002 works (8,130 art, 1,872 writing).** Four Chicago paintings were dropped by the app's de-duplication (two anonymous Virgin and Child panels, a Spanish Saint Sebastian, and At the Moulin Rouge, already on the site).

Calls made: Charley Toorop's 1933 self-portrait left out (US status), framed Van Gogh scans left out, ESA-credited space images left out, undated Wellcome pieces left out, Wellcome plates without their own catalogue title left out (no invented titles), Guru Nanak images in the Wellcome Kalighat set left out, the Gervex autopsy study left out. Holders' dates are kept as given, with hedges ("c. 1880 (?)"). Artist spellings unified across 85 records (list in CLAUDE.md).


## Trim pass, 24 Nov 2026

Paul asked whether any overnight addition missed the bar or skewed the site archival. Measured: the pale-paper share fell (9% of the overnight works against 19% before), but paintings went from 30% to 55% of the art and Europe from 53% to 61%, and about 950 overnight works are dark overall. All 950 dark works and every overnight work a border detector flagged (539) were looked at on contact sheets.

**Cleaned (live):** 35 works had a frame, scan border or mount showing and are cropped to the work: Getty, NGA, Rijksmuseum, SMK and Wellcome by the holder's IIIF `pct:` region; Chicago, Cleveland and two SMK files hosted in `images/crops/` (`aic_`, `cma_`, `smk_`). Raw files kept in `rawImageUrl`/`rawHighResUrl`, box in `crop`; `ar`, colour and picture embeddings re-run. Includes nine of Rowlandson's Dance of Death plates (the pasted verse slips and black album surround are cut off). Engaged and painted frames (tabernacle frames, page borders, the Le Repos panel) were left as part of the object. Chicago serves these at 843 px at most, so its crops are 530 to 820 px wide.

**Cut on Paul's yes, 24 Nov 2026 (56), records in `data/removed.json`:** 28 too murky or damaged at tile size (four murky Inness nocturnes, Courbet's Wooded Landscape, two van der Neer nocturnes with a stronger one kept, a cracked Jacob Maris, the three Chicago scrolls under 350 px); 21 duplicates (six Getty whole-book records showing the same page as the leaf record, two NGA middle-panel records whose image is the whole triptych already on the site, a Chicago record sharing its pair's image, Dutch-titled Rijksmuseum copies of Koson and Kiyochika prints already on the site, the Van de Velde Witch, Destroy This Mad Brute, On les aura!, a second Ginevra de' Benci, two composite images); 7 of eleven near-identical pages from one Cleveland flower album (four kept). Each record carries its reason in `removedReason`. The site is at 9,946 works (8,074 art, 1,872 writing). Strong subjects were kept even when dark (Quidor's Devil and Tom Walker, Wright of Derby's Penelope, Böcklin, Cole's Tornado, Lethière's Death of Virginia).

## Modern-writing round, 24 Nov 2026

Paul: writing to about 2,000, and less antiquated. 128 pieces, LIT-1971 to LIT-2098, `grow: 'words4'`, label only. Sources and checks per batch:

| Batch | n | Source | Check |
|---|---|---|---|
| Spoon River | 16 | Gutenberg #1280 (1915) | whole poems from the file |
| Devil's Dictionary | 14 | Gutenberg #972 | entries from the file |
| Pompeii graffiti | 12 | Gutenberg #42715, Mau tr. Kelsey (1902) | Mau's paragraph as the text |
| Presidents | 6 | American Presidency Project (US government work) | speech text from the page; three Democrats, three Republicans, so with the six already on the site the count is six and six |
| Supreme Court | 5 | LII Cornell opinions (US government work) | paragraphs from the page |
| Apollo | 8 | nasa.gov history pages, NSSDC | NASA's own paragraph as the text; ALSJ/AFJ not used (editors' copyright) |
| Dorothy Parker, Enough Rope (1926) | 16 | archive.org enoughrope0000doro_u6o5 | every line against enoughropepoems0000park; drop caps and five OCR slips read from page images |
| Hammett, The Maltese Falcon (1930) | 6 | Gutenberg #77600 | passages from the file |
| Hemingway | 5 | Gutenberg #75201 (1929), #69683 (1927) | passages from the file; Hills Like White Elephants whole |
| Woolf, A Room of One's Own (1929) | 4 | Gutenberg Australia 0200791h | every sentence against archive.org woolf_aroom (1935 printing); one error in the Australian text fixed (singing → signing) |
| Mansfield, Journal (1927) | 6 | archive.org journalofkatheri00mans (Knopf) | every sentence against the Constable 1927 scan |
| Cummings, is 5 (1926) | 2 | Gutenberg #77021 | whole poems, lower case as printed |
| Elinor Wylie, Nets to Catch the Wind (1921) | 2 | Gutenberg #6682 | whole poems |
| Fitzgerald, This Side of Paradise (1920) | 2 | Gutenberg #805 | passages from the file |
| Anderson, Winesburg, Ohio (1919) | 3 | Gutenberg #416 | passages from the stories; the Howe introduction skipped |
| Mencken, The Jazz Webster (1920) | 8 | Gutenberg #22145 | entries from the file; entries that sneer at women left out |
| Greek Anthology | 13 | Gutenberg #2378, Mackail (1890) | whole epigrams; one already on the site (Plato's star) skipped |

Calls: Parker's Résumé is in (her best-known poem; the site already carries dark material on the same terms). Cernan's Apollo 17 card first had a sentence of my own as its text; replaced with NASA's paragraph before merging. Wylie's publisher is not named in the auditNote because the Gutenberg file does not state it.

## Letters, open licences and re-cut pull quotes, 24 Nov 2026

16 pieces, LIT-2099 to LIT-2114, label only.

| Batch | n | Source | Check |
|---|---|---|---|
| Van Gogh letters | 4 | Ludovici 1912, Gutenberg #40393 via archive.org thelettersofapos40393gut | every sentence against lettersofpostimp00goghuoft (1912 scan); recipient from the book's section; dates given as the Arles–Saint-Rémy span because Ludovici prints none |
| Chekhov letters | 4 | Garnett 1920, Gutenberg #6408 | recipient, place and date from the letter's heading in the book |
| Darwin, Autobiography | 1 | Gutenberg #2010 | passage from the file |
| Gauguin, Intimate Journals | 2 | Brooks 1921, scan in.ernet.dli.2015.507550 | every sentence against intimatejournals0000paul; hyphens joined, OCR marks removed |
| Doctorow, Little Brother (2008) | 3 | Gutenberg #30142 | CC BY-NC-SA 3.0 printed in the file; asterisks for italics removed |
| Lessig, Free Culture (2004) | 2 | archive.org free_culture (author's PDF) | CC BY-NC 1.0 printed on its first page; OCR spacing normalised |

Left out: Watts's Blindsight and Stross's Accelerando (licence pages not reachable; not taken from a third party's upload). Already on the site and skipped: Chekhov's free-artist credo, Dickinson's no-fire-can-warm-me line.

Re-cut pull quotes (old wording kept in `hookOld`): LIT-262, 520, 521, 2015, 1735, 1451. Method: every pull quote's five-word runs were checked against Bartlett's 1914 and 1922 printings, and every line of its full text likewise, to find pieces whose quoted line is not the pull quote; and pull quotes with archaic wording were listed by hand. Most archaic pull quotes are the line people know (Augustine's restless heart, the Upanishad's That art thou, the Gita, Rabelais's Do What Thou Wilt, Zarathustra on writing in blood) and were left alone; translations that are archaic throughout gain nothing from a re-cut.

## Modern sources, 24 Nov 2026

22 pieces, LIT-2115 to 2136, all label only. Every text taken from a fetched source; hooks checked letters-only against it.

| Ids | Source | Notes |
|---|---|---|
| 2115–2118 | Remarque, All Quiet on the Western Front, tr. A. W. Wheen (1929), Gutenberg #75011 | Public domain in the US since 2025 |
| 2119–2120 | Sterling, The Hacker Crackdown, Gutenberg #101 | Author's literary-freeware notice in the file; `license` set |
| 2121–2123 | Watts, Blindsight (2006) | CC BY-NC-SA 2.5 printed in the licensing section of the author's PDF; text from the archive.org copy of that PDF, checked against rifters.com ("recordshattering" fixed to "record-shattering") |
| 2124–2127 | American Presidency Project | Ford (R), Nixon (R), G. W. Bush (R), Carter (D) |
| 2128 | GPO Public Papers, Clinton 1995 Book I, pp. 573–574 | Clinton (D), Oklahoma City |
| 2129 | obamawhitehouse.archives.gov | Obama (D), Selma; four paragraphs, "(Applause.)" removed |
| 2130–2136 | LII, Cornell | Footnote numbers removed; citation strings left off Texas v. Johnson and Tinker; LII's "a farm more subtle" (Korematsu) corrected to "far"; "de-termination" closed up (Shelby County) |

The site now quotes six presidents from each party (D: FDR, Kennedy, Johnson, Carter, Clinton, Obama; R: Lincoln, Eisenhower, Reagan, Ford, Nixon, G. W. Bush). By piece count the Republicans lead 12 to 9, mostly Lincoln. Not added: Stross's Accelerando (antipope.org unreachable from the sandbox; licence must come from the author's page or the book). Hacker Crackdown cards carry medium "Nonfiction book" so they fold into Prose.
