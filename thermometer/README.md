# Thermometer

The **Skills Thermometer**'s memory: what Melbourne employers ask designers for, ad by ad.

- `watchlist.md`: where to look (tested 18 Nov 2026), and where not to
- `skill-map.md`: the skill names the scout uses, so counts stay comparable run to run
- `ads.csv`: every job ad read, with its skills (saved the first time, because ads vanish)
- `skills.csv`: the running count, made by `tally.py`
- `tally.py`: counts skills (`--run YYYY-MM-DD` for one run only)
- `card.py`: draws the Top 10 skills card from the count

It is a **signal, not a census**: it can't read Seek or LinkedIn, so it sees a sample of the market.
