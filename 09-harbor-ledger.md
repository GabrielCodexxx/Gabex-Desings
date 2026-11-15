# Harbor Ledger — Invoices as a Working Desk

A calm receivables workspace that treats each invoice as a document with a history, not another metric tile. Harbor Ledger, clients, amounts, and statuses are fictional examples.

## Product and core flow

For independent designers who need to know what requires action and issue a clear invoice quickly. Flow: review action queue → open a document → resolve missing details → preview → send after deliberate confirmation. Example queue row: “Aster Studio / Identity refinement / Draft / ₱18,000.” Example warning: “Add a billing email before sending.” The product offers visibility and administration; it makes no earnings forecasts or financial advice.

## Visual system

- Background `#F4F5F0`; document white `#FFFFFF`; ink `#203039`; secondary `#54636A`; navy action `#204E66`; teal success `#246953`; warning ink `#785016`; error `#AA3434`; focus `#6845A0`.
- Source Sans 3 for interface text, fallback Arial/sans-serif. Newsreader for document titles, fallback Georgia/serif. Screen title: 32/38 px desktop, 27/33 px mobile. Table and form text: 16/24 px. Monetary totals: 24/30 px with tabular figures.
- Use 8 px spacing, 40 px desktop margins, 20 px mobile margins, 56 px rows, and 1 px slate-tinted dividers. Distinguish state with text plus icon, never color alone. Avoid shiny cards and decorative charts.

## Screen composition

At 1440 px, the working view has a 208 px navigation rail, a 700 px document queue, and a flexible detail inspector. Above the queue, a text summary reads “2 drafts need details. 1 invoice awaits a reply.” Counts come from the visible dataset. Filter tabs sit directly over column headings; the primary “Create invoice” button sits beside the queue title.

Opening a row reveals a paper-like invoice preview in the inspector, with a chronological activity list underneath. Editing takes a dedicated workspace: line items on the left, totals and document checks on the right. Preview and send are separate stages; the final confirmation names recipient, amount, and document number.

At 390 px, replace the table with a semantic list of document rows: client, state, amount, then issue date. Selecting one opens a full-page detail view with a “Back to invoices” link that restores filters. Line-item editing uses stacked fields with clear subtotals, and the final total precedes the action bar. Never force a horizontally scrolling desktop table.

## Interaction and states

Sorting requires an explicit action and communicates direction in the header. Incoming status changes update a row in place; they never auto-reorder the queue, especially around focus. Filters keep their state in the URL. Skeletons preserve row height, and a network failure leaves last-loaded data visible with a timestamp and retry. Empty filtered results say “No drafts match these filters” and offer “Clear filters.” Form errors sit beside fields and in a linked summary. A successful save announces “Draft saved.” Sending is idempotent, disables duplicate submissions, and shows an explicit failure state if delivery cannot be confirmed.

## GSAP motion choreography

| Trigger | Target | Duration / ease | Result |
| --- | --- | --- | --- |
| Inspector intentionally opened | Inspector content | `gsap.to()`, 0.22 s, `power2.out` | Content shifts 12 px into place; rows remain still. |
| Preview mode selected | Document wrapper | `gsap.timeline()`, 0.24 s, `power1.out` | An opacity transition exposes the preview without resizing totals. |
| Draft save confirmed | Saved check icon | 0.18 s, `power2.out` | A single small fade signals success without a notification cascade. |
| Validation summary appears | Summary surface | 0.16 s, `power1.out` | Opacity changes only; focus moves immediately to the summary. |

## Signature button

“Preview invoice” is a document-tab button with a folded-corner icon. Fine-pointer hover translates only the corner 2 px upward. Press scales the surface to `0.985` for 0.08 s; release uses 0.30 s and `back.out(1.10)` to feel springy without bouncing the document. The final “Send invoice” button uses the same restrained response and executes only after the confirmation step. Keep label width stable during “Sending…” and a 3 px focus outline. Reduced motion uses immediate border emphasis; keyboard activation has identical submission behavior. Overshoot easing is spring-style, not physical simulation.

## Accessibility and performance

Use actual table semantics on desktop, labeled form controls, accessible currency labels, and a real dialog for final confirmation. Never announce private invoice contents repeatedly through live regions. Use `gsap.matchMedia()` for reduced motion and `gsap.context()` cleanup. No scroll animation, pinning, or perpetual motion belongs here. Animate transforms and opacity only; defer preview rendering until requested, while preserving readable invoice data.

## Build acceptance criteria

- Sending requires review of recipient and amount and cannot double-submit.
- A live update never moves a focused document row.
- At 390 px, line items, total, and errors remain readable without horizontal scrolling.
- Failed saves retain entered details and expose a clear retry path.
