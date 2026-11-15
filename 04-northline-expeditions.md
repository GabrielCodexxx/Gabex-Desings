# Northline Expeditions — A route journal you can plan with

A fictional alpine-trip planner that combines a field notebook, a readable route profile, and a practical day-by-day builder; this is product-design inspiration, not real travel or safety advice.

## Product and core flow

Design for a small group comparing a guided mountain itinerary and organizing its logistics. The flow is **choose a fictional route → inspect daily requirements → adjust the day sequence → review inclusions and open questions → request an itinerary**. Show the itinerary's assumptions clearly instead of turning landscapes into a substitute for information.

Example content: “Pine Saddle Traverse / Sample route / 4 days,” “Day 2: Forest approach to Ridge Camp,” and “Route details are fictional and require qualified review.” Distance, altitude, conditions, and capacity are explicit placeholders until backed by verified operational sources. A request is an inquiry, not a booking or a guarantee of route suitability. Use “Ask about this itinerary” as the closing action.

## Visual system

- **Palette:** map paper `#F0F1E7`, dark spruce `#173C32` text and actions, muted sage `#566B59` supporting text, pale moss `#DCE4CD` selected regions, rust `#934323` emphasis, white `#FFFFFF` itinerary sheets. Map contours use `#CAD1BE` decoratively.
- **Type:** Fraunces with Georgia fallback for route titles; Source Sans 3 with Arial fallback for descriptions; Space Mono with monospace fallback for day numbers. Titles 76/80px desktop and 42/46px mobile; body 17/27px; labels 13/18px.
- **Geometry:** 64px desktop outside margins, 24px gutters, 12 columns; 20px mobile margins. Spacing: 8, 16, 24, 40, 64, 96px. Rounded itinerary tabs use 10px radii; maps and photographs remain rectangular.

## Screen composition

At 1440px, the opening composition places the route title and description across the upper left, a large annotated landscape across the center, and a vertical day index on the right. A narrow lower band shows trip format, fictional duration, and an inquiry link. The photograph supports the planning information; it does not obscure it.

The route detail area pairs an illustrated topographic map with a day ledger. Selecting a day highlights its map segment and exposes objectives, expected logistics, included services, and open questions. A separate review screen lists the selected day order and unanswered items. The operator profile and preparation pages use readable prose and source placeholders for information requiring verification.

At 390px, place the day ledger before the map. The map has a text route summary and a deliberate “Explore map” control, avoiding scroll capture. Day tabs become a vertical list with expanded details inline. Reordering offers Move up/Move down buttons even if desktop dragging is provided. Review appears as a simple numbered itinerary; images become supporting breaks between content sections.

## Interaction and states

Route selection uses visible names, not unlabeled map markers. Map controls include keyboard zoom and reset. Highlighted segments also have a patterned stroke and text label. Draft changes save explicitly and announce saved state only after persistence. An empty plan invites “Add a sample route.” A missing map shows the route summary and retry control. An invalid sequence explains the conflict in words and retains the previous valid order. Request errors preserve the itinerary and contact fields; a success screen calls it an inquiry and offers a copy of the submitted plan.

## GSAP motion choreography

| Trigger | Target | Duration / ease | Intended result |
|---|---|---|---|
| Opening content ready | Decorative contour lines | `gsap.timeline()`, 0.9s, `power2.out` | Fade contours behind the already-visible route heading. |
| Select itinerary day | SVG route segment | `gsap.fromTo()`, 0.48s, `power2.out` | Reveal a segment using stroke dash offset; do not move the whole map. |
| Day details enter view | Margin annotation | `ScrollTrigger`, 0.35s, `power2.out` | Slide a short marker by 10px, once per section. |
| Reorder completes | Moved day row | `gsap.to()`, 0.2s, `power2.out` | Settle an explicit selection highlight without changing keyboard focus. |

Use native page scrolling. Never suggest that animation verifies a route's safety or suitability.

## Signature button

“Add to itinerary” is a spruce outline button with a small folded-map icon. Fine-pointer hover unfolds the icon by 6 degrees. Press scales its visual surface to `0.965` over 0.09s; release returns over 0.4s with `back.out(1.5)`. This gives a spring-style response through easing. The icon becomes a static check only when the draft update succeeds. Preserve a 48px target, visible 3px focus outline, and a label that remains readable during pending state. Reduced motion uses color and text changes alone.

## Accessibility and performance

Provide the itinerary without requiring map interaction. Use `gsap.matchMedia()` for motion preferences, remove scroll animations when reduced motion is requested, and clean up listeners on route changes. Keep map geometry lightweight, defer enhanced mapping, and reserve media space. Do not auto-pan while a visitor is reading or interacting. Treat unverified condition and safety information as unavailable, never as reassuring sample facts.

## Build acceptance criteria

1. At 390px, a visitor can understand and edit the itinerary without manipulating the map.
2. Reordering works with keyboard controls and preserves focus on the moved day.
3. Every illustrative operational fact is visibly marked as sample or unavailable.
4. Reduced motion uses static route highlighting and immediate state updates.
