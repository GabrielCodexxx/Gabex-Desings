# Vesper — The Anatomy of Time

A watchmaker's digital showroom built like an annotated technical folio: macro photography, engraved rules, and quiet mechanical reveals. Vesper, its products, and all sample details are fictional.

## Product and core flow

For collectors who want to understand a watch before arranging a viewing. The primary task is choosing a reference and requesting an appointment.

Flow: explore the featured reference → inspect dial, movement, and dimensions → compare strap finishes → choose a viewing location → submit a request. Write “Request a private viewing” and “Your preferred time is a request; the atelier will confirm availability.” Never imply the request is an immediate booking.

Example collection entry: “Reference 03 / Brushed steel / Slate dial.” Use genuinely supplied specifications in production; prototype values must remain labeled as sample content.

## Visual system

- Canvas `#EFE9DD`; text `#23211D`; dark section `#253830`; inverse text `#FAF7EE`; bronze ornament `#896B47`; rules `#CCC3B3`. Bronze is for large accents and illustrations, not body text.
- Bodoni Moda for display, with Georgia/serif fallback; Manrope for interface, with Arial/sans-serif fallback. Labels use tabular numerals where appropriate.
- Desktop: 96/96 px display, 44/48 section titles, 16/26 body, 12/18 labels. Mobile: 48/50 display, 30/36 headings, 16/25 body.
- Use an 8 px spacing base, 80 px desktop gutters, 24 px mobile gutters, 128 px chapter spacing. Controls have 48 px minimum touch height. Hairline dividers and square image frames replace rounded cards.

## Screen composition

At 1440 px, place a restrained 88 px masthead above a 12-column spread. The opening title occupies four columns on the left, a watch macro occupies seven on the right, and a narrow numbered chapter rail completes the composition. Put the reference name, short material description, and viewing CTA in the opening viewport. No video is needed.

Below, alternate full-width macro details with two-column technical annotations. A movement illustration has three separately labeled layers and a visible “Show layers” control. A strap comparison uses equal-size swatches beside a stable watch image; selection changes material and caption together. End with a viewing form and an explicit request summary.

At 390 px, use one image followed by title and CTA, then a vertical chapter list. Convert annotations into inline captions. Replace exploded artwork with a static stack and optional next/previous detail controls. Do not shrink the desktop diagram into illegibility.

## Interaction and states

Swatches are labeled radio buttons with selected text and a check, not color alone. The layer disclosure works with Enter and Space. The viewing form preserves entered values after validation errors and focuses an error summary on failed submission. Distinguish submitting, request received, and unavailable dates. If an image fails, retain its caption and technical information. A gallery with no additional assets simply omits its pager.

## GSAP motion choreography

| Trigger | Target | Timing and API | Intended result |
| --- | --- | --- | --- |
| First ready frame | Macro image and title block | `gsap.timeline()`, 0.75 s, `power3.out`; image scale 1.025 → 1; title y 16 → 0 | A single, composed entrance; CTA is usable immediately. |
| Chapter enters | Illustration and annotation rule | `ScrollTrigger`, once, 0.55 s, `power2.out`, y 18 → 0 | Editorial rhythm with normal document scrolling. |
| Activate Show layers | Three illustration planes | Reversible timeline, 0.7 s, `power3.inOut`, maximum separation 32 px | Explain the mechanism without rotating the page or pinning scroll. |
| Change strap | Image overlay and caption | 0.22 s opacity crossfade, `power1.out` | Stable composition and immediate selected state. |

The overshoot below is a spring-style easing curve, not a physical spring simulation.

## Signature button

“Request a private viewing ↗” is a solid forest rectangle with a small bronze edge notch. Animate an inner visual face; keep the semantic button and focus outline stationary. Fine-pointer hover moves the arrow 3 px diagonally over 0.2 s. Press scales the face to 0.968 over 0.1 s; release returns to 1 over 0.56 s using `back.out(1.45)`. Cancel, pointer leave while pressed, and keyboard blur restore the resting state. Navigation or submission starts on activation without waiting for the animation. Use a visible 3 px high-contrast focus ring. Reduced motion keeps the face still and changes the fill instantly.

## Accessibility and performance

Use semantic headings, real form labels, meaningful captions, and an accessible gallery order. Support 200% text zoom without hiding controls. Load one responsive hero image eagerly and defer later macro assets. Restrict animation to transforms and opacity where possible; keep diagram layers few. With reduced motion, reveal all content statically and make the layer state change immediate. No parallax, automatic zoom loops, or scroll interception.

## Build acceptance criteria

- At 1440 px, the opening viewport communicates reference, material, and primary action without waiting for animation.
- At 390 px and 200% text zoom, swatches, captions, and the request form remain usable without page-level horizontal scrolling.
- Keyboard users can choose a strap, inspect the diagram, and submit or correct the request.
- Reduced motion produces a complete static page with immediate button feedback and no hidden chapters.
