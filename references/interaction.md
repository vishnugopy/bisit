# Gestures and keyboard

Apply this when a component already moves between items or states, or opens and dismisses a surface: a carousel, tabs, stepper, drawer, bottom sheet, dialog, or menu. A new input method for an action that already exists is not new behavior; disclose each one you add.

- Add horizontal swipe as an extra trigger for the existing next, previous, open, or dismiss action. Prefer CSS (`scroll-snap-type`, `overscroll-behavior-x: contain`, `touch-action: pan-y`) over script. If script is needed, use Pointer Events, cancel on `pointercancel` and below a distance threshold, ignore mostly vertical movement, leave the screen edges to the browser's back gesture, and skip the animation under reduced motion.
- Never make swipe the only way. Keep visible controls and keyboard operation, each usable with a single pointer.
- Follow the standard keys for the pattern: Tab to enter and leave the widget, arrow keys within tabs, radio groups, menus, and carousels (roving `tabindex`), Home and End for the first and last item, Enter and Space to activate, and Escape to close and return focus to the trigger. Prefer native elements, which supply these keys. Do not invent shortcuts; a single-character shortcut needs a way to turn it off or remap it.
- If the component has no existing navigation or dismiss action, such as swipe-to-delete on list rows, report the opportunity instead of building it.

Done when: every swipe action has a visible control and a keyboard equivalent, and the standard keys for the pattern work.
