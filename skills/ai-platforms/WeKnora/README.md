# WeKnora

Skills from [Tencent/WeKnora](https://github.com/Tencent/WeKnora) at commit [`e1f9a61`](https://github.com/Tencent/WeKnora/tree/e1f9a6166a593a4804a2f99f1d942919c9cc8ea7), copied into SOYL Hub on 2026-10-29. Licence: MIT.

> Open-source LLM knowledge platform: turn raw documents into a queryable RAG, an autonomous reasoning agent, and a self-maintaining Wiki.

All credit goes to the authors of Tencent/WeKnora. Each folder is the upstream skill unchanged, with its licence file added when it had none; build caches and plugin manifests are left out.

| Skill | What it does | Licence |
|---|---|---|
| [pdf-processing](pdf-processing/) | Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction. | MIT |
| [weknora-rag-search](weknora-rag-search/) | Use when retrieving from or asking questions against a WeKnora knowledge base via the `weknora` CLI — and especially when unsure whether to use `chat`, `session ask`, or… | MIT |
| [weknora-shared](weknora-shared/) | Use when driving a WeKnora RAG server through the `weknora` CLI as an agent — authenticating, managing knowledge bases / documents / sessions / agents, running search or… | MIT |

Install one with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/SOYL-AI/soyl-skills-hub/tree/main/skills/ai-platforms/WeKnora/pdf-processing -g -a claude-code
```

Back to [AI platforms](../../../catalog/ai-platforms.md)
