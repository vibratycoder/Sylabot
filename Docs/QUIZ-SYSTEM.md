# Quiz System

## Overview

The quiz system supports two question types -- multiple choice and written -- with per-module question pools, randomization, and a heuristic grading engine for written responses.

## Quiz Flow

1. **Module Selection** -- User picks a module from pill-button selectors
2. **Settings** -- Choose MC question count (1 to min(50, pool size), default 5) and toggle written questions
3. **Quiz Execution** -- Answer MC questions by clicking options; submit written answers via textarea
4. **Results** -- Combined score saved to history, displayed in table and canvas chart

## Multiple Choice

### Question Generation

`generateQuiz()` performs:
1. Copy the full question pool for the selected module
2. Shuffle using Fisher-Yates algorithm
3. Take N questions (per user setting)
4. For each question, shuffle the `opts` array and recalculate the `correct` index

### Answering

`answerQuiz(questionIndex, optionIndex)`:
- Locks all options for that question (prevents re-answering)
- Applies CSS classes: `.correct` (green), `.incorrect` (red), `.reveal-correct` (outline on actual answer)
- Shows the explanation `<div>`
- Increments `quizAnswered` and `quizCorrect` counters

## Written Questions

### Grading Algorithm (`gradeWritten`)

A heuristic scoring system combining three factors:

```
finalScore = round((keywordRatio * 0.45 + reasoningScore * 0.40 + lengthScore * 0.15) * 100)
```

#### Keyword Matching (45%)

```
keywordRatio = (count of keywords found in answer, case-insensitive) / totalKeywords
```

Keywords are defined per question in the content data.

#### Reasoning Pattern Detection (40%)

Six regex patterns are checked against the answer:

| Pattern | What It Detects |
|---------|----------------|
| `/because\|since\|due to\|as a result\|therefore\|this means\|this leads to/` | Causal reasoning |
| `/causes?\|effects?\|impacts?\|results? in\|leads? to/` | Cause-effect language |
| `/for example\|for instance\|such as\|e\.g\./` | Examples |
| `/compared to\|whereas\|while\|unlike\|on the other hand\|in contrast/` | Comparisons |
| `/increases?\|decreases?\|shifts?\|changes?\|moves?/` | Economic change language |
| `/relationship between\|connection between\|linked to\|related to/` | Relational thinking |

```
reasoningScore = min(patternHits / 3, 1.0)
```

Hitting 3 or more patterns yields the maximum score.

#### Length Assessment (15%)

| Word Count | Score |
|-----------|-------|
| 20+ | 1.0 |
| 12-19 | 0.8 |
| 6-11 | 0.5 |
| <6 | 0.2 |

### Grade Thresholds

| Score | Label | Color |
|-------|-------|-------|
| 90+ | Excellent | Green |
| 75-89 | Good | Blue |
| 60-74 | Fair | Yellow |
| 40-59 | Needs Work | Orange |
| <40 | Insufficient | Red |

### Feedback Display

Each graded written answer shows:
- Score badge with label and color
- Concepts covered (green tags for matched keywords)
- Missing concepts (yellow tags for unmatched keywords)
- Reasoning depth assessment
- Model answer for comparison

## Combined Scoring

```
combinedPct = (mcPct * mcCount + writtenAvg * writtenCount) / (mcCount + writtenCount)
```

This weighted average ensures MC and written portions contribute proportionally.

## Quiz History

### Data

Each attempt is saved with: module name, MC score/total, written average, combined percentage, and ISO timestamp.

### Canvas Chart

Drawn directly on `<canvas>` without libraries:

- Grid: dashed horizontal lines at 25%, 50%, 75%, 100%
- Data points: circles (5px radius) colored by score
  - Green: >= 75%
  - Yellow: 50-74%
  - Red: < 50%
- Line: 2px accent color connecting all points
- Area: gradient fill (accent at 0.3 alpha to transparent) below the line
- X-axis: attempt numbers
- Padding: 40px left, 20px right/top, 30px bottom
- Redraws on window resize

## Completion Detection

`checkAllDone()` fires when:
- `quizAnswered === quizTotalMC` (all MC answered)
- `writtenGraded === writtenCount` (all written graded)

On completion: calculates combined score, saves to history, renders results panel.
