# Align — Client relationships with the next step in view

A professional CRM that combines a sales ledger with a readable relationship dossier, keeping commitments and context ahead of decorative funnel charts. Align, its businesses, contacts, deal values, and activity records are fictional.

## Product and core flow

Serve an account manager in a service business who needs to understand a relationship, identify the next commitment, and prepare a relevant follow-up. The central task is making a considered next move rather than maximizing an unexplained lead score.

Flow: open the assigned pipeline → select an opportunity → inspect stakeholders, notes, and the latest quote → prepare a follow-up draft → review recipients and content → explicitly send if authorized. Sample opportunity: “Willow Hotel / Lobby signage / Proposal shared / Next: clarify installation dates.” A draft label reads “Draft only — nothing has been sent.” Use fictional contact addresses on `example.com`.

Separate scheduling a task, changing a stage, and sending a message. Label sample quote amounts and explain the source of any probability field.

## Visual system

- Canvas `#F4F1E8`; dossier white `#FFFEFA`; ink `#26332D`; secondary `#59655D`; olive action `#465A32`; selected wash `#E6EBD8`; amber annotation `#E7C675`; warning text `#7B4E13`; rules `#C8CEC1`.
- **DM Sans**, Arial, sans-serif for controls and ledger rows; **Lora**, Georgia, serif for client names and short relationship summaries.
- Desktop page title 34/40 px; mobile 28/34 px; client heading 30/36 px; body 16/25 px; metadata 13/20 px. Tabular numerals support values and dates.
- Use 8 px spacing, 32 px desktop margins, 20 px mobile margins, 6 px corners, and 48 px controls. Use ruled surfaces and understated amber notes.

## Screen composition

At **1440 px**, a 200 px navigation rail leads to a two-part workspace: a flexible opportunity ledger and a 440 px relationship dossier. The first viewport shows owner and stage filters, an explicit Table/Board switch, opportunity name, client, stage, next commitment, value, and last activity. The dossier opens with client name, relationship owner, next step, and stakeholder list before the activity history.

Board view uses readable stage columns with a count and a concise definition. Every card has a Move to stage action; dragging is optional. The quote screen presents version, line items, share history, and status. A follow-up composer starts beside the selected quote and includes recipients, subject, body, attachments, and a separate send review. An activity screen differentiates logged notes, completed tasks, and acknowledged message events.

At **390 px**, default to a chronological next-step list. Selecting an opportunity opens a dedicated dossier route with Back to opportunities, preserving filters and position. Board mode becomes a stage selector plus its records rather than a horizontally scrolling desktop board. The composer is a full route with a visible draft status and a review step before sending.

## Interaction and states

Table sorting is explicit and exposes its current direction. Background refresh shows “Updates available” without moving focused records. Editing a commitment offers a labeled date/time input and timezone. Stage changes validate any configured prerequisite and explain missing information without silently altering a quote. Empty pipelines offer Add opportunity; empty filtered results offer Clear filters. Loading preserves dossier structure. Failed saves retain an unsaved draft; a version conflict compares the newer record with pending edits. A sent state appears only after the message service acknowledges it, with a reference or timestamp. An unknown send outcome offers status checking before retry, preventing duplicates. Opening a draft never sends outreach.

## GSAP motion choreography

| Trigger | Target | Duration / ease | Result |
| --- | --- | --- | --- |
| Select opportunity | Dossier visual wrapper | `gsap.fromTo()`, 0.23 s, `power2.out`, x 10 → 0 | Introduce context without shifting the opportunity ledger. |
| Select dossier tab | Decorative underline | `gsap.to()`, 0.2 s, `power3.out` | Follow the selection while semantic state changes immediately. |
| Save next step | Small task check | `gsap.timeline()`, 0.28 s, `back.out(1.1)` | Settle the icon in its fixed slot after acknowledgement. |
| Open follow-up draft | Composer heading only | 0.18 s opacity, `power1.out` | Identify the task without moving text fields or their caret. |

Do not animate deal values or move cards automatically after a save. Apply a changed stage immediately in detail; update filtered placement only through an explicit refresh or clear user action. No ScrollTrigger or pinned sales views.

## Signature button

Prepare follow-up is olive with an off-white label and a folded-message icon. Fine-pointer hover separates the icon's small flap by **2 px**. Press the inner face to **0.976** over **0.075 s**; return over **0.35 s** with `back.out(1.28)`. The easing creates a spring-style response, not physical simulation. Keep the outer target and 3 px ink focus ring stationary. Native keyboard activation opens the draft immediately. Reset on pointercancel, release outside, blur, and disabling. Pending preparation prevents duplicates. Reduced motion changes the fill and label instantly without flap travel or scale.

## Accessibility and performance

Use native tables and meaningful lists, labeled stage controls, and semantic tabs where implemented. Provide a button-based alternative to board dragging. Keep client information available without hover, and avoid exposing private notes in list previews by default. Announce completed user actions rather than every activity update. Defer attachment previews, scope GSAP contexts, and clean up transitions on route changes. Reduced motion keeps all content static and preserves the same review and sending flow.

## Build acceptance criteria

- Every opportunity exposes its owner, current stage, and next commitment without opening a chart.
- A keyboard user can change stages and prepare a follow-up without dragging or hovering.
- Background updates and save conflicts preserve focus, pending edits, and queue position.
- At 390 px, recipients and content can be reviewed before an explicit send; drafts never send automatically.
