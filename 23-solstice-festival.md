# Solstice — A Festival Poster You Can Plan With

A music festival site that combines expressive screen-printed artwork with a precise, usable running order. Solstice, its artists, venue, schedule, and ticket details are fictional.

## Product and core flow

For attendees choosing performances, building a personal agenda, and finding ticket information. The key task is planning a day without losing track of clashes or stage locations.

Flow: choose a day → browse stages and set times → save a performance → resolve a clash → review My plan → inspect ticket options. Sample content: “Saturday / Orchard Stage / 18:20–19:05 / Paper Satellites.” Prototype dates are 17–18 July 2027; label them fictional and show the venue's configured timezone rather than assuming the visitor's timezone.

Use “Add to my plan,” “Saved on this device,” and “These sets overlap by 15 minutes.” Keep ticket availability separate from a saved agenda.

## Visual system

- Poster yellow `#FFC94B`; dark ink `#182117`; deep violet `#503184`; paper `#FFF9E9`; muted text `#4D564B`; divider `#B8AC83`; dark red error `#9E2727`.
- Archivo Black with Impact/sans-serif fallback for poster headings; Barlow with Arial/sans-serif fallback for schedules and controls. Use tabular numerals for times.
- Desktop: 116/106 px display, 42/46 section heading, 18/26 artist title, 15/23 supporting text. Mobile: 58/56 display, 32/36 section title, 18/25 artist title, 16/24 body.
- Use 8 px spacing, 40 px desktop gutters, 20 px mobile gutters, 48 px tap targets, and mostly square edges. Two-color cut-paper shapes and visible print misregistration are restricted to artwork, not text.

## Screen composition

At 1440 px, the opening fold is an asymmetrical poster: giant festival name in the left eight columns, a compact date/location/ticket strip on the right, and a cropped sun illustration along the lower edge. A visible “Explore the lineup” anchor links to the timetable. Keep ticket information readable without any motion.

The timetable has a top day selector, stage columns, and an explicit time rail. Each performance shows artist, start/end, stage, and Add to my plan. A nearby agenda panel lists saved sets chronologically with conflict text. Artist pages contain a short introduction, access to an explicitly user-activated audio preview if supplied, set details, and the save action. Venue and access information get their own navigable section.

At 390 px, default to a chronological list with day and stage filters above it. A “My plan (3)” link opens a dedicated agenda view, not a tiny side drawer. Preserve the day selection across views. The poster art reduces to a compact crop; it never pushes the schedule behind multiple screens of decorative content.

## Interaction and states

Use actual buttons for save toggles, reflecting selection in visible text and `aria-pressed`. Saving creates a local state immediately and reports its storage scope. If storage fails, say “Saved for this visit only.” Empty plans suggest browsing the lineup. Empty filtered results offer Clear filters. Cancelled or changed sets show explicit labels and retain the old value only where helpful. A clash is an advisory with actions to inspect both sets, never an automatic deletion. Ticket actions show supplied availability and pricing; prototypes say “Sample ticket options.”

## GSAP motion choreography

| Trigger | Target | Timing and API | Intended result |
| --- | --- | --- | --- |
| First load | Decorative sun and poster frame | `gsap.timeline()`, 0.7 s, `power3.out`; rotation -12 → 0 and y 16 → 0 | One energetic entrance without loops or flashing. |
| Lineup section enters | Section artwork only | `ScrollTrigger`, once, 0.5 s, `power2.out`, y 20 → 0 | Continue the print-poster rhythm while schedule text stays static. |
| Day selection | Day's underline | 0.22 s, `power3.out` | Follow selection without sliding or bouncing the timetable. |
| Save a set | Decorative bookmark tab | 0.28 s, `back.out(1.4)`, y -4 → 0 | A small physical-feeling accent; saved text changes immediately. |

No scroll pinning, autoplay music, flashing stage effects, or animated schedule rearrangements.

## Signature button

Add to my plan is a violet tab with a plus that becomes a check. The inner tab presses to scale 0.95 over 0.08 s and returns over 0.48 s with `elastic.out(1, 0.55)`; constrain it inside a reserved visual area. This is a spring-style curve, not physical simulation. Fine-pointer hover tilts the small plus by 8 degrees, never the label. Keep a 3 px ink focus ring outside the stable button. Restore its scale on cancellation, blur, or removal. Update the plan on activation without waiting for the tween. Reduced motion changes the label and icon instantly without scaling or rotation.

## Accessibility and performance

Give timetable events a sensible DOM reading order and always include full times as text. Do not rely on color to identify stages or conflicts. Allow text zoom and use persistent links for access information. Avoid running animation inside audio or video; media starts only on explicit play. Use compressed artwork and static SVG shapes. In reduced-motion mode, show the final poster composition and disable all spring/rotation effects. Revert GSAP contexts when changing routes.

## Build acceptance criteria

- An attendee can build and inspect a plan at 390 px without horizontal page scrolling.
- Conflicting saved sets remain visible with specific overlap information and user-controlled resolution.
- Keyboard and touch users get identical saving, filtering, and ticket information.
- With reduced motion or failed local storage, the schedule and temporary planning flow remain fully usable.
