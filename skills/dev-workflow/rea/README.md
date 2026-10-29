# rea

Skills from [morluto/rea](https://github.com/morluto/rea) at commit [`f196ebf`](https://github.com/morluto/rea/tree/f196ebf80665107aedc16892af25a1e1f9f26f43), copied into SOYL Hub on 2026-10-29. Licence: MIT.

> Reverse engineer anything with agents, from app behavior down to native binaries.

All credit goes to the authors of morluto/rea. Each folder is the upstream skill unchanged, with its licence file added when it had none; build caches and plugin manifests are left out.

| Skill | What it does | Licence |
|---|---|---|
| [rea-analysis-optimization](rea-analysis-optimization/) | Optimize REA providers and shared analysis workflows for agent context, latency, CPU, and memory while preserving correctness and Evidence. Use for analysis bottlenecks… | MIT |
| [rea-changelog-update](rea-changelog-update/) | Prepare or rewrite REA release changelogs and GitHub release notes from pinned Git history, with verified contributor thanks and Release Please synchronization. | MIT |
| [rea-ci-tests-audit](rea-ci-tests-audit/) | Audit REA CI and test suites for correctness, fixture drift, false passes, and measured performance; use for suite or workflow investigations and efficiency changes… | MIT |
| [rea-tool-design](rea-tool-design/) | Design or change REA investigation tools, CLI/MCP contracts, provider capabilities, and Evidence semantics. | MIT |
| [reverse-engineer-anything](reverse-engineer-anything/) | Reverse engineer native, managed, Electron/JavaScript, packaged, firmware, and browser targets with REA, and build agent environments (AgentEnv bundles) of web… | MIT |

Install one with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/SOYL-AI/soyl-skills-hub/tree/main/skills/dev-workflow/rea/rea-analysis-optimization -g -a claude-code
```

Back to [Developer workflow](../../../catalog/dev-workflow.md)
