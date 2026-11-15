# Mono — A film archive designed for lingering

A cinematic editorial archive built from credits, stills, and careful reading rhythm. Mono, film titles, filmmakers, and publication details here are fictional.

## Product and core flow

Design for curious film viewers and researchers who want to follow a theme through films and writing. The task is to move from a still or essay to reliable-looking, explicitly fictional metadata, then build a personal reading list. Avoid implying streaming rights or availability.

Flow: enter a curated dossier → open a film → inspect credits and related writing → save an essay → return to a reading list. Sample dossier: “Rooms after midnight.” Sample film: “The Last Tram · 1987 · 94 min · fictional entry.” An essay preview reads “How an empty carriage becomes a stage for hesitation.”

## Visual system

- Canvas: almost-black `#171717`; primary text: warm white `#EEE9DE`; secondary text: `#B9B4AA`; light reading canvas: `#F0EBDF`; reading ink: `#252421`; accent: faded gold `#CDB57C`; dividers: `#514E46`.
- Pair **Literata**, Georgia, serif for essays and headlines with **Archivo**, Arial, sans-serif for navigation and credits. Use tabular numerals for years and runtimes.
- Desktop dossier heading: 72/76 px; mobile: 42/46 px. Essay body: 19/31 px desktop and 18/29 px mobile. Metadata: 13/20 px. Use 12 px rhythm and a reading width of 66 characters.
- Stills have consistent credited captions. Film grain is baked into images only where artistically appropriate; do not animate a noise overlay across text.

## Screen composition

At **1440 px**, the first viewport is an asymmetrical screening sheet: a 58% width still on the left, a tall dossier title crossing into generous black negative space on the right, and an index of four essays below the title. A thin metadata strip anchors the bottom. Navigation stays small and explicit: Dossiers, Films, Journal, Saved.

Film detail places its title and credit ledger above a still sequence; related essays appear as numbered text rows. An essay opens on the light canvas with a compact dark masthead, a standfirst, author information, and a chapter index. The saved list is a readable library ledger with length and reading status.

At **390 px**, still → dossier title → introduction → essay index is the DOM order. Titles never overlap images or crop into unreadable text. The chapter index collapses into an ordinary disclosure. Credits become definition-list groups. No horizontal filmstrip is required to reach the next entry; provide previous and next links.

## Interaction and states

Every still link has a descriptive film title. A still sequence provides buttons and a numbered position; swiping is optional. Save controls expose `aria-pressed` and use “Save essay” / “Essay saved.” An empty reading list explains where saved writing appears. Loading preserves title and caption structure. A failed still becomes a captioned placeholder with retry. A failed save keeps the essay available and offers retry without claiming success. Reading progress never marks a piece “read” solely because a user scrolled quickly.

## GSAP motion choreography

| Trigger | Target | Duration / ease | Result |
| --- | --- | --- | --- |
| Dossier opens | Still frame, then title | `gsap.timeline()`, 0.70 s and 0.45 s, `power2.out` | Clip reveal of the still; title opacity follows while remaining in place. |
| Essay index enters view | Fine divider rules | ScrollTrigger once, 0.50 s, `power1.out` | ScaleX 0 → 1 from the left, without moving text. |
| Next still requested | Current and incoming still | 0.32 s, `power1.inOut` | Crossfade the images; caption updates immediately. |
| Essay saved | Bookmark edge | 0.36 s, `back.out(1.6)` | A small tab settles into the page margin. |

ScrollTrigger decorates rules only. It must never reveal paragraphs late, scrub reading text, or pin the essay.

## Signature button

“Open dossier” is a text-forward gold-outlined button with a fixed-width arrow compartment. Fine-pointer hover shifts the arrow **5 px** while a short underline extends beneath the label. Press compresses the arrow compartment to **scaleX 0.94** over **0.07 s**; release returns over **0.44 s**, `back.out(1.55)`. Keep label glyphs unscaled. This is an editorial spring-style gesture, not a physical spring. Navigation starts on click. Focus gets a 3 px warm-white outline separated from the gold border. Reduced motion shows a static underline and immediate state changes.

## Accessibility and performance

Respect the essay’s natural scroll and browser history. Provide full credits as text, descriptive alt text, and caption semantics. Never autoplay trailers or sound. Load responsive stills below the fold lazily; serve the primary image at an appropriate resolution. Use scoped GSAP contexts, clean up ScrollTriggers on navigation, and remove reveal clipping under reduced motion or failed JavaScript.

## Build acceptance criteria

- Every fictional film entry exposes title, year, runtime, credits, and its demo designation.
- Essays remain readable with animation disabled, JavaScript unavailable, and 200% zoom.
- A keyboard user can change stills, save an essay, and reach the next film.
- At 390 px, headlines, credits, and captions never overlap or require page-wide horizontal scrolling.
