"""Count skills in ads.csv and write skills.csv.

Usage:
  python3 thermometer/tally.py                  # all ads, writes thermometer/skills.csv
  python3 thermometer/tally.py --run 2026-11-18 # one run only, prints its Top 10 (no file written)
"""
import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).parent
AI_SKILLS = {
    "AI tools in design work",
    "Designing AI products",
    "Conversational interfaces",
    "Agentic workflows & agents",
}


def load_ads(run=None):
    with open(HERE / "ads.csv", newline="", encoding="utf-8") as f:
        ads = list(csv.DictReader(f))
    if run:
        ads = [a for a in ads if a["date_found"] == run]
    return ads


def tally(ads):
    counts, core_counts = Counter(), Counter()
    first, last = {}, defaultdict(str)
    for ad in ads:
        skills = {s.strip() for s in ad["skills"].split(";") if s.strip()}
        for s in skills:
            counts[s] += 1
            if ad["ai_level"] == "core":
                core_counts[s] += 1
            d = ad["date_found"]
            first[s] = min(first.get(s, d), d)
            last[s] = max(last[s], d)
    # Most ads first; ties broken by AI-core ads, then name
    order = sorted(counts, key=lambda s: (-counts[s], -core_counts[s], s))
    return order, counts, core_counts, first, last


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--run", help="only ads with this date_found (YYYY-MM-DD)")
    args = p.parse_args()

    ads = load_ads(args.run)
    if not ads:
        raise SystemExit("No ads found for that run.")
    order, counts, core, first, last = tally(ads)
    n = len(ads)
    levels = Counter(a["ai_level"] for a in ads)

    print(f"Ads: {n} | AI core: {levels['core']} | mentions: {levels['mentions']} | none: {levels['none']}")
    print("Top 10:")
    for i, s in enumerate(order[:10], 1):
        print(f"{i:>2}. {s}: {counts[s]}/{n} ({round(100 * counts[s] / n)}%)")
    print("AI skills:")
    for s in sorted(AI_SKILLS, key=lambda s: -counts[s]):
        print(f"   {s}: {counts[s]}/{n}")

    if not args.run:
        with open(HERE / "skills.csv", "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["skill", "ads", "share_of_ads", "ads_with_ai_core", "is_ai_skill", "first_seen", "last_seen"])
            for s in order:
                w.writerow([s, counts[s], f"{round(100 * counts[s] / n)}%", core[s],
                            "Y" if s in AI_SKILLS else "N", first[s], last[s]])
        print(f"Wrote skills.csv ({len(order)} skills from {n} ads)")


if __name__ == "__main__":
    main()
