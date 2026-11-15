# Relay — A Developer Workspace With a Human Rhythm

An API documentation and request sandbox that feels like a well-organized instrument panel: persistent context, readable examples, and satisfying microfeedback. Relay and all endpoints are fictional.

## Product and core flow

For developers evaluating an integration and testing an example without losing their place. The primary task is finding an endpoint and understanding its request and response.

Flow: choose a resource → read its purpose and permissions → edit a local sample request → run the mock → inspect the response → copy the example. Example route: `POST /v1/collections`. Sample copy: “Run mock request” and “This sandbox uses sample data and sends no network request.” Use a reserved example host such as `https://api.example.com` in code samples.

Keep a visible distinction between documentation, simulated output, and any future authenticated production console.

## Visual system

- Canvas `#12181C`; raised panel `#1C272D`; text `#F3F7F4`; secondary text `#B2C2BC`; mint action `#7DE5BC` with dark text `#10251C`; divider `#3D5057`; error text `#FFB4AA`.
- IBM Plex Sans with Arial/sans-serif fallback; IBM Plex Mono with Consolas/monospace fallback for code, statuses, and endpoint paths.
- Desktop: 38/44 px endpoint title, 18/28 lead, 15/24 body, 13/21 code. Mobile: 30/36 title, 16/25 body, 13/21 code.
- Use 4 px subdivisions within an 8 px spacing grid. Panels have 8 px corners; action buttons have 6 px corners. Avoid glow, blurred surfaces, and faux-terminal decoration.

## Screen composition

At 1440 px, use a 240 px left resource navigation, a flexible article column, and a 420 px request workspace. A 64 px top bar contains product identity, version selector, and a labeled search control. The first screen shows an endpoint summary, permission notes, request fields, and Run mock request together.

The article contains field descriptions, examples, and clearly separated error cases. The workspace has Request and Response tabs, language selection, copy controls, and a stable output area. A compact “On this page” list belongs inside the article, not as a fourth column. Search results show endpoint names and matching snippets.

At 390 px, replace resource navigation with a labeled drawer and render the sandbox inline immediately after the request schema. Tabs stay in normal document flow. Code blocks may scroll horizontally within themselves; the page may not. Keep copy buttons outside the code's horizontal scroll area.

## Interaction and states

Search is a combobox only if its full keyboard pattern is implemented; otherwise use a simple search form and results list. A mock response displays “Simulated response,” elapsed sample time, and explicit success or error text. Disable Run only while its local simulation is running. Retain the editor contents after errors. Copy success uses a polite status region; copy failure offers selection instructions. An empty response says “Run a mock to inspect its shape,” never a fake spinner. Version changes preserve a valid endpoint or explain the nearest destination.

## GSAP motion choreography

| Trigger | Target | Timing and API | Intended result |
| --- | --- | --- | --- |
| Endpoint navigation | Incoming article section | `gsap.fromTo()`, y 8 → 0, 0.22 s, `power2.out` | Small contextual transition without delaying routing. |
| Tab selection | Decorative active underline | `gsap.to()`, 0.24 s, `power3.out` | Follow the selected tab; content and ARIA state update immediately. |
| Copy succeeds | Copy icon wrapper | 0.16 s fade out, swap icon, 0.18 s fade in | Clear acknowledgement without moving the code. |
| Mock completes | Response header only | Opacity 0.65 → 1, 0.2 s, `power1.out` | Mark new output without bouncing response text. |

Do not use ScrollTrigger or pinning in this tool. Keep editor caret, scrolling, and output stable. All motion can be removed without changing functionality.

## Signature button

Run mock request is a mint button with a dark outlined play glyph and a small “Mock” label. Animate its inner face to scale 0.974 over 0.08 s on press and back to 1 over 0.36 s with `back.out(1.6)` on release. This is spring-style overshoot, not a physics solver. Fine-pointer hover shifts the glyph 2 px right; touch has no hover dependency. A 3 px off-white focus ring stays on the outer button. Restore the face after pointer cancellation, lost focus, or disabling. The click runs immediately. Reduced motion uses only an instant fill change and static pending label.

## Accessibility and performance

Provide a skip link, labeled request fields, readable syntax colors, and a plain-text copy path. Preserve tab focus through output updates. Avoid announcing the entire response automatically; announce only completion. Never place secrets in initial examples. Load the syntax highlighter on demand and reuse a single GSAP context per mounted page, reverting it on unmount. Under reduced motion, remove position and overshoot effects while retaining selected indicators and status text.

## Build acceptance criteria

- A first-time reader can run and copy a labeled mock without an account or a real API key.
- Keyboard navigation reaches search, resource navigation, editor controls, tabs, and response actions in a sensible order.
- At 390 px, only code blocks have horizontal overflow and the copy action remains visible.
- Endpoint changes and reduced-motion mode leave no hidden article content, stale timelines, or shifted editor focus.
