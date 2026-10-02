---
name: bisit
description: Use only when the user explicitly invokes Bisit to audit or fix the design, layout, mobile-first responsiveness, layout shift, or accessibility (contrast, focus, keyboard and swipe support, dark mode, reflow, WCAG 2.2 AA) of selected code, selected files, or a project's HTML/CSS, React, Next.js, Vue, Svelte, or similar frontend.
---

# Bisit

Create deliberate, production-ready interfaces without generic over-styling. Use WCAG 2.2 Level AA as the baseline unless the project requires a stricter standard.

## Choose the scope

Use the narrowest available scope: a target the user names, then selected code, then selected or attached files, then the project's frontend. Treat host-provided editor context as the target without asking the user to repeat it.

- Selection: inspect only enough surrounding code to understand it, and edit the selection's file.
- Selected files: edit only those files unless a required shared dependency must change, and disclose that.
- Project: read tokens and theme first, then entry points, shared primitives, and primary screens. Skip dependencies, generated output, vendored code, and backend files. Report which screens and components were covered.

Do not scan the project when a narrower target exists.

## Work in this order

1. Inspect the target and the project's design system. Record its visible headings, copy, labels, links, values, and data.
2. Read only the references the target needs from `references/`:
   - `design.md`: hierarchy, spacing, borders, shadows, radius, decoration, brand.
   - `accessibility.md`: semantics, focus, contrast, color cues, motion.
   - `responsive.md`: mobile-first layout, reflow, touch sizing, layout shift.
   - `interaction.md`: swipe and keyboard patterns. Read it only when the target has a carousel, tabs, stepper, drawer, sheet, dialog, or menu.

   For a whole-screen or project review, read design, accessibility, and responsive. For a narrower request, read only what it names.
3. If the user asks for an audit, report findings without editing. Otherwise fix the problems in scope, starting with layout, hierarchy, states, and accessibility before cosmetic polish.
4. Verify only what you changed. With a browser, render narrow, intermediate, and wide widths in each supported theme and run the project's accessibility tooling or axe-core; otherwise say the result is a static review. Never claim visual verification without viewing the result.
5. Report scope, highest-impact changes, verification, visible-content changes, and unresolved tradeoffs. Scale the report to the scope: a few lines for a selection, a structured list for a project.

## Preserve meaning

- Keep visible copy, data, sections, information order, product behavior, brand choices, and public component APIs unless the user requests otherwise or one directly causes the problem. Fix layout to fit existing content; never shorten text or invent copy, metrics, features, calls to action, or filler.
- Add non-visible accessible names, descriptions, and state semantics when needed. Change visible wording only when requested or when accessibility cannot otherwise be solved, and disclose it.
- When a placeholder is the only label, promote its exact text, including hints such as "(8+ characters)", to a persistent label.
- Converting an element to native semantics with the same behavior (a clickable `div` to a `button` or radio, a hover-only tip to a focusable disclosure) is allowed; disclose it.
- Do not add product behavior: no validation attributes such as `required` or `minlength`, no copy that follows state, and no handlers for controls that had none. Extra input methods for an existing action follow `references/interaction.md`. Report a stale label, missing handler, or missing validation instead.

## Reuse before adding

When a fix needs a component (button, dialog, tabs, tooltip, field, icon), take the first option that works:

1. A component, primitive, or utility the project already has. Search the shared component folders and design-system imports, and match their props and conventions. Searching is read-only and does not widen the edit scope.
2. A new component from native HTML and the project's tokens, beside its siblings.
3. A package, only when native HTML cannot meet the requirement, such as a complex focus-managed widget. Prefer one already in the dependencies; otherwise add the smallest accessible option as a last resort and disclose it with the reason.

Never duplicate an existing component or add a package for something native HTML or CSS handles.

## Finish

Compare the final visible text with the copy recorded at the start and report every difference. Confirm that content and behavior are preserved and that the closing check of each reference you read holds for the scoped interface.
