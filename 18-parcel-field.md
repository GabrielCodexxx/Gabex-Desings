# Parcel Field — A command center for delivery exceptions

A logistics operations interface that puts accountable next actions ahead of decorative maps. Parcel Field, shipments, service levels, locations, and timestamps are fictional demo records.

## Product and core flow

Serve dispatch coordinators handling delayed, misrouted, or incomplete deliveries. The main job is to understand an exception, assign an owner, and choose a documented next step without losing the queue position.

Flow: triage the exception queue → open a shipment → read its event history → assign a resolution → verify the resulting status. Sample row: “PF-10482 · Address needs review · North depot · 42 min open.” The detail view says “Recipient unit number missing” and offers “Request address clarification” as a reviewable action. Any external message is represented as a draft with an explicit send step; opening a panel never sends anything.

## Visual system

- Canvas: `#EEF1F3`; white work surfaces: `#FFFFFF`; text: `#172F3C`; secondary text: `#4B616E`; primary action: `#164F70`; warning: `#8B4D12` on `#FFF0D4`; critical: `#9D3535` on `#FCE6E4`; borders: `#C9D3D9`.
- Use **Barlow**, Arial, sans-serif for compact headings and **Source Sans 3**, Arial, sans-serif for table content and forms. Shipment IDs use Consolas, monospace.
- Desktop title: 30/36 px; mobile: 25/31 px. Body and table: 15/22 px; labels: 13/18 px. Use 8 px spacing, 16 px cell padding, and 48 px minimum actionable rows.
- The visual language is ruled ledgers, numbered steps, and clean status labels. Severity always includes a word and icon; avoid turning every exception into a red surface.

## Screen composition

At **1440 px**, a 72 px navigation rail supports a queue with filter strip, compact summary counts, and a dense but readable table. The first viewport prioritizes shipment, issue, age, owner, and next action. Selecting a row opens a 440 px detail pane while the queue remains visible. Its first screen contains shipment ID, exception explanation, assigned owner, and resolution action; the event timeline follows.

Supporting screens include assignment history, a draft communication preview, and a resolution audit trail. A map is a secondary expandable view linked to address text, not the dashboard centerpiece.

At **390 px**, queue entries become stacked records with issue and age first. Selecting a record opens a separate detail route with a labeled “Back to queue” link that restores filters and scroll position. Put the resolution form inline above the history. Never squeeze the desktop table into unreadable columns or hide ownership behind hover.

## Interaction and states

Checkbox selection is independent of opening a row. Table headers expose sorting state; bulk assignment shows the exact selected count and excludes ineligible records with reasons. Loading uses stable row placeholders. Empty filtered results retain active filters and a reset action. Fetch errors preserve the last successful queue with a clear stale-data timestamp. If another coordinator changes a record, show a conflict with their latest state and let the user review before retrying. Success reads “PF-10482 assigned to Mara · clarification draft ready.” Keep resolved rows in place until the user refreshes or dismisses them.

## GSAP motion choreography

| Trigger | Target | Duration / ease | Result |
| --- | --- | --- | --- |
| Detail pane opens | Pane visual surface | `gsap.timeline()`, 0.22 s, `power2.out` | TranslateX 16 px → 0 with a short fade; focus moves predictably. |
| Expand event metadata | Metadata wrapper | 0.18 s, `power1.out` | Measured height transition; the event timestamp remains fixed. |
| Assignment succeeds | Owner confirmation icon | 0.28 s, `back.out(1.08)` | Icon settles from scale 0.9 in a reserved slot. |
| Close detail pane | Pane surface | 0.15 s, `power1.in` | Brief exit; return focus to the originating row action. |

No ScrollTrigger, chart scrubbing, animated counters, bouncing rows, or automatic movement of live queue records.

## Signature button

“Assign and prepare draft” is a blue rectangular control with a small forward chevron. On fine-pointer hover, the chevron moves **3 px** inside a fixed compartment. Press scales the button’s inner face to **0.99** over **0.05 s**. Release returns to 1 over **0.24 s**, `back.out(1.08)`: a restrained spring-style curve suitable for repeated operational work. Start the action immediately on click and show a pending label. A 3 px dark focus outline is independent of the animated layer. Reduced motion uses only background and label changes, with no scale or chevron travel.

## Accessibility and performance

Use semantic tables on desktop and meaningful grouped records on mobile. Keep error summaries linked to invalid fields and expose timestamps with timezone, such as “15 Nov 2026, 14:22 PHT · UTC+8.” Announce completed user actions, not every queue poll. Preserve selected IDs across refreshes and retain the focused row in any virtualization strategy. Scope GSAP contexts, cleanup on route changes, and disable transforms under reduced motion. All forms and queue actions work without animation.

## Build acceptance criteria

- A coordinator can identify the issue, owner, and next action without opening a map.
- Refreshes and successful actions do not move the focused queue row automatically.
- Conflicting assignments and failed saves preserve user input and explain the current state.
- Mobile navigation restores queue context, and preparing a draft never sends it automatically.
