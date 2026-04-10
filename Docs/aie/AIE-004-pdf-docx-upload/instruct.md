# Instruct — PDF & Word Document Upload with Server-Side Parsing

**AIE:** AIE-004

## Directive
> "to the file upload make it primarily compatible with PDF and Word documents"

## Context Provided
- `index.html` — current app with file upload area accepting .txt/.json
- `python-docx` already installed (used to parse ECO 114 syllabus at start of session)
- Python 3 available on the system
- Server currently runs via `python -m http.server 8080`

## Scope
**IN scope:**
- `server.py` — custom HTTP server with static file serving + POST `/upload`
- Install `pdfplumber` for PDF parsing
- Update `index.html` upload area to accept .pdf/.docx, POST files to server, show extracted text preview
- Kill old server, start new server

**OUT of scope:**
- AI-powered auto-parsing of syllabus structure (fields, dates, weights)
- OCR for scanned PDFs (text-based PDFs only)
