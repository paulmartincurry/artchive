"""Give every artwork a `medGroup`: the Medium filter's plain categories (22 Nov 2026), from medium text, title and the old macroMedium."""
import json, re, sys
P = 'data/works.js'
def has(t, rx): return re.search(rx, t, re.I)
FILM = r'\bfilm\b|film still|publicity still|frame at|motion picture'
PHOTO = r'telescope|spacecraft|photograph|albumen|gelatin|daguerreotype|ambrotype|tintype|photogravure|cyanotype|platinum print|salted paper|collodion|autochrome|carbon print|negative|transparency|calotype|woodburytype|stereo'
TEXT = r'\bsilk\b(?! paper)|wool|cotton|linen|embroider|tapestry|carpet|rug\b|kimono|robe|textile|velvet|brocade|damask|lace\b|sampler|quilt|ikat|batik|tunic|garment|skirt|dress\b|shawl|fukusa|weav|needlework|chintz|sidewall|wallpaper'
MS = r'manuscript|parchment|vellum|codex|illuminat|book of hours|psalter|qur.?an|gospel|folio|bound volume|binding|calligraph|incunab|printed book|book page'
POSTER = r'poster|placard|broadside|handbill|comic|newspaper|magazine (page|cover)|sheet music|letterform|type specimen|typeface|alphabet|label|trade card|ephemera'
MAP = r'\bmap\b|atlas|star chart|celestial|planisph|chart\b|diagram|globe\b|cosmograph|mappa'
DRAW = r'\bpen\b|chalk|graphite|pencil|charcoal|pastel|crayon|silverpoint|metalpoint|\bwash\b|drawing|sketch|study for|cartoon|\bink\b(?!.*(silk|hanging|handscroll|album))|watercolou?r(?!.*(opaque|gold))'
PRINT = r'woodcut|woodblock|wood engraving|etching|engraving|lithograph|aquatint|mezzotint|drypoint|silkscreen|screenprint|serigraph|linocut|linoleum|stencil|pochoir|chromolith|zincograph|collotype|photomechanical|line block|relief print|intaglio|print\b|surimono|plate \(|book plate|colour plate|color plate|ukiyo'
PAINTMS = r'opaque watercolou?r|gum tempera|tempera|gouache|hanging scroll|handscroll|album leaf|ink and colou?r|colou?rs? on (silk|paper)|fresco|oil\b|acrylic|distemper|encaustic|thangka|miniature'
BUILD = r'cathedral|church|chapel|basilica|mosque|temple|pagoda|stupa|palace|castle|tomb\b|mausoleum|cave|caves|shrine|monastery|abbey|tower|bridge|pyramid|ziggurat|great wall|wat\b|angkor|borobudur|alhambra|parthenon|colosseum|pantheon|sagrada|chartres|petra|stonehenge|lines\b|geoglyph|rock art|petroglyph|cave painting|mural, |dome|minaret|gate\b|citadel|fort\b|city of'
SCULP = r'marble|bronze|stone|limestone|sandstone|granite|basalt|alabaster|terracotta|plaster|statue|figure|bust\b|relief|head\b|sculpt|carved|carving|idol|stele|stela|mask|totem|effigy|wood\b|ivory|jade|steatite|tuff'
CRAFT = r'ceramic|porcelain|stoneware|earthenware|faience|fritware|glaze|pottery|vase|bowl|jar\b|dish|plate\b|cup\b|ewer|teapot|vessel|tile|glass|favrile|enamel|cloisonn|lacquer|gold\b|silver\b|gilt|jewel|necklace|pendant|brooch|earring|ring\b|bracelet|tiara|crown|fibula|coin|tetradrachm|stater|medal|seal\b|inro|netsuke|tsuba|sword|dagger|armou?r|helmet|shield|halberd|burgonet|furniture|chair|cabinet|table\b|piano|guitar|lute|instrument|pipa|yueqin|lamellophone|mirror|lamp|box\b|snuff|clock|fan\b|comb|spoon|candelabr|incense|censer|reliquary|chalice|mug|goblet|bottle|flask|pyx|casket|barge fixture|container|basket|beads?\b|hair-pipe|pin\b'
POSTERW = r'poster|placard|broadside|handbill|newspaper|magazine (page|cover)|periodical|sheet music|tarot|type specimen|manuale tipografico|majuscole|comic (page|strip)'
MAPW = r'\bmap\b|mappa|star chart|planisph|celestial|\bglobe\b|cosmograph|utriusque cosmi|harmonia macrocosmica|uranometria|atlas(?! moth)|tabula|constellation|de revolutionibus'
SCULPW = r'statue|figure|stele|stela|relief|head\b|bust|god\b|goddess|deity|buddha|bodhisattva|vishnu|shiva|krishna|ganesha|riding|mask|effigy|tomb|saint|virgin|christ|venus|apollo|dancer|warrior|guardian|lion|horse|bull'
def group(w):
    mm = w.get('macroMedium') or ''; med = (w.get('medium') or '') + ' ' + (w.get('mediumUnchecked') or ''); t = w.get('title') or ''; both = med + ' ' + t
    pl = w.get('place') or ''
    if mm == 'Photograph & Film':
        return 'Film still' if (has(med, r'frame|still|silent film|recorded score|trailer|^\s*film,') or w.get('grow') == 'film') else 'Photograph'
    if has(med, PHOTO) and not has(med, PRINT + '|' + PAINTMS + '|from an original drawing'): return 'Photograph'
    if has(both, POSTERW) and mm in ('Print & Woodcut', 'Letterform, Score & Ephemera', 'Diagram, Cyanotype & Textile', 'Scroll & Paper'): return 'Poster & Graphic'
    if has(t, MAPW) and mm in ('Diagram, Cyanotype & Textile', 'Print & Woodcut', 'Scroll & Paper', 'Letterform, Score & Ephemera'): return 'Map & Chart'
    if mm not in ('Painting', 'Sculpture & Metalwork') and has(med, TEXT) and not has(med, PAINTMS + r'|on silk|on cotton|ink and colou?r'): return 'Textile'
    if mm == 'Sculpture & Metalwork':
        if has(t, BUILD) and not has(t, r'lamp|effigy|bust|figure|statue|model|vessel|box|tile|panel|plaque|fragment|relief from|cadaver|mourner|buddha|from the tomb'): return 'Building & Site'
        if has(t, SCULPW): return 'Sculpture'
        if has(both, CRAFT): return 'Craft & Object'
        return 'Sculpture'
    if (has(med, MS + '|papyrus') and (not has(med, PRINT) or has(med, 'printed book'))) or (not has(med, PRINT) or has(med, 'printed book')) and has(t, r'manuscript|book of hours|psalter|qur.?an|codex(?! arundel)|folio \d|\bfol\.|leaf from a(?!.*lithograph)|book of the dead'):
        return 'Book & Manuscript'
    if mm == 'Painting': return 'Painting'
    paintish = has(med, PAINTMS) and (pl in ('South Asia', 'Middle East & North Africa', 'Central Asia', 'East Asia', 'Southeast Asia') or has(med, r'oil|fresco|tempera|acrylic|scroll|album leaf'))
    if mm == 'Print & Woodcut':
        return 'Drawing & Watercolour' if has(med, DRAW) and not has(med, PRINT) else 'Print'
    if mm == 'Scroll & Paper':
        if has(med, PRINT) and not has(med, PAINTMS): return 'Print'
        if paintish: return 'Painting'
        if has(med, r'\bink\b|colou?r on') and pl == 'East Asia': return 'Painting'
        return 'Drawing & Watercolour'
    if mm == 'Diagram, Cyanotype & Textile':
        if has(med, PRINT): return 'Print'
        if has(med, DRAW): return 'Drawing & Watercolour'
        return 'Print'
    if mm == 'Letterform, Score & Ephemera':
        if paintish or has(med, r'\bink\b|hanging scroll|handscroll|calligraph'): return 'Book & Manuscript'
        return 'Poster & Graphic'
    return 'Painting'
if __name__ == '__main__':
    s = open(P, encoding='utf8').read(); a, b = s.index('['), s.rindex(']') + 1; d = json.loads(s[a:b])
    from collections import Counter, defaultdict
    c = Counter(); ex = defaultdict(list)
    for w in d:
        if w['itemType'] == 'literature' or w.get('macroMedium') == 'Literature & Verse': continue
        g = group(w); w['medGroup'] = g; c[g] += 1; ex[g].append(f"{w['id']}|{w['title'][:40]}|{(w.get('medium') or '')[:35]}|{w.get('macroMedium','')[:10]}")
    print(c)
    if '--show' in sys.argv:
        import random; random.seed(1)
        for g in ex: print('\n==', g); [print('  ', x) for x in random.sample(ex[g], min(18, len(ex[g])))]
    if '--apply' in sys.argv:
        open(P, 'w', encoding='utf8').write(s[:a] + json.dumps(d, ensure_ascii=False, separators=(',', ':')) + s[b:]); print('applied')
