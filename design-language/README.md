# SOYL Academy design language

The design system behind SOYL Academy's website. It aims for calm, Apple-like clarity: every element is there for a
reason, the product is shown instead of decoration, and motion only explains. Use it for anything SOYL Academy
makes: web pages, product screens, emails, slides and documents. You can also borrow it for your own calm
product pages.

| File | What it is |
|---|---|
| [tokens.css](tokens.css) | Colours, type scale, spacing, radii, shadows and motion timings as CSS custom properties |
| [components.css](components.css) | The foundation and core parts: sections, type, links, buttons, text actions, cards, focus and the arrival motion |
| [reveal.js](reveal.js) | The one scroll motion: blocks rise once as they come into view (about 1 KB) |
| [SKILL.md](SKILL.md) | The same rules for Claude: install this folder as a skill and Claude builds in this style |

## Six rules

1. **One idea per screen.** A headline, one sentence, one action. Reading only the headlines tells the whole story.
2. **Show the product.** The main visuals are real product moments, such as a student's tries, a hint or the
   Evidence Card a teacher reads. No decorative graphics.
3. **Motion explains, it never performs.** Content rises once as it arrives. Nothing moves on its own. With
   reduced motion turned on, the page is still and complete.
4. **A calm palette.** A near-white ground, ink text and one blue for actions and links. Sunflower is only for
   Future Builders. Use at most one dark band per page, where the problem is stated.
5. **One typeface.** Switzer for everything.
6. **Easy to scan.** Centred section heads, short paragraphs, cards with rounded corners, and the browser's own
   scrolling.

## Every section has a job

Before you design a section, name its job and the principle behind it. Here is how the SOYL Academy home page
does it:

| Section | Job | Principle |
|---|---|---|
| Hero: the promise in one line, beside a product moment | Say what it is in five seconds, and show it | Clarity first; show, don't tell |
| One dark band that states the problem | Make the old way's cost felt | Loss framing, side-by-side contrast |
| Three step tiles that each play once | Take the doubt out of "how does it work?" | Show the mechanism |
| Something to try right on the page | Let the visitor feel it | Experience beats claims |
| Cards that answer the reader's fear honestly, limits included | Earn trust | Control and candour |
| FAQ, then one small next step | Clear the last doubts | A small first commitment |

Don't invent proof. Leave the place for a pilot result or a teacher's words empty until you have a real one.

## Colour

| Role | Token | Hex | Use |
|---|---|---|---|
| Ground | `--bg` | `#fbfaf8` | Page background |
| Panel | `--panel` | `#f2f1ec` | Alternate bands, product frames, footer |
| Card | `--card` | `#ffffff` | Cards and product screens, with a soft shadow |
| Ink | `--ink` | `#121212` | Text |
| Muted | `--muted` | `#5f5d58` | Secondary text (6:1 on the ground) |
| Blue | `--blue` | `#2f4bff` | Buttons, links, eyebrows: the action colour (5.6:1) |
| Night | `--night` | `#0b0c10` | The one dark band |
| Sunflower | `--sun` | `#f4c93e` | Future Builders only |
| Red, green, amber | `--red`, `--green`, `--amber` | `#d93a24`, `#1e7a4c`, `#d97706` | Inside the product only: a missed try, a right one, a highlight |

Blue means "you can act here". Don't use it for decoration, and don't add a second accent.

## Type

[Switzer](https://www.fontshare.com/fonts/switzer) (Fontshare, free), variable, self-hosted. `tokens.css` has a
metric-matched Arial fallback, so the page doesn't shift when the font arrives.

| Use | Size | Weight and tracking |
|---|---|---|
| Hero | 44 to 88 px (`--t-hero`) | 650, -0.042 em, line height 1.02 |
| Page title | 40 to 74 px (`--t-h1`) | 650, -0.038 em |
| Section head | 33 to 60 px (`--t-h2`) | 650, -0.034 em |
| Card title | 20 to 24 px (`--t-h3`) | 650, -0.018 em |
| Lead | 18 to 22 px (`--t-lead`) | 400, muted, at most 38 rem wide |
| Body | 17 to 18 px (`--t-body`) | 400, line height 1.55 |

Headlines use `text-wrap: balance` and paragraphs use `text-wrap: pretty`. Use sentence case everywhere.

## Space and shape

- Content is at most 1200 px wide, with 20 to 72 px side margins (`--max`, `--m`).
- Sections sit 88 to 140 px apart (`--sec`). Two neighbours on the same ground share one gap instead of two.
- Panels have a 28 px radius and cards 22 px (22 and 18 on phones). Buttons and chips are pills.
- Shadows are soft and come in two layers (`--shadow`). On hover, a card lifts 3 px (`--shadow-lift`).

## Motion

There is one verb: **arrive and settle**. The easing is `cubic-bezier(0.2, 0.7, 0.2, 1)`.

- On the first screen, the words are there at once. Only the product moment beside them rises 16 px and fades
  in (900 ms, by CSS).
- Further down, each block rises 16 px once as it comes into view (600 ms, 70 ms between items): `reveal.js`.
- A product moment can play its story once when it's seen, for example a try drawing in or a row filling up.
  It never loops.
- Pages crossfade in about a quarter of a second, using cross-document view transitions where the browser
  has them.
- Controls answer at once. A button deepens and lifts 2 px and settles when pressed. A text link underlines and
  its chevron steps forward.
- Don't use smooth-scroll libraries or a global `scroll-behavior: smooth`. Scrolling is the browser's own.
- With reduced motion, everything is in place and pages cut plainly.

## Components

- **Sections.** Choose from `.section` (the ground), `.section--panel` (warm grey), `.section--dark` (night,
  once per page) and `.section--sun` (Future Builders only). Put content inside `.wrap`.
- **Buttons** (`.btn`). A blue pill, at least 48 px tall. Variants: `--ink`, `--light` (on dark), `--quiet`
  (outline) and `--small` (36 px). Use one main action per screen.
- **Text actions** (`.more`). A blue label with a chevron, as in "Plan a pilot ›". Use it for the second action.
- **Cards** (`.card`). White, rounded and softly shadowed. A whole card can be a link, and it lifts on hover.
- **Eyebrow and lead** (`.eyebrow`, `.lead`). A short blue label over a heading, and a muted sentence under it.
- **Focus.** Every control shows a 2 px blue ring when you reach it by keyboard: light blue on dark bands, ink
  on sunflower. Add a skip link at the top of every page.

## Accessibility

- Text holds at least 4.5:1 contrast: muted is 6:1 and blue is 5.6:1 on the ground. Field edges hold 3:1.
- Everything works by keyboard. A block that hasn't risen yet appears at once when focus reaches it.
- Tap targets are at least 44 px. Links in running text get extra padding to reach 24 px.
- Reduced motion gets a still, complete page.

## Use it

**In code.** Load `tokens.css`, then `components.css`, and add `reveal.js` (its comment has the small head
script). Self-host Switzer at `/fonts/switzer-var.woff2`, or change the path in `tokens.css`.

**With Claude.** Install this folder as a skill, then ask Claude to build or review a page "in the SOYL Academy
design language":

```bash
npx skills add https://github.com/SOYL-AI/soyl-skills-hub/tree/main/design-language -g -a claude-code
```

The CSS and JavaScript here are under the MIT licence (see [LICENSE](../LICENSE)). The SOYL and SOYL Academy
names, logos and product screens are not part of it. Use the system for your own work, not to look like SOYL.
