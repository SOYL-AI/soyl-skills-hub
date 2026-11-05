# agentguard

Skills from [GoPlusSecurity/agentguard](https://github.com/GoPlusSecurity/agentguard) at commit [`337b767`](https://github.com/GoPlusSecurity/agentguard/tree/337b767ea42eab3c51df7e6a777e9432d8effd94), copied into SOYL Hub on 2026-11-05. Licence: MIT.

> Security guard for AI agents — blocks malicious skills, prevents data leaks, protects secrets. 24 detection rules, runtime action evaluation, trust registry.

All credit goes to the authors of GoPlusSecurity/agentguard. Each folder is the upstream skill unchanged, with its licence file added when it had none; build caches and plugin manifests are left out.

| Skill | What it does | Licence |
|---|---|---|
| [agentguard](agentguard/) | GoPlus AgentGuard — AI agent security guard. Run /agentguard checkup for a full security health check, scans all installed skills, checks credentials, permissions, and… | MIT |

Install one with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/SOYL-AI/soyl-skills-hub/tree/main/skills/dev-workflow/agentguard/agentguard -g -a claude-code
```

Back to [Developer workflow](../../../catalog/dev-workflow.md)
