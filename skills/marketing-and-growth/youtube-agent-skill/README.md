# youtube-agent-skill

Skills from [Jakeschincariol/youtube-agent-skill](https://github.com/Jakeschincariol/youtube-agent-skill) at commit [`a2feb21`](https://github.com/Jakeschincariol/youtube-agent-skill/tree/a2feb2104981a375ffd4f87ee04f4f5344ac43c6), copied into SOYL Hub on 2026-10-29. Licence: MIT.

> Eleven Claude skills that run a YouTube channel: scripts off 21 hook formulas with a scored hook, title and thumbnail linted as one pairing, an edit decision list from your transcript, a retention reader that finds where viewers actually leave, a Shorts cutter, and a virality engine. Free, MIT.

All credit goes to the authors of Jakeschincariol/youtube-agent-skill. Each folder is the upstream skill unchanged, with its licence file added when it had none; build caches and plugin manifests are left out.

| Skill | What it does | Licence |
|---|---|---|
| [yt-audit](yt-audit/) | Audit a YouTube channel end to end - packaging, consistency, the first fifteen seconds, and what to fix first. Use for "audit my channel", "why isn't my channel… | MIT |
| [yt-chapters](yt-chapters/) | Write YouTube chapters from a transcript, validated against YouTube's own rules so they actually render. Use for "add chapters", "timestamps", "break this video into… | MIT |
| [yt-comment](yt-comment/) | Draft replies to YouTube comments in the creator's voice, triaged by which ones are worth answering. Use for "reply to my comments", "handle the comment section"… | MIT |
| [yt-edit](yt-edit/) | Turn a raw recording's transcript into an edit decision list - dead air, filler cues and retakes, with timecodes. Use for "edit this", "cut the dead space", "tighten… | MIT |
| [yt-package](yt-package/) | Write and lint the title and thumbnail for a YouTube video as one pairing, checking truncation, duplication and vagueness before publish. Use for "title ideas", "what… | MIT |
| [yt-plan](yt-plan/) | Plan a week or a month of YouTube uploads - what to post, when, and in what order, sized to the creator's actual capacity. Use for "plan my week", "content calendar"… | MIT |
| [yt-retention](yt-retention/) | Read a YouTube Studio audience-retention export and find where viewers actually leave, then say what to change. Use for "why do people stop watching", "my retention is… | MIT |
| [yt-script](yt-script/) | Write a YouTube video script from a raw idea - hook options off 21 formulas, scored, then the full spoken script with the retention beats marked. Use whenever the user… | MIT |
| [yt-seo](yt-seo/) | Write the description, tags and search-facing text for a YouTube video, aimed at the query a real person types. Use for "write my description", "tags", "SEO", "help this… | MIT |
| [yt-shorts](yt-shorts/) | Find the Shorts hiding inside a long video and write them, using the transcript to pick self-contained moments. Use for "cut this into shorts", "clip this", "repurpose… | MIT |
| [yt-viral](yt-viral/) | Find what is actually working in the user's niche on YouTube and rank it by how far each video beat its own channel, then name the formula. Use for "what's working right… | MIT |

Install one with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/SOYL-AI/soyl-skills-hub/tree/main/skills/marketing-and-growth/youtube-agent-skill/yt-audit -g -a claude-code
```

Back to [Marketing and growth](../../../catalog/marketing-and-growth.md)
