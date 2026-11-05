# Understand-Anything

Skills from [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) at commit [`4e6d329`](https://github.com/Egonex-AI/Understand-Anything/tree/4e6d3299017a7432da15957874992837a315c5b4), copied into SOYL Hub on 2026-11-05. Licence: MIT.

> Graphs that teach > graphs that impress. Turn any code into an interactive knowledge graph you can explore, search, and ask questions about. Works with Claude Code, Codex, Cursor, Copilot, Gemini CLI, and more.

All credit goes to the authors of Egonex-AI/Understand-Anything. Each folder is the upstream skill unchanged, with its licence file added when it had none; build caches and plugin manifests are left out.

| Skill | What it does | Licence |
|---|---|---|
| [understand](understand/) | Analyze a codebase to produce an interactive knowledge graph for understanding architecture, components, and relationships | MIT |
| [understand-chat](understand-chat/) | Use when you need to ask questions about a codebase or understand code using a knowledge graph | MIT |
| [understand-dashboard](understand-dashboard/) | Launch the interactive web dashboard to visualize a codebase's knowledge graph | MIT |
| [understand-diff](understand-diff/) | Use when you need to analyze git diffs or pull requests to understand what changed, affected components, and risks | MIT |
| [understand-domain](understand-domain/) | Extract business domain knowledge from a codebase and generate an interactive domain flow graph. Works standalone (lightweight scan) or derives from an existing… | MIT |
| [understand-explain](understand-explain/) | Use when you need a deep-dive explanation of a specific file, function, or module in the codebase | MIT |
| [understand-figma](understand-figma/) | Analyze a Figma file via the Figma REST API and generate an interactive design knowledge graph (pages, screens, components, component sets, instances, design tokens)… | MIT |
| [understand-knowledge](understand-knowledge/) | Analyze a Karpathy-pattern LLM wiki knowledge base and generate an interactive knowledge graph with entity extraction, implicit relationships, and topic clustering. | MIT |
| [understand-onboard](understand-onboard/) | Use when you need to generate an onboarding guide for new team members joining a project | MIT |

Install one with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/SOYL-AI/soyl-skills-hub/tree/main/skills/dev-workflow/Understand-Anything/understand -g -a claude-code
```

Back to [Developer workflow](../../../catalog/dev-workflow.md)
