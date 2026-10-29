# AI platforms

Skills that ship with agent frameworks, RAG systems and model tooling.

130 skills here and 1 linked to their source, from 8 projects. [All categories](../CATALOG.md)

**To install a skill**, open it, copy the address from your browser and run `npx skills add <that address> -g -a claude-code`. More ways in [How to install](../README.md#install-a-skill). Skills marked ↗ live in their own repos: install them from there.

## jiuwenswarm

[openJiuwen-ai/jiuwenswarm](https://github.com/openJiuwen-ai/jiuwenswarm) · Apache-2.0 · ★ 8.4k · 48 here

JiuwenSwarm is an intelligent AI Agent built on openJiuwen. It extends the powerful capabilities of large language models directly to your fingertips through various communication apps you use daily.

| Skill | What it does |
|---|---|
| [advanced-daily-report](../skills/ai-platforms/jiuwenswarm/advanced-daily-report/) | 进阶版日报生成器，支持多数据源采集、工作分析、趋势对比、周报月报聚合 |
| [aet-req-analysis](../skills/ai-platforms/jiuwenswarm/aet-req-analysis/) | Requirements analysis skill - transforms raw requirements into structured specifications through Socratic dialogue, behavior analysis, and requirement specification… |
| [aet-req-design](../skills/ai-platforms/jiuwenswarm/aet-req-design/) | Requirements design skill - transforms requirements analysis specifications into implementable system design specifications through architecture design, module change… |
| [aet-req-review](../skills/ai-platforms/jiuwenswarm/aet-req-review/) | Gate pipeline for requirement deliverables — enforces automated quality gates and interactive user validation before handover. Trigger when: (1) structured PRD/spec/SDD… |
| [agent-creator](../skills/ai-platforms/jiuwenswarm/agent-creator/) | Agent 模板包的创建与更新器：从自然语言创建可被 JiuwenSwarm 加载的 agent 模板包，或在同一流程的 update mode 下修改已有自定义专家。 触发词：创建 agent模板包、创建模板包、生成 agent 模板、新建 agent、做一个 agent、create agent… |
| [agent-group-creator](../skills/ai-platforms/jiuwenswarm/agent-group-creator/) | 从自然语言创建可被 JiuwenSwarm 加载和安装的专家团（agent_group）包，包含 Leader、专家成员、协作指令及可选共享技能。用户提出“创建专家团”“组建专家团队”“做一个多专家协作团队”时使用；创建单个专家使用 agent-creator，执行已有专家团的业务任务不使用本技能。 |
| [akg-agents](../skills/ai-platforms/jiuwenswarm/akg-agents/) | 代理执行 AKG 算子任务。先检查固定仓库与分支；若 `~/.akg/check_env.md` 不存在则强制 `FULL_SETUP=true`；忽略所有 `akg_cli` 检查和使用；后端代码生成直接执行 `run_workflow.py --workflow kernelgen`。 |
| [ascend-moe-optimizer-auto-trace](../skills/ai-platforms/jiuwenswarm/ascend-moe-optimizer-auto-trace/) | 为昇腾算子在源码中接入 TRACE_POINT 与 MoeTracing，串通 trace_preprocessor、profiling tensor、point_map.json、 save_profiling_data 与 trace_collector 生成 Chrome trace。强调门禁 G1–G5：全链路预处理与… |
| [ascend-moe-optimizer-trace-analyzer](../skills/ai-platforms/jiuwenswarm/ascend-moe-optimizer-trace-analyzer/) | 在用户提供 Chrome/Perfetto trace.json、或排查 Ascend 上 MoE/FusedDeepMoe 等算子性能时使用。按 phase、category、core group、tid 统计耗时、overlap、bubble，输出 CSV、Markdown 报告与确定性诊断；可选外部 LLM 扩写分析。默认… |
| [baidu-netdisk-guide](../skills/ai-platforms/jiuwenswarm/baidu-netdisk-guide/) | 百度网盘官方 MCP Server 使用指引：文件浏览与检索、文件管理、分享链接、容量查询、内容保存的工具选择策略与写操作安全规则。当用户要求操作百度网盘（查容量、找文件、浏览整理文件、生成分享链接、保存文本或 URL 到网盘）时使用。 |
| [baoyu-image-gen](../skills/ai-platforms/jiuwenswarm/baoyu-image-gen/) | AI image generation with OpenAI GPT Image 2, Azure OpenAI, Google, OpenRouter, DashScope, Z.AI GLM-Image, MiniMax, Jimeng, Seedream, Replicate and Agnes APIs. Supports… |
| [brief](../skills/ai-platforms/jiuwenswarm/brief/) | Turn a user request into an executable design brief. Use when writing the outline, logline, visual style, subjects, setting, duration, audio policy, or the timed clip… |
| [character](../skills/ai-platforms/jiuwenswarm/character/) | Produce one locked character identity plate for later video reference. Use when designing a character sheet, costume, face, or the character1 binding order. |
| [clip](../skills/ai-platforms/jiuwenswarm/clip/) | Generate one reference-to-video shot from locked character and scene plates. Use when producing a single storyboard row as a short video clip. |
| [compose](../skills/ai-platforms/jiuwenswarm/compose/) | Stitch finished shots into one film and mix audio by policy. Use when assembling the timeline, normalizing resolution, or ducking music under speech. |
| [computer-use-macos](../skills/ai-platforms/jiuwenswarm/computer-use-macos/) | Operate macOS application UI through computer_use MCP and the Computer → App → Element SDK. Use when observing, clicking, or typing on a macOS MCP host, including a… |
| [computer-use-windows](../skills/ai-platforms/jiuwenswarm/computer-use-windows/) | Operate Windows application UI through computer_use MCP and the Computer → App → Element SDK. Use when observing, clicking, or typing on a Windows MCP host, including a… |
| [cross-channel-history-retrieval](../skills/ai-platforms/jiuwenswarm/cross-channel-history-retrieval/) | 跨会话检索聊天原文（记忆不足时再用）。在回答任何关于历史事件、日期、人物、过去对话的问题时，如果记忆中没有相关信息或不足以回答，则需要使用跨会话检索聊天原文。用 mcp_exec_command 执行 scripts/search_history.py，读… |
| [deepep-to-cam-converter](../skills/ai-platforms/jiuwenswarm/deepep-to-cam-converter/) | 识别代码中可替换为CAM算子的DeepEP算子，基于实际运行参数校验约束，自动完成通信域转换（NCCL->HCCL）、设备适配（CUDA->NPU）及算子替换。 |
| [delayed-restart-app](../skills/ai-platforms/jiuwenswarm/delayed-restart-app/) | 安排延迟重启本 Agent 所在的服务（JiuwenSwarm app）。执行后当前 Agent 进程会被终止并重新启动，当前会话会断开。用于用户要求重启、配置更新需生效、或服务异常需重载时。使用 bash 调用脚本。 |
| [doc-update](../skills/ai-platforms/jiuwenswarm/doc-update/) | 以源码为唯一事实来源，系统性核对并更新项目文档，确保内容与实现一致、多语言文档 1:1 对齐、结构完整。 |
| [docx-pro](../skills/ai-platforms/jiuwenswarm/docx-pro/) | Professional Word (.docx) document generation, faithful text replacement, Markdown round-trip conversion, document inspection, TOC insertion and watermarking. Use when… |
| [dynamic-memory-cli](../skills/ai-platforms/jiuwenswarm/dynamic-memory-cli/) | Operate a dynamic, UT-backed agent memory with atomic Pending publication, merged Pending/Built search, Memory Snapshot and history cursor state, Built-only validation… |
| [financial-document-parser](../skills/ai-platforms/jiuwenswarm/financial-document-parser/) | Extract and analyze data from invoices, receipts, bank statements, and financial documents. Categorize expenses, track recurring charges, and generate expense reports… |
| [gitcode-api](../skills/ai-platforms/jiuwenswarm/gitcode-api/) | 使用 gitcode-api 命令行工具访问 GitCode REST API。适用于需要查询仓库、Issue、Pull Request、文件内容、用户、组织、搜索结果，或需要获取 Issue 与 Pull Request 模版的场景。还可用于总结仓库最近 commit / PR / issue、责任人、模块、风险或对外接口影响。 |
| [harmonyos-dev-suite](../skills/ai-platforms/jiuwenswarm/harmonyos-dev-suite/) | Unified HarmonyOS development entry skill for ArkTS, ArkUI, DevEco CLI, build/run/debug, device logs, testing, multi-device adaptation, atomic services, native… |
| [huawei-cloud-maas-setup](../skills/ai-platforms/jiuwenswarm/huawei-cloud-maas-setup/) | 引导用户完成华为云 MaaS 服务购买和 API 配置。脚本自动完成授权更新、API Key 创建、模型开通；用户只需完成登录、充值、选择要开通的模型。整个流程预计 3-5 分钟。 适用于首次运行配置、华为云 MaaS 服务开通、API 凭证获取、模型服务配置等场景。 当用户提到华为云、MaaS、Maas、开通模型服务、配置… |
| [jiuwenswarm-pr-review](../skills/ai-platforms/jiuwenswarm/jiuwenswarm-pr-review/) | Review a specified JiuwenSwarm pull request against the repository's technical direction, architecture, feature interactions, documentation, scope, code quality, reuse… |
| [llm-wiki](../skills/ai-platforms/jiuwenswarm/llm-wiki/) | Build and maintain a persistent knowledge base (LLM Wiki) using native backend tools. Supports ingesting PDFs, Markdown, and TXT files, and querying or linting the data… |
| [local-doc-ocr](../skills/ai-platforms/jiuwenswarm/local-doc-ocr/) | 本地离线 OCR——将扫描件 PDF/图片提取为文字。双引擎：(A) RapidOCR 纯本地离线一键出 .md（默认保底、不联网、不占 token、可批量）；(B) 支持多模态读图能力的 Agent 逐页读图（高质量，擅长表格/手写/印章，如 WorkBuddy 的 Read… |
| [openJiuwen-DeepSearch](../skills/ai-platforms/jiuwenswarm/openjiuwen-deepsearch/) | 知识增强型深度检索与深度研究，支持查询规划、信息收集、理解反思、研究报告生成等多 Agent 协同。使用场景：金融分析研报、学术与政策研究、企业级深度搜索等复杂推理任务，可以生成Markdown、Doc和Html格式的研究报告。**每次使用该技能之前都先完整阅读一遍SKILL.md学习技能。** |
| [pdf-extraction](../skills/ai-platforms/jiuwenswarm/pdf-extraction/) | Extract text, tables, and metadata from PDFs using pdfplumber |
| [plugin-creator](../skills/ai-platforms/jiuwenswarm/plugin-creator/) | Plugin 插件包的创建与更新器：从自然语言创建可被 JiuwenSwarm 加载的 plugin 插件包，或在同一流程的 update mode 下修改已有自定义插件。 触发词：创建插件、创建 plugin、做一个插件、plugin 脚手架、修改插件、编辑插件、更新插件、调整插件、create plugin… |
| [ppt-creation](../skills/ai-platforms/jiuwenswarm/ppt-creation/) | 当任务要求创建、读取、解析、提取、编辑、修改、合并、拆分、转换或检查 PPT / 幻灯片 / 演示文稿 / deck / slides / presentation / .pptx 文件时使用。本 skill 以内置模板为版面底座，让 Agent 在内容区自由设计；支持原生 PptxGenJS… |
| [pptx-generator](../skills/ai-platforms/jiuwenswarm/pptx-generator/) | Generate, edit, and read PowerPoint presentations. Create from scratch with PptxGenJS (cover, TOC, content, section divider, summary slides), edit existing PPTX via XML… |
| [project-maintainer](../skills/ai-platforms/jiuwenswarm/project-maintainer/) | Use when initializing or updating structured in-repository project-maintenance docs; exploring existing code; analyzing a full project or repository; documenting… |
| [rsi-program-dataset-creator](../skills/ai-platforms/jiuwenswarm/rsi-program-dataset-creator/) | Use for program evolution — improving a working program by repeated search against a measured score, rather than by one edit. Covers both halves: deciding what is… |
| [scene](../skills/ai-platforms/jiuwenswarm/scene/) | Produce one empty scene plate for later video reference. Use when designing a setting, its geography, weather, lighting, or props. |
| [skill-creator](../skills/ai-platforms/jiuwenswarm/skill-creator/) | Unified entry point for all Skill creators. Routes skill creation and editing requests to the correct specialized creator. Use whenever the user wants to create a new… |
| [skill-creator-normal](../skills/ai-platforms/jiuwenswarm/skill-creator-normal/) | Create new single-agent skills, modify and improve existing single-agent skills, and measure skill performance. Use when users want to create a skill from scratch, edit… |
| [skill-gen-4-enterprise-doc](../skills/ai-platforms/jiuwenswarm/skill-gen-4-enterprise-doc/) | Turn SOPs, URLs, or stated intent into an installed skill package. Use when the user asks to generate a skill from a document, link, or workflow. Follow SKILL.md… |
| [skill-omni-creation](../skills/ai-platforms/jiuwenswarm/skill-omni-creation/) | 当用户说「从这个链接/URL生成skill」「把这个网页/教程做成skill」「从这个视频提取步骤」时触发。先读取此 SKILL.md，再按步骤调用 scripts/ 下的 Python 脚本完成：爬取网页或下载视频 → 下载图片/抽帧 → 生成标准 Skill Markdown… |
| [skvm-general](../skills/ai-platforms/jiuwenswarm/skvm-general/) | Drive the skvm CLI on behalf of a user to profile models, AOT-compile skills, run skill-assisted tasks, run benchmarks, and manage compiled proposals. Trigger when the… |
| [skvm-jit](../skills/ai-platforms/jiuwenswarm/skvm-jit/) | Trigger `skvm jit-optimize` with post-task evidence so it generates a reviewable optimization proposal for a skill. Use after finishing a task that was driven by any… |
| [storyboard](../skills/ai-platforms/jiuwenswarm/storyboard/) | Turn a brief into a one-row-per-shot storyboard table. Use when planning shot size, camera move, action, scene changes, or the prompt for a clip. |
| [swarmskill-creator](../skills/ai-platforms/jiuwenswarm/swarmskill-creator/) | Creates, converts, or modifies Swarm Skills — the multi-role (多角色团队) extension of the Skills standard, optionally with an executable SwarmFlow orchestration script. Use… |
| [wan-reference-video](../skills/ai-platforms/jiuwenswarm/wan-reference-video/) | Best practices for Alibaba Wan reference-to-video (R2V) prompts and reference_images attach order. Use when authoring Design clip prompts, binding character1… / Scene N… |
| [xlsx](../skills/ai-platforms/jiuwenswarm/xlsx/) | Open, create, read, analyze, edit, repair, or validate spreadsheet files (.xlsx, .xlsm, .xltx, .csv, .tsv) with zero format loss, with first-class support for Chinese /… |

## deepseek-harness

[deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) · MIT · ★ 265.7k · 32 here

DeepSeek Harness: Everything is a Plugin.

| Skill | What it does |
|---|---|
| [agent-experience](../skills/ai-platforms/deepseek-harness/agent-experience/) | Use when writing or changing a model-facing tool definition (name, description, parameter schema, or its system-prompt section), and when designing skills, context… |
| [cordis-composition-reference](../skills/ai-platforms/deepseek-harness/cordis-composition-reference/) | Use when writing or reading a Cordis bundle patch or agent preset for this harness and you need the Loader YAML dialect (insert, override by id, group, disabled… |
| [cordis-plugin-development](../skills/ai-platforms/deepseek-harness/cordis-plugin-development/) | Use when designing, reviewing, adding, enabling, disabling, installing, configuring, or debugging a plugin, bundle, feature, page, panel, tool, or MCP connection in the… |
| [cordis-styling-nitpicking](../skills/ai-platforms/deepseek-harness/cordis-styling-nitpicking/) | Use during code review of DeepSeek Harness Cordis plugins and helpers reachable from their entrypoints, including pull requests, and during focused lifecycle audits… |
| [diagnose-windows-sandbox-acl](../skills/ai-platforms/deepseek-harness/diagnose-windows-sandbox-acl/) | Use on Windows for unexpected DSH sandbox access denials: workspace writes or listing fail, or an ordinarily readable path cannot be read. One bundled command inspects… |
| [dsh-archive-agent-notes](../skills/ai-platforms/deepseek-harness/dsh-archive-agent-notes/) | Use when adding, auditing, pruning, archiving, restoring, or reviewing Agent Notes in deepseek-harness; checks every new note for superseded active records, deletes… |
| [dsh-ci-test-reliability](../skills/ai-platforms/deepseek-harness/dsh-ci-test-reliability/) | Design, review, and diagnose DeepSeek Harness tests and fixtures that can fail nondeterministically under CI concurrency, shared host resources, clocks, process-global… |
| [dsh-client-ui-ux](../skills/ai-platforms/deepseek-harness/dsh-client-ui-ux/) | Design and review DeepSeek Harness client UI changes — visual token discipline, reuse-before-adding, feedback surfaces (toast vs in-place notice vs empty state), overlay… |
| [dsh-code-review](../skills/ai-platforms/deepseek-harness/dsh-code-review/) | Use when reviewing a pull request in the deepseek-harness repo — orients the reviewer to this codebase's standards (AGENTS.md conventions, defensive patterns, ADRs… |
| [dsh-create-upgrade-guide](../skills/ai-platforms/deepseek-harness/dsh-create-upgrade-guide/) | Use when a deepseek-harness change breaks an externally perceptible surface (CLI, profiles, cordis.yml or settings keys, persisted user data, SDK or wire APIs, published… |
| [dsh-doc](../skills/ai-platforms/deepseek-harness/dsh-doc/) | Create, restructure, review, audit, or migrate DeepSeek Harness Markdown documentation, package READMEs, and the documentation website using audience-first hierarchy… |
| [dsh-error-handling](../skills/ai-platforms/deepseek-harness/dsh-error-handling/) | Apply error-handling principles when designing or reviewing failures, recovery, retries, background tasks, and user-visible error reports. |
| [dsh-find-simplifications](../skills/ai-platforms/deepseek-harness/dsh-find-simplifications/) | Find evidence-backed simplifications in DeepSeek Harness code, APIs, configuration, tests, and prose; write or consolidate proposals, identify small inline cleanups, or… |
| [dsh-merging-stacked-prs](../skills/ai-platforms/deepseek-harness/dsh-merging-stacked-prs/) | Use when landing a stack of dependent GitHub PRs (A ← B ← C, where each bases on the one below) onto master, merging a PR whose base is another open PR's branch, or… |
| [dsh-official-plugin-artwork](../skills/ai-platforms/deepseek-harness/dsh-official-plugin-artwork/) | Draw and review official DeepSeek Harness plugin icons and optional feature previews, including experimental plugins. Use for package artwork and PluginArtwork glyphs… |
| [dsh-pr-description](../skills/ai-platforms/deepseek-harness/dsh-pr-description/) | Use when creating a deepseek-harness pull request, or when updating its description after later changes or a handled review round. Defines each description section… |
| [dsh-pre-push-checks](../skills/ai-platforms/deepseek-harness/dsh-pre-push-checks/) | Use before pushing, force-pushing, marking ready for review, or claiming checks pass on a deepseek-harness branch, and immediately after gh stack sync publishes… |
| [dsh-prose-standard](../skills/ai-platforms/deepseek-harness/dsh-prose-standard/) | Use when writing, reviewing, restoring, trimming, or auditing prose in the deepseek-harness repo, including deciding where documentation or comments are required across… |
| [dsh-responsive-ui](../skills/ai-platforms/deepseek-harness/dsh-responsive-ui/) | Use when designing, implementing, or reviewing responsive client layouts, mobile and touch detection, text truncation, title wrapping, icon-only controls, mobile hover… |
| [dsh-session-projection](../skills/ai-platforms/deepseek-harness/dsh-session-projection/) | Use when creating, extending, or reviewing a DeepSeek Harness session projection, or migrating session-derived recovery state to one. |
| [dsh-speed-up-perf](../skills/ai-platforms/deepseek-harness/dsh-speed-up-perf/) | Use when investigating or optimizing DeepSeek Harness performance, designing realistic synthetic benchmarks or CI performance gates, profiling long Sessions or Web… |
| [dsh-translate-docs](../skills/ai-platforms/deepseek-harness/dsh-translate-docs/) | Manually run the extended DeepSeek Harness bilingual-document workflow, including generated briefings, delegated prose translation, whole-document translation, and… |
| [dsh-trim-cot-leakage](../skills/ai-platforms/deepseek-harness/dsh-trim-cot-leakage/) | Use when auditing or fixing prose that reads like a leaked reasoning transcript — dead design-session citations such as (decision N), audit item codes, or §N of… |
| [editing-cordis-compositions](../skills/ai-platforms/deepseek-harness/editing-cordis-compositions/) | Use when creating, changing, or validating an agent preset or other Cordis composition for this harness, including deciding host versus preset placement and checking… |
| [office](../skills/ai-platforms/deepseek-harness/office/) | Create, edit, inspect, or convert Office documents, spreadsheets, presentations, and PDFs. Load to choose the relevant workflow. |
| [office-docx](../skills/ai-platforms/deepseek-harness/office-docx/) | Create, read, edit, and validate Word documents (.docx). |
| [office-export-pdf](../skills/ai-platforms/deepseek-harness/office-export-pdf/) | Convert an Office document to a requested PDF with LibreOffice Kit. |
| [office-pptx](../skills/ai-platforms/deepseek-harness/office-pptx/) | Create, read, edit, and validate PowerPoint presentations (.pptx). |
| [office-recalculate](../skills/ai-platforms/deepseek-harness/office-recalculate/) | Refresh spreadsheet formula caches and verify calculated values with LibreOffice Kit. |
| [office-render](../skills/ai-platforms/deepseek-harness/office-render/) | Render requested document images or inspect visual layout with LibreOffice Kit. |
| [office-xlsx](../skills/ai-platforms/deepseek-harness/office-xlsx/) | Read, create, edit, and validate Excel workbooks, data, and formulas (.xlsx). |
| [record-browser-gif](../skills/ai-platforms/deepseek-harness/record-browser-gif/) | Record browser or Web UI interaction demos as optimized GIFs using the available browser-control workflow, optional Playwright Videos for higher capture frame rates, and… |

## OpenMAIC

[THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) · MIT · ★ 41.8k · 26 here

Open Multi-Agent Interactive Classroom — Get an immersive, multi-agent learning experience in just one click

| Skill | What it does |
|---|---|
| [build-personal-skill](../skills/ai-platforms/OpenMAIC/build-personal-skill/) | Evidence-based creation of a reusable personal course-making Skill from the user's own classroom and chat history. Use when the user asks to summarize, analyze, or learn… |
| [curriculum-planner](../skills/ai-platforms/OpenMAIC/curriculum-planner/) | Multi-stage series — a request for several classrooms that belong together, like 「7 天学 Python」, a four-week onboarding track, a semester unit split across lessons, or… |
| [deep-interactive](../skills/ai-platforms/OpenMAIC/deep-interactive/) | Deep Interactive courses. Plans the course so the learner manipulates something on most pages — simulations, diagrams they explore, code they run, games, 3D scenes —… |
| [deep-research](../skills/ai-platforms/OpenMAIC/deep-research/) | Courses whose content rests on current, external or real-world facts that must be verified against live sources before being taught — recent events, market or policy… |
| [fact-check](../skills/ai-platforms/OpenMAIC/fact-check/) | Improve factual reliability while creating or reviewing a course or supplied content. Use when the user asks to fact-check, verify accuracy, reduce hallucinations, make… |
| [feynman-learning](../skills/ai-platforms/OpenMAIC/feynman-learning/) | Turn any concept, lesson, slide deck, or source material into a Feynman learning cycle in which learners explain first, expose the smallest gap, rebuild the explanation… |
| [importer](../skills/ai-platforms/OpenMAIC/importer/) | — |
| [k12-core-literacy-planning](../skills/ai-platforms/OpenMAIC/k12-core-literacy-planning/) | Chinese K-12 core-literacy course design for a single OpenMAIC classroom. Use when a teacher asks for 中小学课程、核心素养、素养导向、2022 课标、真实情境、任务群、表现性评价, or wants a… |
| [learning-to-learn](../skills/ai-platforms/OpenMAIC/learning-to-learn/) | Infuse learning strategies and metacognition into a concept-centered OpenMAIC classroom as a parallel goal. Use when the user wants students to learn how to learn while… |
| [lecture-style](../skills/ai-platforms/OpenMAIC/lecture-style/) | Masterclass lecturing — one continuous explanation carried by slides, with dense pages, long narration that builds an argument across several real cases, and checkpoints… |
| [openmaic](../skills/ai-platforms/OpenMAIC/openmaic/) | OpenMAIC assistant for setting up, generating, and extending OpenMAIC. Use when the user wants to use OpenMAIC, generate a multi-agent interactive classroom, or build on… |
| [page-clone](../skills/ai-platforms/OpenMAIC/page-clone/) | Building one page that looks like a page the course already has — copy the model page with `duplicate_scene`, then rewrite the copy's words with one `patch_stage` op per… |
| [pptx-import](../skills/ai-platforms/OpenMAIC/pptx-import/) | 会话里有上传的 .pptx，且用户要把这份幻灯片填进一节已建的课（先 create_stage 建课，再 import_pptx 把页面追加进这节课堂，保留原版排版；课堂标题以 create_stage 为准，PPT 不接管）。随后逐页检查（有 render_scene_preview 就渲染看）并修 bad… |
| [pro-editing](../skills/ai-platforms/OpenMAIC/pro-editing/) | Professional editing of a course that already exists. Use when the user wants to revise, improve, restructure or polish pages the course already has — fix a page, tune a… |
| [slide-craft](../skills/ai-platforms/OpenMAIC/slide-craft/) | The design law of a slide page — canvas geometry, the text height table, the type scale, contrast pairs, spacing rhythm, and which element type carries which content… |
| [slide-dsl](../skills/ai-platforms/OpenMAIC/slide-dsl/) | The complete slide DSL manual — the canvas and its background, the ten element types field by field with units, defaults and legal values, where each type keeps its… |
| [social-emotional-learning](../skills/ai-platforms/OpenMAIC/social-emotional-learning/) | Infuse social-emotional learning (SEL) into a concept-centered OpenMAIC classroom as a parallel learning goal. Use when the user asks to add emotional awareness… |
| [spiral-curriculum](../skills/ai-platforms/OpenMAIC/spiral-curriculum/) | Design a multi-stage OpenMAIC course series around a small concept spine whose ideas return repeatedly at higher levels of complexity, abstraction, relationship density… |
| [stage-design](../skills/ai-platforms/OpenMAIC/stage-design/) | The baseline method for building ONE stage — a single classroom — with this runtime. Covers how the plan is settled in conversation, the order the generation tools are… |
| [stage-dsl](../skills/ai-platforms/OpenMAIC/stage-dsl/) | The map for reading and editing an OpenMAIC stage document with read_stage, patch_stage, and grep_stage. Load it before patching a structure you have not patched before… |
| [style-clone](../skills/ai-platforms/OpenMAIC/style-clone/) | Building a new course inside someone else's deck — import the deck as a library of layouts, then produce each page of the new course by copying the layout that fits it… |
| [teacher-style-clone](../skills/ai-platforms/OpenMAIC/teacher-style-clone/) | 工作台会话挂载了教师课堂录像/讲义材料时使用。 |
| [understanding-by-design](../skills/ai-platforms/OpenMAIC/understanding-by-design/) | Use Understanding by Design (UbD) to plan one OpenMAIC classroom or a course series around transferable conceptual understanding. Use when the user wants backward… |
| [vocational](../skills/ai-platforms/OpenMAIC/vocational/) | Vocational / technical training courses. Plans the course as a hands-on work task with an operation flow, tool and equipment state, safety boundaries and GO/STOP… |
| [workshop-style](../skills/ai-platforms/OpenMAIC/workshop-style/) | Hands-on workshop — the learner works through the course instead of watching it, with an exercise or a check every couple of pages, short slides that only set up the… |
| [zone-of-proximal-development](../skills/ai-platforms/OpenMAIC/zone-of-proximal-development/) | Design a coherent assessment-and-practice lesson using zone-of-proximal-development principles: independent diagnosis, targeted review, supported practice, fresh… |

## langflow

[langflow-ai/langflow](https://github.com/langflow-ai/langflow) · MIT · ★ 156.1k · 11 here

Langflow is a powerful tool for building and deploying AI-powered agents and workflows.

| Skill | What it does |
|---|---|
| [backend-code-review](../skills/ai-platforms/langflow/backend-code-review/) | Review backend code for quality, security, maintainability, and best practices based on established checklist rules. Use when the user requests a review, analysis, or… |
| [component-refactoring](../skills/ai-platforms/langflow/component-refactoring/) | Refactor high-complexity React components in Langflow frontend. Use when manual complexity assessment shows complexity > 50 or lineCount > 300, when the user asks for… |
| [e2e-testing](../skills/ai-platforms/langflow/e2e-testing/) | Write and review Playwright E2E tests for Langflow. Trigger when the user asks to write, fix, or review E2E tests, spec files, Playwright tests, or integration tests… |
| [frontend-code-review](../skills/ai-platforms/langflow/frontend-code-review/) | Review frontend code (.tsx, .ts, .js files) for quality, performance, and correctness against Langflow's frontend conventions. Supports pending-change reviews and… |
| [frontend-i18n](../skills/ai-platforms/langflow/frontend-i18n/) | Add, change, or review user-facing text in the Langflow frontend using the i18n system (i18next / react-i18next). Use whenever a change adds or edits UI strings —… |
| [frontend-query-mutation](../skills/ai-platforms/langflow/frontend-query-mutation/) | Guide for implementing Langflow frontend query and mutation patterns with Axios and TanStack React Query v5. Trigger when creating or updating API hooks in… |
| [frontend-testing](../skills/ai-platforms/langflow/frontend-testing/) | — |
| [ibm-a11y-level1-audit](../skills/ai-platforms/langflow/ibm-a11y-level1-audit/) | Perform a scoped IBM Equal Access Level 1 compliance audit of a chosen Langflow frontend surface (routes, components, or a PR) and produce a findings report mapped to… |
| [ibm-a11y-pr-remediation](../skills/ai-platforms/langflow/ibm-a11y-pr-remediation/) | Scan every frontend surface touched by the current PR/branch for IBM Equal Access Level 1 accessibility issues and fix all in-scope violations by default. Discovers… |
| [ibm-a11y-route-scan](../skills/ai-platforms/langflow/ibm-a11y-route-scan/) | Batch-scan Langflow frontend routes for accessibility issues using the Python IBM Equal Access scanner (scripts/a11y/a11y_scan.py) and produce JSON/Markdown/HTML… |
| [ibm-a11y-testing-guide](../skills/ai-platforms/langflow/ibm-a11y-testing-guide/) | Reference guide for writing and running Langflow frontend accessibility tests with axe (Jest) and IBM Equal Access (Playwright `page.runA11yScan`). Covers which… |

## OpenHands

[OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) · MIT · ★ 92.2k · 7 here, 1 linked

🙌 OpenHands: AI-Driven Development

| Skill | What it does |
|---|---|
| [desktop-electron](../skills/ai-platforms/OpenHands/desktop-electron/) | This skill should be used when the user asks to "change the desktop app", "package Electron", "build a universal macOS app", "bundle Node or uv", "fix Electron startup"… |
| [e2e-testing](../skills/ai-platforms/OpenHands/e2e-testing/) | This skill should be used when the user asks to "add an E2E test", "run live E2E", "run mock-LLM tests", "debug Playwright CI", "test the Docker image", or changes… |
| [frontend-api-contracts](../skills/ai-platforms/OpenHands/frontend-api-contracts/) | This skill should be used when the user asks to "add an API call", "change a backend", "update settings persistence", "change conversation events", "fix backend auth"… |
| [frontend-development](../skills/ai-platforms/OpenHands/frontend-development/) | This skill should be used when the user asks to "add UI copy", "add a translation", "optimize the frontend bundle", "change onboarding", "change conversation UI", "add a… |
| [local-stack-runtime](../skills/ai-platforms/OpenHands/local-stack-runtime/) | This skill should be used when the user asks to "change the dev stack", "add a runtime service", "change the launcher", "update Docker", "bump Agent Server", "change… |
| [pr-design-doc](../skills/ai-platforms/OpenHands/pr-design-doc/) | For a non-trivial pull request, write a self-contained HTML design doc under the temporary `.pr/` directory and link a visibility-appropriate preview in the PR… |
| [telemetry-analytics](../skills/ai-platforms/OpenHands/telemetry-analytics/) | This skill should be used when the user asks to "add tracking", "add a PostHog event", "change telemetry consent", "instrument onboarding", "debug analytics", or changes… |
| [verify-openhands ↗](https://github.com/OpenHands/OpenHands/tree/main/.agents/skills/verify-openhands) | This skill should be used to "verify OpenHands features", "test the Canvas UI like a user", "drive Agent Canvas", "check a UI change in the real app", "create or update… *(Too big to copy here (6 MB): install it from the source.)* |

## WeKnora

[Tencent/WeKnora](https://github.com/Tencent/WeKnora) · MIT · ★ 35.9k · 3 here

Open-source LLM knowledge platform: turn raw documents into a queryable RAG, an autonomous reasoning agent, and a self-maintaining Wiki.

| Skill | What it does |
|---|---|
| [pdf-processing](../skills/ai-platforms/WeKnora/pdf-processing/) | Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction. |
| [weknora-rag-search](../skills/ai-platforms/WeKnora/weknora-rag-search/) | Use when retrieving from or asking questions against a WeKnora knowledge base via the `weknora` CLI — and especially when unsure whether to use `chat`, `session ask`, or… |
| [weknora-shared](../skills/ai-platforms/WeKnora/weknora-shared/) | Use when driving a WeKnora RAG server through the `weknora` CLI as an agent — authenticating, managing knowledge bases / documents / sessions / agents, running search or… |

## PaddleOCR

[PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) · Apache-2.0 · ★ 91.9k · 2 here

Turn any PDF or image document into structured data for your AI. A powerful, lightweight OCR toolkit that bridges the gap between images/PDFs and LLMs. Supports 100+ languages.

| Skill | What it does |
|---|---|
| [paddleocr-doc-parsing](../skills/ai-platforms/PaddleOCR/paddleocr-doc-parsing/) | Use this skill to extract structured Markdown/JSON from PDFs and document images—tables with cell-level precision, formulas as LaTeX, figures, seals, charts… |
| [paddleocr-text-recognition](../skills/ai-platforms/PaddleOCR/paddleocr-text-recognition/) | Use this skill whenever the user wants text extracted from images, photos, scans, screenshots, or scanned PDFs. Returns exact machine-readable strings with line-level… |

## dspy

[stanfordnlp/dspy](https://github.com/stanfordnlp/dspy) · MIT · ★ 38.8k · 1 here

DSPy: The framework for programming—not prompting—language models

| Skill | What it does |
|---|---|
| [writing-release-notes](../skills/ai-platforms/dspy/writing-release-notes/) | Drafts DSPy release notes from maintainer-selected highlights and a verified, complete Git release range. Use when preparing or updating stable, beta, or… |
