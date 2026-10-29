# roast-room

Skills from [nateherkai/roast-room](https://github.com/nateherkai/roast-room) at commit [`e40f406`](https://github.com/nateherkai/roast-room/tree/e40f40652d5690c4d9f928c4794c673a99f2cd0e), copied into SOYL Hub on 2026-10-29. Licence: MIT.

> Seven AI advisors (Bezos, Paul Graham, Hormozi, Gary Vee, Dan Martell, Gino Wickman, Buffett) debate your business decision in Claude Code, live around a table.

All credit goes to the authors of nateherkai/roast-room. Each folder is the upstream skill unchanged, with its licence file added when it had none; build caches and plugin manifests are left out.

| Skill | What it does | Licence |
|---|---|---|
| [newroaster](newroaster/) | Use when someone wants to add a new advisor to the Roast Room, says "/newroaster", "add a roaster", "add a seat", "add [name] to the council", "build a seat for [name]"… | MIT |
| [roast-room](roast-room/) | Use when a founder wants a hard business decision debated by a council of world-class operators, says "roast room", "put this in the Roast Room", "founder council"… | MIT |

Install one with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/SOYL-AI/soyl-skills-hub/tree/main/skills/marketing-and-growth/roast-room/newroaster -g -a claude-code
```

Back to [Marketing and growth](../../../catalog/marketing-and-growth.md)
