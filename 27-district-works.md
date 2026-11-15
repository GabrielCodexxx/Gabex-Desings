# District Works — A public maintenance request with a visible next step

A local-government public works service that connects a clear resident report to an accountable staff work order. District Works, its districts, reports, priorities, response targets, and agency identity are fictional. It is a non-emergency service concept, not a live emergency or dispatch system.

## Product and core flow

Serve residents reporting ordinary infrastructure problems and coordinators assigning the resulting work. The core citizen task is describing a problem and receiving a meaningful reference; the staff task is assigning an owner without losing the resident's context.

Citizen flow: choose an issue → provide a location → describe it and optionally add a photo → review privacy and details → submit and track. Staff flow: inspect the queue → validate category and location → assign an example crew → update work status → record completion evidence.

Sample copy: “Uneven paving near the east library entrance” and “Add a street or landmark. A map is optional.” Put “For routine maintenance requests only” near the start and provide an agency-configured emergency-help link without inventing a real telephone number or response promise.

## Visual system

- Canvas `#F4F1E8`; surfaces `#FFFFFF`; ink `#2B332D`; secondary `#59635A`; action rust `#8B422B`; pale action `#F3E5DC`; green status `#315C44`; divider `#C8CEC0`; caution ink `#79500F` on `#FFF1CA`.
- **Atkinson Hyperlegible**, Arial, sans-serif for form instructions and status; **Barlow Condensed**, Arial, sans-serif for large district labels and queue headings. Condensed type never appears in dense body copy.
- Desktop title 46/50 px; mobile 32/36 px; body 18/28 px; status text 15/23 px; labels 16/24 px. Use an 8 px spacing rhythm, 32 px desktop gutters, 20 px mobile gutters, and 48 px controls.
- Use a topographic line motif only in empty margins. Category illustrations are simple street-level line drawings; status comes from words and shapes as well as color.

## Screen composition

At **1440 px**, the resident opening screen uses a six-column issue list and a six-column “What happens after you report” strip with a sample reference lookup. The first viewport names the agency demonstration, explains the scope, and makes Report a problem prominent. Categories are large rows with a short explanation, not anonymous pictogram cards.

The report form is a narrow reading column with an adjacent help rail. The location step pairs an address field with an optional map and a textual location summary. The review page shows issue, approximate location, description, attachments, and contact preferences. The receipt states the actual acknowledged status and offers a print/download summary.

The staff screen is a separate workspace: a grouped work-order list occupies eight columns while a four-column assignment inspector shows owner, last update, and next action. A map is optional, never the sole queue. At **390 px**, citizen help appears directly after its related field, maps become opt-in, and staff assignments open as full-page details. Preserve filters and queue position on return.

## Interaction and states

Offer address entry, landmark text, and accessible map controls rather than requiring a pin drag. A possible duplicate report is a suggestion with a visible Continue anyway path. Photo upload shows file name, progress, remove/retry actions, and an explanation if the file is unsupported. Do not require a photo. Validation preserves the narrative and focuses a linked error summary.

If connection drops, distinguish an unsent local draft from an acknowledged request; do not store sensitive photos on a shared device without a deliberate policy. Duplicate-submit protection remains active while awaiting receipt. Public tracking shows only approved, privacy-filtered information. Contact details, exact private addresses, and internal notes stay in the intended restricted view. Empty staff queues retain active filters. Conflicting assignments show the latest owner before retry. Closing or declining a report requires a reason, a review, and a recorded actor/time; success is shown only after confirmation.

## GSAP motion choreography

| Trigger | Target | Duration / ease | Intended result |
| --- | --- | --- | --- |
| Choose issue category | Selected row's decorative edge | `gsap.to()`, 0.18 s, `power2.out` | Reinforce selection while label and state update immediately. |
| Location resolved | Location-summary icon | `gsap.fromTo()`, opacity 0.65 → 1, 0.22 s, `power1.out` | Confirm that the text refers to the chosen location; no automatic map flight. |
| Open staff assignment | Inspector surface | 0.2 s, `power2.out`, x 12 → 0 | Small contextual entrance without shifting the queue. |
| Receipt acknowledged | Static status marker | `gsap.timeline()`, 0.26 s, `power2.out` | One check reveal after the reference is available. |

No ScrollTrigger, pulsing map markers, animated urgency, or row movement during staff selection.

## Signature button

“Review this report” is a rust rectangle with a paper-colored forward arrow. On fine-pointer hover, the arrow advances **2.5 px**. Press the inner face to **0.982** over **0.085 s**; release to 1 over **0.34 s** using `back.out(1.18)`. This supplies restrained spring-style overshoot, not physical dynamics. The outer 48 px target and 3 px ink focus outline remain fixed. Native activation moves to review immediately. Reset the visual after cancellation, pointer leave while pressed, focus loss, or disabling. Reduced motion changes the fill instantly with no displacement.

## Accessibility and performance

Use labeled fieldsets, text status histories, optional contact channels, and meaningful heading order. Do not require precise map interaction, image interpretation, or hovering. Support a text-only report with no map downloads. Provide a public-safe description separate from restricted notes. Compress optional previews, reserve image dimensions, and load maps only when requested. Scope and revert GSAP on navigation; reduced motion removes spatial transitions. A failed map or animation script must not prevent reporting or staff review.

## Build acceptance criteria

- A resident can submit a complete text-only report without a map, photo, or pointer device.
- Pending, unsent, received, assigned, and closed states are visibly distinct and never inferred from animation.
- Public tracking omits private contact data and restricted staff notes; destructive status changes require reason and review.
- At 390 px and reduced motion, citizens can review reports and staff can assign work without losing queue context.
