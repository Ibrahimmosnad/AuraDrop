from lib import *

TONES = {'revived': ['#1C9358', '#2FB86F', '#3FD283'], 'wilted': ['#8E9892', '#A3ABA5', '#B7BDB4']}
VEIN = {'revived': 'rgba(251,248,240,.45)', 'wilted': 'rgba(251,248,240,.35)'}
STEM = {'revived': '#1C7A4A', 'wilted': '#8A9490'}
POT = {'revived': (C['coral'], C['coral_d']), 'wilted': ('#C9C3B6', '#B3AD9F')}

def pot(s, x=100):
    b, r = POT[s]
    return (f'<ellipse cx="{x}" cy="257" rx="52" ry="4" fill="#14352A" opacity=".10"/>'
            f'<path d="M{x-45} 194H{x+45}L{x+37} 250Q{x+36} 256 {x+30} 256H{x-30}Q{x-36} 256 {x-37} 250Z" fill="{b}"/>'
            f'<rect x="{x-52}" y="178" width="104" height="19" rx="7" fill="{r}"/>')

def aura(s):
    if s != 'revived': return '', ''
    d, g = glow(100, 120, 98, 'gl')
    sp = sparkle(36, 64, 9, C['lime']) + sparkle(168, 52, 6, C['cream']) + sparkle(172, 128, 8, C['lime']) + sparkle(30, 140, 5, C['cream'])
    return d, g + sp

def wrap(s, body, label, extra_defs=''):
    d, a = aura(s)
    return svg('0 0 200 260', a + body, label, d + extra_defs)

def tone(s, i): return TONES[s][i % 3]

def fiddle(s):
    rv = s == 'revived'
    p0, c, p2 = (100, 184), ((100, 110) if rv else (92, 92)), ((100, 52) if rv else (146, 92))
    out = stem(p0, c, p2, STEM[s], 6)
    for i, t in enumerate([.3, .45, .6, .75, .9]):
        side = 1 if i % 2 == 0 else -1; x, y = qpt(p0, c, p2, t)
        a = side*(52 if rv else 128) + (0 if rv else 8*i*side)
        out += leaf(x, y, a, 48 if rv else 42, 25 if rv else 20, tone(s, i), VEIN[s])
    x, y = qpt(p0, c, p2, 1)
    out += leaf(x, y, 0 if rv else 150, 44 if rv else 38, 23 if rv else 18, tone(s, 2), VEIN[s])
    return wrap(s, out + pot(s), f'Fiddle-leaf fig, {s}')

def monstera(s):
    rv = s == 'revived'
    spec = ([((62, 116), (66, 164), -10, 50, 30), ((100, 74), (100, 140), 0, 58, 34), ((140, 112), (136, 162), 10, 50, 30)] if rv else
            [((58, 150), (62, 108), 195, 46, 29), ((100, 122), (100, 76), 180, 50, 31), ((142, 148), (138, 106), 165, 46, 29)])
    masks, out = '', ''
    for i, (tip, ctrl, da, L, W) in enumerate(spec):
        out += stem((100, 184), ctrl, tip, STEM[s], 5)
        a = ang(qtan((100, 184), ctrl, tip, 1)) + (da if rv else 0) * (0 if rv else 0)
        a = a + (da if rv else (da-180))
        mid = f'm{i}'
        slits = ''.join(f'<path d="M0 {f(-L*y)}L{f(sx*W*1.4)} {f(-L*(y-.12))}" stroke="#000" stroke-width="{3.4 if rv else 3}" stroke-linecap="round"/>'
                        for y in (.42, .66) for sx in (-1, 1))
        masks += (f'<mask id="{mid}" maskUnits="userSpaceOnUse" x="{f(-W*2)}" y="{f(-L*1.2)}" width="{f(W*4)}" height="{f(L*1.5)}">'
                  f'<rect x="{f(-W*2)}" y="{f(-L*1.2)}" width="{f(W*4)}" height="{f(L*1.5)}" fill="#fff"/>{slits}</mask>')
        out += (f'<g transform="translate({f(tip[0])} {f(tip[1])}) rotate({f(a)})"><g mask="url(#{mid})">'
                f'<path d="{heart_d(L, W)}" fill="{tone(s, i)}"/></g>'
                f'<path d="M0 {f(-L*.06)}L0 {f(-L*.88)}" stroke="{VEIN[s]}" stroke-width="2.6" stroke-linecap="round"/></g>')
    return wrap(s, out + pot(s), f'Monstera, {s}', masks)

def snake(s):
    rv = s == 'revived'
    blades = [(-30, -38, 118), (-14, -16, 150), (4, 4, 168), (20, 26, 146), (34, 46, 114)]
    out = ''
    for i, (bx, tx, L) in enumerate(blades):
        p0 = (100+bx, 186)
        if rv: p2, c = (100+tx, 186-L), (100+bx+(tx-bx)*.4, 186-L*.55)
        else:  p2, c = (100+tx*1.5+(8 if tx>0 else -8), 186-L*.42), (100+bx+(tx-bx)*.5, 186-L*1.0)
        out += ribbon(p0, c, p2, 17, tone(s, i))
        out += f'<path d="M{f(p0[0])} {f(p0[1])}Q{f(c[0])} {f(c[1])} {f(p2[0])} {f(p2[1])}" fill="none" stroke="{VEIN[s]}" stroke-width="2.4" stroke-linecap="round" stroke-dasharray="1 9"/>'
    return wrap(s, out + pot(s), f'Snake plant, {s}')

