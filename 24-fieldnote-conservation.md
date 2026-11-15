# Fieldnote — Conservation Through Observable Evidence

A conservation organization's journal and project directory designed like a contemporary field notebook: map coordinates, dated observations, restrained illustrations, and clear provenance. Fieldnote, its projects, and every example observation are fictional.

## Product and core flow

For supporters who want to understand an organization's work before contributing. The main task is inspecting a project, its evidence, and the available ways to help.

Flow: choose a landscape → open a project → read dated observations and methods → inspect the current needs → choose an action → review the action summary. Example copy: “Morrow Wetland / Sample project / Observation logged 06 May 2027.” Clearly mark illustrative counts and maps; never invent proven environmental outcomes.

The initial version supports “Register interest” for a field update or event. If donations are added, show the actual recipient, currency, frequency, fees, and receipt process before payment.

## Visual system

- Notebook `#F2EBDD`; forest ink `#213F35`; secondary `#4C6256`; pale sage `#DCE4D5`; orange drawing accent `#CE6D38`; accessible action brown `#843A1E`; rules `#B6BCAA`; inverse `#FCFAF2`.
- Literata with Georgia/serif fallback for narrative headings and journal passages; Source Sans 3 with Arial/sans-serif fallback for navigation, project facts, and forms.
- Desktop: 64/68 px feature title, 36/42 chapter title, 19/31 article text, 13/20 field labels. Mobile: 40/44 title, 28/34 section title, 18/29 article text.
- Use 8 px spacing, 64 px desktop gutters, 22 px mobile gutters, and a 720 px reading measure. Rules and small square labels carry structure. Paper texture stays subtle and never sits behind dense text.

## Screen composition

At 1440 px, the first viewport splits into a five-column field-journal introduction and a seven-column illustrated landscape index. Place one featured project's name, last-updated date, evidence status, and “Read the field notes” action beside the illustration. Navigation is compact: Projects, Journal, Methods, Get involved.

The directory offers both Map and List views. Project pages open with a factual summary, then dated observation entries, methodology, image captions, and a visible needs list. A narrow provenance rail names the source and update date for each published measure. Give uncertainty and missing evidence a normal typographic treatment rather than hiding them in footnotes.

At 390 px, show the project list first and offer Map as an option. Move provenance directly beneath its associated observation. Turn multi-column project summaries into labeled definition lists. The contribution form follows the needs list in normal flow; no persistent donation banner covers reading content.

## Interaction and states

Map markers are buttons with project names and equivalent list links. Marker focus reveals the same project summary as pointer interaction. Filters expose selected values and a result count. If map tiles fail, the list and project information remain available. No matching projects offers Clear filters; no published observations says “Field notes are being prepared,” without invented progress bars. Register-interest errors preserve input and link fields to their error messages. Confirmation states exactly what was requested and how contact will occur.

## GSAP motion choreography

| Trigger | Target | Timing and API | Intended result |
| --- | --- | --- | --- |
| Feature enters | Landscape artwork wrapper | `gsap.fromTo()`, y 14 → 0, opacity 0.85 → 1, 0.65 s, `power2.out` | A calm opening with no animated map movement. |
| Journal figure enters | Photo and its caption | `ScrollTrigger`, once, 0.45 s, `power2.out`, y 10 → 0 | Support long-form reading without revealing evidence in fragments. |
| Select a project | Decorative marker halo | 0.2 s opacity transition, `power1.out` | Identify selection without pulsing or resizing map content. |
| Expand methods | Caret only | 0.18 s rotation, `power2.out` | Immediate semantic disclosure with a small visual cue. |

Do not animate evidence totals, grow progress indicators from zero, or scrub a map against document scroll. Those effects can misrepresent information or interrupt reading.

## Signature button

“Read the field notes →” has a forest outline, paper fill, and an inset square arrow stamp. Animate the stamp, not the full reading link: press scale 0.92 over 0.1 s; release to 1 over 0.5 s with `back.out(1.55)`. On fine-pointer hover, shift the arrow 2 px right and darken the outline. Keep a 3 px high-contrast focus ring around the stable link. Reset on cancellation, blur, and route change. Navigation starts immediately. Reduced motion keeps the stamp still and changes its fill. The easing supplies spring-style overshoot, not physical spring behavior.

## Accessibility and performance

Provide descriptive alternatives for illustrative landscapes and a full text alternative for the map. Do not expose sensitive wildlife coordinates in a real deployment; choose the publishing precision deliberately. Use semantic articles, timestamps, definition lists, and labeled forms. Reserve image space and lazy-load below-the-fold photographs. Keep mapping optional until requested. With reduced motion, present all observations and illustrations statically. Keep content readable if animation or maps fail to initialize.

## Build acceptance criteria

- Every example metric, map, and observation is labeled illustrative; production evidence has a source and update date.
- Projects can be found and opened through the list without loading or operating the map.
- At 390 px and with keyboard navigation, provenance remains attached to its observation and forms are usable.
- Reduced motion removes movement while preserving selection, disclosure, and registration feedback.
