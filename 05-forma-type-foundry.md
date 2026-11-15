# Forma Type Foundry — A specimen that becomes the storefront

A fictional independent type foundry where visitors test letterforms in context, compare styles deliberately, and purchase the right license through a clear editorial interface.

## Product and core flow

Serve designers choosing a family and buyers who need to understand its permitted use. The central flow is **explore a family → type a custom specimen → compare weights and glyphs → select a license scope → review the order**. Keep testing and purchasing connected without forcing purchase prompts into every interaction.

Use fictional family names and descriptive copy: “Forma Axis / A compact grotesk with open counters,” “Try a headline,” and “License scope: choose how the fonts will be used.” Font rights, pricing, and available character coverage must come from the real product catalog. Demonstration licenses are explicitly labeled sample and are not legal advice. Never show a “Complete coverage” claim based solely on a display preview.

## Visual system

- **Palette:** near-white `#F7F7F2` canvas, black olive `#20231F` primary text, muted ink `#5C6359` secondary text, electric violet `#5633C7` actions and active controls, pale lilac `#ECE6FF` selected comparison areas. Acid yellow `#E3EF73` appears only as a decorative specimen sheet.
- **Type:** Space Grotesk with Arial fallback for the interface; a fictional specimen font is represented by an explicitly named placeholder until licensed assets exist. Interface title 38/44px desktop and 28/34px mobile. Specimen text scales from 40px to 160px within bounded controls. Body is 16/25px.
- **Layout:** 48px desktop margins, 20px gutters, a 12-column grid; 16px mobile margins. Spacing: 4, 8, 16, 24, 48, 80px. Controls use 4px radii; specimen panels have square corners and firm 1px dividers.

## Screen composition

At 1440px, the first screen is dominated by an editable two-line specimen occupying eight columns, with a four-column control rail for size, weight, width, and sample text. The family name, version, and catalog navigation sit in a compact top band. A bottom specimen index links to “In use,” “Glyphs,” “Styles,” and “License.” Avoid a generic marketing headline above the useful tool.

The “In use” section contains a poster, a dense table, and a long-form paragraph to expose actual typographic behavior. The glyph screen uses labeled character groups and a searchable grid. Style comparison aligns the same phrase in chosen weights. The purchase route shows catalog-sourced license details, selected scope, files, price, and terms before checkout.

At 390px, the editable specimen occupies the full width above a collapsible control tray. Numeric inputs accompany sliders. Comparison becomes stacked, preserving the same text and baseline reference. Glyph groups become disclosures, with search always available. Checkout becomes one column with a visible order summary above the final action. Long text wraps safely; the specimen never widens the page.

## Interaction and states

Use a labeled textarea for custom text, not an unlabeled contenteditable block. Sliders support arrow keys and have synchronized numeric inputs. Keep edits when changing specimen mode. A missing font file displays the fallback and “Preview font unavailable,” without pretending it is the chosen family. Empty custom text restores a clear placeholder rather than a blank panel. Unsupported characters receive a visible coverage notice. Cart errors preserve selections; payment remains an external or implemented transaction step, never a fake success state.

## GSAP motion choreography

| Trigger | Target | Duration / ease | Intended result |
|---|---|---|---|
| Open a family | Specimen frame | `gsap.timeline()`, 0.5s, `power3.out` | Expand a decorative border while editable text remains immediately usable. |
| Switch specimen mode | Mode indicator | `gsap.to()`, 0.2s, `power2.out` | Slide a small indicator under the selected tab. |
| Enter in-use section | Poster annotation | `ScrollTrigger`, 0.38s, `power2.out` | Reveal a 10px margin note once. |
| Add selected license | Cart count marker | `gsap.fromTo()`, 0.32s, `back.out(1.4)` | Brief scale emphasis after the cart update succeeds. |

Do not tween variable-font axes while the user types or drags a control. Input response is direct, preventing lag and motion distraction.

## Signature button

“Add selected license” uses a squared violet surface and a plus icon whose horizontal arm advances 4px on fine-pointer hover. Press scales the visual surface to `0.972` in 0.07s; release uses `back.out(1.8)` over 0.36s. This spring-style overshoot uses an easing curve. Keep its 50px outer target and label fixed. A 3px black-olive focus ring surrounds the control; pending updates show “Adding…” and prevent duplicate requests. Reduced motion uses an immediate color change and updated text.

## Accessibility and performance

Keep interface fonts separate from preview fonts. Load only requested specimen assets and provide stable fallback metrics where practical. Use `gsap.matchMedia()` to remove motion for reduced-motion preferences and revert animation contexts on cleanup. All glyph details must be available as text, with meaningful accessible names. Avoid scroll hijacking, animated cursor replacements, and autoplay specimen loops.

## Build acceptance criteria

1. Custom text survives changing tabs, sizes, and style comparisons.
2. Every slider has a keyboard-operable numeric alternative.
3. Missing preview assets are labeled and never represented as the intended font.
4. Order review exposes selected scope, actual catalog price, and applicable terms before checkout.
