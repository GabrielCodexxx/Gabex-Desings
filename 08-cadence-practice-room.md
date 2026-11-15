# Cadence — The Practice Room

A focused musician's workspace built like an annotated rehearsal desk, with a score rail, task timeline, and deliberately restrained transport. Cadence and all sessions below are fictional.

## Product and core flow

For musicians turning a long practice session into a short, repeatable routine. The flow is select a piece → mark a difficult passage → set a practice loop → start explicitly → add a reflection. Sample session: “Evening study / 25 minutes,” passage “Bars 18–26,” and note “Keep the left hand softer on the return.” The main action reads “Start 6-minute passage.” Duration is adjustable before starting; progress is never framed as a streak penalty.

## Visual system

- Deep canvas `#181B1D`; work surfaces `#242A2D`; primary text `#F3F0E8`; muted text `#BCC4C6`; acid accent `#D8E77A`; recording/error red `#FA9A91`; focus cyan `#8CD9E9`.
- IBM Plex Sans for headings and instructions, fallback Arial/sans-serif; IBM Plex Mono for bar numbers and timing, fallback Consolas/monospace. Title: 36/42 px desktop and 28/34 px mobile. Body: 16/24 px. Numerical timer: 48/52 px, tabular figures.
- A 6 px baseline supports music-style divisions; 24 px panel gaps, 36 px desktop gutters, 18 px mobile gutters. Use hairline beat markers, squared panels with 6 px corners, and one accent surface. Do not cover the UI in waveform decorations.

## Screen composition

At 1440 px, place a 240 px repertoire rail beside an elastic score area and a 320 px session notebook. A compact transport spans the bottom of the score region. The first viewport exposes piece title, passage selection, tempo, loop bounds, and start action. The notebook begins with today's intention, not a generic chart.

The score uses static thumbnails with numbered passages. Selecting a passage opens a readable enlarged view; it does not require precise dragging. A session review screen compares planned versus completed time as text and lets the musician record one observation. A separate library handles uploaded files and attribution.

At 390 px, the repertoire rail becomes a “Change piece” sheet. The score fills the width; the notebook follows below. A persistent transport uses two rows: timer/state, then start/pause and passage controls. It never obscures the last annotation. Tempo and loop boundaries have explicit numeric fields and step buttons alongside any sliders.

## Interaction and states

All sound starts only after an explicit user action; opening a page or changing tempo produces silence. Space activates transport only while focus is in the transport region and never while typing a note. Provide labeled start, pause, and stop buttons. A blocked audio device shows “Audio is unavailable. Continue with a silent timer.” Loading a score preserves the transport dimensions. Empty library copy reads “Add the piece you are practicing.” A failed upload retains the chosen file and offers retry. Completion says “Passage complete. Save one observation?” without automatically starting another segment.

## GSAP motion choreography

| Trigger | Target | Duration / ease | Result |
| --- | --- | --- | --- |
| Workspace loads | Repertoire heading and notebook header | `gsap.timeline()`, 0.30 s, `power2.out` | A subtle 8 px entrance gives structure, with transport immediately interactive. |
| Passage selected | Selection outline | `gsap.to()`, 0.18 s, `power2.out` | The outline moves to the selected passage; score notation stays stationary. |
| Practice begins | Timer status marker | 0.24 s, `power1.out` | A hollow square fills once; there is no pulsing distraction. |
| Review intentionally opened | Review panel | 0.28 s, `power3.out` | The panel rises 16 px while preserving keyboard focus order. |

## Signature button

The transport action is a wide accent key with a distinct play icon and the duration written in words. On a fine pointer, hover shifts the icon 3 px, without moving the label. Press scales only the inner surface to `0.975` over 0.07 s; release reaches `1` in 0.34 s with `back.out(1.25)`. This is spring-style easing, not a simulated physical spring. State changes execute immediately and cancel older tweens with `overwrite: 'auto'`. Pause has the same target size and stable width. Focus uses a 3 px cyan outline. Reduced motion substitutes an immediate fill change and no icon travel.

## Accessibility and performance

Offer a text passage list beside any score image; users can operate the timer without reading notation. Expose elapsed time as readable text, but do not announce every second. Announce state changes only. Honor reduced motion through `gsap.matchMedia()`. No ScrollTrigger or scroll-controlled audio is needed. Keep audio scheduling separate from GSAP, load sound only on request, and release audio resources when the room closes. Use transforms and opacity for interface motion; never animate actual playback timing.

## Build acceptance criteria

- Loading, navigating, or hovering produces no audio.
- A keyboard user can configure and finish a silent practice segment.
- At 390 px, all transport controls remain reachable with 44 px targets.
- Reduced motion preserves selected passage, timer state, and completion feedback without animation.
