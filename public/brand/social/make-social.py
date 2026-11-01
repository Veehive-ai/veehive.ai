#!/usr/bin/env python3
"""Render the social set: avatars, banners and post templates.

    python3 make-social.py

Everything is drawn from the brand files next door, so a change to the mark or
the logotype reaches social by re-running this rather than by hand-editing a
PNG somebody exported months ago.

Platform pixel sizes were current in November 2026. They drift; the shapes do
not. Every avatar is square and gets cropped to a circle, every banner is a
long thin strip with the middle third safe, so a size change usually means
re-rendering at a new number rather than redesigning.
"""
import os, shutil, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
BRAND = os.path.dirname(HERE)
OUT = HERE
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

DARK = '#0E1117'
INK = '#334155'

FONTS = ("<link rel='preconnect' href='https://fonts.googleapis.com'>"
         "<link rel='preconnect' href='https://fonts.gstatic.com' crossorigin>"
         "<link href='https://fonts.googleapis.com/css2?"
         "family=Manrope:wght@500;800&family=IBM+Plex+Sans:wght@400;600"
         "&family=IBM+Plex+Mono:wght@500&display=swap' rel='stylesheet'>")


def page(body, css, w, h):
    return ("<!doctype html><meta charset='utf-8'>" + FONTS +
            "<style>*{box-sizing:border-box;margin:0;padding:0}"
            "body{width:%dpx;height:%dpx;overflow:hidden;"
            "font-family:'IBM Plex Sans',sans-serif}%s</style>%s" % (w, h, css, body))


def shot(html, path, w, h):
    tmp = os.path.join(HERE, '_render.html')
    open(tmp, 'w').write(html)
    subprocess.run([CHROME, '--headless', '--disable-gpu', '--hide-scrollbars',
                    '--window-size=%d,%d' % (w, h), '--screenshot=' + path,
                    '--virtual-time-budget=6000', 'file://' + tmp],
                   capture_output=True)
    os.remove(tmp)
    return os.path.exists(path)


# ── avatars ────────────────────────────────────────────────────────────────
# One square mark, generous margin so a circular crop never clips a petal.
def avatar(ground, size):
    css = ("body{background:%s;display:grid;place-items:center}"
           "img{width:66%%;height:auto;display:block}" % ground)
    return page("<img src='../mark/veehive-mark.svg' alt=''>", css, size, size)


# ── banners ────────────────────────────────────────────────────────────────
# Wide strips. Everything that matters sits in the middle, because every
# platform crops the ends differently on phones.
def banner(w, h, safe_h):
    # a 191px strip cannot hold the long line on two lines; short strips get
    # the short line, and nothing is allowed to wrap and clip
    line = ('Six agentic apps. One harness.' if safe_h < 260
            else 'Power your business with bespoke agentic apps.')
    pad = max(28, int(h * 0.18))
    logo_h = min(int(safe_h * 0.42), int(h * 0.34))
    css = ("body{background:%s;display:grid;place-items:center;padding:%dpx}"
           ".in{display:flex;flex-direction:column;align-items:center;gap:%dpx;"
           "max-width:%dpx;text-align:center}"
           ".in img{height:%dpx;width:auto}"
           ".t{font-family:'Manrope',sans-serif;font-weight:800;color:#EEF0F5;"
           "font-size:%dpx;letter-spacing:-.02em;line-height:1.15;white-space:nowrap}"
           % (DARK, pad, max(10, int(h * 0.07)), int(w * 0.62), logo_h,
              max(15, int(safe_h * 0.21))))
    body = ("<div class='in'><img src='../logo/veehive-ai-logo-white.svg' alt=''>"
            "<div class='t'>%s</div></div>" % line)
    return page(body, css, w, h)


# ── post templates ─────────────────────────────────────────────────────────
# Editable: open the .html, change the headline, re-render.
def post(w, h, headline, kicker):
    pad = int(w * 0.085)
    css = ("body{background:%s;padding:%dpx;display:flex;flex-direction:column;"
           "position:relative;overflow:hidden}"
           ".ground{position:absolute;right:-%dpx;top:-%dpx;height:%dpx;opacity:.07}"
           ".logo{height:%dpx;width:auto;align-self:flex-start;position:relative}"
           ".k{font-family:'IBM Plex Mono',monospace;font-size:%dpx;letter-spacing:.14em;"
           "text-transform:uppercase;color:#6F7788;margin-top:auto;position:relative}"
           ".h{font-family:'Manrope',sans-serif;font-weight:800;color:#EEF0F5;"
           "font-size:%dpx;letter-spacing:-.03em;line-height:1.08;margin-top:%dpx;position:relative}"
           ".f{font-family:'IBM Plex Mono',monospace;font-size:%dpx;letter-spacing:.14em;"
           "text-transform:uppercase;color:#6F7788;margin-top:%dpx;display:flex;gap:%dpx;"
           "align-items:center;position:relative}"
           ".dot{width:%dpx;height:%dpx;border-radius:50%%;background:#EC4899}"
           % (DARK, pad, int(w * 0.18), int(w * 0.12), int(h * 0.78),
              int(w * 0.075), int(w * 0.021), int(w * 0.082), int(w * 0.03),
              int(w * 0.019), int(w * 0.045), int(w * 0.016),
              int(w * 0.012), int(w * 0.012)))
    body = ("<img class='ground' src='../mark/veehive-mark.svg' alt=''>"
            "<img class='logo' src='../logo/veehive-ai-logo-white.svg' alt=''>"
            "<div class='k'>%s</div>"
            "<div class='h'>%s</div>"
            "<div class='f'><span class='dot'></span>veehive.ai</div>" % (kicker, headline))
    return page(body, css, w, h)


AVATARS = [('light', '#FFFFFF'), ('dark', DARK)]
AVATAR_SIZES = [400, 640, 1080]

BANNERS = [
    ('linkedin', 1128, 191, 191),
    ('x',        1500, 500, 500),
    ('facebook',  820, 312, 312),
    ('youtube',  2560, 1440, 423),   # safe strip is 1546 x 423 in the middle
]

POSTS = [
    ('square',   1080, 1080, 'Six agentic apps. One harness.', 'Agentic apps'),
    ('portrait', 1080, 1350, 'Six agentic apps. One harness.', 'Agentic apps'),
    ('story',    1080, 1920, 'Six agentic apps. One harness.', 'Agentic apps'),
]


if __name__ == '__main__':
    made = 0
    for name, ground in AVATARS:
        for s in AVATAR_SIZES:
            f = os.path.join(OUT, 'avatar-%s-%d.png' % (name, s))
            if shot(avatar(ground, s), f, s, s):
                made += 1; print('  avatar  %-28s %dx%d' % (os.path.basename(f), s, s))

    for name, w, h, safe in BANNERS:
        f = os.path.join(OUT, 'banner-%s.png' % name)
        if shot(banner(w, h, safe), f, w, h):
            made += 1; print('  banner  %-28s %dx%d' % (os.path.basename(f), w, h))

    for name, w, h, head, kick in POSTS:
        html = post(w, h, head, kick)
        open(os.path.join(OUT, 'post-%s.html' % name), 'w').write(html)
        f = os.path.join(OUT, 'post-%s.png' % name)
        if shot(html, f, w, h):
            made += 1; print('  post    %-28s %dx%d  (edit post-%s.html)'
                             % (os.path.basename(f), w, h, name))
    print('\n  %d files in %s' % (made, OUT))
