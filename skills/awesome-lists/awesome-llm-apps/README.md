# awesome-llm-apps

Skills from [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) at commit [`4bf51ab`](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/4bf51ab704fb2c5b3803cd5191b30d7dcdb51dc2), copied into SOYL Hub on 2026-10-29. Licence: Apache-2.0.

> 100+ AI Agents, Agent Skills and RAG Apps - Free and Open Source.

All credit goes to the authors of Shubhamsaboo/awesome-llm-apps. Each folder is the upstream skill unchanged, with its licence file added when it had none; build caches and plugin manifests are left out.

| Skill | What it does | Licence |
|---|---|---|
| [advisor-orchestrator-worker](advisor-orchestrator-worker/) | Use when a task is too large for one model pass, needs parallel research or generation across many subtasks (like researching a dozen competitors at once), or the user… | Apache-2.0 |
| [chatgpt-app-builder](chatgpt-app-builder/) | DEPRECATED: This skill has been replaced by `mcp-app-builder`. Check if `mcp-app-builder` is available in the skills folder. If not, install it: `npx skills install… | Apache-2.0 |
| [commit-archaeologist](commit-archaeologist/) | Reconstructs why code exists from local git history, including the introducing commit, later changes, current authors, repeated companion files, and likely intent. Use… | Apache-2.0 |
| [dependency-doctor](dependency-doctor/) | Checks requirements.txt, pyproject.toml, and package.json dependency manifests for surface-level direct-dependency footguns: standard-library shadowing pins, abandoned… | Apache-2.0 |
| [first-reader](first-reader/) | Beta readers for any draft, run by simulating how a real reader experiences it, moment by moment. A skim gate, a no-lookahead timed read producing an attention… | Apache-2.0 |
| [mcp-apps-builder](mcp-apps-builder/) | **MANDATORY for ALL MCP server work** - mcp-use framework best practices and patterns. **READ THIS FIRST** before any MCP server work, including: - Creating new MCP… | Apache-2.0 |
| [mcp-builder](mcp-builder/) | DEPRECATED: This skill has been replaced by `mcp-app-builder`. Check if `mcp-app-builder` is available in the skills folder. If not, install it: `npx skills install… | Apache-2.0 |
| [project-graveyard](project-graveyard/) | Scans the developer's machine for dead side projects, autopsies each one from its git history (died at the payments wall, killed by a newer project, finished but never… | Apache-2.0 |
| [scope-creep-detector](scope-creep-detector/) | Analyzes git diffs against a stated intent to detect scope creep, unrelated files, broad pull requests, changes that grew beyond a fix, dependency additions, public API… | Apache-2.0 |
| [thinking-out-loud](thinking-out-loud/) | A contract for what the agent does when a long, messy, stream-of-consciousness ramble arrives (usually voice dictation): act on nothing until the echo brief is approved… | Apache-2.0 |

Install one with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/SOYL-AI/soyl-skills-hub/tree/main/skills/awesome-lists/awesome-llm-apps/advisor-orchestrator-worker -g -a claude-code
```

Back to [Awesome lists](../../../catalog/awesome-lists.md)
