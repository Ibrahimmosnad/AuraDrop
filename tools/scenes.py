from lib import *
import plants, icons

def phone():
    W, H = 300, 600
    scan_y = 262
    defs = MARK_DEFS + '<clipPath id="scr"><rect x="14" y="14" width="272" height="572" rx="34"/></clipPath><linearGradient id="scan" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#8FE04A" stop-opacity="0"/><stop offset="1" stop-color="#8FE04A" stop-opacity=".55"/></linearGradient>'
    b = ('<rect x="4" y="4" width="292" height="592" rx="44" fill="#14352A"/><rect x="14" y="14" width="272" height="572" rx="34" fill="#FBF8F0"/>'
         '<g clip-path="url(#scr)">'
         '<rect x="14" y="14" width="272" height="330" fill="#E9EDE8"/>'
         + embed(plants.fiddle('wilted'), 55, 56, 190)
         + f'<rect x="14" y="{scan_y-60}" width="272" height="60" fill="url(#scan)"/><rect x="14" y="{scan_y-2}" width="272" height="4" fill="#8FE04A"/>'
         + ''.join(f'<path d="{d}" fill="none" stroke="#14352A" stroke-width="5" stroke-linecap="round"/>' for d in
                   ['M44 80V56H68', 'M256 56H232V80', 'M44 300V324H68', 'M256 324H232V300'])
         + '</g>')
    b += '<rect x="106" y="22" width="88" height="22" rx="11" fill="#14352A"/>'
    b += text('Diagnosing…', 20, 36, 380, C['forest'], 600)
    chips = [('Thirsty', C['water']), ('Pests', C['coral']), ('Tired soil', C['kraft'])]
    x = 36
    for label, col in chips:
        wd = text_width(label, 13, 500) + 32
        b += f'<rect x="{f(x)}" y="396" width="{f(wd)}" height="30" rx="15" fill="{col}" fill-opacity=".35"/><circle cx="{f(x+14)}" cy="411" r="4.5" fill="{col}"/>' + text(label, 13, x+25, 416, C['forest'], 500)
        x += wd + 8
    b += text('Your fiddle-leaf fig is dehydrated.', 14, 36, 462, '#4a6358', 500)
    b += text('Kit: Nutrient drops + soil refresh', 14, 36, 484, '#4a6358', 500)
    b += '<rect x="36" y="508" width="228" height="48" rx="24" fill="#1C9358"/>' + text('Send my kit', 18, 150, 539, C['cream'], 600, 'middle')
    return svg(f'0 0 {W} {H}', b, 'AuraDrop app, diagnosis screen', defs)

def wmark_lockup(x, y, h, dark=False):
    """Inline horizontal logo, height h."""
    s = h/130
    a, b = (C['cream'], '#5FE08F') if dark else (C['forest'], C['leaf'])
    import json
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})">' + mark(8, 2, 126) +
            text('Aura', 68, 150, 86, a, 600, 'start', -1) + text('Drop', 68, 150+text_width('Aura', 68, 600, -1)-1, 86, b, 600, 'start', -1) + '</g>')

def profile():
    d = MARK_DEFS
    b = f'<rect width="800" height="800" fill="#1C9358"/><circle cx="400" cy="400" r="300" fill="#3FD283" opacity=".45"/>'
    b += f'<g transform="translate(180 120) scale(1.76)"><path d="{DROP}" fill="#FBF8F0" transform="translate(-28 0)"/>'
    b += '<g transform="translate(-28 0) rotate(12 128 160)"><path d="M128 218C92 196 92 146 128 104C164 146 164 196 128 218Z" fill="#1C9358"/><path d="M128 208V132" stroke="#FBF8F0" stroke-width="7" stroke-linecap="round"/></g></g>'
    b += sparkle(620, 190, 26, C['lime']) + sparkle(190, 250, 16, C['cream'])
    return svg('0 0 800 800', b, 'AuraDrop profile image', d)

