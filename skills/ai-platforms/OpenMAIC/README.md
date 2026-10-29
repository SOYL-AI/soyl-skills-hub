# OpenMAIC

Skills from [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) at commit [`dff201b`](https://github.com/THU-MAIC/OpenMAIC/tree/dff201b49857918885cc5ebadb4a8af254b6ae9d), copied into SOYL Hub on 2026-10-29. Licence: MIT.

> Open Multi-Agent Interactive Classroom — Get an immersive, multi-agent learning experience in just one click

All credit goes to the authors of THU-MAIC/OpenMAIC. Each folder is the upstream skill unchanged, with its licence file added when it had none; build caches and plugin manifests are left out.

| Skill | What it does | Licence |
|---|---|---|
| [build-personal-skill](build-personal-skill/) | Evidence-based creation of a reusable personal course-making Skill from the user's own classroom and chat history. Use when the user asks to summarize, analyze, or learn… | MIT |
| [curriculum-planner](curriculum-planner/) | Multi-stage series — a request for several classrooms that belong together, like 「7 天学 Python」, a four-week onboarding track, a semester unit split across lessons, or… | MIT |
| [deep-interactive](deep-interactive/) | Deep Interactive courses. Plans the course so the learner manipulates something on most pages — simulations, diagrams they explore, code they run, games, 3D scenes —… | MIT |
| [deep-research](deep-research/) | Courses whose content rests on current, external or real-world facts that must be verified against live sources before being taught — recent events, market or policy… | MIT |
| [fact-check](fact-check/) | Improve factual reliability while creating or reviewing a course or supplied content. Use when the user asks to fact-check, verify accuracy, reduce hallucinations, make… | MIT |
| [feynman-learning](feynman-learning/) | Turn any concept, lesson, slide deck, or source material into a Feynman learning cycle in which learners explain first, expose the smallest gap, rebuild the explanation… | MIT |
| [importer](importer/) | — | MIT |
| [k12-core-literacy-planning](k12-core-literacy-planning/) | Chinese K-12 core-literacy course design for a single OpenMAIC classroom. Use when a teacher asks for 中小学课程、核心素养、素养导向、2022 课标、真实情境、任务群、表现性评价, or wants a… | MIT |
| [learning-to-learn](learning-to-learn/) | Infuse learning strategies and metacognition into a concept-centered OpenMAIC classroom as a parallel goal. Use when the user wants students to learn how to learn while… | MIT |
| [lecture-style](lecture-style/) | Masterclass lecturing — one continuous explanation carried by slides, with dense pages, long narration that builds an argument across several real cases, and checkpoints… | MIT |
| [openmaic](openmaic/) | OpenMAIC assistant for setting up, generating, and extending OpenMAIC. Use when the user wants to use OpenMAIC, generate a multi-agent interactive classroom, or build on… | MIT |
| [page-clone](page-clone/) | Building one page that looks like a page the course already has — copy the model page with `duplicate_scene`, then rewrite the copy's words with one `patch_stage` op per… | MIT |
| [pptx-import](pptx-import/) | 会话里有上传的 .pptx，且用户要把这份幻灯片填进一节已建的课（先 create_stage 建课，再 import_pptx 把页面追加进这节课堂，保留原版排版；课堂标题以 create_stage 为准，PPT 不接管）。随后逐页检查（有 render_scene_preview 就渲染看）并修 bad… | MIT |
| [pro-editing](pro-editing/) | Professional editing of a course that already exists. Use when the user wants to revise, improve, restructure or polish pages the course already has — fix a page, tune a… | MIT |
| [slide-craft](slide-craft/) | The design law of a slide page — canvas geometry, the text height table, the type scale, contrast pairs, spacing rhythm, and which element type carries which content… | MIT |
| [slide-dsl](slide-dsl/) | The complete slide DSL manual — the canvas and its background, the ten element types field by field with units, defaults and legal values, where each type keeps its… | MIT |
| [social-emotional-learning](social-emotional-learning/) | Infuse social-emotional learning (SEL) into a concept-centered OpenMAIC classroom as a parallel learning goal. Use when the user asks to add emotional awareness… | MIT |
| [spiral-curriculum](spiral-curriculum/) | Design a multi-stage OpenMAIC course series around a small concept spine whose ideas return repeatedly at higher levels of complexity, abstraction, relationship density… | MIT |
| [stage-design](stage-design/) | The baseline method for building ONE stage — a single classroom — with this runtime. Covers how the plan is settled in conversation, the order the generation tools are… | MIT |
| [stage-dsl](stage-dsl/) | The map for reading and editing an OpenMAIC stage document with read_stage, patch_stage, and grep_stage. Load it before patching a structure you have not patched before… | MIT |
| [style-clone](style-clone/) | Building a new course inside someone else's deck — import the deck as a library of layouts, then produce each page of the new course by copying the layout that fits it… | MIT |
| [teacher-style-clone](teacher-style-clone/) | 工作台会话挂载了教师课堂录像/讲义材料时使用。 | MIT |
| [understanding-by-design](understanding-by-design/) | Use Understanding by Design (UbD) to plan one OpenMAIC classroom or a course series around transferable conceptual understanding. Use when the user wants backward… | MIT |
| [vocational](vocational/) | Vocational / technical training courses. Plans the course as a hands-on work task with an operation flow, tool and equipment state, safety boundaries and GO/STOP… | MIT |
| [workshop-style](workshop-style/) | Hands-on workshop — the learner works through the course instead of watching it, with an exercise or a check every couple of pages, short slides that only set up the… | MIT |
| [zone-of-proximal-development](zone-of-proximal-development/) | Design a coherent assessment-and-practice lesson using zone-of-proximal-development principles: independent diagnosis, targeted review, supported practice, fresh… | MIT |

Install one with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/SOYL-AI/soyl-skills-hub/tree/main/skills/ai-platforms/OpenMAIC/build-personal-skill -g -a claude-code
```

Back to [AI platforms](../../../catalog/ai-platforms.md)
