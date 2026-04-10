# Align — Smart Syllabus Parser: Auto-extract grades, modules, and deadlines from uploaded documents

**AIE:** AIE-007
**Date:** 2026-04-08
**Severity:** major
**Domain:** frontend

## Problem
When a PDF or DOCX syllabus is uploaded, the app only auto-fills 5 basic fields (course code, name, semester, instructor, schedule/location) using simple regex. The user must still **manually** enter:

- Grade weights (e.g., "Midterm 30%, Final 40%, Homework 15%")
- Modules/topics (e.g., "Module 1: Supply & Demand, Module 2: Elasticity")
- Deadlines (e.g., "Unit 1 Exam — Feb 20", "Homework due Mar 6")

This defeats the purpose of document upload — the whole point is to avoid manual entry.

## Decision
Rewrite `autoFillFromText()` in `index.html` to comprehensively parse extracted syllabus text and auto-populate all four form steps:

**Step 1 — Course Info** (improve existing):
- Better course code detection (handle "ECO113-I", "FIN 201", "ACC 310")
- Better instructor detection (handle "Prof.", "Dr.", name before/after colon)
- Detect course title even when on separate lines from the code

**Step 2 — Grade Weights** (new):
- Detect percentage patterns: "Midterm Exam 30%", "Final: 25%", "Homework (15%)"
- Detect table rows: "In-Class Activities & Discussion\t10"
- Auto-populate the grade weights form rows

**Step 3 — Modules/Topics** (new):
- Detect "Module N:", "Chapter N:", "Week N:", "Unit N:" patterns
- Detect topic names after module numbers
- Detect reading assignments ("Ch. 1", "Chapter 3", etc.)
- Auto-populate the modules form rows

**Step 4 — Deadlines** (new):
- Detect date patterns: "2026-02-20", "Feb 20", "February 20, 2026"
- Associate dates with event names (exams, homework, presentations)
- Classify type (exam, assignment, project, other)
- Auto-populate the deadlines form rows

## Why This Approach
- **All client-side** — no server changes needed; the text is already extracted
- **Regex-based heuristics** — syllabi have common patterns that are reliably detectable
- **Progressive enhancement** — auto-fill is best-effort; user can still edit/correct any field
- **Populates the actual form** — user sees what was detected and can fix mistakes before saving

## Impact
- **Modified:** `index.html` — rewrite `autoFillFromText()`, add helper functions for grade/module/deadline extraction
- **No server changes** — parsing already returns clean text
- **No breaking changes** — existing manual entry still works; auto-fill just pre-populates

## Success Criteria
- Upload the ECO 114 syllabus .docx → all 4 form steps auto-populated correctly
- Grade weights detected and summing to ~100%
- Modules with topic names and readings detected
- Key deadlines (exams, homework) with correct dates detected
- User can review and edit any auto-filled data before saving
