# ADR-001: Monolithic Single-File Architecture

## Status

Accepted

## Date

2026-01-15

## Context

Syllabot is a study companion tool targeting students who need to quickly set up and use the app without technical overhead. We needed to decide how to structure the frontend codebase.

Options considered:
1. **Component-based SPA framework** (React, Vue, Svelte) with a build pipeline
2. **Multi-file vanilla JS** with separate HTML, CSS, and JS files linked via `<script>` and `<link>` tags
3. **Single monolithic HTML file** containing all HTML, CSS (`<style>`), and JavaScript (`<script>`) inline

## Decision

We chose option 3: a single `index.html` file (~4200 lines) containing all frontend code.

## Rationale

- **Zero build step**: No npm, no webpack, no Vite. The file runs as-is in any browser. This eliminates an entire class of tooling issues for contributors and deployers.
- **Instant portability**: The app can be shared as a single file. Copy it to a USB drive, email it, or host it on any static server.
- **No dependency management**: No `package.json`, no `node_modules`, no version conflicts. The app will work identically in 5 years without maintenance.
- **Simplicity for the target audience**: Students and educators can open one file, read the code, and understand the entire application.
- **Fast load**: A single file means one HTTP request. No waterfall of CSS/JS/font downloads.

## Trade-offs

### Accepted downsides
- **File is large** (~4200 lines). Navigation requires a good editor with search/fold.
- **No code splitting**: The entire app loads even if the user only needs one tab.
- **No hot module replacement**: Development requires full page reloads.
- **Merge conflicts**: Multiple contributors editing the same file increases conflict risk.

### Mitigations
- The file is organized in clearly separated sections (CSS, HTML, JS) with comment headers.
- Tab rendering functions are self-contained, making it easy to find and modify specific functionality.
- The app is small enough that full-page load is nearly instant anyway.

## Consequences

- All new frontend features must be added to `index.html`.
- No CSS preprocessors (Sass, Less) or JS transpilers (TypeScript, Babel) can be used.
- Testing is manual (no Jest, no Cypress) since there is no module system to import from.
- The project cannot use npm packages on the frontend.
