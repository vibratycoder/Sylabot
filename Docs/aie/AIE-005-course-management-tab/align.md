# Align -- Course Management Tab

**AIE:** AIE-005
**Date:** 2026-04-08
**Severity:** major
**Domain:** frontend

## Problem
Users need to create, view, switch between, and delete courses. They also need to import syllabi (via file upload to the server) and trigger content generation. This is the entry point for all course data.

## Decision
Implement the Courses tab (Tab 8) in `index.html`:

1. **Course Grid** -- Responsive grid (`repeat(auto-fill, minmax(280px, 1fr))`). Each card shows: color dot (from 10-color COURSE_COLORS palette), code, name, instructor, schedule, location, semester, module/deadline counts. Active course gets purple border with box-shadow glow. Click to switch, delete button per card.

2. **Add Course Options** -- Two buttons: "Add Manually" (opens wizard), "Import Syllabus" (shows upload area).

3. **Course Creation Wizard** -- 4-step modal: Step 0 (course info fields), Step 1 (grade weights with dynamic add/remove rows, validates total), Step 2 (modules with dynamic rows), Step 3 (deadlines with dynamic rows and type dropdown). Step indicators at top. Navigation via indicators and prev/next buttons. On save: generate course ID, assign color, save to localStorage, load as active.

4. **File Upload** -- Drag-and-drop zone + file input. Sends file to POST /upload, receives text, calls `autoFillFromText()` (AIE-004), populates wizard fields.

5. **Auto Content Generation** -- Whenever a course becomes the active course (on creation, on import, or on switching to it from the course grid), check if `activeContent` is empty for that course. If it is, automatically POST all modules to /generate in the background. Show a loading indicator ("Generating content...") in the active tab area. On success, merge returned content (quiz, written, flashcards, tutor) into `activeContent`, save to localStorage, and mark all tabs dirty so they pick up the new content. On failure, show a non-blocking error with a retry option. No manual button, no modal, no module selection -- generation is fully automatic and triggered by `loadActiveCourse()`.

## Why This Approach
- Grid layout provides clear visual overview of all courses
- 4-step wizard breaks complex data entry into digestible steps
- Dynamic rows let users add arbitrary numbers of weights/modules/deadlines
- File upload + auto-fill reduces manual data entry significantly
- Auto-generation removes a manual step -- users don't have to know content generation exists; it just happens
- Generating all modules by default ensures complete content coverage without requiring user decisions

## Impact
- Adds ~300 lines of JavaScript + HTML to `index.html`
- Depends on AIE-001 (server endpoints), AIE-003 (state management), AIE-004 (parser)
- Creates the course data that all other tabs consume
- Color assignment and ID generation defined here

## Success Criteria
- Course grid renders all saved courses with correct info and colors
- Wizard validates grade weight totals before allowing save
- File upload correctly triggers server parsing and auto-fills wizard
- Activating any course with no content automatically triggers generation for all modules
- Loading indicator visible while generation is in progress
- Content (quiz, written, flashcards, tutor) available in all tabs after generation completes
- Generation skips silently if content already exists for the active course
- Generation failure shows a non-blocking error with retry option
- Switching courses updates the header badge and marks all tabs dirty
- Deleting a course removes it from localStorage and grid
