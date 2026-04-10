# ADR-003: No External Frontend Dependencies

## Status

Accepted

## Date

2026-01-15

## Context

Modern web applications typically use libraries for UI components (React, Vue), charting (Chart.js, D3), animations (GSAP), and styling (Tailwind, Bootstrap). We needed to decide whether Syllabot should adopt any of these.

Options considered:
1. **Full framework stack** (React + Chart.js + Tailwind)
2. **Lightweight libraries** (Alpine.js + Chart.js)
3. **Zero external dependencies** -- vanilla HTML5, CSS3, ES6 only

## Decision

We chose option 3: no external CSS or JavaScript libraries.

## Rationale

- **No CDN dependency**: The app works without internet after initial load. No risk of CDN outages or version changes breaking the app.
- **No version conflicts**: Zero chance of dependency hell, breaking changes, or security advisories requiring urgent updates.
- **Educational value**: Students studying the code see real browser APIs (Canvas 2D, CSS transforms, DOM manipulation) rather than library abstractions.
- **Performance**: No library overhead. The entire app is smaller than most framework bundles.
- **Longevity**: Browser APIs are stable for decades. A React app from 2018 may not build today; vanilla JS from 2018 still runs.

## Specific Replacements

| Typical Library | Our Approach |
|----------------|--------------|
| Chart.js / D3 | Hand-drawn Canvas 2D API for quiz history chart |
| React / Vue | Direct DOM manipulation with `innerHTML` and template literals |
| CSS framework | Custom CSS with `:root` variables and hand-written component classes |
| Animation library | CSS `@keyframes` and `transition` properties |
| Flip card library | CSS 3D transforms (`perspective`, `rotateX`, `backface-visibility`) |

## Trade-offs

### Accepted downsides
- **More code to write**: The Canvas chart (~60 lines) could be 5 lines with Chart.js.
- **No component reuse patterns**: Without a framework, similar UI patterns are repeated rather than abstracted.
- **No virtual DOM**: Large re-renders replace entire `innerHTML` blocks, which is less efficient than diffing.
- **No ecosystem**: No pre-built accessible components, date pickers, or drag-and-drop.

### Mitigations
- The app is small enough that raw DOM performance is not a bottleneck.
- Tab rendering is lazy (only when visible and dirty), reducing unnecessary updates.
- CSS custom properties provide a lightweight design system without a framework.
- The Canvas chart is simple (line + dots + fill) and doesn't need a charting library.

## Consequences

- All UI must be built with native browser APIs.
- The quiz history chart must be maintained as raw Canvas drawing code.
- Accessibility features must be implemented manually (ARIA attributes, keyboard navigation).
- Any future charting needs (e.g., grade trends) must also use Canvas 2D.
- Contributors must know vanilla JS DOM APIs rather than framework-specific patterns.
