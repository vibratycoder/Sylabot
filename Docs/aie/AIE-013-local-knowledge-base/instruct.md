# Instruct -- Local Knowledge Base

**AIE:** AIE-013

## Directive

> "Research all courses offered by Bryant University. Create a content/ directory with structured markdown files for every major subject area. Each file should contain key terms, definitions, core concepts, real-world examples, relationships between concepts, common misconceptions, and practice angles. This knowledge base replaces OpenStax scraping as the primary source for generating quizzes, flashcards, written questions, and tutor content. Organize by subject (economics, finance, accounting, marketing, management, info systems, data analytics, math, stats, communication, psychology, sociology, political science, history, legal studies, international business, entrepreneurship, english, science). Use Bryant University course codes where available."

## Context Provided

- Docs/API.md -- /generate endpoint spec
- Docs/CONTENT-GENERATION.md -- How content is generated
- Docs/DATA-MODEL.md -- Content object structure
- server.py -- Current scraping-based generation
- AIE-013 align.md -- Chapter file format specification
- Web research from 8 parallel agents covering Bryant University's full catalog

## Scope

**In scope:**
- content/README.md with format documentation
- Subject _subject.md metadata files
- Chapter .md files for all major Bryant subjects
- Comprehensive key terms, concepts, examples per chapter
- Enough content density to generate quality quizzes/flashcards/tutor material

**Out of scope:**
- Modifying server.py to read these files (separate AIE)
- Graduate-level course content
- Lab/practicum course content
