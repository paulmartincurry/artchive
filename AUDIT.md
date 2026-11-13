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

### Still loose (16)

A usable source probably exists (noted in CLAUDE.md) but was not reached.

- LIT-290 Friedrich Hölderlin, *Hälfte des Lebens*
- LIT-300 Farid ud-Din Attar, *The Conference of the Birds — The Valley of Astonishment*
- LIT-302 Antarah ibn Shaddad, *Muʿallaqa of ʿAntara*
- LIT-314 Nizami Ganjavi, *Haft Paykar (The Black Dome)*
- LIT-325 Thiruvalluvar, *Tirukkuṛaḷ*
- LIT-328 Sant Tukārām, *Abhang*
- LIT-344 Masaoka Shiki, *Haiku (Persimmon)*
- LIT-391 Annette von Droste-Hülshoff, *Am Turme (On the Tower)*
- LIT-402 Anton Chekhov, *Letter to Lazarev-Gruzinsky (1 Nov 1889)*
- LIT-415 Delmira Agustini, *Lo inefable*
- LIT-448 Abu'l-Qasim Ferdowsi, *Shahnameh (conclusion)*
- LIT-476 Simón Bolívar, *The Jamaica Letter*
- LIT-484 Nella Larsen, *Quicksand*
- LIT-130 Traditional Tantric Sanskrit Hymn, *Karpuradi Stotra*
- LIT-184 Napoleon Bonaparte, *Farewell to the Old Guard*
- LIT-190 Victor Hugo, *Funeral Oration for Balzac*

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

## Not yet audited

The 500 artworks (titles, artist credits, dates, museum attributions) have not been through this process. Note for that audit: 370 of them hotlink images from Wikimedia, every artwork carries an AI-written `note` and `craftSpec`, and 500 carry a paired `quote` whose wording and attribution have never been checked. All 425 older writing pieces also carry an AI-written `note`, shown under “Notes” in the reader.
