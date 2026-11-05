# cc-safety-net

Skills from [kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net) at commit [`0fb31bd`](https://github.com/kenryu42/cc-safety-net/tree/0fb31bdf3f5b6f308b51bb0a9807f572fb4f510e), copied into SOYL Hub on 2026-11-05. Licence: MIT.

> A pre-execution guard for AI coding agents. It blocks destructive Git and file system commands, plus common attempts to access sensitive files, before a tool call runs. Supports Amp Code, Antigravity CLI, Claude Code, Codex, Cursor, DeepSeek Harness, Devin CLI, GitHub Copilot CLI, Grok Build…

All credit goes to the authors of kenryu42/cc-safety-net. Each folder is the upstream skill unchanged, with its licence file added when it had none; build caches and plugin manifests are left out.

| Skill | What it does | Licence |
|---|---|---|
| [cc-safety-net](cc-safety-net/) | Operate CC Safety Net: explain why a command was blocked, triage false positives, configure custom rulebooks, manage agent CLI integrations, and diagnose protection. | MIT |
| [ccsn-find-simplifications](ccsn-find-simplifications/) | Use when working in the cc-safety-net repo to find non-obvious simplification candidates: dead, duplicated, speculative, over-built, or contract-exceeding surfaces in… | MIT |
| [ccsn-no-comments](ccsn-no-comments/) | Use in the cc-safety-net repo when `bun run lint:comments` or `bun run check` reports a comment, a stale comment-allowlist entry, or a file it cannot parse, and before… | MIT |
| [release-notes](release-notes/) | Generate and publish concise, evidence-based notes in the body of the latest existing GitHub Release. Use only when the user explicitly invokes `$release-notes` or… | MIT |
| [verify-ccsn](verify-ccsn/) | Launch and drive the real cc-safety-net CLI — the hook decision path, explain, status/doctor/statusline, logs, rule and policy config, and the local policy GUI — against… | MIT |
| [verify-project-tighten-only](verify-project-tighten-only/) | Use in the cc-safety-net repo before finishing any change to how a project policy merges with the user policy or how a merged policy turns into protections… | MIT |

Install one with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/SOYL-AI/soyl-skills-hub/tree/main/skills/dev-workflow/cc-safety-net/cc-safety-net -g -a claude-code
```

Back to [Developer workflow](../../../catalog/dev-workflow.md)
