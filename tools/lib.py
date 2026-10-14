"""Shared helpers for generating AuraDrop SVG assets (flat 2D, no faces)."""
import math, os
from functools import lru_cache
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONT = os.path.join(ROOT, 'tools', 'fonts', 'Fredoka.ttf')

C = dict(forest='#14352A', leaf='#1C9358', mint='#3FD283', lime='#8FE04A', sage='#9AA39E',
         cream='#FBF8F0', coral='#FF7A59', coral_d='#E8603F', kraft='#D9B98A', kraft_d='#C29F6D',
         water='#7BD3EA', sun='#FFD35C', soil='#6B4F3A')

def f(x): return ('%.1f' % x).rstrip('0').rstrip('.')

@lru_cache(None)
def _font(w):
    return instantiateVariableFont(TTFont(FONT), {'wght': w, 'wdth': 100})

def text_width(s, size, w=600, ls=0):
    ft = _font(w); gs = ft.getGlyphSet(); cm = ft.getBestCmap(); u = ft['head'].unitsPerEm
    return sum(gs[cm[ord(c)]].width * size / u + ls for c in s) - ls

def text(s, size, x, y, fill, w=600, anchor='start', ls=0):
    """Outlined text -> <path>. y is the baseline."""
    ft = _font(w); gs = ft.getGlyphSet(); cm = ft.getBestCmap(); u = ft['head'].unitsPerEm
    sc = size / u; tw = text_width(s, size, w, ls)
    cx = x - (tw / 2 if anchor == 'middle' else tw if anchor == 'end' else 0)
    d = []
    for ch in s:
        g = gs[cm[ord(ch)]]; pen = SVGPathPen(gs, ntos=lambda v: f(v))
        g.draw(TransformPen(pen, (sc, 0, 0, -sc, cx, y))); d.append(pen.getCommands())
        cx += g.width * sc + ls
    return f'<path d="{" ".join(d)}" fill="{fill}"/>'

def svg(vb, body, label='', defs=''):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" role="img" aria-label="{label}">'
            f'{"<defs>"+defs+"</defs>" if defs else ""}{body}</svg>\n')

def save(path, s):
    p = os.path.join(ROOT, path); os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w').write(s)

# ---- geometry ---------------------------------------------------------
def qpt(p0, c, p2, t):
    return ((1-t)**2*p0[0]+2*(1-t)*t*c[0]+t*t*p2[0], (1-t)**2*p0[1]+2*(1-t)*t*c[1]+t*t*p2[1])
def qtan(p0, c, p2, t):
    return (2*(1-t)*(c[0]-p0[0])+2*t*(p2[0]-c[0]), 2*(1-t)*(c[1]-p0[1])+2*t*(p2[1]-c[1]))
def ang(v):  # SVG rotate() angle for a vector, 0 = up, clockwise positive
    return math.degrees(math.atan2(v[0], -v[1]))

def leaf_d(L, W):
    return f'M0 0C{f(-W)} {f(-L*.25)} {f(-W*.9)} {f(-L*.8)} 0 {f(-L)}C{f(W*.9)} {f(-L*.8)} {f(W)} {f(-L*.25)} 0 0Z'
def heart_d(L, W):
    a = lambda *v: ' '.join(f(x) for x in v)
    return ('M0 '+f(-.1*L)+'C'+a(-.55*W,.12*L,-1.25*W,-.15*L,-1.1*W,-.5*L)+'C'+a(-1.0*W,-.75*L,-.4*W,-.9*L,0,-L)
            +'C'+a(.4*W,-.9*L,1.0*W,-.75*L,1.1*W,-.5*L)+'C'+a(1.25*W,-.15*L,.55*W,.12*L,0,-.1*L)+'Z')

def leaf(x, y, a, L, W, fill, vein, shape='leaf', extra=''):
    d = leaf_d(L, W) if shape == 'leaf' else heart_d(L, W)
    return (f'<g transform="translate({f(x)} {f(y)}) rotate({f(a)})"><path d="{d}" fill="{fill}"{extra}/>'
            f'<path d="M0 {f(-L*.06)}L0 {f(-L*.82)}" stroke="{vein}" stroke-width="{f(max(1.6,W*.09))}" stroke-linecap="round" fill="none"/></g>')

