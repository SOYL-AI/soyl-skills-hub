# gsap-skills

Skills from [greensock/gsap-skills](https://github.com/greensock/gsap-skills) at commit [`aed9cfd`](https://github.com/greensock/gsap-skills/tree/aed9cfd3277740755f6bfc1155c7aa645403b760), copied into SOYL Hub on 2026-10-29. Licence: MIT.

> Official AI skills for GSAP. These skills teach AI coding agents how to correctly use GSAP (GreenSock Animation Platform), including best practices, common animation patterns, and plugin usage.

All credit goes to the authors of greensock/gsap-skills. Each folder is the upstream skill unchanged, with its licence file added when it had none; build caches and plugin manifests are left out.

| Skill | What it does | Licence |
|---|---|---|
| [gsap-core](gsap-core/) | Official GSAP skill for the core API — gsap.to(), from(), fromTo(), easing, duration, stagger, defaults, gsap.matchMedia() (responsive, prefers-reduced-motion). Use when… | MIT |
| [gsap-frameworks](gsap-frameworks/) | Official GSAP skill for Vue, Svelte, and other non-React frameworks — lifecycle, scoping selectors, cleanup on unmount. Use when the user wants animation in Vue, Nuxt… | MIT |
| [gsap-performance](gsap-performance/) | Official GSAP skill for performance — prefer transforms, avoid layout thrashing, will-change, batching. Use when optimizing GSAP animations, reducing jank, or when the… | MIT |
| [gsap-plugins](gsap-plugins/) | Official GSAP skill for GSAP plugins — registration, ScrollToPlugin, ScrollSmoother, Flip, Draggable, Inertia, Observer, SplitText, ScrambleText, SVG and physics… | MIT |
| [gsap-react](gsap-react/) | Official GSAP skill for React — useGSAP hook, refs, gsap.context(), cleanup. Use when the user wants animation in React or Next.js, or asks about GSAP with React… | MIT |
| [gsap-scrolltrigger](gsap-scrolltrigger/) | Official GSAP skill for ScrollTrigger — scroll-linked animations, pinning, scrub, triggers. Use when building or recommending scroll-based animation, parallax, pinned… | MIT |
| [gsap-timeline](gsap-timeline/) | Official GSAP skill for timelines — gsap.timeline(), position parameter, nesting, playback. Use when sequencing animations, choreographing keyframes, or when the user… | MIT |
| [gsap-utils](gsap-utils/) | Official GSAP skill for gsap.utils — clamp, mapRange, normalize, interpolate, random, snap, toArray, wrap, pipe. Use when the user asks about gsap.utils, clamp… | MIT |

Install one with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/SOYL-AI/soyl-skills-hub/tree/main/skills/web-animation/gsap-skills/gsap-core -g -a claude-code
```

Back to [Web animation](../../../catalog/web-animation.md)
