# Align -- Tutor View Tab

**AIE:** AIE-008
**Date:** 2026-04-08
**Severity:** minor
**Domain:** frontend

## Problem
Users need a way to study module content in a rich, readable format. The server generates HTML-formatted study material per module, and the frontend needs to display it with proper styling.

## Decision
Implement the Tutor tab (Tab 3) in `index.html`:

1. **Topic Selector** -- Row of pill-shaped `.topic-btn` buttons, one per module that has tutor content in `activeContent.tutor`. Clicking a button loads that module's HTML.

2. **Content Display** -- Div that receives the raw HTML from tutor content. Uses semantic CSS classes: `.tutor-section` (main block), `.key-term` (yellow highlight), `.example` (left-bordered box), `.worked-example` (bordered step-by-step box).

3. **Empty State** -- Message shown when no tutor content has been generated.

## Why This Approach
- Pill selector matches the UI pattern used in Quiz and Flashcards tabs for consistency
- Raw HTML injection allows rich formatting from the server-generated content
- Minimal logic -- this tab is essentially a content viewer

## Impact
- Adds ~50 lines of JavaScript + HTML to `index.html`
- Depends on AIE-003 (activeContent.tutor)
- Tutor content CSS classes defined in AIE-002 design system

## Success Criteria
- Topic pills appear for all modules with tutor content
- Clicking a pill loads and displays the correct HTML content
- Key terms, examples, and worked examples render with correct styling
- Empty state shown when no content exists
