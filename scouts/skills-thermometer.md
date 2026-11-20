# Skills Thermometer

**Runs:** monthly, on the last Friday of the month, 10:41am (Melbourne time). Parked from weekly on 20 Nov 2026 so Pedro can focus on agents in super.

**Replaces steps 1, 3 and 5 of `CLAUDE.md`:** this scout uses its own memory in `thermometer/` (not `notebook.csv`) and makes no Bluesky Top 10.

## Goal
Track which skills Melbourne employers ask for in UX, service, product, content, conversation and AI / agent design roles, so Pedro can see what the market wants and how it changes over time.

## It decides for itself
- Which sources and searches to use this run (start from `thermometer/watchlist.md`, try new ones too)
- Which ads count (see the taste test)
- How much AI each ad has: **core**, **mentions** or **none**
- How to group the employer's words into skills (`thermometer/skill-map.md`), and when a new skill deserves its own name
- What the card should highlight

## Tools
- Web search and reading public job pages
- `thermometer/` files: watchlist, skill map, ads, skills table, `tally.py`, `card.py`
- The rules in `CLAUDE.md`

## Limits (power level R0-R1: read + draft)
- Read and draft only. Never apply, never contact anyone, never sign in.
- Seek, LinkedIn and Indeed block robots: don't try to read them. Their ads count only if the same ad can be read on the employer's site or a readable copy (ZipRecruiter, Jobstralia, Lever, Greenhouse, Workable).
- Skills come from the **employer's own words** only. Never from AI-rewritten listings (designproject.io "enhancement notes", IxDF skill tags, any "AI summary").
- No personal details: no recruiter or hiring manager names, emails or phone numbers.

## Memory
- `thermometer/ads.csv`: every ad read, one row each. Never add a link that is already there. **Save the skills the first time**: ads vanish fast.
- `thermometer/skills.csv`: the running count. Rebuilt by `python3 thermometer/tally.py`. Never count by hand.

## Each run
1. Read `thermometer/watchlist.md`, `thermometer/skill-map.md` and `thermometer/ads.csv`.
2. Find new ads (aim for 8-15 a month; fewer is fine, the market is small). Read each ad in full.
3. Add one row per ad to `ads.csv`. Map its skills to the skill map; add a new skill to the map only when nothing fits, with the employer's wording as the example.
4. Run `python3 thermometer/tally.py` (all-time) and `python3 thermometer/tally.py --run YYYY-MM-DD` (this run).
5. Card: this run's Top 10 skills (or all-time Top 10 if the run found fewer than 5 ads; say so on the card) as a bar diagram plus one big idea about AI / agents. `python3 thermometer/card.py --run YYYY-MM-DD --idea "line one" "line two"` draws it (add `--all-time` for the all-time Top 10); check the PNG. Save as `cards/YYYY-MM-DD-skills-thermometer.svg` + `.png` + `.md`.
6. Update `thermometer/watchlist.md` if a source started or stopped working.
7. Add an entry at the top of `runs.md`: sources tried, ads kept, skipped and why, sites that couldn't be read.
8. Commit with the message `Monthly run by my Skills Thermometer` and push to main.
- No Bluesky Top 10 for this scout (job ads aren't on Bluesky). No rows in `notebook.csv` (that is for the build scouts).

## Taste test
Every ad must pass 1-4. Criterion 5 is a label, not a filter: ads with no AI still count, they are the baseline.
1. **Design role:** UX, service, product, content, conversation, research or AI experience design (not graphic, not engineering)
2. **Place:** Melbourne, or remote in Australia
3. **Fresh:** posted in the last 90 days, or still open today when no date is shown
4. **Real words:** the full ad was read, in the employer's own wording
5. **AI signal:** core / mentions / none
