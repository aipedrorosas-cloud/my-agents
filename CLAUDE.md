# Rules for every scout in this repo

## Who I am
Pedro, an experience designer moving into applied AI, building my first autonomous agents for learning and personal branding.

## Research rules
- Official or reputable sources only: the person's or company's own site, universities, research groups, government, established publications.
- No Reddit, no forums.
- Flag vendor material as (vendor).
- Every find needs a working link. Important claims need 2 sources.
- Label what is verified vs my framing.

## Agent definition (use it as a filter)
An autonomous agent is an AI that you give a goal, not steps, and that decides how to reach it by using tools on your behalf, within limits you set.
Test: "Who decides the next step, the builder or the AI?" Builder = workflow or chatbot. AI = agent.
Flag agent washing: assistants, chatbots or automations rebranded as "agents".

## Style checklist (score each 1-5, total out of 25)
1. Easy: a designer gets it in 2 minutes
2. Visual: diagrams, cards, journeys, GIFs or video
3. Low text: not walls of text
4. Beautiful: crafted, pleasant to look at
5. Real: shows a real agent that decides its own steps

## Visual card (the main output of every run)
Draw ONE visual card as an image, ready to post:
- Format: SVG, 1080 x 1350 (portrait, LinkedIn-friendly). Also export a PNG with the same name.
- Look: soft colours only (background #F3F1EC; boxes #FBF3D9, #EDF1F8, #E6F2EA), rounded boxes, dark grey text, clean sans-serif. No icons, no emoji, no logos, no reproduced visuals.
- Layout: small header (scout name + date) · title (max 8 words) · one big idea in a highlight box · 3 boxes: What, Who, Why it matters · footer with sources, verified / my framing label, and "Pedro Rosas · @aiPedroRosas".
- Little text: each box max 2 short lines. Check nothing overflows.
- Also save a short .md with the same name holding the card's text and full source links (alt text).
- Use the latest card in `cards/` as the style reference.

## How every run works
1. Read `notebook.csv`. Never add a link that is already there.
2. Research using the rules above. Decide your own steps.
3. Add each new find as a row in `notebook.csv`.
4. Save the visual card in `cards/` as `YYYY-MM-DD-scout-name.svg` + `.png` + `.md`.
5. Add a short entry at the top of `runs.md`: date, scout, what you searched, what you kept, what you skipped and why.
6. Commit with the message `Weekly run by my <scout name>` and push to the main branch.

## Safety
- Never post, send, email or publish anything outside this repo. Only draft; Pedro decides.
- Public information only. Do not collect personal contact details.
- Inspiration, not copying: describe patterns, never reproduce someone's work or visuals.
- Never ask for approval: if a step is not allowed by these rules, skip it and note why in `runs.md`.
