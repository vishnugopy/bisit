# Loading, empty, error, and sending states

Apply this when the target fetches data, lists data that can be empty, or submits a form or action. Use the project's own loader, empty-state, and button components; add a state only where the code already has the condition (a loading flag, an empty array, a caught error). If the condition does not exist in the code, report it instead of building it.

## Loading

- Use exactly two kinds of loader. A small inline spinner belongs only to the busy state of the control the user activated, inside it, through the button's own loading prop when it has one. A content loader says "fetching, please wait" for a page, section, panel, or dialog body. Never invent a third spinner style for one screen.
- Give a content loader the size of the content it stands for, so nothing shifts when data arrives.
- A dialog or panel that fetches shows its loader in its body; never open an empty frame.
- Drop a redundant "Loading..." caption next to a loader that already announces itself, and give the loader an accessible name or a live status.

## Empty

- Use the project's empty-state component for every "no data" region: a muted icon, a title that names what is missing, an optional one-line description, and the action that fixes it when one exists (create, reset, retry).
- Distinguish "nothing exists" from "nothing matches": with an active search or filter, say there are no results and offer to clear it.
- Keep a plain inline sentence only for tiny placeholders, such as an empty dropdown or a single table cell.

## Errors

- Put a field's error directly under that field, stating the cause and how to fix it, linked to the field (`aria-describedby`, `aria-invalid`). Do not collect field errors only in a banner or a toast.
- Keep a dialog or form open after a failed submit, with the input preserved and a clear message, so the user can try again or try another way. Report code that closes or resets on failure; do not rewrite the flow.
- Word a server refusal as a refusal ("The message could not be sent."). Reserve "not confirmed" or "pending" for when no answer arrived (offline, timeout).

## Sending

- Block the submit control while a request is in flight, using its loading state rather than removing it, so a double click cannot send twice and the button keeps its width.
- Leave the rest of the form readable while sending; disable only what would change the request.

Done when: every fetch has a sized loader of the right kind, every empty region says what is missing and offers the fix, field errors sit under their fields, failures keep the user's input, and a submit cannot fire twice.
