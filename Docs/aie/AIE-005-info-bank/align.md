# Align — INFO Bank: Comprehensive Question & Flashcard Data for ECO 114

**AIE:** AIE-005
**Date:** 2026-04-08
**Severity:** major
**Domain:** frontend + backend

## Problem
The app currently has quiz questions, written questions, and flashcards hardcoded directly inside `index.html` as JavaScript objects (`QUIZ_DATA`, `WRITTEN_DATA`, `FLASHCARD_DATA`). This has three issues:

1. **Limited content** — only ~10 MC questions per module, ~5 written questions, and ~120 flashcards total. Not enough for meaningful study variety.
2. **No separation of data from code** — adding/editing questions requires modifying the 3,200-line `index.html`, increasing risk of breaking the app.
3. **No structured data file** — no way to import, export, or programmatically generate question banks.

## Decision
Create a `data/` folder with a comprehensive `INFO_Bank.json` file containing:

- **~150 multiple-choice questions** across all 13 modules + comprehensive review (10-12 per module)
- **~70 written/free-response questions** with ideal answers and grading keywords (5 per module)
- **~140 flashcards** with front/back pairs (8-12 per module)
- **~30 worked examples** with step-by-step solutions (2-3 per module)

A Python build script (`data/build_bank.py`) will generate the JSON to avoid shell quoting issues with the large dataset.

Then modify `index.html` to:
- Fetch `data/INFO_Bank.json` on load
- Replace hardcoded `QUIZ_DATA`, `WRITTEN_DATA`, and `FLASHCARD_DATA` with data loaded from the bank
- Fall back to existing hardcoded data if the fetch fails

## Why This Approach
- **JSON data file** separates content from code — can be edited, validated, and versioned independently
- **Python build script** avoids shell escaping nightmares with hundreds of questions containing quotes and special characters
- **Fetch with fallback** ensures the app still works if served without the data folder or if the fetch fails
- **All 13 modules + review** covers the complete ECO 114 curriculum for real exam prep value

Alternatives considered:
- Inline expansion of existing JS objects — rejected because it would bloat `index.html` even further
- Multiple JSON files per module — rejected as unnecessary complexity for this scale; one file is manageable
- Database (SQLite/Supabase) — rejected as overkill for a static study tool

## Impact
- **New files:** `data/INFO_Bank.json`, `data/build_bank.py`
- **Modified:** `index.html` (data loading logic, replacement of hardcoded question objects)
- **No breaking changes** — fallback ensures existing behavior is preserved
- `server.py` already serves static files from the project directory, so `data/INFO_Bank.json` is automatically accessible

## Success Criteria
- `data/INFO_Bank.json` exists with valid JSON containing all 13 modules + comprehensive review
- Each module has: 10+ MC questions, 5+ written questions, 8+ flashcards, 2+ worked examples
- `index.html` loads data from the bank file on startup
- Quiz tab generates questions from the bank data
- Flashcard tab uses bank flashcards
- If `INFO_Bank.json` is unreachable, the app falls back to existing hardcoded data gracefully
