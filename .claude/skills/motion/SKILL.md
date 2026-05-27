---
name: motion
description: Add or review web animations in the Emil Kowalski style — subtle, fast, purposeful motion using Motion for React (formerly Framer Motion), CSS, or View Transitions. Triggers on requests to "add animation", "make this animate", "make it feel snappier", "use Framer Motion / Motion for React", "add a transition", "review motion / animations", or when the user references Emil Kowalski, animations.dev, Sonner, Vaul, or cmdk style. Use for entry/exit animations, layout animations, drawer/modal/toast/dropdown motion, hover/press feedback, page transitions, and motion code review.
---

# Motion (Emil Kowalski style)

Motion serves the interface. It clarifies what just happened, where something came from, and what's now interactive. It is not decoration. If an animation doesn't earn its place, remove it.

## Core principles

1. **Fast by default.** Most UI animations are 150–250ms. Anything over 400ms feels sluggish unless it's a deliberate hero moment. Drawers and large surfaces can go 300–500ms; chrome and small elements stay under 250ms.
2. **Ease-out for entry, ease-in for exit, ease-in-out only for moves.** Things appear quickly then settle. Things leave by accelerating away. Symmetric ease-in-out is for transforms that go A→B (layout shifts).
3. **One thing at a time.** Don't fade AND slide AND scale AND blur. Pick the one or two transforms that communicate the change. Usually opacity + a small translate is enough.
4. **Small distances.** Translate by 4–16px, not 100px. Scale by 0.95–1.05, not 0.5–1.5. Motion should feel like the element settling, not flying in.
5. **Spring for direct manipulation, tween for system-initiated.** If the user is dragging/pulling (Vaul drawers, sliders, swipes), use a spring that tracks the finger. If the system is just transitioning state, use a tween with a curve.
6. **Respect `prefers-reduced-motion`.** Always. Skip transforms, keep opacity, or shorten durations to ~0.
7. **No layout thrash.** Animate `transform` and `opacity`. Avoid animating `width`, `height`, `top`, `left`, `margin` — use `layout` animations (Motion) or `view-transition-name` (CSS) instead.
8. **Origin matters.** A dropdown should expand from where it was triggered. A modal should scale from its center. A toast should slide from the edge it lives on. Wrong origin = wrong feel.

## The easing curves Emil uses

These show up across Sonner, Vaul, cmdk, and animations.dev examples:

```ts
// Smooth out — the workhorse for most UI entries
const easeOutQuart = [0.25, 1, 0.5, 1];

// Snappier out — buttons, hovers, small chrome
const easeOutExpo = [0.16, 1, 0.3, 1];

// Smooth in-out — for layout/transform moves between two states
const easeInOutQuart = [0.76, 0, 0.24, 1];

// Spring presets (Motion for React)
const springSnappy = { type: "spring", stiffness: 400, damping: 40 };   // direct manipulation
const springSoft   = { type: "spring", stiffness: 300, damping: 30 };   // drawers, sheets
const springGentle = { type: "spring", stiffness: 200, damping: 25 };   // larger surfaces
```

Default to `easeOutQuart` for entries and `easeInOutQuart` for moves unless there's a reason to deviate.

## Patterns

### Entry / exit (Motion for React)

```tsx
import { motion, AnimatePresence } from "motion/react";

<AnimatePresence>
  {open && (
    <motion.div
      initial={{ opacity: 0, y: 8 }}
      animate={{ opacity: 1, y: 0 }}
      exit={{ opacity: 0, y: 8 }}
      transition={{ duration: 0.2, ease: [0.25, 1, 0.5, 1] }}
    />
  )}
</AnimatePresence>
```

### Dropdown / popover (origin at trigger)

```tsx
<motion.div
  initial={{ opacity: 0, scale: 0.96, y: -4 }}
  animate={{ opacity: 1, scale: 1, y: 0 }}
  exit={{ opacity: 0, scale: 0.96, y: -4 }}
  transition={{ duration: 0.15, ease: [0.16, 1, 0.3, 1] }}
  style={{ transformOrigin: "top right" }}
/>
```

### Drawer / sheet (spring, direct-manipulation feel)

```tsx
<motion.div
  initial={{ y: "100%" }}
  animate={{ y: 0 }}
  exit={{ y: "100%" }}
  transition={{ type: "spring", stiffness: 300, damping: 30 }}
/>
```

Prefer the `vaul` library for real drawers — it handles velocity-aware dismissal, snap points, and accessibility.

### Layout animations (resizing containers, reordering lists)

```tsx
<motion.div layout transition={{ duration: 0.25, ease: [0.76, 0, 0.24, 1] }} />
```

Use `layout` instead of animating width/height by hand. For reordering lists, give each item a stable `layoutId` and let Motion interpolate.

### Hover / press feedback

Keep it almost imperceptible. A button doesn't need to grow — it needs to acknowledge.

```tsx
<motion.button
  whileHover={{ scale: 1.02 }}
  whileTap={{ scale: 0.98 }}
  transition={{ duration: 0.1, ease: [0.16, 1, 0.3, 1] }}
/>
```

### Page / route transitions

Use the native View Transitions API when available — it's cheaper than wrapping the world in `AnimatePresence`.

```css
::view-transition-old(root),
::view-transition-new(root) {
  animation-duration: 0.25s;
  animation-timing-function: cubic-bezier(0.25, 1, 0.5, 1);
}
```

### Reduced motion

```tsx
import { useReducedMotion } from "motion/react";

const reduce = useReducedMotion();
const transition = reduce
  ? { duration: 0 }
  : { duration: 0.2, ease: [0.25, 1, 0.5, 1] };
```

Or in CSS:

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; }
}
```

## Reviewing existing motion

When asked to review animations, check:

1. **Duration sanity** — anything over 400ms on small chrome is wrong.
2. **Easing direction** — entries using ease-in or symmetric curves feel sluggish; exits using ease-out feel like they linger.
3. **Layered transforms** — count what's animating at once. More than two properties per element is usually too much.
4. **Origin** — does the element come from where it should? `transformOrigin` set correctly?
5. **Performance** — are we animating layout-triggering properties? Switch to transform.
6. **Reduced motion** — is it handled?
7. **Cleanup** — are exit animations actually running, or is the element unmounting before exit completes? (`AnimatePresence` wrapping the right level?)

## Output format

When adding motion: ship the code change. When reviewing: same format as the `taste` skill — Top 3 fixes (with specific values, e.g. "300ms → 180ms, ease change `[0.4,0,0.2,1]` → `[0.25,1,0.5,1]`"), then per-component notes, then what's working.

## Anti-patterns

- Wrapping everything in `motion.div` because Motion is installed.
- 500ms+ animations on routine UI — it's not impressive, it's slow.
- Spring physics on system-initiated transitions where the user has no contact with the motion — it just looks wobbly.
- Animating `display: none` ↔ `display: block`. Use `AnimatePresence` or `visibility` + opacity.
- Stagger delays > 50ms per item on lists longer than 5 items — the last item arrives noticeably late.
- Forgetting `transformOrigin` and getting modal-scales-from-corner bugs.
- Adding motion to communicate state that should just be a clear static design. Motion is the last 10%, not the first 50%.

## References

- animations.dev — Emil Kowalski's course (the canonical reference for this style)
- motion.dev — Motion for React docs (formerly Framer Motion)
- Sonner, Vaul, cmdk — open-source examples of the style in practice
