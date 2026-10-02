# Accessibility rules

- Prefer native HTML. Preserve logical headings, landmarks, visible labels, instructions, alternative text, associated errors, and name/role/value for custom controls.
- Keep every control keyboard operable in a logical order. Manage focus entry, containment, closing, and restoration for dialogs and popovers.
- Keep a clear, high-contrast `:focus-visible` indicator in every theme. It is visual feedback for all keyboard users, including sighted users, and is not decorative.
- Keep focused elements clear of sticky and fixed bars: set `scroll-padding` or `scroll-margin` equal to the bar's height.
- Keep focus and selection distinct: focus is the keyboard's current position; selection is persistent state.
- ARIA supplements visual communication; it never replaces a visible label, selection cue, status, error, or instruction. Use `aria-label` only when no equivalent visible name is available, such as an icon-only control. Represent state with native semantics or the correct `aria-*` state, not by changing the accessible name.
- Measure rendered contrast: at least 4.5:1 for normal text, 3:1 for large text, and 3:1 for meaningful component boundaries, icons, and focus indicators where required. Check actual foreground/background combinations, opacity, and overlays in every supported theme.
- When a brand color fails contrast on one element, fix that element with a derived token or a darker gradient end. Leave the shared token and every element that passes unchanged; logotypes are exempt from contrast.
- Never use color alone for meaning. Check default, hover, focus, active, selected, disabled, validation, loading, empty, placeholder, and link states. Preserve forced-colors behavior where feasible.
- Respect reduced motion. Avoid flashing and autoplay; provide controls when motion is necessary.

Done when: focus is visible and never hidden behind a bar, semantics are correct, color is not the only cue, and contrast passes in every supported theme.
