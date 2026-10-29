# instagram-agent-skill

Skills from [Jakeschincariol/instagram-agent-skill](https://github.com/Jakeschincariol/instagram-agent-skill) at commit [`d03c56b`](https://github.com/Jakeschincariol/instagram-agent-skill/tree/d03c56bb598be770c60b201f94237e5d1a4268a6), copied into SOYL Hub on 2026-10-29. Licence: MIT.

> Thirteen Claude skills that run an Instagram account: Reels off 26 scored hook formulas, a viral research skill, a caption linter, and a humanizer. Free, MIT.

All credit goes to the authors of Jakeschincariol/instagram-agent-skill. Each folder is the upstream skill unchanged, with its licence file added when it had none; build caches and plugin manifests are left out.

| Skill | What it does | Licence |
|---|---|---|
| [ig-audit](ig-audit/) | Post-mortem on what the user has already posted - which reels actually worked, why, and what to stop making. Use when the user pastes their Instagram insights or past… | MIT |
| [ig-caption](ig-caption/) | Write the Instagram caption - the line that survives the "... more" cut, the body, the single ask, the search terms and the three hashtags - and lint it before it goes… | MIT |
| [ig-carousel](ig-carousel/) | Build an Instagram carousel - the cover that earns the swipe, slide-by-slide copy, and the 1080x1350 files to upload. Use when the user says "carousel", "slides", "swipe… | MIT |
| [ig-comment](ig-comment/) | Write comments on other people's Instagram posts and reels that read as a person with an opinion, not a bot. Use when the user pastes a post or a reel and wants a… | MIT |
| [ig-dm](ig-dm/) | Write Instagram DMs that get replies - the keyword delivery, the first message to someone who engaged, the collab pitch, and the two follow-ups. Use when the user says… | MIT |
| [ig-plan](ig-plan/) | Build the week on Instagram - what to post, which format, when, and who to engage with. Use when the user says "plan my week", "what should I post", "content calendar"… | MIT |
| [ig-profile](ig-profile/) | Score an Instagram profile out of 100 against a 12-part rubric and rewrite the parts that lose points - name field, bio, link, highlights, pinned three, grid. Use when… | MIT |
| [ig-reel](ig-reel/) | Write an Instagram Reel from a raw idea - hook options off 26 formulas, the spoken script, the on-screen text, and a timed beat sheet - in the user's own voice and… | MIT |
| [ig-reply](ig-reply/) | Handle the comments under the user's own reels and posts - draft replies to the ones worth answering, sorted by which ones are. Use when the user pastes their comments… | MIT |
| [ig-repurpose](ig-repurpose/) | Turn one long asset - a YouTube video, podcast, livestream, newsletter, blog post or client call - into a week of reels and carousels. Use when the user says "repurpose… | MIT |
| [ig-story](ig-story/) | Write the day's Instagram Stories - the frame-by-frame sequence, which stickers to use where, and the one that moves people into the DMs. Use when the user says… | MIT |
| [ig-viral](ig-viral/) | Go and find the reels that are actually working right now in the user's niche, rank them by how far each beat its own account, name the hook formula each one used, and… | MIT |

Install one with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/SOYL-AI/soyl-skills-hub/tree/main/skills/marketing-and-growth/instagram-agent-skill/ig-audit -g -a claude-code
```

Back to [Marketing and growth](../../../catalog/marketing-and-growth.md)
