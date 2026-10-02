# Bisit evals

A test kit for the skill. It answers one question: does an agent that follows `SKILL.md` produce better frontend edits than an agent without it? Not published to npm (`package.json` `files` whitelists only the skill files).

## Layout

- `fixtures/<name>/` – a small page (or project) with planted problems, plus `checks.json`.
- `checks.json` – regex and structural checks on the edited output, shared files that must stay unchanged, a layout-shift measurement, and a `manual` list to review by eye.
- `check.py` – scores one edited fixture: visible-text diff, checks, axe violations (light and dark, 1280 and 320 px), horizontal overflow at 320 px, and layout shift.
- `browser.py` – headless Chrome and axe-core driver. Needs Google Chrome at the macOS path in the file and `npm install` in this folder. Dark mode uses `--force-dark-mode`; `--blink-settings=preferredColorScheme=1` does not work.

```sh
cd evals && npm install
python3 check.py signup-form /path/to/edited/index.html
```

## Fixtures

| Fixture | Tests |
|---|---|
| `signup-form` | placeholder-only labels, div button, removed focus ring, unassociated error, low contrast, fixed width |
| `plan-picker` | selection by border color only, div cards, hover-only tooltip, decoration to remove, looping animation |
| `dashboard-dark` | contrast in both themes, sticky header covering focus, color-only deltas, truncated names, fixed 1200 px layout |
| `brand-landing` | brand gradient token (keep) vs one-off decoration (remove), hero reflow, heading order, missing alt |
| `mobile-first` | desktop-first CSS, zoom-blocking viewport, `100vh`, fixed bar without safe-area inset, 14 px field |
| `layout-shift` | images without dimensions, selected chip that resizes, banner inserted after load |
| `component-reuse` | a project that already ships `ui/` button and dialog; fixes should reuse them |
| `carousel-swipe` | a carousel with no swipe or arrow keys, plus a static list where nothing should be added |

## Running an arm

Copy each fixture folder (without `checks.json`) to its own directory. Give one agent per directory the same request: "Audit and improve the design and accessibility of this page. Edit it in place." The skill arm adds one line: read `SKILL.md` and follow it, then end the reply with the skill files it read. The baseline arm says not to use any skill. Never show agents `checks.json`. Run `check.py` on each result and read the diffs; pattern hits are a screen, not a verdict.

## Results

**Round 1, 2026-10-02, SKILL.md at 91bdbe7 (one 970-word file), one run per cell**

| Fixture | Checks failed (baseline / skill) |
|---|---|
| signup-form | 0 / 0 |
| plan-picker | 3 / 0 |
| dashboard-dark | 0 / 0 |
| brand-landing | 5 / 2 |

A plain agent already fixes everything axe and the overflow check can see. The skill removed decoration the baseline kept and made fewer unrequested changes, but it over-corrected on brand (recolored the logo, dropped the gradient dividers).

**Round 2, SKILL.md at d190ee1 (short core plus `references/`), one run per cell**

| Fixture | Checks failed (baseline / skill) | Note |
|---|---|---|
| signup-form | not run / 0 | |
| plan-picker | not run / 1 | kept two different gradients as a "brand pair" |
| dashboard-dark | not run / 1, then 0 / 0 on two reruns | first run left a sticky header with no `scroll-padding`; `accessibility.md` now says to add it |
| brand-landing | not run / 0 | kept the shared gradient token, used a derived token for the failing CTA |
| mobile-first | 1 / 0 | baseline had no safe-area handling |
| layout-shift | 0 / 0 | skill kept the delayed banner and reserved its space; baseline deleted the script |
| component-reuse | 0 / 1 | both reused `ui/`; skill added one disclosed line to `dialog.css` to fix a real overflow bug |
| carousel-swipe | 2 / 0 | only the skill added swipe and arrow keys |

Narrow request ("Fix the color contrast on this page") on `signup-form`: the agent read only `SKILL.md` and `accessibility.md`, fixed contrast (axe 10 to 5), and listed the other problems instead of fixing them.

Caveats: one sample per cell, so run-to-run variance is unknown. Several checks were corrected or added after seeing outputs (for example `brand-orange-kept`, `dividers-kept`, and the `unchanged` file rule, which is a judgment call). `check.py` cannot see text set by script. Agents self-report which skill files they read.
