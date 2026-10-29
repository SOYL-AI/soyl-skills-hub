---
name: soyl-academy-design
description: SOYL Academy's design language. It gives calm, Apple-like pages in Switzer only, on a near-white ground with ink text, one blue for actions, sunflower only for Future Builders, and motion that only explains. Use when building, redesigning or reviewing anything for SOYL Academy (web pages, landing pages, product screens, emails, slides, documents), or when someone asks for the SOYL Academy look, "calm and Apple-like", or this design language.
license: MIT
---

# SOYL Academy design language

Build so an ordinary visitor understands the page at a glance. Every element must earn its place, either as
part of the story or as a reason to act. When creativity gets in the way of reading, cut it.

Read `tokens.css` and `components.css` in this folder before writing any styles. Use their custom properties
and classes rather than new values. `README.md` has the full system with tables.

## 1. Plan before you style

- Write the page as headlines first. Reading only the headlines must tell the whole story.
- Give each section one job and name the principle behind it: clarity first, loss framing, show the mechanism,
  experience beats claims, trust through candour, or a small first commitment.
- Give each screen one idea: a headline, one sentence and one action.
- Show the product. The main visual of a section is a real product moment (a student's tries, a hint, the
  Evidence Card a teacher reads), drawn in HTML and CSS. Don't use stock art, blobs, gradients or decorative
  icons.
- Never invent proof. Don't write made-up testimonials, school names, numbers or logos. Leave the slot empty
  and say so.

## 2. Build with the system

- **Grounds:** `--bg` for the page, `--panel` for alternate bands, `--card` for cards. Use at most one
  `.section--dark` (`--night`) per page, where the problem is stated.
- **Colour:** text in `--ink` and secondary text in `--muted`. `--blue` is only for things you can act on:
  buttons, links, eyebrows. Use `--sun` (sunflower) only for Future Builders. Use `--red`, `--green` and
  `--amber` only inside product moments.
- **Type:** Switzer for everything (`--f`). Headlines are weight 650 with tight tracking, from `--t-hero`,
  `--t-h1`, `--t-h2` and `--t-h3`. Body is `--t-body` with line height 1.55, and a lead line is `.lead`. Use
  sentence case, `text-wrap: balance` on headings and `text-wrap: pretty` on paragraphs.
- **Layout:** put content in `.wrap` (`--max` 1200 px, `--m` margins), with sections `--sec` apart. Centre the
  section heads. Keep paragraphs short. Two neighbouring sections on the same ground share one gap.
- **Shape:** panels use `--r` (28 px) and cards `--r-card` (22 px), with soft `--shadow`. Buttons and chips are
  pills.
- **Parts:** `.btn` (the blue pill, one main action per screen; `--ink`, `--light`, `--quiet` and `--small`),
  `.more` (a text action with a chevron), `.card` (a whole card can be a link), `.eyebrow`, `.lead` and
  `.section--panel`, `--dark` or `--sun`.

## 3. Motion explains, it never performs

- There is one verb, arrive and settle, with `--ease`. The first screen's words are static, and only its
  product moment rises 16 px (`.arrive`, 900 ms).
- Further down, blocks rise 16 px once as they come into view (`data-reveal` or `data-reveal-group`, with
  `reveal.js`, 600 ms, 70 ms stagger).
- A product moment may play its story once when it's seen. Nothing loops or moves at rest.
- Controls answer at once. Buttons deepen and lift 2 px, and a press scales them to 0.97. Text links underline
  and their chevron steps forward.
- Don't add GSAP, Lenis, smooth-scroll libraries, parallax, cursor effects or a global
  `scroll-behavior: smooth`. In-page links may glide by script.
- Under `prefers-reduced-motion: reduce`, everything shows in place.

## 4. Check before you call it done

- [ ] The headlines alone tell the story. Each screen has one idea and one main action.
- [ ] Blue appears only on things you can act on. There's at most one dark band. Sunflower appears only for
      Future Builders.
- [ ] No decoration stands in for the product, and no proof is invented.
- [ ] Text contrast is at least 4.5:1. Focus rings show on every control, and there's a skip link. Tap targets
      are at least 44 px.
- [ ] At 375 px wide there's no sideways scroll, and headlines still balance.
- [ ] With reduced motion, the page is complete and still. Without JavaScript, all content shows.
- [ ] The page uses the tokens rather than new hex values, sizes or easings.

The SOYL and SOYL Academy names, logos and product screens belong to SOYL. Use this system to build for
SOYL Academy, or in your own work without passing it off as SOYL's.
