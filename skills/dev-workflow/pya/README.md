# pya

Skills from [AgriciDaniel/pya](https://github.com/AgriciDaniel/pya) at commit [`416c17f`](https://github.com/AgriciDaniel/pya/tree/416c17fa09a234a1a34709d31b335d30196b9899), copied into SOYL Hub on 2026-11-05. Licence: MIT.

> PYA (Protect Your Ass): security audit plugin for Claude Code. 9 specialist agents, a dated threat feed, verified findings, offline by default.

All credit goes to the authors of AgriciDaniel/pya. Each folder is the upstream skill unchanged, with its licence file added when it had none; build caches and plugin manifests are left out.

| Skill | What it does | Licence |
|---|---|---|
| [pya](pya/) | Audits a codebase for security problems with parallel read-only specialist agents and a verifier pass. Covers code vulnerabilities, authorization, secrets, dependencies… | MIT |

Install one with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/SOYL-AI/soyl-skills-hub/tree/main/skills/dev-workflow/pya/pya -g -a claude-code
```

Back to [Developer workflow](../../../catalog/dev-workflow.md)
