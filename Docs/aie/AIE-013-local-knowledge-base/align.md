# Align -- Local Knowledge Base

**AIE:** AIE-013
**Date:** 2026-04-08
**Severity:** major
**Domain:** backend

## Problem
Content generation currently depends on live scraping of OpenStax pages at runtime. This is fragile (network failures, URL changes, OpenStax availability), slow (HTTP round-trips per module), and limited to a single textbook. The app needs a local, structured knowledge base of source material that the server reads from disk to generate questions, quizzes, flashcards, and tutor content -- reliably, offline-capable, and expandable to any subject.

## Decision
Create a `content/` directory at the project root with a structured hierarchy of markdown files organized by subject, course, and chapter. Each chapter file contains the key terms, definitions, concepts, examples, and relationships that the content generator uses as source material.

### Directory Structure

```
content/
  README.md                          -- How to add/edit knowledge base files
  economics/
    _subject.md                      -- Subject-level metadata & overview
    microeconomics/
      _course.md                     -- Course metadata (maps to typical Micro course)
      ch01-scarcity-opportunity-cost.md
      ch02-choice-in-a-world-of-scarcity.md
      ch03-supply-and-demand.md
      ch04-elasticity.md
      ch05-consumer-and-producer-surplus.md
      ch06-government-policies.md
      ch07-production-costs.md
      ch08-perfect-competition.md
      ch09-monopoly.md
      ch10-monopolistic-competition.md
      ch11-oligopoly.md
      ch12-labor-markets.md
      ch13-poverty-inequality.md
      ch14-international-trade.md
    macroeconomics/
      _course.md
      ch01-gdp-and-measurement.md
      ch02-economic-growth.md
      ch03-unemployment.md
      ch04-inflation.md
      ch05-aggregate-demand-supply.md
      ch06-fiscal-policy.md
      ch07-monetary-policy.md
      ch08-money-and-banking.md
```

### Chapter File Format

Each chapter .md file follows a consistent structure:

```markdown
---
chapter: 3
title: Supply and Demand
subject: economics
course: microeconomics
keywords: [supply, demand, equilibrium, shortage, surplus, price]
prereqs: [ch01, ch02]
---

# Supply and Demand

## Overview
[2-3 paragraph summary of the chapter's core ideas]

## Key Terms
- **Supply**: [definition]
- **Demand**: [definition]
...

## Core Concepts
### [Concept Name]
[Explanation with enough depth for quiz/tutor generation]

## Examples
### [Example Title]
[Real-world example that can be turned into application questions]

## Relationships
- Supply and Demand → Equilibrium: [how they connect]
- Price changes → Quantity demanded: [inverse relationship]

## Common Misconceptions
- [Misconception]: [Why it's wrong and what's correct]

## Practice Angles
- Compare and contrast: [term A] vs [term B]
- Explain with example: [concept]
- Cause and effect: [if X then Y]
```

### How server.py Uses These Files

The `/generate` endpoint will:
1. Receive module topic and reading (e.g., "Supply and Demand", "Ch. 3")
2. Match against chapter files using chapter number and/or keyword fuzzy match
3. Parse the markdown frontmatter and sections
4. Feed Key Terms → MCQ generation and flashcard generation
5. Feed Core Concepts + Examples → written question generation
6. Feed Overview + Key Terms + Examples → tutor HTML generation
7. Fall back to OpenStax scraping only if no local file matches

## Why This Approach
- **Offline-capable** -- No network dependency for content generation
- **Editable** -- Teachers/contributors can add, correct, or expand content by editing markdown
- **Structured** -- Consistent format means the generator can reliably extract terms, definitions, examples
- **Expandable** -- New subjects (biology, history, CS) just need a new folder with the same file format
- **Version-controlled** -- All content lives in the repo, diffable, reviewable
- **Fallback preserved** -- OpenStax scraping remains as a fallback for chapters without local files

## Impact
- Creates `content/` directory with ~25 markdown files
- Modifies `server.py` to read local files before scraping
- All content generators (`generate_mcq`, `generate_flashcards`, `generate_written`, `generate_tutor_html`) get richer source material
- Content quality improves significantly vs. scraping raw HTML

## Success Criteria
- `content/` directory exists with README, subject/course metadata, and chapter files
- Each chapter file has frontmatter, key terms, concepts, examples, and practice angles
- `server.py` reads and parses local files first, falls back to scraping
- Generated quizzes, flashcards, and tutor content are noticeably richer with local data
- Adding a new chapter file automatically makes it available for content generation
