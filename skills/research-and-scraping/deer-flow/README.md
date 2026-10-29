# deer-flow

Skills from [bytedance/deer-flow](https://github.com/bytedance/deer-flow) at commit [`e9074b7`](https://github.com/bytedance/deer-flow/tree/e9074b7126833b5ca4739bcedcbbed01b211246c), copied into SOYL Hub on 2026-10-29. Licence: MIT.

> An open-source long-horizon SuperAgent harness that researches, codes, and creates. With the help of sandboxes, memories, tools, skill, subagents and message gateway, it handles different levels of tasks that could take minutes to hours.

All credit goes to the authors of bytedance/deer-flow. Each folder is the upstream skill unchanged, with its licence file added when it had none; build caches and plugin manifests are left out.

| Skill | What it does | Licence |
|---|---|---|
| [academic-paper-review](academic-paper-review/) | Use this skill when the user requests to review, analyze, critique, or summarize academic papers, research articles, preprints, or scientific publications. Supports… | MIT |
| [blocking-io-guard](blocking-io-guard/) | Ensure async-path backend code that could block the asyncio event loop is protected by a teeth-verified runtime anchor in tests/blocking_io/. Use when changing backend… | MIT |
| [bootstrap](bootstrap/) | Generate a personalized SOUL.md through a warm, adaptive onboarding conversation. Trigger when the user wants to create, set up, or initialize their AI partner's… | MIT |
| [chart-visualization](chart-visualization/) | This skill should be used when the user wants to visualize data. It intelligently selects the most suitable chart type from 26 available options, extracts parameters… | MIT |
| [claude-to-deerflow](claude-to-deerflow/) | Interact with DeerFlow AI agent platform via its HTTP API. Use this skill when the user wants to send messages or questions to DeerFlow for research/analysis, start a… | MIT |
| [code-documentation](code-documentation/) | Use this skill when the user requests to generate, create, or improve documentation for code, APIs, libraries, repositories, or software projects. Supports README… | MIT |
| [consulting-analysis](consulting-analysis/) | Use this skill when the user requests to generate, create, or write professional research reports including but not limited to market analysis, consumer insights, brand… | MIT |
| [data-analysis](data-analysis/) | Use this skill when the user uploads Excel (.xlsx/.xls) or CSV files and wants to perform data analysis, generate statistics, create summaries, pivot tables, SQL… | MIT |
| [deep-research](deep-research/) | Use this skill instead of WebSearch for ANY question requiring web research. Trigger on queries like "what is X", "explain X", "compare X and Y", "research X", or before… | MIT |
| [deerflow-maintainer-orchestrator](deerflow-maintainer-orchestrator/) | Use when a DeerFlow maintainer needs comment-only GitHub issue or PR handling: resolve issue/PR scopes with gh, analyze issues, post or draft issue comments, perform PR… | MIT |
| [engineer-system-change](engineer-system-change/) | Evaluate and carry out non-trivial software-system changes from first principles. Use when assessing RFCs, issues, designs, features, refactors, migrations, dependency… | MIT |
| [find-skills](find-skills/) | Helps users discover and install agent skills when they ask questions like "how do I do X", "find a skill for X", "is there a skill that can...", or express interest in… | MIT |
| [frontend-design](frontend-design/) | Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, artifacts, posters… | Apache-2.0 |
| [github-deep-research](github-deep-research/) | Conduct multi-round deep research on any GitHub Repo. Use when users request comprehensive analysis, timeline reconstruction, competitive analysis, or in-depth… | MIT |
| [image-generation](image-generation/) | Use this skill when the user requests to generate, create, imagine, or visualize images including characters, scenes, products, or any visual content. Supports… | MIT |
| [music-generation](music-generation/) | Use this skill when the user requests to generate, create, compose, or produce music or songs — background music, theme songs, jingles, or instrumental tracks. Generates… | MIT |
| [newsletter-generation](newsletter-generation/) | Use this skill when the user requests to generate, create, write, or draft a newsletter, email digest, weekly roundup, industry briefing, or curated content summary… | MIT |
| [podcast-generation](podcast-generation/) | Use this skill when the user requests to generate, create, or produce podcasts from text content. Converts written content into a two-host conversational podcast audio… | MIT |
| [ppt-generation](ppt-generation/) | Use this skill when the user requests to generate, create, or make presentations (PPT/PPTX). Creates visually rich slides by generating images for each slide and… | MIT |
| [skill-creator](skill-creator/) | Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, edit, or optimize an existing… | Apache-2.0 |
| [skill-reviewer](skill-reviewer/) | Reviews DeerFlow skill packages for readiness, triggers, safety boundaries, resources, and evidence. Invoke when users ask to audit, grade, or production-check an… | MIT |
| [smoke-test](smoke-test/) | End-to-end smoke test skill for DeerFlow. Guides through: 1) Pulling latest code, 2) Docker OR Local installation and deployment (user preference, default to Local if… | MIT |
| [surprise-me](surprise-me/) | Create a delightful, unexpected "wow" experience for the user by dynamically discovering and creatively combining other enabled skills. Triggers when the user says… | MIT |
| [systematic-literature-review](systematic-literature-review/) | Use this skill when the user wants a systematic literature review, survey, or synthesis across multiple academic papers on a topic. Also covers annotated bibliographies… | MIT |
| [vercel-deploy](vercel-deploy/) | Deploy applications and websites to Vercel. Use this skill when the user requests deployment actions such as "Deploy my app", "Deploy this to production", "Create a… | MIT |
| [video-generation](video-generation/) | Use this skill when the user requests to generate, create, or imagine videos. Supports structured prompts and reference image for guided generation. | MIT |
| [web-design-guidelines](web-design-guidelines/) | Review UI code for Web Interface Guidelines compliance. Use when asked to "review my UI", "check accessibility", "audit design", "review UX", or "check my site against… | MIT |

Install one with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/SOYL-AI/soyl-skills-hub/tree/main/skills/research-and-scraping/deer-flow/academic-paper-review -g -a claude-code
```

Back to [Research and scraping](../../../catalog/research-and-scraping.md)
