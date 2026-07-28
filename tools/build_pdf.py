#!/usr/bin/env python3
"""
Rendert een markdown-rapport naar een PDF in de Gold Lemon-huisstijl.

Huisstijl volgens het Gold Lemon Brand Book:
  Digital Black    #1a1a1a   basiskleur / donkere pagina's
  Electric Cyan    #00ffff   neon-accent
  Vibrant Magenta  #ff00ff   neon-accent
  Future Blue      #1f80ff   secundair accent
  Montserrat                 primaire letterfamilie

Gebruik:
    python3 tools/build_pdf.py <input.md> <output.pdf> [--ondertitel "..."]
"""

import argparse
import base64
import pathlib
import re
import sys

import markdown
from weasyprint import HTML

# --- Huisstijl ---------------------------------------------------------------

BLACK = "#1a1a1a"
CYAN = "#00ffff"
MAGENTA = "#ff00ff"
BLUE = "#1f80ff"

# Neon op wit is onleesbaar; dit zijn de donkere varianten voor tekst op
# lichte pagina's. De pure neonkleuren blijven gereserveerd voor de
# donkere pagina's, waar ze horen.
INK_MAGENTA = "#b0107a"
INK_CYAN = "#08788c"
INK = "#22262b"
MUTED = "#5d666f"
RULE = "#dfe3e8"
WASH = "#f6f8fa"

# Kleurcodering van de betrouwbaarheidslabels uit het rapport.
LABELS = {
    "GEMETEN": ("#0d7a5f", "#e3f5ef"),
    "ZOEK": (INK_CYAN, "#e2f4f8"),
    "AFGELEID": ("#8a6d10", "#fbf3dd"),
    "ONBEVESTIGD": ("#a3341c", "#fbeae5"),
}

