# gstack

Skills from [garrytan/gstack](https://github.com/garrytan/gstack) at commit [`e23f7b8`](https://github.com/garrytan/gstack/tree/e23f7b807ff4788f6d7c90af2ab82960bd8c5851), copied into SOYL Hub on 2026-10-29. Licence: MIT.

> Use Garry Tan's exact Claude Code setup: 23 opinionated tools that serve as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, and QA

All credit goes to the authors of garrytan/gstack. Each folder is the upstream skill unchanged, with its licence file added when it had none; build caches and plugin manifests are left out.

| Skill | What it does | Licence |
|---|---|---|
| [autoplan](autoplan/) | Auto-review pipeline — reads the full CEO, design, eng, and DX review skills from disk and runs them sequentially with auto-decisions using 6 decision principles… | MIT |
| [benchmark](benchmark/) | Web performance regression detection. (gstack) | MIT |
| [benchmark-models](benchmark-models/) | Cross-model benchmark for gstack skills. (gstack) | MIT |
| [browse](browse/) | Drive a real browser through Aside: open a page, read it, click through a flow, take screenshots, check console errors. (gstack) | MIT |
| [canary](canary/) | Post-deploy canary monitoring. (gstack) | MIT |
| [careful](careful/) | Safety guardrails for destructive commands. (gstack) | MIT |
| [codex](codex/) | OpenAI Codex CLI wrapper — three modes. (gstack) | MIT |
| [context-restore](context-restore/) | Restore working context saved earlier by /context-save. (gstack) | MIT |
| [context-save](context-save/) | Save working context. (gstack) | MIT |
| [cso](cso/) | Security audit: supported static findings; qualified profiles add reproduction and repair candidates. (gstack) | MIT |
| [design-consultation](design-consultation/) | Design consultation: understands your product, researches the landscape, proposes a complete design system (aesthetic, typography, color, layout, spacing, motion), and… | MIT |
| [design-html](design-html/) | Design finalization: generates production-quality Pretext-native HTML/CSS. (gstack) | MIT |
| [design-review](design-review/) | Designer's eye QA: finds visual inconsistency, spacing issues, hierarchy problems, AI slop patterns, and slow interactions — then fixes them. (gstack) | MIT |
| [design-shotgun](design-shotgun/) | Design shotgun: generate multiple AI design variants, open a comparison board, collect structured feedback, and iterate. (gstack) | MIT |
| [deslop-shared-libs](deslop-shared-libs/) | Find worthwhile shared-code extractions in recent work. (gstack) | MIT |
| [devex-review](devex-review/) | Live developer experience audit. (gstack) | MIT |
| [diagram](diagram/) | Turn an English description (or mermaid source) into a diagram triplet: the source, an editable .excalidraw file you can open on excalidraw.com, and rendered SVG + PNG… | MIT |
| [document-generate](document-generate/) | Generate missing documentation from scratch for a feature, module, or entire project. (gstack) | MIT |
| [document-release](document-release/) | Release documentation audit. (gstack) | MIT |
| [eval-plan](eval-plan/) | Preregister a paid eval (bars, arms, decoys, stop rules), dry-run it at zero cost, then run a three-item priced pilot whose spend table gates approval. (gstack) | MIT |
| [freeze](freeze/) | Restrict file edits to a specific directory for the session. (gstack) | MIT |
| [gstack-openclaw-ceo-review](gstack-openclaw-ceo-review/) | Use when asked to review a plan, challenge a proposal, run a CEO review, poke holes in an approach, think bigger about scope, or decide whether to expand or reduce the… | MIT |
| [gstack-openclaw-investigate](gstack-openclaw-investigate/) | Use when asked to debug, fix a bug, investigate an error, or do root cause analysis, and when users report errors, stack traces, unexpected behavior, or say something… | MIT |
| [gstack-openclaw-office-hours](gstack-openclaw-office-hours/) | Use when asked to brainstorm, evaluate whether an idea is worth building, run office hours, or think through a new product idea or design direction before any code is… | MIT |
| [gstack-openclaw-retro](gstack-openclaw-retro/) | Weekly engineering retrospective. Analyzes commit history, work patterns, and code quality metrics with persistent history and trend tracking. Team-aware with per-person… | MIT |
| [gstack-upgrade](gstack-upgrade/) | Upgrade gstack to the latest version. | MIT |
| [guard](guard/) | Full safety mode: destructive command warnings + directory-scoped edits. (gstack) | MIT |
| [hackernews-frontpage](hackernews-frontpage/) | Scrape the Hacker News front page (titles, points, comment counts). | MIT |
| [health](health/) | Code quality dashboard. (gstack) | MIT |
| [investigate](investigate/) | Systematic debugging with root cause investigation. (gstack) | MIT |
| [ios-clean](ios-clean/) | Remove the DebugBridge SPM package and all #if DEBUG wiring from an iOS app. (gstack) | MIT |
| [ios-design-review](ios-design-review/) | Visual design audit for iOS apps on real hardware. (gstack) | MIT |
| [ios-fix](ios-fix/) | Autonomous iOS bug fixer. (gstack) | MIT |
| [ios-qa](ios-qa/) | Live-device iOS QA for SwiftUI apps. (gstack) | MIT |
| [ios-sync](ios-sync/) | Regenerate the iOS debug bridge against the latest upstream gstack templates. (gstack) | MIT |
| [land-and-deploy](land-and-deploy/) | Land and deploy workflow. (gstack) | MIT |
| [landing-report](landing-report/) | Read-only queue dashboard for workspace-aware ship. (gstack) | MIT |
| [learn](learn/) | Manage project learnings. | MIT |
| [make-pdf](make-pdf/) | Turn any markdown file into a publication-quality PDF. (gstack) | MIT |
| [office-hours](office-hours/) | YC Office Hours — two modes. (gstack) | MIT |
| [open-gstack-browser](open-gstack-browser/) | Launch GStack Browser — AI-controlled Chromium with the sidebar extension baked in. | MIT |
| [pair-agent](pair-agent/) | Pair a remote AI agent with your browser. (gstack) | MIT |
| [plan-ceo-review](plan-ceo-review/) | CEO/founder-mode plan review. (gstack) | MIT |
| [plan-design-review](plan-design-review/) | Designer's eye plan review — interactive, like CEO and Eng review. (gstack) | MIT |
| [plan-devex-review](plan-devex-review/) | Interactive developer experience plan review. (gstack) | MIT |
| [plan-eng-review](plan-eng-review/) | Eng manager-mode plan review. (gstack) | MIT |
| [plan-tune](plan-tune/) | Self-tuning question sensitivity + developer psychographic for gstack (v1: observational). (gstack) | MIT |
| [qa](qa/) | Fix browser/API/CLI/job/worker/webhook bugs. (gstack) | MIT |
| [qa-only](qa-only/) | Report browser/API/CLI/job/worker/webhook bugs. (gstack) | MIT |
| [retro](retro/) | Weekly engineering retrospective. (gstack) | MIT |
| [review](review/) | Pre-landing PR review. (gstack) | MIT |
| [scrape](scrape/) | Pull data from a web page through the Aside browser — your real, already signed-in sessions. (gstack) | MIT |
| [setup-browser-cookies](setup-browser-cookies/) | Import cookies from your real Chromium browser into the headless browse session. (gstack) | MIT |
| [setup-deploy](setup-deploy/) | Configure deployment settings for /land-and-deploy. | MIT |
| [setup-gbrain](setup-gbrain/) | Set up gbrain for this coding agent: install the CLI, initialize a local PGLite or Supabase brain, register MCP, capture per-remote trust policy. (gstack) | MIT |
| [ship](ship/) | Ship workflow: detect + merge base branch, run tests, review diff, bump VERSION, update CHANGELOG, commit, push, create PR. (gstack) | MIT |
| [skillify](skillify/) | Codify the most recent successful /scrape flow into a permanent browser-skill on disk. (gstack) | MIT |
| [spec](spec/) | Turn vague intent into a precise, executable spec in five phases. (gstack) | MIT |
| [sync-gbrain](sync-gbrain/) | Keep gbrain current with this repo's code and refresh agent search guidance in CLAUDE.md. (gstack) | MIT |
| [test-audit](test-audit/) | Find low-value or duplicate tests and the test-only code they keep alive. (gstack) | MIT |
| [unfreeze](unfreeze/) | Clear the freeze boundary set by /freeze, allowing edits to all directories again. (gstack) | MIT |

Install one with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/SOYL-AI/soyl-skills-hub/tree/main/skills/dev-workflow/gstack/autoplan -g -a claude-code
```

Back to [Developer workflow](../../../catalog/dev-workflow.md)