def og(w=1200, h=630, banner=False):
    d = MARK_DEFS
    bg = f'<rect width="{w}" height="{h}" fill="{C["forest"]}"/>'
    g, gd = glow(w*.76, h*.55, h*.62, 'og', C['lime'], .35)
    b = bg + gd
    if banner:
        b = f'<rect width="{w}" height="{h}" fill="{C["cream"]}"/>' + glow(w*.74, h*.6, h*.9, 'og', C['lime'], .35)[1]
    b += wmark_lockup(60 if not banner else 80, 60 if not banner else 80, 100 if not banner else 110, dark=not banner)
    col = C['cream'] if not banner else C['forest']
    sz = 60 if not banner else 52
    y0 = h*.58 if not banner else h*.58
    b += text('Your plant’s', sz, 64, y0, col, 600) + text('second wind.', sz, 64, y0+sz*1.15, C['mint'] if not banner else C['leaf'], 600)
    b += text('Snap a photo. We diagnose it and ship the kit.', 26 if not banner else 22, 66, y0+sz*1.15+52, '#B7C9BE' if not banner else '#4a6358', 500)
    ph = h*.9; pw = ph*200/260
    for i, (fn, dx) in enumerate([(plants.monstera, -170), (plants.fiddle, 0), (plants.snake, 170)]):
        x = w*.74 - pw/2 + dx*(h/630); sc = 1 if i == 1 else .78
        yy = h - ph*sc - (10 if i == 1 else 0)
        b += embed(fn('revived'), x + (pw - pw*sc)/2, yy, pw*sc)
    return svg(f'0 0 {w} {h}', b, 'AuraDrop social card', d + g)

def favicon():
    return svg('28 8 200 250', '<path d="' + DROP + '" fill="#2FB86F"/><g transform="rotate(12 128 160)"><path d="M128 218C92 196 92 146 128 104C164 146 164 196 128 218Z" fill="#FBF8F0"/><path d="M128 208V132" stroke="#1C9358" stroke-width="9" stroke-linecap="round"/></g>', 'AuraDrop favicon')

def patterns():
    # seamless tile of drops, leaves and sparkles
    t = 160
    tile = (f'<rect width="{t}" height="{t}" fill="{C["cream"]}"/>'
            f'<g transform="translate(30 38) scale(.18)"><path d="{DROP}" fill="#3FD283" opacity=".9"/></g>'
            f'<g transform="translate(104 90) rotate(32)"><path d="{leaf_d(34,13)}" fill="#1C9358" opacity=".9"/></g>'
            + sparkle(112, 30, 8, C['lime']) + sparkle(36, 118, 6, C['lime']) +
            f'<g transform="translate(70 148) rotate(-24)"><path d="{leaf_d(22,8)}" fill="#3FD283" opacity=".7"/></g>'
            f'<circle cx="150" cy="140" r="3" fill="#FF7A59" opacity=".8"/><circle cx="12" cy="76" r="3" fill="#7BD3EA"/>')
    pat = svg('0 0 640 640', '<rect width="640" height="640" fill="url(#t)"/>', 'Leaf and drop pattern', f'<pattern id="t" width="{t}" height="{t}" patternUnits="userSpaceOnUse">{tile}</pattern>')
    rings = svg('0 0 600 600', ''.join(f'<circle cx="300" cy="300" r="{r}" fill="none" stroke="#8FE04A" stroke-width="{w}" stroke-opacity="{o}"/>'
                for r, w, o in [(60, 14, 1), (110, 12, .75), (160, 10, .55), (210, 8, .4), (260, 6, .25)]), 'Aura rings')
    sp = svg('0 0 400 160', sparkle(60, 80, 44, C['lime']) + sparkle(160, 50, 26, C['mint']) + sparkle(240, 100, 34, C['leaf']) + sparkle(330, 60, 20, C['lime']) + sparkle(350, 120, 12, C['mint']), 'Sparkles')
    blobs = svg('0 0 600 300', f'<path d="M60 160C40 80 120 20 200 50C270 76 260 150 220 200C170 260 80 250 60 160Z" fill="#8FE04A" opacity=".55"/>'
                f'<path d="M300 80C350 30 440 40 470 100C500 160 460 230 390 240C320 250 250 130 300 80Z" fill="#3FD283" opacity=".5"/>'
                f'<path d="M470 190C490 150 560 150 580 200C596 240 560 280 520 280C480 280 452 230 470 190Z" fill="#FFD35C" opacity=".6"/>', 'Background blobs')
    return pat, rings, sp, blobs

def build():
    save('assets/ui/phone-diagnosis.svg', phone())
    save('assets/social/profile.svg', profile()); save('assets/social/og-card.svg', og()); save('assets/social/banner.svg', og(1500, 500, True))
    save('assets/social/favicon.svg', favicon())
    for n, s in zip(['pattern-leaf-drop', 'aura-rings', 'sparkles', 'blobs'], patterns()): save(f'assets/patterns/{n}.svg', s)
if __name__ == '__main__': build()
