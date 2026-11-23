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

## Color is reserved for action

- Keep text and surfaces neutral by default. Spend solid brand color on the screen's main action and on what reflects it, such as a progress meter; one solid action per region.
- Show states with the project's status tokens on a small carrier: a tinted badge, a dot, or an icon. Never color a whole background, row, or card, and never use a gradient, to say a status. Highlight a row discreetly.
- Show selection with a light tint of the brand color plus a non-color cue, never the solid action color, so selection does not read as the primary action.
- Report a main button whose label does not name its action or its value ("Continue" where it charges $79.00 is better as "Charge $79.00"); this changes copy, so do not rewrite it unasked.

## Same size, same rhythm

- Give controls placed side by side one shared height from a single size scale: buttons, inputs, selects, date pickers, and segmented controls in a row match. Do not pick sizes one by one.
- Give icons in a group one size, matched to the control size, and keep icon stroke weight consistent.
- Give rows and cards in one list the same padding, radius, and gap.
- Keep a control's width fixed across states: a button entering its loading state, or a label turning bold when selected, reserves that width in advance.
- Before choosing spacing, type size, or control size, read the neighbouring screen or component and copy its scale and variants. When two disagree, follow the shared primitive's default.
- Put short related fields on one line (a note and its date) and long fields on their own lines (an amount, then a recipient).
- Use the same icon for the same action everywhere in the scope; report a mismatch with other screens.

## Charts and gauges tell the truth

- Keep proportions exact: a value of zero takes no space, and no minimum-width segment, label, or legend crowds the real data.
- Keep labels off the data they describe. If a label does not fit, move it outside or into a tooltip.
- Make a visualization readable on its own: units, the total it is measured against, and visible values, not color alone.
- Keep the key figure a screen is about, such as an amount due, visible at every step of a flow instead of only on the first.

## Dark mode as elevation

- Build dark surfaces as a ladder: page darkest, then panel, card, nested block, each raised layer slightly lighter. Elevation in dark mode is a lighter surface, not a shadow or a border.
- Keep dark greys neutral unless the brand defines tinted ones; do not introduce blue or purple casts.
- Use status tokens tuned for each theme: deeper shades (around the 700 step) for status text on light surfaces, lighter tuned tokens on dark ones, and verify each pair for contrast.

Done when: hierarchy is clear, every remaining border, surface, shadow, and radius has a purpose, selected states persist, brand effects are intact, solid color belongs to the main action, sibling controls share one size, visualizations are proportional, and dark surfaces rise in steps.
