# Smarter colour: plan (21 Nov 2026). Paul said go with Claude's picks; built the same day on the preview (AUDIT.md, "Smarter colour").

Paul's question: a work with several colours sits as high under each of them as a work that is mostly that colour, which is confusing. He wants all four ideas: strongest first, accents weighed properly, two colours meaning the pair, and any shade. Research and tests first; nothing is built until he says go.

## What the research says

- **Cooper Hewitt** (the model most people cite). They extract up to five dominant colours per image and snap them to a fixed list of named web colours, then search by that list. Colour became the main way people browsed: 48.89% of visits used colour navigation, against 4.39% for normal search. Lesson: colour can carry a collection site, and every swatch should be a link to more of that colour.
- **Google Arts & Culture, Art Palette.** Pick up to five colours, or upload a photo, and it finds artworks with that palette. Lesson: palettes, not single colours, are what designers think in.
- **Dribbble.** Search by a hex colour with a "variance" setting: wide gives more, looser results; narrow gives fewer, closer ones. Each shot shows its colours, and each colour links to a colour search. Lesson: a tolerance setting is useful but optional; the linked swatch is the habit worth copying.
- **Adobe Stock.** A hex colour filter plus a "vivid" slider from muted to bright, and "find similar by colour" from any image. Lesson: vividness is its own axis, separate from hue.
- **Colour science.** Plain RGB distance is wrong for judging how different two colours look. CIELab is better but bends blue toward purple. OKLab (2020) fixes that, and its distance is still simple Euclidean, so it is fast in a browser. CIEDE2000 is a little more accurate on small differences but slower and fussier; not worth it here.
- **Colour names.** English has eleven basic colour terms: black, white, red, green, yellow, blue, brown, orange, pink, purple and grey. Those are the words people type. The site's six families (with their art names) miss orange, brown, pink, purple and grey.
- **Variety.** Maximal marginal relevance (MMR) is the standard way to stop a ranked list repeating itself: each next pick trades how well it matches against how similar it is to what is already shown.
- **Where the colour sits.** Saliency research uses a centre bias: the subject is usually near the middle, so colour there counts more than colour at the edges.

## What our own tests showed (contact sheet: colour_tests.jpg)

Run on all 3,236 measured artworks, eight colour clusters each, with area plus centre-weighted area.

1. **Strongest first works.** "Red" opens on Malevich's red square, Dalí's elephants, Matisse's Red Studio and The Dance, Mondrian's composition, Sargent's Dr Pozzi and a Keith Haring wall. The first screen was already varied without any caps; capping two per artist and eight per medium barely changed it.
2. **Pairs work, but less crisply.** Red with gold, ranked by the weaker of the two, gives Demuth's I Saw the Figure 5 in Gold, Matisse's L'Escargot, Modigliani and Dalí, with some odd ones lower down.
3. **Exact shade is the most striking of the four.** Oxblood brings up Dr Pozzi, McCurry's Afghan Girl, Piero's Duke of Urbino, Gentileschi and Petra by night. Klein blue opens on Matisse's Blue Nude, then WPA posters, Rothko and Anna Atkins's cyanotypes.
4. **Two failures to fix before it ships.**
   - *Paper.* Pale, quiet shades (sage, putty, cream) match the paper of prints and the mounts of miniatures, so a sage search returns Japanese prints on greenish paper rather than green things.
   - *Sky.* Lilac matched photographed blue sky. That is CIELab's blue-purple bend; OKLab should fix it.
5. **Pink and purple are thin as fixed names.** Only 7 works carry real pink and 12 real purple (10% or more of the picture, weighted). The top "pink" results were mostly pink mounts. As fixed names they would look broken; as exact-shade searches they work.
6. **The Mona Lisa** measures as black, brown, green and a little gold. Under strongest first she would sit low in green and gold and nowhere under red, which is the behaviour Paul wants.

## The plan

### A. Measure better (the pipeline, `tools/search/colour.py`, run once)

- Switch from CIELab to **OKLab** for clustering, naming and distance.
- **Eight clusters** per image, each kept with its colour, its share of the area and its share weighted towards the centre.
- **Find the ground.** The low-chroma cluster that covers most of the outer edge is paper, mount or wall. It counts at about a third of its area for everything except Cream and White, so "sage" stops finding paper and a cream print still reads as cream.
- **Vividness counts.** A strong small red outweighs a dull large brown. The current weighting, which already favours saturated colour, carries over.
- **Ignore colour targets.** Some museum scans include a printed colour bar at the edge (the R.U.R. poster has one). Crop the outer 6% as now, and drop a cluster that sits only in a thin strip at one edge.
- **Per-work strength for each named colour**, 0 to 100, stored with the work (about 11 bytes each).
- **Per-work clusters for exact-shade search** in a separate file loaded only when someone uses colour, like see.json: about 130 KB.

### B. Named colours (idea 1, strongest first)

