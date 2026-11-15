# PermitDesk — A review desk with a readable case history

An internal government licensing interface arranged like a structured dossier: a stable queue, evidence side by side with decisions, and a clear chain of responsibility. PermitDesk, its agency, permit types, review rules, staff, and records are fictional demonstration material; real policy and authority must be supplied by the owning organization.

## Product and core flow

For case officers and supervisors reviewing applications with multiple documents and handoffs. The main job is understanding what remains unresolved before making a reviewable decision.

Flow: choose an assigned case → inspect checklist and evidence → record findings → prepare an outcome or information request → review and submit the authorized action. Example: “PD-2084 / Community stall application / Awaiting document review.” Sample copy: “The address differs between these two files. Record a finding before requesting clarification.” This is an illustrative workflow, not a real legal requirement.

Separate internal notes from messages an applicant will receive. Clearly describe role-based permissions as intended behavior; the design itself does not implement authorization or an audit service.

## Visual system

- Canvas `#F0F0ED`; dossier `#FFFFFF`; ink `#292D36`; secondary `#5B616C`; action plum `#5E3C65`; selected tint `#EEE7F1`; divider `#C9C9D0`; warning ink `#7C5018` on `#FFF0D8`; error ink `#963333` on `#FCE9E9`.
- **Public Sans**, Arial, sans-serif for controls and narrative; **IBM Plex Mono**, Consolas, monospace for identifiers, timestamps, and document versions. Use explicit labels rather than tiny icon-only toolbars.
- Desktop title 30/36 px; mobile 25/31 px; body 16/25 px; table 14/22 px; labels 13/20 px. Use 4 px subdivisions, 24 px major gaps, and 16 px panel padding.
- The identity comes from numbered tabs, firm dividers, and pale document margins. Restrained 6 px corners distinguish controls from square document previews.

## Screen composition

At **1440 px**, give the case desk three regions: a 280 px assignment queue, a flexible evidence workspace, and a 360 px findings panel. A compact top strip shows case ID, owner, status, and freshness. The initial view exposes unresolved checks, the selected document's name/version, and the next allowed action. Queue rows stay in place while a case is open.

The evidence workspace offers document preview and an accessible extracted-text view. A checklist links each finding to its source. Findings show author, date, rationale, and whether they are internal or applicant-visible. A separate decision review screen summarizes evidence, unresolved issues, proposed wording, recipient, and authority required. History is a readable event list, not an unexplained wall of system codes.

At **390 px**, default to the assignment list. Opening a case creates a full route with Overview, Evidence, Findings, and History as labeled navigation. Documents offer download and text alternatives instead of a miniature desktop viewer. Place the decision summary and review action after the findings; preserve queue position on return. This mobile path supports inspection and permitted actions without pretending every side-by-side desktop task fits on a phone.

## Interaction and states

Checklist controls record explicit states such as Not reviewed, Meets example criteria, and Needs clarification; never make green mean “approved” without text. A missing attachment explains what is unavailable. A loading preview retains document metadata. An empty queue says “No cases match these filters” and offers reset without implying no work exists elsewhere.

Save notes as visible drafts with a last-saved indicator from the actual response. Failed saves preserve text and mark it unsaved. If another officer changes the case, show a conflict and current version before allowing resubmission. Permission-limited actions explain the required role. Requesting information, rejecting, withdrawing, or approving requires a reason, a review screen, and a deliberate final action. A proposed applicant message remains a draft until explicitly sent. Success appears only after confirmation and adds an intended history event containing actor, action, time, and reason.

## GSAP motion choreography

| Trigger | Target | Duration / ease | Intended result |
| --- | --- | --- | --- |
| Select a case | Dossier heading wrapper | `gsap.fromTo()`, opacity 0.8 → 1, 0.18 s, `power1.out` | Establish context without moving the queue or focus. |
| Switch evidence tab | Decorative tab rule | `gsap.to()`, 0.2 s, `power2.out` | Follow the selected document; actual content switches immediately. |
| Open finding details | Caret and note highlight | `gsap.timeline()`, 0.18 s, `power1.out` | Clarify the relationship without animating document text. |
| Draft save confirmed | Saved-status icon | 0.22 s opacity, `power1.out` | Quiet acknowledgement, with persistent text. |

Do not use ScrollTrigger, animated decision counters, bouncing statuses, or automatic row sorting during work. Cancel stale preview transitions on rapid case changes.

## Signature button

“Review proposed decision” uses a plum face and a small outlined dossier-tab icon. On fine-pointer hover, lift the decorative tab 1.5 px. Press the inner face to **0.99** over **0.065 s**; release to 1 over **0.28 s** using `back.out(1.08)`. This is subtle spring-style easing, not a physics model. Keep the 48 px hit area, text alignment, and 3 px charcoal focus outline stable. Activation opens review immediately. Reset after pointer cancellation, leaving while pressed, blur, or disabling. Reduced motion uses a static fill change; the final decision action stays visually sober.

## Accessibility and performance

Use semantic tables or lists, real buttons for document actions, field labels, and linked error summaries. Keep document and finding focus predictable; return focus after closing overlays. Never announce every autosave tick or poll. Protect sensitive information through the intended authorization model and avoid real personal data in prototypes. Load one document preview at a time and defer large files. Scope and clean up GSAP work. With reduced motion, every state changes immediately and the full review remains available.

## Build acceptance criteria

- An officer can trace each example finding to a named document and version using keyboard navigation.
- A conflicting update or failed draft save preserves work and cannot silently overwrite another officer's decision.
- Applicant-facing communications and final outcomes require an explicit review and authorized final action.
- At 390 px and reduced motion, queue return, document alternatives, findings, and permitted review actions remain accessible.
