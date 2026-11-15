# Pulseboard — Tactical analysis without the visual noise

An esports match-analysis workspace built around round structure, decisions, and shared notes. Pulseboard, the game, teams, maps, and match statistics are fictional demonstration content.

## Product and core flow

Serve team analysts reviewing a recorded match with a coach. The goal is to connect a moment on a tactical map to a round outcome and create a review note that can be found later. Avoid the stereotypical neon gamer dashboard and decorative live counters.

Flow: choose a match → select a round → scrub a recorded event → inspect a player or zone → save an annotated moment. Sample header: “Glass Owls vs. Red Current · Practice set 04 · Demo match.” A sample note says “Round 08 · 00:42 — pause the rotation until the east lane is checked.” Statistics are labeled demo data and retain clear denominators.

## Visual system

- Background: ink `#111A24`; panels: `#192633`; raised selection: `#243747`; text: `#E9F0F2`; muted text: `#A5B7C4`; team A: `#75D3C4`; team B: `#F2BE83`; boundary lines: `#425868`.
- Pair **Sora**, Arial, sans-serif for headings and controls with **IBM Plex Mono**, Consolas, monospace for round numbers, timestamps, and compact statistics.
- Desktop heading: 28/34 px; mobile: 24/30 px; body: 14/22 px; key score: 40/44 px. Use 4 px increments, 16 px panel padding, and 24 px major gutters.
- Team identity uses shape and initials as well as color. Map glyphs are consistent vector symbols. No chromatic glow, scanlines, or constantly moving backgrounds.

## Screen composition

At **1440 px**, use a three-zone analyst desk: 220 px match and round rail, flexible map and event timeline, and a 320 px note inspector. The first viewport shows the selected round, a static tactical map, explicit playback controls, a labeled event track, and the current annotation. The scoreboard is compact and subordinate to analysis.

Supporting screens include a round comparison table and a review queue organized by explicit tags such as “Rotation” and “Utility.” Selecting a comparison row opens the same event context, preserving orientation.

At **390 px**, show match summary, round selector, map, playback controls, then notes. The inspector becomes an inline tab set labelled Events / Notes / Players. Provide a textual event list with jump buttons; the map is not the only route to information. Use full-screen map inspection only when requested, with a visible close button and restored focus.

## Interaction and states

Space toggles playback only when the player region is focused, never while typing. Arrow keys step the focused scrubber; a visible time field supports direct entry. Keep draggable annotation tools paired with “Add note at current time.” Loading retains the selected round and shows a status label. Empty notes say “Add the first coaching note for round 08.” A failed save retains the note as an explicitly unsaved draft. Success shows its round and timestamp. Incoming annotations do not steal focus or automatically reorder the queue.

## GSAP motion choreography

| Trigger | Target | Duration / ease | Result |
| --- | --- | --- | --- |
| Match workspace opens | Panel shells | `gsap.timeline()`, 0.25 s, `power1.out` | A simple opacity entrance; match data is immediately readable. |
| User steps to an event | Event marker halo | 0.20 s, `power2.out` | One ring expands from scale 0.8 to 1 and fades; no repeating pulse. |
| Select a player | Corresponding map glyph | 0.16 s, `power1.out` | Outline and opacity clarify selection without changing its coordinates. |
| Annotation saved | Small note flag | 0.34 s, `back.out(1.2)` | Flag settles from y: -3 into its fixed slot. |

Do not use ScrollTrigger or pin the workspace. Replay positions are authoritative data, not tweened approximations. Seek operations show the selected state immediately.

## Signature button

“Save review note” uses a mint face and dark text with a bracket icon. Fine-pointer hover slides only the bracket ends outward by **2 px**. Press scales the inner face to **0.98** over **0.065 s**; release returns over **0.30 s**, `back.out(1.2)`. The brief spring-style response never shakes the note editor or map. Save begins on click, with a pending state that prevents duplicate submissions. A 3 px warm-white focus ring stays outside the animated face. Reduced motion removes bracket travel and scale; the pending and saved labels remain.

## Accessibility and performance

Offer text equivalents for map events and retain team labels in monochrome. Use semantic tab controls and a labeled range input for the timeline. Distinguish unsaved drafts visibly and programmatically. Respect `prefers-reduced-motion`; scope and revert GSAP work on match changes. Virtualize long event lists carefully while retaining the focused item. Render replay updates directly and animate only decorative feedback, avoiding per-frame layout work.

## Build acceptance criteria

- A user can create and retrieve a timestamped note using only the keyboard.
- Team identities and selected players remain distinguishable without color.
- Changing rounds never loses an unsaved note without an explicit decision.
- At 390 px and reduced motion, the event list exposes the same review actions as the map.
