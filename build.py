# Builds portfolio.html from template.html by embedding screenshots as data URIs.
import base64, io, os, sys
from PIL import Image

O = os.path.dirname(os.path.abspath(__file__))
S = sys.argv[1] if len(sys.argv) > 1 else os.path.join(O, 'screenshots')  # source screenshots
IMAGES = {
    'photo': 'photo.png',
    'cert': 'cert.png',
    'ywei': 'ywei.png', 'ywei_cycle': 'steps/yst-6.png', 'ywei_table': 'steps/yst-5.png',
    'ywei_join': 'steps/yst-4.png', 'ywei_login': 'ywei-login.png',
    'auction': 'auction-en.png',
    'pos_tables': 'pos-tables.png', 'pos_pos': 'pos-pos.png', 'pos_reports': 'pos-reports.png', 'cafe': 'cafe.png',
    'hotel': 'hotel.png', 'hotel_rooms': 'steps/rooms-1.png', 'hotel_menu': 'steps/rest-1.png',
    'hotel_services': 'steps/home-1.png', 'hotel_admin': 'hotel-login.png',
    'tuabaeb': 'tuabaeb.png',
}
ADMIN = ['tb-admin', 'tb-grades', 'tb-attendance', 'tb-statistics']  # added if present
ADMIN_CAPS = {'tb-admin': 'admin dashboard', 'tb-grades': 'grades', 'tb-attendance': 'attendance stats', 'tb-statistics': 'student statistics'}


def encode(path, key):
    im = Image.open(path).convert('RGB')
    if im.width == 1440:
        im = im.crop((0, 0, im.width - 15, im.height))  # drop scrollbar
    im.thumbnail((1400, 1400))
    im.save(f'{O}/images/{key}.jpg', quality=82)
    b = io.BytesIO(); im.save(b, 'JPEG', quality=82)
    return 'data:image/jpeg;base64,' + base64.b64encode(b.getvalue()).decode()


os.makedirs(O + '/images', exist_ok=True)
html = open(O + '/template.html', encoding='utf-8').read()
for k, f in IMAGES.items():
    html = html.replace('{{%s}}' % k, encode(f'{S}/{f}', k))

admin = [a for a in ADMIN if os.path.exists(f'{S}/{a}.png')]
if admin:
    thumbs = ''.join(
        f'<div class="frame"><button type="button" data-cap="Tuabaeb School · {ADMIN_CAPS[a]}">'
        f'<img src="{encode(f"{S}/{a}.png", a)}" alt="School management system: {ADMIN_CAPS[a]}"></button></div>'
        for a in admin)
    html = html.replace('<!--TUABAEB_ADMIN-->', f'<div class="thumbs">{thumbs}</div>')

open(O + '/portfolio.html', 'w', encoding='utf-8').write(html)
print(os.path.getsize(O + '/portfolio.html') // 1024, 'KB', 'admin shots:', admin)
