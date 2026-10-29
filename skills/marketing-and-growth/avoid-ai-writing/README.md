# avoid-ai-writing

Skills from [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) at commit [`209815c`](https://github.com/conorbronsdon/avoid-ai-writing/tree/209815cdeb4af942616daec89a5e0a706c804e3a), copied into SOYL Hub on 2026-10-29. Licence: MIT.

> Skill that audits and rewrites content to remove AI writing patterns. Use it with your favorite agents including Claude Code, OpenClaw, Codex, and Hermes.

All credit goes to the authors of conorbronsdon/avoid-ai-writing. Each folder is the upstream skill unchanged, with its licence file added when it had none; build caches and plugin manifests are left out.

| Skill | What it does | Licence |
|---|---|---|
| [ai-writing-detector](ai-writing-detector/) | Use when the user asks to detect, scan, audit, score, or flag AI-writing patterns without rewriting the text, including requests for a deterministic local detector… | MIT |
| [avoid-ai-writing](avoid-ai-writing/) | Audit and rewrite content to remove AI writing patterns ("AI-isms"). Use this skill when asked to "remove AI-isms," "clean up AI writing," "edit writing for AI… | MIT |
| [avoid-ai-writing-router](avoid-ai-writing-router/) | Use when a request combines AI-writing audit, rewrite, file editing, voice preservation, false-positive interpretation, verification, or when the user invokes Avoid AI… | MIT |
| [false-positive-reviewer](false-positive-reviewer/) | Use when a user asks what AI-writing flags mean, whether detector output proves AI authorship, or wants a careful interpretation of possible false positives, especially… | MIT |
| [file-edit-in-place](file-edit-in-place/) | Use when the user names a local file and explicitly asks to clean, rewrite, humanize, or remove AI-writing patterns in that file itself, with minimal targeted edits and… | MIT |
| [preservation-verifier](preservation-verifier/) | Use when the user provides an original and rewritten version, asks whether a rewrite preserved protected content, or wants a deterministic check for code, frontmatter… | MIT |
| [voice-preserving-rewriter](voice-preserving-rewriter/) | Use when the user asks to rewrite, humanize, clean up, or remove AI-isms from text while preserving the writer's voice, facts, intent, structure, register, and protected… | MIT |

Install one with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/SOYL-AI/soyl-skills-hub/tree/main/skills/marketing-and-growth/avoid-ai-writing/ai-writing-detector -g -a claude-code
```

Back to [Marketing and growth](../../../catalog/marketing-and-growth.md)
