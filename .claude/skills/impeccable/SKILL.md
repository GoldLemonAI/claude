---
name: impeccable
description: The final-pass craft review before something ships. Holds work to a maximum-strictness bar across four dimensions — pixel-perfect UI, code craft, copy, and motion — and either flags the gaps or fixes them. Use when the user asks "is this ready to ship", "make this impeccable", "final polish pass", "ship-ready review", "is this Linear/Vercel/Stripe quality", or before a launch/PR-merge moment. Stricter and broader than /taste — taste asks "is this good?", impeccable asks "is there a single thing left that a craftsman would notice?".
---

# Impeccable

Impeccable means: a careful person, looking closely, finds nothing left to fix. It is not "good enough." It is not "shippable." It is the bar where every detail has been considered and either kept on purpose or fixed.

This skill runs the final pass. It is intentionally strict. The default answer is "not yet" — earn the "yes."

## When to invoke

- Before merging a PR that touches user-facing surface.
- Before a launch, demo, or screenshot for marketing.
- When the user explicitly wants the highest bar applied.
- After `/taste` or `/code-review` has caught the big things, and you want the last 5%.

If the work is still in mid-iteration, use `/taste` or `/code-review` instead. Impeccable is for things that are already "done" — that's when this pass matters.

## The four dimensions

Run all four. Skip a dimension only if it truly doesn't apply (e.g., a backend-only PR has no UI dimension). Skipping should be the exception, not the default.

### 1. Pixel-perfect UI

Look at the actual rendered pixels — screenshot or running app. Source code is not enough.

- **1px alignments** — edges of cards, inputs, buttons line up across the layout. Icon centers align with text baselines, not text bounding boxes.
- **Optical adjustments** — geometric centers are wrong for triangles/play icons; they need to shift right. Round shapes next to square shapes need to overshoot slightly to look the same size.
- **Radius consistency** — every radius in the design comes from a defined scale (e.g., 4/6/8/12). No accidental 7px or 10px.
- **Shadow physics** — one light source. Shadow direction and softness consistent. Color tinted by the background, not pure black at 20% opacity.
- **Stroke weight** — icons all share the same stroke weight. No 1.5px next to 2px next to 1px.
- **Asset crispness** — images served at 2x for retina. SVGs preferred over PNGs for icons. No JPEG artifacts on UI chrome.
- **Color discipline** — every color used appears in the palette. No one-off hex values. Neutrals consistently warm or cool.
- **Type details** — kerning on display sizes, optical sizes used where supported, numeric figures (tabular vs proportional) chosen on purpose, hanging punctuation in quotes/lists.
- **Empty/loading/error states** — each one designed, not stubbed.
- **Hover/focus/active** — every interactive element has all three. Focus rings visible and consistent.
- **Dark mode** — if it exists, parity with light. Not just inverted, properly designed.
- **Density at extremes** — what happens with 1 item, 10,000 items, 1-char name, 200-char name, very long URL? All handled.
- **Browsers/devices** — verified in Chrome, Safari, Firefox; mobile and desktop; landscape and portrait if relevant.

### 2. Code craft

Read the diff or files carefully.

