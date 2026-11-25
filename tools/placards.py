#!/usr/bin/env python3
"""Placards for work that is not on the wall.

A search that is plainly for one work or one maker the site does not have shows
one blank wall label as the first tile of the results (Paul, 25 Nov 2026). This
tool writes data/placards.json, the list of searches that trigger one. Run from
the repo root, and again after any round that adds works:

    python3 tools/placards.py            # print what would trigger, write nothing
    python3 tools/placards.py --apply    # write data/placards.json and tools/placards/wanted.json

Two sources:

  1. data/look-archive.json: the 247 works cut on 23 Nov 2026. Checked one by
     one, so the hand-kept lists below (ONE_WORD, DENY_TITLES, NICKNAMES,
     SURNAMES) decide what triggers.
  2. tools/placards/wikidata.json: about 3,400 well-known makers, artworks,
     films and poems, ranked by how many Wikipedia editions cover them (pulled
     by tools/placards/fetch_wikidata.py). Each is sorted into one of three:
       here      the site has it, or has the maker: nothing to do
       wanted    it could be free (made in or before PD_YEAR, a public-domain
                 mark, a maker born before 1850): no placard, it goes on the
                 shopping list in tools/placards/wanted.json
       placard   made after PD_YEAR, or the maker was born in 1910 or later:
                 "It is not free to use." A maker born 1850 to 1909 who is not
                 on the site gets the label with no reason line, because early
                 work may be free and the card must not claim otherwise.

Rules for what triggers (Paul, 25 Nov 2026): only a search plainly for that
work or maker. Never on the wall, never for a theme, one per search.

  - a title typed exactly, when it has two words or more, is not also a title
    on the site, is not a phrase in the search lexicon, and (for the wide list)
    holds at least one word the site's own text almost never uses, so Morning
    Sun and Modern Times do not fire but Citizen Kane does
  - a title with its maker before or after it (worked out in the browser from
    the `titles` and `makers` indexes), or a film title with "film", "movie" or
    its year, or a poem's with "poem"
  - a maker's full name; a surname alone only from SURNAMES, or for the wide
    list when it is unique, at least five letters, never used in the site's
    text and not in DENY_SURNAMES
  - a bracketed gloss in a title ("after Hokusai", "Dead Sea") never triggers
    on its own; add it to NICKNAMES if it should

Matching is on a normalised string (accents off, lower case, anything that is
not a letter or digit becomes a space). index.html does the same in pNorm().
"""
import datetime, json, os, re, sys, unicodedata
from urllib.parse import urlparse, quote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARCHIVE = os.path.join(ROOT, 'data', 'look-archive.json')
WORKS = os.path.join(ROOT, 'data', 'works.js')
LEXICON = os.path.join(ROOT, 'data', 'lexicon.json')
OUT = os.path.join(ROOT, 'data', 'placards.json')

# Single-word titles that are safe to match alone. Everything else with one
# word (Flag, Jazz, Gas, Mao, Mural, Vertigo, Psycho, Dracula, M …) needs the
# maker's name beside it.
ONE_WORD = {'guernica', 'golconda', 'tuttomondo', 'abaporu', 'whaam', 'automat',
            'rashomon', 'vampyr', 'godzilla', 'akira', 'maman'}

# Titles of two words or more that read as a theme or a person, not as a hunt
# for this work.
DENY_TITLES = {
    'self portrait', 'morning sun', 'weeping woman', 'human condition', 'face of war', 'song of love',
    'eclipse of the sun', 'mountains and sea', 'calla lily', 'unfinished painting', 'flower power',
    'temptation of st anthony', 'modern times', 'lovers', 'street', 'critic', 'jungle', 'gates',
    'elephants', 'snail', 'sir winston churchill', 'vladimir mayakovsky', 'president barack obama',
    'dinner party', 'sunflower seeds', 'my bed', 'big electric chair', 'kiss on the sidewalk',
    'new york movie', 'early sunday morning', 'many mansions', 'blue nude ii', 'black on maroon',
    'orange red yellow', 'death dealer', 'weather project', 'wounded deer', 'broken column',
    'red ceiling', 'burning monk', 'terror of war', 'falling soldier', 'drowning girl', 'le reve',
    'three musicians', 'drawing hands', 'still life reviving', 'tenement fire harlem',
    'their first murder', 'invisible man', 'subtlety', 'migration series', 'king kong',
    'bicycle thieves', 'tokyo story', 'days of heaven', 'godfather', 'son of man', 'nuclear energy',
    'freedom from want', 'la dolce vita', 'seventh seal', 'wizard of oz', 'lawrence of arabia',
    'hyeres france', 'no i z', 'larmes', 'jazz', 'memphis', 'for the love of god',
    'portrait of an artist', 'in the mood for love', 'order of the angels',
    'midnight ride of paul revere', 'no 61',
}

# Nicknames in the archive that read as a place or a theme.
ALIAS_DENY = {'tiananmen'}

# Nicknames, exact phrase only. The archive's own `aliases` are added to these.
NICKNAMES = {
    "Campbell's Soup Cans": ['soup cans', 'campbells soup', 'warhol soup cans', 'warhol soup'],
    'Marilyn Diptych': ['warhol marilyn', 'marilyn warhol'],
    'Tank Man': ['tank man', 'tiananmen tank man'],
    'The Terror of War': ['napalm girl'],
    'V-J Day in Times Square': ['times square kiss', 'the kiss in times square', 'vj day kiss', 'v j day kiss'],
    'Raising the Flag on Iwo Jima': ['iwo jima flag', 'iwo jima photo', 'flag raising iwo jima'],
    'Guerrillero Heroico': ['che guevara photo', 'che guevara portrait'],
    'The Persistence of Memory': ['dali melting clocks'],
    'The Treachery of Images': ['magritte pipe'],
    'The Son of Man': ['magritte apple', 'man with apple face'],
    'Girl with Balloon': ['balloon girl', 'banksy balloon'],
    'Christina\'s World': ['christinas world'],
    'The Physical Impossibility of Death in the Mind of Someone Living': ['hirst shark', 'damien hirst shark', 'shark in formaldehyde'],
    'Cloud Gate': ['the bean chicago', 'chicago bean'],
    'Balloon Dog (Blue)': ['balloon dog', 'koons balloon dog'],
    'Comedian': ['banana taped to a wall', 'banana duct tape', 'cattelan banana'],
    'Lunch atop a Skyscraper': ['men on a beam', 'lunch on a skyscraper'],
    'The Two Fridas': ['two fridas', 'las dos fridas'],
    'L.H.O.O.Q.': ['lhooq', 'mona lisa with moustache', 'mona lisa with mustache'],
    '2001: A Space Odyssey': ['2001 space odyssey', 'space odyssey'],
    'The Shining': ['the shining'],
    'The 400 Blows': ['400 blows'],
    'Dr. Strangelove': ['strangelove'],
    'The Night of the Hunter': ['night of the hunter'],
    'Rhein II': ['gursky rhine', 'rhein 2'],
    'Celebes (The Elephant Celebes)': ['the elephant celebes', 'elephant celebes'],
    'Time Transfixed (La durée poignardée)': ['la duree poignardee'],
    'Not to Be Reproduced (La reproduction interdite)': ['la reproduction interdite'],
    'Still Life Reviving (Naturaleza muerta resucitando)': ['naturaleza muerta resucitando'],
    'Autoportrait (Tamara in a Green Bugatti)': ['tamara in a green bugatti', 'tamara in the green bugatti'],
    'Le Rêve (The Dream)': ['picasso the dream', 'picasso le reve'],
    '8½': ['8 1 2', 'eight and a half', 'fellini 8 1 2', '8 1 2 fellini'],
    'American Collection #5: Bessie\'s Blues': ['bessies blues'],
}

