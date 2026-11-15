# Orbit Studio — Case Studies as Storyboards

A creative studio portfolio shaped like a film contact sheet: bold crops, purposeful sequencing, and a clear role for every image. Orbit and its showcased projects are fictional concepts.

## Product and core flow

For founders and creative leads evaluating the studio's judgment, not just its visual range. Flow: scan selected work → enter a relevant case → understand the brief and decisions → inspect deliverables → send a project outline. Example case: “Nacre / Packaging for a fictional coastal soap maker.” Case copy names the role, constraints, and proposed design choices. Use “Concept project” prominently; do not invent client endorsements or conversion claims. Main CTA: “Tell us what you're making.”

## Visual system

- Canvas `#F0EEE8`; ink `#20201F`; high-contrast section `#242522` with text `#F7F4EC`; accent orange `#B8401E`; secondary text `#62625B`; pale annotation `#DEDACF`; focus blue `#255CAB`.
- Space Grotesk for assertive titles and controls, fallback Arial/sans-serif. Libre Baskerville for short reflections, fallback Georgia/serif. Project title: 88/88 px desktop, 46/48 px mobile. Body: 18/28 px desktop, 16/25 px mobile. Metadata: 13/20 px with normal readable tracking.
- A 12-column grid uses 48 px desktop and 20 px mobile gutters. Frames have square corners, deliberate white space, and printed frame numbers. Reserve orange for navigation and meaningful accents; avoid gradient backgrounds and cursor gimmicks.

## Screen composition

At 1440 px, the first viewport starts with a compact studio wordmark, then “Ideas with a clear point of view” on the left and a single oversized project frame cropped into the right edge. A slim project list sits below the headline with discipline, year, and concept label. The image is a real link with a visible title, not an unlabeled hover target.

Selected work unfolds as a contact sheet: a wide primary frame, two uneven supporting crops, then a narrow caption column. Each case page opens with Brief, Role, and Constraint, followed by a sequence labeled Frame 01–05. The middle of the case pairs a rejected concept with the chosen direction and an explanation. A plain text deliverables list and project inquiry close the page.

At 390 px, preserve the sequence as a single readable column. Side captions move above their images. Cropped previews become full compositions when opened. The navigation is a normal disclosure menu; the project index is always reachable. There is no horizontally controlled page or wheel-driven slideshow.

## Interaction and states

On fine-pointer hover, the project title underlines and a frame number changes fill; the title and concept label are always visible. Keyboard focus gets the same information. Opening a case preserves the previous index position through normal history behavior. Image loading reserves the full frame and retains caption text. A failed video offers a poster, transcript, and “Retry playback”; media plays only on request. Inquiry errors stay near fields and preserve the draft. Success says “Your project outline was received” only when the submission actually succeeds. The empty work filter offers a clear reset.

## GSAP motion choreography

| Trigger | Target | Duration / ease | Result |
| --- | --- | --- | --- |
| Landing page ready | Headline lines and frame label | `gsap.timeline()`, 0.70 s, `power3.out`, 70 ms stagger | A 30 px rise gives the opening a measured editorial cadence. |
| Case frame enters view | Image inside a clipping wrapper | `ScrollTrigger`, 0.75 s, `power2.out`, once | A restrained scale from 1.035 to 1 reveals the composition without parallax. |
| Project hovered or focused | Number tab | `gsap.to()`, 0.18 s, `power2.out` | The tab shifts 4 px along its printed rule. |
| Inquiry stage changes | Step content | 0.22 s, `power2.out` | An 8 px transition connects steps without withholding fields. |

## Signature button

The inquiry button is a typographic ticket with a circular arrow inset at its edge. Fine-pointer hover rotates the arrow 35 degrees over 0.20 s; the button stays fixed. Press scales the arrow disc to `0.88` and the surface to `0.98` over 0.08 s. Release brings both to `1` over 0.44 s with `back.out(1.9)`. This is a spring-style flourish using overshoot easing. Focus surrounds the complete 48 px-high hit area with a 3 px outline. Reduced motion changes the arrow-disc fill immediately. No magnetic movement follows the cursor, and no animation delays navigation.

## Accessibility and performance

Make work links meaningful out of context, and describe visual decisions in text alongside images. Do not put essential copy inside artwork. Respect reduced motion using `gsap.matchMedia()`, and clean up ScrollTrigger instances on route changes. Render text visible before enhancement. Animate only transforms and opacity, size images responsively, and load case media after the primary frame. No scroll trapping, autoplay, or animated custom cursor is necessary.

## Build acceptance criteria

- Every case makes role, constraint, and concept status visible in its opening section.
- A keyboard user can inspect all work and complete the inquiry.
- At 390 px, case imagery and captions retain their intended reading order.
- Reduced motion removes scale, rotation, and reveals without hiding the portfolio.