CSS = f"""
@page {{
    size: A4;
    margin: 20mm 17mm 18mm 17mm;
    @bottom-left {{
        content: "Gold Lemon · vertrouwelijk";
        font-family: Montserrat; font-size: 7.5pt; color: {MUTED};
    }}
    @bottom-right {{
        content: counter(page) " / " counter(pages);
        font-family: Montserrat; font-size: 7.5pt; color: {MUTED};
    }}
}}
@page cover {{
    margin: 0;
    background: {BLACK};
    @bottom-left {{ content: none; }}
    @bottom-right {{ content: none; }}
}}

*, *::before, *::after {{ box-sizing: border-box; }}
html {{ font-family: Montserrat, "Liberation Sans", sans-serif; }}
body {{ font-size: 9.4pt; line-height: 1.62; color: {INK}; }}

/* ---------- Omslag ---------- */
.cover {{
    page: cover;
    height: 297mm; width: 210mm;
    background: {BLACK};
    color: #ffffff;
    padding: 30mm 22mm 22mm 22mm;
    position: relative;
    /* space-between verdeelt kop, titel en voet over de hoogte. Dat is
       robuuster dan absolute positionering, die in de paginacontext
       van WeasyPrint wegvalt. */
    display: flex; flex-direction: column; justify-content: space-between;
}}
/* Neon-raster: de "lines and grids" uit het brand book. */
.cover .grid {{
    position: absolute; left: 0; right: 0; top: 0; height: 297mm;
    background-image:
        linear-gradient(rgba(0,255,255,.055) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255,0,255,.055) 1px, transparent 1px);
    background-size: 11mm 11mm, 11mm 11mm;
}}
.cover .glow {{
    position: absolute; top: 0; left: 0; right: 0; height: 3.2mm;
    background: linear-gradient(90deg, {CYAN} 0%, {BLUE} 48%, {MAGENTA} 100%);
}}
.wordmark {{
    font-size: 27pt; font-weight: 800; letter-spacing: .10em;
    text-transform: uppercase; line-height: 1;
    color: #ffffff;
    text-shadow: 0 0 1px {CYAN}, 0 0 9px rgba(0,255,255,.85),
                 0 0 26px rgba(255,0,255,.55);
}}
.wordmark .lemon {{ color: {CYAN}; }}
.cover .kicker {{
    margin-top: 4mm; font-size: 8pt; letter-spacing: .30em;
    text-transform: uppercase; color: {CYAN}; font-weight: 600;
}}
.cover h1 {{
    margin: 0; font-size: 26pt; font-weight: 800;
    line-height: 1.14; letter-spacing: -.015em; color: #ffffff;
    max-width: 150mm; overflow-wrap: break-word;
    /* Moet de globale h1-regel overrulen, anders springt de titel
       van de omslag naar de volgende pagina. */
    break-before: avoid;
    border-bottom: none; padding-bottom: 0;
}}
.cover .accentbar {{
    width: 46mm; height: 1.6mm; margin: 7mm 0 7mm 0;
    background: linear-gradient(90deg, {MAGENTA}, {CYAN});
}}
.cover .sub {{ font-size: 12.5pt; color: #d7dde3; font-weight: 300; max-width: 130mm; }}
.cover .meta {{
    border-top: .35mm solid rgba(255,255,255,.18); padding-top: 6mm;
    font-size: 8.6pt; color: #aeb6be;
}}
.cover .head, .cover .mid, .cover .meta {{ position: relative; z-index: 2; }}
.cover .meta b {{ color: #ffffff; font-weight: 600; }}
.cover .meta .row {{ margin-bottom: 1.6mm; }}

/* ---------- Kopniveaus ---------- */
h1 {{
    font-size: 17pt; font-weight: 800; color: {BLACK};
    margin: 0 0 6mm 0; padding-bottom: 2.5mm;
    border-bottom: .9mm solid {MAGENTA};
    string-set: chapter content();
    break-before: page;
}}
h1.first {{ break-before: avoid; }}
h2 {{
    font-size: 12.2pt; font-weight: 700; color: {BLACK};
    margin: 8mm 0 3mm 0; padding-left: 3.6mm;
    border-left: 1.1mm solid {CYAN};
    break-after: avoid;
}}
h3 {{
    font-size: 10.2pt; font-weight: 700; color: {INK_MAGENTA};
    margin: 6mm 0 2mm 0; break-after: avoid;
}}
p {{ margin: 0 0 3mm 0; orphans: 2; widows: 2; }}
strong {{ font-weight: 700; color: {BLACK}; }}
em {{ color: {MUTED}; }}
a {{ color: {INK_CYAN}; text-decoration: none; word-break: break-word; }}

ul, ol {{ margin: 0 0 3.5mm 0; padding-left: 5.5mm; }}
li {{ margin-bottom: 1.4mm; padding-left: 1mm; }}
li::marker {{ color: {MAGENTA}; font-weight: 700; }}

/* ---------- Tabellen ---------- */
table {{
    width: 100%; border-collapse: collapse; margin: 3mm 0 5mm 0;
    font-size: 8.1pt; line-height: 1.42;
}}
thead {{ display: table-header-group; }}
tr {{ break-inside: avoid; }}
th {{
    background: {BLACK}; color: #ffffff; font-weight: 600;
    text-align: left; padding: 2.1mm 2.4mm; font-size: 7.9pt;
    letter-spacing: .02em;
}}
th:first-child {{ border-left: 1mm solid {CYAN}; }}
/* strong is standaard bijna-zwart; op de zwarte kopregel zou dat
   onzichtbaar zijn. Zelfde voor code en links in een kopcel. */
th strong, th em, th code, th a {{ color: #ffffff; background: none; }}
td {{
    padding: 2.1mm 2.4mm; border-bottom: .2mm solid {RULE};
    vertical-align: top;
}}
tbody tr:nth-child(even) td {{ background: {WASH}; }}

/* ---------- Blokken ---------- */
blockquote {{
    margin: 4mm 0; padding: 3.5mm 4.5mm;
    background: {WASH}; border-left: 1.2mm solid {MAGENTA};
    break-inside: avoid;
}}
blockquote p {{ margin: 0; }}
code {{
    font-family: "DejaVu Sans Mono", monospace; font-size: 8pt;
    background: {WASH}; padding: .3mm 1mm; border-radius: .6mm;
    color: {INK_MAGENTA};
}}
pre {{
    background: {BLACK}; color: #e9edf1; padding: 4mm;
    font-size: 7.6pt; line-height: 1.5; overflow-wrap: break-word;
    white-space: pre-wrap; break-inside: avoid; margin: 3mm 0 5mm 0;
    border-left: 1.1mm solid {CYAN};
}}
pre code {{ background: none; color: inherit; padding: 0; }}
hr {{ border: none; border-top: .25mm solid {RULE}; margin: 7mm 0; }}

/* ---------- Betrouwbaarheidslabels ---------- */
.lbl {{
    font-size: 6.9pt; font-weight: 700; letter-spacing: .05em;
    padding: .35mm 1.5mm; border-radius: .8mm; white-space: nowrap;
}}
""" + "".join(
    f'.lbl-{k.lower()} {{ color: {fg}; background: {bg}; }}\n'
    for k, (fg, bg) in LABELS.items()
)