# Surnames that may stand alone. A surname is used only if exactly one maker in
# the archive ends with it. Left out on purpose: Wood, Frank, Wall, Parks,
# Bacon, Penn, Ray, Adams, Freud, Chicago, Bourgeois, Tanning, Sherman, Smith,
# Moore, Scott, Lean, Lang, Wilder, Whale, Newman, Johns, Nash, Lam, Honda.
SURNAMES = {
    'picasso', 'dali', 'kahlo', 'magritte', 'warhol', 'hopper', 'pollock', 'rothko', 'basquiat',
    'lichtenstein', 'escher', 'banksy', 'matisse', 'haring', 'kusama', 'hockney', 'de kooning',
    'wyeth', 'hirst', 'koons', 'kapoor', 'eliasson', 'abramovic', 'duchamp', 'rodchenko', 'grosz',
    'nolde', 'kertesz', 'brassai', 'doisneau', 'sugimoto', 'eggleston', 'karsh', 'crewdson',
    'leibovitz', 'gursky', 'korda', 'giacometti', 'rauschenberg', 'twombly', 'orozco', 'kiefer',
    'calder', 'giger', 'frazetta', 'chagall', 'miro', 'lempicka', 'frankenthaler', 'rockwell',
    'beuys', 'de chirico', 'mapplethorpe', 'capa', 'cartier bresson', 'arbus', 'avedon',
    'eisenstaedt', 'salgado', 'mccurry', 'af klint', 'o keeffe', 'okeeffe', 'varo', 'bearden',
    'ringgold', 'dubuffet', 'kubrick', 'hitchcock', 'kurosawa', 'fellini', 'godard', 'truffaut',
    'welles', 'coppola', 'ozu', 'malick', 'weegee', 'rivera', 'ai weiwei', 'emin', 'gormley',
    'cattelan', 'catlett', 'wifredo lam', 'tarsila',
}

# Makers who answer to a name that is not the end of their full name.
MAKER_KEYS = {'Christo and Jeanne-Claude': ['christo'], 'Tarsila do Amaral': ['tarsila'],
              'Margaret Bourke-White': ['bourke white']}

# Records that get no placard: the work is public domain and only this
# photograph of it was not free, so "not free to use" would mislead.
SKIP_IDS = {'VAULT-1794'}   # Sagrada Família, Interior Vaults
SKIP_MAKERS = {'Antoni Gaudí (design)'}

FILM_RX = re.compile(r',\s*(?:Still|Publicity|Trailer|Frame|Press|Production|the Match Cut|the Final Frame|'
                     r'Welles and|Anthony Perkins)\b')


def norm(s):
    s = unicodedata.normalize('NFD', str(s or ''))
    s = ''.join(c for c in s if not ('̀' <= c <= 'ͯ')).lower()
    return re.sub(r'[^a-z0-9]+', ' ', s).strip()


def _apos(s):
    """Christina's World is also typed Christinas World."""
    return {s, re.sub(r"[\u2019']", '', s)}


def title_forms(title):
    """The title as typed: whole, without a bracketed gloss, without the apostrophe, without a leading The."""
    out = set()
    bare = re.sub(r'\s*\([^)]*\)', '', title).strip()
    for t in (title, bare):
        for v in _apos(t):
            out.add(norm(v))
    more = {t[4:] for t in out if t.startswith('the ') and len(t.split()) >= 3}
    return {t for t in out | more if t}


def denied(t):
    return re.sub(r'^(?:the|a) ', '', t) in DENY_TITLES or t.startswith('untitled')


def maker_forms(maker):
    """Full names a maker answers to, and the endings that could be a surname."""
    names = [re.sub(r'\s*\([^)]*\)', '', maker).strip()]
    for m in re.findall(r'\(([^)]*)\)', maker):
        if not re.search(r'attribution|design', m, re.I):
            names.append(m)                               # Weegee (Arthur Fellig)
    full, last = set(), set()
    for n in names:
        for v in _apos(n):
            toks = norm(v).split()
            if not toks:
                continue
            full.add(' '.join(toks))
            lead = 0
            while lead < len(toks) - 1 and len(toks[lead]) == 1:
                lead += 1
            if lead:                                      # M. C. Escher: mc escher
                full.add(''.join(toks[:lead]) + ' ' + ' '.join(toks[lead:]))
                if len(toks) - lead >= 2:                 # W. Eugene Smith: eugene smith
                    full.add(' '.join(toks[lead:]))
            mid = [t for i, t in enumerate(toks) if len(t) > 1 or i == 0 or i == len(toks) - 1]
            if lead == 0 and len(mid) >= 2:               # Charles C. Ebbets: charles ebbets
                full.add(' '.join(mid))
            for k in (1, 2):
                if len(toks) >= k:
                    last.add(' '.join(toks[-k:]))
    return full, last



# ---------------------------------------------------------------------------
# The wide list (25 Nov 2026)
WIDE = os.path.join(ROOT, 'tools', 'placards', 'wikidata.json')
SEE = os.path.join(ROOT, 'data', 'see.json')
WANTED = os.path.join(ROOT, 'tools', 'placards', 'wanted.json')

# Works published in or before this year are public domain in the United States. It moves on by itself each 1 January.
PD_YEAR = datetime.date.today().year - 96

# Who counts as a maker: an art or film occupation, and none that says the person is known for something else
# (George W. Bush, Madonna and Thomas Edison are all "painter" or "director" on Wikidata).
ART_RX = re.compile(r'paint|photograph|sculpt|illustrat|printmaker|graphic|artist|draftsperson|engrav|lithograph|etcher|'
                    r'watercolor|mural|ceramic|comics|cartoon|caricatur|animator|film director|filmmaker|cinematograph|'
                    r'collag|calligraph|illuminator|pastellist|designer')
