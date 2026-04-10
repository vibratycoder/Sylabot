# Smart Syllabus Parser

The `autoFillFromText` function extracts structured course data from raw syllabus text. It uses a multi-strategy approach with regex patterns and fallbacks for resilience across different syllabus formats.

## Overview

The parser extracts four categories of information:
1. Course Info (code, name, instructor, semester, schedule, location)
2. Grade Weights (component names and percentages)
3. Modules (numbered topics with readings)
4. Deadlines (assignments with dates and types)

---

## 1. Course Info Extraction

### Course Code
```regex
/\b([A-Z]{2,4})\s*(\d{3}[A-Z]?)\b/
```
Matches patterns like `ECO 114`, `MATH 201B`, `CS 101`.

### Semester
```regex
/(?:Spring|Summer|Fall|Winter)\s+\d{4}/i
```
Matches `Spring 2026`, `Fall 2025`, etc.

### Instructor
```regex
/(?:Instructor|Professor|Prof\.|Dr\.)[:\s]+(.+)/i
```
Extracts the name following instructor-related titles.

### Schedule
```regex
/\b([MTWRF]{1,5})\s+(\d{1,2}:\d{2}\s*(?:AM|PM)?)\s*[-–]\s*(\d{1,2}:\d{2}\s*(?:AM|PM)?)/i
```
Matches patterns like `TF 9:35-10:50AM`, `MWF 1:00 PM - 2:15 PM`.

### Location
```regex
/\b([A-Z]{2,4})\s+(\d{2,4}[A-Z]?)\b/
```
Matched near contextual keywords like "room" or "building".

### Course Name
Extracted from the line containing the course code -- the remainder after the code pattern.

---

## 2. Grade Weight Extraction

### Strategy 1: Section-Based
Finds a section header containing "% of Grade", "Grading", or similar text, then scans lines within that section.

### Strategy 2: Pattern Matching
Four patterns are tried in order:

| Pattern | Example |
|---------|---------|
| Tab-separated | `Quizzes\t20%` |
| Space-separated | `Quizzes    20%` |
| Colon-separated | `Quizzes: 20%` |
| Parenthesized | `Quizzes (20%)` |

### Filtering
The parser removes false positives:
- Grade scale entries (e.g., `A = Excellent`)
- Names shorter than 3 characters
- Letter grade patterns

### Validation
- Minimum 2 weights required
- Total must be between 80% and 110%
- If section-based search fails, falls back to scanning all lines for `(\d{1,3})%`

---

## 3. Module Extraction

### Primary Pattern
```regex
/Module\s+(\d+)[:\s]+(.+)/i
```

### Fallback 1
```regex
/(?:Chapter|Week|Topic|Lesson|Unit)\s+(\d+)[:\s]+(.+)/i
```

### Fallback 2
```regex
/^\d+[\.\)]\s+(.+)/
```
Numbered list items.

### Reading Extraction
From the same line as the module:
```regex
/Ch\.?\s*\d+|Chapter\s+\d+|pp\.\s*\d+/i
```

### Post-Processing
- Deduplicate by module number
- Sort ascending by number

---

## 4. Deadline Extraction

### Date Formats Recognized
- `YYYY-MM-DD` (ISO format)
- `Month DD` (e.g., "February 14")
- `Month DD, YYYY` (e.g., "February 14, 2026")

### Type Classification

| Pattern | Assigned Type |
|---------|--------------|
| `/exam\|midterm\|final\|test/i` | `exam` |
| `/hw\|homework\|assignment\|problem set/i` | `hw` |
| `/paper\|presentation\|project\|essay/i` | `project` |
| `/read\|chapter/i` | `reading` |
| Everything else | `other` |

### Month Mapping
Full month names mapped to numbers: January = 1, February = 2, ... December = 12.

### Post-Processing
- Deduplicate by name + date
- Sort by date ascending
- Limit to 50 entries

---

## Design Principles

1. **Resilience** -- Multiple regex strategies with cascading fallbacks ensure parsing works across different syllabus formats (tables, paragraphs, lists).

2. **Validation** -- Grade weight totals are checked, modules are deduplicated, and false positives are filtered.

3. **Format agnostic** -- Handles tab-separated tables, paragraph-style descriptions, and mixed formatting.

4. **Conservative extraction** -- Prefers missing data over incorrect data. The user can always manually fill in gaps through the course wizard.
