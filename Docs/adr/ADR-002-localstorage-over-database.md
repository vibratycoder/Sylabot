# ADR-002: localStorage Over Database

## Status

Accepted

## Date

2026-01-15

## Context

Syllabot needs to persist course data, quiz history, module progress, and generated content across browser sessions. We needed to choose a storage mechanism.

Options considered:
1. **Server-side database** (SQLite, PostgreSQL) with REST API
2. **IndexedDB** in the browser
3. **localStorage** in the browser
4. **File-based storage** (JSON files on disk)

## Decision

We chose option 3: browser `localStorage` with JSON serialization.

## Rationale

- **No server required for persistence**: The app works offline and without the Python server running. Data survives page reloads and browser restarts.
- **Zero setup**: No database installation, no schema migrations, no connection strings.
- **Simple API**: `getItem`/`setItem` with `JSON.parse`/`JSON.stringify` covers all use cases.
- **Sufficient for the data volume**: A typical student has 4-6 courses. Even with full content generation, this fits well within the 5-10 MB localStorage limit.
- **Privacy**: Student data never leaves their browser. No accounts, no cloud sync, no data collection.

## Trade-offs

### Accepted downsides
- **No cross-device sync**: Data is locked to one browser on one machine.
- **Storage limit**: Browsers typically cap localStorage at 5-10 MB. Heavy use with many courses could hit this.
- **No query capabilities**: All filtering and searching is done in-memory after loading the full dataset.
- **Data loss risk**: Clearing browser data, using incognito mode, or switching browsers loses all data.
- **No concurrent access**: Multiple tabs could create race conditions (not currently handled).

### Mitigations
- Data is namespaced by course ID, so individual courses can be deleted to free space.
- The data model is flat and simple -- no complex queries are needed.
- Students typically use one device for coursework.
- JSON export/import via the Courses tab allows manual backup.

## Consequences

- No user accounts or authentication system is needed or possible.
- The server (`server.py`) is stateless -- it processes requests and returns results without storing anything.
- All data management (CRUD) happens client-side in JavaScript.
- A future migration to IndexedDB would require rewriting the persistence layer but not the data model.

## Data Namespace Convention

```
syllabot_courses                          -- All course objects
syllabot_activeCourse                     -- Active course ID
syllabot_content_${courseId}              -- Generated content per course
syllabot_${courseId}_quizHistory          -- Quiz attempts per course
syllabot_${courseId}_mod-${moduleNum}     -- Module completion flags
```
