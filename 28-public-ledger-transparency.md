# Public Ledger — A budget that can be read, compared, and traced

A public-sector transparency portal designed as a contemporary financial publication: strong table hierarchy, visible period definitions, and a source beside every number. Public Ledger, its agency, programs, amounts, datasets, release dates, and reporting rules are fictional demonstration content; the concept makes no claim of actual regulatory compliance.

## Product and core flow

For residents, researchers, journalists, and public staff who need to understand published allocations and spending. The primary task is comparing like-for-like periods and tracing a figure back to its source.

Flow: choose a reporting period → inspect the summary and definitions → drill into a department or program → compare a compatible period → open methodology or download the source. Sample row: “Community libraries / Demo allocation ₱12,000,000 / Demo reported spending ₱4,500,000 / Reporting period: sample Q1 2027.” These figures are illustrative, not statements about any real agency.

Use “Reported spending” rather than an unexplained “Used” label. Explain that missing, provisional, revised, and zero are different states. Never imply that budget allocation is the same as a payment or an outcome.

## Visual system

- Paper `#F7F5EF`; table surface `#FFFFFF`; ink `#25313A`; secondary `#53616B`; action navy `#234B66`; comparison teal `#226B62`; allocation tint `#DCE7EE`; spending tint `#CDE6DD`; divider `#BFCBD1`; revision ink `#7B4C14` on `#FFF0D4`.
- **Libre Franklin**, Arial, sans-serif for controls and financial tables; **Literata**, Georgia, serif for editorial headings and short explanatory notes. Identifiers and amounts use tabular figures.
- Desktop headline 52/58 px; mobile 34/40 px; body 17/27 px; table 15/23 px; source notes 14/22 px. Use 8 px spacing, 48 px desktop margins, 20 px mobile margins, and a restrained 4 px control radius.
- A document edition line, ruled tables, numbered notes, and small comparison bars establish the identity. Avoid oversized KPI tiles and decorative dashboard gauges.

## Screen composition

At **1440 px**, the first screen reads like a public report cover: agency demonstration label, period selector, publication timestamp, and one clear question—“How was the sample budget allocated?” Below it, a wide program table occupies eight columns and a four-column reading guide explains allocation, spending, reporting cut-off, and source status. Keep the download link and sample-data label visible.

The table shows program, allocation, reported spending, remaining arithmetic balance, and dataset status. Any calculated balance is labeled as a calculation, not an available-to-spend promise. An optional horizontal bar view mirrors the table and shares its exact values. A program page includes period history, notes, source files, and revision history. Comparison places two compatible periods side by side and states whether values are nominal and whether program definitions changed.

At **390 px**, use labeled record groups instead of squeezing five columns. Period controls stack above the results. A Compare view presents each program with period A and B values vertically aligned. Show definitions next to the relevant values through accessible disclosures. Downloads give format and file size when known; the HTML view remains useful without opening a spreadsheet or PDF.

## Interaction and states

Filters update the result count and retain selected values in shareable URLs without personal information. Sorting announces direction and never changes silently after a refresh. No matching programs offers Reset filters. An unpublished period says “No dataset published for this period,” not zero spending. Missing values use explicit text; provisional and revised entries carry persistent labels and notes.

Loading preserves table headings and period context. A failed fetch can retain the last successful result with a visible stale timestamp and retry action. Comparison rejects incompatible units or explains a changed definition instead of calculating a misleading percentage. A source download failure offers the source page and retry. Revised data does not animate or replace an actively inspected row without notice; show “A newer release is available” and let the reader load it. The public portal is read-only; internal publishing is a separate authorized workflow with review and a revision record.

## GSAP motion choreography

| Trigger | Target | Duration / ease | Intended result |
| --- | --- | --- | --- |
| Report opens | Decorative edition rule | `gsap.fromTo()`, scaleX 0.95 → 1, 0.28 s, `power2.out` | Establish publication rhythm; all data is visible immediately. |
| Switch table/bar view | Decorative selected-tab marker | `gsap.to()`, 0.18 s, `power2.out` | Follow the selected view without growing bars from zero. |
| Open a source note | Note's left rule | 0.2 s opacity, `power1.out` | Associate the note with its figure without moving rows. |
| Copy share link succeeds | Link icon | 0.22 s crossfade, `power1.out` | Confirm copying while persistent status text remains available. |

No ScrollTrigger, count-up numbers, animated percentages, bouncing bars, or scroll-scrubbed budget totals. Values and chart geometry are always truthful representations of the selected data state.

## Signature button

“Compare selected periods” is navy with an outlined paired-column icon. On fine-pointer hover, only the decorative icon's two bars separate by **1 px**. Press the inner face to **0.992** over **0.07 s**; release to 1 over **0.27 s** using `back.out(1.05)`. This is minimal spring-style easing, not physical simulation. Keep the 48 px target and 3 px charcoal focus outline stationary. Comparison begins immediately on native activation. Reset on cancellation, leaving while pressed, blur, or disabling. Reduced motion changes the background and label without movement.

## Accessibility and performance

Use real table headers and captions, explicit currency/units, meaningful dates, and downloadable machine-readable alternatives where supplied. Provide chart values in text and never rely on color alone. Keep keyboard focus stable during filtering and announce only the result summary. Support print and a low-bandwidth HTML route without chart libraries. Load only the selected dataset, preserve source metadata, and avoid hidden rounding differences. Scope GSAP cleanup and display static final states under reduced motion or script failure.

## Build acceptance criteria

- Every displayed figure has a visible period, unit, sample-data status, and reachable source or clear source-unavailable explanation.
- Missing, zero, provisional, revised, and stale values remain distinguishable in tables, comparisons, and downloads.
- Incompatible periods cannot produce an unexplained percentage or misleading side-by-side chart.
- At 390 px, keyboard-only, print, and reduced-motion reading expose the same core financial information without requiring chart interaction.
