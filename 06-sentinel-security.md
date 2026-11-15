# Sentinel Security — Account protection explained in plain language

A fictional account-security console that makes sessions, sign-in methods, and recovery actions understandable through clear timelines and consequence-aware controls.

## Product and core flow

Design for an account owner investigating an unfamiliar sign-in or improving account access. The main journey is **review current security state → inspect an event or session → understand available actions → complete the required verification → see the confirmed result**. Do not reduce security to a decorative percentage score.

Example content: “3 active sessions,” “Current session / Windows / Last activity 2 minutes ago,” and “Location is approximate and may reflect a network provider.” Demo events must be labeled. “Review unfamiliar session” invites investigation rather than declaring a breach. Security state and action outcomes must originate from the backend; a completed animation never means a session was actually revoked.

## Visual system

- **Palette:** porcelain `#F4F6F8` canvas, white `#FFFFFF` panels, midnight `#172A3A` headings and primary text, slate `#526579` supporting text, deep blue `#2458A5` actions, amber ink `#805000` on `#FFF0CB` for review items, red `#A52A2A` for destructive controls.
- **Type:** Inter with Arial fallback for the interface; IBM Plex Mono with monospace fallback for event identifiers and recovery-code presentation. Desktop page title 32/40px, mobile 26/34px; body 16/25px; event labels 14/21px. Keep recovery codes large enough to read without zoom.
- **Geometry:** 248px desktop navigation rail, 40px content margins, 24px gaps. At 390px, use a compact top navigation disclosure and 16px margins. Spacing: 4, 8, 12, 20, 32, 48px. Panels have 10px radii, with no translucent overlays behind critical text.

## Screen composition

At 1440px, open with the account name and a plain status sentence, followed by a wide “Actions to review” region and a narrow recovery-readiness panel. Beneath, display active sessions as a structured list with device, rough location, last activity, and a specific review action. Sign-in methods and recovery options live on separate routes, keeping the opening screen focused.

The session detail screen shows a chronological event ledger and a clearly separated action area. A revocation confirmation names the selected session and explains what will happen. A sign-in-method setup page uses numbered steps and authentic server-generated enrollment information. A recovery screen emphasizes secure storage and shows actual codes only when authorized.

At 390px, actions to review appear first, followed by the current session and the remaining session list. Device information wraps into two lines without truncating essential status. Confirmation dialogs become constrained full-width sheets with a clear heading and cancel control. Recovery codes are presented in a readable single-column list, with copy and download actions that respect authorization and disclosure rules.

## Interaction and states

Use explicit actions such as “Sign out this session” rather than ambiguous icons. Before a consequential change, explain the affected session and any required reauthentication. Trap focus only within an actual modal; return it to the source control afterward. Loading skeletons preserve list geometry. An empty additional-session list says “No other active sessions.” A failed revocation leaves the session visible and offers retry. A pending state remains pending until the server confirms. Never expose recovery codes in toast messages, analytics, or decorative animation.

## GSAP motion choreography

| Trigger | Target | Duration / ease | Intended result |
|---|---|---|---|
| Open event detail | Supplemental timeline panel | `gsap.to()`, 0.2s, `power2.out` | Fade and move 12px, keeping the selected event anchored. |
| Open confirmation | Dialog surface | `gsap.fromTo()`, 0.18s, `power2.out` | Enter from 8px below; text remains crisp and readable. |
| Verification succeeds | Non-sensitive confirmation mark | `gsap.timeline()`, 0.3s, `power2.out` | Draw a small checkmark once after server confirmation. |
| Close detail | Panel surface | 0.14s, `power1.in` | Exit without delaying focus restoration or route navigation. |

Keep event data and recovery codes static. Do not use `ScrollTrigger`, perpetual pulses, or bouncing warnings in security workflows.

## Signature button

“Review session” has a deep-blue outline and a small inset chevron. Fine-pointer hover moves the chevron 2px over 0.14s. Press scales only its inner surface to `0.99` in 0.06s; release returns over 0.27s with `back.out(1.1)`. This subtle spring-style effect is an eased overshoot. Keep the outer 48px target stationary, add a 3px midnight focus outline, and preserve labels during pending states. Destructive actions use a separate static red treatment. Reduced motion removes the scale and chevron movement.

## Accessibility and performance

Use semantic headings, lists, forms, and buttons. Connect errors to fields and use a polite live region for confirmed outcomes; urgent server-reported failures can receive an appropriate alert. `gsap.matchMedia()` disables movement under reduced motion and cleanup reverts animations. Avoid automatic list reordering, scroll trapping, hidden essential instructions, and exposing private information in the document before it is authorized.

## Build acceptance criteria

1. A failed or pending revocation can never display the confirmed-success state.
2. Keyboard focus returns to the correct session action after a dialog closes.
3. Location estimates are labeled as approximate, and review states do not imply proven compromise.
4. Reduced motion retains every action and confirmation without translation or scale effects.
