# deepseek-harness

Skills from [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) at commit [`22ddee3`](https://github.com/deepseek-ai/deepseek-harness/tree/22ddee3792402c3e70ec5f86a63c3e3e895a2f60), copied into SOYL Hub on 2026-10-29. Licence: MIT.

> DeepSeek Harness: Everything is a Plugin.

All credit goes to the authors of deepseek-ai/deepseek-harness. Each folder is the upstream skill unchanged, with its licence file added when it had none; build caches and plugin manifests are left out.

| Skill | What it does | Licence |
|---|---|---|
| [agent-experience](agent-experience/) | Use when writing or changing a model-facing tool definition (name, description, parameter schema, or its system-prompt section), and when designing skills, context… | MIT |
| [cordis-composition-reference](cordis-composition-reference/) | Use when writing or reading a Cordis bundle patch or agent preset for this harness and you need the Loader YAML dialect (insert, override by id, group, disabled… | MIT |
| [cordis-plugin-development](cordis-plugin-development/) | Use when designing, reviewing, adding, enabling, disabling, installing, configuring, or debugging a plugin, bundle, feature, page, panel, tool, or MCP connection in the… | MIT |
| [cordis-styling-nitpicking](cordis-styling-nitpicking/) | Use during code review of DeepSeek Harness Cordis plugins and helpers reachable from their entrypoints, including pull requests, and during focused lifecycle audits… | MIT |
| [diagnose-windows-sandbox-acl](diagnose-windows-sandbox-acl/) | Use on Windows for unexpected DSH sandbox access denials: workspace writes or listing fail, or an ordinarily readable path cannot be read. One bundled command inspects… | MIT |
| [dsh-archive-agent-notes](dsh-archive-agent-notes/) | Use when adding, auditing, pruning, archiving, restoring, or reviewing Agent Notes in deepseek-harness; checks every new note for superseded active records, deletes… | MIT |
| [dsh-ci-test-reliability](dsh-ci-test-reliability/) | Design, review, and diagnose DeepSeek Harness tests and fixtures that can fail nondeterministically under CI concurrency, shared host resources, clocks, process-global… | MIT |
| [dsh-client-ui-ux](dsh-client-ui-ux/) | Design and review DeepSeek Harness client UI changes — visual token discipline, reuse-before-adding, feedback surfaces (toast vs in-place notice vs empty state), overlay… | MIT |
| [dsh-code-review](dsh-code-review/) | Use when reviewing a pull request in the deepseek-harness repo — orients the reviewer to this codebase's standards (AGENTS.md conventions, defensive patterns, ADRs… | MIT |
| [dsh-create-upgrade-guide](dsh-create-upgrade-guide/) | Use when a deepseek-harness change breaks an externally perceptible surface (CLI, profiles, cordis.yml or settings keys, persisted user data, SDK or wire APIs, published… | MIT |
| [dsh-doc](dsh-doc/) | Create, restructure, review, audit, or migrate DeepSeek Harness Markdown documentation, package READMEs, and the documentation website using audience-first hierarchy… | MIT |
| [dsh-error-handling](dsh-error-handling/) | Apply error-handling principles when designing or reviewing failures, recovery, retries, background tasks, and user-visible error reports. | MIT |
| [dsh-find-simplifications](dsh-find-simplifications/) | Find evidence-backed simplifications in DeepSeek Harness code, APIs, configuration, tests, and prose; write or consolidate proposals, identify small inline cleanups, or… | MIT |
| [dsh-merging-stacked-prs](dsh-merging-stacked-prs/) | Use when landing a stack of dependent GitHub PRs (A ← B ← C, where each bases on the one below) onto master, merging a PR whose base is another open PR's branch, or… | MIT |
| [dsh-official-plugin-artwork](dsh-official-plugin-artwork/) | Draw and review official DeepSeek Harness plugin icons and optional feature previews, including experimental plugins. Use for package artwork and PluginArtwork glyphs… | MIT |
| [dsh-pr-description](dsh-pr-description/) | Use when creating a deepseek-harness pull request, or when updating its description after later changes or a handled review round. Defines each description section… | MIT |
| [dsh-pre-push-checks](dsh-pre-push-checks/) | Use before pushing, force-pushing, marking ready for review, or claiming checks pass on a deepseek-harness branch, and immediately after gh stack sync publishes… | MIT |
| [dsh-prose-standard](dsh-prose-standard/) | Use when writing, reviewing, restoring, trimming, or auditing prose in the deepseek-harness repo, including deciding where documentation or comments are required across… | MIT |
| [dsh-responsive-ui](dsh-responsive-ui/) | Use when designing, implementing, or reviewing responsive client layouts, mobile and touch detection, text truncation, title wrapping, icon-only controls, mobile hover… | MIT |
| [dsh-session-projection](dsh-session-projection/) | Use when creating, extending, or reviewing a DeepSeek Harness session projection, or migrating session-derived recovery state to one. | MIT |
| [dsh-speed-up-perf](dsh-speed-up-perf/) | Use when investigating or optimizing DeepSeek Harness performance, designing realistic synthetic benchmarks or CI performance gates, profiling long Sessions or Web… | MIT |
| [dsh-translate-docs](dsh-translate-docs/) | Manually run the extended DeepSeek Harness bilingual-document workflow, including generated briefings, delegated prose translation, whole-document translation, and… | MIT |
| [dsh-trim-cot-leakage](dsh-trim-cot-leakage/) | Use when auditing or fixing prose that reads like a leaked reasoning transcript — dead design-session citations such as (decision N), audit item codes, or §N of… | MIT |
| [editing-cordis-compositions](editing-cordis-compositions/) | Use when creating, changing, or validating an agent preset or other Cordis composition for this harness, including deciding host versus preset placement and checking… | MIT |
| [office](office/) | Create, edit, inspect, or convert Office documents, spreadsheets, presentations, and PDFs. Load to choose the relevant workflow. | MIT |
| [office-docx](office-docx/) | Create, read, edit, and validate Word documents (.docx). | MIT |
| [office-export-pdf](office-export-pdf/) | Convert an Office document to a requested PDF with LibreOffice Kit. | MIT |
| [office-pptx](office-pptx/) | Create, read, edit, and validate PowerPoint presentations (.pptx). | MIT |
| [office-recalculate](office-recalculate/) | Refresh spreadsheet formula caches and verify calculated values with LibreOffice Kit. | MIT |
| [office-render](office-render/) | Render requested document images or inspect visual layout with LibreOffice Kit. | MIT |
| [office-xlsx](office-xlsx/) | Read, create, edit, and validate Excel workbooks, data, and formulas (.xlsx). | MIT |
| [record-browser-gif](record-browser-gif/) | Record browser or Web UI interaction demos as optimized GIFs using the available browser-control workflow, optional Playwright Videos for higher capture frame rates, and… | MIT |

Install one with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/SOYL-AI/soyl-skills-hub/tree/main/skills/ai-platforms/deepseek-harness/agent-experience -g -a claude-code
```

Back to [AI platforms](../../../catalog/ai-platforms.md)
