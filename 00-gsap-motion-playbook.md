# Shared GSAP Motion Playbook

Use this alongside any of the 36 design briefs. It defines practical behavior for motion, spring-style buttons, and graceful fallbacks. The individual brief supplies the final timing and visual character.

## Motion has a job

Use animation to establish hierarchy, connect a selection to its details, explain a mechanism, or acknowledge an action. Give each screen one signature interaction and a small supporting vocabulary. Operational interfaces need stable information; editorial pages can carry more expressive transitions.

| Purpose | Typical range | Starting ease | Boundary |
| --- | --- | --- | --- |
| Press feedback | 0.07–0.12 s | `power2.out` | Animate a visual face, not the hit area. |
| Spring-style release | 0.32–0.56 s | `back.out(1.4)` | Small overshoot, with space reserved around the face. |
| Soft elastic accent | 0.4–0.55 s | `elastic.out(1, 0.55)` | Reserve for playful icons or small controls. |
| Detail or panel change | 0.18–0.3 s | `power2.out` | State changes immediately; motion is supporting feedback. |
| Editorial entrance | 0.45–0.8 s | `power3.out` | A single short sequence, never an intro gate. |
| Selection indicator | 0.16–0.25 s | `power3.out` | Move decoration while preserving readable content. |

`back.out(...)` and `elastic.out(...)` produce spring-style easing curves. They do not implement a physical spring with mass, stiffness, damping, or velocity continuity. If a project requires actual physics, specify that separately rather than describing easing parameters as physics values.

## A springy button that stays usable

Keep the real button's bounds, focus ring, and text accessible while an inner visual face animates. A typical structure is:

```html
<button class="spring-button" type="button">
  <span class="spring-button__face" data-spring-face>
    <span>Review selection</span>
    <svg aria-hidden="true" focusable="false"><!-- arrow --></svg>
  </span>
</button>
```

Use an anchor instead when the action navigates. Choose `type="submit"` only for the intended form submission. Give the outer control at least a 44 × 44 px target, preferably 48 px high. Put the visible fill on the inner face and the focus outline on the stable outer element. The face needs an appropriate display mode such as `inline-flex` for transforms.

These are motion primitives, not a complete event handler. Apply the specific scale, duration, and easing from the chosen brief:

```js
// `gsap` is imported and `face` references the visual child.
function pressFace() {
  gsap.to(face, {
    scale: 0.96,
    duration: 0.09,
    ease: "power2.out",
    overwrite: "auto"
  });
}

function releaseFace() {
  gsap.to(face, {
    scale: 1,
    duration: 0.44,
    ease: "back.out(1.5)",
    overwrite: "auto"
  });
}
```

Connect these primitives deliberately:

1. On a primary pointer press, compress the face if the control is enabled. Restore it on pointerup, pointercancel, and leaving while pressed. Ensure a release outside the control cannot leave it compressed.
2. Give keyboard activation equivalent visual feedback. Native buttons use Space and Enter; links use Enter. Ignore repeat events for decorative motion and preserve native activation behavior.
3. Restore the face on blur, disabling, route change, or interrupted interaction. Ignore new press effects on disabled controls.
4. Start the real action on native activation. Never delay navigation, submission, or state updates until a tween completes.
5. Use hover movement only inside `(hover: hover) and (pointer: fine)`. Keep offsets small, normally 2–4 px, and retain a large stationary hit area.
6. With reduced motion, skip scaling, overshoot, and travel; provide an instant fill, border, icon, or label change.

Do not replace a focus outline with a shadow animation. Keep pending and disabled states visually distinct, and communicate pending/success/error through text as well as icons. Let the product determine whether a pending action should disable the control or use `aria-disabled` with explicit event guarding; prevent duplicate work either way.

## GSAP implementation pattern

Use `gsap.timeline()` for a short coordinated sequence and `gsap.to()`/`gsap.fromTo()` for local changes. Register `ScrollTrigger` only when the brief calls for scroll-linked behavior. In React or another component system, scope selectors to the component and create a clear teardown path.

