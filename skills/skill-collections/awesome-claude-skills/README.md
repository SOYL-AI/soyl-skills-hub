# awesome-claude-skills

Skills from [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) at commit [`be2a406`](https://github.com/ComposioHQ/awesome-claude-skills/tree/be2a406907dbc61b73e6827ded415c96139d13a2), copied into SOYL Hub on 2026-10-29. Licence: None.

> A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows

All credit goes to the authors of ComposioHQ/awesome-claude-skills. Each folder is the upstream skill unchanged, with its licence file added when it had none; build caches and plugin manifests are left out.

| Skill | What it does | Licence |
|---|---|---|
| [artifacts-builder](artifacts-builder/) | Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui). Use for complex… | Apache-2.0 |
| [mcp-builder](mcp-builder/) | Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. Use when building… | Apache-2.0 |
| [skill-creator](skill-creator/) | Guide for creating effective skills. This skill should be used when users want to create a new skill (or update an existing skill) that extends Claude's capabilities… | Apache-2.0 |
| [slack-gif-creator](slack-gif-creator/) | Toolkit for creating animated GIFs optimized for Slack, with validators for size constraints and composable animation primitives. This skill applies when users request… | Apache-2.0 |

Install one with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/SOYL-AI/soyl-skills-hub/tree/main/skills/skill-collections/awesome-claude-skills/artifacts-builder -g -a claude-code
```

Back to [Big collections](../../../catalog/skill-collections.md)
