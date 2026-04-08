# Align — Standardize Visual Formatting Across All 7 Tabs

**AIE:** AIE-001
**Date:** 2026-04-08
**Severity:** moderate
**Domain:** frontend

## Problem
The 7 tabs (Dashboard, Planner, Tutor, Quiz, Flashcards, Progress, Grade Calc) were built incrementally and have inconsistent formatting:

1. **No tab headers** — tabs jump straight into content with no title or description. Dashboard has stat cards as a visual anchor, but Planner, Tutor, Flashcards, and Quiz start with bare cards.
2. **Inconsistent card spacing** — some tabs use `margin-bottom:20px` inline, others rely on the card class's `margin-bottom:16px`. No uniform section gaps.
3. **No section icons/accents on card headers** — `<h2>` tags inside cards are plain text with no visual differentiation. Dashboard, Progress, and Grade Calc cards all look identical despite serving very different purposes.
4. **Inline styles everywhere** — stat cards, grid containers, timeline labels, and grade scale colors use inline `style=""` attributes instead of reusable CSS classes, making the layout fragile and inconsistent.
5. **Flashcards tab is sparse** — just a card with module buttons and a flip card. No instructions, no progress indicator for how many cards are in the deck, no keyboard shortcut hints.
6. **Planner tab lacks visual hierarchy** — This Week vs. Next Week vs. AEC vs. Full Schedule all look like identical cards with no visual priority signal.
7. **Grade Calc grading scale table** is plain with no row hover highlighting or visual banding.
8. **Progress tab risk cards** use inline styles for colored left-borders rather than reusable CSS classes.

## Decision
Introduce a consistent formatting system across all tabs:

1. **Tab hero headers** — Add a `.tab-header` component at the top of each tab with the tab title, subtitle/description, and an accent-colored left border. Gives every tab a clear visual identity.
2. **Card header icons** — Add a small colored icon/dot before each `<h2>` inside cards using a `.card-header` class with a `::before` pseudo-element. Color-code by section type (deadlines = red, study = blue, grades = accent, project = yellow).
3. **Section dividers** — Add a `.section-gap` utility class for consistent 24px spacing between card groups.
4. **Extract inline styles to CSS** — Move all repeated inline `style=""` patterns (stat card colors, grid margins, timeline labels, risk card borders) into proper CSS classes.
5. **Flashcards tab enhancement** — Add a tab header, deck size indicator, keyboard shortcut hint ("Press Space to flip"), and a progress bar showing current position in the deck.
6. **Planner visual hierarchy** — Add urgency accent bars to This Week (yellow) and Next Week (blue) cards. AEC gets a special accent (orange). Full Schedule is dimmer.
7. **Grade scale table** — Add alternating row backgrounds and a highlight on the row matching the user's current projected grade.
8. **Progress risk cards** — Replace inline border-left styles with `.risk-high`, `.risk-medium`, `.risk-low` CSS classes.

## Why This Approach
- **CSS-class-based** rather than more inline styles ensures consistency and easy future changes.
- **Tab headers** give each page a clear identity without adding new functionality — purely visual clarity.
- **Minimal HTML changes** — mostly adding CSS classes to existing elements and a small header div per tab. Does not alter any JavaScript logic or data flow.
- Alternative considered: full CSS framework (Tailwind/Bootstrap) — rejected because the app is a single file and adding a framework would bloat it.

## Impact
- **Files touched:** `index.html` only (single-file app)
- **CSS section:** ~60 new lines of CSS classes
- **HTML body:** Adding `.tab-header` div to each of the 7 tabs, adding CSS classes to existing elements, removing inline styles
- **JavaScript:** Zero changes — no logic affected
- **Risk:** Low. Purely presentational. Worst case is a visual regression that's immediately visible.

## Success Criteria
- Every tab opens with a clear header (title + subtitle)
- Card headers have color-coded accent indicators
- No more inline `style=""` for recurring patterns (risk cards, stat colors, grid gaps)
- Flashcards tab shows deck progress and keyboard hint
- Planner cards have visual urgency differentiation
- Grade scale table has row banding
- Consistent spacing between all card sections across all tabs
