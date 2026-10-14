from lib import *

def bottle_drops():
    body = (f'<ellipse cx="100" cy="258" rx="40" ry="4" fill="#14352A" opacity=".1"/>'
            f'<path d="M62 120Q62 108 74 108H126Q138 108 138 120V240Q138 256 122 256H78Q62 256 62 240Z" fill="#3FD283"/>'
            f'<path d="M62 150H138V232Q138 256 120 256H80Q62 256 62 232Z" fill="#1C9358" opacity=".35"/>'
            f'<rect x="72" y="146" width="56" height="70" rx="8" fill="#FBF8F0"/>'
            f'<path d="M100 158C100 158 88 174 88 184a12 12 0 0 0 24 0C112 174 100 158 100 158Z" fill="#1C9358"/>'
            f'<path d="M108 122H92L88 98H112Z" fill="#14352A"/><rect x="82" y="108" width="36" height="12" rx="4" fill="#14352A"/>'
            f'<ellipse cx="100" cy="86" rx="16" ry="28" fill="#14352A"/><path d="M76 118V240" stroke="#fff" stroke-opacity=".5" stroke-width="5" stroke-linecap="round"/>'
            f'<path d="M100 48C100 48 92 60 92 66a8 8 0 0 0 16 0C108 60 100 48 100 48Z" fill="#8FE04A"/>')
    return svg('0 0 200 270', body, 'Nutrient drops bottle')

def spray():
    body = (f'<ellipse cx="100" cy="258" rx="42" ry="4" fill="#14352A" opacity=".1"/>'
            f'<path d="M62 130Q62 118 74 118H126Q138 118 138 130V240Q138 256 122 256H78Q62 256 62 240Z" fill="#FBF8F0" stroke="#E6E1D3" stroke-width="3"/>'
            f'<rect x="70" y="160" width="60" height="76" rx="9" fill="#FF7A59"/>'
            f'<circle cx="100" cy="190" r="16" fill="#FBF8F0"/><path d="M100 202V182M100 192L92 186M100 196L108 190" stroke="#E8603F" stroke-width="3.5" stroke-linecap="round" fill="none"/>'
            f'<rect x="88" y="100" width="24" height="22" rx="4" fill="#14352A"/><path d="M84 104H132Q142 104 142 92V84H108V96H84Z" fill="#14352A"/>'
            f'<rect x="138" y="82" width="10" height="14" rx="3" fill="#1C9358"/>'
            f'<circle cx="160" cy="76" r="3" fill="#8FE04A"/><circle cx="168" cy="88" r="2.5" fill="#8FE04A"/><circle cx="162" cy="98" r="2" fill="#8FE04A"/>'
            f'<path d="M72 130V240" stroke="#fff" stroke-opacity=".8" stroke-width="4" stroke-linecap="round"/>')
    return svg('0 0 200 270', body, 'Pest remedy spray')

def soil():
    body = (f'<ellipse cx="100" cy="258" rx="58" ry="5" fill="#14352A" opacity=".1"/>'
            f'<path d="M48 70H152L162 244Q163 256 150 256H50Q37 256 38 244Z" fill="#6B4F3A"/>'
            f'<path d="M48 70H152L154 86H46Z" fill="#53392A"/><path d="M52 62H148L152 74H48Z" fill="#8A6A50"/>'
            f'<path d="M54 62L60 54H140L146 62" fill="#8A6A50"/><path d="M62 80H138" stroke="#53392A" stroke-width="3" stroke-dasharray="6 5"/>'
            f'<rect x="58" y="112" width="84" height="104" rx="10" fill="#FBF8F0"/>'
            f'<path d="M100 134C100 134 82 152 82 166a18 18 0 0 0 36 0C118 152 100 134 100 134Z" fill="#1C9358"/>'
            f'<path d="M100 178V152" stroke="#FBF8F0" stroke-width="4" stroke-linecap="round"/>')
    body += text('SOIL', 15, 100, 204, C['forest'], 600, 'middle', 2)
    return svg('0 0 200 270', body, 'Organic soil bag')

