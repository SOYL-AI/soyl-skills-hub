# mem0

Skills from [mem0ai/mem0](https://github.com/mem0ai/mem0) at commit [`ed1f10f`](https://github.com/mem0ai/mem0/tree/ed1f10fc87080f0b67f99be370817504888462ab), copied into SOYL Hub on 2026-11-05. Licence: Apache-2.0.

> The Memory Layer for AI Agents - Drop-in memory infrastructure for AI agents and apps. Context that persists. Built for production.

All credit goes to the authors of mem0ai/mem0. Each folder is the upstream skill unchanged, with its licence file added when it had none; build caches and plugin manifests are left out.

| Skill | What it does | Licence |
|---|---|---|
| [context-loader](context-loader/) | Search memories from earlier Pi sessions in this repository. Use it when earlier work may already explain the code, error, decision, or command you need, so you can… | Apache-2.0 |
| [forget](forget/) | Delete the Mem0 memories stored for this repository and this user. Use when the user asks to forget, clear, wipe, or delete memories. | Apache-2.0 |
| [mem0](mem0/) | Mem0 Platform SDK for adding persistent memory to AI applications. TRIGGER when: user mentions "mem0", "MemoryClient", "memory layer", "remember user preferences"… | Apache-2.0 |
| [mem0-cli](mem0-cli/) | Mem0 CLI -- the command-line interface for mem0 memory operations. TRIGGER when: user mentions "mem0 cli", "mem0 command line", "@mem0/cli", "mem0-cli", "pip install… | Apache-2.0 |
| [mem0-context-loader](mem0-context-loader/) | Search memories from earlier OpenCode sessions in this repository. Use it when earlier work may already explain the code, error, decision, or command you need, so you… | Apache-2.0 |
| [mem0-forget](mem0-forget/) | Deletes memories by search query or memory ID with confirmation before removal. Use when removing outdated decisions, incorrect memories, sensitive data, or cleaning up… | Apache-2.0 |
| [mem0-integrate](mem0-integrate/) | Integrate Mem0 into an existing repository using a goal-driven, TDD pipeline. Detects the repo's language automatically and asks the user to pick between Mem0 Platform… | Apache-2.0 |
| [mem0-oss-to-platform](mem0-oss-to-platform/) | Plan, then execute, a migration of a project from the mem0 open-source / self-hosted SDK (local `Memory` class) to the mem0 Platform / hosted SDK (`MemoryClient`)… | Apache-2.0 |
| [mem0-remember](mem0-remember/) | Stores a memory verbatim from user input with appropriate type classification and metadata. Use when the user says remember this, save this, store this, note that, or… | Apache-2.0 |
| [mem0-scope](mem0-scope/) | Views or changes the default memory scope (project, session, or global) used when saving and searching memories. Use when the user wants to control whether memories are… | Apache-2.0 |
| [mem0-search](mem0-search/) | Searches memories and displays compact one-liner results, or looks up a specific memory by ID. Use for quick memory lookups, checking if a decision was recorded… | Apache-2.0 |
| [mem0-status](mem0-status/) | Diagnoses mem0 connectivity, API key validity, and memory read/write functionality. Use when memory operations fail, searches return empty, add_memory errors occur, or… | Apache-2.0 |
| [mem0-test-integration](mem0-test-integration/) | Verify a Mem0 integration produced by /mem0-integrate. Runs in the same workspace on the same branch (loose coupling) — installs dependencies, runs the repo's native… | Apache-2.0 |
| [mem0-tour](mem0-tour/) | Browses all stored memories grouped by category with full content display. Use when reviewing all project memories, exploring stored knowledge, onboarding to a project… | Apache-2.0 |
| [mem0-vercel-ai-sdk](mem0-vercel-ai-sdk/) | Mem0 provider for Vercel AI SDK (@mem0/vercel-ai-provider). TRIGGER when: user mentions "vercel ai sdk", "@mem0/vercel-ai-provider", "createMem0", "retrieveMemories"… | Apache-2.0 |
| [memory-triage](memory-triage/) | Persistent long-term memory protocol powered by mem0. Evaluate conversations for durable facts worth storing via memory_add. Handles identity, preferences, decisions… | Apache-2.0 |
| [pause](pause/) | Pause Mem0 memory capture on this machine. Use when the user wants to stop memories being recorded, for example for private work or experiments. | Apache-2.0 |
| [remember](remember/) | Acknowledge a "remember this" request and make sure it is captured well. Use when the user explicitly asks to remember, note, or save something for future sessions. | Apache-2.0 |
| [resume](resume/) | Resume Mem0 memory capture after it was paused with /mem0:pause. | Apache-2.0 |
| [search](search/) | Search memories from earlier Antigravity sessions in this repository. Use it when earlier work may already explain the code, error, decision, or command you need, so you… | Apache-2.0 |
| [status](status/) | Show whether Mem0 memory is working in this repository, covering configuration, capture state, pending flushes, and whether the Mem0 API key is valid. Use when the user… | Apache-2.0 |
| [tour](tour/) | Browses all stored memories grouped by category with full content display. Use when reviewing all memories, exploring stored knowledge, onboarding to a new session, or… | Apache-2.0 |

Install one with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/SOYL-AI/soyl-skills-hub/tree/main/skills/ai-platforms/mem0/context-loader -g -a claude-code
```

Back to [AI platforms](../../../catalog/ai-platforms.md)
