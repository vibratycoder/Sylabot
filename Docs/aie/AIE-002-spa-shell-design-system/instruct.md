# Instruct -- SPA Shell & Design System

**AIE:** AIE-002

## Directive

> "Create index.html in the project root. Single file, no external dependencies. Include:
>
> 1. Inline CSS with :root custom properties for the full dark-mode color palette (--bg:#0f1117, --surface:#1a1d27, --surface2:#232736, --border:#2e3346, --text:#e2e4eb, --text-dim:#8b8fa3, --accent:#6c5ce7, --accent-light:#a29bfe, --green:#00b894, --yellow:#fdcb6e, --red:#e17055, --orange:#f39c12, --blue:#74b9ff). Font stack: Segoe UI, system-ui, -apple-system, sans-serif. Component classes: .card, .stat-card, .badge (with variants: urgent/soon/upcoming/later/done/exam), .topic-btn, .quiz-opt, .grade-input-row. Animations: fadeIn keyframes, flashcard 3D flip. Responsive breakpoint at 768px.
>
> 2. HTML structure: fixed header with logo text 'Syllabot', course badge span, and formatted date. 8-tab nav bar with Unicode icons. 8 tab content div panels (dashboard, planner, tutor, quiz, flashcards, progress, grades, courses). Course creation wizard modal (4 steps). File upload area with drag-and-drop.
>
> 3. Inline JS: tab switching click handler that shows/hides panels and updates active nav state. Dashboard visible by default."

## Context Provided

- Docs/DESIGN-SYSTEM.md -- Full color palette, typography, component specs, animations
- Docs/UI-GUIDE.md -- Layout structure, tab descriptions, all 8 tabs
- Docs/README.md -- Tech stack confirmation (single index.html)

## Scope

**In scope:**
- Complete CSS design system
- HTML skeleton for all 8 tabs (empty content areas)
- Tab switching JS
- Wizard modal structure (4 steps with indicators)
- Upload area HTML

**Out of scope:**
- Tab content rendering logic (AIE-003 through AIE-012)
- State management (AIE-003)
- Parser logic (AIE-004)
