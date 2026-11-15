# Dockside — Wholesale ordering without spreadsheet archaeology

A B2B purchasing portal organized like a carefully typeset trade catalogue: clear pack sizes, visible quantity breaks, and an order worksheet that remains readable at volume. Dockside, its customers, products, stock, and prices are fictional demonstration content.

## Product and core flow

Design for a store buyer replenishing dozens of lines while checking quantity tiers and delivery expectations. The central job is assembling a correct order, not browsing an endless consumer storefront.

Flow: choose an account and delivery location → search or paste product codes → enter case quantities → resolve stock and pack-size exceptions → review a quote or order request. Sample line: “DS-204 / Stackable tray, sand / 6 units per case / 4 cases.” Sample pricing reads “Demo tier: 1–9 cases, ₱1,440 per case; 10+ cases, ₱1,320 per case.” Distinguish units, cases, tax treatment, and currency.

Use “Review order request” before commitment. Distinguish received, accepted, and awaiting supplier confirmation. Sample inventory is never labeled live.

## Visual system

- Catalogue paper `#F6F2E9`; white work area `#FFFFFF`; deep ink `#233336`; muted text `#536366`; burnt-orange action `#A04422`; pale clay selection `#F5E4D8`; border `#C8CDC8`; backorder ink `#785014` on `#FFF0D1`.
- **Archivo**, Arial, sans-serif for product names and controls; **IBM Plex Mono**, Consolas, monospace for item codes, quantities, and aligned prices.
- Desktop title 36/42 px; mobile 28/34 px; product labels 16/23 px; worksheet text 14/22 px; quantity input 18/24 px. Tabular figures prevent price columns from shifting.
- Use an 8 px spacing grid, 32 px desktop gutters, 16 px mobile gutters, 4 px corners, and 48 px input targets. Crop product imagery consistently on neutral paper.

## Screen composition

At **1440 px**, a 72 px account header contains customer, delivery address, currency, and a persistent order reference. The main screen allocates a 208 px category rail, a flexible trade catalogue, and a 340 px order worksheet. The opening viewport shows search, a Quick add codes action, product rows with thumbnails, pack sizes, stock text, and quantity inputs. The worksheet exposes case count, estimated totals, unresolved lines, and Review order request without a wall of KPI cards.

Quick add opens a structured import screen with code and case-quantity columns, line-specific errors, and an editable preview. Product detail shows dimensions, pack contents, quantity tiers, and supplied lead-time information. Review repeats every requested line and separates available, backordered, and unavailable quantities. Request history includes accepted quantities and downloadable documents when supplied.

At **390 px**, catalogue rows become stacked product records with name, code, pack size, stock, then quantity. A labeled “Order worksheet (12 lines)” link opens a full route rather than a cramped side drawer. Quick add supports one code per line with explicit formatting guidance. Keep totals above the review action, and retain catalogue filters when returning.

## Interaction and states

Quantity fields accept cases only and show the equivalent unit count. Validate increments without silently rounding. Updating a quantity changes the applicable price tier and explains the cause. Backorders require an explicit choice; never add them silently. Search loading preserves row dimensions; no matches offers code search or cleared filters. A stock-refresh failure displays the last checked time and labels availability unconfirmed. If stock or price changes before review, highlight affected lines and request acknowledgement. Save a draft only after confirmation, or label it “Unsynced local draft.” Empty worksheets explain Quick add. Prevent duplicate submissions and show success only after the request is acknowledged.

## GSAP motion choreography

| Trigger | Target | Duration / ease | Result |
| --- | --- | --- | --- |
| Open worksheet | Worksheet visual shell | `gsap.fromTo()`, 0.24 s, `power2.out`, x 12 → 0 | Connect catalogue selection to its order context without moving product rows. |
| Add a line | Small line-added icon | `gsap.timeline()`, 0.3 s, `back.out(1.15)`, scale 0.88 → 1 | Acknowledge the addition in a reserved icon slot; quantities update immediately. |
| Expand quantity tiers | Disclosure caret | `gsap.to()`, 0.18 s, `power2.out` | Rotate the caret while the tier table is immediately available. |
| Quote request confirmed | Receipt heading wrapper | 0.2 s opacity transition, `power1.out` | Mark acknowledgement without animating monetary totals. |

Use no ScrollTrigger, scrolling cart fly-ins, animated prices, or automatic row sorting. Cancel stale transitions when the worksheet changes rapidly.

## Signature button

Review order request is a rust-colored rectangle with white text and an inset page-corner glyph. On fine-pointer hover, the glyph shifts 2 px right. Press the inner face to **0.982** over **0.07 s**; release over **0.32 s** with `back.out(1.18)`. This is restrained spring-style easing, not physical simulation. Keep the 48 px outer hit area and 3 px ink focus outline stationary. Native click or keyboard activation advances immediately. Restore the face on pointercancel, release outside, blur, and disabling. Reduced motion uses an instant fill change with no translation or scale.

## Accessibility and performance

Use semantic tables for price tiers and worksheet review, labeled number inputs, and an error summary linked to invalid lines. Make pack size understandable without imagery. Keep a text-based Quick add path and do not require drag-and-drop uploads. Announce the completed line addition, not every intermediate total. Use small responsive thumbnails; defer product photography. Scope GSAP contexts, clean up handlers and tweens on navigation, and provide complete static behavior under reduced motion.

## Build acceptance criteria

- A buyer can distinguish cases, units, quantity tiers, and backorders before submitting.
- A price or stock conflict preserves quantities and requires review of affected lines.
- At 390 px, the worksheet and catalogue retain their context without page-level horizontal scrolling.
- Keyboard and reduced-motion users can import, correct, review, and submit the same order request.
