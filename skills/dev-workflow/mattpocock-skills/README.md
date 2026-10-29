# mattpocock-skills

Skills from [mattpocock/skills](https://github.com/mattpocock/skills) at commit [`5beb35b`](https://github.com/mattpocock/skills/tree/5beb35b040e3de97e54fa9e386d7e42d15c295c2), copied into SOYL Hub on 2026-10-29. Licence: MIT.

> Skills for Real Engineers. Straight from my .agents directory.

All credit goes to the authors of mattpocock/skills. Each folder is the upstream skill unchanged, with its licence file added when it had none; build caches and plugin manifests are left out.

| Skill | What it does | Licence |
|---|---|---|
| [ask-matt](ask-matt/) | Ask which skill or flow fits your situation. A router over the skills in this repo. | MIT |
| [chief-of-staff](chief-of-staff/) | Pursue a long-running goal in a single session by co-ordinating subagents. | MIT |
| [claude-handoff](claude-handoff/) | Hand the current conversation off to a fresh background agent that picks up the work immediately. | MIT |
| [code-review](code-review/) | Review the changes since a fixed point (commit, branch, tag, or merge-base) along two axes: Standards (does the code follow this repo's documented coding standards?) and… | MIT |
| [codebase-design](codebase-design/) | Shared vocabulary for designing deep modules. Use when the user wants to design or improve a module's interface, find deepening opportunities, decide where a seam goes… | MIT |
| [diagnosing-bugs](diagnosing-bugs/) | Diagnosis loop for hard bugs and performance regressions. Use when the user says "diagnose"/"debug this", or reports something broken/throwing/failing/slow. | MIT |
| [domain-modeling](domain-modeling/) | Build and sharpen a project's domain model. Use when discussing codebase terminology, writing or editing a GLOSSARY.md, or recording or editing an ADR. | MIT |
| [git-guardrails-claude-code](git-guardrails-claude-code/) | Set up Claude Code hooks to block dangerous git commands (push, reset --hard, clean, branch -D, etc.) before they execute. Use when user wants to prevent destructive git… | MIT |
| [grill-me](grill-me/) | A relentless interview to sharpen a plan or design. | MIT |
| [grill-with-docs](grill-with-docs/) | A relentless interview to sharpen a plan or design, which also creates docs (ADR's and glossary) as we go. | MIT |
| [grilling](grilling/) | Grill the user relentlessly about a plan, decision, or idea. Use when the user wants to stress-test their thinking, or uses any 'grill' trigger phrases. | MIT |
| [handoff](handoff/) | Compact the current conversation into a handoff document for another agent to pick up. | MIT |
| [implement](implement/) | Implement a piece of work based on a spec or set of tickets. | MIT |
| [implement-spec](implement-spec/) | Implement the result of /to-spec and /to-tickets in code. | MIT |
| [improve-codebase-architecture](improve-codebase-architecture/) | Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill through whichever one you pick. | MIT |
| [loop-me](loop-me/) | Grill me about specs for the workflows I want to build, within this workspace. | MIT |
| [migrate-to-shoehorn](migrate-to-shoehorn/) | Migrate test files from `as` type assertions to @total-typescript/shoehorn. Use when user mentions shoehorn, wants to replace `as` in tests, or needs partial test data. | MIT |
| [pr](pr/) | Use when writing a PR body. | MIT |
| [prototype](prototype/) | Build a throwaway prototype to answer a design question. Use when the user wants to sanity-check whether a state model or logic feels right, or explore what a UI should… | MIT |
| [research](research/) | Investigate a question against high-trust primary sources and capture the findings as a Markdown file in the repo. Use when the user wants a topic researched, docs or… | MIT |
| [retro](retro/) | Conduct a retrospective on a coding session. | MIT |
| [scaffold-exercises](scaffold-exercises/) | Create exercise directory structures with sections, problems, solutions, and explainers that pass linting. Use when user wants to scaffold exercises, create exercise… | MIT |
| [setup-matt-pocock-skills](setup-matt-pocock-skills/) | Configure this repo for the engineering skills: set up its issue tracker, triage label vocabulary, and domain doc layout. Run once before first use of the other… | MIT |
| [setup-pre-commit](setup-pre-commit/) | Set up Husky pre-commit hooks with lint-staged (Prettier), type checking, and tests in the current repo. Use when user wants to add pre-commit hooks, set up Husky… | MIT |
| [setup-ts-deep-modules](setup-ts-deep-modules/) | Wire dependency-cruiser into a TypeScript repo so each package is a deep module, with implementation hidden in subfolders and reachable only through its entry-point… | MIT |
| [tdd](tdd/) | Test-driven development. Use when the user wants to build features or fix bugs test-first, mentions "red-green-refactor", or wants integration tests. | MIT |
| [teach](teach/) | Teach the user a new skill or concept, within this workspace. | MIT |
| [to-questionnaire](to-questionnaire/) | Turn a decision you can't fully answer into a questionnaire for someone else to fill in. | MIT |
| [to-spec](to-spec/) | Turn the current conversation into a spec and publish it to the project issue tracker: no interview, just synthesis of what you've already discussed. | MIT |
| [to-tickets](to-tickets/) | Break a plan, spec, or the current conversation into a set of tracer-bullet tickets, each declaring its blocking edges, published to the configured tracker (edges as… | MIT |
| [triage](triage/) | Move issues and external PRs through a state machine of triage roles, categorise, verify, grill if needed, and write agent-ready briefs. | MIT |
| [wait-what](wait-what/) | Stop. That last message did not land: re-pitch it. | MIT |
| [wayfinder](wayfinder/) | Plan a huge chunk of work (more than one agent session can hold) as a shared map of decision tickets on your issue tracker, and resolve them one at a time until the way… | MIT |
| [wizard](wizard/) | Generate an interactive bash wizard that walks a human through steps only they can perform. Use when provisioning infrastructure, setting up credentials or CI secrets… | MIT |
| [writing-beats](writing-beats/) | Writing, exploit; assemble raw material into a journey of beats, grounding each term before a beat leans on it. | MIT |
| [writing-for-agents](writing-for-agents/) | Writing documents for agents. Use when creating or editing skills, or modifying AGENTS.md or CLAUDE.md. | MIT |
| [writing-fragments](writing-fragments/) | Writing, explore: mine raw fragments, no structure yet. | MIT |
| [writing-shape](writing-shape/) | Writing, exploit: shape raw material into an article, paragraph by paragraph. | MIT |

Install one with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/SOYL-AI/soyl-skills-hub/tree/main/skills/dev-workflow/mattpocock-skills/ask-matt -g -a claude-code
```

Back to [Developer workflow](../../../catalog/dev-workflow.md)
