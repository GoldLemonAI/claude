---
name: taste
description: Critique the visual design of a UI — spacing, typography, hierarchy, color, alignment, density, and overall polish. Use when the user asks for design feedback, a "taste check," or a review of a mockup, screenshot, Figma frame, or running app's look-and-feel. Triggers on phrases like "review the design", "how does this look", "taste check", "is this UI good", or when a screenshot/figma.com URL is shared with intent to critique.
---

# Taste

Give honest, specific design critique. Avoid vague praise ("looks great") and avoid checklist-padding ("consider accessibility"). Point at concrete pixels and say what's wrong and what to do.

## Inputs

Work from whichever of these the user provides:
- A screenshot or image file → read it directly.
- A figma.com URL or current Figma selection → use `get_design_context` and `get_screenshot` from the Figma MCP server.
- A running app → use the `run` skill to launch it, then capture a screenshot.
- A code file rendering UI → read the source, but still request a screenshot if none is provided. Static code reading misses real layout.

If none of the above is available, ask for a screenshot before reviewing. Do not critique blind.

## What to look at

Go through these dimensions. For each, either flag a specific issue or skip — do not write "looks fine" filler.

1. **Hierarchy** — Is the primary action obvious within 1 second? Are headings, body, and metadata visually distinct? Is anything competing that shouldn't be?
2. **Spacing & rhythm** — Consistent scale (4/8px grid or similar)? Cramped or floating elements? Vertical rhythm between sections?
3. **Typography** — Too many sizes/weights? Line length comfortable (45–75ch for body)? Line-height tight on headings, looser on body? Numeric vs. proportional figures used correctly?
4. **Color** — Contrast meets at least 4.5:1 for body text? Accent color used sparingly enough to actually mean something? Neutrals warm/cool consistently?
5. **Alignment** — Optical alignment, not just mathematical. Icons centered with their labels. Edges of cards/inputs line up across the layout.
6. **Density** — Right amount of information per screen for the user's task? Empty states feel intentional, not broken?
7. **Affordance** — Buttons look pressable, links look clickable, disabled states look disabled. Hover/focus states defined.
8. **Polish** — Border radii consistent. Shadows consistent and physically plausible (one light source). No 1px misalignments, no off-by-one paddings.
9. **Voice** — Microcopy clear and human. No "An error occurred" — say what broke and what to do.

## Output format

Structure the critique as:

**Top 3 fixes** — the highest-leverage changes, in priority order. Each: what's wrong, where (point at the element), and the specific fix (with values when you can — "16px → 24px", not "more padding").

**Other notes** — smaller issues, bulleted. Skip this section if there aren't any worth mentioning.

**What's working** — one or two things, only if genuinely strong. Not a participation trophy.

Be willing to say "this needs to be redesigned, not tweaked" when that's the honest answer. Don't dress up a fundamental problem as five small ones.

## Anti-patterns to avoid

- Generic accessibility lectures unrelated to the actual design.
- Suggesting "more whitespace" without saying where and how much.
- Listing every minor inconsistency at equal weight with major hierarchy problems.
- Recommending a redesign when a tweak would do, or tweaks when a redesign is needed.
- Praising things that aren't praiseworthy to soften criticism.
