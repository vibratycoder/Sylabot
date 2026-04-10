# Align -- Content Generation from Local Knowledge Base

**AIE:** AIE-014
**Date:** 2026-04-08
**Severity:** major
**Domain:** backend

## Problem
The current content generation in server.py scrapes OpenStax at runtime, producing generic template-based questions with weak distractors ("An unrelated concept from a different field"). The local knowledge base (93 markdown files + 5 JSON agent files) contains rich structured data: key terms with definitions, core concepts, real-world examples, common misconceptions, and practice angles. This data should drive much higher-quality quizzes, flashcards, and tutoring content.

## Decision
Rewrite server.py's content generation pipeline to:

1. **Parse local content files** -- Read markdown chapter files from content/, extract frontmatter (keywords, prereqs) and sections (Key Terms, Core Concepts, Examples, Misconceptions, Practice Angles). Also parse the JSON knowledge bases from agent research.

2. **Match modules to content** -- When /generate receives a module topic, fuzzy-match against local file titles, keywords, and chapter numbers. Fall back to OpenStax scraping only if no local match.

3. **Generate rich MCQs** -- Use real definitions as correct answers. Generate plausible distractors from: other key terms in the same chapter, common misconceptions, and related-but-wrong concepts. Questions from Practice Angles (compare/contrast, cause/effect, apply).

4. **Generate rich flashcards** -- Front: term name or concept question. Back: full definition from Key Terms section. Also create concept cards from Core Concepts and example cards from Examples section.

5. **Generate rich written questions** -- Directly from Practice Angles section. Include proper keyword lists and ideal answers drawn from the chapter content.

6. **Generate rich tutor HTML** -- Full study guide from Overview, Key Terms (highlighted), Core Concepts (with headers), Examples (in styled boxes), Common Misconceptions (myth vs fact format), and Relationships (concept map).

## Why This Approach
- Local content is curated, accurate, and structured for quiz generation
- Real distractors from misconceptions and related terms are far more educational than generic filler
- Practice Angles were designed specifically to generate good questions
- Tutor content becomes a real study guide instead of scraped HTML fragments
- Offline-capable -- no network dependency

## Impact
- Major rewrite of server.py content generation functions
- All existing courses will get dramatically better content on next generation
- content/ directory becomes the primary content source

## Success Criteria
- MCQs have plausible, educational distractors drawn from the same domain
- Flashcards cover all key terms with accurate definitions
- Written questions come from curated Practice Angles with proper rubrics
- Tutor content reads like a real study guide with terms, concepts, examples, and misconceptions
- Fallback to OpenStax scraping works for topics not in the local KB
