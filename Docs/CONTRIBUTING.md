# Contributing

## Project Philosophy

Syllabot is intentionally simple. Before adding anything, ask: does this serve the student using the app right now?

### Principles

1. **Single-file frontend** -- All HTML, CSS, and JS live in `index.html`. No build step, no bundler, no npm.
2. **No external dependencies** -- No jQuery, no React, no Chart.js. If the browser can do it natively, use the native API.
3. **Offline-first** -- The app must work without a server for core features. The server is only for file parsing and content generation.
4. **localStorage only** -- No databases, no accounts, no cloud sync. Data lives in the browser.

## Architecture

```
index.html    -- Monolithic SPA (~4200 lines)
server.py     -- Python micro-server (~450 lines)
Docs/         -- Documentation and ADRs
```

See [State Management](STATE-MANAGEMENT.md) for how the app manages data flow.

## Making Changes

### Frontend (index.html)

The file is organized in three sections:
1. `<style>` -- All CSS, starting with `:root` variables
2. `<body>` -- HTML structure (header, nav, 8 tab panels, modals)
3. `<script>` -- All JavaScript (globals, helpers, renderers, event handlers, init)

When editing:
- Follow existing naming conventions (camelCase for JS, kebab-case for CSS)
- Use CSS custom properties (`var(--accent)`) for all colors
- Keep tab rendering functions self-contained
- Test all 8 tabs after changes

### Backend (server.py)

- Keep it as a single file
- No frameworks (no Flask, no Django)
- Handle errors gracefully and return JSON error responses
- Clean up temp files after upload processing

## Testing

Manual testing checklist:

1. Create a course manually via the wizard
2. Import a syllabus (PDF, DOCX, TXT)
3. Generate content for at least 2 modules
4. Take a quiz (MC only, then MC + written)
5. Use flashcards
6. Check all dashboard stats render correctly
7. Verify grade calculator math
8. Switch between multiple courses
9. Reload the page and confirm data persists
10. Test on mobile viewport (768px and below)

## Code Style

- No semicolons at line ends (match existing style)
- Template literals for HTML generation
- `let` over `var`, `const` where appropriate
- Descriptive function names: `renderDashboard`, `gradeWritten`, `autoFillFromText`
- No TypeScript, no JSDoc unless clarifying non-obvious logic

## What Not To Do

- Do not split `index.html` into multiple files
- Do not add npm, webpack, or any build tooling
- Do not add external CSS or JS libraries
- Do not add user authentication or server-side storage
- Do not add features beyond the current 8-tab scope without discussion
