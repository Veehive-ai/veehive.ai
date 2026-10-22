#!/usr/bin/env python3
"""Render one card per person in people.json.

card.html is the single source of the design; this only swaps the four fields
that differ between people. Add someone to people.json and re-run.

    python3 make-cards.py

Writes cards/<slug>.html, cards/<slug>-front.png, cards/<slug>-back.png and
cards/<slug>.pdf. A person with no phone simply loses that line.
"""
import json, os, re, shutil, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'cards')
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

TEMPLATE = open(os.path.join(HERE, 'card.html')).read()
PEOPLE = json.load(open(os.path.join(HERE, 'people.json')))

# the fields that vary, as they appear in the template
T_NAME = 'Sathish Jeyakumar'
T_ROLE = 'Founder &amp; CEO'
T_MAIL = 'sathish@veehive.ai'
T_PHONE = '+971 50 275 3576'


def build(person):
    s = TEMPLATE
    s = s.replace('<h1>%s</h1>' % T_NAME, '<h1>%s</h1>' % person['name'])
    s = s.replace('<div class="role">%s</div>' % T_ROLE,
                  '<div class="role">%s</div>' % person['role'])
    s = s.replace(T_MAIL, person['email'])
    if person.get('phone'):
        s = s.replace(T_PHONE, person['phone'])
    else:
        # drop the whole <li>, so the list closes up rather than showing a gap
        s = re.sub(r'\s*<li><svg viewBox="0 0 24 24"><path d="M22 16\.9.*?</svg>'
                   + re.escape(T_PHONE) + r'</li>', '', s, flags=re.S)
        assert T_PHONE not in s, 'phone line not removed for ' + person['slug']
    # the template's own person is in the list, so check the result instead
    assert person['name'] in s, 'name not set for ' + person['slug']
    assert person['email'] in s, 'email not set for ' + person['slug']
    if person['slug'] != 'sathish-jeyakumar':
        assert T_NAME not in s and T_MAIL not in s, 'template field left behind'
    return s


def render(slug, path):
    page = os.path.join(OUT, 'page-%s.png' % slug)
    subprocess.run([CHROME, '--headless', '--disable-gpu', '--hide-scrollbars',
                    '--force-device-scale-factor=2', '--window-size=1170,1380',
                    '--screenshot=' + page, '--virtual-time-budget=7000',
                    'file://' + path], capture_output=True)
    from PIL import Image
    im = Image.open(page)
    im.crop((120, 120, 2220, 1320)).save(os.path.join(OUT, '%s-front.png' % slug))
    im.crop((120, 1440, 2220, 2640)).save(os.path.join(OUT, '%s-back.png' % slug))
    os.remove(page)
    subprocess.run([CHROME, '--headless', '--disable-gpu', '--no-pdf-header-footer',
                    '--print-to-pdf=' + os.path.join(OUT, '%s.pdf' % slug),
                    '--virtual-time-budget=9000', 'file://' + path],
                   capture_output=True)


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    # the cards render from this folder, so the artwork resolves relatively
    for p in PEOPLE:
        html = os.path.join(HERE, '_render-%s.html' % p['slug'])
        open(html, 'w').write(build(p))
        render(p['slug'], html)
        shutil.move(html, os.path.join(OUT, '%s.html' % p['slug']))
        pdf = os.path.join(OUT, '%s.pdf' % p['slug'])
        print('  %-20s %-26s %s%s' % (p['name'], p['role'].replace('&amp;', '&'),
                                      p['email'],
                                      '' if p.get('phone') else '   (no phone)'))
