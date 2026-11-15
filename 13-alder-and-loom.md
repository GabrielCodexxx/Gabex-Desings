# Alder & Loom — Furniture as a material study

A quiet furniture configurator built around grain, joinery, and room proportions. Alder & Loom, all products, and all prices below are fictional design content.

## Product and core flow

Design for homeowners and interior designers choosing one considered piece, beginning with the **Rowan reading chair**. The main job is to compare materials without losing the relationship between appearance, dimensions, price, and delivery.

Flow: open a collection → inspect a chair → choose wood and upholstery → check dimensions against a room → save a configuration or add it to the bag. Sample copy: “Oak, softly brushed. Bouclé, warm chalk.” The decision summary says “Your chair: natural oak / chalk wool” instead of an opaque variant code. Clearly label the sample price, “Demo price: ₱28,400.”

## Visual system

- Background: warm paper `#F3F0E8`; panels: `#E7E3D9`; text: charcoal `#242923`; secondary text: `#575E54`; accent: forest `#355745`; dividers: `#C8C6BA`.
- Pair **Source Serif 4**, Georgia, serif for product names with **Manrope**, Arial, sans-serif for controls. Reserve the serif for short editorial statements; material codes remain sans-serif.
- Desktop title: 60/64 px; mobile: 38/42 px. Body: 16/25 px; labels: 13/18 px. Use a 4 px spacing base, 24 px gutters, and 80 px collection breaks.
- Photography uses a consistent neutral side light. Include close crops of joints and upholstery alongside honest full-product views. Avoid showroom stock imagery behind text.

## Screen composition

At **1440 px**, use a 12-column page with a 64 px header. The first viewport allocates seven columns to the chair image and five to a product ledger. Product name sits beside a small “01 / Reading chairs” index. The ledger stacks wood swatches, fabric choices, availability, dimensions, and one full-width purchase button. Price changes appear next to their cause.

Below, a three-part material library pairs a 1:1 texture crop, a tactile description, and care notes. The dimensions screen uses a measured line drawing with text equivalents. Saved configurations use a comparison table with one row per attribute.

At **390 px**, place image → title and price → materials → delivery → purchase in reading order. Swatches wrap into labeled tiles instead of a horizontal carousel. A compact purchase bar appears only after the original button leaves view, with enough bottom padding to avoid covering content. Comparison becomes stacked attribute groups.

## Interaction and states

Wood and fabric controls are native radio groups with visible names, selected outlines, and arrow-key navigation. Selecting a material updates a pending image state immediately; preserve the previous image until the replacement loads. Announce the new configuration once, not every animation frame. An unavailable combination explains “Chalk wool is unavailable with this finish” and offers available choices. A failed image retains its alt text and a retry action. Empty saved items show “Keep a configuration to compare it here.” Adding to the bag confirms the exact combination and quantity, with a link to review it.

## GSAP motion choreography

| Trigger | Target | Duration / ease | Result |
| --- | --- | --- | --- |
| First product render | Product image and title | `gsap.timeline()`, 0.55 s, `power2.out`; title follows by 0.08 s | Image settles from y: 16; title fades without delaying controls. |
| Material selection | Old/new texture images | 0.24 s, `power1.out` | Crossfade only after the next asset is ready; never morph wood grain. |
| Material library enters viewport | Image crop frame | ScrollTrigger once, 0.60 s, `power2.out` | A subtle clipped reveal from the bottom; no pinned scroll. |
| Save configuration | Bookmark icon | 0.32 s, `back.out(1.25)` | Scale 0.85 → 1 inside a fixed-size button. |

## Signature button

"Add this chair" is forest with paper text, squared corners softened to 6 px, and a small plus icon. On a fine-pointer hover, lift the plus icon 2 px; preserve the button’s hit area. Pointer down scales the inner visual to **0.975** over **0.08 s**. Release returns to **1** over **0.38 s**, `back.out(1.25)`. This is a spring-style easing curve, not a physical spring. Activate the purchase on click immediately. Keyboard focus gets a separate 3 px charcoal outline with a paper gap. Under reduced motion, remove translation and overshoot; retain color, focus, and confirmation text.

## Accessibility and performance

Keep controls at least 44 px high and material names visible without hover. Supply dimension text alongside diagrams. Use responsive image sources and preload only the primary product view. Animate opacity and transforms, not layout. Mount GSAP in a scoped context, revert on teardown, and use `gsap.matchMedia()` for reduced motion. Every reveal must leave content visible if JavaScript fails.

## Build acceptance criteria

- A keyboard user can select every available material and add the exact configuration.
- At 390 px, the purchase bar never covers fabric names or delivery information.
- Rapidly changing materials never displays an older image as the final selection.
- Reduced motion shows complete content with no entrance movement or button overshoot.
