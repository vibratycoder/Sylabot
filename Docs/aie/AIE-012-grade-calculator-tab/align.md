# Align -- Grade Calculator Tab

**AIE:** AIE-012
**Date:** 2026-04-08
**Severity:** moderate
**Domain:** frontend

## Problem
Users need to calculate their current weighted grade and determine what score they need on the final exam to achieve target letter grades.

## Decision
Implement the Grade Calculator tab (Tab 7) in `index.html`:

1. **Grade Input** -- Dynamic rows, one per grade weight component from the course. Each row: label + number input (0-100). Recalculates on every `oninput` event via `calcGrade()`.

2. **Calculation** -- `weighted = sum(score * weight / 100)`, `percentage = weighted / weightUsed * 100` (only counting weights with entered scores).

3. **Letter Grade Scale** -- A (93+), A- (90-92), B+ (86-89), B (83-85), B- (80-82), C+ (76-79), C (73-75), C- (70-72), F (<70). Display current letter grade and percentage.

4. **Final Exam Calculator** -- Auto-detects a grade weight containing "final" (case-insensitive). For each target grade (A through C-), calculates the needed final score using: `needed = (targetPct * 100 - currentWeighted) / finalWeight * 100`. Displays "Already achieved!", the needed percentage, or "Not possible" as appropriate.

## Why This Approach
- Real-time recalculation on input gives instant feedback
- Final exam calculator is the most-requested feature for students
- Auto-detecting the "final" weight avoids requiring user configuration
- Standard letter grade scale covers most US universities

## Impact
- Adds ~100 lines of JavaScript + HTML to `index.html`
- Depends on AIE-003 (activeGradeWeights)

## Success Criteria
- Grade inputs render one row per grade weight component
- Weighted average calculates correctly, excluding empty inputs
- Letter grade displays correctly at all thresholds
- Final exam calculator shows correct needed scores for each target grade
- "Already achieved" and "Not possible" messages appear at correct thresholds