WRITER_RX = re.compile(r'poet|novelist|playwright|short story|children\'s writer|science fiction writer|essayist|dramaturge')
BAD_RX = re.compile(r'politic|singer|musician|\bactor|compos|rapper|guitar|pianist|recording artist|songwriter|physicist|'
                    r'astronom|inventor|engineer|chemist|explorer|mathematic|monarch|military|aristocrat|athlete|player|'
                    r'martial|presenter|business|entrepreneur|diplomat|comedian|wrestler|boxer|pilot|astronaut|economist|'
                    r'physician|manufacturer|stunt|scientist|naturalist|botanist|zoologist|anthropolog|sociolog|conductor|'
                    r'drummer|bassist|disc jockey|youtuber|blogger|lawyer|judge|priest|cleric|theolog|racing|footballer|chess|'
                    r'serial killer|clown|photo lab|secretary|occultist|pornograph|empress|queen|prince|duke|duchess|sultan|'
                    r'caliph|consort|first lady|revolutionary|terrorist|\bspy|criminal|pope|rabbi|imam|missionary|\bnun|monk|'
                    r'ufolog|astrolog|psychiatr|psycholog|psychoanal|neurolog|biolog|geolog|statesman|president|minister|'
                    r'chancellor|emperor|governor|senator|art dealer|socialite|esoteric|banker|merchant|soldier|officer')

HARD_BAD = re.compile(r'politic|monarch|emperor|empress|queen|president|chancellor|minister|serial killer|pope|statesman|governor|senator|'
                      r'sultan|caliph|consort|first lady|terrorist|criminal|duchess|duke|prince|aristocrat')

# Makers the occupation test gets wrong (an actor who is better known as a director, a novelist with a stray "musician").
FORCE_MAKERS = {'Orson Welles', 'Harper Lee', 'Octavio Paz', 'Saul Bellow', 'C. S. Lewis', 'Arthur C. Clarke', 'Mario Vargas Llosa',
                'Paulo Coelho', 'Svetlana Alexievich', 'Shel Silverstein', 'Clint Eastwood', 'Leonard Cohen', 'Patti Smith',
                'George Orwell', 'Pablo Neruda', 'Jean-Paul Sartre', 'Simone de Beauvoir', 'Ezra Pound', 'Bob Dylan'}

# Well-known writers the Wikidata pull missed: name, born, died. Each still goes through every test below
# (on the site already, old enough to be free, and so on); the name must be the title of the English Wikipedia article.
EXTRA_MAKERS = [('Mary Oliver', 1935, 2019), ('Ocean Vuong', 1988, None), ('Anne Sexton', 1928, 1974), ('Elizabeth Bishop', 1911, 1979),
                ('Philip Larkin', 1922, 1985), ('Ted Hughes', 1930, 1998), ('Cormac McCarthy', 1933, 2023), ('Joan Didion', 1934, 2021),
                ('Audre Lorde', 1934, 1992), ('Stan Lee', 1922, 2018), ('Wallace Stevens', 1879, 1955),
                ('William Carlos Williams', 1883, 1963), ('Adrienne Rich', 1929, 2012), ('Gwendolyn Brooks', 1917, 2000),
                ('Frank O\'Hara', 1926, 1966), ('John Ashbery', 1927, 2017), ('Lucille Clifton', 1936, 2010), ('Raymond Carver', 1938, 1988),
                ('Jack Kerouac', 1922, 1969), ('Richard Brautigan', 1935, 1984), ('Anne Carson', 1950, None), ('Louise Erdrich', 1954, None),
                ('Joy Harjo', 1951, None), ('Billy Collins', 1941, None), ('Amanda Gorman', 1998, None), ('Claudia Rankine', 1963, None),
                ('Nikki Giovanni', 1943, 2024), ('Sharon Olds', 1942, None), ('Robert Hass', 1941, None), ('W. S. Merwin', 1927, 2019),
                ('Zadie Smith', 1975, None), ('Sally Rooney', 1991, None), ('Donna Tartt', 1963, None), ('David Foster Wallace', 1962, 2008),
                ('Thomas Pynchon', 1937, None), ('Don DeLillo', 1936, None), ('Philip Roth', 1933, 2018), ('Ursula K. Le Guin', 1929, 2018),
                ('Octavia E. Butler', 1947, 2006), ('Flannery O\'Connor', 1925, 1964), ('Truman Capote', 1924, 1984),
                ('Tennessee Williams', 1911, 1983), ('Arthur Miller', 1915, 2005), ('Ralph Ellison', 1913, 1994)]

# Makers who worked for the US government (FSA, OWI): much of their work is free, so no "not free" claim.
GOV_MAKERS = {'gordon parks', 'jack delano', 'esther bubley', 'john vachon', 'marjory collins', 'arthur rothstein',
              'marion post wolcott', 'russell lee', 'carl mydans', 'ben shahn', 'dorothea lange', 'walker evans'}
# Films after PD_YEAR that are public domain all the same: wanted, not placards.
PD_FILMS = {'night of the living dead', 'charade', 'his girl friday', 'the little shop of horrors', 'plan 9 from outer space',
            'carnival of souls', 'detour', 'scarlet street', 'the last man on earth', 'reefer madness', 'house on haunted hill'}
