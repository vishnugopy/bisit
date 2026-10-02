# Responsive and layout stability

## Mobile-first layout

- Design the narrowest layout first: single column in source order, base styles for small screens, and `min-width` media or container queries that add columns and spacing where the content needs them. Take breakpoints from where the content breaks, reusing the project's existing ones.
- Write the rules you edit mobile-first. Convert an existing desktop-first `max-width` override only inside rules you are already changing; report the remaining desktop-first patterns instead of rewriting the stylesheet.
- Keep `<meta name="viewport" content="width=device-width, initial-scale=1">`. Remove `user-scalable=no` and any `maximum-scale` below 5, and do not lock orientation.
- Verify narrow, intermediate, and wide layouts, starting at 320 CSS pixels. Check 400% zoom, 200% text zoom, and increased text spacing when relevant.
- Prevent truncation, overlap, hidden controls, and two-dimensional scrolling except where the content genuinely requires it. Account for long or translated text and unbroken strings.
- Prefer fluid and intrinsic layout, wrapping, `minmax()`, `clamp()`, and `min-width: 0`. Provide keyboard and touch equivalents for hover behavior.
- Size primary touch controls at least 44 by 44 CSS pixels where space allows; 24 by 24 is the floor. Keep text fields at 16px or larger so mobile browsers do not zoom on focus. Offset fixed and sticky bars with `env(safe-area-inset-*)` and use `dvh` rather than `vh` for full-height sections.

## Layout stability

- Reserve space before content arrives: give images, video, iframes, and embeds `width` and `height` or `aspect-ratio`, and give loading, async, and lazy regions a placeholder of their final size.
- Keep border width, padding, and font weight constant between states. Show selection, focus, and validation with `outline`, `box-shadow`, or an always-present transparent border. Reserve the slot for banners and messages instead of inserting them above existing content.
- Animate `transform` and `opacity`, not `width`, `height`, `top`, or `margin`.
- Prevent font-swap reflow with a metric-matched fallback, and use `scrollbar-gutter: stable` where a scrollbar appears and disappears.

Done when: the scoped interface reflows from 320 CSS pixels up without lost content or functionality, and layout does not shift between states or while content loads.
