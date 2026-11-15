# Meridian — A forecast desk with a clear time horizon

A weather intelligence workspace structured like an analyst’s chart table. Meridian and its locations, readings, and alerts are fictional demonstration data, not an operational forecast.

## Product and core flow

Build for outdoor operations coordinators comparing timing, confidence, and thresholds across several locations. The task is to find a suitable work window and document the assumptions behind it. Do not turn uncertainty into a decorative percentage badge.

Flow: choose a location → inspect the hourly horizon → compare wind and rainfall → set a threshold → save a planning window. Example: “North Quay · demo station” and “Updated 15 Nov 2026, 08:00 PHT · UTC+8.” Sample values explicitly use units: “Wind 18 km/h; gusts 29 km/h; rainfall 1.2 mm/h.” The save confirmation reads “Planning window saved: 10:00–12:00 PHT. Forecast may change.”

## Visual system

- Canvas: chalk `#EFF2F0`; primary text: navy `#142B3A`; secondary text: `#4E626E`; chart surface: `#FFFFFF`; cool accent: `#175D7A`; caution: `#8A4B12` on `#FFF0D6`; grid: `#CDD7DC`.
- Use **IBM Plex Sans**, Arial, sans-serif for interface text and **IBM Plex Mono**, Consolas, monospace for timestamps and readings. Tabular numerals align the forecast table.
- Desktop heading: 32/38 px; mobile: 26/32 px; readings: 28/34 px; body: 15/23 px. Use 8 px spacing, 24 px panel padding, and 40 px section gaps.
- Encode weather variables through labeled lines and patterned uncertainty bands. A muted blue band never means “safe” by itself.

## Screen composition

At **1440 px**, a 224 px location rail sits beside a main chart desk. The first viewport contains location and update time, a 24-hour timeline, an uncertainty legend, and the threshold editor. A 288 px right summary lists the currently selected window, source label, and notes. The chart carries time along a shared x-axis; wind and rainfall occupy aligned plots rather than competing dual axes.

Supporting views include a full forecast table, saved windows, and alert-rule history. Always provide a table equivalent to plotted data. Show stale data next to the timestamp, above the chart.

At **390 px**, replace the rail with a location selector. Stack time range, wind, rainfall, and the window summary. Default to six visible hours with explicit “Earlier” and “Later” controls; avoid forcing precision dragging. The threshold editor opens as an inline section, retaining the selected location and time. The complete table can scroll horizontally inside a labeled region with a visible scroll hint.

## Interaction and states

Arrow keys move a focused time cursor by one hour; Home and End jump to range boundaries. Screen-reader output includes time, unit, and the selected variable. Threshold fields have visible units and inline validation: “Enter a wind limit from 0 to 150 km/h.” Loading keeps the previous forecast labeled “Updating”; errors show its age and a retry action. Empty saved windows explain the save flow. A successful rule displays its actual condition, never just “Done.” Refreshes preserve the cursor, selected window, and row order.

## GSAP motion choreography

| Trigger | Target | Duration / ease | Result |
| --- | --- | --- | --- |
| Initial workspace mount | Panel shells | `gsap.timeline()`, 0.28 s, `power1.out` | Opacity 0 → 1; readings appear without counting up. |
| Cursor changes hour | Cursor line | 0.12 s, `power1.out` | The line glides to the selected tick; values update immediately. |
| Toggle a variable | Chart layer | 0.18 s, `power1.out` | Fade the layer while keeping axes and data extents stable. |
| Save a planning window | Saved marker | 0.30 s, `back.out(1.1)` | A small marker settles from scale 0.92; the chart remains still. |

Do not use ScrollTrigger, pinning, parallax, or animated chart redrawing on live updates. Time-series geometry must remain easy to compare.

## Signature button

“Save planning window” is a navy rectangle with a small bracket icon. Fine-pointer hover draws a 14 px underline inside the label’s allocated space. Press scales the inner label group to **0.985** over **0.06 s**; release uses **0.26 s**, `back.out(1.05)`, returning to 1. The restrained spring-style curve is an affordance, not data feedback. The click saves immediately, independent of animation. Focus uses a 3 px blue ring with a 2 px white gap. Reduced motion substitutes a static border emphasis and persistent success text.

## Accessibility and performance

Give chart patterns and status labels text equivalents. Announce stale data and completed actions in a polite live region, avoiding announcements on routine refreshes. Support zoom without hiding units. Render chart paths once and update only changed attributes; never animate large filters. Scope GSAP and clean it up on view changes. Reduced motion retains immediate cursor movement and static plot layers. A basic HTML table remains available without animation support.

## Build acceptance criteria

- Every reading exposes units, demo status, and the forecast update timestamp.
- Keyboard controls can select and save a complete time window without dragging.
- Refreshing data preserves the selected hour and never bounces or reorders rows.
- At 390 px and with reduced motion, all threshold errors and forecast values remain readable.