# Titles of common words that are still plainly the work (mostly films).
TITLE_ALLOW = {
    'the good the bad and the ugly', 'good the bad and the ugly', 'the sound of music', 'sound of music', 'e t the extra terrestrial',
    'crouching tiger hidden dragon', 'mad max fury road', 'eyes wide shut', 'midnight cowboy', 'easy rider', 'close encounters of the third kind',
    'who framed roger rabbit', 'everything everywhere all at once', 'the breakfast club', 'breakfast club', 'dog day afternoon',
    'a nightmare on elm street', 'nightmare on elm street', 'the girl with the dragon tattoo', 'girl with the dragon tattoo', 'north by northwest',
    'for a few dollars more', 'from russia with love', 'the fifth element', 'fifth element', 'american history x', 'requiem for a dream',
    'the magnificent seven', 'magnificent seven', 'from here to eternity', 'it happened one night', 'the fast and the furious', 'fast and the furious',
    'spider man', 'spider man 2', 'spider man 3', 'iron man', 'iron man 2', 'iron man 3', 'the lives of others', 'lives of others', 'call me by your name',
    'an american in paris', 'my fair lady', 'west side story', 'the wild bunch', 'the passion of the christ', 'passion of the christ',     'love actually', 'mean girls', 'gone girl', 'shutter island', 'the last emperor', 'the last samurai', 'the imitation game',
    'the theory of everything', 'blood diamond', 'midnight in paris', 'the day after tomorrow', 'fantastic beasts and where to find them',
    'wild strawberries', 'all about eve', 'all about my mother', 'in the heat of the night', 'mission impossible', 'mission impossible 2',
    'mission impossible iii', 'the man with the golden gun', 'the name of the rose', 'enemy at the gates', 'fifty shades of grey', 'good bye lenin',
    'moscow does not believe in tears', 'a star is born', 'edge of tomorrow', 'the danish girl', 'the iron giant', 'a man for all seasons',     'superman returns', 'the african queen', 'the best years of our lives', 'the diamond arm', 'das boot', 'death becomes her', 'kong skull island',
    'never say never again', '21 grams', '50 first dates', 'all the king s men', 'fanny and alexander', 'the blind side', 'the iron lady',
    'cat on a hot tin roof', 'cloud atlas', 'cold mountain', 'home alone', 'home alone 2', 'home alone 3', 'knives out', 'la vie en rose', 'lady bird',
    'midnight express', 'mona lisa smile', 'paths of glory', 'seven years in tibet', 'the 39 steps', 'the greatest show on earth', 'the longest day',
    'how green was my valley', 'live and let die', 'diamonds are forever', 'you only live twice', 'dr no', 'i am legend', 'as good as it gets',
    'the hateful eight', 'district 9', 'i robot', '127 hours', 'captain phillips', 'dirty harry', 'in bruges', 'licence to kill',
    'one battle after another', 'girl interrupted', 'blade ii', 'ghost rider', 'star wars', 'the matrix', 'pulp fiction', 'fight club', 'forrest gump',
    'the dark knight', 'dark knight', 'the shawshank redemption', 'shawshank redemption', 'the lion king', 'lion king', 'toy story', 'spirited away',
    'taxi driver', 'back to the future', 'jurassic park', 'the lord of the rings', 'lord of the rings', 'harry potter', 'the big lebowski', 'big lebowski',
    'blade runner 2049', 'no country for old men', 'there will be blood', 'the truman show', 'truman show', 'a clockwork orange', 'clockwork orange',
    'full metal jacket', 'the shape of water', 'shape of water', 'la la land', 'the wolf of wall street', 'wolf of wall street', 'the green mile',
    'green mile', 'one flew over the cuckoo s nest', 'the silence of the lambs', 'schindler s list', 'schindlers list', 'reservoir dogs', 'kill bill',
    'the terminator', 'terminator 2 judgment day', 'die hard', 'top gun', 'the exorcist', 'raging bull', 'the deer hunter', 'deer hunter',
    'the princess bride', 'princess bride', 'my neighbor totoro', 'princess mononoke', 'howl s moving castle', 'howls moving castle',
    'grave of the fireflies', 'finding nemo', 'the incredibles', 'monsters inc',     'snow white and the seven dwarfs', 'gone with the wind', 'singin in the rain', 'singing in the rain', 'some like it hot',
    'breakfast at tiffany s', 'breakfast at tiffanys', 'rebel without a cause', '12 angry men', 'to kill a mockingbird', 'the grapes of wrath',
    'game of thrones', 'breaking bad', 'twin peaks', 'the sopranos', 'the simpsons', 'stranger things', 'squid game',
}
# One-word film titles nobody types meaning anything else.
ONE_WORD_FILMS = {'amelie', 'scarface', 'borat', 'robocop', 'beetlejuice', 'gattaca', 'dogville', 'oldboy', 'yojimbo', 'amarcord', 'deadpool',
                  'maleficent', 'aquaman', 'apocalypto', 'octopussy', 'thunderball', 'hellboy', 'stargate', 'watchmen', 'sicario', 'goodfellas',
                  'shrek', 'zootopia', 'ghostbusters', 'trainspotting', 'koyaanisqatsi', 'eraserhead', 'braveheart',
                  'goldfinger', 'skyfall', 'moonraker', 'goldeneye', 'dumbo', 'tron', 'zoolander', 'inception', 'interstellar', 'encanto',
                  'moana', 'jumanji', 'tootsie', 'whiplash', 'coraline', 'ponyo', 'rango'}
# Films whose titles are made of everyday words but mean the film to anyone who types them (the full title, two words or more).
ALLOW_NAMES = set('''Dead Poets Society|A Beautiful Mind|Toy Story 2|Toy Story 3|Toy Story 4|The Godfather Part II|The Godfather Part III|American Beauty|
The King's Speech|12 Years a Slave|Catch Me If You Can|Rain Man|The Social Network|Life of Pi|Million Dollar Baby|The Hunger Games|
Back to the Future Part II|Back to the Future Part III|Good Will Hunting|Lost in Translation|Once Upon a Time in Hollywood|The Usual Suspects|Annie Hall|
12 Monkeys|Men in Black|The Nightmare Before Christmas|Once Upon a Time in America|Once Upon a Time in the West|Sin City|The Third Man|Fantastic Mr. Fox|
Barry Lyndon|Kill Bill: Volume 1|Children of Men|The Thin Red Line|Get Out|The Dark Knight Rises|The Da Vinci Code|Home Alone 2: Lost in New York|
Indiana Jones and the Kingdom of the Crystal Skull|How to Train Your Dragon|Dances with Wolves|The Elephant Man|Mystic River|Dallas Buyers Club|
Bonnie and Clyde|Driving Miss Daisy|Big Hero 6|Wreck-It Ralph|Guardians of the Galaxy|Guardians of the Galaxy Vol. 2|
Guardians of the Galaxy Vol. 3|Captain America: Civil War|Captain America: The Winter Soldier|Spider-Man: No Way Home|Spider-Man: Far From Home|
Spider-Man: Into the Spider-Verse|Spider-Man: Across the Spider-Verse|The Lord of the Rings: The Fellowship of the Ring|The Lord of the Rings: The Two Towers|
The Lord of the Rings: The Return of the King|Harry Potter and the Philosopher's Stone|Harry Potter and the Chamber of Secrets|Harry Potter and the Goblet of Fire|
Harry Potter and the Half-Blood Prince|Harry Potter and the Order of the Phoenix|Star Wars: Episode IV – A New Hope|Star Wars: Episode V – The Empire Strikes Back|
The Prince of Egypt|The Great Mouse Detective|Brother Bear|Monsters University|Castle in the Sky|Corpse Bride|Space Jam|
The Butterfly Effect|The Boss Baby|Bee Movie|Happy Feet|WALL-E|Léon: The Professional|The English Patient|Shakespeare in Love|Green Book|Doctor Strange|
Wonder Woman|Man of Steel|Suicide Squad|Chicken Run|Mr. & Mrs. Smith|Treasure Planet|Turning Red|Chicken Little|
10 Things I Hate About You|Die Another Day|First Blood|No Time to Die|Scent of a Woman|The World Is Not Enough|Chariots of Fire|Fast Five|
Furious 7|High School Musical|Live Free or Die Hard|Pretty Woman|Tomorrow Never Dies|X-Men: Days of Future Past|2 Fast 2 Furious|The Good Dinosaur|
X-Men: The Last Stand|A.I. Artificial Intelligence|The Fate of the Furious|American Pie|Fantastic Four|Open Season|The Mummy Returns|Night at the Museum|
Notting Hill|Over the Hedge|X-Men: Apocalypse|X-Men: First Class|A View to a Kill|Fast & Furious 6|Interview with the Vampire|Justice League|
The Angry Birds Movie|Die Hard with a Vengeance|The Spy Who Loved Me|Solo: A Star Wars Story|Saw II|The Black Cauldron|
Oliver & Company|Ant-Man|Out of Africa'''.replace('\n', '').split('|'))

