#!/usr/bin/env python3
"""Rebuild the kit's card carousel and download chips from people.json.

Run after make-cards.py when the team changes:

    python3 make-cards.py && python3 sync-kit.py

Touches only the two generated blocks, so hand edits elsewhere in the guide
survive.
"""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
PEOPLE = json.load(open(os.path.join(HERE, 'people.json')))

TARGETS = [('public/brand/index.html', ''),
           ('assets/brand/guidelines/veehive-brand-kit.html', '../')]


def slides(base):
    out = []
    for p in PEOPLE:
        who = '%s &middot; %s' % (p['name'], p['role'])
        out.append(
            '<figure class="slide" data-who="%s &middot; %s">'
            '<img src="%sbusiness-card/cards/%s-front.png" alt="%s’s card, front" loading="lazy">'
            '<figcaption>%s</figcaption></figure>'
            % (p['name'], p['role'].replace('&amp;', '&'), base, p['slug'], p['name'], who))
    out.append(
        '<figure class="slide" data-who="The back, shared by everyone">'
        '<img src="%sbusiness-card/cards/%s-front.png" alt="Business card, back" loading="lazy">'
        '<figcaption>Back &middot; the same on every card</figcaption></figure>'
        % (base, 'sathish-jeyakumar-back'.replace('-front', '')))
    return out


def main():
    for rel, base in TARGETS:
        p = os.path.join(ROOT, rel)
        s = open(p).read()

        # the back slide points at the -back image; build it plainly
        sl = slides(base)
        sl[-1] = sl[-1].replace('sathish-jeyakumar-back-front.png', 'sathish-jeyakumar-back.png')

        track = re.search(r'(<div class="carou-track"[^>]*>)(.*?)(</div>)', s, re.S)
        assert track, (rel, 'carousel track')
        s = s[:track.start(2)] + ''.join(sl) + s[track.end(2):]

        dots = ''.join('<button type="button" aria-label="Card %d"></button>' % (i + 1)
                       for i in range(len(sl)))
        d = re.search(r'(<span class="carou-dots" id="cards-dots">)(.*?)(</span>)', s, re.S)
        assert d, (rel, 'dots')
        s = s[:d.start(2)] + dots + s[d.end(2):]

        chips = ''.join('<a class="dl" href="%sbusiness-card/cards/%s.pdf" download>%s</a>'
                        % (base, q['slug'], q['name'].upper()) for q in PEOPLE)
        c = re.search(r'(<div class="dl-row" style="margin-top:12px">)(.*?)(</div>)', s, re.S)
        assert c, (rel, 'chip row')
        s = s[:c.start(2)] + chips + s[c.end(2):]

        open(p, 'w').write(s)
        print('  %-48s %d slides, %d chips' % (rel, len(sl), len(PEOPLE)))


if __name__ == '__main__':
    main()