def globe():
    body = (f'<ellipse cx="100" cy="258" rx="38" ry="4" fill="#14352A" opacity=".1"/>'
            f'<path d="M92 100H108V130H92Z" fill="#FBF8F0" stroke="#E6E1D3" stroke-width="3"/>'
            f'<path d="M92 132Q92 124 100 124Q108 124 108 132V210H92Z" fill="#7BD3EA" opacity=".6"/>'
            f'<circle cx="100" cy="170" r="62" fill="#7BD3EA" opacity=".28"/>'
            f'<path d="M40 172A60 60 0 0 0 160 172Q100 160 40 172Z" fill="#7BD3EA" opacity=".8"/>'
            f'<circle cx="100" cy="170" r="62" fill="none" stroke="#FBF8F0" stroke-width="5"/>'
            f'<path d="M62 150A44 44 0 0 1 90 120" stroke="#fff" stroke-width="6" stroke-linecap="round" fill="none" opacity=".85"/>'
            f'<path d="M100 74C100 74 90 88 90 96a10 10 0 0 0 20 0C110 88 100 74 100 74Z" fill="#7BD3EA"/>'
            f'<rect x="84" y="226" width="32" height="14" rx="4" fill="#14352A"/>'
            f'<circle cx="80" cy="190" r="4" fill="#fff" opacity=".7"/><circle cx="118" cy="196" r="3" fill="#fff" opacity=".7"/><circle cx="104" cy="204" r="2.5" fill="#fff" opacity=".7"/>')
    return svg('0 0 200 270', body, 'Mini self-watering globe')

def box(open_=False):
    W = 360; defs = MARK_DEFS; body = ''
    if not open_:
        body += ('<ellipse cx="180" cy="270" rx="150" ry="8" fill="#14352A" opacity=".10"/>'
                 '<rect x="40" y="110" width="280" height="150" rx="10" fill="#D9B98A"/>'
                 '<rect x="30" y="86" width="300" height="38" rx="9" fill="#C29F6D"/>'
                 '<rect x="158" y="86" width="44" height="174" fill="#FBF8F0" opacity=".55"/>'
                 '<rect x="40" y="248" width="280" height="12" rx="6" fill="#B38D58" opacity=".5"/>')
        body += mark(144, 138, 72)
        body += text('AuraDrop', 24, 180, 238, C['forest'], 600, 'middle', .5)
        return svg(f'0 0 {W} 290', body, 'AuraDrop box, closed', defs)
    d, g = glow(180, 110, 130, 'bg')
    body += ('<ellipse cx="180" cy="288" rx="150" ry="8" fill="#14352A" opacity=".10"/>' + g +
             '<path d="M70 118L26 54L62 44L96 112Z" fill="#E6CFA6"/><path d="M290 118L334 54L298 44L264 112Z" fill="#E6CFA6"/>'
             '<rect x="50" y="100" width="260" height="30" rx="6" fill="#8F6D40"/>'
             + leaf(180, 112, 0, 92, 26, C['mint'], VEIN['x'] if False else 'rgba(251,248,240,.5)')
             + leaf(180, 112, -34, 70, 20, C['leaf'], 'rgba(251,248,240,.5)') + leaf(180, 112, 34, 70, 20, '#2FB86F', 'rgba(251,248,240,.5)')
             + '<rect x="96" y="76" width="32" height="42" rx="6" fill="#FBF8F0"/><rect x="104" y="64" width="16" height="14" rx="3" fill="#14352A"/>'
             '<path d="M44 124H316L304 276Q303 284 295 284H65Q57 284 56 276Z" fill="#D9B98A"/>'
             '<rect x="44" y="116" width="272" height="20" rx="6" fill="#C29F6D"/>')
    body += mark(150, 160, 60) + text('AuraDrop', 20, 180, 266, C['forest'], 600, 'middle', .5)
    body += sparkle(60, 40, 9, C['lime']) + sparkle(310, 30, 7, C['cream']) + sparkle(250, 60, 6, C['lime'])
    return svg(f'0 0 {W} 300', body, 'AuraDrop box, open', defs + d)

def build():
    for n, s in [('nutrient-drops', bottle_drops()), ('pest-spray', spray()), ('soil-bag', soil()), ('self-watering-globe', globe()),
                 ('box-closed', box()), ('box-open', box(True))]:
        save(f'assets/kit/{n}.svg', s)
if __name__ == '__main__': build()