# Makers the site has under a spelling the name test does not connect.
SITE_HAS = {'Fyodor Dostoyevsky', 'Hafez', 'Saadi', 'Zhuang Zhou', 'Giovanni Antonio Canal', 'Fra Bartolomeo'}

# Other things people type for an item (by the item's title, or the maker's name for a maker card).
WIDE_ALIASES = {'Star Wars: Episode IV – A New Hope': ['star wars', 'star wars a new hope', 'a new hope'],
                'Star Wars: Episode V – The Empire Strikes Back': ['the empire strikes back', 'empire strikes back'],
                'The Lord of the Rings: The Fellowship of the Ring': ['the fellowship of the ring', 'fellowship of the ring', 'lord of the rings film', 'lord of the rings movie'],
                "Harry Potter and the Philosopher's Stone": ["harry potter and the sorcerer's stone", 'harry potter and the sorcerers stone', 'harry potter film', 'harry potter movie'],
                'J. K. Rowling': ['harry potter'], 'The Godfather': ['the godfather', 'godfather'], 'George Lucas': [],
                'Kill Bill: Volume 1': ['kill bill'], 'Léon: The Professional': ['leon the professional', 'the professional'],
                'Death Fugue': ['todesfuge'], 'Do not go gentle into that good night': ['do not go gentle into that good night', 'do not go gentle'], 'Kurt Vonnegut': ['vonnegut']}

# Surnames that pass the automatic test but read as something else (a city, a word, a first name).
DENY_SURNAMES = {'trier', 'kazan', 'leone', 'kirby', 'passos', 'xingjian', 'esquivel', 'besson', 'mann', 'grass', 'miller', 'ford', 'moore',
                 'clezio', 'thiong', 'xiaobo', 'quasimodo', 'hesse', 'valery', 'allende', 'gluck', 'golding', 'clancy', 'laurie', 'hanks',
                 'allen', 'lynch', 'burton', 'gibson', 'boyle', 'lucas', 'bass', 'stella', 'judd', 'andre', 'caro', 'steiner', 'braun'}
# Wide-list titles that read as a theme, a person, a place, or an older book the film was made from.
DENY_WIDE = {'sherlock holmes', 'robin hood', 'the last of the mohicans', 'last of the mohicans', 'andrei rublev', 'barry lyndon', 'the dictator',
             'notting hill', 'the hangover', 'the social network', 'social network', 'the usual suspects', 'usual suspects', 'bonnie and clyde',
             'the great gatsby', 'great gatsby', 'les miserables', 'around the world in 80 days', 'the reluctant dragon', 'reluctant dragon',
             'king arthur', 'the maltese falcon', 'maltese falcon', 'life is beautiful', 'lost in translation', 'city of god', 'the third man',
             'city lights', 'roman holiday', 'black swan', 'blue velvet', 'the pianist', 'the apartment', 'the graduate', 'the notebook',
             'the butterfly effect', 'butterfly effect', 'public enemies', 'love story', 'the interview', 'wall street', 'the leopard', 'open season',
             'the hours', 'get out', 'the crow', 'grand hotel', 'the beach', 'the proposal', 'the descendants', 'the mission', 'the piano',
             'the village', 'the fighter', 'the ring', 'the reader', 'darkest hour', 'the searchers', 'pride prejudice', 'the little mermaid',
             'beauty and the beast', 'the curious case of benjamin button', 'winnie the pooh', 'puss in boots', 'the passion of the christ', 'eternal sunshine of the spotless mind', 'snow white', 'pinocchio', 'bambi',
             'mutiny on the bounty', 'bram stoker s dracula', 'bram stokers dracula', 'beowulf', 'cinderella', 'aladdin', 'noah', 'frankenstein',
             'alice in wonderland', 'the jungle book', 'jungle book', 'peter pan', 'sleeping beauty', 'the hunchback of notre dame', 'war and peace',
             'anna karenina', 'romeo and juliet', 'romeo juliet', 'hamlet', 'macbeth', 'the ten commandments', 'ten commandments', 'ben hur',
             'the little prince', 'little women', 'wuthering heights', 'jane eyre', 'oliver twist', 'great expectations', 'a christmas carol',
             'treasure island', 'the three musketeers', 'three musketeers', 'the count of monte cristo', 'count of monte cristo', 'don quixote',
             'the war of the worlds', 'war of the worlds', 'the time machine', 'time machine', 'the invisible man', 'dr jekyll and mr hyde',
             'the picture of dorian gray', 'the phantom of the opera', 'phantom of the opera', 'the secret garden', 'secret garden', 'heart of darkness'}
# Records to leave out altogether: not makers in any sense a visitor means, a wrong record, or a double of an archive placard.
SKIP_WIDE = {'Eva Braun', 'Alexandra Feodorovna', 'Abdülmecid II', 'Marie of Romania', 'Sophie, Duchess of Hohenberg', 'Victoria of Baden',
             'Joseph Merrick', 'John Wayne Gacy', 'Traudl Junge', 'Cynthia Lennon', 'Lili Elbe', 'Theo Van Gogh', 'Theo van Gogh', 'Rudolf Steiner',
             'Erich von Däniken', 'Zelda Fitzgerald', 'Rudolf Laban', 'Cícero Moraes', 'Adolfo Pérez Esquivel', 'Steve McQueen', 'Józef Gosławski',
             'Augusto De Luca', 'Andrea Benetti', 'Genco Gülan', 'Salvatore Garau', 'Abel Azcona', 'Malina Suliman', 'Adolf Hitler',
             'Marilyn Diptyque', 'Balloon Girl', 'The Kiss of Death (1957)', 'Scene at the Signing of the Constitution of the United States',
             'Wait for Me, Daddy!', 'The Legend of Sigurd and Gudrún', 'Wikidata Sandbox', 'The Kiss of Death', 'Madonna of Kyiv',
             'Klaus Ebner', 'Jean-Joseph Sanfourche', 'Julius Evola', 'Tom Hanks', 'Ben Affleck', 'Kevin Costner', 'Sean Penn', 'Hugh Laurie',
             'Bryan Cranston', 'Sylvester Stallone', 'Harry Potter',
             'Margaret Mead', 'Jamie Lee Curtis', 'Jean Marais', 'Sirindhorn, Princess Royal', 'JR', 'Anna Politkovskaya', 'L. Ron Hubbard',
             # poems whose status is not certain enough for the card's claim: possibly never renewed, or given to the public domain by the writer
             'Do Not Stand at My Grave and Weep', 'End Poem', 'First they came…', 'Stalin Epigram'}


