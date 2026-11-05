# ghostsecurity-skills

Skills from [ghostsecurity/skills](https://github.com/ghostsecurity/skills) at commit [`25fdf06`](https://github.com/ghostsecurity/skills/tree/25fdf068760723b85b40e0224a3b8533e4aab31f), copied into SOYL Hub on 2026-11-05. Licence: Apache-2.0.

> Ghost Security's collection of AppSec skills for AI coding agents

All credit goes to the authors of ghostsecurity/skills. Each folder is the upstream skill unchanged, with its licence file added when it had none; build caches and plugin manifests are left out.

| Skill | What it does | Licence |
|---|---|---|
| [ghost-exo](ghost-exo/) | The single interface for building, improving, and debugging exo workflows. Routes to one of three intents. BUILD takes a rough idea, or an agent template slug from the… | Apache-2.0 |
| [ghost-proxy](ghost-proxy/) | Starts and controls the reaper MITM proxy to capture, inspect, search, and replay HTTP/HTTPS traffic between clients and servers. Capabilities include starting/stopping… | Apache-2.0 |
| [ghost-repo-context](ghost-repo-context/) | Scans directory structure, detects projects, maps dependencies, and documents code organization into a repo.md file. Use when the user needs a codebase overview, project… | Apache-2.0 |
| [ghost-report](ghost-report/) | Ghost Security — combined security report. Aggregates findings from all scan skills (scan-deps, scan-secrets, scan-code) into a single prioritized report focused on the… | Apache-2.0 |
| [ghost-scan-code](ghost-scan-code/) | Ghost Security - SAST code scanner. Finds security vulnerabilities in source code by planning and executing targeted scans for issues like SQL injection, XSS, BOLA… | Apache-2.0 |
| [ghost-scan-deps](ghost-scan-deps/) | Ghost Security - Software Composition Analysis (SCA) scanner. Scans dependency lockfiles for known vulnerabilities, identifies CVEs, and generates findings with severity… | Apache-2.0 |
| [ghost-scan-secrets](ghost-scan-secrets/) | Ghost Security - Secrets and credentials scanner. Scans codebase for leaked API keys, tokens, passwords, and sensitive data. Detects hardcoded secrets and generates… | Apache-2.0 |
| [ghost-validate](ghost-validate/) | This skill should be used when the user asks to "validate a finding", "check if a vulnerability is real", "triage a security finding", "confirm a vulnerability"… | Apache-2.0 |

Install one with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/SOYL-AI/soyl-skills-hub/tree/main/skills/dev-workflow/ghostsecurity-skills/ghost-exo -g -a claude-code
```

Back to [Developer workflow](../../../catalog/dev-workflow.md)
