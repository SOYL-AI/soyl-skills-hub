# vercel-skills-cli

Skills from [vercel-labs/skills](https://github.com/vercel-labs/skills) at commit [`13e4063`](https://github.com/vercel-labs/skills/tree/13e4063a1cf913f5606d57d42ab83a86f5001e04), copied into SOYL Hub on 2026-10-29. Licence: MIT.

> The open agent skills tool - npx skills

All credit goes to the authors of vercel-labs/skills. Each folder is the upstream skill unchanged, with its licence file added when it had none; build caches and plugin manifests are left out.

| Skill | What it does | Licence |
|---|---|---|
| [find-skills](find-skills/) | Helps users discover and install agent skills when they ask questions like "how do I do X", "find a skill for X", "is there a skill that can...", or express interest in… | MIT |
| [pr-labeling](pr-labeling/) | Classify a skills CLI pull request from its description and patch, while respecting existing labels. | MIT |
| [triage](triage/) | Identify focused, evidence-backed skills CLI bug fixes worth quuu's attention. | MIT |

Install one with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/SOYL-AI/soyl-skills-hub/tree/main/skills/dev-workflow/vercel-skills-cli/find-skills -g -a claude-code
```

Back to [Developer workflow](../../../catalog/dev-workflow.md)
