# reelmimic

Skills from [edenfunf/reelmimic](https://github.com/edenfunf/reelmimic) at commit [`d445b23`](https://github.com/edenfunf/reelmimic/tree/d445b23f404dc6f577b8fdff50255fdbf85d1e97), copied into SOYL Hub on 2026-10-29. Licence: MIT.

> Show it a video you love. Get a new video in the same style. An AI crew (Claude Code or Codex) plans, builds and reviews it with you.

All credit goes to the authors of edenfunf/reelmimic. Each folder is the upstream skill unchanged, with its licence file added when it had none; build caches and plugin manifests are left out.

| Skill | What it does | Licence |
|---|---|---|
| [anime-cel](anime-cel/) | Make Japanese TV-anime style videos (MP4) with code — cel-shaded characters with tapered line art, big detailed eyes, hair clumps with a specular band, comedic anime… | MIT |
| [blender-product-film](blender-product-film/) | Premium 3D product films rendered in Blender (headless, GPU) — dark studio, rim light, light sweeps, glass/liquid/metal materials, condensation and bubbles, macro and… | MIT |
| [crayon-storybook](crayon-storybook/) | Make warm children's picture-book animations (MP4) drawn in crayon, coloured pencil and pastel on cream drawing paper — waxy crayon scribble fills broken by paper tooth… | MIT |
| [embedded-captions](embedded-captions/) | Add captions or subtitles to an existing single-subject talking-head video without editing the footage. Use for plain verbatim captions, cinematic captions embedded… | MIT |
| [faceless-explainer](faceless-explainer/) | Turn arbitrary text — an article, notes, a topic, a brief — into a faceless explainer video: there is no site or footage to capture, so the visuals are invented per… | MIT |
| [figma](figma/) | Import Figma content into a HyperFrames composition — rendered assets, brand tokens, components, storyboard sections → reconstructed motion (frames read as states, not… | MIT |
| [general-video](general-video/) | Author or edit a custom HyperFrames composition when no specialized workflow fits, or when BRIEF.md sets flow: companion. Use for longer or multi-scene pieces, brand and… | MIT |
| [hyperframes](hyperframes/) | Mandatory entry point: read this first for any request to make, create, edit, animate, or render a video, animation, or motion graphic, including a promo, explainer… | MIT |
| [hyperframes-animation](hyperframes-animation/) | All animation knowledge for HyperFrames — atomic motion rules, multi-phase scene blueprints, scene transitions, broader motion-design techniques, AND the seven runtime… | MIT |
| [hyperframes-audio](hyperframes-audio/) | Use when audio already placed in a HyperFrames composition needs to be mixed: fade-in/fade-out, crossfade, track gain or volume, volume automation, ducking, a music bed… | MIT |
| [hyperframes-cli](hyperframes-cli/) | Use the HyperFrames CLI development loop: init, add, catalog, capture, lint, check, snapshot, compare, grade-compare, preview, play, present, beats, keyframes, single or… | MIT |
| [hyperframes-core](hyperframes-core/) | The HyperFrames composition contract — build one renderable project. Use for composition structure, the `data-*` timing attributes, `class="clip"`, tracks… | MIT |
| [hyperframes-creative](hyperframes-creative/) | Non-animation creative direction for HyperFrames videos. Use for design spec (frame.md / design.md) handling, palettes, typography, narration, beat planning… | MIT |
| [hyperframes-keyframes](hyperframes-keyframes/) | Use when a HyperFrames composition needs a punch-in, punch-out, zoom, reframe, Ken Burns treatment, camera move, visual match/whip handoff, or other seek-safe 2D/3D… | MIT |
| [hyperframes-registry](hyperframes-registry/) | Search, install, and wire registry blocks and components into HyperFrames compositions. Use BEFORE hand-building any named visual — whenever a brief, a user, or a… | MIT |
| [hyperframes-studio](hyperframes-studio/) | Use when building or editing a HyperFrames project that people open in Studio: how the timeline should be laid out so it reads well (one caption track, one element kind… | MIT |
| [media-use](media-use/) | Agent Media OS, the single skill for every media need in a HyperFrames project. Resolve BGM, SFX, image, icon, brand logo, voice, color grade, or LUT into a frozen local… | MIT |
| [motion-graphics](motion-graphics/) | A short, design-led motion graphic where motion is the message — kinetic typography, stat count-up, chart/data-viz hit, logo sting / brand lockup, lower-third / callout… | MIT |
| [paper-cutout](paper-cutout/) | Make paper cut-out / stop-motion style animated videos (MP4) with code — handmade construction paper, cardstock, kraft, felt and tissue pieces with scissor-cut or torn… | MIT |
| [pixel-art](pixel-art/) | Make modern, polished pixel-art animated videos (MP4) with code — indie-game look (Celeste / Eastward / Stardew-level scenes, original), 480×270 art upscaled ×4 with… | MIT |
| [pr-to-video](pr-to-video/) | Turn a GitHub pull request (a PR URL, owner/repo#N, or 'this PR' in a checked-out repo) into a code-change explainer video — changelog, feature reveal, fix, or refactor… | MIT |
| [product-launch-video](product-launch-video/) | Turn a product or marketing URL, pasted script, or brief into a product launch / promo video — SaaS promos, feature reveals, product demos, app and company launches. Use… | MIT |
| [remotion-to-hyperframes](remotion-to-hyperframes/) | Port an existing Remotion (React) composition''s source to HyperFrames HTML. Use ONLY on an explicit ask to port/convert/migrate/translate a Remotion source — one-way… | MIT |
| [slideshow](slideshow/) | Author a HyperFrames slideshow — a presentation, pitch deck, or interactive deck with discrete slides, fragment reveals, branching, hotspot navigation, and built-in… | MIT |
| [talking-head-recut](talking-head-recut/) | Package an existing talking-head / interview / podcast video with timed, designed GRAPHIC OVERLAY cards — kinetic titles, lower-thirds, data callouts, quotes, side… | MIT |
| [video-clone](video-clone/) | 參考影片風格克隆器 — 使用者給一支參考影片（本機檔案、螢幕錄影或 YouTube/網址）加上一句需求（「做一支類似風格的影片，主軸是…」），就拆解它的剪法與視覺風格、判斷屬於哪種風格、交給對應的製作 skill，寫分鏡、做動畫、逐格自我審查，最後輸出 MP4 並依回饋修改。Use whenever the user supplies… | MIT |
| [whiteboard](whiteboard/) | Make hand-drawn whiteboard / doodle-explainer / sketch-note animation videos (MP4) with code — marker lines that draw themselves on, a cartoon hand holding a marker that… | MIT |

Install one with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/SOYL-AI/soyl-skills-hub/tree/main/skills/video-and-motion/reelmimic/anime-cel -g -a claude-code
```

Back to [Video and motion](../../../catalog/video-and-motion.md)
