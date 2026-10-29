# PaddleOCR

Skills from [PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) at commit [`dab3fe3`](https://github.com/PaddlePaddle/PaddleOCR/tree/dab3fe35379033fdcb2d0e9572fac0b36c9a9ebf), copied into SOYL Hub on 2026-10-29. Licence: Apache-2.0.

> Turn any PDF or image document into structured data for your AI. A powerful, lightweight OCR toolkit that bridges the gap between images/PDFs and LLMs. Supports 100+ languages.

All credit goes to the authors of PaddlePaddle/PaddleOCR. Each folder is the upstream skill unchanged, with its licence file added when it had none; build caches and plugin manifests are left out.

| Skill | What it does | Licence |
|---|---|---|
| [paddleocr-doc-parsing](paddleocr-doc-parsing/) | Use this skill to extract structured Markdown/JSON from PDFs and document images—tables with cell-level precision, formulas as LaTeX, figures, seals, charts… | Apache-2.0 |
| [paddleocr-text-recognition](paddleocr-text-recognition/) | Use this skill whenever the user wants text extracted from images, photos, scans, screenshots, or scanned PDFs. Returns exact machine-readable strings with line-level… | Apache-2.0 |

Install one with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/SOYL-AI/soyl-skills-hub/tree/main/skills/ai-platforms/PaddleOCR/paddleocr-doc-parsing -g -a claude-code
```

Back to [AI platforms](../../../catalog/ai-platforms.md)
