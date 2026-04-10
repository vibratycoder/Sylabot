# Align -- SPA Shell & Design System

**AIE:** AIE-002
**Date:** 2026-04-08
**Severity:** major
**Domain:** frontend

## Problem
The application needs a foundational HTML structure, CSS design system, and tab-based navigation to host all 8 feature tabs. Everything lives in a single `index.html` file (per ADR-001) with no external CSS/JS dependencies (per ADR-003).

## Decision
Create `index.html` with:

1. **CSS Design System** -- All colors as CSS custom properties on `:root` (--bg: #0f1117, --surface: #1a1d27, --accent: #6c5ce7, etc.), typography using Segoe UI/system-ui stack, component classes (.card, .stat-card, .badge, .topic-btn, .quiz-opt), badge variants (urgent/soon/upcoming/later/done/exam), fadeIn animation, flashcard flip animation, responsive breakpoint at 768px.

2. **HTML Structure** -- Fixed header (logo + course badge + date), 8-tab navigation bar with Unicode icons (Dashboard, Planner, Tutor, Quiz, Flashcards, Progress, Grade Calc, Courses), 8 tab content panels (only one visible at a time), course creation wizard modal, content generation modal, file upload area.

3. **Tab Switching** -- Click handler on nav buttons that shows/hides panels, updates active nav state. Max content width 1200px centered.

## Why This Approach
- Monolithic single-file avoids build tools and module bundlers (ADR-001)
- CSS custom properties provide theming without preprocessors (ADR-003)
- Dark-mode-first design matches the project spec
- Tab panels with show/hide is simpler than SPA routing for this scope

## Impact
- Creates `index.html` in project root
- Establishes the visual foundation all other tabs build on
- All subsequent AIE entries (003-012) depend on this shell existing
- No external dependencies

## Success Criteria
- `index.html` opens in a browser showing the dark-mode header and 8 nav tabs
- Clicking each tab shows its (initially empty) content panel
- CSS variables, component classes, and animations are defined and usable
- Layout is responsive at 768px breakpoint
- Course badge in header shows "No Course" when no course is loaded
