# Instruct — Multi-Syllabus Storage & Course Switcher

**AIE:** AIE-003

## Directive
> "now create a tab that allows you to switch between the syllibi as well as a part that says 'new class' that allows you to upload a new syllabus"

User wants a dedicated tab (not just a header dropdown) for managing courses — switching between them and adding new ones via file upload.

## Context Provided
- `index.html` — current monolithic single-course app
- ECO 114 hardcoded as constants (DEADLINES, MODULES, GRADE_COMPONENTS, QUIZ_DATA, etc.)
- Python 3 available with python-docx installed for .docx parsing
- User previously uploaded a .docx syllabus that was parsed server-side

## Scope
**IN scope:**
- New "Courses" tab in the tab nav
- Course list view showing all stored courses with switch functionality
- "New Class" section with file upload (.docx, .pdf, .txt) and manual entry form
- localStorage persistence for multiple courses
- All existing tabs read from active course data dynamically
- ECO 114 pre-seeded as default course

**OUT of scope:**
- Server-side syllabus parsing (would require a backend — use manual entry + JSON paste for now)
- AIE-001 formatting standardization (separate entry)
- AIE-002 file splitting (separate entry)
