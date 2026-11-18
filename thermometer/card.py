"""Draw the Skills Thermometer card (SVG 1080x1350 + PNG) from ads.csv.

Usage:
  python3 thermometer/card.py --run 2026-11-18 --idea "AI is in 6 of 10 ads." "Agents: only 2." [--name ...] [--all-time]
Needs rsvg-convert for the PNG.
"""
import argparse
import subprocess
from datetime import date
from html import escape
from pathlib import Path

from tally import AI_SKILLS, load_ads, tally

ROOT = Path(__file__).parent.parent
FONT = "Inter, -apple-system, 'Helvetica Neue', Helvetica, Arial, sans-serif"


def build(run, idea, name, all_time=False):
    ads = load_ads(None if all_time else run)
    order, counts, _, _, _ = tally(ads)
    n = len(ads)
    employers = len({a["company"] for a in ads})
    top = order[:10]
    d = date.fromisoformat(run)
    header = f"SKILLS THERMOMETER · {d.day} {d.strftime('%b').upper()} {d.year}"

    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1350" viewBox="0 0 1080 1350" font-family="{FONT}">',
         '<rect width="1080" height="1350" fill="#F3F1EC"/>',
         f'<text x="80" y="110" font-size="26" fill="#6B6B6B" letter-spacing="2">{header}</text>',
         '<text x="80" y="200" font-size="68" font-weight="700" fill="#2B2B2B">What Melbourne asks</text>',
         '<text x="80" y="278" font-size="68" font-weight="700" fill="#2B2B2B">designers for</text>',
         f'<text x="80" y="330" font-size="26" fill="#6B6B6B">Top 10 skills in {n} design job ads{" (all runs so far)" if all_time else ""}</text>',
         '<rect x="80" y="365" width="920" height="625" rx="32" fill="#FFFFFF" opacity="0.6"/>']

    bar_x, bar_max, row_h, y0 = 500, 400, 54, 400
    for i, s in enumerate(top):
        y = y0 + i * row_h
        ai = s in AI_SKILLS
        w = max(24, round(bar_max * counts[s] / n))
        fill, stroke = ("#E6F2EA", "#A9CDB5") if ai else ("#EDF1F8", "#C9D3E3")
        label = s.replace(" & ", " &amp; ")
        o.append(f'<text x="480" y="{y + 25}" font-size="22" fill="#2B2B2B" text-anchor="end"'
                 f'{" font-weight=\"700\"" if ai else ""}>{label}</text>')
        o.append(f'<rect x="{bar_x}" y="{y}" width="{w}" height="36" rx="12" fill="{fill}" stroke="{stroke}" stroke-width="2"/>')
        o.append(f'<text x="{bar_x + w + 14}" y="{y + 26}" font-size="22" font-weight="700" fill="#3A3A3A">{counts[s]}</text>')

    # legend
    ly = y0 + 10 * row_h + 12
    o += [f'<rect x="500" y="{ly}" width="28" height="20" rx="6" fill="#E6F2EA" stroke="#A9CDB5" stroke-width="2"/>',
          f'<text x="538" y="{ly + 17}" font-size="20" fill="#6B6B6B">AI skill</text>',
          f'<rect x="660" y="{ly}" width="28" height="20" rx="6" fill="#EDF1F8" stroke="#C9D3E3" stroke-width="2"/>',
          f'<text x="698" y="{ly + 17}" font-size="20" fill="#6B6B6B">number of ads (of {n})</text>']

    o.append('<rect x="80" y="1010" width="920" height="150" rx="28" fill="#FBF3D9"/>')
    lines = idea[:2]
    ys = [1075, 1128] if len(lines) == 2 else [1100]
    for y, line in zip(ys, lines):
        o.append(f'<text x="540" y="{y}" font-size="38" fill="#2B2B2B" text-anchor="middle">{escape(line)}</text>')

    o += [f'<text x="80" y="1210" font-size="28" fill="#3A3A3A"><tspan font-weight="700">Read:</tspan> {n} public job ads, {employers} employers</text>',
          '<text x="80" y="1250" font-size="20" fill="#6B6B6B">Sources: each ad is linked in thermometer/ads.csv (github.com/aipedrorosas-cloud/my-agents)</text>',
          '<text x="80" y="1282" font-size="20" fill="#6B6B6B">Counts verified by script · skill grouping and big idea = my framing · a sample, not all ads</text>',
          '<text x="80" y="1318" font-size="20" font-weight="700" fill="#6B6B6B">Pedro Rosas · @aiPedroRosas</text>',
          '</svg>']

    svg = ROOT / "cards" / f"{name}.svg"
    svg.write_text("\n".join(o), encoding="utf-8")
    subprocess.run(["rsvg-convert", "-w", "1080", "-h", "1350", str(svg), "-o", str(svg.with_suffix(".png"))], check=True)
    print(f"Wrote {svg} and .png")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--run", required=True)
    p.add_argument("--idea", nargs="+", required=True, help="one or two short lines")
    p.add_argument("--name")
    p.add_argument("--all-time", action="store_true", help="count every ad so far (use when a run found fewer than 5)")
    a = p.parse_args()
    build(a.run, a.idea, a.name or f"{a.run}-skills-thermometer", a.all_time)
