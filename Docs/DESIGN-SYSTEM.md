# Design System

## Color Palette

All colors are defined as CSS custom properties on `:root`.

| Variable | Value | Usage |
|----------|-------|-------|
| `--bg` | `#0f1117` | Deep navy page background |
| `--surface` | `#1a1d27` | Card and container fill |
| `--surface2` | `#232736` | Elevated surface (inputs, nested elements) |
| `--border` | `#2e3346` | Dividers, outlines |
| `--text` | `#e2e4eb` | Primary text |
| `--text-dim` | `#8b8fa3` | Muted/secondary text |
| `--accent` | `#6c5ce7` | Purple -- primary action color |
| `--accent-light` | `#a29bfe` | Hover/glow variant |
| `--green` | `#00b894` | Success, done, correct |
| `--yellow` | `#fdcb6e` | Warning, current, caution |
| `--red` | `#e17055` | Danger, urgent, incorrect |
| `--orange` | `#f39c12` | Secondary warning |
| `--blue` | `#74b9ff` | Info, links, secondary |

## Typography

- **Font stack**: `'Segoe UI', system-ui, -apple-system, sans-serif`
- **Base size**: 0.9rem body, 1rem inputs
- **Weights**: 400 (body), 600 (semibold labels), 700 (headings)

## Components

### Card (`.card`)
| Property | Value |
|----------|-------|
| Padding | 20px |
| Border-radius | 12px |
| Border | 1px solid var(--border) |
| Background | var(--surface) |

### Stat Card (`.stat-card`)
| Property | Value |
|----------|-------|
| Padding | 16px |
| Border-radius | 12px |
| Border | 1px solid var(--border) |
| Background | var(--surface) |

### Badge (`.badge`)
| Property | Value |
|----------|-------|
| Padding | 2px 8px |
| Border-radius | 6px |
| Border | none |
| Background | Varies by variant |

### Topic Button (`.topic-btn`)
| Property | Value |
|----------|-------|
| Padding | 8px 16px |
| Border-radius | 20px |
| Border | 1px solid var(--border) |
| Background | transparent (default), var(--accent) (active) |

### Quiz Option (`.quiz-opt`)
| Property | Value |
|----------|-------|
| Padding | 10px 14px |
| Border-radius | 8px |
| Border | 1px solid var(--border) |
| Background | var(--surface2), green on correct, red on incorrect |

### Grade Input Row (`.grade-input-row`)
| Property | Value |
|----------|-------|
| Padding | 8px 12px |
| Border-radius | 8px |
| Border | 1px solid var(--border) |
| Background | var(--surface2) |

## Badge Variants

| Class | Background | Text Color | Use Case |
|-------|-----------|------------|----------|
| `.badge.urgent` | rgba(red, 0.15) | var(--red) | 3 days or fewer |
| `.badge.soon` | rgba(orange, 0.15) | var(--orange) | 7 days or fewer |
| `.badge.upcoming` | rgba(yellow, 0.15) | var(--yellow) | 14 days or fewer |
| `.badge.later` | rgba(blue, 0.15) | var(--blue) | More than 14 days |
| `.badge.done` | rgba(green, 0.15) | var(--green) | Completed |
| `.badge.exam` | rgba(red, 0.2) | var(--red) | Exam type |

## Animations

### Fade In
```css
@keyframes fadeIn {
  0%   { opacity: 0; transform: translateY(8px); }
  100% { opacity: 1; transform: translateY(0); }
}
.fade-in {
  animation: fadeIn 0.3s ease;
}
```

### Flashcard Flip
- Container: `perspective: 1000px`
- Card: `transform-style: preserve-3d`, `transition: transform 0.5s`
- Flipped state: `rotateX(180deg)`
- Both faces: `backface-visibility: hidden`

### Progress Bars
```css
transition: width 0.5s ease;
```

## Responsive Breakpoints

```css
@media (max-width: 768px) {
  /* Stat grid: 2 columns instead of 4 */
  /* Nav: horizontal scroll or wrap */
  /* Course grid: single column */
  /* Flashcard: full width */
  /* Form: single column layout */
}
```

## Layout Constraints

- Max content width: 1200px
- Centered with `margin: 0 auto`
- Course grid: `grid-template-columns: repeat(auto-fill, minmax(280px, 1fr))`, gap 16px
- Stat cards: 4-column grid on desktop, 2-column on mobile
