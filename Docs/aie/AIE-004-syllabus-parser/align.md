# Align -- Smart Syllabus Parser

**AIE:** AIE-004
**Date:** 2026-04-08
**Severity:** major
**Domain:** frontend

## Problem
Users need to upload a syllabus file and have the app automatically extract course info (code, name, instructor, semester, schedule, location), grade weights, modules, and deadlines -- rather than entering everything manually. The parser must handle diverse syllabus formats (tables, paragraphs, lists).

## Decision
Implement `autoFillFromText(text)` in `index.html` that uses regex-based multi-strategy extraction:

1. **Course Info** -- Regex for course code (`/\b([A-Z]{2,4})\s*(\d{3}[A-Z]?)\b/`), semester (`/(?:Spring|Summer|Fall|Winter)\s+\d{4}/i`), instructor (`/(?:Instructor|Professor|Prof\.|Dr\.)[:\s]+(.+)/i`), schedule (`/\b([MTWRF]{1,5})\s+(\d{1,2}:\d{2}\s*(?:AM|PM)?)\s*[-]\s*(\d{1,2}:\d{2}\s*(?:AM|PM)?)/i`), location, and course name from the code's line.

2. **Grade Weights** -- Two strategies: section-based (find "Grading" header, scan lines) and pattern matching (tab/space/colon/parenthesis separated). Filter false positives (grade scale entries, short names). Validate: min 2 weights, total 80-110%.

3. **Modules** -- Primary pattern (`/Module\s+(\d+)[:\s]+(.+)/i`), fallback to Chapter/Week/Topic/Lesson/Unit, then numbered lists. Extract readings from same line. Deduplicate and sort.

4. **Deadlines** -- Recognize ISO, "Month DD", "Month DD, YYYY" date formats. Classify type (exam/hw/project/reading/other). Deduplicate by name+date, sort by date, limit to 50.

## Why This Approach
- Client-side parsing keeps text extraction local (server only handles binary file decoding)
- Multi-strategy with fallbacks maximizes compatibility across syllabus formats
- Conservative extraction (prefer missing over incorrect) lets users manually fix gaps via wizard
- No AI/NLP dependency keeps it working offline

## Impact
- Adds ~200 lines of JavaScript to `index.html`
- Called after file upload response from server (AIE-001)
- Populates the course creation wizard (AIE-005) with extracted data
- Parser quality directly affects the first-run experience

## Success Criteria
- Correctly extracts course code, name, semester from standard syllabus text
- Finds grade weights in both table and paragraph formats
- Extracts modules with readings from numbered/labeled lists
- Identifies deadlines with dates and classifies their types
- Returns empty/partial results gracefully rather than crashing on unusual formats
