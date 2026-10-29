# ponytail

Skills from [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) at commit [`09c434a`](https://github.com/DietrichGebert/ponytail/tree/09c434ab73ca43761c5d8b0c5d341926c2fba710), copied into SOYL Hub on 2026-10-29. Licence: MIT.

> Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.

All credit goes to the authors of DietrichGebert/ponytail. Each folder is the upstream skill unchanged, with its licence file added when it had none; build caches and plugin manifests are left out.

| Skill | What it does | Licence |
|---|---|---|
| [ponytail](ponytail/) | Lazy senior dev mode: the smallest change that fully solves the task, and a reply a busy human understands in one read. Use on any coding task (writing, fixing… | MIT |
| [ponytail-audit](ponytail-audit/) | Quality audit of a whole repo: bugs, security holes, what breaks under real load, risky code without tests, slow paths, and what to delete, merge or split. Ranked, each… | MIT |
| [ponytail-debt](ponytail-debt/) | List every `shortcut:` comment (and older `ponytail:` ones) as a debt ledger. One-shot report, changes nothing. Use for "ponytail debt", "what did ponytail defer", "list… | MIT |
| [ponytail-gain](ponytail-gain/) | Show ponytail's measured savings (code, cost, speed) from the benchmark. One-shot display. Use for /ponytail-gain, "what does ponytail save", "ponytail impact". | MIT |
| [ponytail-help](ponytail-help/) | Quick reference for ponytail levels, skills and commands. One-shot display. Use for /ponytail-help, "ponytail help", "how do I use ponytail". | MIT |
| [ponytail-review](ponytail-review/) | Quality review of a change: is the logic right, is it safe, does it hold under real load, is risky code tested, is it fast enough, and is every line needed. Reads the… | MIT |

Install one with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/SOYL-AI/soyl-skills-hub/tree/main/skills/dev-workflow/ponytail/ponytail -g -a claude-code
```

Back to [Developer workflow](../../../catalog/dev-workflow.md)
