# Align -- Progress Tracker Tab

**AIE:** AIE-011
**Date:** 2026-04-08
**Severity:** moderate
**Domain:** frontend

## Problem
Users need to visualize their overall course progress, identify at-risk deadlines, and receive actionable study recommendations.

## Decision
Implement the Progress tab (Tab 6) in `index.html`:

1. **Stats Row** -- Three metrics: modules completed vs total, completion percentage, exams taken vs total exams.

2. **Module Tracker** -- Grid of circular indicators, one per module. Colors: green = done, yellow = current, gray = upcoming. Click toggles completion status, persisted to `localStorage['syllabot_${courseId}_mod-${moduleNum}']`.

3. **Risk Analysis** -- Top 5 upcoming deadlines ranked by urgency: URGENT (<=3 days, red), HIGH RISK (<=10 days, red), MEDIUM (<=21 days, yellow), LOW (>21 days, green).

4. **Recommendations** -- Conditional tips based on state: suggest generating content if none exists, suggest starting quizzes if content exists but no history, suggest reviewing weak modules based on quiz scores, etc.

## Why This Approach
- Visual module tracker gives instant spatial sense of progress
- Click-to-toggle makes marking modules done frictionless
- Risk analysis surfaces the most urgent items without requiring the user to calculate
- Recommendations provide actionable next steps based on actual data

## Impact
- Adds ~120 lines of JavaScript + HTML to `index.html`
- Depends on AIE-003 (activeModules, activeDeadlines, daysUntil, module completion localStorage keys)

## Success Criteria
- Module circles reflect correct completion status from localStorage
- Clicking a circle toggles and persists its completion state
- Risk analysis correctly categorizes deadlines by urgency
- Recommendations change based on content/quiz history availability
- Stats row shows accurate counts
