# Execute — PDF & Word Document Upload with Server-Side Parsing

**AIE:** AIE-004

## Files Changed

| File | Action | What Changed |
|------|--------|-------------|
| `server.py` | created | Custom HTTP server with static file serving + POST `/upload` endpoint. Parses .docx via python-docx, .pdf via pdfplumber, .json/.txt natively. Manual multipart parser (cgi module removed in Python 3.13+). |
| `index.html` | modified | Upload area accepts `.pdf,.docx,.doc,.json,.txt`. File upload POSTs to `/upload` endpoint. Added extracted text preview area. Added `autoFillFromText()` that regex-detects course code, semester, instructor, schedule, location from extracted text. |

## Outcome
Implementation matches align.md plan.

- .docx upload tested with the original ECO 114 syllabus — 30,884 chars extracted including all tables
- .pdf parsing implemented via pdfplumber with table extraction
- .json files auto-populate the JSON import area
- .txt files show in the preview area
- Auto-fill detects common patterns: course code (e.g., "ECO 114"), semester ("Spring 2026"), instructor ("Instructor: Name"), schedule, location
- Extracted text shown in a readonly textarea for user review
- Manual form stays available below for structured entry

**Surprise:** Python 3.14 removed the `cgi` module entirely. Had to write a manual multipart/form-data parser instead. Works correctly.

## Side Effects
- Server must now be started with `python server.py` instead of `python -m http.server 8080`
- `pdfplumber` installed as new dependency (pulls in pdfminer.six, pypdfium2, cryptography)

## Tests
- [x] .docx upload — 30,884 chars extracted from ECO 114 syllabus
- [x] Static file serving still works on port 8080
- [x] CORS headers present on responses
- [ ] .pdf upload — pdfplumber installed, endpoint coded, needs manual test with a PDF file
- [ ] Auto-fill detection accuracy on varied syllabus formats

## Follow-Up Required
- [ ] Future AIE: OCR support for scanned PDFs (currently text-based only)
- [ ] Future AIE: More robust auto-fill with better regex patterns for varied syllabus formats
