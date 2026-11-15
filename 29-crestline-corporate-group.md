# Crestline — A Corporate Group With a Clear Structure

An authoritative corporate website presented as an institutional editorial: strong business narratives, a visible group structure, and a dependable document centre. Crestline, its divisions, projects, and example publications are fictional.

## Product and core flow

Serve prospective partners, job candidates, journalists, and readers seeking company information. The primary journey is **understand the group → choose a business division → inspect its capabilities and projects → find the responsible contact or source document**. A second direct path leads returning visitors to publications without passing through marketing content.

Sample navigation: “The group / Our businesses / Projects / Publications / Careers / Contact.” Example division: “Crestline Infrastructure — Planning, delivery, and ongoing asset services.” Say “Read the group profile” rather than “Discover limitless possibilities.” Credentials, locations, clients, ownership information, financial results, and sustainability statements must come from supplied records. Illustrative content carries a visible sample label; omit unsupported accolades and growth counters.

## Visual system

- **Palette:** institutional navy `#182D40`; paper `#F3F0E8`; white `#FFFFFF`; body ink `#22313B`; secondary text `#52616A`; accessible copper action `#87472C`; decorative copper `#B87852`; rules `#C9CEC9`.
- **Typography:** Libre Baskerville, Georgia, serif for editorial titles; IBM Plex Sans, Arial, sans-serif for navigation, captions, division names, and document metadata. Keep report codes in tabular figures rather than decorative monospace blocks.
- **Scale:** desktop feature 68/74 px, section title 38/45 px, body 17/28 px, metadata 13/20 px. At mobile, use 40/46 px, 28/35 px, and 16/26 px respectively.
- **Geometry:** 12 columns, 64 px desktop gutters, 24 px column gaps, 20 px mobile gutters, and an 8 px spacing base. Editorial images have square edges. Controls use 4 px corners and 48 px minimum height. Thin rules and numbered division labels establish order.

## Screen composition

At **1440 px**, place a 96 px masthead above a five-column editorial statement and a seven-column documentary image. The opening viewport explains what the group does and exposes a compact, numbered division index. A slim publications link and contact route remain visible; avoid an oversized carousel or a generic row of three benefit cards.

Below, a vertical business atlas pairs each division with its actual scope, selected project, and accountable contact route. A project detail includes problem, contribution, partners where supplied, and dated status. The group page shows a readable organization diagram with an equivalent nested text list. The publication centre uses a filterable document ledger: title, period, publication date, file type, size, language, and download action. A report detail offers an HTML summary and a clearly named file.

At **390 px**, the masthead becomes a labeled menu, the division index becomes stacked links, and the photograph follows the introductory statement. The organization list replaces the visual diagram by default. Documents become grouped records with their metadata beside the download action. Keep division links and the report search easy to find without endless decorative scrolling.

## Interaction and states

Use real links for division navigation and downloads. Menu disclosure communicates expanded state, traps focus only if implemented as a modal, and returns focus to its trigger. Report filters expose their selections and result count; an empty result provides Clear filters. Loading reserves document-row height. A failed document request states which file failed and offers retry or a contact route. Do not silently replace a missing report with another period. A contact form preserves the selected business and message after validation or network errors. Success confirms receipt only after acknowledgement. Stale publication metadata displays its last update rather than pretending to be current.

## GSAP motion choreography

| Trigger | Target | Duration / ease | Result |
| --- | --- | --- | --- |
| First feature render | Image wrapper and decorative rule | `gsap.timeline()`, 0.65 s, `power3.out` | Image settles from y: 18; rule extends within its reserved track. Text and links remain ready. |
| Business section enters | Image caption and division numeral | `ScrollTrigger`, once, 0.4 s, `power2.out` | A small 10 px reveal supplies editorial rhythm without pinning. |
| Division selection | Decorative index marker | `gsap.to()`, 0.24 s, `power2.out` | Follow the chosen item while navigation proceeds normally. |
| Publication filters change | New result contents | 0.16 s opacity, `power1.out` | Clarify changed results without staggering rows or displacing focus. |

## Signature button

“Read the group profile” is an outlined navy link with a copper arrow compartment. Animate only its inner arrow tile: press scale **0.955** over **0.09 s**, release over **0.42 s** using `back.out(1.35)`. This is spring-style easing, not a physical spring simulation. Fine-pointer hover moves the arrow 3 px right; the label and hit target stay fixed. A 3 px navy focus outline surrounds the whole link. Enter navigates immediately. Restore decoration on pointer cancellation, pressed-pointer leave, blur, and route teardown. Reduced motion uses an instant fill change with no scale or travel.

## Accessibility and performance

Provide skip links, semantic landmarks, descriptive report names, and text alternatives for diagrams. Do not imply that a supplied PDF is accessible without reviewing it; provide key information in HTML. Keep photography responsive and defer below-fold imagery. No automatic video playback, animated credibility metrics, or scroll interception. Scope GSAP contexts and revert on navigation. Reduced motion presents all final compositions immediately and retains selected indicators, document metadata, and readable confirmations.

## Build acceptance criteria

- A visitor can identify a relevant division and its contact route from the homepage without waiting for animation.
- The publication centre exposes period, language, file type, and size before a download starts.
- At 390 px and by keyboard, organization information and reports remain usable without page-level horizontal scrolling.
- Unsupported credentials never appear as factual claims, and reduced motion preserves the full corporate narrative.
