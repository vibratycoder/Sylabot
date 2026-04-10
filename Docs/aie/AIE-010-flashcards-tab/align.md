# Align -- Flashcards Tab

**AIE:** AIE-010
**Date:** 2026-04-08
**Severity:** moderate
**Domain:** frontend

## Problem
Users need a flashcard study mode with visual card-flip animations to review key terms and concepts per module.

## Decision
Implement the Flashcards tab (Tab 5) in `index.html`:

1. **Module Selector** -- Pill buttons for modules with flashcard content.

2. **Flashcard Display** -- CSS 3D flip card: `perspective: 1000px` on container, `transform-style: preserve-3d` on card, click toggles `.flipped` class applying `rotateX(180deg)`, `backface-visibility: hidden` on both faces, `transition: transform 0.5s`. Front shows question, back shows answer.

3. **Navigation** -- Prev/Next buttons, "Card X of Y" counter. Next button auto-unflips the card before advancing. State tracked via `currentFCModule` and `fcIndex`.

4. **Empty State** -- Message when no flashcard content exists.

## Why This Approach
- CSS 3D transforms create a satisfying flip animation without JavaScript animation libraries
- Simple prev/next navigation is intuitive for sequential card review
- Auto-unflip on advance prevents showing the answer of the next card

## Impact
- Adds ~80 lines of JavaScript + HTML to `index.html`
- Depends on AIE-003 (activeContent.flashcards, fcIndex, currentFCModule)
- Flip animation CSS defined in AIE-002

## Success Criteria
- Cards flip with smooth 3D animation on click
- Front and back content display correctly with no bleedthrough
- Navigation advances through cards and auto-unflips
- Counter shows accurate position
- Module switching resets to card 1
