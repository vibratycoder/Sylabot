# Align -- Python Micro-Server

**AIE:** AIE-001
**Date:** 2026-04-08
**Severity:** major
**Domain:** backend

## Problem
The application needs a backend server to handle two operations that cannot run in the browser: (1) parsing uploaded syllabus files (PDF/DOCX) using Python libraries, and (2) generating study content (quizzes, flashcards, written questions) by scraping OpenStax textbook pages and applying template-based generation.

## Decision
Build a single `server.py` file using Python's built-in `http.server` module. It serves static files and exposes two POST endpoints:

- **POST /upload** -- Accepts multipart/form-data file uploads (.pdf, .docx, .txt, .json). Uses `pdfplumber` for PDF extraction, `python-docx` for DOCX, built-in for TXT/JSON. Returns extracted text or parsed JSON.
- **POST /generate** -- Accepts JSON with course name, modules array, and content type flags. For each module: scrapes OpenStax Principles of Economics 3e, extracts up to 15 key terms, generates up to 15 MCQs (definition + application templates with 3 generic distractors), up to 12 flashcards (definition + importance pairs), and up to 3 written questions (explain, compare, real-world example). Returns structured JSON keyed by module.

CORS headers (`Access-Control-Allow-Origin: *`) on all responses. Runs on port 8000.

## Why This Approach
- Python's `http.server` requires zero external web framework dependencies (per ADR-005)
- `pdfplumber` and `python-docx` are the only pip dependencies needed
- Single-file server keeps the architecture minimal (per ADR-001)
- Template-based content generation avoids requiring an LLM API key for basic functionality
- OpenStax is open-source and freely accessible

## Impact
- Creates `server.py` in project root
- Requires `pip install pdfplumber python-docx`
- All frontend features that depend on file upload or content generation will call these endpoints
- Content quality is limited by template-based generation and OpenStax scraping reliability

## Success Criteria
- `python server.py` starts on port 8000 and serves `index.html` at `/`
- POST /upload correctly parses PDF, DOCX, TXT, and JSON files
- POST /generate returns valid quiz, flashcard, and written question JSON for a given module list
- CORS headers present on all responses
- Graceful error responses for unsupported file types and scraping failures
