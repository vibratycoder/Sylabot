# Align -- Dashboard Tab

**AIE:** AIE-006
**Date:** 2026-04-08
**Severity:** moderate
**Domain:** frontend

## Problem
Users need an at-a-glance overview of their active course: how many days until the final, what module they're on, upcoming deadlines, and what to work on right now.

## Decision
Implement the Dashboard tab (Tab 1, default view) in `index.html`:

1. **Stat Cards** -- 4-column grid: Days to Final (countdown with color coding: red <=7, yellow <=21, green otherwise), Current Unit (from first "current" module), Grade Weight Remaining (sum of weights with unfinished deadlines), Current Module (topic name).

2. **Upcoming Deadlines Table** -- All deadlines sorted by date. Columns: Assignment, Due Date (with "X days" count), Status Badge (EXAM/URGENT/THIS WEEK/UPCOMING/LATER/DONE based on type and days remaining).

3. **Do Right Now Checklist** -- Top 5 upcoming future deadlines. Each has: checkbox (toggles strikethrough), context-sensitive verb by type (Study for/Work on/Complete reading/Prepare for), estimated time range.

4. **Semester Timeline** -- Visual bar of week blocks from earliest to latest deadline + 1 week. Past weeks = accent purple, current = yellow, future = gray. Label "Week X of Y".

5. **Grade Weight Breakdown** -- Horizontal bars per grade weight component. Width proportional to weight %. Badge: "Done" (green) if all matching deadlines passed, "Active" (accent) otherwise.

## Why This Approach
- Dashboard renders immediately (not lazy) as it's the landing page
- Stat cards give quick metrics without scrolling
- Checklist provides actionable next steps
- Timeline gives temporal context for the semester

## Impact
- Adds ~200 lines of JavaScript + HTML to `index.html`
- Depends on AIE-003 (activeDeadlines, activeModules, activeGradeWeights, daysUntil)
- Always renders on course load (not lazy)

## Success Criteria
- Stat cards show correct values derived from course data
- Deadline table sorts correctly and shows appropriate badges
- Checklist shows only future deadlines with correct verbs and time estimates
- Timeline accurately reflects current position in the semester
- All elements update when switching courses
