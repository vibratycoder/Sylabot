# Setup Guide

## Prerequisites

- Python 3.8 or higher
- A modern web browser (Chrome, Firefox, Edge, Safari)
- No Node.js, npm, or build tools required

## Installation

### 1. Install Python Dependencies

```bash
pip install pdfplumber python-docx
```

These are only needed for server-side syllabus parsing:
- **pdfplumber** -- Extracts text from uploaded PDF syllabi
- **python-docx** -- Extracts text from uploaded DOCX syllabi

### 2. Start the Server

```bash
python server.py
```

The server starts on port **8000** by default. It serves:
- Static files from the project directory (including `index.html`)
- Two POST API endpoints (`/upload` and `/generate`)

### 3. Open the App

Navigate to `http://localhost:8000` in your browser.

## Running Without the Server

The server is optional for basic usage. Without it you can:
- Create courses manually via the course wizard
- Use all 8 tabs (dashboard, planner, tutor, quiz, flashcards, progress, grade calc, courses)
- Store and retrieve data from localStorage

You **cannot** do the following without the server:
- Upload and parse syllabus files (PDF/DOCX/TXT)
- Generate quiz/flashcard/written content from modules

To run without the server, open `index.html` directly in a browser via `file://` protocol.

## Troubleshooting

### Port 8000 already in use

```bash
# Find and kill the process using port 8000
# Linux/Mac:
lsof -ti:8000 | xargs kill
# Windows:
netstat -ano | findstr :8000
taskkill /PID <pid> /F
```

### pdfplumber import error

```bash
pip install --upgrade pdfplumber
```

### CORS issues

The server adds CORS headers to all responses. If you see CORS errors, ensure you are accessing the app through the server (`http://localhost:8000`) rather than opening the HTML file directly.

### localStorage full

Each browser has a localStorage limit (typically 5-10 MB). If you hit this:
- Delete unused courses from the Courses tab
- Clear quiz history for old courses
- Use the browser console: `localStorage.clear()` (warning: deletes all data)

## Data Persistence

All data is stored in the browser's localStorage. There is no server-side database. This means:
- Data persists across page reloads and browser restarts
- Data does NOT sync between browsers or devices
- Clearing browser data will delete all courses and progress
- Private/incognito mode will lose data when the window closes
