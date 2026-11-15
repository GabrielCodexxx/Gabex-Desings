# Common Ground — Choose a Place to Work

A coworking booking tool that combines the calm of an architectural plan with the clarity of a travel checkout. Common Ground, its spaces, inventory, and rates are fictional.

## Product and core flow

For independent workers and small teams choosing a desk or room for a specific date. The task is finding a suitable space and understanding the complete booking before committing.

Flow: choose location and local date → filter by needs → select a desk or room → review time, amenities, and itemized sample price → reserve → receive confirmation from the booking system. Example: “Window Desk 12 / Quiet zone / Near a power outlet.” Label prototype prices “Sample rate” and never create a false live-availability indicator.

Use “Review reservation” before commitment, then “Confirm reservation” on the final step. State the location's timezone beside the booking time.

## Visual system

- Warm ground `#F6F3EC`; ink `#202B32`; blue action `#1F4CB7`; selected tint `#E1E9FF`; available outline `#53675E`; occupied fill `#D5D8D3`; caution text `#80521D`; dividers `#CBCFC8`.
- DM Sans with Arial/sans-serif fallback for interface; Fraunces with Georgia/serif fallback for room names and welcoming editorial fragments.
- Desktop: 40/46 px title, 24/30 panel title, 16/25 body, 13/20 metadata. Mobile: 30/36 title, 22/28 panel title, 16/25 body.
- Use 8 px spacing, 32 px desktop page padding, 20 px mobile padding, 12 px panel corners, and 48 px controls. Floorplan furniture uses clear silhouettes without photographic shadows.

## Screen composition

At 1440 px, a 72 px masthead leads into a toolbar with location, date, start/end time, and an Availability legend. The main region gives seven columns to a floorplan and four to a selected-space panel, with a one-column gap. Keep the plan title, selection summary, and Review reservation visible above the fold. A labeled switch changes between Map and List.

The detail panel contains one modest room image, name, capacity, access information, included amenities, and an itemized rate. A review screen repeats location, local times, attendee count, cancellation terms supplied by the business, and the final total before submission. The confirmation is a durable page, not a disappearing toast.

At 390 px, default to List view. Each result gives name, category, availability text, and a Select button. Map is an optional separate view with zoom controls and a matching selectable list. Selection opens an inline detail section with a focusable heading. A bottom review bar may be sticky only if it has safe-area padding and never obscures content or the onscreen keyboard.

## Interaction and states

Desktop map seats are real keyboard controls with accessible names such as “Desk 12, quiet zone, available.” Map and list selection stay synchronized. Unavailable seats expose their status without appearing selectable. Date changes preserve filters and explain any invalidated selection. Loading shows a stable plan placeholder and text. No results suggests another date or fewer filters. A booking conflict retains the user's details and offers alternatives; success appears only after authoritative confirmation. Disable duplicate submission while pending and expose a textual status.

## GSAP motion choreography

| Trigger | Target | Timing and API | Intended result |
| --- | --- | --- | --- |
| Select a space | Decorative selection outline | `gsap.to()`, opacity 0 → 1, 0.18 s, `power1.out` | Identify the choice immediately without moving the seat. |
| Selected detail changes | Detail content wrapper | `gsap.fromTo()`, y 8 → 0 and opacity, 0.25 s, `power2.out` | Associate new details with the selected space. |
| Expand amenities | Decorative caret | 0.22 s rotation, `power2.out` | Disclosure content opens immediately with correct expanded state. |
| Reservation succeeds | Confirmation check stroke | `gsap.timeline()`, 0.35 s, `power2.out` | A small acknowledgement after real confirmation; the message is already visible. |

No ScrollTrigger, animated map panning, bouncing seats, or automatic reordering during selection.

## Signature button

Review reservation is blue with white text and a compact right-facing chevron. Its inner face presses to 0.975 over 0.09 s and releases over 0.42 s using `back.out(1.2)`. A fine-pointer hover shifts only the chevron 3 px right. Keep focus on the stable outer control with a 3 px dark outline separated by a 2 px gap. Restore the face after pointercancel, blur, and disabled-state changes. Activation advances immediately; it never waits for the spring-style easing. Reduced motion uses a darker fill and no transform.

## Accessibility and performance

Provide a complete list alternative to the floorplan, accessible date entry, real field labels, and error summaries. Do not require dragging, precise map targeting, or distinguishing colors. Keep selected state in text. Render the floorplan as lightweight SVG with a sensible DOM size; load room photography after essential controls. Respect reduced motion by skipping all movement and drawing a static confirmation check. Maintain scroll position and focus when availability refreshes.

## Build acceptance criteria

- A keyboard-only user can select, review, and confirm a booking entirely through List view.
- At 390 px, booking details and validation remain visible with the software keyboard open.
- A simulated inventory conflict preserves user input and never displays a success state.
- Map/list selection, itemized totals, timezone labels, and reduced-motion feedback remain consistent.
