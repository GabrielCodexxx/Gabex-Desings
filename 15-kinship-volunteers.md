# Kinship — Volunteering organized around real commitments

A civic volunteering interface that feels like a well-kept neighborhood noticeboard. Kinship, organizations, events, and availability are fictional design examples.

## Product and core flow

Serve people fitting a useful shift into ordinary life and coordinators who need reliable attendance. The primary decision is “Can I do this, at this time, with these requirements?” Make that answer visible before a signup form.

Flow: choose availability → compare opportunities → review duties and access details → reserve a shift → receive an on-screen preparation checklist. Example listing: “Garden sorting morning · Saturday, 21 Nov 2026 · 09:00–11:00 PHT.” The detail copy says “Seated tasks available. Tools provided. Contact the organizer for step-free entry details.” Treat those as fictional listing fields, not verified claims. A clear commitment summary precedes “Reserve this shift.”

## Visual system

- Paper canvas: `#FAF4E7`; dark text: `#23382F`; moss accent: `#355E48`; pale green surface: `#E1EBDD`; terracotta accent: `#9E4C35`; rule: `#C8C8B5`.
- Pair **Fraunces**, Georgia, serif for warm section titles with **Public Sans**, Arial, sans-serif for tasks, forms, and schedules. Use the serif sparingly, without playful letter wobble.
- Desktop title: 50/56 px; mobile: 34/40 px. Body: 16/26 px. Labels: 14/20 px. Keep a 6 px spacing rhythm, 24 px card padding, and generous 48 px gaps between decision stages.
- Visual motifs are punched-paper tabs, a restrained date stamp, and line-drawn tools. Opportunity photos show the actual type of work rather than abstract smiling portraits.

## Screen composition

At **1440 px**, divide the page into a 280 px availability panel and an opportunity ledger. The first viewport begins with “A few hours can have a place” aligned left, followed by date filters and three full-width opportunity rows. Each row has a calendar tile, task name, location, duration, access information, and remaining demo capacity. The detail view uses a two-thirds reading column and a one-third commitment summary.

The coordinator view groups volunteers by shift with explicit attendance statuses. A personal schedule shows upcoming commitments and cancellation terms, not a gamified impact score.

At **390 px**, availability becomes an expandable inline filter with a concise applied-filter summary. Opportunity rows become stacked sheets with the date above the title and the requirement list still visible. The commitment summary moves before the signup action. Avoid a floating action that hides cancellation terms or emergency contact information.

## Interaction and states

Use native date fields and checkboxes with clear labels. Filtering announces the number of matching opportunities while keeping focus on the changed control. Empty results say “No Saturday morning shifts match these filters” and offer a reset. Loading reserves the result area height; failed loading leaves filters intact with retry. If the final place is taken, preserve entered form values and offer a waitlist with explicit consent. Confirmation shows the exact date, local timezone, meeting point, and cancellation link. A cancellation dialog returns focus to its trigger.

## GSAP motion choreography

| Trigger | Target | Duration / ease | Result |
| --- | --- | --- | --- |
| First results load | Opportunity sheets | `gsap.timeline()`, 0.34 s, `power2.out`, 0.04 s stagger | Sheets rise only 8 px; all actions are usable immediately. |
| Expand duties | Details content wrapper | 0.22 s, `power1.out` | A measured height transition respects the final content size. |
| Reserve succeeds | Date-stamp illustration | 0.40 s, `back.out(1.4)` | Stamp settles from rotation -4° and scale 0.94 beside the confirmation. |
| Cancel confirmed | Existing status chip | 0.18 s, `power1.out` | Crossfade its label without removing or moving the focused row. |

No scroll pinning or scroll-triggered hiding. The schedule is a functional list, not a cinematic timeline.

## Signature button

“Reserve this shift” resembles a solid moss paper tab with a pale inset border. Fine-pointer hover lifts a small corner mark by 2 px; the label stays still. Press scales the inner face to **0.97** over **0.09 s**. Release returns to 1 over **0.42 s**, `back.out(1.45)`. This supplies a friendly spring-style overshoot without simulating physical mass. Commit on click; do not wait for the bounce. A 3 px terracotta focus outline has a paper separation gap. Reduced motion removes the lift and scale and keeps the selected border and status message.

## Accessibility and performance

Use plain commitment language, visible required-field labels, and an error summary linked to each invalid field. Do not require a phone number for browsing. All controls meet a 44 px target. Respect reduced motion through `gsap.matchMedia()` and render expanded text immediately in that mode. Cleanup scoped timelines when changing routes. Keep illustrations lightweight and disable stagger after the first load so filtering stays calm.

## Build acceptance criteria

- A first-time visitor can identify duties, time, access details, and cancellation terms before submitting.
- A full shift never displays a successful reservation; entered form values survive the conflict.
- Keyboard focus remains predictable when filtering, reserving, and closing a cancellation dialog.
- Mobile and reduced-motion versions expose the same preparation checklist and confirmation details.
