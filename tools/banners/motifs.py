#!/usr/bin/env python3
"""Bannières génératives pour la section Code — palette Catppuccin Mocha,
reprise de la bannière tei-mcp existante. Motifs réimplémentés, rien d'emprunté."""
import math, random

BASE, BLUE, TEXT = "#1e1e2e", "#89b4fa", "#cdd6f4"
W, H = 800, 400

# ---------------------------------------------------------------- ITA2 : bande perforée
# Le motif est le sujet même : la bande code réellement « ITA2 » en ITA2.
ITA2 = {'I': '00110', 'T': '10000', 'A': '00011', 'FIG': '11011', '2': '11001'}

def tape():
    seq = [ITA2[c] for c in ['I', 'T', 'A', 'FIG', '2']]
    step, r, sr = 48, 9.5, 3.0           # pas, rayon de trou, rayon d'entraînement
    rows, total = 5, 13                  # amorce vierge de part et d'autre : une vraie bande
    lead = (total - len(seq)) // 2
    codes = ['00000'] * lead + seq + ['00000'] * (total - len(seq) - lead)
    gw = total * step
    x0, y0 = (W - gw) / 2 + step / 2, 62
    p = []
    for edge in (y0 - step * 0.72, y0 + (rows - 1) * step + step * 0.72):
        p.append(f'<line x1="24" y1="{edge:.1f}" x2="{W-24}" y2="{edge:.1f}" '
                 f'stroke="{BLUE}" stroke-width="1" opacity="0.30"/>')
    for c, code in enumerate(codes):
        for b in range(rows):
            cx, cy = x0 + c * step, y0 + b * step
            if code[b] == '1':
                p.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r}" fill="{BLUE}"/>')
            else:
                p.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r}" fill="none" '
                         f'stroke="{BLUE}" stroke-width="1.1" opacity="0.34"/>')
            if b == 2:
                p.append(f'<circle cx="{cx:.1f}" cy="{cy + step/2:.1f}" r="{sr}" '
                         f'fill="{BLUE}" opacity="0.7"/>')
    return "\n".join(p)

# ------------------------------------------------------- Multi-Saxon : champ d'ondes
# Lignes parallèles traitées ensemble : le parallélisme, dessiné.
def ridges():
    random.seed(7)
    lines, n, cols = [], 16, 150
    for i in range(n):
        y0 = 102 + i * 12.0
        pts = []
        for j in range(cols + 1):
            x = 96 + j * (608 / cols)
            t = j / cols
            env = math.exp(-((t - 0.5) ** 2) / 0.055)          # crête centrale
            amp = 30 * env * (0.35 + 0.65 * math.sin(math.pi * (i + 1) / (n + 1)))
            y = y0 - amp * (0.55 * math.sin(t * 11 + i * 0.7)
                            + 0.45 * math.sin(t * 19 + i * 1.9))
            pts.append(f"{x:.1f},{y:.1f}")
        lines.append(f'<polyline points="{" ".join(pts)}" fill="{BASE}" stroke="{BLUE}" '
                     f'stroke-width="1.2" opacity="{0.30 + 0.55 * i / n:.2f}"/>')
    return "\n".join(lines)

# ------------------------------------------------------- persNamer : floraison phyllotaxique
# Beaucoup d'unités rangées par une règle : l'ordre d'autorité, en somme.
def phyllotaxis():
    golden = math.pi * (3 - math.sqrt(5))
    cx, cy, n, out = W / 2, 176, 380, []
    for i in range(n):
        a = i * golden
        rad = 8.4 * math.sqrt(i)
        x, y = cx + rad * math.cos(a), cy + rad * math.sin(a)
        if not (60 < x < W - 60 and 34 < y < 288):
            continue
        t = i / n
        out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{1.4 + 3.2 * t:.1f}" '
                   f'fill="{BLUE}" opacity="{0.22 + 0.6 * t:.2f}"/>')
    return "\n".join(out)

def svg(motif, word, tagline, wy=330, ty=366):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<rect width="{W}" height="{H}" fill="{BASE}"/>
{motif}
<text x="{W/2}" y="{wy}" text-anchor="middle" fill="{TEXT}"
      font-family="SF Mono, Menlo, DejaVu Sans Mono, monospace" font-size="34"
      font-weight="700" letter-spacing="7">{word}</text>
<text x="{W/2}" y="{ty}" text-anchor="middle" fill="{TEXT}" opacity="0.62"
      font-family="SF Mono, Menlo, DejaVu Sans Mono, monospace" font-size="17"
      letter-spacing="1">{tagline}</text>
</svg>'''

if __name__ == "__main__":
    open("m_ita2.svg", "w").write(svg(tape(), "ITA2", "Baudot-Murray telegraph code"))
    open("m_multisaxon.svg", "w").write(svg(ridges(), "MULTI-SAXON", "Parallel XSLT for TEI corpora"))
    open("m_persnamer.svg", "w").write(svg(phyllotaxis(), "PERSNAMER", "VIAF identifiers to TEI persons"))
    print("m_ita2.svg m_multisaxon.svg m_persnamer.svg")
