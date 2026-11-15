# Accord — A Considerate Employee Workspace

A corporate people-operations system organized around personal tasks, clear requests, and accountable approvals. Accord, its employees, sample balances, and policy examples are fictional.

## Product and core flow

Serve employees requesting time away and managers reviewing requests within their authorized scope. The principal flow is **review available options → enter dates and request type → inspect the request summary → submit → track the decision**. Managers have a separate task flow: open an assigned request, inspect relevant scheduling context, request clarification or record a decision, and verify the resulting state.

Sample copy: “Time away / 12–13 April / 2 working days in this example calendar” and “Submitted for review; these dates are not approved yet.” Balances, working calendars, eligibility, required fields, and routing come from the organization's configured policy. Do not encode real statutory entitlements or present demo balances as employment advice. Avoid unnecessary health details in free-text fields.

## Visual system

- **Palette:** warm canvas `#F5F2F4`; white surfaces `#FFFFFF`; plum ink `#352E3C`; secondary text `#655B6A`; action plum `#653E70`; pale selected background `#EDE3F0`; rule `#D6CCD9`; warning ink `#855013` on `#FFF1DA`.
- **Typography:** DM Sans, Arial, sans-serif for interface and employee tasks; Lora, Georgia, serif only for a brief welcome line and section introductions. Never use the serif for dense balances or dates.
- **Scale:** desktop heading 34/42 px, section 23/30 px, body 16/25 px, labels 13/20 px. Mobile heading 28/35 px; body stays 16/25 px. Use tabular date and balance values.
- **Layout:** 8 px spacing, 24 px desktop gutters, 20 px mobile gutters, 16 px panel gaps, 10 px corners, and 48 px controls. Use calm ruled lists and one warm section label, rather than a grid of employee scorecards.

## Screen composition

At **1440 px**, use a 216 px navigation rail and a three-part working area. A broad personal task column sits beside a modest calendar and a narrow requests summary. The first viewport shows “Your next actions,” a clear Request time away button, and the status of the latest request. Balances have explanations and an “As of” timestamp; they are not oversized performance metrics.

The request screen uses a two-column form and live summary. Dates, type, and an optional handover note appear on the left; calculated days, calendar assumptions, and approver destination appear on the right. Review precedes submission. The manager screen separates requests needing action from a read-only team schedule and shows only necessary information. Request detail includes the submitted values, clarification thread, decision, and dated history.

At **390 px**, place tasks before the calendar. The calendar becomes an accessible upcoming-date list with an optional month view. Stack the request form above its summary, then offer Review request. Manager queues become individual request records. Detail opens as a full route with Back to requests restoring filters and scroll position. Sensitive information never depends on hover reveals.

## Interaction and states

Allow typed dates as an alternative to the picker, stating the expected format. Selection and calculated day counts update immediately with explicit assumptions. Loading shows stable balance placeholders; unavailable balances say “Balance could not be retrieved,” with a retry action. Empty requests explain how to create one. Preserve the draft after validation or submission errors. If the calendar or balance changes during review, show the new calculation and require the employee to review again. Pending means submitted, not approved. A manager decision appears only after confirmation and includes its scope. Keep requests in place after updates until the user refreshes; never move a focused row automatically. Role changes must cause permissions to be checked again before exposing protected records.

## GSAP motion choreography

| Trigger | Target | Duration / ease | Result |
| --- | --- | --- | --- |
| Open request form | Form section wrapper | `gsap.fromTo()`, y: 8 → 0, 0.22 s, `power2.out` | A small orientation cue with fields immediately usable. |
| Change request type | Decorative selected marker | `gsap.to()`, 0.18 s, `power2.out` | Follow the selection; updated requirements appear immediately. |
| Expand calculation details | Caret only | 0.16 s rotation, `power1.out` | Semantic disclosure opens without moving the surrounding controls. |
| Submission acknowledged | Status icon | `gsap.timeline()`, 0.28 s, `power2.out` | A one-time check in a reserved slot; text says Submitted for review. |

Do not use ScrollTrigger, animated balances, or bouncing calendar cells.

## Signature button

“Review request” is a plum control with a small calendar-corner icon. Fine-pointer hover lifts that icon **2 px**. Press scales the inner face to **0.984** over **0.075 s**; release returns to 1 over **0.32 s** using `back.out(1.15)`. This restrained spring-style curve does not simulate physical dynamics. Keep the outer 48 px target and 3 px plum focus ring stationary. Native keyboard activation advances immediately. Restore the face on cancellation, pressed-pointer leave, blur, or disabling. Reduced motion provides an instant border/fill change, retaining all pending and decision labels.

## Accessibility and performance

Use real labels, linked field errors, an error summary, and a clear review heading. Keep private notes out of notification previews and shared calendar entries. Treat audit events and role-limited access as implementation requirements, not claims that the prototype already enforces them. Announce the result of the user's action, not every balance poll. Cache only information appropriate to the deployment's privacy model. Scope and revert GSAP contexts; remove listeners on teardown. With reduced motion, present all panels statically and preserve clear focus movement.

## Build acceptance criteria

- An employee can enter dates, correct errors, review, and submit using the keyboard without operating a visual calendar.
- A changed calculation interrupts final submission for review while preserving the draft.
- Pending, approved, declined, and clarification-needed states are textually distinct and authorized for the current user.
- At 390 px and reduced motion, personal tasks and manager decisions remain complete without exposing unnecessary private information.
