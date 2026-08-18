---
name: bisit
description: Frontend design and accessibility review that removes gratuitous borders, shadows, accent rails, card nesting, and other templated AI-generated styling while correcting alignment, spacing, hierarchy, color contrast, light and dark themes, keyboard behavior, semantics, and responsive reflow. Use only when explicitly invoked with $bisit to audit, refine, or build accessible web interfaces in HTML/CSS, React, Next.js, Vue, Svelte, or similar frontend projects.
---

# Bisit

Create deliberate, production-ready interfaces that feel designed for their content rather than assembled from generic UI effects.

## Run the workflow

1. Inspect the frontend structure, existing design system, shared components, tokens, and the requested screen before editing.
2. Preserve product behavior, brand choices, and established component APIs unless they cause the design problem.
3. Audit the interface against the rules below. Prioritize structural problems over cosmetic polishing.
4. For an implementation request, make focused code changes and reuse existing primitives. For a review-only request, report findings without editing.
5. Use WCAG 2.2 Level AA as the accessibility baseline unless the project specifies a newer or stricter standard.
6. Verify relevant tests, linting, responsive behavior, themes, and interaction states when the project supports them. Combine automated checks with manual inspection; never claim accessibility from an automated score alone.
7. Never claim visual verification without inspecting a rendered result or screenshot.

When invoked without a target, inspect the current frontend and improve the primary visible surface or shared layout. Avoid an unbounded redesign; state the scope chosen.

## Fix layout and alignment first

- Align related content to shared edges, columns, gutters, and text baselines.
- Use grid or flex layout instead of compensating with arbitrary margins, transforms, or absolute positioning.
- Keep repeated components equal where equality communicates structure; let content determine size where it does not.
- Correct icon and control alignment optically when geometric centering looks wrong.
- Maintain a clear container strategy and consistent page gutters across breakpoints.
- Remove accidental width changes, uneven columns, orphaned elements, and controls that drift from their labels or content.

## Use disciplined spacing and hierarchy

- Reuse the project's spacing scale. Consolidate near-duplicate values instead of introducing arbitrary gaps.
- Make spacing reflect relationships: tight within a group, larger between groups, and largest between page sections.
- Establish hierarchy with typography, placement, whitespace, and restrained color before adding containers or effects.
- Keep headings, labels, body text, and actions consistent across equivalent sections.
- Avoid oversized headings, excessive empty hero space, and tiny uppercase eyebrow labels used only to imitate a template.

## Restrain borders, shadows, and surfaces

- Start with no border and no shadow. Add one only when it communicates a necessary boundary, state, or layer.
- Prefer whitespace, alignment, typography, or a subtle background shift to separate ordinary sections.
- Do not wrap every section in a card. Remove nested cards and repeated rounded rectangles when page structure already provides grouping.
- Use borders for inputs, tables, dividers, selection, validation, or dense content only when the boundary improves comprehension.
- Use shadows primarily for genuine elevation such as menus, popovers, dialogs, and dragged or sticky elements. Keep the shadow scale subtle and consistent.
- Avoid combining a border, shadow, tinted background, and large radius on the same surface without a concrete reason.

## Keep corner radii visually consistent

- Reuse a small radius scale from the project's tokens. Consolidate accidental one-off values such as several nearly identical radii.
- Give components with the same role, size, and visual weight the same radius. Keep equivalent buttons, inputs, cards, dialogs, and menus consistent across screens and states.
- Match adjacent controls of equal height unless a different shape communicates a meaningful distinction.
- Make nested corners visually concentric. Account for the gap or padding between an outer surface and its inner element instead of applying the same numeric radius blindly.
- Reduce the radius as component size decreases. Reserve fully rounded pills for tags, compact filters, statuses, or controls whose shape has a purpose.
- Preserve intentional exceptions such as circular avatars, icon buttons, segmented-control ends, sheets, or brand-specific shapes.
- Judge optical consistency in the rendered interface, not only equality of CSS values.

## Remove AI-slop patterns

- Remove decorative thick left borders, accent rails, and `border-left` stripes unless they encode a real status, selection, timeline, quote, or warning.
- Remove gratuitous gradients, glows, glass effects, blurred color blobs, dot grids, and decorative background noise.
- Avoid excessive pills, oversized corner radii, and icons placed in colored rounded squares by default.
- Replace repeated generic cards with a layout shaped by the actual content and user task.
- Avoid arbitrary fixed widths and heights added only to make a composition look balanced at one viewport.
- Do not add badges, metrics, callouts, side panels, or placeholder marketing copy merely to fill space.
- Avoid identical landing-page formulas when the product calls for a simpler or more task-focused structure.

