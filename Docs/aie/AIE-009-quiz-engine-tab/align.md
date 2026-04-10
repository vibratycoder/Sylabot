# Align -- Quiz Engine Tab

**AIE:** AIE-009
**Date:** 2026-04-08
**Severity:** major
**Domain:** frontend

## Problem
Users need to test their knowledge with multiple-choice and written questions, receive immediate feedback, and track their performance over time with visualizations.

## Decision
Implement the Quiz tab (Tab 4) in `index.html`:

1. **Module Selection** -- Pill buttons for modules with quiz content.

2. **Settings Panel** -- Question count slider (1 to min(50, pool size), default 5), written questions toggle checkbox.

3. **Quiz Generation** (`generateQuiz()`) -- Copy question pool, Fisher-Yates shuffle, take N questions, shuffle each question's options and recalculate correct index.

4. **MC Answering** (`answerQuiz(qIdx, optIdx)`) -- Lock all options for that question, apply CSS classes (.correct green, .incorrect red, .reveal-correct outline), show explanation div, increment counters.

5. **Written Question Grading** (`gradeWritten(answer, question)`) -- Heuristic scoring: keyword matching (45% weight), reasoning pattern detection via 6 regex patterns (40% weight), length assessment (15% weight). Score thresholds: Excellent (90+), Good (75-89), Fair (60-74), Needs Work (40-59), Insufficient (<40). Feedback shows matched/missing keyword tags, reasoning depth, model answer.

6. **Combined Scoring** -- `combinedPct = (mcPct * mcCount + writtenAvg * writtenCount) / (mcCount + writtenCount)`.

7. **Completion Detection** (`checkAllDone()`) -- Fires when all MC answered and all written graded. Saves to quiz history, renders results.

8. **Quiz History** -- Table of past attempts. Canvas chart drawn without libraries: dashed grid at 25/50/75/100%, colored dots (green >=75%, yellow >=50%, red <50%), connecting line, gradient area fill. Redraws on window resize.

## Why This Approach
- Fisher-Yates ensures fair randomization without bias
- Heuristic grading avoids requiring an LLM for written assessment (ADR-004)
- Hand-drawn canvas chart avoids chart library dependency (ADR-003)
- Combined scoring weights MC and written proportionally

## Impact
- Adds ~350 lines of JavaScript + HTML to `index.html`
- Depends on AIE-003 (quiz state variables, activeContent, quiz history persistence)
- Most complex single tab in the application

## Success Criteria
- Questions shuffle correctly with options and correct index recalculated
- MC answers lock and show correct/incorrect feedback immediately
- Written grading produces reasonable scores based on keyword coverage and reasoning
- Quiz history persists and displays in both table and canvas chart
- Chart redraws on window resize without artifacts
- Combined scoring is mathematically correct
