# Syllabot

A dark-mode, single-page study companion that lets students import any course syllabus (PDF/DOCX/TXT), auto-extracts grades, modules, and deadlines via a smart parser, generates quizzes/flashcards/written questions from module topics, and tracks progress across unlimited courses.

## Features

- **Syllabus Import** -- Upload PDF, DOCX, or TXT syllabi and auto-extract course info, grade weights, modules, and deadlines
- **Quiz Engine** -- Multiple-choice and written questions with heuristic grading, per-module question pools, shuffled each attempt
- **Flashcards** -- 3D CSS flip cards with per-module navigation
- **Tutor View** -- Rich HTML study content organized by module
- **Grade Calculator** -- Real-time weighted grade computation with "What do I need on the final?" projections
- **Progress Tracker** -- Module completion, risk analysis, and recommendations
- **Planner** -- Weekly deadline view with urgency badges
- **Multi-Course Support** -- Unlimited courses, each fully isolated in localStorage

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Single `index.html` -- vanilla HTML5 + CSS3 + ES6 JavaScript |
| Backend | Single `server.py` -- Python 3 `http.server` |
| Storage | Browser `localStorage` |
| Charts | Canvas 2D API (hand-drawn) |
| File Parsing | `pdfplumber`, `python-docx` |
| Content Scraping | `urllib` -- OpenStax textbooks |

## Quick Start

```bash
# Install Python dependencies
pip install pdfplumber python-docx

# Start the server
python server.py

# Open in browser
# http://localhost:8000
```

## Project Structure

```
project/
  index.html      -- Monolithic SPA (HTML + CSS + JS all inline)
  server.py       -- Python micro-server (static files + 2 API endpoints)
  Docs/           -- Documentation
    adr/          -- Architecture Decision Records
```

## Documentation

- [Setup Guide](SETUP.md)
- [API Reference](API.md)
- [Data Model](DATA-MODEL.md)
- [UI Guide](UI-GUIDE.md)
- [Design System](DESIGN-SYSTEM.md)
- [Syllabus Parser](PARSER.md)
- [Quiz System](QUIZ-SYSTEM.md)
- [Content Generation](CONTENT-GENERATION.md)
- [State Management](STATE-MANAGEMENT.md)
- [Contributing](CONTRIBUTING.md)

## Architecture Decisions

- [ADR-001: Monolithic Single-File Architecture](adr/ADR-001-monolithic-single-file.md)
- [ADR-002: localStorage Over Database](adr/ADR-002-localstorage-over-database.md)
- [ADR-003: No External Dependencies](adr/ADR-003-no-external-dependencies.md)
- [ADR-004: Heuristic Written Grading](adr/ADR-004-heuristic-written-grading.md)
- [ADR-005: Python Micro-Server](adr/ADR-005-python-micro-server.md)

## License

Educational project. Not licensed for redistribution.
