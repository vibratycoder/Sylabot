# Align — PDF & Word Document Upload with Server-Side Parsing

**AIE:** AIE-004
**Date:** 2026-04-08
**Severity:** major
**Domain:** frontend + backend

## Problem
The file upload currently only supports .txt and .json files parsed client-side. Students typically receive syllabi as .pdf or .docx files. The user explicitly requested: "make it primarily compatible with PDF and Word documents."

Client-side JavaScript cannot parse .docx (ZIP format containing XML) or .pdf (binary format) natively. A server-side component is required.

## Decision
Build a lightweight Python HTTP server that:

1. **Serves static files** (existing functionality via `http.server`)
2. **Exposes a `/upload` POST endpoint** that accepts .pdf and .docx files
3. **Parses the document** server-side using `python-docx` (already installed) and `PyPDF2`/`pdfplumber` for PDFs
4. **Extracts raw text** and returns it to the client as JSON
5. **Client pre-fills the manual form** with extracted text, allowing the user to review and correct before saving

### Server: `server.py`
- Custom `HTTPRequestHandler` subclass
- GET requests → serve static files (same as `http.server`)
- POST `/upload` → accept multipart file, parse, return `{ text: "...", filename: "..." }`
- Runs on port 8080

### Client changes in `index.html`:
- Upload area accepts `.pdf, .docx, .doc, .json, .txt`
- On file select, POST to `/upload` for .pdf/.docx files
- Display extracted text in a preview area
- Auto-populate form fields where detectable (course name, instructor, dates)
- Keep JSON and manual entry as fallbacks

## Why This Approach
- **Server-side parsing is mandatory** — no reliable client-side .docx/.pdf parsing exists without massive libraries (pdf.js is 500KB+, JSZip+XML parsing is fragile)
- **python-docx already installed** from the initial syllabus parse at the start of this conversation
- **Lightweight custom server** — just one Python file, no Flask/Django dependency
- **Text extraction, not AI parsing** — returns raw text for the user to review. Avoids hallucinating course structure from ambiguous syllabi.
- **Alternative considered:** pdf.js client-side — rejected, too large and unreliable for complex PDFs with tables
- **Alternative considered:** Full NLP parsing to auto-fill all fields — rejected, too error-prone. Better to show extracted text and let the user fill the form.

## Impact
- **New file:** `server.py` — custom HTTP server (~80 lines)
- **New dependency:** `pdfplumber` (pip install)
- **Modified:** `index.html` — upload area accepts new file types, POSTs to `/upload`, shows extracted text preview
- **Server process change:** Must run `python server.py` instead of `python -m http.server 8080`
- **Risk:** Low. The static file serving is identical. The upload endpoint is additive. If parsing fails, the user still has JSON paste and manual entry.

## Success Criteria
- User can upload a .docx file and see extracted text
- User can upload a .pdf file and see extracted text
- Extracted text is shown in a preview area for the user to review
- User can then manually fill in the course form using the extracted text as reference
- .json files still auto-import as before
- Server starts with a single `python server.py` command
