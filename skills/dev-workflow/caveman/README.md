# caveman

Skills from [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) at commit [`1f951fb`](https://github.com/JuliusBrussee/caveman/tree/1f951fb4ad40ba63302c6e7f987147e034d599d9), copied into SOYL Hub on 2026-10-29. Licence: Apache-2.0+MIT.

> 🪨 why use many token when few token do trick. Viral skill + proxy for coding agents that cuts 65% of tokens by talking like a caveman.

All credit goes to the authors of JuliusBrussee/caveman. Each folder is the upstream skill unchanged, with its licence file added when it had none; build caches and plugin manifests are left out.

| Skill | What it does | Licence |
|---|---|---|
| [cavecrew](cavecrew/) | When to delegate to `cavecrew-investigator` (locate code), `cavecrew-builder` (1-2 file edit) or `cavecrew-reviewer` (diff review) instead of working inline or using… | Apache-2.0+MIT |
| [caveman](caveman/) | Terse caveman voice: answer first, fluff gone, every technical fact kept. Use for /caveman, "caveman mode", "talk like caveman", "be brief", "less tokens". Stays on… | Apache-2.0+MIT |
| [caveman-commit](caveman-commit/) | Write a Conventional Commits message compressed to intent only. Use for "write a commit", "commit message", /commit or /caveman-commit. | Apache-2.0+MIT |
| [caveman-compress](caveman-compress/) | Compress a memory file such as CLAUDE.md or a todo list into caveman format to save input tokens, keeping a readable backup. Sends the file's text to the configured… | Apache-2.0+MIT |
| [caveman-discover](caveman-discover/) | Find and label every LLM workflow in the repository so Caveman Cloud groups spend by workflow instead of one bucket. Use for "discover workflows" or breaking LLM spend… | Apache-2.0+MIT |
| [caveman-evidence-review](caveman-evidence-review/) | Read-only review of Caveman Cloud evidence: cost, Cave Score, workflows, traces, latency, errors, routing, savings. Use when asked what Caveman found or where LLM spend… | Apache-2.0+MIT |
| [caveman-explore](caveman-explore/) | Read-only repository explorer for cold-start orientation, broad cross-file localization, or when a direct search failed. Skip it when the exact file or symbol is already… | Apache-2.0+MIT |
| [caveman-help](caveman-help/) | Quick-reference card for the three caveman skills and their commands. Trigger: /caveman-help or "caveman help". | Apache-2.0+MIT |
| [caveman-learn](caveman-learn/) | Act on a Caveman learn report - review the ranked token sinks, apply cost-lowering fixes with per-edit consent, and report what those fixes returned. Use when asked to… | Apache-2.0+MIT |
| [caveman-manage](caveman-manage/) | Inspect Caveman Cloud's experiment lifecycle and block unsafe execution. Use when asked to start, approve, cancel, promote or roll back a Caveman experiment. | Apache-2.0+MIT |
| [caveman-optimize](caveman-optimize/) | Turn a Caveman optimization observation into an operator-chosen candidate with a paired baseline evaluation. Use when asked to inspect or evaluate a Caveman optimization… | Apache-2.0+MIT |
| [caveman-review](caveman-review/) | Compressed code review - one line per finding with location, problem and fix. Use for /caveman-review, "review this PR", or "review the diff". | Apache-2.0+MIT |
| [caveman-setup](caveman-setup/) | Wire a repository through the Caveman Cloud gateway so every LLM request is measured, with no behavior change. Use for "set up caveman" or adding LLM spend observability. | Apache-2.0+MIT |
| [caveman-stats](caveman-stats/) | Show recorded output and cache-read token usage and mode attribution for the current Claude Code session, or locate the host's native usage report. Trigger… | Apache-2.0+MIT |
| [investigate-first](investigate-first/) | Diagnose ambiguous failures before editing. Use for unknown causes, intermittent behavior, performance regressions, or investigations needing evidence-ranked hypotheses. | Apache-2.0+MIT |
| [lean-build](lean-build/) | Build feature work with high overbuilding risk. Use for new behavior, product slices, or integrations where repository reuse, strict scope, and an explicit stop… | Apache-2.0+MIT |
| [megacave](megacave/) | Caveman in Classical Chinese: 文言文 register, far fewer characters, technical terms verbatim. Invoke only with /megacave or /caveman wenyan. Stays on until "stop caveman"… | Apache-2.0+MIT |
| [migration](migration/) | Implement reversible compatibility-safe transitions. Use for schema, data, API, protocol, configuration, or dependency migrations requiring rollback and preservation… | Apache-2.0+MIT |
| [safe-refactor](safe-refactor/) | Restructure code while preserving behavior. Use for extraction, consolidation, ownership moves, or cleanup where verification must bracket structural edits. | Apache-2.0+MIT |
| [surgical-patch](surgical-patch/) | Fix bugs and small behavior changes at the narrowest responsible layer. Use when regression proof, preserved surrounding behavior, and task-relevant tests matter. | Apache-2.0+MIT |
| [ultracave](ultracave/) | Caveman at maximum compression: fragments, one word when one word is enough, each fact once. Invoke only with /ultracave or /caveman ultra. Stays on until "stop caveman"… | Apache-2.0+MIT |
| [verify-and-stop](verify-and-stop/) | Prove existing work meets acceptance conditions without expanding scope. Use for validation-only tasks, completion checks, focused gate runs, and last-mile proof. | Apache-2.0+MIT |

Install one with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/SOYL-AI/soyl-skills-hub/tree/main/skills/dev-workflow/caveman/cavecrew -g -a claude-code
```

Back to [Developer workflow](../../../catalog/dev-workflow.md)