- The Colour menu offers names people actually say. Proposed: **Red, Orange, Gold, Green, Blue, Purple, Pink, Brown, Black, Grey, Cream.** "Gold" stays (it is how people describe ochre, gilding and old varnish in art); "Cream" covers white and paper. Pink and Purple are honest but thin; see decision 1.
- Picking a colour **ranks by strength**. Works where it is only a small accent come lower. Works below a floor (about a tenth of the picture, weighted) are left out.
- **Variety on the first screens:** at most two works per artist in each run of 24, and no more than eight of one medium. MMR is held in reserve if tests show runs of near-identical images.

### C. Two or more colours (idea 3)

- Two colours means **together**: rank by the weaker of the two strengths, so a work has to carry both. The read-back line says "Red with Gold".
- Three colours: the same, ranked by the weakest. This is also the Art Palette idea.
- An "either" mode is not offered. It is what the current version does, and it is the confusing part.

### D. Any shade (idea 4)

- In the Colour panel, under the names: **a strip of named pigments** (vermilion, oxblood, ultramarine, Prussian blue, Klein blue, verdigris, sap green, ochre, Naples yellow, lead white, lamp black, rose madder, Tyrian purple, plus a few more), then a **picker for any colour**.
- **Every swatch in the lightbox's palette row becomes a link** ("more in this colour"). From a work you love, one tap finds its shade across the collection. This copies Cooper Hewitt and Dribbble and is the most "find a thing, keep looking" part of the whole plan.
- Ranking: closeness in OKLab, weighted by how much of the picture is that close colour, with the ground discounted. The list shows the best matches down to a relative floor (a quarter of the top score), so a rare shade still returns something.
- **No tolerance slider at first.** Less UI. Add "closer / looser" only if testing shows people need it.
- The read-back line shows the swatch and its name ("Oxblood"), or a hex value for picked colours.

### E. How colour plays with everything else

- **Colour alone:** strongest first.
- **Colour plus a search word or a mood:** the search leads and colour filters (with a small boost for stronger colour). "Storm" in blue gives storms that are blue, best storms first.
- **Colour plus Arrange:** the arrangement wins (by date, by mood), inside the colour filter.
- **Clear:** back to the daily wall, as now.
- The live site's old six-colour filter keeps working until the preview is approved.

## How it will be checked before Paul sees it

- **A fixed list of 24 test searches with works that must appear near the top:** Red (Red Studio, Malevich), Blue (Blue Nude, Starry Night), Yellow or Gold (Sunflowers, Klimt), Green (Nighthawks?), Black (Goya's Black Paintings), Cream (prints and paper, deliberately), Red with Gold, Blue with Yellow (Starry Night, Hokusai), oxblood, Klein blue, vermilion, verdigris, sage (no paper), lilac (no sky), plus a swatch taken from five lightbox palettes.
- A contact sheet of the first 24 for every test, read by eye. Paul gets the sheets.
- Speed: ranking 3,236 works in the browser must stay under 30 ms on a phone; the cluster file loads only when colour is used.
- The usual headless run on desktop and phone, and the pre-push checks.

## Decisions for Paul

1. **Pink and Purple as named swatches?** They are honest but thin (7 and 12 strong works). Options: keep them (it says something true about the collection), or drop them from the names and let the pigment strip carry rose madder and Tyrian purple. Recommendation: drop them as names, keep them as pigments.
2. **Pigment names or plain names in the strip?** "Oxblood, verdigris, Naples yellow" suits a creative audience and the site's voice; plain hex is clinical. Recommendation: pigment names.
3. **Should colour from a work's palette open a search straight away from the lightbox,** or only when tapped with a hint? Recommendation: tap a swatch and it searches; the swatch shows "More in this colour" on hover.
4. **Does the old colour view (the "Chromatic" view under More) stay?** Once this is built it is redundant. Recommendation: hide it, don't delete it, and decide later.

## Order of work after "go"

1. Re-measure with OKLab, eight clusters, ground and colour-bar handling. Contact sheets per name; tune the boundaries by eye.
2. Strength per name into works.js, the cluster file into data/colour.json, build_pages and make_preview updated.
3. The Colour panel: names, pigment strip, picker; ranking, pairs and floors in preview_tools.js.
4. Palette swatches in the lightbox become links.
5. The 24 test searches with sheets; fix what fails.
6. Headless tests, push to the preview, send Paul the sheets and the link. CLAUDE.md and AUDIT.md updated.

Estimated time: one long session. No describers are needed; the images are already in the sandbox.

## Sources
- Cooper Hewitt Labs: colour search, Rijkscolors, Dive into Color (labs.cooperhewitt.org)
- Google Arts & Culture, Art Palette (artsandculture.google.com)
- Dribbble, Color Coding (dribbble.com/stories/2011/05/26/color-coding)
- Adobe Stock help, colour and vivid filters (helpx.adobe.com/stock)
- Björn Ottosson, OKLab (2020), and the W3C colour workshop notes on Lab and OKLab
- Berlin and Kay (1969), Basic Color Terms; Wikipedia, Color term
- Elastic, Maximum Marginal Relevance (elastic.co/search-labs)
- Center-bias saliency (arXiv 1501.03383)
