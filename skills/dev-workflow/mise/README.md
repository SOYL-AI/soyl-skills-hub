# mise

Skills from [jdx/mise](https://github.com/jdx/mise) at commit [`16e4de8`](https://github.com/jdx/mise/tree/16e4de8bdee6c0a26846815969c3bb5f1cad18d5), copied into SOYL Hub on 2026-11-05. Licence: MIT.

> dev tools, env vars, task runner

All credit goes to the authors of jdx/mise. Each folder is the upstream skill unchanged, with its licence file added when it had none; build caches and plugin manifests are left out.

| Skill | What it does | Licence |
|---|---|---|
| [entire-search](entire-search/) | Search Entire checkpoint history and transcripts with `entire search --json`. Use proactively when the user asks about previous work, commits, sessions, prompts, or… | MIT |
| [jouet-init](jouet-init/) | Configure jouet for a project's actual build, test and agent workflows when setting it up or investigating why it is not helping. Inspect the project and timing history… | MIT |
| [pr-description](pr-description/) | How to write or revise a mise pull request title and description. PR titles and bodies feed the release notes, so use this whenever opening a PR, editing a PR body, or… | MIT |
| [registry-submission](registry-submission/) | Rules for adding a new tool or shorthand to mise's `registry/` — the popularity bar, the required user warning and popularity check, the PR's Popularity section, and… | MIT |
| [update-aube](update-aube/) | Procedure for bumping the aube package manager that mise embeds for its npm backend (the `aube` and `aube-registry` crates). Use when updating aube, reviewing an aube… | MIT |

Install one with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/SOYL-AI/soyl-skills-hub/tree/main/skills/dev-workflow/mise/entire-search -g -a claude-code
```

Back to [Developer workflow](../../../catalog/dev-workflow.md)
