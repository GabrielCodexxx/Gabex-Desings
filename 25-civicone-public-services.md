# CivicOne — Public services organized around a person's task

A government-service portal with the clarity of a well-run public counter: plain-language choices, visible next steps, and a dependable application record. CivicOne, its demonstration agency, services, requirements, records, and dates are fictional; the concept claims no actual government affiliation or legal compliance.

## Product and core flow

Serve residents who may visit infrequently, use a shared phone, or have limited bandwidth. The main job is finding the right service and understanding what happens after applying. Do not make residents learn an agency's internal organization chart.

Flow: describe the task → compare relevant services → read the service overview → complete and review an application → save the acknowledgement and track progress. Sample service: “Request a copy of an archived community record.” Sample instruction: “Check the details before you send. You can return to any section.” Requirements and fees are explicitly labeled demonstration content until supplied by the responsible agency.

Offer a visible assisted-service route, language choice, and “Save and finish later” when an actual secure resume mechanism exists. Avoid promising a completion date that the service cannot substantiate.

## Visual system

- Canvas `#F5F3ED`; surfaces `#FFFFFF`; ink `#22352F`; secondary text `#52635C`; action green `#285B45`; selected wash `#E2ECE5`; accent ochre `#B9882D`; divider `#C5CEC6`; error ink `#9A302D` on `#FDECE8`.
- **Source Sans 3**, Arial, sans-serif for navigation, forms, and body; **Source Serif 4**, Georgia, serif for service titles and introductory statements. Use the ochre only for decorative rules and large illustrations, not small text.
- Desktop title 48/54 px; mobile 32/38 px. Form headings 26/32 px, body 18/28 px, labels 16/24 px. Use 8 px spacing, 40 px desktop gutters, 20 px mobile gutters, and a 720 px form measure.
- A simple text agency identifier and a thin green rule establish identity. No invented seal, national emblem, gradients, glass panels, or stock photograph behind instructions.

## Screen composition

At **1440 px**, the header clearly reads “CivicOne demonstration agency” above a compact navigation bar. The opening screen uses a seven-column task finder beside a five-column service-status and help panel. A large labeled search field asks “What do you need to do?” Beneath it, show a short ordered list of common tasks with one-line explanations, not decorative category cards. Keep “Track an application” visible without scrolling.

The service overview is a document-like page with Purpose, Before you start, Example requirements, Possible charges, and What happens next. The application uses one meaningful section per page with a numbered progress list. The review page repeats answers with specific Change links. The acknowledgement page provides a reference, current status, submission time, and a printable summary without exposing sensitive details publicly.

At **390 px**, stack task discovery before status and help. Convert the progress list into “Step 2 of 4” plus a labeled disclosure containing all steps. Keep Back, Save, and Continue in document flow. Status tracking opens as a full page; long references wrap rather than widening the screen.

## Interaction and states

Search returns useful task names and an alternative help route when nothing matches. Do not require registration merely to read service instructions. Sensitive application status requires an appropriate authenticated or verified flow; a reference alone must not reveal personal information. Loading retains the page title and explains the activity once. Validation preserves answers, focuses an error summary, and links each error to its field.

If a saved application changes elsewhere, show the latest version and let the resident review differences before continuing. A failed submit retains input and states whether receipt is known. Prevent duplicates while pending. Show “Application received” only after acknowledgement; distinguish Received, Under review, More information requested, and Completed in words. On shared devices, offer a clear sign-out and avoid leaving personal data in browser storage without an explicit product decision.

## GSAP motion choreography

| Trigger | Target | Duration / ease | Intended result |
| --- | --- | --- | --- |
| Service page opens | Decorative title rule | `gsap.fromTo()`, scaleX 0.9 → 1, 0.3 s, `power2.out` | A small editorial cue while the heading and action are already visible. |
| Continue to valid step | Incoming section wrapper | `gsap.to()`, opacity 0.85 → 1, 0.18 s, `power1.out` | Confirm a deliberate step change without sliding the form. |
| Expand guidance | Disclosure caret only | 0.16 s rotation, `power2.out` | Content and expanded state change immediately. |
| Submission acknowledged | Confirmation icon | `gsap.timeline()`, 0.25 s, `power2.out` | One quiet checkmark after the receipt exists. |

No ScrollTrigger, animated progress percentages, auto-scrolling explanations, or entrance gates in the application.

## Signature button

“Continue to review” is forest green with a right arrow inside a fixed icon compartment. Fine-pointer hover moves the arrow 2 px; no essential information depends on hover. Press scales its inner face to **0.985** over **0.08 s**; release returns to 1 over **0.32 s** using `back.out(1.15)`. This is restrained spring-style easing, not physical simulation. Keep the 48 px outer target and 3 px ink focus ring stationary. Begin validation on native activation immediately. Reset the face on pointercancel, leaving while pressed, blur, or disabling. Reduced motion uses an immediate fill change and static pending text.

## Accessibility and performance

Use visible labels, sensible autocomplete, semantic fieldsets, a skip link, and a logical heading order. Explain required fields in text; never clear a form because a session expires without an opportunity to preserve work securely. Support keyboard, touch, 200% text zoom, and a complete text-first experience. Avoid mandatory maps, autoplay, and unnecessary font weights. Scope GSAP and revert it on route changes. Reduced motion displays final states instantly; animation failure never hides content or blocks submission.

## Build acceptance criteria

- A resident can identify a service and read its example requirements without signing in.
- Keyboard users can correct every validation error and review changed answers without losing data.
- A failed or uncertain submission never displays a false acknowledgement or creates an automatic duplicate.
- At 390 px, low-bandwidth mode, and reduced motion, discovery, application review, and secure status tracking remain usable.
