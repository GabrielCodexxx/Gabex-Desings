# Origin — Procurement as a Traceable Decision

A corporate sourcing and requisition workspace built around comparable evidence, visible approval steps, and a dependable purchasing record. Origin, suppliers, quotations, prices, and approval examples are fictional.

## Product and core flow

Serve purchasing coordinators and authorized approvers evaluating a business request. The job is to turn a clearly described need into a reviewable sourcing decision without losing quote context.

Flow: define the requirement → collect and normalize supplier quotes → compare equivalent scope → select an option with a reason → submit the requisition for review → track its decision. Sample requirement: “Replacement task chairs / 24 units / Operations floor.” A summary says “Submitted for review. No purchase order has been issued.” Approval thresholds, tax treatment, supplier eligibility, and actual purchasing authority must be supplied by the organization rather than invented by the design.

## Visual system

- **Palette:** stone canvas `#F1F2EE`; white surfaces `#FFFFFF`; blue-black text `#20313B`; muted text `#596A70`; indigo action `#384E83`; selected wash `#E7ECF8`; rules `#C9D0CF`; amber text `#815017` on `#FFF0D5`.
- **Typography:** Public Sans, Arial, sans-serif for forms and tables; IBM Plex Mono, Consolas, monospace for requisition IDs, quote versions, and totals. Use tabular figures and explicit currency codes.
- **Scale:** desktop title 32/39 px, section title 22/29 px, table and body 15/23 px, metadata 13/19 px. At mobile use 26/33 px title and 16/25 px body.
- **Geometry:** a 4 px subdivision within an 8 px rhythm, 32 px desktop page margins, 16 px table cell padding, 20 px mobile margins, 6 px corners, and 48 px primary controls. Rows and definition lists do the structural work; avoid decorative KPI tiles.

## Screen composition

At **1440 px**, a 200 px navigation rail supports a requisition header, a horizontal process tracker, and a comparison workspace. The first viewport contains the requirement summary, version, status, current responsible person, and the key supplier comparison. A 300 px decision rail shows the selected offer, included scope, missing evidence, and Review requisition.

The comparison matrix gives suppliers columns and attributes rows: unit price, currency, quantity, delivery assumption, inclusions, exclusions, quote date, and validity as supplied. Missing values read “Not provided,” never zero. Separate rows distinguish normalized totals from original quoted values and explain calculations. A source link opens each quote beside its extracted fields. Supporting screens include supplier documents, a requisition review page, and a chronological approval history with actor and timestamp.

At **390 px**, default to attribute-by-attribute comparison: an attribute heading followed by supplier values, preserving full labels. Offer an optional horizontally scrollable matrix within its own region. The decision rail becomes an inline summary after the comparison. Quote review opens as a separate route with a visible return link. Approval steps become a vertical ordered list. Do not compress currency values into unlabeled abbreviated numbers.

## Interaction and states

Supplier choice uses a labeled radio group and a required rationale where the configured workflow needs one. Attachment upload exposes progress, filename, type, and retry; failed uploads do not appear as accepted evidence. Loading reserves the comparison structure. An empty sourcing request explains what evidence is missing. Validation links the review summary to incomplete fields. If a quote expires or another coordinator changes the requisition, preserve the draft and show the newer version for review. Submitted, awaiting clarification, approved, rejected, and order-issued remain distinct states. Do not imply that approval itself places an order. Rejections require an attributable reason and review step. Updating data must not reorder focused suppliers or requisitions automatically.

## GSAP motion choreography

| Trigger | Target | Duration / ease | Result |
| --- | --- | --- | --- |
| Open source quote | Document pane shell | `gsap.timeline()`, x: 14 → 0, 0.22 s, `power2.out` | Connect the source to its fields while retaining the comparison. |
| Select supplier | Decorative column header rule | `gsap.to()`, 0.18 s, `power1.out` | Highlight selection without animating totals or resizing columns. |
| Expand calculation | Disclosure chevron | 0.16 s rotation, `power2.out` | Expose the calculation immediately with a modest orientation cue. |
| Requisition acknowledged | Process marker outline | `gsap.fromTo()`, opacity 0.6 → 1, 0.25 s, `power1.out` | Mark a confirmed workflow transition with stable text. |

No ScrollTrigger, rolling totals, automatic chart scrubbing, or bouncing approval steps.

## Signature button

“Review requisition” uses an indigo face with a fixed right-hand document tab. The tab shifts **2 px** upward on fine-pointer hover. Press compresses the inner face to **0.988** over **0.06 s**; release returns over **0.28 s** with `back.out(1.1)`. This is a spring-style easing curve, not a physics simulation. Keep its hit target and 3 px dark focus outline fixed. Enter or Space activates a native button immediately. Reset the face after cancellation, pressed-pointer leave, focus loss, and disabled-state changes. Reduced motion uses static fill and label feedback. Pending submission prevents duplicate requests and never hides the reviewed total.

## Accessibility and performance

Use semantic table headers with explicit supplier and attribute associations. Provide source documents with meaningful filenames and text summaries; do not assume attachments are accessible. Format amounts consistently while retaining original values. Announce completed actions through a concise status region. Role-based decision controls and audit events are requirements for implementation, not guarantees supplied by the visual prototype. Lazy-load document previews, preserve focused records when lists refresh, and scope/revert GSAP work. Reduced motion removes movement without losing source context, selected state, or error recovery.

## Build acceptance criteria

- Every compared total can be traced to a supplied quote and an explained calculation, with missing values visibly distinct from zero.
- A user can inspect sources, select a supplier, explain the choice, and review the requisition using only the keyboard.
- Version conflicts and failed uploads preserve input and prevent an outdated or incomplete submission from appearing successful.
- At 390 px, supplier comparisons retain attribute labels, and approval never masquerades as order issuance.
