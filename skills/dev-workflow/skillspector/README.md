# skillspector

Skills from [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) at commit [`d7338f5`](https://github.com/NVIDIA/SkillSpector/tree/d7338f58200a9ae2a24810cee08911ab68b107a7), copied into SOYL Hub on 2026-10-29. Licence: Apache-2.0.

> Security scanner for AI agent skills. Detect vulnerabilities, malicious patterns, security risks, prompt injection, data exfiltration, and supply-chain risks in Claude Code, Codex, and MCP skills before you install them.

All credit goes to the authors of NVIDIA/SkillSpector. Each folder is the upstream skill unchanged, with its licence file added when it had none; build caches and plugin manifests are left out.

| Skill | What it does | Licence |
|---|---|---|
| [skill-inspector](skill-inspector/) | Review AI agent skills before installation using NVIDIA SkillSpector and source-aware semantic review. Use when asked whether a skill or downloaded skill folder is safe… | Apache-2.0 |

Install one with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/SOYL-AI/soyl-skills-hub/tree/main/skills/dev-workflow/skillspector/skill-inspector -g -a claude-code
```

Back to [Developer workflow](../../../catalog/dev-workflow.md)