def build_cover(title, subtitle, meta_rows):
    rows = "".join(f'<div class="row">{r}</div>' for r in meta_rows)
    return f"""
<section class="cover">
  <div class="glow"></div><div class="grid"></div>
  <div class="head">
    <div class="wordmark">Gold <span class="lemon">Lemon</span></div>
    <div class="kicker">AI &amp; Digital Marketing</div>
  </div>
  <div class="mid">
    <h1>{title}</h1>
    <div class="accentbar"></div>
    <div class="sub">{subtitle}</div>
  </div>
  <div class="meta">{rows}</div>
</section>
"""


def transform(md_text):
    """Splitst de titel af en zet de labels om in gekleurde badges."""
    lines = md_text.split("\n")

    title = "Rapport"
    if lines and lines[0].startswith("# "):
        title = lines[0][2:].strip()
        lines = lines[1:]

    # Metaregels bovenaan (**Voor:** ... etc.) worden omslagregels.
    meta_rows, rest = [], []
    for i, line in enumerate(lines):
        s = line.strip()
        if s.startswith("**") and ":**" in s and len(meta_rows) < 6:
            row = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
            meta_rows.append(row)
        elif s == "---" and meta_rows:
            rest = lines[i + 1:]
            break
        elif s:
            rest = lines[i:]
            break
    body_md = "\n".join(rest)

    html = markdown.markdown(
        body_md, extensions=["tables", "fenced_code", "attr_list", "sane_lists"]
    )

    # [GEMETEN] -> gekleurde badge
    def badge(m):
        key = m.group(1)
        return f'<span class="lbl lbl-{key.lower()}">{key}</span>'

    html = re.sub(r"\[(" + "|".join(LABELS) + r")\]", badge, html)
    return title, meta_rows, html


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input")
    ap.add_argument("output")
    ap.add_argument("--ondertitel", default="")
    args = ap.parse_args()

    md_text = pathlib.Path(args.input).read_text(encoding="utf-8")
    title, meta_rows, body = transform(md_text)

    # Eerste h1 mag geen paginabreak forceren: die volgt al op de omslag.
    body = body.replace("<h1>", '<h1 class="first">', 1)

    doc = f"""<!doctype html><html lang="nl"><head><meta charset="utf-8">
<title>{title}</title><style>{CSS}</style></head><body>
{build_cover(title, args.ondertitel, meta_rows)}
{body}
</body></html>"""

    out = pathlib.Path(args.output)
    HTML(string=doc, base_url=str(pathlib.Path(args.input).parent)).write_pdf(out)
    print(f"{out}  ({out.stat().st_size / 1024:.0f} kB)")


if __name__ == "__main__":
    sys.exit(main())
