# Obsidian Atelier — Architecture as an editorial space

A fictional architecture practice whose website feels like a carefully annotated building monograph: generous negative space, architectural drawings, and photographic evidence instead of ornamental effects.

## Product and core flow

Serve prospective residential and cultural clients who need to understand the studio's judgment before making contact. The primary journey is **select project type → study a project → inspect drawings and constraints → request an introductory conversation**. Keep the project inquiry reachable throughout the journey.

Use specific demonstration copy: “Courtyard House / Residential / Batangas / Concept study” and “A shaded room between street and garden.” Project information includes brief, site conditions, design response, materials, and project status. Do not invent awards, client testimonials, or completed-building claims. The inquiry begins with project location and intended use; budget and contact details follow on the same clearly labeled page.

## Visual system

- **Palette:** limestone `#EEEAE2` canvas, carbon `#232420` body text, chalk `#FAF8F3` drawing plates, graphite `#65675E` secondary text, moss `#405D45` links and actions. Use a dark surface only around full-bleed photography.
- **Type:** Bodoni Moda with Georgia fallback for project titles; Manrope with Arial fallback for descriptions; IBM Plex Mono with monospace fallback for drawing references. Desktop title 92/94px; mobile 46/48px; body 17/28px desktop and 16/25px mobile. Keep paragraphs below 66 characters.
- **Geometry:** 12-column desktop grid, 64px outside margins, 24px gutters. At 390px, use 20px margins and a four-column grid. Spacing steps: 8, 16, 24, 40, 64, 104px. Borders are 1px; corners remain square.

## Screen composition

At 1440px, open with a left-aligned studio wordmark and a 3-column project directory beside a 7-column courtyard photograph. The lower edge of the photograph aligns with an oversized project number, not the title baseline. A narrow annotation column holds location, year, status, and a visible “View project” link. This should resemble a composed spread rather than a conventional hero.

Below, alternate large exterior photographs, paired material details, and a drawing on an off-white plate. A project detail view has a persistent compact contents list, a plain-language design rationale, accessible image captions, and a drawing toggle. The studio page exposes people, approach, and service scope. The inquiry page shows an honest expected response message without promising an unsupported timeframe.

At 390px, the project directory becomes a labeled project selector above the image. Metadata becomes a two-column definition list. Drawings use an explicit “Open drawing” action with zoom controls; do not require pinch gestures. The contents list becomes a disclosure. Keep the inquiry link in normal navigation rather than covering the photograph.

## Interaction and states

Project filters use real buttons with selected states and a visible count. Preserve focus on the chosen filter; announce the resulting count without reading every card. Empty results say “No projects match this combination. Clear filters.” Image failures retain the caption and aspect ratio. Inquiry validation preserves entered values, connects errors to fields, and moves focus to an error summary after submission. A successful submission displays the submitted project name and a confirmation message only after the server succeeds.

## GSAP motion choreography

| Trigger | Target | Duration / ease | Intended result |
|---|---|---|---|
| First render | Decorative photo frame | `gsap.timeline()`, 0.8s, `power3.out` | Reveal an inset frame from a 3% crop; text is already readable. |
| Project enters viewport | Caption rule | `ScrollTrigger`, 0.45s, `power2.out` | Draw a short rule once; never pin the article. |
| Drawing toggle | Drawing layer | `gsap.to()`, 0.24s, `power1.out` | Crossfade registered photo and drawing while preserving controls. |
| Filter changes | New project previews | 0.26s, `power2.out`, 0.035s stagger | Settle previews upward by 10px without delaying links. |

## Signature button

“Discuss a project” is a square-cornered moss button with a small inset directional arrow. On fine-pointer hover, move only the arrow 5px and expand its internal gap by 3px. Press scales the button to `0.975` over 0.08s; release returns to `1` over 0.42s using `back.out(1.7)`. This is a spring-style overshoot, not a physical spring simulation. Keep the hit area stationary and at least 48px high. Keyboard focus adds a 3px carbon outline with 4px offset. Reduced motion retains only color and focus changes.

## Accessibility and performance

Keep headings and links present before animation. Use `gsap.matchMedia()` to enable movement only when motion is allowed; revert timelines on route cleanup. Provide static drawing alternatives and descriptive image text. Never trap scrolling or hide content behind a reveal. Load responsive photography, reserve image dimensions, and animate transforms rather than layout properties.

## Build acceptance criteria

1. At 390px, metadata and drawing controls fit without horizontal page scrolling.
2. Every project, drawing switch, and inquiry field works with keyboard alone.
3. Reduced motion shows complete content immediately with no scale or crop animation.
4. A failed inquiry retains field values and exposes an actionable error message.