DENY_BARE = {re.sub(r'^(?:the|a|an) ', '', t) for t in DENY_WIDE}


def toks(s):
    return [t for t in norm(s).split() if len(t) > 1]


def same_maker(a, b):
    """Two names for one person: one name's words all sit inside the other's (Hokusai, Katsushika Hokusai)."""
    A, B = (set(a) if not isinstance(a, str) else set(toks(a))), (set(b) if not isinstance(b, str) else set(toks(b)))
    if not A or not B:
        return False
    if A == B:
        return True
    small, big = (A, B) if len(A) <= len(B) else (B, A)
    return small <= big and (len(small) >= 2 or len(next(iter(small))) >= 6)


def main():
    apply = '--apply' in sys.argv
    arch = json.load(open(ARCHIVE, encoding='utf-8'))['works']
    raw = open(WORKS, encoding='utf-8').read()
    site = json.loads(raw[raw.index('['):raw.rindex(']') + 1])
    lex = {norm(k) for k in json.load(open(LEXICON, encoding='utf-8')) if not k.startswith('_')}
    see = json.load(open(SEE, encoding='utf-8')) if os.path.exists(SEE) else {}
    wide = json.load(open(WIDE, encoding='utf-8')) if os.path.exists(WIDE) else {'makers': [], 'works': [], 'films': [], 'poems': []}

    # ---- what the site has
    site_titles, site_pairs, site_films = set(), set(), set()
    site_makers = {}                       # frozenset of name words -> the artist string
    by_site_maker = {}                     # artist string -> title word sets
    df = {}                                # word -> how many works on the site use it anywhere
    for w in site:
        forms = title_forms(w.get('title', '')) | {norm(a) for a in str(w.get('aliases') or '').split(',') if norm(a)}
        for t in forms:
            site_titles.add(t)
            site_pairs.add((t, norm(w.get('artist'))))
        site_films.add(norm(re.split(r',\s*frame at', w.get('title', ''))[0]))
        a = w.get('artist') or ''
        if a and not re.match(r'(?:Maker unknown|Anonymous|Unknown|Traditional|Various)\b', a, re.I):
            full, _ = maker_forms(a)
            for f in full:
                site_makers[frozenset(t for t in f.split() if len(t) > 1)] = a
            by_site_maker.setdefault(a, []).extend(set(t.split()) for t in forms)
        text = ' '.join(str(w.get(k) or '') for k in ('title', 'artist', 'aliases', 'searchTags', 'subjectShort', 'emotionShort',
                                                       'region', 'medium', 'note', 'hook', 'museum')) + ' ' + str(see.get(w['id'], ''))
        for t in set(norm(text).split()):
            df[t] = df.get(t, 0) + 1
    site_makers.pop(frozenset(), None)
    site_last = {norm(a).split()[-1] for a in by_site_maker if norm(a)}

    def on_site_maker(names):
        for n in names:
            A = set(toks(n))
            for k, a in site_makers.items():
                if same_maker(A, k):
                    return a
        return None

    def on_site_work(forms, maker_names):
        """The site has this work: the same title (with a compatible maker), or the maker is here with a near title."""
        here = on_site_maker(maker_names) if maker_names else None
        for t in forms:
            if t in site_titles and (not maker_names or here or (t, '') in site_pairs or not any(m for (tt, m) in site_pairs if tt == t and m)):
                return True
            if t in site_titles and maker_names:
                if any(same_maker(n, m) for (tt, m) in site_pairs if tt == t and m for n in maker_names):
                    return True
        if here:
            for t in forms:
                T = set(t.split())
                for S in by_site_maker.get(here, []):
                    if T and S and len(T & S) / len(T | S) >= 0.6:
                        return True
        return False

    def rare(t):
        """A phrase that holds a word the site's own text almost never uses: not a theme."""
        return any(len(x) >= 4 and not x.isdigit() and df.get(x, 0) <= 2 for x in t.split())

    items, direct, titles, notes = [], {}, {}, []
    mk, mk_keys = {}, {}                   # maker display name -> id; key -> ids, for "title + maker" searches

    def maker_id(display, names):
        i = mk.setdefault(display, len(mk))
        for n in names:
            full, last = maker_forms(n)
            for k in full | {x for x in last if len(x) >= 3}:
                mk_keys.setdefault(k, set()).add(i)
        return i

    def put(key, idx):
        key = norm(key)
        if not key or len(key) < 3:
            return
        if key in direct and direct[key] != idx:
            notes.append(f'  clash, kept first: "{key}" ({items[direct[key]].get("t") or items[direct[key]]["a"]}) vs ({items[idx].get("t") or items[idx]["a"]})')
            return
        direct[key] = idx

    def index_title(forms, idx):
        for t in forms:
            if len(t) >= 2:
                titles.setdefault(t, [])
                if idx not in titles[t]:
                    titles[t].append(idx)

    # ---- 1. the archive: checked by hand, so the hand-kept lists decide
    surname_owner = {}
    makers = sorted({w['artist'] for w in arch if w.get('artist') and w['id'] not in SKIP_IDS and w['artist'] not in SKIP_MAKERS})
    for m in makers:
        _, last = maker_forms(m)
        for sname in last:
            surname_owner.setdefault(sname, set()).add(m)
    nick = {norm(k): v for k, v in NICKNAMES.items()}
    seen_film, arch_titles = {}, set()
    for w in arch:
        if w['id'] in SKIP_IDS:
            continue
        title, maker = w.get('title', ''), w.get('artist', '')
        film = bool(FILM_RX.search(title))
        shown = FILM_RX.split(title)[0].strip() if film else title
        if film and norm(shown) in seen_film:
            continue
        if any((t, norm(maker)) in site_pairs for t in title_forms(shown)):
            notes.append(f'  skipped, same title and maker is on the site: {shown} / {maker}')
            continue
        idx = len(items)
        it = {'t': shown, 'a': maker_clean(maker), 'd': w.get('dateLabel') or ''}
        if w.get('museum'):
            it['h'] = w['museum']
        # One click to where the work can be seen. `k` says what the link is, so the label is honest:
        # hold = the holder's own page, wiki = its Wikipedia article, find = a Wikipedia search (no page of its own on file).
        src = w.get('sourceUrl') or ''
        host = urlparse(src).netloc.replace('www.', '')
        if film:
            it['f'] = 1
            year = re.search(r'\d{4}', str(w.get('dateLabel') or ''))
            it['u'], it['k'] = wiki_find(f'{shown} {year.group(0) if year else ""} film'), 'find'   # the source was the still's file page
            seen_film[norm(shown)] = idx
        elif host.endswith('wikipedia.org'):
            it['u'], it['k'] = src, 'wiki'
        elif host and w.get('museum') and not host.endswith(('wikimedia.org', 'wikidata.org')):
            it['u'], it['k'] = src, 'hold'
        else:
            it['u'], it['k'] = wiki_find(f'{shown} {maker_clean(maker)}'), 'find'
        it['m'] = maker_id(maker_clean(maker), [maker] + MAKER_KEYS.get(maker, []))
        items.append(it)
        forms = title_forms(shown)
        arch_titles |= forms
        index_title(forms, idx)
        for t in forms:
            if (len(t.split()) >= 2 and not denied(t) and t not in site_titles and t not in lex) or t in ONE_WORD:
                put(t, idx)
        own = [a for a in str(w.get('aliases') or '').split(',') if len(norm(a).split()) >= 2 and norm(a) not in ALIAS_DENY]
        for a in own + nick.get(norm(shown), []) + nick.get(norm(title), []):
            if norm(a) and norm(a) not in site_titles and norm(a) not in lex:
                put(a, idx)
    arch_makers = set()
    for m in makers:
        cut = sum(1 for w in arch if w.get('artist') == m and w['id'] not in SKIP_IDS)
        idx = len(items)
        items.append({'a': maker_clean(m), 'n': cut, 'x': 1, 'u': wiki_find(maker_clean(m)), 'k': 'find',
                      'm': maker_id(maker_clean(m), [m] + MAKER_KEYS.get(m, []))})
        arch_makers.add(m)
        full, _ = maker_forms(m)
        for k in full:
            if len(k.split()) >= 2 or k in SURNAMES or len(full) == 1:
                put(k, idx)
        for sname in SURNAMES:
            if surname_owner.get(sname) == {m}:
                put(sname, idx)
        for k in MAKER_KEYS.get(m, []):
            put(k, idx)
    n_arch = len(items)

    # ---- 2. the wide list
    wanted = {'makers': [], 'works': [], 'films': [], 'poems': []}
    tally = {}

    piles, who = {}, ['']

    def count(kind, pile):
        tally[(kind, pile)] = tally.get((kind, pile), 0) + 1
        piles.setdefault((kind, pile), []).append(who[0])

    def in_archive_maker(names):
        return any(same_maker(n, maker_clean(a)) for n in names for a in arch_makers)

    film_count = {}
    for f in wide['films']:
        if f.get('maker'):
            film_count[norm(f['maker'])] = film_count.get(norm(f['maker']), 0) + 1

    kept = []                               # makers that get a placard
    known_makers = []                       # every real maker in the pull, for linking sculptures to someone known
    have = {m['name'] for m in wide['makers']}
    extra = [{'id': '', 'name': n, 'wiki': n, 'n': 60, 'born': b, 'died': d, 'occ': ['writer'], 'aka': [], 'lists': ['writer']}
             for n, b, d in EXTRA_MAKERS if n not in have]
    for m in wide['makers'] + extra:
        if m['name'] in SKIP_WIDE or m.get('born') is None or not m.get('name'):
            continue
        who[0] = m['name']
        occ = ' | '.join(m['occ'])
        director = bool(re.search(r'film director|filmmaker', occ))
        # Known as a maker: more art or writing occupations than others, and none that settles it the other way
        # (Tolkien was an officer and Camus a footballer; George W. Bush and Madonna are not painters to anyone searching).
        good = sum(1 for o in m['occ'] if (ART_RX.search(o) or WRITER_RX.search(o)) and not BAD_RX.search(o))
        bad = sum(1 for o in m['occ'] if BAD_RX.search(o))
        films_made = film_count.get(norm(m['name']), 0)
        if not bad and m.get('lists'):
            good = max(good, 1)             # a plain "writer" and nothing else: Vonnegut
        if m['name'] in FORCE_MAKERS:
            pass
        elif not good or HARD_BAD.search(occ) or (bad >= good and not (director and films_made >= 2)):
            count('maker', 'not a maker'); continue
        names = [m['name']] + [a for a in m['aka'] if toks(a) and toks(m['name']) and toks(a)[-1] == toks(m['name'])[-1]]
        known_makers.append(m['name'])
        if in_archive_maker(names):
            count('maker', 'in the archive'); continue
        if m['name'] in SITE_HAS:
            count('maker', 'here'); continue
        if on_site_maker(names):
            count('maker', 'here'); continue
        if m['born'] < 1850 or (m.get('died') and m['died'] <= PD_YEAR):      # everything they published is old enough to be free
            wanted['makers'].append({'name': m['name'], 'born': m['born'], 'died': m.get('died'), 'n': m['n']})
            count('maker', 'wanted'); continue
        soft = m['born'] < 1910 or norm(m['name']) in GOV_MAKERS
        kept.append((m, names, soft))
        count('maker', 'placard, no reason line' if soft else 'placard')

    # surnames: one owner among everyone who has or could have a placard, and nobody on the site
    last_owner = {}
    for m, names, soft in kept:
        last_owner.setdefault(toks(m['name'])[-1], set()).add(m['name'])
    for a in arch_makers:
        t = toks(maker_clean(a))
        if t:
            last_owner.setdefault(t[-1], set()).add(a)
    new_surnames = []
    for m, names, soft in kept:
        idx = len(items)
        it = {'a': m['name'], 'x': 1, 'wk': m['wiki'], 'k': 'find', 'w': 1, 'm': maker_id(m['name'], names)}
        if soft:
            it['s'] = 1
        items.append(it)
        for n in names:
            full, _ = maker_forms(n)
            for k in full:
                if len(k.split()) >= 2 and k not in site_titles and k not in lex:
                    put(k, idx)
        last = toks(m['name'])[-1]
        solo = len(toks(m['name'])) == 1
        if (len(last) >= 5 and df.get(last, 0) == 0 and last not in lex and last_owner.get(last) == {m['name']}
                and last not in site_last and last not in DENY_SURNAMES and (m['n'] >= 60 or solo)):
            put(last, idx)
            new_surnames.append(f'{last} ({m["name"]})')

    person_names = set()                    # a film called Andrei Rublev or Frida must not answer to the person's name
    for m in wide['makers']:
        if m.get('name'):
            person_names |= maker_forms(m['name'])[0]
    person_names |= {norm(a) for a in by_site_maker}

    def link_maker(name):
        return maker_id(name, [name]) if name else None

    def add_work(rec, kind, forms, akas):
        idx = len(items)
        it = {'t': rec['name'], 'a': rec.get('maker') or '', 'd': str(rec['year']), 'wk': rec['wiki'], 'k': 'wiki' if kind == 'work' else 'read', 'w': 1}
        if rec.get('holder') and kind == 'work':
            it['h'] = rec['holder']
        if kind == 'film':
            it['f'] = 1
        if kind == 'poem':
            it['p'] = 1
        if rec.get('maker'):
            it['m'] = link_maker(rec['maker'])
        items.append(it)
        index_title(forms, idx)
        alone = []
        for t in sorted(forms | akas):
            ok = (t not in site_titles and t not in lex and not denied(t) and re.sub(r'^(?:the|a|an) ', '', t) not in DENY_BARE and t not in arch_titles and t not in person_names
                  and ((len(t.split()) >= 2 and (rare(t) or t in TITLE_ALLOW or rec['name'] in ALLOW_NAMES)) or (kind == 'film' and t in ONE_WORD_FILMS)))
            if ok:
                put(t, idx)
                alone.append(t)
        return alone

    review = {'work': [], 'film': [], 'poem': [], 'film_needs_more': []}
    for w in wide['works']:
        if w['name'] in SKIP_WIDE or w.get('year') is None:
            continue
        names = [w['maker']] if w.get('maker') else []
        if w['kind'] in ('sculpture', 'install', 'mural', 'print') and not (names and (any(same_maker(names[0], k) for k in known_makers) or in_archive_maker(names) or on_site_maker(names))):
            count('work', 'a monument, left out'); continue
        forms = title_forms(w['name'])
        akas = set().union(*[title_forms(a) for a in w['aka']]) if w['aka'] else set()
        if forms & arch_titles:
            count('work', 'in the archive'); continue
        if on_site_work(forms | akas, names):
            count('work', 'here'); continue
        if not names and w['year'] > PD_YEAR and not w.get('pd'):
            count('work', 'no maker on record, left out'); continue    # The Falling Man, Bliss: not leads, and too little known for a label
        if w['year'] <= PD_YEAR or w.get('pd') or not names or norm(names[0]) in GOV_MAKERS or re.search(r'\bnasa\b|apollo|government', norm(names[0])):
            wanted['works'].append({'name': w['name'], 'maker': w.get('maker'), 'year': w['year'], 'holder': w.get('holder'), 'n': w['n']})
            count('work', 'wanted'); continue
        alone = add_work(w, 'work', forms, akas)
        review['work'].append(f'{w["name"]} / {w.get("maker")}, {w["year"]}: {" | ".join(alone) or "(with the maker only)"}')
        count('work', 'placard')
    for f in wide['films']:
        if f['name'] in SKIP_WIDE or f.get('year') is None or not f.get('name'):
            continue
        forms = title_forms(f['name'])
        if any(t in seen_film for t in forms) or forms & arch_titles:
            count('film', 'in the archive'); continue
        if forms & site_films:
            count('film', 'here'); continue
        if f['year'] <= PD_YEAR or f.get('pd') or forms & PD_FILMS:
            wanted['films'].append({'name': f['name'], 'maker': f.get('maker'), 'year': f['year'], 'n': f['n']})
            count('film', 'wanted'); continue
        alone = add_work(f, 'film', forms, set())
        (review['film'] if alone else review['film_needs_more']).append(f'{f["name"]} ({f["year"]})')
        count('film', 'placard')
    for p in wide['poems']:
        if p['name'] in SKIP_WIDE or p.get('year') is None or not p.get('maker'):
            continue
        forms = title_forms(p['name'])
        if on_site_work(forms, [p['maker']]):
            count('poem', 'here'); continue
        if p['year'] <= PD_YEAR or p.get('pd') or (p.get('makerDied') and p['makerDied'] <= PD_YEAR):
            if p['year'] > 1500:
                wanted['poems'].append({'name': p['name'], 'maker': p.get('maker'), 'year': p['year'], 'n': p['n']})
            count('poem', 'wanted'); continue
        alone = add_work(p, 'poem', forms, set())
        review['poem'].append(f'{p["name"]} / {p["maker"]}, {p["year"]}: {" | ".join(alone) or "(with the maker or the word poem)"}')
        count('poem', 'placard')

    # ---- report
    by = {}
    for k, i in direct.items():
        by.setdefault(i, []).append(k)
    by_name = {}
    for i, it in enumerate(items):
        by_name.setdefault(it['a'] if it.get('x') else it['t'], i)
    for name, keys in WIDE_ALIASES.items():
        if name in by_name:
            for k in keys:
                if norm(k) not in site_titles:
                    put(k, by_name[name])
    print(f'{len(items)} placards: {n_arch} from the archive, {len(items) - n_arch} from the wide list; {len(direct)} exact searches, '
          f'{len(titles)} titles and {len(mk_keys)} maker names for title-with-maker searches. Public domain through {PD_YEAR}.')
    for (kind, pile), n in sorted(tally.items()):
        print(f'  {kind:6} {pile:26} {n}')
    if '--review' in sys.argv:
        print('\nARCHIVE (searches that trigger without the maker)')
        for i, it in enumerate(items[:n_arch]):
            print(f'- {it.get("t") or it["a"]}: {" | ".join(sorted(by.get(i, [])))}')
        print('\nNEW SURNAMES ALONE:', ', '.join(sorted(new_surnames)))
        for k in ('work', 'poem'):
            print(f'\nNEW {k.upper()}S'); [print('-', x) for x in review[k]]
        print('\nNEW FILMS, title alone:', '; '.join(review['film']))
        print('\nNEW FILMS, need "film", the year or the director:', '; '.join(review['film_needs_more']))
        for pile in ('not a maker', 'here', 'in the archive', 'wanted'):
            print(f'\nMAKERS, {pile}:', '; '.join(piles.get(('maker', pile), [])))
        print('\nNEW MAKERS:', '; '.join(f'{m["name"]}{"*" if soft else ""}' for m, _, soft in kept), '\n(* no reason line)')
    for n in notes:
        if '--review' in sys.argv or not n.startswith('  clash'):
            print(n)
    if apply:
        out = {'_about': 'Blank wall labels for work that is not on the site. Made by tools/placards.py; do not edit by hand.', 'v': 2,
               'items': items, 'direct': dict(sorted(direct.items())), 'titles': dict(sorted(titles.items())),
               'makers': {k: sorted(v) for k, v in sorted(mk_keys.items())}}
        json.dump(out, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
        for k in wanted:
            wanted[k].sort(key=lambda e: -e['n'])
        wanted['_about'] = ('Well-known makers and works the site does not have and that could be free (made in or before %d, marked public domain, '
                            'or by a maker born before 1850): a shopping list for future rounds, not checked. n = Wikipedia editions. Made by tools/placards.py.' % PD_YEAR)
        json.dump(wanted, open(WANTED, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
        print('wrote', OUT, os.path.getsize(OUT), 'bytes;', WANTED, {k: len(v) for k, v in wanted.items() if k != '_about'})


def wiki_find(q):
    """A Wikipedia search: an exact title goes straight to the article, anything else to the results."""
    return 'https://en.wikipedia.org/wiki/Special:Search?search=' + quote(' '.join(q.split()))


def maker_clean(m):
    return re.sub(r'\s*\((?:attribution[^)]*|design)\)', '', m).strip()


if __name__ == '__main__':
    main()
