"""Synthesises the promo's sound effects (no music) into video/sfx.wav.
Usage: python3 video/sfx.py   (needs numpy). video/build.sh muxes it into the MP4s."""
import numpy as np, wave, os
SR = 48000; DUR = 13.0
rng = np.random.default_rng(7)
mix = np.zeros(int(SR * (DUR + 0.5)))
T = lambda d: np.arange(int(SR * d)) / SR
def add(t, s, g=1.0):
    i = int(t * SR); s = s * g; mix[i:i + len(s)] += s[:len(mix) - i]

def lp_sweep(x, f0, f1):
    """one-pole low-pass whose cutoff sweeps f0->f1 (Hz)"""
    out = np.empty_like(x); y = 0.0; n = len(x)
    for k in range(n):
        f = f0 + (f1 - f0) * k / n; a = 1 - np.exp(-2 * np.pi * f / SR); y += a * (x[k] - y); out[k] = y
    return out
def hp(x, f):
    a = np.exp(-2 * np.pi * f / SR); y = 0.0; lp = np.empty_like(x)
    for k in range(len(x)): y = (1 - a) * x[k] + a * y; lp[k] = y
    return x - lp

def whoosh(d=0.16, f0=300, f1=5000):
    n = rng.standard_normal(int(SR * d)); t = np.linspace(0, 1, len(n))
    env = np.sin(np.pi * t ** 0.8) ** 1.5
    return lp_sweep(n, f0, f1) * env * 2.2
def thud(d=0.28, f0=150, f1=42, click=1.0):
    t = T(d); ph = 2 * np.pi * np.cumsum(f1 + (f0 - f1) * np.exp(-t * 28)) / SR
    s = np.sin(ph) * np.exp(-t * 11)
    c = lp_sweep(rng.standard_normal(int(SR * .012)), 6000, 900) * np.linspace(1, 0, int(SR * .012)) * click
    s[:len(c)] += c * 1.4; return s
def boom(d=0.7):
    t = T(d); s = np.sin(2 * np.pi * np.cumsum(38 + 90 * np.exp(-t * 18)) / SR) * np.exp(-t * 5)
    tail = lp_sweep(rng.standard_normal(len(t)), 900, 120) * np.exp(-t * 6) * .5
    return s * 1.3 + tail
def pop(f=700, d=0.09):
    t = T(d); s = np.sin(2 * np.pi * np.cumsum(f * (1 + 1.4 * np.exp(-t * 40))) / SR) * np.exp(-t * 38)
    return s + hp(rng.standard_normal(len(t)), 2500) * np.exp(-t * 250) * .25
def ping(f=1760, d=0.4):
    t = T(d); return (np.sin(2 * np.pi * f * t) + .4 * np.sin(2 * np.pi * f * 2.01 * t)) * np.exp(-t * 11) * .5
def shutter():
    s = np.zeros(int(SR * .14))
    for off, g in ((0, 1), (.045, .7)):
        n = hp(rng.standard_normal(int(SR * .02)), 1800) * np.exp(-T(.02) * 220) * g; i = int(off * SR); s[i:i + len(n)] += n
    return s * 1.6
def scan(d=0.5):
    t = T(d); f = 300 + 1700 * (t / d) ** 1.6
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.sin(np.pi * t / d) * .22
def shimmer(d=0.5):
    out = np.zeros(int(SR * d))
    for k, f in enumerate((1568, 2093, 2637, 3136)):
        p = ping(f, d - .1 - k * .02); i = int(k * .05 * SR); out[i:i + len(p)] += p * .7
    return out
def slam(t, g=1.0, heavy=False, d=.13, f0=300, f1=5000):
    add(t - d, whoosh(d, f0, f1), .5 * g)
    add(t, boom() if heavy else thud(), (.85 if heavy else .7) * g)

# ---- timeline (absolute seconds; landing time = scene start + enter start + duration) ----
slam(.16); slam(.17, .6); slam(.63, 1, True)                     # 0 YOUR PLANT / IS FADING.
slam(1.13); slam(1.21, .6); add(1.5, shutter(), .9)               # 1 SNAP. + camera click
slam(2.16); slam(2.17, .5); slam(2.63, .9)                        # 2 ONE PHOTO.
slam(3.13); slam(3.15, .5); add(3.06, scan(), .8)                 # 3 DIAGNOSE.
for t in (3.32, 3.5, 3.68): add(t, pop(700), .9); add(t, thud(.15, 120, 60, .3), .5)
slam(4.13, .8); slam(4.31, 1.0, True, .11)                        # 4 DROP. + box crash
slam(5.13, .6); slam(5.15, .5)                                    # 5 ONE KIT.
for k, t in enumerate((5.27, 5.41, 5.55, 5.69)): add(t - .12, whoosh(.12), .35); add(t, pop(520 + k * 90, .12), .9); add(t, thud(.18, 110, 55), .5)
add(6.0, boom(), 1.0); add(6.0, shimmer(.7), .8); slam(6.15, .7)  # 6 GLOW.
for t in (6.4, 6.5, 6.6): add(t, ping(1568 + (t - 6.4) * 4000, .4), .6)
slam(7.15, .8)                                                    # 7 BEFORE -> AFTER
add(7.5, whoosh(.14, 800, 9000), 1.0); add(7.64, boom(.5), .8); add(7.64, shimmer(.6), .7)
slam(8.13, .6)                                                    # 8 ANY PLANT.
for i in range(6): add(8.23 + i * .1, pop(520 + i * 70, .09), .8); add(8.23 + i * .1, thud(.12, 130, 60, .3), .4)
slam(9.13, .6)                                                    # 9 4 STEPS.
for k, t in enumerate((9.23, 9.43, 9.63, 9.83)): add(t - .1, whoosh(.1), .35); add(t, thud(.2, 160, 50), .9); add(t, pop(600 + k * 120, .08), .6)
slam(10.13, 1, True); slam(10.63, 1, True)                        # 10 SECOND / WIND.
slam(11.15, 1, True, .15); add(11.15, shimmer(.8), .6); slam(11.58, .5, False, .1)   # 11 logo + tagline
slam(12.13, .8, True); slam(12.38, .8, True); slam(12.63, .6)     # 12 CTA
add(12.72, ping(2093, .3), .6); add(12.82, ping(2637, .35), .6)

# ---- master: soft-limit, normalise to about -4 dBFS, 16-bit WAV ----
m = mix[:int(SR * DUR)]; m = np.tanh(m * 1.1); m *= 0.63 / max(1e-6, np.abs(m).max())
fade = int(SR * .08); m[-fade:] *= np.linspace(1, 0, fade)
here = os.path.dirname(os.path.abspath(__file__)); wav = os.path.join(here, 'sfx.wav')
with wave.open(wav, 'wb') as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((m * 32767).astype('<i2').tobytes())
print('wrote', wav)
