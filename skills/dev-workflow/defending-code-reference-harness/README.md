# defending-code-reference-harness

Skills from [anthropics/defending-code-reference-harness](https://github.com/anthropics/defending-code-reference-harness) at commit [`d3bea6b`](https://github.com/anthropics/defending-code-reference-harness/tree/d3bea6b5793b5f3d59a75ebe69a58efa88383145), copied into SOYL Hub on 2026-11-05. Licence: Apache-2.0.

> Skills for threat modeling, scanning, triage, patching, plus an autonomous scanning harness you can /customize

All credit goes to the authors of anthropics/defending-code-reference-harness. Each folder is the upstream skill unchanged, with its licence file added when it had none; build caches and plugin manifests are left out.

| Skill | What it does | Licence |
|---|---|---|
| [customize](customize/) | Adapt this C/C++ ASAN vulnerability pipeline to a different vulnerability class, target shape, language, or detection mechanism. Use when the user wants to port… | Apache-2.0 |
| [dnr-hunt](dnr-hunt/) | Proactive threat hunt over web/application logs — no alert in hand. Profiles the corpus, runs a hypothesis-driven hunt loop with a mandatory written ledger, confirms… | Apache-2.0 |
| [dnr-respond](dnr-respond/) | Incident response workup for a lead in hand — an alert, an IOC, or a /dnr-hunt finding. Scopes the lead across the logs, verdicts whether the attack succeeded… | Apache-2.0 |
| [patch](patch/) | Generate candidate fixes for verified security findings. Consumes TRIAGE.json (preferred), VULN-FINDINGS.json, INCIDENTS.json, or a vuln-pipeline results directory… | Apache-2.0 |
| [quickstart](quickstart/) | The front door for this repo. With no argument: a 30-second intro, then an offer to walk you through your first run on the canary target. With a question: answers it… | Apache-2.0 |
| [threat-model](threat-model/) | Build a threat model for a target codebase. Three modes: "interview" walks an application owner through the four-question framework and produces a threat model from… | Apache-2.0 |
| [triage](triage/) | Triage a batch of raw security findings. Verify each is real, collapse duplicates, re-rank by derived exploitability, and tag with an owner. Takes a directory or file of… | Apache-2.0 |
| [verify](verify/) | Verify harness changes end-to-end without docker — drive the real pinned CLI against a header-capturing stub server with the exact env resolve_auth_env() produces. | Apache-2.0 |
| [vuln-scan](vuln-scan/) | Static source-code vulnerability scan. Reads a target directory (and THREAT_MODEL.md if present), spawns parallel review subagents per focus area, and writes… | Apache-2.0 |

Install one with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/SOYL-AI/soyl-skills-hub/tree/main/skills/dev-workflow/defending-code-reference-harness/customize -g -a claude-code
```

Back to [Developer workflow](../../../catalog/dev-workflow.md)
