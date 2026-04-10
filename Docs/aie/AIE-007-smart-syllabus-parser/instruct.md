# Instruct — Smart Syllabus Parser

**AIE:** AIE-007

## Directive
> "make it so it automatically sets up modules and due dates based on the parsed document"

## Context Provided
- `index.html` — current `autoFillFromText()` at line ~3565, `addGradeWeightRow()`, `addModuleRow()`, `addDeadlineRow()` form helpers
- `eco114_course.json` — reference for what a correctly parsed syllabus looks like
- `server.py` — `parse_docx()` and `parse_pdf()` return raw text with `\t` for table cells and `\n` for rows

## Scope
**IN scope:**
- Rewrite `autoFillFromText()` to extract grade weights, modules, and deadlines
- Auto-populate all 4 form steps from parsed text
- Handle common syllabus formatting patterns (tables, bullet lists, numbered lists)

**OUT of scope:**
- Server-side changes
- OCR for scanned PDFs
- AI/LLM-based parsing
