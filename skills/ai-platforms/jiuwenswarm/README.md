# jiuwenswarm

Skills from [openJiuwen-ai/jiuwenswarm](https://github.com/openJiuwen-ai/jiuwenswarm) at commit [`fd8f735`](https://github.com/openJiuwen-ai/jiuwenswarm/tree/fd8f735c9fcb9b08657632fece07858be6ca4dc1), copied into SOYL Hub on 2026-10-29. Licence: Apache-2.0.

> JiuwenSwarm is an intelligent AI Agent built on openJiuwen. It extends the powerful capabilities of large language models directly to your fingertips through various communication apps you use daily.

All credit goes to the authors of openJiuwen-ai/jiuwenswarm. Each folder is the upstream skill unchanged, with its licence file added when it had none; build caches and plugin manifests are left out.

| Skill | What it does | Licence |
|---|---|---|
| [advanced-daily-report](advanced-daily-report/) | 进阶版日报生成器，支持多数据源采集、工作分析、趋势对比、周报月报聚合 | Apache-2.0 |
| [aet-req-analysis](aet-req-analysis/) | Requirements analysis skill - transforms raw requirements into structured specifications through Socratic dialogue, behavior analysis, and requirement specification… | Apache-2.0 |
| [aet-req-design](aet-req-design/) | Requirements design skill - transforms requirements analysis specifications into implementable system design specifications through architecture design, module change… | Apache-2.0 |
| [aet-req-review](aet-req-review/) | Gate pipeline for requirement deliverables — enforces automated quality gates and interactive user validation before handover. Trigger when: (1) structured PRD/spec/SDD… | Apache-2.0 |
| [agent-creator](agent-creator/) | Agent 模板包的创建与更新器：从自然语言创建可被 JiuwenSwarm 加载的 agent 模板包，或在同一流程的 update mode 下修改已有自定义专家。 触发词：创建 agent模板包、创建模板包、生成 agent 模板、新建 agent、做一个 agent、create agent… | Apache-2.0 |
| [agent-group-creator](agent-group-creator/) | 从自然语言创建可被 JiuwenSwarm 加载和安装的专家团（agent_group）包，包含 Leader、专家成员、协作指令及可选共享技能。用户提出“创建专家团”“组建专家团队”“做一个多专家协作团队”时使用；创建单个专家使用 agent-creator，执行已有专家团的业务任务不使用本技能。 | Apache-2.0 |
| [akg-agents](akg-agents/) | 代理执行 AKG 算子任务。先检查固定仓库与分支；若 `~/.akg/check_env.md` 不存在则强制 `FULL_SETUP=true`；忽略所有 `akg_cli` 检查和使用；后端代码生成直接执行 `run_workflow.py --workflow kernelgen`。 | Apache-2.0 |
| [ascend-moe-optimizer-auto-trace](ascend-moe-optimizer-auto-trace/) | 为昇腾算子在源码中接入 TRACE_POINT 与 MoeTracing，串通 trace_preprocessor、profiling tensor、point_map.json、 save_profiling_data 与 trace_collector 生成 Chrome trace。强调门禁 G1–G5：全链路预处理与… | Apache-2.0 |
| [ascend-moe-optimizer-trace-analyzer](ascend-moe-optimizer-trace-analyzer/) | 在用户提供 Chrome/Perfetto trace.json、或排查 Ascend 上 MoE/FusedDeepMoe 等算子性能时使用。按 phase、category、core group、tid 统计耗时、overlap、bubble，输出 CSV、Markdown 报告与确定性诊断；可选外部 LLM 扩写分析。默认… | Apache-2.0 |
| [baidu-netdisk-guide](baidu-netdisk-guide/) | 百度网盘官方 MCP Server 使用指引：文件浏览与检索、文件管理、分享链接、容量查询、内容保存的工具选择策略与写操作安全规则。当用户要求操作百度网盘（查容量、找文件、浏览整理文件、生成分享链接、保存文本或 URL 到网盘）时使用。 | Apache-2.0 |
| [baoyu-image-gen](baoyu-image-gen/) | AI image generation with OpenAI GPT Image 2, Azure OpenAI, Google, OpenRouter, DashScope, Z.AI GLM-Image, MiniMax, Jimeng, Seedream, Replicate and Agnes APIs. Supports… | Apache-2.0 |
| [brief](brief/) | Turn a user request into an executable design brief. Use when writing the outline, logline, visual style, subjects, setting, duration, audio policy, or the timed clip… | Apache-2.0 |
| [character](character/) | Produce one locked character identity plate for later video reference. Use when designing a character sheet, costume, face, or the character1 binding order. | Apache-2.0 |
| [clip](clip/) | Generate one reference-to-video shot from locked character and scene plates. Use when producing a single storyboard row as a short video clip. | Apache-2.0 |
| [compose](compose/) | Stitch finished shots into one film and mix audio by policy. Use when assembling the timeline, normalizing resolution, or ducking music under speech. | Apache-2.0 |
| [computer-use-macos](computer-use-macos/) | Operate macOS application UI through computer_use MCP and the Computer → App → Element SDK. Use when observing, clicking, or typing on a macOS MCP host, including a… | Apache-2.0 |
| [computer-use-windows](computer-use-windows/) | Operate Windows application UI through computer_use MCP and the Computer → App → Element SDK. Use when observing, clicking, or typing on a Windows MCP host, including a… | Apache-2.0 |
| [cross-channel-history-retrieval](cross-channel-history-retrieval/) | 跨会话检索聊天原文（记忆不足时再用）。在回答任何关于历史事件、日期、人物、过去对话的问题时，如果记忆中没有相关信息或不足以回答，则需要使用跨会话检索聊天原文。用 mcp_exec_command 执行 scripts/search_history.py，读… | Apache-2.0 |
| [deepep-to-cam-converter](deepep-to-cam-converter/) | 识别代码中可替换为CAM算子的DeepEP算子，基于实际运行参数校验约束，自动完成通信域转换（NCCL->HCCL）、设备适配（CUDA->NPU）及算子替换。 | Apache-2.0 |
| [delayed-restart-app](delayed-restart-app/) | 安排延迟重启本 Agent 所在的服务（JiuwenSwarm app）。执行后当前 Agent 进程会被终止并重新启动，当前会话会断开。用于用户要求重启、配置更新需生效、或服务异常需重载时。使用 bash 调用脚本。 | Apache-2.0 |
| [doc-update](doc-update/) | 以源码为唯一事实来源，系统性核对并更新项目文档，确保内容与实现一致、多语言文档 1:1 对齐、结构完整。 | Apache-2.0 |
| [docx-pro](docx-pro/) | Professional Word (.docx) document generation, faithful text replacement, Markdown round-trip conversion, document inspection, TOC insertion and watermarking. Use when… | Apache-2.0 |
| [dynamic-memory-cli](dynamic-memory-cli/) | Operate a dynamic, UT-backed agent memory with atomic Pending publication, merged Pending/Built search, Memory Snapshot and history cursor state, Built-only validation… | Apache-2.0 |
| [financial-document-parser](financial-document-parser/) | Extract and analyze data from invoices, receipts, bank statements, and financial documents. Categorize expenses, track recurring charges, and generate expense reports… | Apache-2.0 |
| [gitcode-api](gitcode-api/) | 使用 gitcode-api 命令行工具访问 GitCode REST API。适用于需要查询仓库、Issue、Pull Request、文件内容、用户、组织、搜索结果，或需要获取 Issue 与 Pull Request 模版的场景。还可用于总结仓库最近 commit / PR / issue、责任人、模块、风险或对外接口影响。 | Apache-2.0 |
| [harmonyos-dev-suite](harmonyos-dev-suite/) | Unified HarmonyOS development entry skill for ArkTS, ArkUI, DevEco CLI, build/run/debug, device logs, testing, multi-device adaptation, atomic services, native… | Apache-2.0 |
| [huawei-cloud-maas-setup](huawei-cloud-maas-setup/) | 引导用户完成华为云 MaaS 服务购买和 API 配置。脚本自动完成授权更新、API Key 创建、模型开通；用户只需完成登录、充值、选择要开通的模型。整个流程预计 3-5 分钟。 适用于首次运行配置、华为云 MaaS 服务开通、API 凭证获取、模型服务配置等场景。 当用户提到华为云、MaaS、Maas、开通模型服务、配置… | Apache-2.0 |
| [jiuwenswarm-pr-review](jiuwenswarm-pr-review/) | Review a specified JiuwenSwarm pull request against the repository's technical direction, architecture, feature interactions, documentation, scope, code quality, reuse… | Apache-2.0 |
| [llm-wiki](llm-wiki/) | Build and maintain a persistent knowledge base (LLM Wiki) using native backend tools. Supports ingesting PDFs, Markdown, and TXT files, and querying or linting the data… | Apache-2.0 |
| [local-doc-ocr](local-doc-ocr/) | 本地离线 OCR——将扫描件 PDF/图片提取为文字。双引擎：(A) RapidOCR 纯本地离线一键出 .md（默认保底、不联网、不占 token、可批量）；(B) 支持多模态读图能力的 Agent 逐页读图（高质量，擅长表格/手写/印章，如 WorkBuddy 的 Read… | MIT |
| [openJiuwen-DeepSearch](openjiuwen-deepsearch/) | 知识增强型深度检索与深度研究，支持查询规划、信息收集、理解反思、研究报告生成等多 Agent 协同。使用场景：金融分析研报、学术与政策研究、企业级深度搜索等复杂推理任务，可以生成Markdown、Doc和Html格式的研究报告。**每次使用该技能之前都先完整阅读一遍SKILL.md学习技能。** | Apache-2.0 |
| [pdf-extraction](pdf-extraction/) | Extract text, tables, and metadata from PDFs using pdfplumber | MIT |
| [plugin-creator](plugin-creator/) | Plugin 插件包的创建与更新器：从自然语言创建可被 JiuwenSwarm 加载的 plugin 插件包，或在同一流程的 update mode 下修改已有自定义插件。 触发词：创建插件、创建 plugin、做一个插件、plugin 脚手架、修改插件、编辑插件、更新插件、调整插件、create plugin… | Apache-2.0 |
| [ppt-creation](ppt-creation/) | 当任务要求创建、读取、解析、提取、编辑、修改、合并、拆分、转换或检查 PPT / 幻灯片 / 演示文稿 / deck / slides / presentation / .pptx 文件时使用。本 skill 以内置模板为版面底座，让 Agent 在内容区自由设计；支持原生 PptxGenJS… | Apache-2.0 |
| [pptx-generator](pptx-generator/) | Generate, edit, and read PowerPoint presentations. Create from scratch with PptxGenJS (cover, TOC, content, section divider, summary slides), edit existing PPTX via XML… | MIT |
| [project-maintainer](project-maintainer/) | Use when initializing or updating structured in-repository project-maintenance docs; exploring existing code; analyzing a full project or repository; documenting… | Apache-2.0 |
| [rsi-program-dataset-creator](rsi-program-dataset-creator/) | Use for program evolution — improving a working program by repeated search against a measured score, rather than by one edit. Covers both halves: deciding what is… | Apache-2.0 |
| [scene](scene/) | Produce one empty scene plate for later video reference. Use when designing a setting, its geography, weather, lighting, or props. | Apache-2.0 |
| [skill-creator](skill-creator/) | Unified entry point for all Skill creators. Routes skill creation and editing requests to the correct specialized creator. Use whenever the user wants to create a new… | Apache-2.0 |
| [skill-creator-normal](skill-creator-normal/) | Create new single-agent skills, modify and improve existing single-agent skills, and measure skill performance. Use when users want to create a skill from scratch, edit… | Apache-2.0 |
| [skill-gen-4-enterprise-doc](skill-gen-4-enterprise-doc/) | Turn SOPs, URLs, or stated intent into an installed skill package. Use when the user asks to generate a skill from a document, link, or workflow. Follow SKILL.md… | Apache-2.0 |
| [skill-omni-creation](skill-omni-creation/) | 当用户说「从这个链接/URL生成skill」「把这个网页/教程做成skill」「从这个视频提取步骤」时触发。先读取此 SKILL.md，再按步骤调用 scripts/ 下的 Python 脚本完成：爬取网页或下载视频 → 下载图片/抽帧 → 生成标准 Skill Markdown… | Apache-2.0 |
| [skvm-general](skvm-general/) | Drive the skvm CLI on behalf of a user to profile models, AOT-compile skills, run skill-assisted tasks, run benchmarks, and manage compiled proposals. Trigger when the… | Apache-2.0 |
| [skvm-jit](skvm-jit/) | Trigger `skvm jit-optimize` with post-task evidence so it generates a reviewable optimization proposal for a skill. Use after finishing a task that was driven by any… | Apache-2.0 |
| [storyboard](storyboard/) | Turn a brief into a one-row-per-shot storyboard table. Use when planning shot size, camera move, action, scene changes, or the prompt for a clip. | Apache-2.0 |
| [swarmskill-creator](swarmskill-creator/) | Creates, converts, or modifies Swarm Skills — the multi-role (多角色团队) extension of the Skills standard, optionally with an executable SwarmFlow orchestration script. Use… | Apache-2.0 |
| [wan-reference-video](wan-reference-video/) | Best practices for Alibaba Wan reference-to-video (R2V) prompts and reference_images attach order. Use when authoring Design clip prompts, binding character1… / Scene N… | Apache-2.0 |
| [xlsx](xlsx/) | Open, create, read, analyze, edit, repair, or validate spreadsheet files (.xlsx, .xlsm, .xltx, .csv, .tsv) with zero format loss, with first-class support for Chinese /… | MIT |

Install one with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/SOYL-AI/soyl-skills-hub/tree/main/skills/ai-platforms/jiuwenswarm/advanced-daily-report -g -a claude-code
```

Back to [AI platforms](../../../catalog/ai-platforms.md)
