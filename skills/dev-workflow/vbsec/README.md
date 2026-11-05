# vbsec

Skills from [tanviet12/vbsec](https://github.com/tanviet12/vbsec) at commit [`1b86c27`](https://github.com/tanviet12/vbsec/tree/1b86c27936d350d1a9ca67f044341262d4219d4e), copied into SOYL Hub on 2026-11-05. Licence: MIT.

> Security scanning skill for Claude Code, Codex and Antigravity. Finds the 21 most common vulnerabilities in AI-written code and shows how to fix each one.

All credit goes to the authors of tanviet12/vbsec. Each folder is the upstream skill unchanged, with its licence file added when it had none; build caches and plugin manifests are left out.

| Skill | What it does | Licence |
|---|---|---|
| [vbs-scan-security](vbs-scan-security/) | Use when scanning code for security vulnerabilities. Use when user says "scan security", "kiểm tra bảo mật", "security audit", "review security", or invokes… | MIT |

Install one with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/SOYL-AI/soyl-skills-hub/tree/main/skills/dev-workflow/vbsec/vbs-scan-security -g -a claude-code
```

Back to [Developer workflow](../../../catalog/dev-workflow.md)
