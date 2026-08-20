---
name: bisit
description: Audit or refine frontend design and accessibility while preserving content, behavior, meaningful state cues, and brand choices. Use only when explicitly invoked for selected code, selected files, or a project-wide HTML/CSS, React, Next.js, Vue, Svelte, or similar interface review.
---

# Bisit

Create deliberate, production-ready interfaces without generic over-styling. Use WCAG 2.2 Level AA as the baseline unless the project requires a stricter standard.

## Choose the scope

Use the narrowest available scope in this order:

1. A target explicitly named by the user.
2. Selected text or code supplied by the host editor.
3. Selected or attached file(s).
4. The current project's frontend when none of the above is present.

For a selection, inspect only enough surrounding code and dependencies to understand it; edit the selection's file and do not broaden the change without necessity. For selected files, limit edits to those files unless a required shared dependency must change, and disclose that expansion. For project scope, inspect frontend entry points, shared primitives, tokens, and primary screens; exclude dependencies, generated output, vendored code, and unrelated backend files.

Do not scan the full project when a narrower target exists. Treat host-provided editor context as the target without asking the user to repeat it.

## Work efficiently

1. Inspect the target and its existing design system before editing. Record its visible headings, copy, labels, links, values, and data.
2. Prioritize layout, hierarchy, states, and accessibility over cosmetic polish. Reuse existing primitives and tokens.
3. If the user asks for an audit, report actionable findings without editing. If they ask to improve, fix the problems in scope.
4. Run only checks relevant to the changed scope. Combine automation with keyboard and rendered inspection when available; never claim visual verification without viewing the result.
5. Report the scope, highest-impact changes, verification, visible-content changes, and any unresolved tradeoff concisely.

## Preserve meaning

- Preserve visible copy, data, sections, information order, product behavior, information architecture, brand choices, and public component APIs unless the user requests otherwise or one directly causes the problem.
- Fix layout to support existing content; do not shorten text, delete information, or invent copy, metrics, features, calls to action, or filler.
- Add non-visible accessible names, descriptions, or state semantics when needed. Change visible wording only when requested or when accessibility cannot otherwise be solved, and disclose it.

## Design rules

- Align related content to shared edges, columns, gutters, and baselines. Prefer grid, flex, intrinsic sizing, and consistent page gutters over arbitrary margins, transforms, fixed dimensions, or breakpoint patches.
- Use the project's spacing and typography scales. Let spacing show relationships and typography, placement, whitespace, and restrained color establish hierarchy.
- Start ordinary sections, headers, navigation, and metric groups without borders or shadows. Use whitespace or a subtle surface change when separation is needed.
- Keep borders that communicate a boundary or state: inputs, tables, selection, focus, validation, warnings, and dense regions may need them. Never remove a meaningful border merely to make the interface borderless.
- If replacing a selected, active, checked, focused, or invalid border, provide an equally clear, persistent non-color cue such as shape, weight, text, or an icon. Selection must remain identifiable after focus moves away.
- Reserve shadows for real elevation such as menus, dialogs, popovers, dragged items, or sticky layers. Avoid stacking border, shadow, tint, and a large radius without a reason.
- Use a small, consistent radius scale. Keep equivalent controls consistent and nested corners visually concentric; reserve pills and circles for roles that justify the shape.
- Remove decorative accent rails, gratuitous gradients, glows, glass effects, blurred blobs, dot grids, excessive pills, nested generic cards, colored icon tiles, arbitrary fixed sizing, and template filler. Preserve an effect when it conveys status, selection, hierarchy, or brand meaning.

## Accessibility rules

- Prefer native HTML. Preserve logical headings, landmarks, visible labels, instructions, alternative text, associated errors, and name/role/value for custom controls.
- Keep every control keyboard operable in a logical order. Manage focus entry, containment, closing, and restoration for dialogs and popovers.
- Keep a clear, high-contrast `:focus-visible` indicator in every theme. It is visual feedback for all keyboard users, including sighted users, and is not decorative.
- Keep focus and selection distinct: focus is the keyboard's current position; selection is persistent state.
- ARIA supplements visual communication; it never replaces a visible label, selection cue, status, error, or instruction. Use `aria-label` only when no equivalent visible name is available, such as an icon-only control. Represent state with native semantics or the correct `aria-*` state, not by changing the accessible name.
- Measure rendered contrast: at least 4.5:1 for normal text, 3:1 for large text, and 3:1 for meaningful component boundaries, icons, and focus indicators where required. Check actual foreground/background combinations, opacity, and overlays in every supported theme.
- Never use color alone for meaning. Check default, hover, focus, active, selected, disabled, validation, placeholder, and link states. Preserve forced-colors behavior where feasible.
- Respect reduced motion. Avoid flashing and autoplay; provide controls when motion is necessary.

## Responsive rules

- Verify narrow, intermediate, and wide layouts where content breaks. Check 320 CSS-pixel reflow, 400% zoom, 200% text zoom, and increased text spacing when relevant.
- Prevent truncation, overlap, hidden controls, and two-dimensional scrolling except where the content genuinely requires it. Account for long or translated text and unbroken strings.
- Prefer fluid and intrinsic layout, wrapping, `minmax()`, `clamp()`, and `min-width: 0`. Keep required targets at least 24 by 24 CSS pixels and provide keyboard and touch equivalents for hover behavior.

## Finish

Confirm that content and behavior are preserved; hierarchy is clear; every remaining border, surface, shadow, and radius has a purpose; selected states persist; focus is visible; semantics are correct; color is not the only cue; contrast passes in supported themes; and the scoped interface reflows without lost content or functionality.
