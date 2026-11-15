# Stillwater Ceramics — A Shop That Feels Like a Studio Visit

An asymmetric, tactile storefront where scale, glaze, and the maker's hand lead the purchase. Stillwater is a fictional ceramics brand; products and stock examples are illustrative.

## Product and core flow

For buyers choosing functional objects they cannot touch online. The central job is understanding the piece before committing: open a collection → inspect scale and surface → choose a glaze → review delivery → add to basket. Sample copy: “Low bowl / river ash,” “Holds approximately 650 ml,” and “Each glaze settles differently. View three examples.” Explain intentional variation beside the photographs, not in an obscure policy footer. The primary action is “Add river ash bowl — ₱1,450.”

## Visual system

- Canvas `#F3EEE5`; panels `#E8DFD1`; body ink `#292820`; secondary text `#605B50`; moss action `#334A39`; focus blue `#245F99`; error `#9C3229`.
- Fraunces for quiet product titles, with Georgia and serif fallbacks. DM Sans for controls and prose, with Arial and sans-serif fallbacks. Titles: 64/66 px desktop, 40/44 px mobile. Body: 17/27 px; controls and specifications: 15/22 px.
- Use an 8 px spacing scale, 64 px desktop gutters, 24 px mobile gutters, and thin ink rules. Product photography has unretouched shadows and neutral white balance. Preserve irregular object silhouettes; avoid rounded cards around every photograph.

## Screen composition

At 1440 px, the first viewport is a 56/44 composition: a large overhead bowl photograph on the left; a narrow vertical image of a hand holding the bowl interrupts its lower edge. The right column contains title, price, stock, glaze selection, dimensions, and basket action. A small “Made for slow breakfasts” line sits above the title. There is no oversized promotional banner.

Below, a three-image scale sequence contrasts palm, table, and shelf views. A ruled specification sheet and an expanded shipping summary precede related pieces arranged as an uneven studio shelf. The basket is a review drawer with item quantity and delivery estimate; checkout is a full page.

At 390 px, place one photograph, the purchase details, then the scale strip in document order. Glaze swatches become two labeled columns. A bottom purchase bar appears only after the main action leaves view and must reserve safe-area space. Images use a swipeable, labeled gallery with visible previous/next buttons; no gesture is required.

## Interaction and states

Glazes are labeled radio inputs, with selection expressed by a check and text. Changing glaze retains gallery position and updates availability. Loading uses fixed-size image placeholders; failure exposes “Retry photograph” without hiding specifications. An unavailable variant retains its image and says “This glaze is currently unavailable.” An empty basket offers “Return to the collection.” Successful addition announces the item and quantity in a polite live region, then leaves focus on the triggering button. Escape closes the basket drawer and restores focus; opening it intentionally moves focus to its heading.

## GSAP motion choreography

| Trigger | Target | Duration / ease | Result |
| --- | --- | --- | --- |
| Product page ready | Small studio label and title | `gsap.timeline()`, 0.55 s, `power2.out`, 40 ms stagger | An 18 px rise introduces text; purchase controls remain immediately usable. |
| Scale sequence enters viewport | Photograph wrappers | `ScrollTrigger`, 0.65 s, `power2.out`, once | A 24 px reveal exposes the scale story without pinning. |
| Glaze selection | Alternate image layers | `gsap.to()`, 0.20 s, `power1.out` | Crossfade only after the next image has decoded. |
| Basket opened | Drawer surface | 0.32 s, `power3.out` | Slide from 28 px; overlay opacity settles separately. |

## Signature button

The “Add” button resembles a pressed clay stamp: inset border, small batch-code label, and a right-aligned plus. Fine-pointer hover raises the surface 2 px over 0.16 s. Pointer press scales to `0.965` over 0.09 s; release returns to `1` over 0.42 s using `back.out(1.65)` for spring-style overshoot. Keyboard activation gets the same release response without delaying the action. Keep a 3 px focus ring outside the button. Reduced motion removes transforms and changes border and background immediately. A pending action says “Adding…” and cannot submit twice.

## Accessibility and performance

Use descriptive image alternatives for form and scale, and empty alternatives for decorative studio imagery. Keep 44 px targets and visible currency, quantity, and stock text. Register ScrollTrigger once; use `gsap.matchMedia()` for reduced motion and breakpoint branches, reverting on teardown. Animate opacity and transforms only. Render content visible before enhancement, avoid scroll trapping, and reserve image aspect ratios to prevent shifts.

## Build acceptance criteria

- A keyboard user can select a glaze, add it, and review the basket without losing position.
- At 390 px, price and availability appear before the primary purchase action.
- Reduced motion exposes every image and section without movement or hidden content.
- Failed image loads and unavailable glazes never remove product dimensions or shipping information.