- **Naming** — every identifier reads cleanly aloud. No abbreviations that aren't industry standard. No `data`, `info`, `manager`, `helper`, `utils` unless truly accurate.
- **No dead code** — unused imports, vars, exports, branches all removed. Commented-out code deleted, not parked.
- **No premature abstraction** — wrappers that have one caller, generics that allow flexibility nobody asked for, config objects with one field. Inline them.
- **No defensive programming for impossible states** — internal callers are trusted. Only validate at system boundaries.
- **Types are precise** — no `any`, minimal `unknown`, no `as` casts that hide a real type mismatch. Discriminated unions instead of optional flags.
- **Error handling matches the error** — every catch either recovers, transforms with context, or rethrows. Never swallow.
- **No magic numbers/strings** — meaningful constants extracted; one-off literals inlined and obvious.
- **File and function sizes** — if a function does more than its name, split. If a file has unrelated exports, split.
- **Tests cover behavior, not implementation** — tests would survive an internal refactor. Mocks at boundaries, not all over.
- **No TODOs without a ticket** — TODO without a name and link is just litter. Remove or convert.
- **Consistency with the codebase** — same patterns as nearby code unless the diff is explicitly the place to change a pattern.
- **Performance hotspots** — N+1s, unnecessary re-renders, blocking work on the main thread, missing keys on lists, missing memoization where it matters (and absent where it doesn't).
- **Security boundaries** — input validated, output encoded, secrets not logged, authn/authz checks present.

### 3. Copy

Read every word the user will see.

- **No filler** — "simply", "just", "easily", "powerful", "robust", "seamless", "intuitive" all deleted unless they earn it.
- **Lead with the point** — first sentence states the conclusion. Headings are the answer, not a tease.
- **Concrete over abstract** — numbers, names, specifics. "Saves 4 hours a week" not "boosts productivity."
- **Verb-led CTAs** — "Save changes", not "Submit." "Delete project", not "OK."
- **Errors say what to do** — never "An error occurred." State what failed, why if useful, and the next step.
- **Empty states earn their text** — explain what should be here and how to get there.
- **Consistent terminology** — one name per concept across the product. Not "project" in one place and "workspace" in another.
- **Capitalization style** — sentence case or title case, picked and applied. Not mixed.
- **Punctuation** — em dashes for asides, en dashes for ranges, hyphens for compounds. Smart quotes, not straight. Oxford comma policy applied consistently.
- **Voice match** — copy sounds like one person wrote it, in the brand's voice, throughout.

### 4. Motion

If anything moves, it should move on purpose.

- **Durations in range** — chrome under 250ms, surfaces under 400ms, hero moments only when intentional.
- **Easing matches direction** — ease-out for entries, ease-in for exits, ease-in-out only for moves.
- **Origin correct** — dropdowns expand from their trigger, modals scale from center, toasts slide from their edge.
- **One or two properties at a time** — not opacity + slide + scale + blur + rotate.
- **No layout thrash** — `transform` and `opacity` only; layout/view-transitions for size changes.
- **Springs for direct manipulation, tweens for system** — finger-tracked = spring, system-triggered = tween.
- **`prefers-reduced-motion` honored** — actually tested, not just declared.
- **Exit animations complete** — `AnimatePresence` (or equivalent) wrapping at the right level so things don't unmount mid-fade.
- **No stagger pileup** — list stagger ≤ 50ms per item, capped or removed past 5 items.
- **60fps verified** — DevTools Performance tab confirms, not assumed.

See `/motion` for the specific curves and patterns.

## How to run

1. **Gather artifacts.** Screenshot(s) of every changed screen, in both states (light/dark, empty/full, etc.). The diff. The running app. The copy in context.
2. **Run each dimension** in order. For each, either flag specific issues or skip explicitly with one sentence why ("backend-only PR, no UI dimension").
3. **Rank by severity.** Three tiers:
   - **Blockers** — would be visibly wrong or broken to a user. Must fix before shipping.
   - **Craft gaps** — won't break anything but a careful eye notices. Should fix before claiming impeccable.
   - **Nits** — debatable, personal preference, or so minor they don't matter. Optional.
4. **Produce the report** in the format below.

## Output format

```
Verdict: [Ship-ready / Craft gaps remain / Not ready]

Blockers
- [file:line or screen — what's wrong — specific fix]
- ...

Craft gaps
- [file:line or screen — what's wrong — specific fix]
- ...

Nits (optional)
- ...

What's already impeccable
- [one or two specific things, only if genuinely strong]

Skipped dimensions
- [dimension] — [one-sentence reason]
```

If `--fix` is passed (or the user asks to apply), fix Blockers and Craft gaps in the working tree, leave Nits for the user. Same convention as `/code-review --fix`.

## The bar

Impeccable is calibrated against work like Linear, Vercel, Stripe, Apple, Things, Arc — products where craft is a feature. If you would not be embarrassed to put this next to their work, it passes. If you would, it doesn't.

That bar is high on purpose. The skill exists because most things ship without it, and you want a tool that holds the line.

## Anti-patterns

- Approving work as impeccable because it's "pretty good." It's not the same bar as `/taste`.
- Flagging everything at equal severity — the tiering matters.
- Inventing problems to seem thorough. If a dimension is clean, say so in one line.
- Demanding a redo when targeted fixes would land it.
- Padding with generic accessibility/SEO/performance notes unrelated to the actual artifact.
- Stopping at code review when there's UI to look at, or vice versa.
