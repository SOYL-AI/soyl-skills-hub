# paint-mv-skills

Skills from [lintsinghua/paint-mv-skills](https://github.com/lintsinghua/paint-mv-skills) at commit [`ca8f5f7`](https://github.com/lintsinghua/paint-mv-skills/tree/ca8f5f75f186d590e687542b106aa73ceff9133c), copied into SOYL Hub on 2026-11-12. Licence: MIT.

> Agent skills that turn a song and its lyrics into a hand-painted watercolour music video (p5.brush + headless Chrome + ffmpeg), following PDoomVideo's pipeline

All credit goes to the authors of lintsinghua/paint-mv-skills. Each folder is the upstream skill unchanged, with its licence file added when it had none; build caches and plugin manifests are left out.

| Skill | What it does | Licence |
|---|---|---|
| [paint-mv](paint-mv/) | Turns a song (audio file + lyrics) into a hand-painted watercolour music video (MP4) in the style of PDoomVideo, following its pipeline end to end: measure the beat grid… | MIT |
| [paint-mv-animate](paint-mv-animate/) | Paints one chapter (src/ch/cNN_name.js) of a paint-mv music video in the PDoomVideo style: watercolour-and-ink frames drawn with p5.brush, the song's own characters… | MIT |
| [paint-mv-render](paint-mv-render/) | Checks and renders a paint-mv music video with its render.mjs (Puppeteer drives studio.html in headless Chrome, ffmpeg encodes): contact sheets and stills for visual… | MIT |
| [paint-mv-storyboard](paint-mv-storyboard/) | Writes STORYBOARD.md for a paint-mv music video the way the PDoomVideo storyboard was written, with everything specific taken from the song's own lyrics: a concept with… | MIT |

Install one with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/SOYL-AI/soyl-skills-hub/tree/main/skills/video-and-motion/paint-mv-skills/paint-mv -g -a claude-code
```

Back to [Video and motion](../../../catalog/video-and-motion.md)
