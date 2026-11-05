# openai-agents-python

Skills from [openai/openai-agents-python](https://github.com/openai/openai-agents-python) at commit [`814de8b`](https://github.com/openai/openai-agents-python/tree/814de8b1cfdaf6c70212dca9ca23563dd0b789ac), copied into SOYL Hub on 2026-11-05. Licence: MIT.

> A lightweight, powerful framework for multi-agent workflows

All credit goes to the authors of openai/openai-agents-python. Each folder is the upstream skill unchanged, with its licence file added when it had none; build caches and plugin manifests are left out.

| Skill | What it does | Licence |
|---|---|---|
| [code-change-verification](code-change-verification/) | Run the required final formatting, lint, type, and test checks after eligible SDK changes pass review. | MIT |
| [credit-note-fixer](credit-note-fixer/) | Fix the tiny credit-note formatting bug and rerun the exact targeted test command. | MIT |
| [csv-workbench](csv-workbench/) | Analyze CSV files in /mnt/data and return concise numeric summaries. | MIT |
| [docs-sync](docs-sync/) | Audit or update English SDK documentation against the requested implementation scope. | MIT |
| [examples-run-analysis](examples-run-analysis/) | Analyze logs and source from a completed manual examples run. Never execute or control examples. | MIT |
| [final-release-review](final-release-review/) | Assess a Python SDK release candidate or release plan against the previous release and recommend ship or block. | MIT |
| [implementation-final-review](implementation-final-review/) | Review completed implementation changes before final verification. Use when repository policy requires independent review or the user explicitly requests it. | MIT |
| [implementation-kickoff](implementation-kickoff/) | Carry implementation through an isolated worktree and local handoff. Use only when this skill is explicitly invoked. | MIT |
| [implementation-strategy](implementation-strategy/) | Choose supported scope and compatibility boundaries for SDK behavior changes; revisit when feedback changes the design. | MIT |
| [maintainer-review](maintainer-review/) | Assess a GitHub issue or PR for demonstrated need, supported alternatives, correctness, and maintainer action. Desk review only. | MIT |
| [openai-knowledge](openai-knowledge/) | Retrieve authoritative OpenAI API and platform documentation when an integration or claim needs current external evidence. | MIT |
| [playwright](playwright/) | Use when the task requires capturing or automating a real browser from the terminal. | MIT |
| [pr-draft-summary](pr-draft-summary/) | Prepare the required local PR title, description, and branch suggestion after eligible implementation work is complete. | MIT |
| [prior-auth-packet-builder](prior-auth-packet-builder/) | Build a concise prior authorization packet from local case files and payer policy docs. | MIT |
| [release-candidate-prep](release-candidate-prep/) | Prepare a local Python SDK release candidate in a dedicated worktree. Use only when explicitly invoked with a version. | MIT |
| [runtime-behavior-probe](runtime-behavior-probe/) | Plan controlled runtime probes when explicitly invoked; execute only after the required probe approval. | MIT |
| [sensitive-logging-audit](sensitive-logging-audit/) | Audit or fix sensitive-data exposure in Python SDK diagnostics, exceptions, logging, and telemetry. | MIT |
| [test-coverage-improver](test-coverage-improver/) | Measure Python SDK coverage or address measured coverage gaps. Use for coverage audits and metric regressions, not routine test additions. | MIT |

Install one with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/SOYL-AI/soyl-skills-hub/tree/main/skills/ai-platforms/openai-agents-python/code-change-verification -g -a claude-code
```

Back to [AI platforms](../../../catalog/ai-platforms.md)
