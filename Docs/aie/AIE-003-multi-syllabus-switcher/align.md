# Align — Multi-Syllabus Storage & Course Switcher

**AIE:** AIE-003
**Date:** 2026-04-08
**Severity:** major
**Domain:** frontend

## Problem
The application currently hardcodes a single course (ECO 114). A student taking multiple courses has no way to:
- Add additional syllabi
- Switch between courses
- Have each course maintain its own independent data (quizzes, progress, grades, history)
- Persist course data across sessions

The user requested: "add a section so you can change what syllabus you are trying to look at as well as storing the information, and switching between the different sections."

## Decision
Build a multi-course system with three components:

### 1. Course Switcher (Header Dropdown)
- Replace the static "ECO 114" badge in the header with a clickable course selector dropdown
- Shows all stored courses with color-coded dots
- Active course is highlighted
- "Add New Course" button at the bottom of the dropdown

### 2. Add Course Modal
- Full-screen modal overlay triggered from the dropdown or first-run
- Form fields: Course Name, Course Code, Instructor, Schedule (days/time), Location, Semester
- Sections to add: grade weights (dynamic rows), modules/topics (dynamic rows with dates), deadlines/assignments (dynamic rows with dates and types)
- "Import from JSON" option — paste raw JSON to bulk-load a course
- On save, course is stored in localStorage and becomes the active course

### 3. Per-Course Data Isolation
- All localStorage keys become namespaced: `syllabot_{courseId}_quizHistory`, `syllabot_{courseId}_modules`, etc.
- Switching courses reloads all tab data (deadlines, modules, quiz history, progress, grade inputs) from that course's namespace
- Each course gets a unique ID generated on creation
- Course metadata stored in `syllabot_courses` (array of {id, name, code, color})
- Active course ID stored in `syllabot_activeCourse`

### Data Structure (localStorage)
```
syllabot_courses        → [{id, code, name, instructor, schedule, location, semester, color, gradeWeights, modules, deadlines}]
syllabot_activeCourse   → "eco114-spring2026"
syllabot_eco114_quizHistory  → [...]
syllabot_eco114_modules      → {mod-1: "done", ...}
syllabot_eco114_grades       → {exam1: 85, ...}
```

### UI Flow
1. First visit with no courses → modal opens automatically to add first course
2. ECO 114 is pre-loaded as a default course (migrated from current hardcoded data)
3. Header shows: `SYLLABOT | [dropdown: ECO 114 ▾]  | April 8, 2026`
4. Clicking dropdown shows all courses + "Manage Courses" link
5. "Manage Courses" opens a dedicated settings panel where you can edit/delete courses

## Why This Approach
- **localStorage** — keeps it fully client-side, no backend needed. Data persists across sessions.
- **Namespace isolation** — prevents quiz history from one course bleeding into another.
- **Pre-load ECO 114** — user doesn't lose their existing course; it migrates automatically.
- **Modal for adding** — keeps the main UI clean. Course management is an occasional action, not a constant one.
- **Alternative considered:** Separate HTML pages per course — rejected because it duplicates the entire app and makes updates painful.
- **Alternative considered:** File upload for syllabus — rejected for now (can be added later). Manual entry + JSON import covers the use case.

## Impact
- **index.html** — header modified (dropdown), modal HTML added, all JS data references refactored to read from active course
- **All tab JS** — every `renderX()` function must read from the active course's data instead of hardcoded constants
- **localStorage** — new key structure. Existing `quizHistory` and `mod-*` keys migrated to namespaced versions.
- **Risk:** Medium-high. Every tab currently reads from global `const` objects (DEADLINES, MODULES, etc.). These must become dynamic reads from the active course. If any tab still references the old constants, it will show stale/wrong data.

## Success Criteria
- User can add a new course via the modal with name, code, weights, modules, deadlines
- User can switch between courses via the header dropdown
- Each course has independent quiz history, progress, and grade data
- ECO 114 data is preserved and accessible after the refactor
- Refreshing the page remembers the last active course
- Deleting a course removes all its associated data
- All 7 tabs update immediately when switching courses