- Use `gsap.matchMedia()` for responsive motion and `prefers-reduced-motion`. Revert it on teardown; handle a preference change while the page is open.
- Use `gsap.context()` to scope and revert animations. Tweens created in later event handlers also need to be captured in that context or explicitly killed and cleaned up. Merely creating a context around mounting does not automatically manage every future handler.
- Remove event listeners and observers on teardown. Kill temporary tweens and remove only the ScrollTriggers owned by that component; avoid globally destroying unrelated animation.
- Use `overwrite: "auto"` for repeated hover/press targets so rapid input does not queue a long animation backlog. Separate DOM wrappers if two effects need independent transforms.
- Use `gsap.quickTo()` only for repeated interpolated pointer movement when it serves the design. It is optional; magnetic cursors are not a required feature.
- If a timeline is interrupted, reconcile it with the current UI state. An old animation must not restore a previous selection or success message.

GSAP core handles the ease examples in this collection. ScrollTrigger is an additional plugin used only by the applicable editorial reveals; the briefs do not require a custom spring plugin.

## Editorial scrolling

The browser owns scrolling. Use normal anchors, respect sticky headers with `scroll-margin-top`, and avoid scroll interception. For simple entrances, create ScrollTriggers that run once near viewport entry. Animate a visual wrapper while leaving headings and controls available.

Keep the CSS baseline visible: no global `opacity: 0` on all content while waiting for JavaScript. Initialize motion only after the target exists. If animation fails to initialize, the document should already be complete. Under reduced motion, use the final composition immediately and remove spatial movement, scrubbing, pinning, and decorative loops.

Reserve image space before layout. If loaded fonts or media change geometry, refresh the relevant ScrollTrigger measurements after layout settles. Avoid unnecessary refresh loops and repeated measurements during pointer movement. Never pin operational dashboards or scrub live data against scroll position.

## Data and product interfaces

Selection, text, ARIA state, and data updates should change immediately. A moving underline or icon can follow; it must not determine the actual state.

Do not bounce values, count evidence metrics up from zero, automatically reorder a focused row, or make live status blink. Preserve the user's selection and scroll position during refresh. Indicate updates through timestamped text, deliberate status labels, and a polite live region only where useful. Keep loading placeholders dimensionally stable. Never show success before the underlying action is confirmed.

## Business, corporate, and public-service systems

The sector briefs use motion to clarify a task and acknowledge user input. Keep the official-looking identity, current record, primary action, and service status readable from the first frame. Example government branding must remain visibly fictional; production identity comes from the organization.

For repeated staff tasks, use the brief's restrained press/release values and animate an inner face or a small icon. A spring-style review button can feel responsive while the decision summary, amounts, selected records, and focus ring remain still. Show important transaction details in a persistent review screen. Never make a consequential action depend on completing a visual sequence.

Separate local feedback from saved state. A pressed button can respond immediately, but “Application submitted,” “Approved,” “Order placed,” or “Stock updated” needs an acknowledged result from the relevant system. Pending, failed, stale, offline, and conflicting records require readable labels and a path forward. Preserve entered information when an action fails.

Citizen portals need direct language, an accessible alternative to maps and charts, and a complete path on slower devices. Staff workspaces need a stable queue, predictable focus, and clearly scoped actions. Corporate document centers need visible publication dates and versions. The interface should still communicate all of these details with reduced motion enabled and without loading decorative assets.

## Performance and accessibility checks

- Prefer transforms and opacity. Small illustrations can use other properties when profiled, but avoid animating large blur/filter layers or page-wide layout continuously.
- Keep motion on a small number of targets; avoid hundreds of independent text-character tweens. Never split a heading in a way that damages its accessible name or selection.
- Use `will-change` sparingly and remove it when no longer needed. Do not promote every item to a persistent compositing layer.
- Provide the complete keyboard and touch path. No action may require hover, drag precision, custom cursors, or an animated target that moves away from the pointer.
- Test rapid press/release, press then leave, cancellation, keyboard activation, focus loss, pending state, route teardown, and changing reduced-motion preferences.
- Check the brief at 1440 px and 390 px, then at intermediate widths and with 200% text zoom. Essential controls, content, and focus outlines must remain visible.
- Check a slow asset load and an animation initialization failure. The user must still be able to read, navigate, and complete the core task.

Use these checks as implementation guidance. The Markdown collection itself does not install GSAP, ship a UI, or claim browser performance results.
