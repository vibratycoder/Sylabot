# ADR-004: Heuristic Written Answer Grading

## Status

Accepted

## Date

2026-01-20

## Context

Syllabot includes written questions where students type free-form answers. These need to be graded to provide feedback. We needed to decide how to evaluate written responses.

Options considered:
1. **LLM-based grading** -- Send answers to an AI API (OpenAI, Anthropic) for evaluation
2. **NLP library** -- Use a local NLP model (spaCy, NLTK) for semantic similarity
3. **Heuristic scoring** -- Keyword matching + pattern detection + length assessment
4. **Self-grading** -- Let students grade themselves against a rubric

## Decision

We chose option 3: a heuristic scoring algorithm combining keyword matching (45%), reasoning pattern detection (40%), and response length (15%).

## Rationale

- **No API dependency**: Grading works offline, instantly, and for free. No API keys, rate limits, or costs.
- **Deterministic**: The same answer always produces the same score. Students can learn what the system values and improve.
- **Transparent**: The feedback shows exactly which keywords were found, which were missing, and what reasoning patterns were detected. Nothing is a black box.
- **Fast**: Runs in milliseconds client-side. No network latency.
- **Good enough for self-study**: The goal is formative feedback ("you forgot to mention opportunity cost"), not authoritative grading. Students are studying for themselves, not submitting for credit.

## Algorithm Details

```
finalScore = round((keywordRatio * 0.45 + reasoningScore * 0.40 + lengthScore * 0.15) * 100)
```

### Keyword Matching (45% weight)
- Each question defines expected keywords
- Case-insensitive search in the student's answer
- Score = found keywords / total keywords

### Reasoning Pattern Detection (40% weight)
Six regex patterns detect:
- Causal reasoning (because, therefore, due to)
- Cause-effect language (causes, effects, results in)
- Examples (for example, such as)
- Comparisons (compared to, whereas, unlike)
- Change language (increases, decreases, shifts)
- Relational thinking (relationship between, linked to)

Score = min(patterns matched / 3, 1.0)

### Length Assessment (15% weight)
Rewards substantive responses: 20+ words = full marks, <6 words = minimal.

## Trade-offs

### Accepted downsides
- **Cannot evaluate correctness**: A factually wrong answer with the right keywords scores well. The system checks coverage, not accuracy.
- **Gameable**: A student who memorizes the keyword list can score 100% without understanding.
- **No semantic understanding**: "Scarcity means abundance" would score well for the keyword "scarcity" despite being wrong.
- **English-centric**: Reasoning patterns are English regex patterns. Non-English answers would score poorly on reasoning.

### Mitigations
- The feedback explicitly shows the model answer, so students can self-correct even if the score is misleading.
- Missing keyword tags (yellow) highlight gaps in coverage.
- The system is positioned as a study aid, not an exam. Students are motivated to learn, not to cheat themselves.
- The 40% reasoning weight rewards well-structured answers beyond keyword stuffing.

## Consequences

- Written question authors must provide a `keywords` array and `idealAnswer` for each question.
- The grading system cannot be used for formal assessment or credit-bearing work.
- Future improvements could add semantic similarity (e.g., word embeddings) without changing the interface.
- The score thresholds (Excellent/Good/Fair/Needs Work/Insufficient) are calibrated for encouragement, not precision.
