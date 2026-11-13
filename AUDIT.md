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

## Not yet audited

The 500 artworks (titles, artist credits, dates, museum attributions) have not been through this process.
