# Counterline — A retail counter with dependable state

A point-of-sale and stock-control interface shaped around quick recognition, deliberate totals, and recoverable work. Counterline, its shop, products, transactions, prices, and stock records are fictional design examples.

## Product and core flow

Design for a small retail team alternating between customer service, held sales, and stock checks. The central job is preparing a correct basket without losing it when another task interrupts.

Flow: find or scan a product → review quantity and price → hold or continue the sale → review the selected tender handoff → record the confirmed result. Sample basket: “Cotton notebook / 2 × demo price ₱180.” A hold is named “Counter 2 / Held at 14:08 / 3 lines,” with no unnecessary customer identity.

Never label an unconfirmed or offline payment paid. Keep the inventory workflow distinct: start a count → record observed quantities → review discrepancies → submit adjustments for acknowledgement.

## Visual system

- Terminal frame `#172A32`; primary work surface `#F5F7F4`; receipt white `#FFFFFF`; text `#182D35`; secondary text `#51656D`; teal action `#17605D`; teal tint `#E1EFEB`; alert ink `#8A4617` on `#FFF0DC`; divider `#C8D3D2`.
- **Atkinson Hyperlegible**, Arial, sans-serif for product names and controls; **Roboto Mono**, Consolas, monospace for stock codes, basket amounts, and receipts.
- Desktop title 28/34 px; mobile 25/31 px; product name 17/24 px; body 16/24 px; primary total 34/40 px. Avoid tiny labels in a busy physical environment.
- Use 8 px spacing, 24 px desktop gutters, 16 px mobile gutters, 8 px corners, and 52 px primary targets. The dark frame holds context; the light receipt area holds the current task. No glowing controls.

## Screen composition

At **1440 px**, a narrow dark station rail shows Sale, Held sales, Products, and Stock count. The center is a catalogue with a large search/scan field and labeled category tabs; the right 420 px is a receipt-style basket. The first viewport always shows the station name, connection state, selected basket, quantities, adjustments, total, Hold sale, and Review tender. Products use compact name-led tiles with optional images.

Held sales form a searchable list with line count, creation time, and a clear Resume action. Stock count is a separate full-width worksheet grouped by shelf, with expected, counted, and difference columns. Discrepancy review shows the original snapshot and any newer stock movement before posting an adjustment. Transaction detail shows its actual state and supplied reference, with a receipt view only where appropriate.

At **390 px**, use three explicit destinations: Catalogue, Basket, and Held. The basket count is visible in navigation. Search stays at the top; catalogue records become full-width selectable rows. Tender review and stock discrepancy review use their own routes, not compressed side panels. A mobile stock count shows one item per record with a labeled quantity field and next-item action.

## Interaction and states

Provide manual entry as well as barcode input; avoid global keystroke capture that steals form typing. Scanning an unknown code offers search and keeps the basket intact. Quantity edits show their effect immediately but keep totals stable in place. Empty baskets invite search; loading reserves catalogue dimensions. Hold confirmation appears only after its persistence is acknowledged; failed holds leave the active basket recoverable. Offline state explains which local drafts remain available and labels unsynced work. Tender handoff failures retain the basket and distinguish unknown outcome from confirmed failure. Concurrent stock changes trigger discrepancy review, never a silent overwrite. Inventory numbers do not bounce or reorder during updates.

## GSAP motion choreography

| Trigger | Target | Duration / ease | Result |
| --- | --- | --- | --- |
| Product added | Reserved basket-row indicator | `gsap.to()`, 0.16 s, `power1.out`, opacity emphasis | Mark the line without flying a tile across the counter. |
| Resume held sale | Receipt header wrapper | `gsap.fromTo()`, 0.2 s, `power2.out`, y 6 → 0 | Identify the restored basket; line contents appear immediately. |
| Open stock discrepancy details | Decorative chevron | 0.16 s, `power2.out` | Express disclosure state without animating quantity values. |
| Hold acknowledged | Hold icon | `gsap.timeline()`, 0.26 s, `back.out(1.05)`, scale 0.92 → 1 | Small confirmation after successful persistence. |

No ScrollTrigger, continuous status pulses, receipt auto-scrolling, or checkout animation that delays the next customer.

## Signature button

Hold sale is a broad outlined control with a pause-tab glyph. Fine-pointer hover moves the glyph upward **1 px** and darkens the border. Compress the inner face to **0.988** over **0.055 s** and return over **0.25 s** with `back.out(1.05)`. This is a subtle spring-style ease, not physics. The outer 52 px target and 3 px dark focus ring remain fixed. Enter and Space retain native button behavior. Restore the face on pointercancel, release outside, blur, and disabled state. Begin holding on activation immediately and prevent repeated pending requests. Reduced motion uses only instant border and label changes.

## Accessibility and performance

Offer visible labels, high-contrast status text, keyboard-accessible quantities, and a non-scanner path. A software keyboard must not hide basket validation on mobile. Announce completed additions sparingly and expose a silent visual history of recent scans. Distinguish availability and connection with words as well as color. Keep receipt dimensions stable; defer images and reuse list components. Scope GSAP contexts and dispose event handlers on station changes. Reduced motion removes all movement without altering the transaction flow.

## Build acceptance criteria

- A held sale can be resumed with its exact lines and quantities after acknowledged persistence.
- Offline or unknown tender outcomes never appear as confirmed payment success.
- A concurrent stock movement is visible before an adjustment can be posted.
- Keyboard users at desktop and touch users at 390 px can prepare, hold, resume, and review a sale without scanning hardware.
