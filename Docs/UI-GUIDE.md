# UI Guide

Syllabot is an 8-tab single-page application with a fixed header and navigation bar.

## Layout

```
+---------------------------------------------+
| HEADER: Logo | Course Badge | Date          |
+---------------------------------------------+
| NAV: Dashboard | Planner | Tutor | Quiz |   |
|      Flashcards | Progress | Grade | Courses |
+---------------------------------------------+
|                                             |
|           ACTIVE TAB CONTENT                |
|                                             |
+---------------------------------------------+
```

- Max content width: 1200px, centered
- Navigation uses Unicode characters as icons (not emoji)
- Header updates dynamically to show active course code and name

## Tab Rendering

Tabs use a lazy rendering pattern. On course load, all tabs are marked dirty. When a tab becomes visible, it renders only if dirty, then clears its flag.

---

## Tab 1: Dashboard

The landing page showing an overview of the active course.

### Stat Cards (4-column grid)

1. **Days to Final** -- Countdown to `finalExamDate`. Red if <=7 days, yellow if <=21, green otherwise.
2. **Current Unit** -- Derived from the first module with status `"current"`.
3. **Grade Weight Remaining** -- Sum of weights whose deadlines have not all passed.
4. **Current Module** -- Topic name of the current module.

### Upcoming Deadlines Table

All deadlines sorted by date. Columns: Assignment, Due Date (with days-away count), Status Badge.

Badge logic:
- `EXAM` -- type is exam
- `URGENT` -- 3 days or fewer
- `THIS WEEK` -- 7 days or fewer
- `UPCOMING` -- 14 days or fewer
- `LATER` -- more than 14 days
- `DONE` -- date has passed

### Do Right Now Checklist

Top 5 upcoming future deadlines. Each item has:
- Checkbox (toggles strikethrough)
- Context-sensitive verb based on type
- Estimated time range

| Type | Verb | Time Estimate |
|------|------|---------------|
| exam | Study for | 60-90 min |
| hw | Work on | 45-60 min |
| reading | Complete reading: | 30-45 min |
| project | Work on | 45-60 min |
| other | Prepare for | 30-45 min |

### Semester Timeline

Visual bar of week blocks from earliest deadline to latest + 1 week. Colors: past weeks = accent purple, current week = yellow, future weeks = gray. Label: "Week X of Y".

### Grade Weight Breakdown

Horizontal bars for each grade weight component. Bar width proportional to weight percentage. Badge shows "Done" (green) if all matching deadlines have passed, otherwise "Active" (accent).

---

## Tab 2: Planner

Three chronological sections:

1. **This Week** -- Deadlines within the current week (days 0-6 from week start)
2. **Next Week** -- Deadlines 7-13 days from week start
3. **Full Schedule** -- All future deadlines, chronologically

Each item shows: date, days-away label, verb, name. Same-day items get a "Today!" flag.

---

## Tab 3: Tutor

Topic selector row of pill-shaped `.topic-btn` buttons (one per module with tutor content). Clicking a topic loads its HTML content into the display area.

Content uses semantic classes:
- `.tutor-section` -- Main content block
- `.key-term` -- Yellow highlighted term
- `.example` -- Left-bordered example box
- `.worked-example` -- Bordered box with step-by-step content

---

## Tab 4: Quiz

### Flow

1. **Module Selection** -- Pill buttons for modules with quiz content
2. **Settings Panel** -- Question count slider, written questions toggle
3. **Quiz** -- MC questions with clickable options, optional written questions
4. **Results** -- Score breakdown, quiz history table, canvas chart

### Multiple Choice

- 4 options labeled A-D
- Click locks all options for that question
- Correct answer highlighted green, wrong answer red, actual correct revealed
- Explanation shown below

### Written Questions

- Textarea input with submit button
- Graded using heuristic algorithm (see [Quiz System](QUIZ-SYSTEM.md))

### Quiz History Chart

Hand-drawn on HTML Canvas. Shows score trend across attempts with colored dots (green >= 75%, yellow >= 50%, red < 50%), connecting line, and gradient area fill.

---

## Tab 5: Flashcards

Module selector pills. Selected module loads its card set.

Card uses CSS 3D transforms:
- `perspective: 1000px` on container
- `transform-style: preserve-3d` on card
- Click toggles `.flipped` class applying `rotateX(180deg)`
- `backface-visibility: hidden` on both faces
- Transition: 0.5s

Navigation: Prev/Next buttons, "Card X of Y" counter. Next auto-unflips.

---

## Tab 6: Progress

### Stats Row
- Modules completed vs total
- Completion percentage
- Exams taken vs total exams

### Module Tracker
Grid of circular indicators per module. Green = done, yellow = current, gray = upcoming. Click to toggle completion (persisted to localStorage).

### Risk Analysis
Top 5 upcoming deadlines ranked by urgency:
- URGENT: 3 days or fewer (red)
- HIGH RISK: 10 days or fewer (red)
- MEDIUM: 21 days or fewer (yellow)
- LOW: more than 21 days (green)

### Recommendations
Conditional tips based on available content and progress.

---

## Tab 7: Grade Calculator

### Grade Input
Dynamic rows, one per grade weight component. Label + number input (0-100). Recalculates on every input change.

### Calculation
```
weighted = sum(score * weight / 100)
percentage = weighted / weightUsed * 100
```

### Letter Grade Scale
| Range | Grade |
|-------|-------|
| 93+ | A |
| 90-92 | A- |
| 86-89 | B+ |
| 83-85 | B |
| 80-82 | B- |
| 76-79 | C+ |
| 73-75 | C |
| 70-72 | C- |
| <70 | F |

### Final Exam Calculator
Auto-detects a grade weight containing "final" (case-insensitive). For each target grade, calculates the score needed on the final. Displays "Already achieved!", the needed percentage, or "Not possible" as appropriate.

---

## Tab 8: Courses

### Course Grid
Responsive grid (`repeat(auto-fill, minmax(280px, 1fr))`). Each card shows: color dot, code, name, instructor, schedule, location, semester, module/deadline counts. Active course has purple border with box-shadow glow.

### Add Course Options
- **Add Manually** -- Opens the 4-step wizard
- **Import Syllabus** -- Upload area for PDF/DOCX/TXT/JSON
- **Generate Content** -- Opens content generation modal

### Course Creation Wizard (4 Steps)
- **Step 0**: Course Info (code, name, instructor, semester, schedule, location, final exam date)
- **Step 1**: Grade Weights (dynamic rows, name + weight %, validates total)
- **Step 2**: Modules (dynamic rows, number + topic + reading)
- **Step 3**: Deadlines (dynamic rows, name + date + type dropdown)

Step indicators at top: active = accent, completed = green, future = gray. Navigation via indicator clicks and prev/next buttons.
