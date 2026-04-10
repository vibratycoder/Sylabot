# State Management

Syllabot manages state through global JavaScript variables synchronized with browser localStorage.

## Global Variables

### Course State
| Variable | Type | Description |
|----------|------|-------------|
| `activeCourse` | object/null | Current course object |
| `activeContent` | object | Content for active course (`{tutor, quiz, written, flashcards}`) |
| `activeDeadlines` | array | Deadlines from active course |
| `activeModules` | array | Modules from active course |
| `activeGradeWeights` | array | Grade weights from active course |

### Quiz State
| Variable | Type | Description |
|----------|------|-------------|
| `currentQuizModule` | string/null | Module key for active quiz |
| `quizAnswered` | number | MC questions answered this quiz |
| `quizCorrect` | number | MC questions correct this quiz |
| `quizTotalMC` | number | Total MC in current quiz |
| `writtenCount` | number | Written questions in current quiz |
| `writtenGraded` | number | Written questions graded so far |
| `writtenPoints` | number | Sum of written scores |
| `quizHistory` | array | All quiz attempts for active course |

### Flashcard State
| Variable | Type | Description |
|----------|------|-------------|
| `currentFCModule` | string/null | Module key for active flashcards |
| `fcIndex` | number | Current flashcard position |

### Form State
| Variable | Type | Description |
|----------|------|-------------|
| `gwRowCount` | number | Grade weight form row counter |
| `modRowCount` | number | Module form row counter |
| `dlRowCount` | number | Deadline form row counter |
| `currentFormStep` | number | Current wizard step (0-3) |

### Rendering State
| Variable | Type | Description |
|----------|------|-------------|
| `_dirtyTabs` | object | Tracks which tabs need re-rendering |

## Lazy Tab Rendering

Tabs render on-demand to avoid unnecessary DOM updates.

```javascript
const TAB_RENDERERS = {
  planner: renderPlanner,
  tutor: renderTutor,
  quiz: renderQuizControls,
  flashcards: renderFlashcardControls,
  progress: renderProgress,
  grades: renderGradeCalc,
  courses: renderCourses
};
```

### Lifecycle

1. **On course load**: All tabs marked dirty (`_dirtyTabs = { planner:1, tutor:1, ... }`)
2. **On tab switch**: If dirty, call renderer then clear flag
3. **Dashboard**: Always renders immediately (not lazy)

```javascript
function renderTabIfDirty(tabName) {
  if (_dirtyTabs[tabName] && TAB_RENDERERS[tabName]) {
    TAB_RENDERERS[tabName]();
    _dirtyTabs[tabName] = false;
  }
}
```

## Initialization Sequence

```
1. Document loads
2. Set today = new Date()
3. Display formatted date in header
4. Attach event listeners:
   - Tab clicks -> show/hide panels, call renderTabIfDirty
   - Upload drag/drop + file input -> handleFileUpload
   - Form step navigation -> goToFormStep
   - Grade calc inputs -> calcGrade (oninput)
   - Window resize -> redraw quiz history chart
5. loadActiveCourse():
   a. Get all courses from localStorage
   b. Find active course (from localStorage pointer, or first course)
   c. Load course content, deadlines, modules, gradeWeights
   d. Load quiz history
   e. Mark all non-dashboard tabs dirty
   f. Render dashboard immediately
6. App is interactive
```

## Persistence Helpers

```javascript
getAllCourses()           // JSON.parse(localStorage['syllabot_courses'] || '[]')
saveCourses(arr)         // localStorage['syllabot_courses'] = JSON.stringify(arr)
getCourseContent(id)     // JSON.parse(localStorage['syllabot_content_'+id] || '{}')
setCourseContent(id, c)  // localStorage['syllabot_content_'+id] = JSON.stringify(c)
```

## Utility Functions

```javascript
daysUntil(dateStr)       // Math.ceil((new Date(dateStr+'T00:00:00') - today) / 86400000)
shuffleArray(arr)        // Fisher-Yates in-place shuffle, returns new array
```

## Content Accessors

```javascript
getQuiz(mod)             // activeContent.quiz?.[mod] || []
getWritten(mod)          // activeContent.written?.[mod] || []
getFlashcards(mod)       // activeContent.flashcards?.[mod] || []
```

## Multi-Course Isolation

Every piece of data is namespaced by `courseId`:
- Content: `syllabot_content_${courseId}`
- Quiz history: `syllabot_${courseId}_quizHistory`
- Module completion: `syllabot_${courseId}_mod-${moduleNum}`

Switching courses via `loadActiveCourse()` loads a completely fresh state, resetting all global variables and marking all tabs dirty.
