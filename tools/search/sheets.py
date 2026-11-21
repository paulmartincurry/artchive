"""Contact sheets for the describers: 9 works per sheet (3 x 3, 400 px cells, numbered), with a text list."""
import json, os, sys
from PIL import Image, ImageDraw, ImageFont
art = {w['id']: w for w in json.load(open('art.json'))}
done = set()
for f in os.listdir('desc') if os.path.isdir('desc') else []:
    for line in open('desc/' + f):
        try: done.add(json.loads(line)['id'])
        except Exception: pass
os.makedirs('sheets', exist_ok=True)
sheeted = set()
for f in os.listdir('sheets'):
    if f.endswith('.txt'):
        for line in open('sheets/' + f):
            if '\t' in line: sheeted.add(line.split('\t')[1])
ids = [i for i in sorted(art) if os.path.exists(f'img/{i}.jpg') and i not in done and i not in sheeted]
start = len([f for f in os.listdir('sheets') if f.endswith('.txt')])
try: font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 30)
except Exception: font = ImageFont.load_default()
n = 0
for s in range(0, len(ids), 9):
    chunk = ids[s:s+9]; k = start + n; n += 1
    S = Image.new('RGB', (1200, 1200), '#202020'); d = ImageDraw.Draw(S); lines = []
    for j, i in enumerate(chunk):
        im = Image.open(f'img/{i}.jpg').convert('RGB'); im.thumbnail((388, 388))
        x, y = (j % 3) * 400, (j // 3) * 400
        S.paste(im, (x + 6 + (388 - im.size[0]) // 2, y + 6 + (388 - im.size[1]) // 2))
        d.rectangle((x + 4, y + 4, x + 44, y + 42), fill='#ffd400'); d.text((x + 14, y + 6), str(j + 1), fill='#000', font=font)
        w = art[i]; lines.append(f"{j+1}\t{i}\t{w['t']}\t{w['a'] or ''}\t{w['d'] or ''}\t{w['m'] or ''}")
    S.save(f'sheets/s{k:04d}.jpg', quality=85)
    open(f'sheets/s{k:04d}.txt', 'w').write('\n'.join(lines) + '\n')
print('new sheets', n, 'from', start)
