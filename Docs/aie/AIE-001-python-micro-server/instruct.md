# Instruct -- Python Micro-Server

**AIE:** AIE-001

## Directive

> "Build server.py in the project root. Use Python's http.server module. Serve static files from the project directory on port 8000. Add CORS headers (Access-Control-Allow-Origin: *) to all responses. Implement two POST endpoints:
>
> POST /upload -- Accept multipart/form-data file upload. Use pdfplumber for .pdf, python-docx for .docx, built-in for .txt and .json. Return JSON with type, text/data, and filename. Return error JSON on failure.
>
> POST /generate -- Accept JSON body with course name, modules array (num, topic, reading), and types object (quiz, written, flashcards booleans). For each module: scrape OpenStax Principles of Economics 3e by chapter number, extract up to 15 key terms, generate up to 15 MCQs using definition/application templates with 3 generic distractors, up to 12 flashcards (definition + importance), up to 3 written questions (explain, compare, real-world). Return structured JSON keyed by 'Module N: Topic' strings. Include tutor HTML content in the response as well."

## Context Provided

- Docs/API.md -- Full endpoint specs, request/response formats
- Docs/CONTENT-GENERATION.md -- Pipeline details, templates, scraping source
- Docs/QUIZ-SYSTEM.md -- Question format, keyword/grading structure
- Docs/DATA-MODEL.md -- Content object structure
- Docs/SETUP.md -- Dependencies (pdfplumber, python-docx)

## Scope

**In scope:**
- server.py with static file serving, CORS, /upload, /generate
- scrape_topic_info, extract_key_terms, generate_mcq, generate_flashcards, generate_written, generate_tutor_html
- Error handling for unsupported files, scraping failures, empty content

**Out of scope:**
- Frontend code (AIE-002+)
- Any database or auth