def pothos(s):
    rv = s == 'revived'
    vines = ([((90, 184), (40, 116), (42, 186)), ((110, 184), (160, 112), (158, 184)), ((100, 184), (96, 100), (104, 64))] if rv else
             [((62, 188), (36, 204), (48, 226)), ((138, 188), (164, 204), (152, 226)), ((100, 184), (112, 150), (104, 130))])
    out = ''
    for vi, (p0, c, p2) in enumerate(vines):
        out += stem(p0, c, p2, STEM[s], 4)
        for i, t in enumerate([.3, .45, .6, .75, .9, 1.0]):
            x, y = qpt(p0, c, p2, t); a = ang(qtan(p0, c, p2, t)); side = 1 if i % 2 == 0 else -1
            if t == 1.0: side = 0
            L = (30 if rv else 24) * (1 if vi < 2 else 1.05)
            out += leaf(x, y, a + side*(62 if rv else 40), L, 17 if rv else 13, tone(s, vi+i), VEIN[s], 'heart')
    return wrap(s, (pot(s) + out) if not rv else (out + pot(s)), f'Pothos, {s}')

def succulent(s):
    rv = s == 'revived'
    k = 1 if rv else 1.75
    rows = [([-62, -31, 0, 31, 62], 70, 19, 0), ([-48, -16, 16, 48], 56, 18, 1), ([-78, -40, 0, 40, 78], 38, 16, 2)]
    out = ''
    for angs, L, W, ti in rows:
        for j, a in enumerate(angs):
            aa = a*k if abs(a) > 0 else 0
            if not rv and a == 0: aa = 8
            out += leaf(100, 178, max(-112, min(112, aa)), L*(1 if rv else .78), W*(1 if rv else .9), tone(s, ti), VEIN[s])
    return wrap(s, out + pot(s), f'Succulent, {s}')

def terrarium(s):
    rv = s == 'revived'
    sc, sc2 = (C['soil'], '#8A6A50') if rv else ('#8A8478', '#9C968A')
    body = (f'<path d="M62 92Q62 70 82 70H118Q138 70 138 92V222Q138 252 108 252H92Q62 252 62 222Z" fill="{C["water"] if rv else "#C4CBC8"}" opacity=".32"/>'
            f'<path d="M62 190H138V222Q138 252 108 252H92Q62 252 62 222Z" fill="{sc}"/><path d="M62 190Q100 178 138 190V198Q100 186 62 198Z" fill="{sc2}"/>'
            f'<circle cx="80" cy="232" r="5" fill="#FBF8F0" opacity=".7"/><circle cx="98" cy="238" r="4" fill="#E6E0D2"/><circle cx="118" cy="230" r="5.5" fill="#FBF8F0" opacity=".7"/>')
    if rv:
        body += (leaf(100, 192, 0, 62, 17, tone(s, 0), VEIN[s]) + leaf(100, 192, -32, 50, 15, tone(s, 1), VEIN[s]) + leaf(100, 192, 32, 50, 15, tone(s, 2), VEIN[s])
                 + leaf(82, 194, -58, 30, 10, tone(s, 2), VEIN[s]) + leaf(120, 194, 58, 30, 10, tone(s, 1), VEIN[s]))
    else:
        body += (leaf(100, 192, 28, 46, 13, tone(s, 0), VEIN[s]) + leaf(100, 192, -118, 40, 12, tone(s, 1), VEIN[s]) + leaf(100, 192, 120, 36, 12, tone(s, 2), VEIN[s])
                 + leaf(84, 194, -140, 24, 8, tone(s, 2), VEIN[s]))
    body += (f'<path d="M62 92Q62 70 82 70H118Q138 70 138 92V222Q138 252 108 252H92Q62 252 62 222Z" fill="none" stroke="#FBF8F0" stroke-opacity=".9" stroke-width="3.5"/>'
             f'<path d="M72 100V196" stroke="#fff" stroke-opacity=".7" stroke-width="4" stroke-linecap="round"/>'
             f'<rect x="76" y="56" width="48" height="18" rx="7" fill="{C["forest"] if rv else "#7C8782"}"/>')
    return wrap(s, f'<ellipse cx="100" cy="257" rx="50" ry="4" fill="#14352A" opacity=".10"/>' + body, f'Terrarium, {s}')

PLANTS = dict(fiddle_leaf_fig=fiddle, monstera=monstera, snake_plant=snake, pothos=pothos, succulent=succulent, terrarium=terrarium)

def build():
    for name, fn in PLANTS.items():
        for s in ('wilted', 'revived'):
            save(f'assets/plants/{name.replace("_","-")}-{s}.svg', fn(s))
if __name__ == '__main__': build()
