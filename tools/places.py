"""Give every work a `place`: one of ten map regions, from its `region` text (22 Nov 2026).
Run after any merge; build_pages carries the field to the site. Unmatched works fall back on macroRegion."""
import json, re, sys
P = 'data/works.js'
R = [  # order matters: first match wins
 ('Latin America & Caribbean', r'Mexic|Mesoameric|Maya|Aztec|Nahua|Olmec|Teotihuacan|Toltec|Mixtec|Zapotec|Peru\b|Moche|Nazca|Nasca|Inca|Chimú|Paracas|Bolivia|Colombia|Guatemala|Argentina|Brazil|Ecuador|Chile|Andean|Suriname|Jamaica|Caribbean|Haiti|Cuba|Puerto Rico|Panama|Costa Rica|Honduras|Nicaragua|Salvador|Venezuela|Uruguay|Paraguay|Taíno|Latin America|Dominican|Trinidad|Barbados|Martinique|Saint Lucia|Bahamas'),
 ('North America', r'United States|\bUSA?\b|American|North America|Canada|Alaska|British America|New York|Chicago|Boston|Philadelphia|California|Massachusetts|Washington, D\.?C|New England|Virginia|Ohio|Cleveland|Arizona|New Mexico|Texas|Louisiana|New Orleans|Kentucky|Pennsylvania|Maryland|Illinois|Michigan|Missouri|Montana|Wyoming|Colorado|Oregon|Seattle|Carolina|Georgia \(US|Tennessee|Mississippi|Alabama|Connecticut|Rhode Island|Vermont|Maine|New Jersey|Ojibwe|Kiowa|Nez Perce|Navajo|Diné|Lakota|Sioux|Cheyenne|Cherokee|Hopi|Zuni|Pueblo|Pacific Northwest|Tlingit|Haida|Kwakwaka|Inuit|Plains|Apsaroke|Crow \(|Blackfeet|Iroquois|Haudenosaunee|Mohawk|Chilkat|Nakota|Ohlone|Apache|Shoshone|Arapaho|Dakota|Pawnee|Nebraska|Oklahoma'),
 ('Middle East & North Africa', r'Egypt|Cairo|Sinai|Dead Sea|Asia Minor|Galilee|Ephesus|Moab|Bethlehem|Azerbaijan|Caucasus|Amarna|Giza|Alexandria|Morocc|Algeri|Tunis|Libya|Maghreb|Turkey|Turkish|Ottoman|Istanbul|Constantinople|Anatolia|Iznik|Syria|Damascus|Lebanon|Levant|Palestin|Jerusalem|Israel|Judea|Jordan|Arabia|Mecca|Medina|Yemen|Oman|Iraq|Baghdad|Mesopotamia|Babylon|Assyria|Sumer|Akkad|Ur\b|Nineveh|Nimrud|Persia|Persian|Iran|Isfahan|Tabriz|Shiraz|Herat|Safavid|Qajar|Ilkhanid|Timurid|Seljuk|Kurd|Armenia|Hittite|Phoenicia|Carthage|Andalus|Granada \(Nasrid|Nasrid|Mamluk|Fatimid|Abbasid|Umayyad|Islamic|Near East|Sasanian|Achaemenid|Parthia|Elam|Ugarit|Canaan|Hebrew|Biblical'),
 ('Oceania', r'Australia|New Zealand|Aotearoa|Māori|Maori|Hawai|Polynesia|Melanesia|Micronesia|Papua|New Guinea|Fiji|Samoa|Tonga|Tahiti|Marquesas|Easter Island|Rapa Nui|Solomon Islands|Vanuatu|New Ireland|New Britain|Oceania|Pacific Islands|Aboriginal|South Pacific|Torres Strait|Caroline Island'),
 ('Africa', r'Africa|Nigeria|Yoruba|Benin|Ife|Igbo|Ghana|Asante|Ashanti|Akan|Mali|Dogon|Bamana|Côte d|Ivory Coast|Baule|Senegal|Sierra Leone|Liberia|Guinea|Cameroon|Bamileke|Congo|Kongo|Kuba|Luba|Angola|Gabon|Fang|Kenya|Tanzania|Uganda|Ethiopia|Abyssinia|Eritrea|Somali|Sudan|Nubia|Kush|Meroë|Zimbabwe|Zambia|Malawi|Mozambique|Madagascar|Zulu|Xhosa|Swahili|Zanzibar|Burkina|Niger\b|Chad|Mande|Bushoong|Nguni|Botswana|Namibia|Lesotho'),
 ('South Asia', r'India\b|Indian\b|Mughal|Rajasthan|Rajput|Pahari|Kangra|Mewar|Udaipur|Kota|Bundi|Deccan|Golconda|Bijapur|Bengal|Kalighat|Delhi|Agra|Lahore|Punjab|Gujarat|Kashmir|Tamil|Chola|Kerala|Mysore|Hyderabad|Lucknow|Awadh|Bihar|Odisha|Orissa|Madhya|Mathura|Gandhara|Pakistan|Indus|Harappa|Sri Lanka|Ceylon|Nepal|Kathmandu|Bhutan|Bangladesh|Hindustan|Mandi|Basohli|Jaipur|Ajmer|Mandu|Malwa|Sanskrit|Vedic|Tibet|Himalaya|Ladakh'),
 ('Central Asia', r'Afghan|Uzbek|Samarkand|Bukhara|Turkmen|Kazakh|Kyrgyz|Tajik|Mongol|Siberia|Scythia|Sogdia|Bactria|Central Asia|Steppe'),
 ('Southeast Asia', r'Java|Bali|Sumatra|Indonesia|Dutch East Indies|Borneo|Malay|Singapore|Thai|Siam|Bangkok|Cambodia|Khmer|Angkor|Vietnam|Annam|Laos|Burma|Myanmar|Mandalay|Philippine|Manila|Champa|Borobudur'),
 ('East Asia', r'Japan|Japanese|Edo|Kyoto|Tokyo|Osaka|Nara|Heian|Kamakura|Muromachi|Meiji|Taish|Showa|Ainu|Okinawa|Ryukyu|China|Chinese|Tang\b|Song\b|Ming\b|Qing\b|Han\b|Yuan\b|Zhou|Shang|Beijing|Peking|Canton|Guangzhou|Shanghai|Suzhou|Hangzhou|Nanjing|Sichuan|Taiwan|Hong Kong|Macau|Korea|Joseon|Goryeo|Silla|Baekje|Seoul|Manchu'),
 ('Europe', r'Europe|England|English|Britain|British|Scotland|Wales|Ireland|Irish|London|France|French|Paris|Germany|German|Italy|Italian|Rome\b|Roman|Florence|Venice|Spain|Spanish|Portugal|Netherlands|Dutch|Holland|Flanders|Flemish|Belgium|Austria|Vienna|Switzerland|Swiss|Russia|Soviet|Ukrain|Poland|Polish|Czech|Bohemia|Prague|Hungary|Romania|Bulgaria|Serbia|Croatia|Slovenia|Bosnia|Greece|Greek|Athens|Crete|Minoan|Mycenae|Cyclad|Sweden|Swedish|Norway|Norse|Denmark|Danish|Finland|Iceland|Estonia|Latvia|Lithuania|Belarus|Georgia|Celtic|Viking|Anglo-Saxon|Frankish|Merovingian|Carolingian|Etruscan|Sicily|Sardinia|Corsica|Malta|Cyprus|Lascaux|Gaul|Mosan|Rhine|Burgundy|Normandy|Brittany|Provence|Catalonia|Castile|Andalusia|Bavaria|Prussia|Saxony|Weimar|Dresden|Munich|Hamburg|Nuremberg|Antwerp|Bruges|Ghent|Amsterdam|Delft|Haarlem|Leiden|Utrecht|Madrid|Seville|Toledo|Barcelona|Lisbon|Milan|Naples|Genoa|Siena|Bologna|Padua|Ferrara|Mantua|Urbino|Pompeii|Byzant'),
]
FALLBACK = {'Europe': 'Europe', 'Americas': 'North America', 'East & Inner Asia': 'East Asia', 'Near East & South Asia': 'Middle East & North Africa', 'Africa, Oceania & Indigenous Americas': 'Africa'}
CR = [(n, re.compile(rx)) for n, rx in R]
SPACE = re.compile(r'^(Space|The Moon|Moon|Mars|Antarctica|International|Worldwide|Lunar|Earth orbit|Outer solar|Saturn orbit|South Georgia)')
def place(w):
    t = (w.get('region') or '')
    if SPACE.search(t): return None, True
    # the place named first wins (a writer's "Britain / Egypt" is British); rule order breaks ties
    hits = [(m.start(), k, n, m.group(0)) for k, (n, rx) in enumerate(CR) for m in [rx.search(t)] if m]
    # an adjective of empire ("French Polynesia", "British India", "Roman Egypt") names the ruler, not the place
    if len(hits) > 1: hits = [h for h in hits if not re.match(r'(?i)(french|british|roman|english|dutch|spanish|portuguese)$', h[3])] or hits
    # overseas places beat the country that ruled them
    if re.search(r'(?i)martinique|guadeloupe|bahamas|haiti', t): return 'Latin America & Caribbean', True
    if re.search(r'(?i)tahiti|polynesia|marquesas|hawai', t): return 'Oceania', True
    if re.search(r'(?i)great lakes|indiana territory', t): return 'North America', True
    if hits: return min(hits)[2], True
    return FALLBACK.get(w.get('macroRegion'), 'Europe'), False
if __name__ == '__main__':
    s = open(P, encoding='utf8').read(); a, b = s.index('['), s.rindex(']') + 1; d = json.loads(s[a:b])
    from collections import Counter
    miss = Counter(); c = Counter()
    for w in d:
        p, ok = place(w); w['place'] = p; c[p] += 1
        if not ok: miss[(w.get('region'), w.get('macroRegion'))] += 1
    print(c); print('fallback', sum(miss.values())); print(miss.most_common(60))
    if '--apply' in sys.argv:
        open(P, 'w', encoding='utf8').write(s[:a] + json.dumps(d, ensure_ascii=False, separators=(',', ':')) + s[b:]); print('applied')
