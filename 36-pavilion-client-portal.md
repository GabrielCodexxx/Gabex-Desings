# Pavilion — A client portal built around clear decisions

A service-business project dossier with milestone context, a legible review surface, and version-specific approvals. Pavilion, its clients, projects, dates, and files are fictional examples.

## Product and core flow

Design for clients reviewing architecture, brand, or digital work. The job is understanding the requested decision, reviewing the deliverable, and responding unambiguously.

Flow: open a project → identify the current review milestone → inspect the named deliverable version → add comments or request changes → review the decision summary → submit and receive acknowledgement. Sample copy: “Cedar House identity / Milestone 02: Direction review / Version 3.” A review action says “Approve version 3,” never the vague “Done.” Request changes asks for a clear description and distinguishes optional annotations from required response text.

Keep approval scope explicit: approving a design version never silently approves fees, future revisions, or other documents. The business supplies production approval wording and permissions.

## Visual system

- Dossier ground `#F3EFEA`; file canvas `#FFFFFF`; aubergine ink `#342E39`; secondary `#655D6A`; plum action `#5F3C68`; pale lavender selection `#EDE3F0`; divider `#D0C5D2`; caution ink `#825116` on `#FFF1D8`.
- **Plus Jakarta Sans**, Arial, sans-serif for navigation, file names, and controls; **Libre Baskerville**, Georgia, serif for milestone titles and project introductions.
- Desktop project title 38/44 px; mobile 29/36 px; milestone title 28/35 px; body 16/26 px; metadata 13/20 px.
- Use an 8 px spacing grid, 40 px desktop margins, 20 px mobile margins, 10 px file frames, and 48 px controls. Thin numbered tabs and generous margins define the dossier.

## Screen composition

At **1440 px**, a 240 px project spine lists Overview, Milestones, Files, Decisions, and Messages. The central review canvas occupies the remaining width, with a 320 px decision panel on the right. The opening viewport names the project, milestone, deliverable, version, due date if supplied, and requested decision. A preview sits beside a compact summary of what changed since the previous version. Keep Download original available outside the preview.

The decision panel separates Add comment, Request changes, and Approve version. The overview is a chronological milestone ledger with owner and status. File history groups versions under a stable deliverable identity. The decision register records actor, version, scope, timestamp, and acknowledgement state. A conversational “looks good” never silently becomes approval.

At **390 px**, show project context, version selector, preview or download, change summary, comments, then decision controls. The project spine becomes a labeled menu. Decisions use dedicated review screens with the version name repeated above the final action. Annotation tools are optional; the plain comment list and page reference input provide the full review path without a canvas.

## Interaction and states

Version selection preserves the current comment draft or asks before discarding it. A newly uploaded version shows a clear banner; it never replaces the file under an open review automatically. If a version is superseded or access changes, block only the affected decision and explain how to review the current version. Preview loading reserves its frame and offers the original file. Unsupported previews provide filename, format, size, and download. Empty comments invite the first note; failed comments remain visibly unsent. Approval pending prevents duplicate decisions, and success appears only after acknowledgement for the exact version. Conflicts retain the proposed response and require renewed review. Offline mode labels local drafts and disables authoritative decisions with an explanation.

## GSAP motion choreography

| Trigger | Target | Duration / ease | Result |
| --- | --- | --- | --- |
| Open milestone | Milestone title and dossier tab | `gsap.timeline()`, 0.3 s, `power2.out`, y 8 → 0 | Establish the review context while the file controls remain available. |
| Change preview version | Preview visual wrapper | `gsap.to()`, 0.18 s opacity crossfade, `power1.out` | Swap only after the new asset is ready; keep its version label immediately correct. |
| Open decision review | Decorative review-rule | 0.22 s, `power2.out`, scaleX 0.8 → 1 | Mark the commitment step without moving the confirmation text. |
| Decision acknowledged | Small decision seal icon | `gsap.fromTo()`, 0.32 s, `back.out(1.12)`, scale 0.9 → 1 | Quiet completion in a reserved slot, without confetti or a fake official stamp. |

Do not scrub files with scroll, animate comment coordinates, or delay approval processing for a completion sequence. No ScrollTrigger is needed.

## Signature button

Review approval is a plum button with an inset document-check icon. Fine-pointer hover moves only the check **2 px** upward. Press its inner face to **0.98** over **0.08 s** and release over **0.37 s** using `back.out(1.22)`. This is spring-style easing, not physical simulation. The stationary outer control retains a 48 px hit area and 3 px ink focus ring. Activation opens review immediately; final approval is a separate explicit action naming the version. Reset on pointercancel, release outside, blur, or disabling. Reduced motion uses immediate fill and icon changes with no scaling.

## Accessibility and performance

Provide a downloadable accessible source document or a structured text alternative where supplied. Do not make image annotation the only means of feedback. Give preview zoom controls accessible names and maintain a logical tab sequence outside the canvas. Decision errors focus a linked summary, preserving the response. Keep permission-sensitive actions explained rather than implying access from visual state alone. Load large previews on demand, scope GSAP contexts, cancel old crossfades on version changes, and remove all movement under reduced motion.

## Build acceptance criteria

- Every approval and change request names the exact deliverable version and scope before submission.
- A new upload cannot silently replace a file under active review or inherit its pending approval.
- Failed or offline comments remain recoverable, and authoritative success waits for acknowledgement.
- Keyboard users at 390 px can review an alternative file view, leave feedback, and complete the same decision flow without canvas annotation.