## Validate colors and themes

- Measure contrast using the rendered foreground and background colors, including opacity and overlays; do not judge contrast by eye.
- Require at least 4.5:1 contrast for normal text, 3:1 for large text, and 3:1 for meaningful UI component boundaries, icons, charts, and focus indicators where WCAG requires it.
- Check default, hover, focus, active, selected, disabled, error, success, warning, placeholder, and link states. Do not allow interaction to reduce readable contrast.
- Never use color as the only signal. Pair status and validation colors with text, an icon, a pattern, or another persistent visual cue.
- Test every semantic color token against its actual surface in both light and dark modes. Do not assume reversing a palette preserves contrast or hierarchy.
- Check elevated surfaces, overlays, menus, dialogs, tooltips, code blocks, charts, illustrations, and third-party widgets in both themes.
- Support the system color preference when appropriate and keep a user-selected theme stable. Give any theme control an accessible name and programmatic state.
- Use `color-scheme` for compatible native controls when appropriate. Check browser autofill, form controls, scrollbars, selection colors, and focus indicators in each theme.
- Check forced-colors or high-contrast mode when feasible. Avoid CSS that suppresses user-agent accessibility adjustments without an equivalent.

## Preserve keyboard and screen-reader access

- Prefer native semantic elements. Add ARIA only when native HTML cannot express the required behavior.
- Keep a logical heading structure, landmarks, labels, accessible names, instructions, alternative text, and programmatically associated errors.
- Make every interactive element keyboard operable in a logical order without traps. Manage initial focus, containment, closing, and focus restoration for dialogs and popovers.
- Keep a clearly visible `:focus-visible` indicator with sufficient contrast in light and dark modes. Never remove an outline without providing an equally clear replacement.
- Preserve skip navigation, live-region announcements, expanded and selected states, and name/role/value for custom controls where relevant.
- Do not remove boundaries users need to recognize inputs, tables, selected states, errors, focus, or interactive regions.

## Test responsive behavior and reflow

- Test narrow mobile, intermediate, and wide layouts based on where content actually breaks, not only popular device presets.
- Verify reflow at 320 CSS pixels and at 400% zoom without loss of content, functionality, or two-dimensional scrolling, except for content such as data tables or diagrams that genuinely requires two dimensions.
- Verify text at 200% zoom and with increased line, paragraph, word, and letter spacing. Prevent truncation, overlap, hidden controls, and loss of functionality.
- Prefer fluid sizing, intrinsic layout, wrapping, `minmax()`, `clamp()`, and `min-width: 0` over fixed dimensions and breakpoint patches.
- Test long titles, translated copy, validation messages, empty results, dense data, user-generated content, and unbroken strings.
- Keep controls at least 24 by 24 CSS pixels where the WCAG target-size requirement applies, with adequate spacing; aim larger for primary touch actions.
- Ensure hover behavior has keyboard and touch equivalents. Do not hide essential actions behind hover alone.
- Support both orientations unless one orientation is essential. Keep sticky elements, virtual keyboards, safe areas, and zoom from obscuring content or focus.

## Check remaining accessibility risks

- Check empty, loading, error, success, timeout, offline, hover, focus, active, disabled, overflow, and destructive-action states relevant to the UI.
- Respect reduced-motion preferences. Avoid autoplay, flashing, parallax, and nonessential animation; provide controls when moving content cannot be avoided.
- Keep readable line lengths, scalable text, clear language, descriptive link text, and consistent navigation.
- Make responsive images and media preserve meaning. Provide alternatives, captions, transcripts, and controls when the content requires them.
- Treat automated accessibility tools as coverage aids. Manually test keyboard flow, focus visibility, zoom/reflow, theme contrast, and core screen-reader semantics.

## Finish with a design check

Confirm that:

- Major edges and baselines align.
- Spacing follows a small, consistent scale.
- Visual hierarchy remains clear without decorative effects.
- Every remaining border and shadow has a specific purpose.
- Equivalent components use a consistent radius scale, and nested corners appear concentric.
- Repeated elements are consistent without making the page monotonous.
- Text and meaningful non-text elements meet contrast requirements in light and dark modes.
- Meaning is never communicated by color alone.
- The core workflow is usable by keyboard with visible focus and correct semantics.
- The interface reflows at 320 CSS pixels, survives zoom and text spacing, and works across relevant breakpoints and interaction states.
- The result still belongs to the existing product.

Summarize the scope, the highest-impact changes, and the verification performed. Mention unresolved subjective tradeoffs briefly instead of presenting them as defects.
