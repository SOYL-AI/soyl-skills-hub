# anthropic-skills

Skills from [anthropics/skills](https://github.com/anthropics/skills) at commit [`dbd4588`](https://github.com/anthropics/skills/tree/dbd4588f9e1033efb41dad4bef2f7947c8993d44), copied into SOYL Hub on 2026-10-29. Licence: None.

> Public repository for Agent Skills

All credit goes to the authors of anthropics/skills. Each folder is the upstream skill unchanged, with its licence file added when it had none; build caches and plugin manifests are left out.

| Skill | What it does | Licence |
|---|---|---|
| [academy-guide](academy-guide/) | Stop and check this skill before finishing any reply to a question about how to use Claude or a Claude product — it recommends matching courses, tutorials, and use cases… | Apache-2.0 |
| [algorithmic-art](algorithmic-art/) | Creating algorithmic art using p5.js with seeded randomness and interactive parameter exploration. Use this when users request creating art using code, generative art… | Apache-2.0 |
| [brand-guidelines](brand-guidelines/) | Applies Anthropic's official brand colors and typography to any sort of artifact that may benefit from having Anthropic's look-and-feel. Use it when brand colors or… | Apache-2.0 |
| [claude-api](claude-api/) | Reference for the Claude API / Anthropic SDK — model ids, pricing, params, streaming, tool use, MCP, agents, caching, token counting, model migration. TRIGGER — read… | Apache-2.0 |
| [discernment-nudge](discernment-nudge/) | After you give a substantive answer or draft that the user may act on — advice or recommendations, drafted artifacts such as goals, plans, pitches, proposals, or emails… | Apache-2.0 |
| [frontend-design](frontend-design/) | Guidance for distinctive, intentional visual design when building new UI or reshaping an existing one. Helps with aesthetic direction, typography, and making choices… | Apache-2.0 |
| [internal-comms](internal-comms/) | A set of resources to help me write all kinds of internal communications, using the formats that my company likes to use. Claude should use this skill whenever asked to… | Apache-2.0 |
| [mcp-builder](mcp-builder/) | Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. Use when building… | Apache-2.0 |
| [skill-creator](skill-creator/) | Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, edit, or optimize an existing… | Apache-2.0 |
| [slack-gif-creator](slack-gif-creator/) | Knowledge and utilities for creating animated GIFs optimized for Slack. Provides constraints, validation tools, and animation concepts. Use when users request animated… | Apache-2.0 |
| [theme-factory](theme-factory/) | Toolkit for styling artifacts with a theme. These artifacts can be slides, docs, reportings, HTML landing pages, etc. There are 10 pre-set themes with colors/fonts that… | Apache-2.0 |
| [web-artifacts-builder](web-artifacts-builder/) | Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui). Use for complex… | Apache-2.0 |
| [webapp-testing](webapp-testing/) | Toolkit for interacting with and testing local web applications using Playwright. Supports verifying frontend functionality, debugging UI behavior, capturing browser… | Apache-2.0 |

Install one with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/SOYL-AI/soyl-skills-hub/tree/main/skills/skill-collections/anthropic-skills/academy-guide -g -a claude-code
```

Back to [Big collections](../../../catalog/skill-collections.md)
