# Syllabot Knowledge Base

Local content repository for generating quizzes, flashcards, written questions, and tutor material. Structured around Bryant University's course catalog.

## Directory Structure

```
content/
  {subject}/
    _subject.md          -- Subject metadata and overview
    {course-area}/       -- Optional subdirectory for large subjects
      _course.md         -- Course-area metadata
      chNN-slug.md       -- Chapter/topic content files
    chNN-slug.md         -- Chapter/topic content files (if no subdirectory needed)
```

## Chapter File Format

Every chapter file uses YAML frontmatter + consistent markdown sections:

```markdown
---
chapter: 3
title: Supply and Demand
subject: economics
course: microeconomics
prefix: ECO
code: "114"
keywords: [supply, demand, equilibrium, shortage, surplus]
prereqs: [ch01, ch02]
---

# Title

## Overview
2-3 paragraph summary of the chapter's core ideas.

## Key Terms
- **Term**: Definition
- **Term**: Definition

## Core Concepts
### Concept Name
Explanation with enough depth for quiz and tutor generation.

## Examples
### Example Title
Real-world example that can be turned into application questions.

## Relationships
- Concept A -> Concept B: how they connect
- Concept C -> Concept D: cause and effect

## Common Misconceptions
- Misconception: Why it's wrong and what's correct

## Practice Angles
- Compare and contrast: term A vs term B
- Explain with example: concept
- Cause and effect: if X then Y
```

## How server.py Uses These Files

1. Receives module topic + reading from `/generate` request
2. Matches against chapter files by keyword/chapter number/title fuzzy match
3. Parses frontmatter and sections
4. Key Terms -> MCQ generation + flashcard generation
5. Core Concepts + Examples -> written question generation
6. Overview + Key Terms + Examples -> tutor HTML generation
7. Falls back to OpenStax scraping only if no local match found

## Adding New Content

1. Create a new `.md` file in the appropriate subject folder
2. Follow the chapter file format above
3. Include at least: frontmatter, Key Terms (5+), Core Concepts (3+), Examples (2+)
4. The server picks up new files automatically on next `/generate` request

## Bryant University Course Prefixes

| Prefix | Subject | Directory |
|--------|---------|-----------|
| ECO | Economics | economics/ |
| FIN | Finance | finance/ |
| ACG | Accounting | accounting/ |
| MKT | Marketing | marketing/ |
| MGT | Management | management/ |
| CIS/ISM | Information Systems | information-systems/ |
| DSA | Data Analytics | data-analytics/ |
| MATH | Mathematics | mathematics/ |
| STAT | Statistics | statistics/ |
| COM | Communication | communication/ |
| PSY | Psychology | psychology/ |
| SOC | Sociology | sociology/ |
| PSC | Political Science | political-science/ |
| HIS | History | history/ |
| LCS | Legal Studies | legal-studies/ |
| IB | International Business | international-business/ |
| ENT | Entrepreneurship | entrepreneurship/ |
| ENG | English | english/ |
| SCI | Science | science/ |
