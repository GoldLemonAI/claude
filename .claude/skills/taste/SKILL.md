---
name: taste
description: Give honest, specific critique across four lenses — (1) visual UI design (spacing, typography, hierarchy, color, alignment, polish), (2) product/UX (flows, empty/error states, end-to-end feel), (3) writing/copy (tone, voice, concision of microcopy or prose), and (4) brand/visual identity (logo, color system, type system coherence). Use when the user asks for a "taste check", design/copy/brand feedback, or a review of a mockup, screenshot, Figma frame, running app, written text, or brand asset. Triggers on phrases like "review the design", "taste check", "how does this read", "is this on-brand", "does this flow make sense", or when a screenshot/figma.com URL/copy block is shared with intent to critique.
---

# Taste

Give honest, specific critique. Avoid vague praise ("looks great", "reads well") and avoid checklist-padding ("consider accessibility"). Point at the concrete thing — pixel, word, screen, asset — and say what's wrong and what to do.

## Pick a lens

First, identify which lens(es) apply. The user may ask for one explicitly, or you infer it from what they shared:

- **Visual UI** — a screenshot, Figma frame, or running screen.
- **Product/UX** — a flow, multi-screen sequence, or full task ("can a user do X?").
- **Writing/copy** — microcopy, marketing text, docs, error messages, prose.
- **Brand/identity** — logo, palette, type system, brand application across surfaces.

A single artifact often deserves more than one lens (a landing page is visual + copy + brand). Run each applicable lens and label sections clearly.

## Inputs

Work from whichever of these the user provides:
- A screenshot or image file → read it directly.
- A figma.com URL or current Figma selection → use `get_design_context` and `get_screenshot` from the Figma MCP server.
- A running app → use the `run` skill to launch it, then capture a screenshot.
- A code file rendering UI → read the source, but still request a screenshot if none is provided. Static code reading misses real layout.
- A copy block, doc, or pasted text → read it directly.
- A flow → ask for the screens in order, or walk the running app end-to-end.
- A brand asset (logo, palette, type spec) → read the file or Figma frame.

If the artifact needed for the requested lens isn't available, ask for it before reviewing. Do not critique blind.

## What to look at — by lens

For each applicable lens, go through these dimensions. For each, either flag a specific issue or skip — do not write "looks fine" filler.

### Visual UI

1. **Hierarchy** — Is the primary action obvious within 1 second? Are headings, body, and metadata visually distinct? Anything competing that shouldn't be?
2. **Spacing & rhythm** — Consistent scale (4/8px grid)? Cramped or floating elements? Vertical rhythm between sections?
3. **Typography** — Too many sizes/weights? Line length comfortable (45–75ch for body)? Line-height tight on headings, looser on body? Numeric vs. proportional figures used correctly?
4. **Color** — Contrast ≥ 4.5:1 for body text? Accent color used sparingly enough to mean something? Neutrals warm/cool consistently?
5. **Alignment** — Optical, not just mathematical. Icons centered with labels. Edges of cards/inputs line up across the layout.
6. **Density** — Right amount of information per screen for the task? Empty states intentional, not broken?
7. **Affordance** — Buttons look pressable, links look clickable, disabled looks disabled. Hover/focus states defined.
8. **Polish** — Border radii consistent. Shadows consistent and physically plausible (one light source). No 1px misalignments.

### Product/UX

1. **Goal clarity** — Within 3 seconds of landing on a screen, does the user know what they can do here and why?
2. **Path of least resistance** — Is the happy path the shortest path? Count taps/clicks for the primary task.
3. **State coverage** — Empty, loading, error, partial, and success states all designed? Or only the "data exists" state?
4. **Error recovery** — When something fails, can the user actually fix it without leaving the screen?
5. **Reversibility** — Destructive actions need undo or confirmation. Non-destructive actions should NOT have confirmations.
6. **Feedback latency** — Anything > 200ms needs immediate acknowledgement (skeleton, spinner, optimistic update).
7. **Continuity** — Across the flow, does context carry forward? Or does the user re-enter/re-find things?
8. **Stakes match** — High-stakes actions get friction; low-stakes get speed. Inverted = bad.

### Writing/copy

1. **Voice consistency** — Same speaker throughout? Or does it swing between corporate, casual, and technical?
2. **Concision** — Cut every word that doesn't earn its place. Read each sentence and ask "what breaks if this is gone?"
3. **Specificity** — Concrete over abstract. "Saves 4 hours/week" beats "boosts productivity."
4. **Verbs over nouns** — "Ship faster" not "acceleration of shipping velocity."
5. **Lead with the point** — First sentence states the conclusion. Supporting detail follows.
6. **Error messages** — Say what broke, why, and what to do. Never just "An error occurred."
7. **Reading level** — Match the audience. Aim for clarity, not simplicity-as-condescension.
8. **Microcopy on buttons/CTAs** — Verb + object beats generic verbs. "Save changes" > "Submit" > "OK."

### Brand/visual identity

1. **Distinctiveness** — Could this logo/palette/type belong to 50 other companies? If yes, it's not identity, it's wallpaper.
2. **System, not assets** — Is there a system (rules for combining) or just a pile of files? Identity needs the system.
3. **Color discipline** — Primary, accent, neutrals — each with a role. Not a rainbow. Define when each is used.
4. **Type pairing** — Display + text pair has clear contrast in voice. Not two near-identical sans-serifs.
5. **Logo behavior** — Clear-space, min-size, mono/inverse versions, behavior on photos. Defined or guessed?
6. **Application coherence** — Does the brand feel like one thing across web, app, social, print, swag? Or different teams winging it?
7. **Tone alignment** — Visual identity and verbal identity say the same thing about the company. If the brand reads playful but the copy reads enterprise, fix one.
8. **Longevity** — Will this still look good in 3 years, or is it riding a trend (gradients-of-the-month, AI-glow, etc.)?

## Output format

Structure the critique as:

**Top 3 fixes** — the highest-leverage changes across all lenses combined, in priority order. Each: what's wrong, where (point at the element/word/screen), and the specific fix (with values when you can — "16px → 24px", not "more padding"; "cut the second sentence", not "tighten the copy").

**By lens** — one short section per applicable lens with the remaining concrete issues. Skip a lens if it has nothing worth noting. Skip the whole section if everything fits in the top 3.

**What's working** — one or two things, only if genuinely strong. Not a participation trophy.

Be willing to say "this needs to be redone, not tweaked" when that's the honest answer. Don't dress up a fundamental problem as five small ones.

## Anti-patterns to avoid

- Generic accessibility lectures unrelated to the actual artifact.
- Suggesting "more whitespace" / "tighten the copy" / "stronger brand" without saying where and how.
- Listing every minor inconsistency at equal weight with major problems.
- Recommending a redo when a tweak would do, or tweaks when a redo is needed.
- Praising things that aren't praiseworthy to soften criticism.
- Running all four lenses when the user only asked for one — pick what fits.
