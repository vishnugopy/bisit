# Design rules

- Align related content to shared edges, columns, gutters, and baselines. Prefer grid, flex, intrinsic sizing, and consistent page gutters over arbitrary margins, transforms, fixed dimensions, or breakpoint patches.
- Use the project's spacing and typography scales. Let spacing show relationships and typography, placement, whitespace, and restrained color establish hierarchy.
- Start ordinary sections, headers, navigation, and metric groups without borders or shadows. Use whitespace or a subtle surface change when separation is needed.
- Keep borders that communicate a boundary or state: inputs, tables, selection, focus, validation, warnings, and dense regions may need them. Never remove a meaningful border merely to make the interface borderless.
- If replacing a selected, active, checked, focused, or invalid border, provide an equally clear, persistent non-color cue such as shape, weight, text, or an icon. Selection must remain identifiable after focus moves away.
- Reserve shadows for real elevation such as menus, dialogs, popovers, dragged items, or sticky layers. Avoid stacking border, shadow, tint, and a large radius without a reason.
- Use a small, consistent radius scale. Keep equivalent controls consistent and nested corners visually concentric; reserve pills and circles for roles that justify the shape.
- Remove decorative accent rails, gratuitous gradients, glows, glass effects, blurred blobs, dot grids, excessive pills, nested generic cards, colored icon tiles, arbitrary fixed sizing, and template filler. Preserve an effect when it conveys status, selection, hierarchy, or brand meaning.
- Treat a color, gradient, or effect as brand when it is a shared token or appears on three or more elements, such as the logo, the primary action, and dividers; keep it. Treat an effect on a single component as decoration.

Done when: hierarchy is clear, every remaining border, surface, shadow, and radius has a purpose, selected states persist, and brand effects are intact.
