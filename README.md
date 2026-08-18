# Bisit

Bisit is an opinionated frontend design and accessibility skill for AI coding agents. It helps turn generic, over-styled interfaces into deliberate, accessible, and responsive experiences.

## Install

Install directly from the public skill repository:

```sh
npx skills add vishnugopy/bisit --skill bisit
```

Or install the npm package first:

```sh
npm install --save-dev bisit-skill
npx skills add ./node_modules/bisit-skill --skill bisit
```

## Use

Invoke the skill explicitly with `$bisit` in Codex:

```text
$bisit audit and improve this dashboard
```

You can give it a narrower task too:

```text
$bisit check this form in light and dark mode, fix its alignment, and improve its mobile layout
```

The exact invocation syntax may differ in other compatible agents.

## What it checks

- Alignment, spacing, hierarchy, and consistent layout
- Excessive borders, shadows, nested cards, gradients, and other AI-slop patterns
- Decorative left borders and accents that do not communicate meaning
- Preservation of existing visible copy, labels, links, metrics, values, and data
- Consistent corner radii across related components
- WCAG 2.2 AA color contrast in light and dark modes
- Keyboard navigation, focus states, semantics, and screen-reader support
- Responsive reflow, zoom behavior, overflow, and touch-target sizing
- Hover, active, disabled, error, loading, and reduced-motion states

Bisit preserves user-facing content and intentional brand choices by default. It removes a visual effect only when the effect adds noise rather than meaning.

## Links

- [npm package](https://www.npmjs.com/package/bisit-skill)
- [GitHub repository](https://github.com/vishnugopy/bisit)
- [skills.sh listing](https://www.skills.sh/vishnugopy/bisit/bisit)

## License

MIT
