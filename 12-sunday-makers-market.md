# Sunday Makers Market — A Neighborhood Noticeboard

A friendly, precise vendor directory organized around stalls, visit planning, and useful details rather than promotional noise. Sunday Makers Market, its location, vendors, and dates are fictional examples.

## Product and core flow

For visitors deciding whether and how to visit, and makers seeking the right stall. Visitor flow: check the next market → filter makers → inspect access and payment details → save a visit list → review the route. Example copy: “Sunday, 22 November 2026 / 9 am–4 pm,” “Riverside Hall — fictional venue,” and “Bring your own bag.” A separate maker path explains stall requirements and leads to an application. Do not imply live availability, verified accessibility, or real opening hours from illustrative content.

## Visual system

- Paper `#FFF7E7`; ink `#26382D`; panel green `#E0E9D6`; main action `#31533A`; rust accent `#A33D24`; muted text `#5B665B`; focus violet `#6546A5`; error `#AC3035`.
- Bricolage Grotesque for expressive headings, fallback Arial/sans-serif. Atkinson Hyperlegible for practical details, fallback Arial/sans-serif. Display: 58/61 px desktop and 36/40 px mobile. Body and controls: 17/26 px. Stall numbers: 24/28 px with tabular figures.
- Use 8 px spacing, 48 px desktop and 20 px mobile gutters, modest 8 px corners, and small printed stamp details. Illustrations appear only in margins. Real listing data stays on flat, readable surfaces. Category tags use text and icons, never a rainbow of unexplained colors.

## Screen composition

At 1440 px, a large date poster occupies four columns, with the current market's practical facts in an adjacent eight-column noticeboard. The first screen reveals date, venue label, hours, access-information link, and “Browse this market.” Below it, a two-column maker list sits next to a simplified stall plan. Each row includes maker name, category, stall number, accepted payments, and save control.

Vendor detail pages use one making-process photograph, a short description, products, and visit details. A “Your visit list” page groups saved vendors by stall aisle with a print-friendly view. The maker application has a requirements checklist before the form and an explicit review step.

At 390 px, the date poster becomes a compact date strip. Practical facts come before imagery. Filters open in a labeled sheet with Apply and Clear controls; the list remains the default view. The stall plan becomes an optional separate view with zoom buttons and a complete text stall list. Saved vendors stay accessible through a normal navigation link with a count.

## Interaction and states

Category filters use checkbox groups, and applying filters announces the result count once. Saving a maker updates a labeled toggle such as “Save Loom House” to “Remove Loom House from visit list.” An empty visit list explains how to add makers; an empty search suggests clearing filters. Loading keeps the list geometry stable. A failed update retains previous listings with “Details may be out of date” and retry. Application errors link to affected fields and preserve answers. A success screen shows the submitted application summary without promising acceptance. Never infer verified access information from a decorative wheelchair icon.

## GSAP motion choreography

| Trigger | Target | Duration / ease | Result |
| --- | --- | --- | --- |
| Market page loads | Date stamp and venue heading | `gsap.timeline()`, 0.45 s, `power2.out` | A 12 px reveal establishes the noticeboard without delaying information. |
| Maker section enters view | Section title and rule | `ScrollTrigger`, 0.40 s, `power1.out`, once | One restrained reveal marks the start of browsing; listing rows remain static. |
| Vendor saved | Small bookmark icon | `gsap.to()`, 0.22 s, `back.out(1.3)` | A brief icon response confirms the state; the row does not move. |
| Filter sheet opens | Sheet surface | 0.26 s, `power3.out` | The sheet moves 20 px; focus transfers to its heading immediately. |

## Signature button

“Plan my visit” has a ticket-shaped border and a small arrow printed inside a square. Fine-pointer hover shifts the arrow 3 px to the right. Press compresses the surface to `0.955` over 0.10 s; release reaches `1` over 0.46 s with `back.out(1.6)` for a playful, spring-style response. The pointer hit area remains unchanged. Keyboard activation opens the visit list immediately; focus uses a 3 px violet outline. Reduced motion removes translation and scaling, using an immediate darker fill. Bookmark buttons remain quieter than this primary action.

## Accessibility and performance

Provide the stall list as the complete alternative to the map and useful venue-access prose with a source/status label. Targets are at least 44 px. Saved lists work locally without requiring an account; clarify whether they sync. Use `gsap.matchMedia()` for motion preferences and clean up contexts on navigation. No scroll trapping or auto-reordering. Lazy-load vendor photos with fixed aspect ratios, and keep practical visit details in normal HTML before enhancement.

## Build acceptance criteria

- The opening mobile screen makes the fictional date, venue, and hours clear.
- Every map stall can be found through the text list without zooming or dragging.
- Saving a vendor preserves focus and exposes its new state to assistive technology.
- Reduced motion and failed image loads leave visit planning fully usable.
