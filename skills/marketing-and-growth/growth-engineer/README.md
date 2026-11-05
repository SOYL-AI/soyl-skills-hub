# growth-engineer

Skills from [GetBrew/growth-engineer](https://github.com/GetBrew/growth-engineer) at commit [`d8a0e45`](https://github.com/GetBrew/growth-engineer/tree/d8a0e45417ebe2f047a7bbe2b44a176b5f31718d), copied into SOYL Hub on 2026-11-05. Licence: MIT.

> Open-source catalog of go-to-market tools and workflows, written as markdown files any agent can run. Includes a read-only MCP server.

All credit goes to the authors of GetBrew/growth-engineer. Each folder is the upstream skill unchanged, with its licence file added when it had none; build caches and plugin manifests are left out.

| Skill | What it does | Licence |
|---|---|---|
| [add-workflow](add-workflow/) | Write a growth.engineer workflow — workflows/&lt;name>.md, a growth play as up to ten steps across catalog tools, with the outcome the user gets, its one motion and the… | MIT |
| [research-company](research-company/) | Research a company from its domain and write its growth.engineer catalog files — companies/&lt;handle>/company.md (who they are and how an agent connects: MCP server… | MIT |

Install one with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/SOYL-AI/soyl-skills-hub/tree/main/skills/marketing-and-growth/growth-engineer/add-workflow -g -a claude-code
```

Back to [Marketing and growth](../../../catalog/marketing-and-growth.md)
