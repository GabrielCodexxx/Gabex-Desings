# Voltgrid Operations — A calm charging command room

A fictional fleet-charging dashboard organized around exceptions, departure readiness, and actionable equipment status rather than decorative energy charts.

## Product and core flow

Design for a depot operator responsible for the next shift. The main flow is **choose depot → inspect departure readiness → investigate an exception → propose a charging change → confirm the result**. The first useful answer is “Which vehicles need attention before departure?”

Use clearly labeled demonstration data such as “Depot: Marikina East,” “Van 018 / Target 80% / Departure 06:30,” and “Charger C-07 / Communication lost.” Display an explicit “Demo data” badge and a last-updated timestamp. Distinguish observed charge from estimated completion. No savings, reliability, or emissions claims should appear without a defined data source.

## Visual system

- **Palette:** cool canvas `#F3F5F4`, panel white `#FFFFFF`, primary text `#142823`, secondary text `#52665F`, action green `#245C45`, warning ink `#7A4C00` on `#FFF0D1`, fault ink `#9D2F2B` on `#FDE9E6`. Pair every status color with text and an icon.
- **Type:** IBM Plex Sans with Arial fallback; IBM Plex Mono with monospace fallback for charger identifiers and times. Page title 30/38px desktop, 24/32px mobile; table text 14/20px; supporting copy 15/23px. Use tabular figures.
- **Layout:** 224px navigation rail, 32px content margins, 16px panel gaps at 1440px. At 390px, use a 56px header and 16px margins. Spacing scale: 4, 8, 12, 16, 24, 32px. Panels have 8px radii and restrained 1px borders.

## Screen composition

The desktop first screen contains a compact depot/time header, a departure-readiness strip, a wide exception table, and a right-hand charging-capacity timeline. The readiness strip states actual categories—“Ready,” “At risk,” and “Not connected”—with a timestamp and plain-language definitions. Avoid a row of indistinguishable metric tiles.

The exception table prioritizes fixed columns: vehicle, issue, departure, current charge, and recommended next action. Selecting a row opens a side panel with recent events and editable scheduling options. A change preview lists affected vehicles before confirmation. Separate screens cover chargers, schedules, and an immutable activity history.

On a 390px viewport, replace the table with an ordered list of exception summaries; preserve the desktop order and show issue, departure, and action without expansion. The timeline becomes a labeled hourly capacity list. A detail panel becomes a full-screen route with a visible back link. Keep filters in a disclosure, while depot and freshness remain visible.

## Interaction and states

Use native table semantics on desktop and semantic lists on mobile. Checkboxes enable explicit bulk selection with a selected-count bar. Do not reorder rows while a user is selecting or focused; offer a “New updates available” action. Loading reserves row height and exposes a single status message. An empty exception list says “No departure risks detected in the current data” and includes data age. A disconnected feed shows stale values, a prominent timestamp, and a retry action. Permission-denied changes explain the required role. Confirmation success names the schedule change only after acknowledgement; pending commands remain visibly pending.

## GSAP motion choreography

| Trigger | Target | Duration / ease | Intended result |
|---|---|---|---|
| Open vehicle detail | Side panel | `gsap.to()`, 0.22s, `power2.out` | Translate panel by 24px and fade in, with focus placed after it opens. |
| Expand event details | Supplemental event region | 0.18s, `power1.out` | Fade content while the container uses a measured height transition. |
| Select rows | Selection action bar | `gsap.fromTo()`, 0.16s, `power2.out` | Enter from 6px below without moving the table header. |
| Command confirmed | Confirmation icon | `gsap.timeline()`, 0.28s, `power2.out` | Draw one checkmark; table values update without bounce. |

Use no `ScrollTrigger` pinning or numeric count-up effects in operational views. Cancel obsolete transitions when rapidly switching vehicles.

## Signature button

“Review charging change” has a fixed-width label region and a small right arrow. On fine-pointer hover, the arrow advances 3px over 0.16s. Press scales the inner visual surface to `0.985` over 0.07s; release uses `back.out(1.2)` over 0.3s. This restrained spring-style response uses easing, not simulated physical dynamics. The outer button and 48px hit area never shrink. Show a strong green focus outline, keep pending text readable, prevent duplicate requests, and replace motion with an immediate state change under reduced motion.

## Accessibility and performance

Manage panel focus and return it to its source row. Label capacity charts with equivalent values. Announce significant status changes through a polite live region, never every telemetry tick. Use `gsap.matchMedia()` for reduced motion and clean up route animations. Virtualize only when necessary and preserve accessibility. Animate panels, not live readings; reserve all data-region dimensions.

## Build acceptance criteria

1. A stale data feed cannot appear indistinguishable from a healthy feed.
2. Updating telemetry never moves a focused or selected row.
3. A schedule preview identifies all affected vehicles before confirmation.
4. At 390px and with keyboard alone, an operator can review and submit a permitted change.
