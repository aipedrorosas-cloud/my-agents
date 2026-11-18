# Learning log

Every change to my agents, and **why**. Newest at the top.
(GitHub keeps the exact before/after of every file; this is the human version.)

---

## 18 Nov 2026 · Day 1

| Change | Why | What I learned |
|---|---|---|
| Moved the notebook from the Claude project to GitHub | The agent must write it alone, and I want a history | An agent's memory should live where it can read **and** write |
| Rules live in `CLAUDE.md` in the repo | The scout reads them every run | I never update the agent by hand: I change its rules |
| Turned on "never ask for approval" (safe, R0–R1) | I won't remember to approve things | Zero friction comes from **narrow power**, not from trust |
| First run: kept 2, skipped 5 | Few designers document real autonomous agents | Thin results are a finding: evidence for my visual-first gap |
| Card changed from text to a **visual card** (SVG + PNG) | I wanted something ready to post, like my board cards | The output format is a design decision, not a detail |
| Added Bluesky (free) | Fresher, more visual posts | Tested it: reading feeds works, keyword search needs a login. **Test before promising** |
| Added a Bluesky Top 10 (likes + replies) | See what resonates | "Most liked" only means most liked **among what the agent found** |
| Parked X (paid API) | Keep it $0 | Every data source has a price and an access rule |
| Taste test: finds = useful; card = make it **more visual** | Text-heavy cards don't feel like me | Cards are now **diagram first, words second** |
| "Partly autonomous" builds now count, with a label | I was unsure; including them finds more designers | When unsure, include and **label** rather than exclude |
