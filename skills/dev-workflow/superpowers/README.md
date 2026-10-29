# superpowers

Skills from [obra/superpowers](https://github.com/obra/superpowers) at commit [`bb92a77`](https://github.com/obra/superpowers/tree/bb92a77741419a4ab5f06e711a283343f1ada0c3), copied into SOYL Hub on 2026-10-29. Licence: MIT.

> An agentic skills framework & software development methodology that works.

All credit goes to the authors of obra/superpowers. Each folder is the upstream skill unchanged, with its licence file added when it had none; build caches and plugin manifests are left out.

| Skill | What it does | Licence |
|---|---|---|
| [brainstorming](brainstorming/) | You MUST use this before any creative work - creating features, building components, adding functionality, modifying behavior, or planning anything new, in software or… | MIT |
| [diagnosing-superpowers](diagnosing-superpowers/) | Use when a superpowers session went wrong and your human partner wants to know why — repeated work, ignored plans, stumbles, poor results, a skill that didn't fire, "it… | MIT |
| [dispatching-parallel-agents](dispatching-parallel-agents/) | Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies | MIT |
| [executing-plans](executing-plans/) | Use when executing an implementation plan in the current session as the implementer yourself — your human partner chose inline execution, or no subagent tool is available | MIT |
| [finishing-a-development-branch](finishing-a-development-branch/) | Use when implementation is complete, all tests pass, and you need to decide how to integrate the work | MIT |
| [receiving-code-review](receiving-code-review/) | Use when receiving code review feedback, before implementing suggestions, especially if feedback seems unclear or technically questionable - requires technical rigor and… | MIT |
| [requesting-code-review](requesting-code-review/) | Use when completing tasks, implementing major features, or before merging to verify work meets requirements | MIT |
| [subagent-driven-development](subagent-driven-development/) | Use when executing implementation plans with independent tasks in the current session | MIT |
| [systematic-debugging](systematic-debugging/) | Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes | MIT |
| [test-driven-development](test-driven-development/) | Use when implementing any feature or bugfix, before writing implementation code | MIT |
| [using-git-worktrees](using-git-worktrees/) | Use when starting feature work that needs isolation from current workspace or before executing implementation plans - ensures an isolated workspace exists via native… | MIT |
| [using-superpowers](using-superpowers/) | Use when starting any conversation - establishes how to find and use skills, requiring skill invocation before ANY response including clarifying questions | MIT |
| [verification-before-completion](verification-before-completion/) | Use when about to claim work is complete, fixed, or passing, before committing or creating PRs - requires running verification commands and confirming output before… | MIT |
| [writing-plans](writing-plans/) | Use when you have a spec or requirements for a multi-step task, before touching code | MIT |
| [writing-skills](writing-skills/) | Use when creating new skills, editing existing skills, or verifying skills work before deployment | MIT |

Install one with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/SOYL-AI/soyl-skills-hub/tree/main/skills/dev-workflow/superpowers/brainstorming -g -a claude-code
```

Back to [Developer workflow](../../../catalog/dev-workflow.md)
