from lib import *
F, L, M, LI, CR = C['forest'], C['leaf'], C['mint'], C['lime'], C['cream']
S = f'fill="none" stroke="{F}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"'
LEAF = 'M0 0C-14 -8 -14 -30 0 -44C14 -30 14 -8 0 0Z'

def st(w=5,col=F): return f'fill="none" stroke="{col}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"'

def icon(label, body): return svg('0 0 96 96', body, label)

def snap():
    return icon('Snap', f'<rect x="12" y="28" width="72" height="50" rx="12" fill="{CR}" {S[S.index("stroke="):]}/>'
        f'<path d="M34 28L39 18H57L62 28" {S}/><circle cx="48" cy="53" r="17" fill="{LI}" stroke="{F}" stroke-width="5"/>'
        f'<g transform="translate(48 63) scale(.5)"><path d="{LEAF}" fill="{L}"/></g><circle cx="73" cy="40" r="3" fill="{F}"/>')

def diagnose():
    return icon('Diagnose', f'<g transform="translate(40 66) rotate(-18)"><path d="{LEAF}" fill="{M}" stroke="{F}" stroke-width="4" stroke-linejoin="round" transform="scale(.9)"/></g>'
        f'<circle cx="46" cy="42" r="26" fill="{CR}" fill-opacity=".55" stroke="{F}" stroke-width="5"/><path d="M65 61L82 78" {st(7)}/>'
        f'<path d="M31 43H40L44 33L50 52L54 43H61" {st(4,L)}/>')

def drop():
    return icon('Drop', f'<path d="M14 40L48 24L82 40V72L48 86L14 72Z" fill="{CR}" {S[S.index("stroke="):]}/>'
        f'<path d="M14 40L48 56L82 40M48 56V86" {S}/><path d="M48 4C48 4 38 16 38 22a10 10 0 0 0 20 0C58 16 48 4 48 4Z" fill="{LI}" stroke="{F}" stroke-width="4"/>')

def glow_i():
    return icon('Glow', f'<circle cx="48" cy="52" r="34" fill="{LI}" opacity=".45"/><g transform="translate(48 82)"><path d="{LEAF}" fill="{M}" stroke="{F}" stroke-width="3.6" stroke-linejoin="round" transform="scale(1.35)"/>'
        f'<path d="M0 -4V-52" stroke="{F}" stroke-width="4" stroke-linecap="round"/></g>' + sparkle(18, 22, 8, F) + sparkle(78, 30, 6, L) + sparkle(76, 76, 5, F))

def water():
    return icon('Water', f'<path d="M48 12C48 12 22 40 22 58a26 26 0 0 0 52 0C74 40 48 12 48 12Z" fill="{C["water"]}" {S[S.index("stroke="):]}/><path d="M36 60Q38 70 48 72" {st(4,CR)}/>')

def sun():
    rays = ''.join(f'<path d="M48 {y1}V{y2}" {S} transform="rotate({a} 48 48)"/>' for a in range(0, 360, 45) for y1, y2 in [(10, 20)])
    return icon('Light', f'<circle cx="48" cy="48" r="17" fill="{C["sun"]}" stroke="{F}" stroke-width="5"/>{rays}')

def bug():
    return icon('Pests', f'<ellipse cx="48" cy="56" rx="18" ry="24" fill="{C["coral"]}" stroke="{F}" stroke-width="5"/><circle cx="48" cy="28" r="10" fill="{CR}" stroke="{F}" stroke-width="5"/>'
        f'<path d="M30 48H14M30 60H12M30 72L18 82M66 48H82M66 60H84M66 72L78 82M42 18L36 8M54 18L60 8M48 34V78" {st(4)}/>')

def soil_i():
    return icon('Soil', f'<path d="M10 80Q16 52 48 52Q80 52 86 80Z" fill="{C["soil"]}" stroke="{F}" stroke-width="5" stroke-linejoin="round"/>'
        f'<path d="M48 52V30" {S}/><path d="M48 36C38 36 32 30 32 20C42 20 48 26 48 36Z" fill="{M}" stroke="{F}" stroke-width="4" stroke-linejoin="round"/><path d="M48 40C58 40 64 34 64 24C54 24 48 30 48 40Z" fill="{LI}" stroke="{F}" stroke-width="4" stroke-linejoin="round"/>')

def build():
    items = dict(snap=snap(), diagnose=diagnose(), drop=drop(), glow=glow_i(), water=water(), light=sun(), pests=bug(), soil=soil_i())
    for n, s in items.items(): save(f'assets/icons/{n}.svg', s)
if __name__ == '__main__': build()
