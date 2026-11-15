# Studio Index — A Portfolio as a Living Catalogue

An art director's portfolio organized as an exhibition index: giant type, precise metadata, generous paper, and projects that reveal themselves through intentional selection. Studio Index and its projects are fictional.

## Product and core flow

For creative leads commissioning an identity or digital experience. The central task is assessing the designer's thinking, craft, and fit for a brief.

Flow: scan the project index → filter by discipline → open a case study → read the problem and design decisions → review deliverables → contact the studio. Example project: “No. 07 — Tidal Reading Room / Identity + digital / 2027.” Use “View case study” and “Tell me about your project,” with an honest availability line supplied by the owner.

Every case study must show reasoning, constraints, and actual work. Prototype results are labeled illustrative; do not invent conversion percentages or client endorsements.

## Visual system

- Paper `#F5F4EE`; ink `#171715`; quiet text `#5A5A53`; rules `#B9B9AF`; vermilion artwork accent `#D43329`; accessible red text/action `#AC2B24`; inverse `#FFFFFF`.
- Space Grotesk with Arial/sans-serif fallback for the index and interface; Newsreader with Georgia/serif fallback for project essays.
- Desktop wordmark 148/132 px, project rows 32/38, essay 21/33, metadata 12/18. Mobile wordmark 62/60, row title 24/29, essay 18/29.
- Use a 12-column grid, 48 px desktop gutters, 20 px mobile gutters, and 8 px spacing units. Numbering, rules, and intentional empty space create the identity. Avoid ornamental cards.

## Screen composition

At 1440 px, a large typographic masthead occupies the upper quarter of the screen. Below it, a seven-column ruled project index sits beside a five-column preview frame. Each row contains number, project name, discipline, year, and an arrow. Keep at least four rows visible on a 900 px tall reference viewport. A short introduction and contact link live at the edge of the masthead, not in a centered hero.

Selection updates the adjacent preview and an image caption. The active project name remains legible and stable. A case study opens as a real page with a two-column opening spread, a problem statement, annotated work, and a compact outcome section. The footer offers a next case and contact.

At 390 px, remove the side preview. Render one thumbnail inline beneath each project title, with readable metadata and a full-row link. Filters wrap into real buttons. Case study spreads become stacked images followed by their own captions. Never use a hover-only preview as the mobile content source.

## Interaction and states

Filters use selected text and `aria-pressed` where they are toggle buttons. Applying a filter updates the count and keeps focus on its control; an empty result offers Clear filters. Desktop row focus shows the same preview as pointer hover. The row's primary action is a real link, and opening a new tab works normally. Failed images retain aspect ratio, title, and caption. Contact submission distinguishes sending, received, and error, preserving the message on failure.

## GSAP motion choreography

| Trigger | Target | Timing and API | Intended result |
| --- | --- | --- | --- |
| Initial load | Masthead visual wrapper | `gsap.fromTo()`, y 22 → 0, 0.65 s, `power3.out` | One purposeful typographic arrival; text exists and is readable before JS. |
| Preview selection | Two image layers inside the preview frame | `gsap.timeline()`, 0.3 s opacity crossfade, `power2.out` | A crisp editorial swap; overwrite the previous transition on rapid input. |
| Case study chapter enters | Figure and its caption as one unit | `ScrollTrigger`, once, 0.45 s, y 12 → 0, `power2.out` | Keep explanatory text associated with its image. |
| Filter changes | Newly shown row contents | 0.18 s opacity, `power1.out`; no stagger | Immediate results and a stable reading order. |

Avoid scrambling letters, custom cursor dependencies, endless marquees, and route transitions that intercept navigation.

## Signature button

The case-study link ends in a red square containing an arrow. Animate only this square: press scale 0.94 over 0.09 s, release 1 over 0.42 s with `back.out(1.8)`. On fine-pointer hover, the arrow travels 4 px diagonally inside its clipped square over 0.2 s. The label never moves. An outer 3 px ink focus outline frames the whole link. Enter activates the link immediately; restore the decorative square on keyup, blur, or pointer cancellation. Reduced motion swaps the square's fill with no movement. The overshoot is spring-style easing rather than a simulated physical spring.

## Accessibility and performance

Maintain logical heading order and native link behavior. Use concise image descriptions; captions supply project context without duplicating alt text. Serve appropriately sized previews and preload only the first. Cancel previous preview tweens rather than stacking timelines. Reserve image dimensions to prevent shifts. Reduced motion removes entrances and crossfades, presenting all case content immediately. Navigation and project selection must remain functional if GSAP fails to load.

## Build acceptance criteria

- Four project rows and a labeled preview are visible at the desktop reference size; mobile rows include their own imagery.
- Pointer and keyboard selection reveal identical project information.
- Filtering preserves control focus and displays a truthful count or an actionable empty state.
- Opening case studies in a new tab, browser Back, and reduced-motion reading all work without animation dependencies.
