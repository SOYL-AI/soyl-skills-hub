# plannotator

Skills from [backnotprop/plannotator](https://github.com/backnotprop/plannotator) at commit [`5cf5177`](https://github.com/backnotprop/plannotator/tree/5cf5177267aa96405fec56faa3e8426c12bd648b), copied into SOYL Hub on 2026-11-21. Licence: Apache-2.0+MIT.

> The workspace to stay in the loop and on top of agents - shape, decide, plan, annotate, review code, share with team, and send all feedback to agents with one click.

All credit goes to the authors of backnotprop/plannotator. Each folder is the upstream skill unchanged, with its licence file added when it had none; build caches and plugin manifests are left out.

| Skill | What it does | Licence |
|---|---|---|
| [plannotator](plannotator/) | Reference for using Plannotator (its `plannotator` tool when you have one, otherwise the CLI): plan review, code review, annotating files, URLs, folders, and running… | Apache-2.0+MIT |
| [plannotator-annotate](plannotator-annotate/) | Open Plannotator's annotation UI for a file, folder, or URL, then address the returned annotations. | Apache-2.0+MIT |
| [plannotator-compound](plannotator-compound/) | Analyze a user's Plannotator plan archive to extract denial patterns, feedback taxonomy, evolution over time, and actionable prompt improvements — then produce a… | Apache-2.0+MIT |
| [plannotator-inbox](plannotator-inbox/) | Open the Plannotator Inbox in the browser (starting it if needed), say its address, and learn how to use the Inbox for the rest of the session. | Apache-2.0+MIT |
| [plannotator-last](plannotator-last/) | Open Plannotator on the latest rendered assistant message and use the returned annotations to revise that message or continue. | Apache-2.0+MIT |
| [plannotator-review](plannotator-review/) | Open Plannotator's browser-based code review UI and address the returned feedback. | Apache-2.0+MIT |
| [plannotator-setup-goal](plannotator-setup-goal/) | Turn an idea or objective into a goal package for /goal. Interviews the user, builds a reviewed fact sheet via Plannotator, then explores the codebase to produce an… | Apache-2.0+MIT |
| [plannotator-visual-explainer](plannotator-visual-explainer/) | Generate self-contained HTML visualizations with Plannotator theming. Use for implementation plans, PR explainers, architecture diagrams, data tables, slide decks, and… | Apache-2.0+MIT |
| [release-plannotator](release-plannotator/) | Prepare and execute a Plannotator release — draft release notes with full contributor credit, bump versions across all package files, build in dependency order, and kick… | Apache-2.0+MIT |
| [review-renovate](review-renovate/) | Review Renovate bot PRs that update GitHub Actions dependencies. Verifies supply chain integrity by checking pinned commit SHAs against upstream tagged releases, reviews… | Apache-2.0+MIT |
| [update-deps](update-deps/) | Audit and update npm/Bun dependencies with supply chain integrity checks — verifies maintainers, publish age, tarball diffs, and provenance before bumping. Defers risky… | Apache-2.0+MIT |

Install one with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/SOYL-AI/soyl-skills-hub/tree/main/skills/dev-workflow/plannotator/plannotator -g -a claude-code
```

Back to [Developer workflow](../../../catalog/dev-workflow.md)
