# OpenChatCut

Skills from [0xsline/OpenChatCut](https://github.com/0xsline/OpenChatCut) at commit [`7fa4b79`](https://github.com/0xsline/OpenChatCut/tree/7fa4b7903e7ebecf832a36249f0c0c755200cc17), copied into SOYL Hub on 2026-10-29. Licence: AGPL-3.0.

> Open-source, local-first conversational AI video editor with a professional multi-track timeline, Agent Skills, MCP integration, and Remotion rendering.

All credit goes to the authors of 0xsline/OpenChatCut. Each folder is the upstream skill unchanged, with its licence file added when it had none; build caches and plugin manifests are left out.

| Skill | What it does | Licence |
|---|---|---|
| [ai-cinematic-short-film](ai-cinematic-short-film/) | Plan AI short films with story, shots, prompts, and continuity. | AGPL-3.0 |
| [asset-import](asset-import/) | Use when acquiring or importing media into a OpenChatCut project asset library for video editing or creation, including local/attached videos, user-provided paths… | AGPL-3.0 |
| [batch-montage-variants](batch-montage-variants/) | Turn one pool of existing project media into a batch of distinct, publishable montage cuts instead of a single hero edit. Use for batch montage, one-source-many-outputs… | AGPL-3.0 |
| [beat-sync-montage](beat-sync-montage/) | Plan and build a finished beat-synced montage where cut placement serves the content, not just the metronome. Use for 卡点混剪, 卡点剪辑, 踩点视频, beat-sync montage, rhythm edit… | AGPL-3.0 |
| [create-motion-graphics](create-motion-graphics/) | Use whenever the agent needs to add, create, hand-author, patch, or place Motion Graphic JSX assets in a OpenChatCut project. This is the direct-authoring path: use… | AGPL-3.0 |
| [ecommerce-product-montage](ecommerce-product-montage/) | Assemble product footage, UGC, and b-roll into a conversion-oriented montage with a hook → pain → demo → proof → CTA rhythm. Use for 带货混剪, 产品混剪, 商品短视频, 种草视频, ecommerce… | AGPL-3.0 |
| [explainer-video](explainer-video/) | Create finished explainer videos from a topic, script, outline, voiceover, product logic, data, technical concept, course material, or reference assets. Use when the… | AGPL-3.0 |
| [export](export/) | Use when a OpenChatCut video editing or creation workflow needs export, render, download, share, final delivery, subtitle-file export, render choice, local-only asset… | AGPL-3.0 |
| [image-gen](image-gen/) | AI image generation via Fal.ai, gpt-image-2, nano-banana, MiniMax image-01, and xAI Grok Imagine. Use when the user wants to generate or create an image / picture /… | AGPL-3.0 |
| [known-errors](known-errors/) | Use when a OpenChatCut tool call fails or returns an unexpected shape. | AGPL-3.0 |
| [livestream-to-clips](livestream-to-clips/) | Cut an imported livestream recording of any genre into evidence-backed, platform-ready clips by combining transcript, visual, audio, interaction, and domain-specific… | AGPL-3.0 |
| [long-video-to-shorts](long-video-to-shorts/) | Cut one long podcast, interview, course, livestream, or other source video into social-ready shorts, reels, highlights, or clip timelines from existing project media… | AGPL-3.0 |
| [motion-graphic-placement](motion-graphic-placement/) | Add motion graphics at the right moments without blocking the story. Use when the user wants to enhance talking-head, lecture, tutorial, interview, podcast, or creator… | AGPL-3.0 |
| [multi-clips-to-reels](multi-clips-to-reels/) | Turn multiple product shots, event footage, travel clips, gameplay moments, UGC/product footage, B-roll, or mixed media into social-ready reels, highlights, recaps, or… | AGPL-3.0 |
| [music](music/) | Music generation via Mureka, MiniMax, Atlas Cloud, and Sonilo. Use for instrumentals, songs, soundtracks, track/stem generation, covers, or video-conditioned scoring of… | AGPL-3.0 |
| [music-intelligence](music-intelligence/) | Run or inspect local music analysis and plan or apply beat-, downbeat-, or section-synced video cuts or photo placements. Use for BGM beat edits, rhythm cuts, 卡点剪辑… | AGPL-3.0 |
| [news-rough-cut](news-rough-cut/) | 新闻素材智能粗剪——把新闻素材粗剪为一条内容完整、逻辑清晰、节奏紧凑的新闻短视频。Use when the user asks to 粗剪新闻、新闻剪辑、把新闻素材剪成短视频、智能粗剪、news rough cut、编辑新闻视频, or provides news footage (发布会/采访/现场/监控素材) to be cut… | AGPL-3.0 |
| [openchatcut](openchatcut/) | Connect an MCP-capable coding agent to OpenChatCut and edit local video projects. Use when the user asks to install, connect, or set up OpenChatCut; inspect or edit an… | AGPL-3.0 |
| [openchatcut-plugin-basics](openchatcut-plugin-basics/) | Use for video editing or video creation work that should be editable in OpenChatCut, even when the user does not explicitly mention OpenChatCut. Covers local/attached… | AGPL-3.0 |
| [product-ad-video-script](product-ad-video-script/) | Turn a product into ad angles, hooks, scenes, and CTA. | AGPL-3.0 |
| [product-help](product-help/) | OpenChatCut product knowledge — UI layout, editor features, and how generation providers are configured. Use when the user asks about the product interface, how to use a… | AGPL-3.0 |
| [shader-gen](shader-gen/) | AI shader generator for WebGL video effects, transitions, masks, and color grading (LUT / 调色 / 电影感 / film look). Use when the user wants a video effect (滤镜 / 特效), a… | AGPL-3.0 |
| [skill-creator](skill-creator/) | Create or improve OpenChatCut custom skills. Use whenever the user asks to create a skill, capture a workflow as a skill, write a SKILL.md, add a reusable workflow… | AGPL-3.0 |
| [storyboard-shot-breakdown](storyboard-shot-breakdown/) | Break down each shot and turn the analysis into a storyboard reference. Use when the user wants shot-by-shot film analysis, director logic, cinematography breakdown, or… | AGPL-3.0 |
| [talking-head-guide](talking-head-guide/) | Guide for editing videos where the primary content is people talking — talking-head / 口播, interview / 访谈, lecture, tutorial, podcast, course content, and similar… | AGPL-3.0 |
| [transcription](transcription/) | Use when a video/audio task needs OpenChatCut transcription, captions, subtitles, subtitle styling, transcript search, transcript readiness checks, or enabling captions… | AGPL-3.0 |
| [verification](verification/) | Use when checking whether agent edits are reflected in the OpenChatCut project and editor. | AGPL-3.0 |
| [video-gen](video-gen/) | AI video generation via Fal.ai, Seedance 2.0, Kling, MiniMax Hailuo, xAI Grok Imagine, and OFox. Use when the user wants to generate a video clip — text-to-video… | AGPL-3.0 |
| [video-thumbnail-generator](video-thumbnail-generator/) | Create platform-ready thumbnails from real video frames. Use when the user wants a thumbnail, cover image, YouTube cover, Shorts cover, Bilibili cover, Xiaohongshu… | AGPL-3.0 |
| [voice](voice/) | Text-to-Speech (TTS), voiceover, narration placement/sync, and custom sound effects (SFX) generator. Use when the user wants generated speech from text, wants to… | AGPL-3.0 |
| [widget-forms](widget-forms/) | Use when the agent should ask the user for structured input with an in-chat form, including single-select, multi-select, text fields, style pickers, or voice audition… | AGPL-3.0 |

Install one with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/SOYL-AI/soyl-skills-hub/tree/main/skills/video-and-motion/OpenChatCut/ai-cinematic-short-film -g -a claude-code
```

Back to [Video and motion](../../../catalog/video-and-motion.md)
