# ADR-005: Python Micro-Server

## Status

Accepted

## Date

2026-01-18

## Context

Syllabot needs server-side capabilities for two features: parsing uploaded syllabus files (PDF/DOCX) and generating study content by scraping open-source textbooks. We needed to choose a backend approach.

Options considered:
1. **Node.js + Express** with npm packages for PDF/DOCX parsing
2. **Python + Flask/FastAPI** with a full web framework
3. **Python + `http.server`** as a minimal built-in server
4. **Serverless functions** (AWS Lambda, Cloudflare Workers)
5. **Browser-only** using client-side PDF.js and WASM-based parsing

## Decision

We chose option 3: a single `server.py` file (~450 lines) using Python's built-in `http.server` module with two POST endpoints.

## Rationale

- **Python is already installed** on most academic machines (macOS, Linux, university lab computers). No additional runtime needed.
- **Minimal dependencies**: Only two pip packages (`pdfplumber`, `python-docx`). No framework, no ORM, no middleware.
- **Single file**: The entire server is one file. No project structure, no config files, no `requirements.txt` (though one could be added).
- **Built-in static serving**: `SimpleHTTPRequestHandler` serves `index.html` and any other static files automatically. No routing configuration needed.
- **Matches the frontend philosophy**: Just as the frontend is one file with no build step, the backend is one file with no framework.
- **Easy to understand**: A student reading `server.py` sees raw HTTP handling -- `do_POST`, parse body, return JSON. No framework magic.

## Server Responsibilities

The server handles exactly two things:

### 1. File Upload (`POST /upload`)
- Accepts multipart form-data with a file attachment
- Parses PDF (pdfplumber), DOCX (python-docx), TXT (built-in), or JSON (built-in)
- Returns extracted text as JSON
- Cleans up temp files after parsing

### 2. Content Generation (`POST /generate`)
- Receives course info and module list
- Scrapes OpenStax textbook content via `urllib`
- Generates quiz questions, flashcards, and written questions using templates
- Returns structured JSON content

### What the server does NOT do:
- Store any data (stateless)
- Manage sessions or authentication
- Serve any purpose beyond these two endpoints
- Run in production (development server only)

## Trade-offs

### Accepted downsides
- **Not production-ready**: Python's `http.server` is single-threaded and not designed for concurrent users. Fine for single-student local use.
- **No WSGI/ASGI**: Cannot be deployed behind Gunicorn/Uvicorn without rewriting.
- **Custom multipart parsing**: Since Python's `cgi` module is deprecated in 3.13, we implement our own multipart form-data parser. This is fragile compared to a framework's parser.
- **No input validation framework**: Request validation is manual.
- **No async support**: Scraping multiple modules happens sequentially.

### Mitigations
- The server is only used locally by one student at a time. Concurrency is not a concern.
- CORS headers are added to all responses for cross-origin flexibility.
- The custom multipart parser handles the specific case we need (single file upload) reliably.
- If production deployment is ever needed, the two endpoint functions can be trivially wrapped in Flask or FastAPI.

## Consequences

- The server must be started manually (`python server.py`) before using upload or generation features.
- The server runs on port 8000 by default.
- All server-side logic must fit in one file.
- No middleware, no plugins, no extensions.
- Content generation quality is limited by template-based approaches (no AI/LLM involved server-side).
- Future enhancements (e.g., supporting more textbook sources) require modifying `server.py` directly.