def stem(p0, c, p2, color, w=5):
    return (f'<path d="M{f(p0[0])} {f(p0[1])}Q{f(c[0])} {f(c[1])} {f(p2[0])} {f(p2[1])}" '
            f'fill="none" stroke="{color}" stroke-width="{w}" stroke-linecap="round"/>')

def ribbon(p0, c, p2, w, fill, n=18):
    """Blade of width w tapering to a point along a quadratic curve."""
    L, R = [], []
    for i in range(n+1):
        t = i/n; x, y = qpt(p0, c, p2, t); tx, ty = qtan(p0, c, p2, t); m = math.hypot(tx, ty) or 1
        nx, ny = -ty/m, tx/m; ww = w*(1-t**1.6)**0.9
        L.append((x+nx*ww, y+ny*ww)); R.append((x-nx*ww, y-ny*ww))
    pts = L + R[::-1]
    return f'<path d="M{" L".join(f(a)+" "+f(b) for a,b in pts)}Z" fill="{fill}"/>'

def sparkle(x, y, r, fill, op=1):
    k = r*.28
    return (f'<path d="M{f(x)} {f(y-r)}Q{f(x+k)} {f(y-k)} {f(x+r)} {f(y)}Q{f(x+k)} {f(y+k)} {f(x)} {f(y+r)}'
            f'Q{f(x-k)} {f(y+k)} {f(x-r)} {f(y)}Q{f(x-k)} {f(y-k)} {f(x)} {f(y-r)}Z" fill="{fill}" opacity="{op}"/>')

def glow(cx, cy, r, gid='g', color=C['lime'], op=.55):
    return (f'<radialGradient id="{gid}"><stop offset="0" stop-color="{color}" stop-opacity="{op}"/>'
            f'<stop offset="1" stop-color="{color}" stop-opacity="0"/></radialGradient>',
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#{gid})"/>')

DROP = 'M128 20C128 20 44 108 44 164a84 84 0 0 0 168 0C212 108 128 20 128 20Z'
def mark(x, y, size, simple=False):
    """Inline AuraDrop mark (gradient id mgrad needs defs MARK_DEFS)."""
    sc = size/250
    arcs = '' if simple else ('<path d="M158.5 46A118 118 0 0 1 234.9 110.1" fill="none" stroke="#8FE04A" stroke-width="10" stroke-linecap="round"/>'
        '<path d="M164.2 24.8A140 140 0 0 1 254.9 100.8" fill="none" stroke="#8FE04A" stroke-opacity=".5" stroke-width="10" stroke-linecap="round"/>')
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(sc)}) translate(-20 -8)">{arcs}<path d="{DROP}" fill="url(#mgrad)"/>'
            '<g transform="rotate(12 128 160)"><path d="M128 218C92 196 92 146 128 104C164 146 164 196 128 218Z" fill="#FBF8F0"/>'
            '<path d="M128 208V132" stroke="#1C9358" stroke-width="6" stroke-linecap="round"/>'
            + ('' if simple else '<path d="M128 170L110 156M128 186L146 172" stroke="#1C9358" stroke-width="5" stroke-linecap="round"/>') + '</g></g>')
MARK_DEFS = '<linearGradient id="mgrad" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3FD283"/><stop offset="1" stop-color="#1C9358"/></linearGradient>'

_n = [0]
def embed(svgstr, x, y, w, h=None):
    """Nest another generated SVG inside a scene, prefixing ids to avoid clashes."""
    import re
    _n[0] += 1; p = f'e{_n[0]}_'
    m = re.match(r'<svg[^>]*viewBox="([^"]+)"[^>]*>', svgstr); vb = m.group(1)
    vw, vh = [float(v) for v in vb.split()[2:]]; h = h or w*vh/vw
    inner = svgstr[m.end():].rsplit('</svg>', 1)[0]
    inner = re.sub(r'id="([^"]+)"', lambda k: f'id="{p}{k.group(1)}"', inner)
    inner = re.sub(r'url\(#([^)]+)\)', lambda k: f'url(#{p}{k.group(1)})', inner)
    return f'<svg x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(h)}" viewBox="{vb}" overflow="visible">{inner}</svg>'
