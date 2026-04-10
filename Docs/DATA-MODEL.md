# Data Model

All data is stored in the browser's `localStorage` as JSON-serialized strings. Each piece of data is namespaced by course ID to ensure multi-course isolation.

## Storage Keys

| Key | Type | Description |
|-----|------|-------------|
| `syllabot_courses` | JSON array | All course objects |
| `syllabot_activeCourse` | string | ID of the currently active course |
| `syllabot_content_${courseId}` | JSON object | Generated content (tutor, quiz, written, flashcards) |
| `syllabot_${courseId}_quizHistory` | JSON array | Quiz attempt history |
| `syllabot_${courseId}_mod-${moduleNum}` | string | Module completion flag (`"done"`) |

---

## Course Object

Stored in the `syllabot_courses` array.

```javascript
{
  id: "eco114-spring2026",
  code: "ECO 114",
  name: "Microeconomic Principles",
  instructor: "Liam Rice",
  schedule: "TF 9:35-10:50AM",
  location: "UNI 268",
  semester: "Spring 2026",
  color: "#6c5ce7",
  finalExamDate: "2026-05-12",
  gradeWeights: [ ... ],
  modules: [ ... ],
  deadlines: [ ... ],
  hasBuiltInContent: false
}
```

### ID Generation

```
code.toLowerCase().replace(/\s/g, '') + '-' + semester.toLowerCase().replace(/\s/g, '')
```

Example: `"ECO 114"` + `"Spring 2026"` = `"eco114-spring2026"`

### Color Assignment

Colors are assigned from a 10-color palette, cycling with modulo:

```javascript
COURSE_COLORS = [
  "#6c5ce7", "#00b894", "#e17055", "#74b9ff", "#fdcb6e",
  "#a29bfe", "#55efc4", "#fd79a8", "#0984e3", "#ffeaa7"
]
// course.color = COURSE_COLORS[courses.length % 10]
```

---

## Grade Weight

```javascript
{
  name: "Quizzes",
  weight: 20,        // percentage (should sum to ~100 across all weights)
  id: "gw-0"         // unique identifier
}
```

---

## Module

```javascript
{
  num: 1,
  topic: "Scarcity & Opportunity Cost",
  unit: 1,
  reading: "Ch. 1",
  status: "done" | "current" | "upcoming"
}
```

Module status drives the dashboard "Current Module" stat card and the progress tracker visual indicators.

---

## Deadline

```javascript
{
  name: "Quiz 1",
  date: "2026-02-14",        // ISO date string (YYYY-MM-DD)
  type: "hw" | "reading" | "project" | "exam" | "aec" | "other"
}
```

The `type` field determines:
- Badge styling (exam type gets a special red badge)
- Action verb in the planner ("Study for", "Complete reading:", "Work on", etc.)
- Time estimates in the "Do Right Now" checklist

---

## Course Content

Stored per course at `syllabot_content_${courseId}`.

```javascript
{
  tutor: {
    "Module 1: Scarcity & Opportunity Cost": "<div class='tutor-section'>...HTML...</div>"
  },
  quiz: {
    "Module 1: Scarcity & Opportunity Cost": [
      {
        q: "Which best defines scarcity?",
        opts: ["A", "B", "C", "D"],
        correct: 0,
        explain: "Because..."
      }
    ]
  },
  written: {
    "Module 1: Scarcity & Opportunity Cost": [
      {
        q: "Explain scarcity...",
        keywords: ["scarcity", "resources", "unlimited wants"],
        idealAnswer: "..."
      }
    ]
  },
  flashcards: {
    "Module 1: Scarcity & Opportunity Cost": [
      {
        front: "What is scarcity?",
        back: "The condition where unlimited wants exceed limited resources."
      }
    ]
  }
}
```

All content is keyed by module using the format `"Module N: Topic Name"`.

---

## Quiz History Entry

Stored per course at `syllabot_${courseId}_quizHistory`.

```javascript
{
  module: "Module 1: Scarcity & Opportunity Cost",
  score: 4,          // MC questions correct
  total: 5,          // MC questions total
  written: 85,       // average written score (0-100)
  pct: 78,           // combined percentage
  date: "2026-03-15T14:30:00.000Z"
}
```

---

## Helper Functions

```javascript
getAllCourses()           // Parse syllabot_courses from localStorage
saveCourses(arr)         // Serialize and save course array
getCourseContent(id)     // Parse content for a specific course
setCourseContent(id, c)  // Save content for a specific course
```
