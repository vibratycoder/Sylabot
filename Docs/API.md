# API Reference

The server exposes two POST endpoints alongside static file serving.

## POST /upload

Parses an uploaded syllabus file and returns its text content.

### Request

```
Content-Type: multipart/form-data
Body: file (binary) -- .pdf, .docx, .txt, or .json
```

### Response

For text-based files (PDF, DOCX, TXT):
```json
{
  "type": "text",
  "text": "Full extracted text content of the syllabus...",
  "filename": "syllabus.pdf"
}
```

For JSON files:
```json
{
  "type": "json",
  "data": { "...parsed JSON object..." },
  "filename": "course.json"
}
```

### File Processing

| Format | Parser | Notes |
|--------|--------|-------|
| `.pdf` | pdfplumber | Extracts text from all pages |
| `.docx` | python-docx | Extracts paragraph text |
| `.txt` | Built-in | Reads as UTF-8 text |
| `.json` | Built-in | Parses and returns JSON data |

### Error Response

```json
{
  "error": "Description of what went wrong"
}
```

Common errors:
- Unsupported file type
- File parsing failure
- Empty file content

---

## POST /generate

Generates study content (quizzes, written questions, flashcards) for course modules.

### Request

```json
{
  "course": "ECO 114 -- Microeconomic Principles",
  "modules": [
    { "num": 1, "topic": "Scarcity & Opportunity Cost", "reading": "Ch. 1" },
    { "num": 2, "topic": "Supply and Demand", "reading": "Ch. 3" }
  ],
  "types": {
    "quiz": true,
    "written": true,
    "flashcards": true
  }
}
```

| Field | Type | Description |
|-------|------|-------------|
| `course` | string | Course code and name |
| `modules` | array | Modules to generate content for |
| `modules[].num` | number | Module number |
| `modules[].topic` | string | Module topic name |
| `modules[].reading` | string | Associated reading (e.g., "Ch. 1") |
| `types` | object | Which content types to generate |

### Response

```json
{
  "quiz": {
    "Module 1: Scarcity & Opportunity Cost": [
      {
        "q": "Which best defines scarcity?",
        "opts": ["Option A", "Option B", "Option C", "Option D"],
        "correct": 0,
        "explain": "Explanation of the correct answer."
      }
    ]
  },
  "written": {
    "Module 1: Scarcity & Opportunity Cost": [
      {
        "q": "Explain scarcity and why it matters in economics.",
        "keywords": ["scarcity", "resources", "unlimited wants"],
        "idealAnswer": "Model answer text..."
      }
    ]
  },
  "flashcards": {
    "Module 1: Scarcity & Opportunity Cost": [
      {
        "front": "What is scarcity?",
        "back": "The condition where unlimited wants exceed limited resources."
      }
    ]
  }
}
```

Only requested content types are included in the response.

### Content Generation Pipeline

For each module, the server:

1. **Scrapes** topic information from OpenStax Principles of Economics 3e
2. **Extracts** key terms from scraped content (up to 15 terms)
3. **Generates** multiple-choice questions (up to 15 per module)
4. **Generates** flashcards (up to 12 per module)
5. **Generates** written questions (up to 3 per module)

---

## CORS

All responses include the following headers:

```
Access-Control-Allow-Origin: *
Access-Control-Allow-Methods: POST, GET, OPTIONS
Access-Control-Allow-Headers: Content-Type
```

## Static File Serving

All other requests are served as static files from the project directory using Python's `SimpleHTTPRequestHandler`. The root URL `/` serves `index.html`.
