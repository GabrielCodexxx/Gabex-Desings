# Prism Research — Evidence With an Editorial Spine

A research studio website arranged as a sequence of annotated observations, connecting strong art direction to inspectable methods. Prism is fictional; project descriptions are illustrative and make no clinical or scientific outcome claims.

## Product and core flow

For collaborators deciding whether a research team fits their question. Flow: understand the studio's focus → explore a project → inspect method and limitations → meet the contributors → submit a specific inquiry. Sample project: “Mapping material fatigue / A methods study.” Supporting copy: “Explore the setup, assumptions, and open questions.” The primary action is “Discuss a research question,” followed by a form requesting topic, context, and reply address. Avoid invented publications, partner logos, awards, or impact statistics.

## Visual system

- Warm white canvas `#F7F6F1`; black-green ink `#172E2B`; muted ink `#526763`; soft field `#E5EAE0`; emerald action `#245C4C`; annotation purple `#654C88`; focus `#A3421F`; error `#A62F37`.
- Instrument Sans for headings and interface text, fallback Arial/sans-serif. Source Serif 4 for long-form analysis, fallback Georgia/serif. Heading: 72/76 px desktop, 42/46 px mobile. Article body: 19/31 px desktop and 17/28 px mobile. Figure captions: 14/21 px.
- Use 12 columns, 56 px desktop gutters, 22 px mobile gutters, and 8 px spacing increments. Fine numbered rules connect figures and notes. Imagery resembles recorded work rather than futuristic stock graphics; decorative diagram lines never imply actual measurements.

## Screen composition

At 1440 px, the opening screen is a two-thirds editorial headline aligned left and a one-third vertical project index on the right. Beneath the headline, one large specimen image sits next to a small “Question / Method / Status” block. The first project link appears above the fold; there is no carousel of vague benefits.

Project pages use an 8-column article with a 3-column annotation gutter. A persistent section outline links to Question, Setup, Observations, Limitations, and Team. Figure captions include whether imagery is conceptual. The methods block provides plain-language explanation before technical detail. Contact is an uncluttered page with two short form steps and a review screen.

At 390 px, collapse annotations into inline disclosures immediately after their referenced paragraphs. The project index becomes a numbered list below the headline. The section outline becomes a native select-style navigation control with a visible label. Figures fit the page; large diagrams offer a separate zoom view with buttons and a textual equivalent.

## Interaction and states

Figure references are real anchor links and retain useful positions after navigation. Disclosures expose expanded state and work with Enter and Space. Search labels conceptual projects as examples, with an empty state reading “No projects match this topic. Clear your filters.” Loading never replaces article text with a blank frame. An unavailable attachment shows its title, type, and “File unavailable” beside retry. The inquiry form validates fields individually, retains entered data after failure, and confirms submission with a reference and an editable copy of the message. No completion promise is fabricated.

## GSAP motion choreography

| Trigger | Target | Duration / ease | Result |
| --- | --- | --- | --- |
| Page enters | Numbered masthead and headline block | `gsap.timeline()`, 0.60 s, `power3.out` | A 20 px reveal introduces the editorial rhythm; content remains readable without scripts. |
| Figure enters viewport | Figure frame | `ScrollTrigger`, 0.55 s, `power2.out`, once | Frame and caption fade in together without measurement-like line drawing. |
| Annotation expanded | Inner note surface | `gsap.fromTo()`, 0.18 s, `power1.out` | A 6 px motion clarifies disclosure; layout opens natively first. |
| Inquiry review selected | Review summary | 0.24 s, `power2.out` | A restrained crossfade links the input and confirmation stages. |

## Signature button

The inquiry button is a dark rectangular label with an offset annotation bracket. Fine-pointer hover moves the bracket outward 4 px while the text stays anchored. Press compresses the inner label to `0.97` over 0.09 s; release uses `back.out(1.45)` for 0.38 s. Keep action execution immediate. Keyboard focus outlines the complete hit area with a 3 px ring, and the decorative bracket is hidden from assistive technology. With reduced motion, the bracket and label remain stationary and switch fill instantly. The easing supplies spring-style overshoot, not a physical spring model.

## Accessibility and performance

Maintain readable line lengths around 65 characters and document headings in order. All diagrams need meaningful text descriptions. Do not encode evidence strength through animation, color, or opacity. Use `gsap.matchMedia()` and revert animation contexts during navigation. No pinned article sections or scroll hijacking. Reserve image sizes and lazy-load supporting figures; prioritize the opening image. Forms and article navigation remain functional before GSAP initializes.

## Build acceptance criteria

- Every project exposes methods and limitations without requiring a download.
- At 390 px, annotations appear directly beside their reading context.
- Reduced motion shows all figures and inquiry controls immediately.
- No fictional outcome, affiliation, or diagram is presented as established scientific evidence.
