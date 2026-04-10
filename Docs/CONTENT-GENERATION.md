# Content Generation

The server-side content generation engine (`server.py`) creates quiz questions, flashcards, and written questions for each module by scraping open-source textbook content and applying template-based generation.

## Pipeline

For each module in a generation request:

```
1. scrape_topic_info(topic, reading)
2. extract_key_terms(topic_info)
3. generate_mcq(topic_info, terms)        -- if quiz requested
4. generate_flashcards(topic_info, terms)  -- if flashcards requested
5. generate_written(topic_info, terms)     -- if written requested
```

---

## Step 1: Scrape Topic Info

`scrape_topic_info(topic, reading)`:

1. Extract chapter number from the reading string (e.g., "Ch. 3" -> 3)
2. Fetch the corresponding page from OpenStax Principles of Economics 3e
3. Parse HTML paragraphs as scraped content
4. Return structured info:

```python
{
    "topic": "Supply and Demand",
    "keywords": [...],
    "reading": "Ch. 3",
    "scraped_content": "Full text from textbook page..."
}
```

## Step 2: Extract Key Terms

`extract_key_terms(topic_info)`:

1. Find capitalized multi-word terms in scraped content
2. Split the topic string by common delimiters (commas, ampersands, "and")
3. Filter: length > 3 characters, unique entries only
4. Return up to 15 terms

## Step 3: Generate Multiple Choice Questions

`generate_mcq(topic_info, terms, count=15)`:

For each key term:
1. Find its definition in the scraped content
2. Create a **definition question** using templates
3. Create a paired **application question**
4. Generate 3 distractors per question

### Question Templates

```python
QUESTION_TEMPLATES = {
    "definition": [
        "Which of the following best defines {term}?",
        "The concept of {term} refers to:",
        "{term} is best described as:"
    ],
    "application": [
        "Which scenario best illustrates {term}?",
        "A real-world example of {term} would be:"
    ],
    "comparison": [
        "What is the key difference between {term_a} and {term_b}?"
    ]
}
```

### Distractor Generation

Each MC question gets 3 wrong answers (template-based):

1. "An unrelated concept from a different field of study"
2. "The opposite of what {term} actually describes"
3. "A concept that applies only in theory, not in real-world scenarios"

These are deliberately generic. They serve the purpose of self-study practice without requiring AI-generated alternatives.

## Step 4: Generate Flashcards

`generate_flashcards(topic_info, terms, count=12)`:

For each key term, two cards are created:
- **Definition card**: Front = "What is {term}?", Back = definition from scraped content
- **Importance card**: Front = "Why is {term} important?", Back = contextual explanation

Returns up to 12 cards per module.

## Step 5: Generate Written Questions

`generate_written(topic_info, terms, count=3)`:

Three question types, each conditional on having enough terms:

| # | Template | Condition |
|---|----------|-----------|
| 1 | "Explain {term} and why it matters" | >= 1 term |
| 2 | "Compare and contrast {termA} and {termB}" | >= 3 terms |
| 3 | "Using a real-world example, explain {term}" | >= 2 terms |

Each includes:
- `keywords` array for grading
- `idealAnswer` string for student reference

---

## Content Storage

Generated content is returned as a JSON response and merged into the client-side `activeContent` object, then persisted to `localStorage['syllabot_content_${courseId}']`.

All content is keyed by module using the format `"Module N: Topic Name"`.

## Limitations

- Content scraping depends on OpenStax availability
- Distractors are template-based, not contextually generated
- Only economics textbooks are currently supported as a source
- Content quality depends on the scraped text quality
