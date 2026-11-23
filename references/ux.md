# Truthful, direct screens

Apply this to a whole-screen or project review, or when the target's copy, statuses, or choice of controls is in question. Most items here change visible copy or behavior, so they follow the preserve-meaning rules: fix only what keeps the same options, data, and actions; report the rest with the exact text and the proposed wording.

## The screen says only what is true

For every text, badge, color, and gauge in scope, ask: is this true at this moment?

- A status appears only once reached. "Paid", "Sent", "Done", or a green check before anything is saved or confirmed is false; report it with the condition that should gate it.
- Close states get distinct words: "charged", "settled", and "received but not deposited" are different facts. Report one word used for two states.
- A label names what this window actually does: "to save" where the user saves, "to convert" where the user converts. A shared component should take its labels from each caller; report a default label leaking into a screen that does something else.
- Each fact is said in one place. Several messages that repeat or contradict each other create doubt; report the duplicates and name the one to keep.
- A message that can only be false, or that no state can make true, should be removed; report it.
- Do not let the interface decide for the user: report a prefilled value that one click would commit (an amount defaulted to the total due). A default is fine when it saves a click and commits nothing; a shortcut button ("Pay the rest") is better than a prefilled field.

## Choose the control for the number of options

| Situation | Control |
|---|---|
| 2 to 4 options | All options visible as radio tiles or buttons of one size, ideally with an icon |
| Many options | A select or combobox with search |
| Two mutually exclusive modes | A segmented control or a two-option radio group, not two stacked blocks |
| Several entries of the same kind | Rows added one at a time with a running summary, saying clearly that more can be added |
| Detail that does not fit | A tooltip or disclosure that also works on focus and touch |
| Long input beside the page | A side panel rather than a centered modal |

- Fix a control mismatch when the swap keeps the same options, values, and handler (a three-option select into a radio group). Otherwise report it.
- Flatten nesting: a menu that opens tiles that open options that open a field should become one visible level; report it when flattening changes the flow.
- No search box for three choices, and no dropdown for two.

## Consistency across screens

- The same element behaves and looks the same on every screen: same component, same variant, same icon for the same action.
- After fixing a display defect in a shared component or pattern, search the other screens that use it for the same defect, and report each one found outside the scope.
- Show a past time as relative up to about a week ("5 minutes ago"), then as an exact date; report mixed formats.
- Separate what does different things; merge what is the same into one screen or one reusable component, and report duplicates.

Done when: no status, badge, or message in scope claims something not yet true, each fact appears once, controls fit their number of options, and every defect fixed in a shared pattern has been looked for elsewhere.
