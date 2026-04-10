# Align -- Planner Tab

**AIE:** AIE-007
**Date:** 2026-04-08
**Severity:** moderate
**Domain:** frontend

## Problem
Users need a chronological view of their deadlines organized by week to plan their study schedule. The dashboard shows an overview, but the planner provides detailed weekly breakdown.

## Decision
Implement the Planner tab (Tab 2) in `index.html`:

1. **This Week** -- Deadlines within days 0-6 from current week start. Each item shows: date, days-away label, context-sensitive verb, assignment name. Same-day items get a "Today!" flag.

2. **Next Week** -- Deadlines 7-13 days from week start. Same item format.

3. **Full Schedule** -- All future deadlines chronologically. Same item format.

Each section is a card with a header. Empty sections show a "Nothing scheduled" message.

## Why This Approach
- Three-section layout (this week / next week / all) provides both immediate and long-term views
- Same badge and verb system as dashboard ensures consistency
- Simple chronological sort is the most useful for planning

## Impact
- Adds ~80 lines of JavaScript + HTML to `index.html`
- Depends on AIE-003 (activeDeadlines, daysUntil)
- Uses lazy tab rendering

## Success Criteria
- Deadlines appear in the correct week section
- "Today!" flag shows for same-day deadlines
- Days-away labels are accurate
- Empty sections handled gracefully
- Re-renders correctly when switching courses
