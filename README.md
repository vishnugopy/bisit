# Bisit

Bisit is a portable Agent Skill for frontend design and accessibility. It helps compatible coding agents turn generic, over-styled interfaces into deliberate, accessible, and responsive experiences.

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

Invoke Bisit through your host's skill picker or command interface. In Codex CLI and the IDE extension, type `$bisit` or run `/skills` and choose Bisit. In the ChatGPT desktop app, enabled skills appear in the `/` menu. Hosts that expose skill names as direct slash commands may show `/bisit`.

```text
$bisit audit and improve this dashboard
```

Scope is automatic:

1. Selected text or code
2. Selected or attached file(s)
3. The current project's frontend when no selection or file is supplied

An explicitly named target takes priority. You can also give a narrower instruction:

```text
$bisit check this form in light and dark mode, fix its alignment, and improve its mobile layout
```

The workflow contains no Codex-specific tool dependency, so the same `SKILL.md` works with Grok or another CLI when that host supports the open Agent Skills format. Invocation syntax and editor-selection forwarding are controlled by the host.

## What it checks

- Alignment, spacing, hierarchy, and consistent layout
- Excessive borders, shadows, nested cards, gradients, and other AI-slop patterns, while preserving borders that communicate state or structure
- Decorative left borders and accents that do not communicate meaning
- Preservation of existing visible copy, labels, links, metrics, values, and data
- Consistent corner radii across related components
- WCAG 2.2 AA color contrast in light and dark modes
- Keyboard navigation, visible focus and selection states, semantics, and screen-reader support without using ARIA as a substitute for visual cues
- Responsive reflow, zoom behavior, overflow, and touch-target sizing
- Hover, active, disabled, error, loading, and reduced-motion states

Bisit preserves user-facing content and intentional brand choices by default. It removes a visual effect only when the effect adds noise rather than meaning.

## Links

- [npm package](https://www.npmjs.com/package/bisit-skill)
- [GitHub repository](https://github.com/vishnugopy/bisit)
- [skills.sh listing](https://www.skills.sh/vishnugopy/bisit/bisit)

## License

MIT
