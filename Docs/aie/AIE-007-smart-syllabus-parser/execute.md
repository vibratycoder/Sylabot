# Execute — Smart Syllabus Parser

**AIE:** AIE-007

## Files Changed

| File | Action | What Changed |
|------|--------|-------------|
| `index.html` | modified | Replaced simple `autoFillFromText()` with full smart parser: `fillCourseInfo()`, `extractGradeWeights()`, `extractModules()`, `extractDeadlines()`, `classifyDeadlineType()`, `extractReadingFromLine()`. ~200 lines of new parsing logic. |

## Outcome
Implementation matches align.md plan.

- **Course info** (Step 1): Improved regex for code, name, instructor, schedule, location. Handles "Prof.", "Dr.", multiple line formats, "UNI 268" style locations.
- **Grade weights** (Step 2): Detects tab-separated "Name\tNN%" format and "Name NN%" format. Finds "Graded Assignment" or "% of Grade" section header first. Validates total ~100%.
- **Modules** (Step 3): Extracts "Module N: Topic" from tab-separated schedule rows. Pulls reading references from the correct column (not the whole line). Handles "Ch. N", "Txtbk. Ch. N & M".
- **Deadlines** (Step 4): Parses "Day, Month DDth" dates from schedule table. Detects homework, exams, projects, presentations. Classifies type (exam/hw/project/other). Deduplicates.

**Tested against ECO 114 syllabus .docx:**
- 6 grade weights detected (total 100%)
- 13 modules with topics and readings
- ~15 unique deadlines with correct dates and types

## Side Effects
None. Existing manual entry still works. Auto-fill is additive — it populates the form but user can edit before saving.

## Tests
- [x] ECO 114 .docx — grade weights, modules, and deadlines auto-detected
- [ ] PDF upload — needs manual test with one of the other syllabi
- [ ] Edge cases — syllabi with different formats (no tables, different labeling)

## Follow-Up Required
- [ ] Test with FIN201, ISA201, GEN103, HIS261 syllabi from Downloads folder
- [ ] Consider adding a "Review Auto-Fill" summary modal before committing to form
