# Council — A Deliberate Governance Workspace

A board and committee workspace designed as a contemporary meeting dossier: document hierarchy, version certainty, restrained annotation, and explicit decision ownership. Council, committees, participants, and meeting records are fictional.

## Product and core flow

Serve authorized committee members, secretaries, and meeting coordinators preparing and following up on a meeting. The principal journey is **open the meeting → verify the current pack → inspect an agenda item → add a private note or assigned action → review the meeting's recorded outcomes**.

Sample header: “Facilities Committee / Session 04 / Demo meeting / 10:00–11:30 PHT, UTC+8.” An agenda item says “04. Workspace renewal proposal / For discussion / Pack version 3.” A recorded outcome must distinguish “Proposed,” “Reviewed,” and “Confirmed” according to the organization's configured process. The visual design does not establish legal validity, statutory retention rules, or actual permission enforcement.

## Visual system

- **Palette:** dossier paper `#F4F1EB`; surface white `#FFFFFF`; graphite `#282F34`; secondary text `#606970`; burgundy action `#753E4D`; pale active sheet `#EEE2E5`; divider `#C9CDCB`; dark teal status `#285B51`.
- **Typography:** Source Serif 4, Georgia, serif for meeting names and agenda headings; Inter, Arial, sans-serif for tools, lists, metadata, and controls. Document versions use tabular figures.
- **Scale:** desktop title 36/44 px, agenda title 25/33 px, document reading 18/29 px, interface 15/23 px, metadata 13/20 px. Mobile title 28/36 px and reading text 17/28 px.
- **Geometry:** 8 px spacing, 24 px desktop outer margins, 20 px mobile margins, 12 px agenda gaps, and 4 px control corners. Paper panels use thin borders, not stacked shadows. Focus on ordered information and a generous reading measure.

## Screen composition

At **1440 px**, use a 280 px agenda rail, a flexible central reading pane, and a 300 px contextual notes column. A 72 px meeting bar shows title, local time, pack version, and an explicit access label. The first viewport exposes the selected agenda item, its purpose, current source document, and note visibility. Do not begin with a generic meeting-statistics dashboard.

The agenda rail shows order, title, purpose, and unread-document indicators with text equivalents. The reading pane offers document title, version, publication time, page navigation, download permission where applicable, and an HTML item summary. The notes column separates My private notes from Shared actions using clearly labeled modes. Supporting screens include version comparison, a meeting action register, and a draft outcome review with named owners and dates.

At **390 px**, the agenda becomes the landing view. Selecting an item opens its summary and document with an explicit Agenda return link. Notes and Actions are separate labeled tabs below the item heading, not floating icons over the document. Provide readable text summaries and an intentional full-screen document viewer; do not shrink a desktop PDF into the whole mobile workflow. Return navigation restores the prior agenda position.

## Interaction and states

Private notes never become shared when switching tabs. Any publish or share action shows the intended audience and a reviewable preview. Loading retains the selected agenda item and document frame. An empty note state says “Only you can see notes in this section” only when that access rule is actually enforced in the implementation. Otherwise prototype copy states the intended privacy model. Failed saves retain a visibly unsaved draft. A newer pack version triggers a notice with Review changes; it does not silently replace the document while someone reads. A lost permission removes protected content and explains the next step. Confirmed saves name the note or action and timestamp. Releasing minutes or recording an attributable decision requires a distinct explicit review action; opening a document never publishes anything.

## GSAP motion choreography

| Trigger | Target | Duration / ease | Result |
| --- | --- | --- | --- |
| Open meeting dossier | Agenda and reading shells | `gsap.timeline()`, 0.24 s, `power1.out` | A short opacity entrance that leaves document tools immediately available. |
| Select agenda item | Decorative edge tab | `gsap.to()`, 0.2 s, `power2.out` | Mark the selected item without moving agenda rows. |
| Open version comparison | Comparison header | `gsap.fromTo()`, y: 6 → 0, 0.2 s, `power2.out` | Orient the reader while document content changes directly. |
| Note save confirmed | Small saved-state stamp | 0.26 s, `back.out(1.08)`, scale 0.94 → 1 | One restrained acknowledgement in a reserved position. |

No ScrollTrigger, animated page turning, floating document parallax, or automatic agenda progression.

## Signature button

“Save private note” is an understated burgundy-outlined button with a narrow inset rule. Fine-pointer hover lengthens only the rule by **4 px** within reserved space. Press scales the inner visual face to **0.992** over **0.055 s**; release returns to 1 over **0.25 s** with `back.out(1.06)`. The gentle spring-style easing is not a physical spring model. Keep the outer target and 3 px graphite focus ring stationary. Native activation saves immediately and pending text prevents duplicate work. Restore visuals on pointer cancellation, pressed-pointer leave, blur, or disabling. Reduced motion replaces all movement with a static fill change and an explicit saved/unsaved label.

## Accessibility and performance

Provide semantic agenda lists, correctly implemented tabs, real document titles, and stable focus after pane changes. Keyboard shortcuts must be optional, documented, and inactive while typing. Ensure the access model applies to document retrieval as well as visible controls; the brief specifies behavior, not security certification. Avoid caching protected packs without a deliberate implementation policy. Announce save results rather than every autosave attempt. Load only the current document preview, retain readable item summaries if preview fails, and scope/revert GSAP contexts on meeting changes. Reduced motion preserves version notices and all review steps.

## Build acceptance criteria

- A participant can identify the meeting, selected agenda item, current document version, and note audience without opening settings.
- A failed save retains a recoverable draft, and a new pack version never silently replaces the current reading context.
- Keyboard users can inspect an item, save a note, and review an assigned action at desktop and 390 px widths.
- Sharing, decision confirmation, and minutes release require explicit review; reduced motion leaves every state understandable.
