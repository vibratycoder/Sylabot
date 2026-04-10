# Instruct -- Content Generation from Local Knowledge Base

**AIE:** AIE-014

## Directive

> "Rewrite server.py's content generation pipeline to read from the local content/ directory and JSON knowledge bases. Add a markdown parser that extracts frontmatter and sections. Add a matching function that finds the best content file for a given module topic. Rewrite generate_mcq to use real definitions as correct answers with distractors from other terms, misconceptions, and related concepts. Rewrite generate_flashcards to create cards from Key Terms definitions. Rewrite generate_written to use Practice Angles with proper keyword lists. Rewrite generate_tutor_html to produce a full study guide with Overview, Key Terms, Core Concepts, Examples, and Misconceptions sections. Keep OpenStax scraping as a fallback."

## Context Provided

- server.py -- Current content generation with OpenStax scraping
- content/ -- 93 markdown files with structured chapter content
- JSON KB files -- Agent-generated knowledge bases with course data
- Docs/CONTENT-GENERATION.md -- Pipeline documentation
- Docs/QUIZ-SYSTEM.md -- Question format specs

## Scope

**In scope:**
- Markdown parser for content/ files (frontmatter + sections)
- JSON KB parser for agent-generated files
- Topic-to-file matching function
- Rewritten generate_mcq, generate_flashcards, generate_written, generate_tutor_html
- OpenStax scraping as fallback

**Out of scope:**
- Frontend changes
- New question types
- AI/LLM-based generation
