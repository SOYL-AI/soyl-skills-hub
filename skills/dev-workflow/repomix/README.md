# repomix

Skills from [yamadashy/repomix](https://github.com/yamadashy/repomix) at commit [`64c9671`](https://github.com/yamadashy/repomix/tree/64c9671337d865177486360caefb80cfd77a164e), copied into SOYL Hub on 2026-10-29. Licence: MIT.

> 📦 Repomix is a powerful tool that packs your entire repository into a single, AI-friendly file. Perfect for when you need to feed your codebase to Large Language Models (LLMs) or other AI tools like Claude, ChatGPT, DeepSeek, Perplexity, Gemini, Gemma, Llama, Grok, and more.

All credit goes to the authors of yamadashy/repomix. Each folder is the upstream skill unchanged, with its licence file added when it had none; build caches and plugin manifests are left out.

| Skill | What it does | Licence |
|---|---|---|
| [agent-carnet](agent-carnet/) | Use this skill when the user asks to save, recall, find, or organize notes. Triggers on: 'remember this', 'save this', 'note this', 'what did we discuss about...'… | MIT |
| [browser-extension-developer](browser-extension-developer/) | Use this skill when developing or maintaining browser extension code in the `browser/` directory, including Chrome/Firefox/Edge compatibility, content scripts… | MIT |
| [contextual-commit](contextual-commit/) | Write contextual commits that capture intent, decisions, and constraints alongside code changes. Use when committing code, finishing a task, or when the user asks to… | MIT |
| [repomix](repomix/) | Pack and analyze codebases into AI-friendly single files using Repomix. Use when the user wants to explore repositories, analyze code structure, find patterns, check… | MIT |
| [repomix-explorer](repomix-explorer/) | Analyze or explore a codebase (remote or local repository) by packing it with the Repomix CLI, then reading and searching the generated output. Use when the user wants a… | MIT |
| [website-maintainer](website-maintainer/) | Use this skill when working on the Repomix documentation website in `website/` directory, including VitePress configuration, multi-language content, or translation… | MIT |

Install one with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/SOYL-AI/soyl-skills-hub/tree/main/skills/dev-workflow/repomix/agent-carnet -g -a claude-code
```

Back to [Developer workflow](../../../catalog/dev-workflow.md)
