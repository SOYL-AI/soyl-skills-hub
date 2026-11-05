# pixijs

Skills from [pixijs/pixijs](https://github.com/pixijs/pixijs) at commit [`4fabfa6`](https://github.com/pixijs/pixijs/tree/4fabfa6409c35cc114cb4fbfbb812c9cd8abdced), copied into SOYL Hub on 2026-11-05. Licence: MIT.

> The HTML5 Creation Engine: Create beautiful digital content with the fastest, most flexible 2D WebGL renderer.

All credit goes to the authors of pixijs/pixijs. Each folder is the upstream skill unchanged, with its licence file added when it had none; build caches and plugin manifests are left out.

| Skill | What it does | Licence |
|---|---|---|
| [pixijs](pixijs/) | Use this skill first for ANY PixiJS v8 task; it routes to the right specialized skill for the job. Covers the full PixiJS surface: Application setup, the scene graph… | MIT |
| [pixijs-accessibility](pixijs-accessibility/) | Use this skill when adding screen reader and keyboard navigation to PixiJS v8 apps. Covers AccessibilitySystem options (enabledByDefault, debug, activateOnTab… | MIT |
| [pixijs-application](pixijs-application/) | Use this skill when creating and configuring a PixiJS v8 Application. Covers new Application() + async app.init() options (width, height, background, antialias… | MIT |
| [pixijs-assets](pixijs-assets/) | Use this skill when loading and managing resources in PixiJS v8. Covers Assets.init, Assets.load/add/unload, bundles, manifests, background loading, onProgress, caching… | MIT |
| [pixijs-blend-modes](pixijs-blend-modes/) | Use this skill when compositing display objects with blend modes in PixiJS v8. Covers standard modes (normal, add, multiply, screen, erase, min, max), advanced modes via… | MIT |
| [pixijs-color](pixijs-color/) | Use this skill when creating, converting, or manipulating colors in PixiJS v8. Covers Color class input formats (hex, CSS names, RGB/HSL objects, arrays, Uint8Array)… | MIT |
| [pixijs-core-concepts](pixijs-core-concepts/) | Use this skill when understanding how PixiJS v8 renders frames: the systems-and-pipes renderer, the render loop, and how the library adapts to different environments… | MIT |
| [pixijs-create](pixijs-create/) | Use this skill when scaffolding a new PixiJS v8 project with the create-pixi CLI or adding PixiJS to an existing project. Covers npm/yarn/pnpm/bun create commands… | MIT |
| [pixijs-custom-rendering](pixijs-custom-rendering/) | Use this skill when writing custom shaders, uniforms, filters, batchers, or low-level draw code in PixiJS v8. Covers Shader.from({gl, gpu, resources})… | MIT |
| [pixijs-environments](pixijs-environments/) | Use this skill when running PixiJS v8 outside a standard browser: Web Workers, OffscreenCanvas, Node/SSR, or CSP-restricted contexts. Covers DOMAdapter.set… | MIT |
| [pixijs-events](pixijs-events/) | Use this skill when handling pointer, mouse, touch, or wheel input in PixiJS v8. Covers eventMode (none, passive, auto, static, dynamic), FederatedEvent types… | MIT |
| [pixijs-filters](pixijs-filters/) | Use this skill when applying visual effects to PixiJS v8 containers via the filter pipeline. Covers built-in filters (AlphaFilter, BlurFilter, ColorMatrixFilter… | MIT |
| [pixijs-html-source](pixijs-html-source/) | Use this skill when rendering live HTML/DOM elements (or frozen snapshots of them) as PixiJS v8 textures via the EXPERIMENTAL HTML-in-Canvas browser APIs. Covers the… | MIT |
| [pixijs-math](pixijs-math/) | Use this skill when working with coordinates, vectors, matrices, shapes, hit testing, or layout rectangles in PixiJS v8. Covers Point/ObservablePoint, Matrix (2D affine… | MIT |
| [pixijs-migration-v8](pixijs-migration-v8/) | Use this skill when upgrading to PixiJS v8 from v7 or diagnosing broken v7 code after an upgrade. Covers async app.init, single pixi.js package (deprecated @pixi/*… | MIT |
| [pixijs-performance](pixijs-performance/) | Use this skill when profiling or optimizing a PixiJS v8 app for FPS, draw calls, or GPU memory. Covers destroy patterns (cacheAsTexture(false), releaseGlobalResources)… | MIT |
| [pixijs-scene-container](pixijs-scene-container/) | Use this skill when grouping, positioning, or transforming display objects in PixiJS v8. Covers Container constructor options (isRenderGroup, sortableChildren… | MIT |
| [pixijs-scene-core-concepts](pixijs-scene-core-concepts/) | Use this skill when reasoning about the PixiJS v8 scene graph as a whole: how containers, leaves, transforms, and render order fit together. Covers leaf vs container… | MIT |
| [pixijs-scene-dom-container](pixijs-scene-dom-container/) | Use this skill when overlaying HTML elements on the PixiJS v8 canvas. Covers DOMContainer with element, anchor, and scene-graph-driven CSS transforms, the pixi.js/dom… | MIT |
| [pixijs-scene-gif](pixijs-scene-gif/) | Use this skill when displaying animated GIFs in PixiJS v8. Covers the pixi.js/gif side-effect import, Assets.load returning a GifSource, GifSprite playback… | MIT |
| [pixijs-scene-graphics](pixijs-scene-graphics/) | Use this skill when drawing vector shapes and paths in PixiJS v8. Covers the Graphics API: shape-then-fill methods… | MIT |
| [pixijs-scene-mesh](pixijs-scene-mesh/) | Use this skill when rendering custom geometry in PixiJS v8. Covers Mesh with MeshGeometry (positions, uvs, indices, topology), MeshSimple for per-frame vertex animation… | MIT |
| [pixijs-scene-particle-container](pixijs-scene-particle-container/) | Use this skill when rendering thousands of lightweight sprites in PixiJS v8. Covers ParticleContainer with Particle instances, addParticle/removeParticle… | MIT |
| [pixijs-scene-sprite](pixijs-scene-sprite/) | Use this skill when drawing images in PixiJS v8. Covers Sprite with anchor/tint/texture, AnimatedSprite for frame animation, NineSliceSprite for resizable UI panels… | MIT |
| [pixijs-scene-text](pixijs-scene-text/) | Use this skill when rendering text in PixiJS v8. Covers Text for canvas-quality styled labels, BitmapText for cheap per-frame updates via glyph atlas, HTMLText for… | MIT |
| [pixijs-ticker](pixijs-ticker/) | Use this skill when running per-frame logic or controlling the PixiJS v8 render loop. Covers Ticker.add/addOnce/remove, deltaTime vs deltaMS vs elapsedMS… | MIT |

Install one with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/SOYL-AI/soyl-skills-hub/tree/main/skills/web-animation/pixijs/pixijs -g -a claude-code
```

Back to [Web animation](../../../catalog/web-animation.md)
