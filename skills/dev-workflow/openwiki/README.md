# openwiki

Skills from [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) at commit [`305599f`](https://github.com/langchain-ai/openwiki/tree/305599f8e44203f9ca6b74bb6b38eebaf0b0405e), copied into SOYL Hub on 2026-10-29. Licence: MIT.

> OpenWiki is a CLI that writes and maintains agent documentation for your codebase.

All credit goes to the authors of langchain-ai/openwiki. Each folder is the upstream skill unchanged, with its licence file added when it had none; build caches and plugin manifests are left out.

| Skill | What it does | Licence |
|---|---|---|
| [mermaid-diagrams](mermaid-diagrams/) | Embed Mermaid diagrams in generated wiki pages. Use whenever documenting a runtime or request flow, a call sequence, a state machine or lifecycle, a data model or entity… | MIT |
| [openwiki](openwiki/) | Search and read an existing repository OpenWiki when requested or needed to resolve a concrete architecture or dependency uncertainty, or initialize and update one… | MIT |
| [write-connector](write-connector/) | Add a new built-in OpenWiki source connector. Use when a user asks to create or implement an OpenWiki connector. | MIT |

Install one with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/SOYL-AI/soyl-skills-hub/tree/main/skills/dev-workflow/openwiki/mermaid-diagrams -g -a claude-code
```

Back to [Developer workflow](../../../catalog/dev-workflow.md)
