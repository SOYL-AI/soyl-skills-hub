# claude-mem

Skills from [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) at commit [`75fc021`](https://github.com/thedotmack/claude-mem/tree/75fc021a40655cbdd258f0e070f55a03ea9c8642), copied into SOYL Hub on 2026-10-29. Licence: Apache-2.0.

> Persistent Context Across Sessions for Every Agent – Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More

All credit goes to the authors of thedotmack/claude-mem. Each folder is the upstream skill unchanged, with its licence file added when it had none; build caches and plugin manifests are left out.

| Skill | What it does | Licence |
|---|---|---|
| [Agent Cost Report](agent-cost-report/) | Believable agent cost report for any period, default the last 7 full days PT, not counting today. Measured tokens from Claude Code transcripts priced at OpenRouter list… | Apache-2.0 |
| [babysit](babysit/) | Watch a pull request or review cycle until it is ready to merge. Use when asked to babysit, monitor, or keep checking PR comments, reviews, and CI until all actionable… | Apache-2.0 |
| [build-and-release](build-and-release/) | Fully automate building and releasing a coding task. | Apache-2.0 |
| [ccs-align](ccs-align/) | Run the CCS Align seat's hourly breathing cycle — prove the local claude-mem worker is healthy, pull needle observations through search → timeline → get_observations… | Apache-2.0 |
| [childhood](childhood/) | Babysit a shipped release after merge, publication, or deployment. Verify published packages, production behavior, installed plugins, and late CI or user reports until… | Apache-2.0 |
| [claude-mem-install](claude-mem-install/) | Use this when setting up claude-mem on Cursor: local or remote worker, local host-login observer or remote cmem.ai inference. | Apache-2.0 |
| [cloud-sync](cloud-sync/) | Set up or check claude-mem cloud sync with cmem.ai Pro. Use when the user says "set up cloud sync", "sync my memories", "cmem pro", "cloud backup", "sync status", or… | Apache-2.0 |
| [design-is](design-is/) | Audit a design against Dieter Rams' ten "Good design is..." principles, then hand off a /make-plan prompt for one of three outcomes — new design, refine design, or… | Apache-2.0 |
| [handoff](handoff/) | Generate a HANDOFF.md that captures goal, current state, files touched, failed attempts, and next steps — so a fresh Claude session can continue exactly where this one… | Apache-2.0 |
| [host-observer](host-observer/) | Use this when fulfilling claude-mem observer jobs on Grok Bot: reply only skip_summary or one full observation XML, never prose. | Apache-2.0 |
| [how-it-works](how-it-works/) | Explain how claude-mem captures observations, when memory injection kicks in, and where data lives. Use when the user asks "how does claude-mem work?" or "what is this… | Apache-2.0 |
| [knowledge-agent](knowledge-agent/) | Build and query AI-powered knowledge bases from claude-mem observations. Use when users want to create focused "brains" from their observation history, ask questions… | Apache-2.0 |
| [learn-codebase](learn-codebase/) | Prime a codebase by reading every source file in full. Use when starting work on a new or unfamiliar project, or when the user asks to "learn the codebase", "read the… | Apache-2.0 |
| [mem-search](mem-search/) | Use this when the user asks to search memory, "did we already solve this?", "how did we do X last time?", or wants work from previous sessions. | Apache-2.0 |
| [mem-setup](mem-setup/) | This skill should be used when the user asks to "set up claude-mem", "pair claude-mem", "connect cmem", "add my cmem key", "set up cloud sync in Cowork", or provides… | Apache-2.0 |
| [mode-creator](mode-creator/) | Interactively create, install, activate, and verify custom claude-mem modes, including domain-specific observation types, concept tags, optional Telegram alerts, bot… | Apache-2.0 |
| [oh-my-issues](oh-my-issues/) | Cluster a GitHub issue backlog by root cause into a small set of plan-master issues, redirect children with a standardized comment, and bundle architectural-fix PRs that… | Apache-2.0 |
| [openclaw](openclaw/) | — | Apache-2.0 |
| [owner-goals](owner-goals/) | Map what the owner wants from the prompts they typed themselves (prompts an agent wrote are left out), then put their top priorities and open asks, each with dated… | Apache-2.0 |
| [pathfinder](pathfinder/) | Map a codebase into feature-grouped flowcharts, identify duplicated concerns across features, and propose a unified architecture. Use when asked to "find the ideal… | Apache-2.0 |
| [release](release/) | Fully automate a release with version-bump and childhood. | Apache-2.0 |
| [request-progress](request-progress/) | Group recent conversations into overall requests, review each one's progress from memory, link each to the owner goals it serves, and write the build story, so My Work… | Apache-2.0 |
| [screenpipe](screenpipe/) | Search screen and audio history recorded by Screenpipe and optionally save selected context into claude-mem. Use when the user asks to recall desktop activity, a… | Apache-2.0 |
| [smart-explore](smart-explore/) | Token-optimized structural code search using tree-sitter AST parsing. Use instead of reading full files when you need to understand code structure, find functions, or… | Apache-2.0 |
| [standup](standup/) | Facilitate a read-only standup across git worktrees, branches, or PRs to compare changes and produce one consolidation plan. | Apache-2.0 |
| [timeline-report](timeline-report/) | Generate a "Journey Into [Project]" narrative report analyzing a project's entire development history from claude-mem's timeline. Use when asked for a timeline report… | Apache-2.0 |
| [version-bump](version-bump/) | Automated semantic versioning and release workflow for Claude Code plugins. Handles version increments across package.json, marketplace.json, plugin.json manifests… | Apache-2.0 |
| [weekly-digests](weekly-digests/) | Generate a serial week-by-week narrative digest of a project's full claude-mem timeline. Splits the timeline into per-ISO-week files, then runs one consecutive subagent… | Apache-2.0 |
| [what-the](what-the/) | What the? Use when the user wants a plain-English breakdown of something technical — the who, what, where, why, and when. | Apache-2.0 |
| [wowerpoint](wowerpoint/) | Turn one document into a kawaii NotebookLM slide deck. Use for "wowerpoint this", "make a deck about &lt;file>", "turn this report into slides", or any request to render… | Apache-2.0 |

Install one with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/SOYL-AI/soyl-skills-hub/tree/main/skills/dev-workflow/claude-mem/agent-cost-report -g -a claude-code
```

Back to [Developer workflow](../../../catalog/dev-workflow.md)
