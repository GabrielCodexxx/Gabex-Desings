# Ember House — A reservation experience with the rhythm of service

A fictional chef-led restaurant presented as a warm, typographic service notebook: precise dining information, tactile menu details, and a reservation path that never makes visitors hunt.

## Product and core flow

Serve guests deciding whether the evening, menu, access, and available seating fit their plans. The core flow is **understand the dining format → inspect a sample menu → choose party/date/time → review terms → confirm reservation**. Keep the menu and reservation entry visible in the opening screen.

Use grounded demonstration copy: “An evening around the hearth,” “Sample menu — changes with availability,” and “Thursday, 19:00 / 2 guests.” Availability must be labeled demo until connected. Dietary requests receive “Tell us what we should know; the team will confirm what can be accommodated.” Do not imply that a free-text note guarantees an accommodation. Present cancellation terms before the final action, with prices and deposits only when real information exists.

## Visual system

- **Palette:** parchment `#F4EBDD` background, espresso `#302019` text, burgundy `#782D35` primary actions, muted brown `#715B4F` supporting text, pale peach `#F0D9C8` reserved panels. Restrict copper `#A9693C` to decorative rules, not small text.
- **Type:** Cormorant Garamond with Georgia fallback for dining headlines; DM Sans with Arial fallback for forms and menu descriptions. Desktop headline 84/86px; mobile 44/46px. Body 17/27px; menu item 23/29px desktop and 20/26px mobile.
- **Layout:** 12-column grid with 56px desktop margins and 28px gutters. Mobile uses 20px margins. Spacing: 8, 16, 24, 36, 56, 88px. Menu sheets have 2px-radius corners; controls have 6px radii and 48px minimum height.

## Screen composition

At 1440px, create a split composition: a tall, tightly cropped hearth photograph occupies the left five columns; on the right, the restaurant name, concise dining format, opening information, and a compact reservation form align like a service card. A thin running date label and an illustrated ember mark establish character without relying on cinematic video.

Below, show a two-page menu spread: course names on one side, ingredient and service notes on the other. Follow with room photographs, access information, arrival instructions, and a plain contact section. The reservation review screen clearly groups selected slot, guest details, requests, and terms. A completed reservation page includes a reference, venue details, and management actions only after a real confirmation response.

At 390px, shorten the image to a 260px opening crop, then display the title and reservation controls. Dates become a horizontal native-scroll list with explicit previous/next buttons and a full-calendar option. The menu becomes a single continuous document. Reservation review uses stacked sections; keep the primary action after the terms, without a bottom bar obscuring fields.

## Interaction and states

Use labeled select controls or accessible comboboxes for party size and time. Date selection supports keyboard navigation and a manual-entry alternative. A full slot remains readable and disabled with “Fully booked,” not just low opacity. Loading availability announces “Checking tables” and retains the selected date. No availability offers another date and contact details. A failed hold returns the guest to fresh availability without erasing guest information. Explain hold expiration with a real expiry timestamp only if the backend supplies it. Distinguish reservation request, pending hold, and confirmed booking.

## GSAP motion choreography

| Trigger | Target | Duration / ease | Intended result |
|---|---|---|---|
| Page ready | Decorative image mat | `gsap.timeline()`, 0.7s, `power3.out` | Reveal the photograph from a small inset, leaving booking controls immediately usable. |
| Menu enters view | Section rule and course label | `ScrollTrigger`, 0.42s, `power2.out` | Introduce each menu section once with 12px translation. |
| Choose date | Selected date underline | `gsap.to()`, 0.24s, `power2.out` | Glide a decorative underline beneath the selected date. |
| Review opens | Review sheet | 0.25s, `power2.out` | Fade and translate 14px; never animate form field positions during entry. |

## Signature button

“Find a table” resembles an inked reservation stamp with a small arrow enclosed in a thin circle. Fine-pointer hover rotates only that arrow by 12 degrees. Pointer press compresses the inner surface to `scaleX: 0.98, scaleY: 0.95` in 0.08s; release returns to `1` in 0.46s with `back.out(2)`. The spring-style overshoot is an easing effect. Keep the 52px outer target stable. A 3px espresso focus ring remains visible. Pending submission uses “Checking availability…” without changing width. Reduced motion removes compression and rotation.

## Accessibility and performance

Keep all dining details in HTML, not baked into photographs or downloadable menus alone. Supply clear ingredient text without unsupported dietary guarantees. Respect `prefers-reduced-motion` through `gsap.matchMedia()`, use static menu reveals, and restore focus after dialogs. Avoid autoplay sound, custom scrolling, and parallax over form fields. Load one prioritized opening image and lazy-load the rest with reserved dimensions.

## Build acceptance criteria

1. A keyboard user can select a date, party size, and available time without opening a pointer-only calendar.
2. Cancellation terms appear before the final reservation action.
3. Failed availability checks preserve selections and provide a retry action.
4. Reduced motion keeps the full menu and reservation flow visible immediately.
