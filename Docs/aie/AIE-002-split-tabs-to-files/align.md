# Align — Split Monolithic index.html Into Separate Tab Files

**AIE:** AIE-002
**Date:** 2026-04-08
**Severity:** major
**Domain:** frontend

## Problem
The entire Syllabot application lives in a single `index.html` file (~2,300+ lines). This makes it:
- Hard to maintain — CSS, JS, and HTML for all 7 tabs are interleaved
- Difficult to work on one tab without scrolling past thousands of lines
- Impossible to track changes per-tab in version control
- Prone to merge conflicts if multiple features are developed simultaneously

The user explicitly requested: "create new files for all of the different tabs."

## Decision
Split the application into a modular file structure:

```
Sylabus Compiler/
├── index.html              ← Shell: header, tab nav, script loader
├── css/
│   └── styles.css          ← All CSS (shared + tab-specific)
├── js/
│   ├── data.js             ← Course data, quiz data, written data, flashcard data, tutor content
│   ├── app.js              ← Initialization, tab switching, shared utilities
│   ├── dashboard.js        ← Dashboard tab rendering
│   ├── planner.js          ← Planner tab rendering
│   ├── tutor.js            ← Tutor tab rendering
│   ├── quiz.js             ← Quiz tab logic (slider, MC, written, grading, history)
│   ├── flashcards.js       ← Flashcards tab logic
│   ├── progress.js         ← Progress tab rendering
│   └── grades.js           ← Grade calculator tab logic
├── tabs/
│   ├── dashboard.html      ← Dashboard tab HTML
│   ├── planner.html        ← Planner tab HTML
│   ├── tutor.html          ← Tutor tab HTML
│   ├── quiz.html           ← Quiz tab HTML
│   ├── flashcards.html     ← Flashcards tab HTML
│   ├── progress.html       ← Progress tab HTML
│   └── grades.html         ← Grade calculator tab HTML
└── docs/aie/               ← AIE documentation
```

Each tab HTML file contains ONLY the inner content of that tab (no `<html>`, `<head>`, etc.). They are loaded into the shell via JavaScript `fetch()` at startup.

## Why This Approach
- **Separation of concerns** — CSS, JS, HTML, and data are each in their own files
- **Tab-per-file** — each tab can be edited independently without touching other tabs
- **Data layer isolated** — course data, quiz banks, tutor content all in `data.js`, easy to update without touching logic
- **No build tools required** — plain JS modules loaded via `<script>` tags, served by Python HTTP server. No webpack/vite/bundler needed.
- **Alternative considered:** ES modules with `import/export` — rejected because Python's `http.server` doesn't set correct MIME types for `.mjs` files, causing CORS issues. Plain `<script>` tags in order are simpler and work universally.
- **Alternative considered:** Keep single file, just add comments — rejected because user explicitly requested separate files.

## Impact
- **Every line of index.html is affected** — the file is being decomposed
- **17 new files created** (1 CSS + 8 JS + 7 HTML + 1 updated index.html)
- **Zero functionality changes** — every feature works identically after the split
- **Server still works** — Python `http.server` serves static files from the directory, no config changes needed
- **Risk:** Medium. Tab loading order matters. If a JS file references a function defined in another file that hasn't loaded yet, it will error. Mitigation: load data.js first, then app.js, then tab-specific JS files, then call init.

## Success Criteria
- `http://localhost:8080` works identically to before the split
- Each tab renders the same content
- All quiz, flashcard, tutor, grading, and history features still work
- Each tab's HTML, JS are in their own files
- CSS is in one external stylesheet
- No inline `<style>` or `<script>` blocks in index.html (except the loader)
