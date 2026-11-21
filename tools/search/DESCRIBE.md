# Brief: plain descriptions for search (hidden, never shown on the site)

The Artchive is an art site. Its search only matches words, so a painting of a woman alone in a diner at night is invisible to someone who types "lonely woman at night" unless those words are in its record. You will write a plain, literal description of what each picture shows. These descriptions are **never displayed**; they are only used to match searches. Accuracy matters more than style.

## Your batch
You get a range of contact sheets in `/home/claude/vis/sheets/`. Each `sNNNN.jpg` shows up to 9 works with yellow numbers 1–9; `sNNNN.txt` lists, per number: id, title, maker, date, medium (tab-separated).

For each sheet: Read the `.txt`, then Read the `.jpg` (one image per Read call), then describe every numbered work.

## What to write, per work (25–45 words)
- What is depicted: people (how many, what they are doing, clothing if notable), animals, objects, setting, weather, time of day, light.
- What kind of thing it is: oil painting, woodblock print, etching, photograph, film still, sculpture, mask, manuscript page, textile, poster, map, plate of jellyfish, etc.
- The main colours and the overall look (dark, bright, misty, crowded, empty, close-up, vast).
- End with 3–6 plain feel words a searcher might use, after "Feel:" (e.g. "Feel: lonely, quiet, nocturnal, urban.").
- You may use the title to name a subject when the picture matches it (e.g. "Saint Sebastian tied to a tree, pierced by arrows", "Mount Fuji behind a giant wave"). Do not repeat the maker's name or the date: those are already searchable.
- Only what you can see. No interpretation of meaning, no praise ("masterful", "stunning"), no guesses about the artist's intent. If you can't make something out, leave it out.
- Nudity, violence or death: state plainly and briefly what is shown ("a nude woman reclining", "a severed head on a platter", "corpses hanging from a tree"). That is fine and needed for search.
- If a cell is blank, black or clearly not an artwork (error page, placeholder), write `"d": "UNREADABLE"`.

## If the picture does not match its title
If a picture is clearly a different work from the title (wrong subject, wrong kind of object), still describe what you see, and add `"mismatch": "<what it looks like instead>"` to that line. This finds broken images on the site.

## Output
Append one JSON object per line to `/home/claude/vis/desc/<your batch name>.jsonl`:
`{"id": "VAULT-123", "d": "…"}`
Write after each sheet (append with a short Python or Bash heredoc), so nothing is lost if you stop. Use the ids from the `.txt`, matched by number. Check the number of lines you wrote equals the number of works.

## Keep your messages short
Do not repeat descriptions in your replies. Final reply: sheets done, works written, any UNREADABLE ids. Under 60 words.
