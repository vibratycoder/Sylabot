# Align -- State Management & Data Layer

**AIE:** AIE-003
**Date:** 2026-04-08
**Severity:** major
**Domain:** frontend

## Problem
The app needs a way to persist course data across page reloads (using localStorage per ADR-002), manage global JavaScript state for the active course, and implement lazy tab rendering so tabs only re-render when their data changes.

## Decision
Implement in the `<script>` section of `index.html`:

1. **Global Variables** -- `activeCourse`, `activeContent`, `activeDeadlines`, `activeModules`, `activeGradeWeights`, quiz state vars (`currentQuizModule`, `quizAnswered`, `quizCorrect`, `quizTotalMC`, `writtenCount`, `writtenGraded`, `writtenPoints`, `quizHistory`), flashcard state (`currentFCModule`, `fcIndex`), form state (`gwRowCount`, `modRowCount`, `dlRowCount`, `currentFormStep`), rendering state (`_dirtyTabs`).

2. **localStorage Helpers** -- `getAllCourses()`, `saveCourses(arr)`, `getCourseContent(id)`, `setCourseContent(id, c)`. Keys namespaced by course ID: `syllabot_courses`, `syllabot_activeCourse`, `syllabot_content_${courseId}`, `syllabot_${courseId}_quizHistory`, `syllabot_${courseId}_mod-${moduleNum}`.

3. **Course ID Generation** -- `code.toLowerCase().replace(/\s/g,'') + '-' + semester.toLowerCase().replace(/\s/g,'')`.

4. **Lazy Tab Rendering** -- `TAB_RENDERERS` map, `_dirtyTabs` object, `renderTabIfDirty(tabName)`. On course load, all tabs marked dirty. Dashboard always renders immediately.

5. **Initialization Sequence** -- On DOMContentLoaded: set date, attach event listeners, call `loadActiveCourse()` which loads from localStorage, sets globals, marks tabs dirty, renders dashboard, and checks if `activeContent` is empty -- if so, automatically triggers content generation via POST /generate for all modules (see AIE-005).

6. **Utility Functions** -- `daysUntil(dateStr)`, `shuffleArray(arr)`, content accessors (`getQuiz`, `getWritten`, `getFlashcards`).

## Why This Approach
- Global variables are appropriate for a single-file SPA with no module system (ADR-001)
- localStorage is the chosen persistence layer (ADR-002)
- Lazy rendering avoids unnecessary DOM updates when switching between courses
- Course ID namespacing ensures multi-course data isolation

## Impact
- Adds ~150 lines of JavaScript to `index.html`
- All feature tabs (AIE-005 through AIE-012) depend on this data layer
- `loadActiveCourse()` is the central function that hydrates the entire app

## Success Criteria
- Courses persist across page reloads via localStorage
- Switching courses resets all global state and marks tabs dirty
- Lazy rendering only fires tab renderers when tabs are dirty and visible
- Multiple courses can coexist without data leakage between them
