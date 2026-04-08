# Instruct — Standardize Visual Formatting Across All 7 Tabs

**AIE:** AIE-001

## Directive
> "use the aie skill to format all of the seperate tabs"

Followed by:
> "now create new files for all of the different tabs and use the same skill and log all of the changes in the respective files from now on"

The user wants the monolithic index.html split into separate files per tab AND the formatting standardization applied. AIE-001 covers the formatting plan; AIE-002 will cover the file splitting architecture.

## Context Provided
- `index.html` — single-file Syllabot app with 7 tabs, all CSS/JS/HTML inline
- `eco114_course.json` — parsed course data
- Prior conversation establishing all tab functionality

## Scope
**IN scope (AIE-001):** CSS formatting standardization — tab headers, card accents, extracted classes, spacing.
**OUT of scope (AIE-001):** File splitting — handled by AIE-002.
