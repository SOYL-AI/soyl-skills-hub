# OpenMontage

Skills from [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) at commit [`e01dbf4`](https://github.com/calesthio/OpenMontage/tree/e01dbf433f46eeb91d39bf905e194162921019a3), copied into SOYL Hub on 2026-10-29. Licence: AGPL-3.0.

> World's first open-source, agentic video production system. 12 production pipelines, 100+ tools, 700+ agent skill and production-knowledge files. Turn your AI coding assistant into a full video production studio.

All credit goes to the authors of calesthio/OpenMontage. Each folder is the upstream skill unchanged, with its licence file added when it had none; build caches and plugin manifests are left out.

| Skill | What it does | Licence |
|---|---|---|
| [3d-asset-generation](3d-asset-generation/) | Generate, reconstruct, inspect, and route production 3D assets for OpenMontage worlds using Atlas Cloud, fal.ai, licensed catalogs, and Blender. | AGPL-3.0 |
| [acestep](acestep/) | AI music generation with ACE-Step 1.5 — background music, vocal tracks, covers, stem extraction for video production. Use when generating music, soundtracks, jingles, or… | AGPL-3.0 |
| [agents](agents/) | Build voice AI agents with ElevenLabs. Use when creating voice assistants, customer service bots, interactive voice characters, or any real-time voice conversation… | MIT |
| [ai-video-gen](ai-video-gen/) | Generate AI videos from text prompts using multiple provider gateways. Use when: (1) Generating videos from text descriptions, (2) Creating AI-generated video clips for… | AGPL-3.0 |
| [atlas-cloud](atlas-cloud/) | Generate or edit images and videos through the Atlas Cloud gateway. Use for Atlas-hosted Seedance 2.5/2.0, Gemini Omni Flash, MiniMax H3, Seedream 5.0, GPT Image 2, Nano… | AGPL-3.0 |
| [avatar-video](avatar-video/) | Create AI avatar videos with precise control over avatars, voices, scripts, scenes, and backgrounds using HeyGen's v2 API. Use when: (1) Choosing a specific avatar and… | AGPL-3.0 |
| [azure-speech-to-text](azure-speech-to-text/) | Transcribe audio to text using Azure AI Speech (Fast Transcription REST API). Use when converting audio/video to text, generating subtitles, or processing spoken content… | MIT |
| [azure-text-to-speech](azure-text-to-speech/) | Generate neural narration audio using Azure AI Speech (REST text-to-speech). Use when synthesizing voiceovers or narration in OpenMontage. Optional cloud TTS provider —… | MIT |
| [beautiful-mermaid](beautiful-mermaid/) | Render Mermaid diagrams as SVG and PNG using the Beautiful Mermaid library. Use when the user asks to render a Mermaid diagram. | AGPL-3.0 |
| [bfl-api](bfl-api/) | BFL FLUX API integration guide covering endpoints, async polling patterns, rate limiting, error handling, webhooks, and regional endpoints with Python and TypeScript… | AGPL-3.0 |
| [canvas-procedural-animation](canvas-procedural-animation/) | Use p5.js/canvas for local procedural character effects: particles, weather, squash/stretch, walk cycles, and environmental motion. | MIT |
| [character-animation-qa](character-animation-qa/) | Review local character animation with schema checks, Playwright browser previews, frame sampling, and FFmpeg/ffprobe final output checks. | MIT |
| [character-rigging](character-rigging/) | Build data-driven 2D character rigs for local animation: parts, pivots, layers, constraints, views, and reusable rig packages. | MIT |
| [comfyui](comfyui/) | Use when working with ComfyUI workflows in OpenMontage, including comfyui_image/comfyui_video/comfyui_music, custom workflow_json/workflow_path inputs, output_node… | AGPL-3.0 |
| [create-video](create-video/) | Create videos from a text prompt using HeyGen's Video Agent. Use when: (1) Creating a video from a description or idea, (2) Generating explainer, demo, or marketing… | AGPL-3.0 |
| [d3-viz](d3-viz/) | Creating interactive data visualisations using d3.js. This skill should be used when creating custom charts, graphs, network diagrams, geographic visualisations, or any… | AGPL-3.0 |
| [dashscope](dashscope/) | DashScope (Alibaba Cloud Bailian / 阿里云百炼) integration — image generation (qwen-image-2.0-pro), text-to-speech (qwen3-tts-flash), and ASR with word-level timestamps… | AGPL-3.0 |
| [doubao-tts](doubao-tts/) | Generate Mandarin and multilingual narration with Volcengine Doubao Speech 2.0. Use when creating Chinese voiceovers, when the user prefers Doubao/Volcengine/火山引擎/豆包… | AGPL-3.0 |
| [elevenlabs](elevenlabs/) | Generate AI voiceovers, sound effects, and music using ElevenLabs APIs. Use when creating audio content for videos, podcasts, or games. Triggers include generating… | AGPL-3.0 |
| [faceswap](faceswap/) | Swap faces in a video using AI via the HeyGen API. Use when: (1) Replacing a face in a video with another face, (2) Face swapping from a source image onto a target… | AGPL-3.0 |
| [ffmpeg](ffmpeg/) | Video and audio processing with FFmpeg. Use for format conversion, resizing, compression, audio extraction, and preparing assets for Remotion. Triggers include… | AGPL-3.0 |
| [fish-audio-tts](fish-audio-tts/) | Generate expressive, multilingual narration with fish.audio (S1 / S2-generation models) and reuse cloned voices via reference_id. Use when the user prefers… | AGPL-3.0 |
| [flux-best-practices](flux-best-practices/) | Comprehensive guide for BFL FLUX image generation models. Covers prompting, T2I, I2I, structured JSON, hex colors, typography, multi-reference editing, and… | AGPL-3.0 |
| [framer-motion](framer-motion/) | Use when implementing Disney's 12 animation principles with Framer Motion in React applications | AGPL-3.0 |
| [gemini-omni](gemini-omni/) | Generate and conversationally edit short videos with stable Google Gemini Omni Flash (`gemini-omni-1.1-flash`). Use when: (1) iterating on a clip with natural-language… | AGPL-3.0 |
| [grok-media](grok-media/) | xAI Grok image and video generation guide covering authentication, endpoints, prompt structure, image editing, reference-image video, and async polling. | AGPL-3.0 |
| [gsap-frameworks](gsap-frameworks/) | Official GSAP skill for Vue, Svelte, and other non-React frameworks — lifecycle, scoping selectors, cleanup on unmount. Use when the user wants animation in Vue, Nuxt… | MIT |
| [gsap-plugins](gsap-plugins/) | Official GSAP skill for GSAP plugins — registration, ScrollToPlugin, ScrollSmoother, Flip, Draggable, Inertia, Observer, SplitText, ScrambleText, SVG and physics… | MIT |
| [heygen](heygen/) | [DEPRECATED] Use `create-video` for prompt-based video generation or `avatar-video` for precise avatar/scene control. This legacy skill combines both workflows — the… | AGPL-3.0 |
| [hyperframes](hyperframes/) | READ THIS FIRST for any request to make, create, edit, animate, or render a video, animation, or motion graphic — a promo, explainer, captioned clip, title card… | AGPL-3.0 |
| [hyperframes-cli](hyperframes-cli/) | HyperFrames CLI dev loop. Use when running npx hyperframes init, add, catalog, capture, lint, validate, inspect, layout, snapshot, preview, play, render, publish… | AGPL-3.0 |
| [hyperframes-core](hyperframes-core/) | The HyperFrames composition contract — build one renderable project. Use for composition structure, the `data-*` timing attributes, `class="clip"`, tracks… | AGPL-3.0 |
| [hyperframes-creative](hyperframes-creative/) | Non-animation creative direction for HyperFrames videos. Use for design spec (frame.md / design.md) handling, palettes, typography, narration, beat planning… | AGPL-3.0 |
| [hyperframes-media](hyperframes-media/) | Audio and media assets for HyperFrames compositions, produced by one shared audio engine (`scripts/audio.mjs`) — multi-provider TTS (HeyGen / ElevenLabs / Kokoro local)… | AGPL-3.0 |
| [hyperframes-registry](hyperframes-registry/) | Install and wire registry blocks and components into HyperFrames compositions. Use when running hyperframes add, installing a block or component, wiring an installed… | AGPL-3.0 |
| [kling-official](kling-official/) | Official Kling direct API guidance for OpenMontage providers. Use before calling `kling_official_video`, `kling_official_image`, `kling_tts`, `kling_avatar`, or… | AGPL-3.0 |
| [lottie-bodymovin](lottie-bodymovin/) | Use when implementing Disney's 12 animation principles with Lottie animations exported from After Effects | AGPL-3.0 |
| [ltx2](ltx2/) | AI video generation with LTX-2.3 22B — text-to-video, image-to-video clips for video production. Use when generating video clips, animating images, creating b-roll… | AGPL-3.0 |
| [lyria](lyria/) | Generate and validate music with Google Lyria 3 through the Gemini Interactions API. Use before calling OpenMontage `google_music`, designing Lyria 3 Clip or Pro… | AGPL-3.0 |
| [manim-composer](manim-composer/) | Trigger when: (1) User wants to create an educational/explainer video, (2) User has a vague concept they want visualized, (3) User mentions "3b1b style" or "explain like… | AGPL-3.0 |
| [manimce-best-practices](manimce-best-practices/) | Trigger when: (1) User mentions "manim" or "Manim Community" or "ManimCE", (2) Code contains `from manim import *`, (3) User runs `manim` CLI commands, (4) Working with… | MIT |
| [media-use](media-use/) | Agent Media OS — resolve any media need (BGM, SFX, image, icon) into a frozen local file + ledger record. One verb (`resolve`) handles the full cascade — project cache… | AGPL-3.0 |
| [minimax-h3](minimax-h3/) | Generate MiniMax H3 (Hailuo 3.0) video through the official MiniMax v2 API, fal.ai, Runway, ComfyUI Partner Nodes, or local open weights in ComfyUI. Use for 4-15 second… | AGPL-3.0 |
| [motion-graphics](motion-graphics/) | Use when the user wants a short, design-led motion graphic where motion is the message: kinetic typography, stat or number count-up, chart/data-viz hit, logo sting… | AGPL-3.0 |
| [music](music/) | Generate music using ElevenLabs Music API. Use when creating instrumental tracks, songs with lyrics, background music, jingles, or any AI-generated music composition… | MIT |
| [playwright-recording](playwright-recording/) | Record browser interactions as video using Playwright. Use for capturing demo videos, app walkthroughs, and UI flows for Remotion videos. Triggers include recording a… | AGPL-3.0 |
| [pose-library-design](pose-library-design/) | Design reusable 2D character pose libraries, action cycles, and expression states for data-driven animation. | MIT |
| [provider-model-refresh](provider-model-refresh/) | Use the September 2026 image, video, speech and Avatar V adapters with explicit model/host contracts. | AGPL-3.0 |
| [provider-refresh-oct23](provider-refresh-oct23/) | API contracts and production routing for the October 23, 2026 provider refresh. | AGPL-3.0 |
| [remotion](remotion/) | Toolkit-specific Remotion patterns — custom transitions, shared components, and project conventions. For core Remotion framework knowledge (hooks, animations, rendering… | AGPL-3.0 |
| [remotion-best-practices](remotion-best-practices/) | Best practices for Remotion - Video creation in React | AGPL-3.0 |
| [remotion-to-hyperframes](remotion-to-hyperframes/) | Port an existing Remotion (React) composition to HyperFrames HTML. Use ONLY when the user explicitly asks to port/convert/migrate/translate a Remotion source. Do NOT… | AGPL-3.0 |
| [seedance-2-0](seedance-2-0/) | Generate cinematic clips with ByteDance Seedance 2.0 — the preferred premium video model in OpenMontage when a paid gateway is configured. Use when: (1) producing… | AGPL-3.0 |
| [seedance-2-5](seedance-2-5/) | Generate 4-30 second cinematic video with ByteDance Seedance 2.5 through fal.ai, Volcengine Ark, Runway, or ComfyUI Partner Nodes. Use for long single generations… | AGPL-3.0 |
| [setup-api-key](setup-api-key/) | Guides users through setting up an ElevenLabs API key for ElevenLabs MCP tools. Use when the user needs to configure an ElevenLabs API key, when ElevenLabs tools fail… | MIT |
| [sound-effects](sound-effects/) | Generate sound effects from text descriptions using ElevenLabs. Use when creating sound effects, generating audio textures, producing ambient sounds, cinematic impacts… | MIT |
| [speech-to-text](speech-to-text/) | Transcribe audio to text using ElevenLabs Scribe v2. Use when converting audio/video to text, generating subtitles, transcribing meetings, or processing spoken content. | MIT |
| [svg-character-animation](svg-character-animation/) | Animate SVG character rigs with GSAP, CSS transforms, Remotion frame control, and HyperFrames-compatible browser previews. | MIT |
| [synthetic-screen-recording](synthetic-screen-recording/) | Synthetic terminal-style screen recording guidance for Remotion `TerminalScene`. | MIT |
| [tailwind-design-system](tailwind-design-system/) | Build scalable design systems with Tailwind CSS v4, design tokens, component libraries, and responsive patterns. Use when creating component libraries, implementing… | AGPL-3.0 |
| [text-to-speech](text-to-speech/) | HeyGen native Voice1 and catalog speech, voice discovery, timestamps, and streaming. | AGPL-3.0 |
| [threejs-world-generation](threejs-world-generation/) | Build deterministic, editable, free-viewpoint Three.js worlds from text or structured briefs. Use for cinematic 3D terrain, semantic regions, procedural biomes, explicit… | AGPL-3.0 |
| [vercel-composition-patterns](vercel-composition-patterns/) | React composition patterns that scale. Use when refactoring components with boolean prop proliferation, building flexible component libraries, or designing reusable… | MIT |
| [vercel-react-best-practices](vercel-react-best-practices/) | React and Next.js performance optimization guidelines from Vercel Engineering. This skill should be used when writing, reviewing, or refactoring React/Next.js code to… | MIT |
| [video-download](video-download/) | Download video and audio from YouTube and 1000+ sites using yt-dlp. No API keys needed. Use when: (1) Downloading a video from YouTube or other sites, (2) Extracting… | AGPL-3.0 |
| [video-edit](video-edit/) | Edit videos locally using ffmpeg. Trim, concat, resize, speed, overlay, extract audio, compress, and convert. Use when: (1) Trimming or cutting video segments, (2)… | AGPL-3.0 |
| [video-toolkit](video-toolkit/) | Create professional videos autonomously using claude-code-video-toolkit — AI voiceovers, image generation, music, talking heads, and Remotion rendering. | AGPL-3.0 |
| [video-translate](video-translate/) | Translate and dub existing videos into multiple languages using HeyGen. Use when: (1) Translating a video into another language, (2) Dubbing video content with lip-sync… | AGPL-3.0 |
| [video-understand](video-understand/) | Understand video content locally using ffmpeg frame extraction and Whisper transcription. No API keys needed. Use when: (1) Understanding what a video contains, (2)… | AGPL-3.0 |
| [visual-style](visual-style/) | Create, extract, and apply portable visual design systems via visual-style.md files. Use when: (1) Creating a visual-style.md design system from scratch, (2) Extracting… | AGPL-3.0 |
| [website-to-video](website-to-video/) | Capture a general website/URL and turn it into a HyperFrames video (site tour, showcase, or social clip from the site's own visuals). Uses headless Chrome screenshots +… | AGPL-3.0 |

Install one with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/SOYL-AI/soyl-skills-hub/tree/main/skills/video-and-motion/OpenMontage/3d-asset-generation -g -a claude-code
```

Back to [Video and motion](../../../catalog/video-and-motion.md)
