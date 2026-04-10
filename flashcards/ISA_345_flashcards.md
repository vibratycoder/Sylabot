# ISA 345: Web Design and Development - Flashcard Reference Bank

---

## HTML

### Key Terms & Definitions
- **HTML**: HyperText Markup Language; the standard markup language for structuring content on the web
- **Element**: A component of an HTML document defined by a start tag, content, and an end tag (e.g., `<p>Hello</p>`)
- **Tag**: The opening or closing marker of an element (e.g., `<div>` is an opening tag, `</div>` is a closing tag)
- **Attribute**: A name-value pair inside an opening tag that provides additional information (e.g., `class="header"`, `id="main"`)
- **Semantic HTML**: HTML elements that convey meaning about their content to browsers and assistive technologies (e.g., `<nav>`, `<article>`, `<main>`)
- **DOCTYPE**: The `<!DOCTYPE html>` declaration that tells the browser to render the page in standards mode
- **DOM**: Document Object Model; the tree-like representation of an HTML document that browsers construct for programmatic access
- **Anchor Tag**: The `<a>` element used to create hyperlinks; the `href` attribute specifies the destination URL
- **Void Element**: An element that cannot have child content and has no closing tag (e.g., `<img>`, `<br>`, `<input>`, `<hr>`)
- **Block vs. Inline**: Block elements (`<div>`, `<p>`, `<h1>`) start on a new line and take full width; inline elements (`<span>`, `<a>`, `<strong>`) flow within text

### Core Concepts (Q&A Format)
- Q: What is the basic structure of every HTML document?
- A: `<!DOCTYPE html>`, a root `<html>` element, a `<head>` section (metadata, title, links), and a `<body>` section (visible content).

- Q: Why is semantic HTML important?
- A: It conveys meaning to browsers, screen readers, and search engines, improving accessibility, SEO, and code readability.

- Q: Name five semantic HTML5 elements and their purposes.
- A: `<header>` (introductory content), `<nav>` (navigation links), `<main>` (primary page content, used once per page), `<article>` (self-contained content), `<footer>` (closing information like copyright).

- Q: What is the difference between `<div>` and `<section>`?
- A: `<div>` is a non-semantic generic container with no meaning; `<section>` is a semantic element representing a thematic grouping of content, typically with a heading.

- Q: What elements are used to create an HTML form?
- A: `<form>` (container), `<input>` (text fields, checkboxes, radio buttons), `<select>` (dropdowns), `<textarea>` (multi-line text), `<button>` (submit/reset), and `<label>` (accessible field labels).

- Q: What is the difference between an ordered list and an unordered list?
- A: `<ol>` renders items with numbers/letters (sequential order matters); `<ul>` renders items with bullet points (order does not matter). Both use `<li>` for list items.

- Q: What does the `alt` attribute do on an `<img>` tag?
- A: It provides alternative text describing the image for screen readers and displays when the image fails to load; it is essential for accessibility and SEO.

- Q: What is the difference between `id` and `class` attributes?
- A: `id` must be unique per page and identifies a single element; `class` can be reused on multiple elements for shared styling or behavior.

### Important Facts & Figures
- HTML5 is the current version, introduced in 2014 by the W3C and WHATWG
- The `<main>` element should appear only once per page
- Semantic elements improve SEO because search engines weight content inside headings and semantic tags higher than content in generic `<div>` containers
- The `<figure>` and `<figcaption>` elements pair media content with a descriptive caption
- HTML is not a programming language; it is a markup language that defines document structure
- The `<head>` section contains metadata, the `<title>`, CSS links, and scripts -- none of it is rendered visually on the page
- Forms use the `action` attribute to specify where data is sent and the `method` attribute (`GET` or `POST`) to specify how

### Common Exam Questions
- Q: Which element should be used for the main navigation of a website? A: `<nav>`
- Q: What is the purpose of the `<!DOCTYPE html>` declaration? A: It tells the browser to use HTML5 standards mode for rendering.
- Q: True or False: `<div>` is a semantic element. A: False -- `<div>` is a non-semantic generic container.
- Q: Which attribute makes a form field required before submission? A: The `required` attribute on the `<input>` element.
- Q: What is the correct way to embed an image? A: `<img src="image.jpg" alt="Description">` -- a void element with `src` and `alt` attributes.

---

## JavaScript

### Key Terms & Definitions
- **DOM (Document Object Model)**: A tree-structured programming interface representing the HTML document; JavaScript uses it to access and modify page content
- **Event Listener**: A function registered on an element that executes when a specified event occurs (e.g., click, keypress)
- **Event Bubbling**: The default propagation behavior where an event fired on a child element travels upward through its ancestors
- **Event Capturing**: The opposite of bubbling; the event travels from the root down to the target element (set via `addEventListener`'s third parameter as `true`)
- **Callback Function**: A function passed as an argument to another function, to be executed later (e.g., in event handlers or async operations)
- **Promise**: An object representing the eventual completion or failure of an asynchronous operation; has states: pending, fulfilled, rejected
- **async/await**: Syntactic sugar over Promises that allows writing asynchronous code in a synchronous-looking style
- **Closure**: A function that retains access to variables from its outer (enclosing) scope even after the outer function has returned
- **Arrow Function**: A concise function syntax (`=>`) that does not have its own `this` binding; inherits `this` from the enclosing scope
- **Template Literal**: A string enclosed in backticks (`` ` ``) that supports embedded expressions (`${variable}`) and multi-line strings
- **Destructuring**: Syntax for unpacking values from arrays or properties from objects into distinct variables

### Core Concepts (Q&A Format)
- Q: What is the difference between `let`, `const`, and `var`?
- A: `let` is block-scoped and reassignable; `const` is block-scoped and cannot be reassigned; `var` is function-scoped, hoisted, and generally discouraged in modern JS.

- Q: How does `getElementById()` differ from `querySelector()`?
- A: `getElementById()` selects by ID only and returns a single element; `querySelector()` accepts any CSS selector and returns the first matching element.

- Q: What is event propagation and how do you stop it?
- A: Events propagate through capturing (root to target) then bubbling (target to root). Use `event.stopPropagation()` to prevent further propagation.

- Q: What does `preventDefault()` do?
- A: It cancels the browser's default action for an event (e.g., prevents a form from submitting or a link from navigating).

- Q: What are JavaScript's primitive data types?
- A: String, Number, Boolean, null, undefined, Symbol, and BigInt.

- Q: What is the difference between `==` and `===`?
- A: `==` performs type coercion before comparison; `===` (strict equality) checks both value and type without coercion.

- Q: How do you add a new element to the DOM?
- A: Create it with `document.createElement('tag')`, set its content/attributes, then attach it with `parentElement.appendChild(newElement)`.

- Q: What is the difference between `innerHTML` and `textContent`?
- A: `innerHTML` parses and renders HTML tags within the string; `textContent` treats everything as plain text, escaping HTML.

### Important Facts & Figures
- JavaScript is single-threaded but uses an event loop to handle asynchronous operations non-blockingly
- The six falsy values in JS: `false`, `0`, `""` (empty string), `null`, `undefined`, `NaN`
- ES6 (ECMAScript 2015) introduced `let`/`const`, arrow functions, template literals, classes, modules, destructuring, and Promises
- `addEventListener()` is preferred over inline event attributes (`onclick`) because it supports multiple listeners and propagation control
- The spread operator (`...`) expands an iterable into individual elements; the rest operator (`...`) collects multiple elements into an array
- JSON (JavaScript Object Notation) is derived from JavaScript object syntax and is the standard format for data exchange on the web

### Common Exam Questions
- Q: What will `typeof null` return? A: `"object"` -- this is a well-known JavaScript quirk.
- Q: Which method attaches an event handler to an element? A: `addEventListener('event', callback)`
- Q: What is hoisting? A: JavaScript moves `var` declarations and function declarations to the top of their scope before execution; `let` and `const` are hoisted but not initialized (temporal dead zone).
- Q: Write code to select all elements with class "item". A: `document.querySelectorAll('.item')` returns a NodeList of all matching elements.
- Q: What is the output of `console.log(1 + '2')`? A: `"12"` -- JavaScript coerces the number to a string and concatenates.

---

## jQuery

### Key Terms & Definitions
- **jQuery**: A fast, lightweight JavaScript library that simplifies DOM manipulation, event handling, animation, and AJAX
- **$() / jQuery()**: The jQuery selector function; accepts CSS selectors to select DOM elements and returns a jQuery object
- **jQuery Object**: A wrapped set of DOM elements returned by `$()` that provides access to jQuery methods
- **Chaining**: The ability to call multiple jQuery methods sequentially on the same selection because each method returns the jQuery object
- **CDN**: Content Delivery Network; a common way to include jQuery via a hosted URL rather than a local file
- **.on()**: The primary jQuery method for attaching event handlers; supports event delegation for dynamically created elements
- **.ajax()**: The core jQuery method for making asynchronous HTTP requests with configurable options (URL, method, callbacks)
- **.ready()**: `$(document).ready(fn)` ensures code runs after the DOM is fully loaded; shorthand: `$(function() {...})`
- **Event Delegation**: Binding an event handler to a parent element that listens for events on child elements, including those added dynamically
- **.detach()**: Removes elements from the DOM but preserves their jQuery data and event handlers for later reinsertion

### Core Concepts (Q&A Format)
- Q: How does jQuery simplify DOM selection compared to vanilla JavaScript?
- A: jQuery uses CSS-style selectors in `$()` -- e.g., `$('.class')`, `$('#id')`, `$('div > p')` -- returning a jQuery object with built-in methods, vs. verbose `document.querySelector` calls.

- Q: What is method chaining and why is it useful?
- A: Chaining calls multiple methods on the same jQuery object in one statement (e.g., `$('#box').addClass('active').fadeIn().css('color','red')`). It improves readability and performance since the browser does not re-select the element.

- Q: What is the difference between `.html()` and `.text()`?
- A: `.html()` gets/sets the inner HTML including tags; `.text()` gets/sets only the text content, escaping any HTML.

- Q: How does `.on()` support event delegation?
- A: By passing a child selector as the second argument: `$(parent).on('click', '.child', handler)`. This catches events from dynamically added `.child` elements.

- Q: What are jQuery's AJAX shorthand methods?
- A: `$.get()` for GET requests, `$.post()` for POST requests, `$.getJSON()` for JSON responses. All are wrappers around `$.ajax()`.

- Q: What does `$.when()` do?
- A: It accepts multiple Deferred/Promise objects and returns a master Promise that resolves when all inputs resolve, useful for coordinating parallel AJAX calls.

- Q: What is the difference between `.remove()` and `.detach()`?
- A: Both remove elements from the DOM, but `.detach()` preserves jQuery data and event handlers so the element can be reinserted with its bindings intact.

### Important Facts & Figures
- jQuery's motto is "Write less, do more"
- jQuery normalizes event behavior across different browsers, solving cross-browser compatibility issues
- `$(document).ready()` fires after the DOM is loaded but before images/stylesheets finish loading; shorter than `window.onload`
- jQuery is widely used in legacy systems and CMS platforms like WordPress
- The `$` symbol is an alias for the `jQuery` function; `jQuery.noConflict()` releases `$` for other libraries
- Global AJAX handlers (`ajaxStart`, `ajaxComplete`, `ajaxError`) allow centralized monitoring of all AJAX requests
- jQuery 3.x is the current major version, with improved Promise/A+ compliance and removal of deprecated APIs

### Common Exam Questions
- Q: What does `$('ul li').first().css('color', 'red')` do? A: Selects all `<li>` elements inside `<ul>` elements, takes the first one, and sets its text color to red.
- Q: How do you hide an element with jQuery? A: `$('#element').hide()` sets `display: none`; `.show()` reverses it; `.toggle()` switches between both states.
- Q: What is the shorthand for `$(document).ready(function() {})`? A: `$(function() {})`.
- Q: How do you make a GET request that expects JSON? A: `$.getJSON('url', function(data) { /* use data */ })`.
- Q: What is the purpose of `.each()` in jQuery? A: It iterates over a jQuery collection, executing a function for each matched element.

---

## CSS

### Key Terms & Definitions
- **CSS**: Cascading Style Sheets; a stylesheet language that controls the visual presentation (layout, colors, fonts, spacing) of HTML documents
- **Selector**: A pattern used to target HTML elements for styling (e.g., element, `.class`, `#id`, `[attribute]`, `:pseudo-class`, `::pseudo-element`)
- **Specificity**: The algorithm that determines which CSS rule wins when multiple rules target the same element; hierarchy: inline styles (1000) > ID (100) > class/attribute/pseudo-class (10) > element/pseudo-element (1)
- **Box Model**: Every element is a rectangular box with four layers: content, padding, border, and margin (from inside out)
- **Flexbox**: A one-dimensional layout model (`display: flex`) for distributing space along a single axis (row or column)
- **CSS Grid**: A two-dimensional layout system (`display: grid`) for managing rows and columns simultaneously
- **Media Query**: A `@media` rule that applies styles conditionally based on viewport width, device type, or orientation for responsive design
- **Cascade**: The set of rules determining which styles take effect: origin (user-agent, author, user), specificity, and source order
- **Inheritance**: Some CSS properties (e.g., `color`, `font-family`) are automatically passed from parent to child elements; others (e.g., `margin`, `padding`) are not
- **`box-sizing: border-box`**: Makes padding and border included in the element's total width and height, simplifying layout calculations
- **Viewport Units**: `vw` (1% of viewport width), `vh` (1% of viewport height); relative units useful for responsive design

### Core Concepts (Q&A Format)
- Q: What are the four components of the CSS box model, from inside out?
- A: Content (the actual text/image area), padding (space between content and border), border (the edge around padding), margin (space outside the border separating the element from others).

- Q: How does specificity work when two rules conflict?
- A: The rule with higher specificity wins: inline styles > IDs > classes/attributes/pseudo-classes > elements. If specificity is equal, the last rule in source order wins.

- Q: When would you use Flexbox vs. CSS Grid?
- A: Flexbox for one-dimensional layouts (a row of buttons, a vertical navigation list). Grid for two-dimensional layouts (a full page layout with defined rows and columns).

- Q: What is responsive design and how is it achieved?
- A: Designing websites that adapt to different screen sizes. Achieved using media queries (`@media (max-width: 768px) {...}`), relative units (`em`, `rem`, `%`, `vw`), and flexible layout systems (Flexbox, Grid).

- Q: What is the difference between `margin` and `padding`?
- A: Padding is space inside the element's border (between content and border); margin is space outside the border (between the element and neighboring elements). Background color fills padding but not margin.

- Q: What does `display: none` vs. `visibility: hidden` do?
- A: `display: none` removes the element from the layout entirely (no space reserved); `visibility: hidden` hides the element but it still occupies space in the layout.

- Q: What are CSS transitions and animations?
- A: Transitions smoothly animate property changes between two states (e.g., on hover). Animations use `@keyframes` to define multi-step sequences with full control over timing and iteration.

### Important Facts & Figures
- The three ways to include CSS: inline (`style` attribute), internal (`<style>` tag in `<head>`), external (linked `.css` file via `<link>`)
- `!important` overrides all specificity but should be used sparingly as it makes debugging difficult
- Flexbox key properties: `justify-content` (main axis), `align-items` (cross axis), `flex-wrap`, `flex-grow`, `flex-shrink`, `flex-basis`
- Grid key properties: `grid-template-columns`, `grid-template-rows`, `grid-gap`, `grid-area`, `fr` unit (fractional)
- The `fr` unit in Grid represents a fraction of available space (e.g., `1fr 2fr` gives 1/3 and 2/3)
- CSS preprocessors like Sass/SCSS add variables, nesting, and mixins to standard CSS
- Margin collapse: adjacent vertical margins of block elements collapse to the larger value, not the sum

### Common Exam Questions
- Q: What is the default value of `position` in CSS? A: `static` -- the element follows normal document flow.
- Q: Which has higher specificity: `.nav .link` or `#menu`? A: `#menu` (specificity 100) beats `.nav .link` (specificity 20).
- Q: What does `box-sizing: border-box` do? A: It includes padding and border in the element's declared width and height, so a `width: 200px` element with `padding: 20px` remains 200px total.
- Q: How do you center a div horizontally with CSS? A: Set a width and use `margin: 0 auto;` or use Flexbox: parent gets `display: flex; justify-content: center;`.
- Q: What is the difference between `em` and `rem`? A: `em` is relative to the parent element's font size; `rem` is relative to the root (`<html>`) font size.

---

## Web Design Principles

### Key Terms & Definitions
- **Visual Hierarchy**: The arrangement of elements by importance using size, color, contrast, and placement to guide the user's eye in a deliberate order
- **Typography**: The art of selecting and arranging typefaces; includes font family, size, weight, line-height, and letter-spacing
- **Color Theory**: The study of how colors interact, create contrast, and evoke emotions; guides palette selection for branding and usability
- **Whitespace (Negative Space)**: Intentional empty space around elements that reduces clutter, improves readability, and creates visual breathing room
- **60-30-10 Rule**: A color proportion guideline: 60% dominant color, 30% secondary color, 10% accent color for balanced visual design
- **F-Pattern / Z-Pattern**: Common reading patterns on web pages; F-pattern for text-heavy pages, Z-pattern for minimal-text layouts
- **Contrast**: The difference between elements (color, size, weight) that creates visual distinction and draws attention
- **Proximity**: Grouping related elements close together to indicate they belong to the same category or function
- **Alignment**: Placing elements along common edges or axes to create order, cohesion, and a professional appearance
- **User-Centered Design (UCD)**: A design philosophy that prioritizes the needs, goals, and behaviors of the target audience through research and iterative testing

### Core Concepts (Q&A Format)
- Q: What is visual hierarchy and why does it matter?
- A: It is the deliberate arrangement of design elements so users see the most important information first. It guides attention flow and improves comprehension.

- Q: Explain the 60-30-10 color rule.
- A: 60% of the design uses the dominant/background color, 30% uses a secondary color for contrast, and 10% uses an accent color to highlight calls-to-action or key elements.

- Q: How does whitespace improve a design?
- A: It reduces cognitive load, increases readability, separates distinct sections, and creates a sense of elegance and professionalism. It is an active design tool, not wasted space.

- Q: What is the difference between the F-pattern and Z-pattern?
- A: The F-pattern applies to text-heavy pages (users scan horizontally across the top, then down the left side). The Z-pattern applies to simpler layouts (users scan in a Z shape: top-left to top-right, diagonally down, bottom-left to bottom-right).

- Q: Why should you limit typefaces to 2-3 per page?
- A: Too many fonts create visual chaos and inconsistency. A limited palette (one for headings, one for body, optionally one for accents) establishes clear hierarchy and brand identity.

- Q: What is the principle of consistency in web design?
- A: Using uniform styling for buttons, links, headings, colors, and spacing across all pages builds user familiarity, trust, and reduces the learning curve.

- Q: How does the Rule of Thirds apply to web design?
- A: Dividing the layout into a 3x3 grid and placing key elements at intersections creates naturally balanced and visually engaging compositions.

### Important Facts & Figures
- Nielsen Norman Group research shows users spend 80% of their viewing time on the left half of a page (F-pattern)
- Sans-serif fonts (Arial, Helvetica, Roboto) are preferred for screen readability; serif fonts (Times, Georgia) are preferred for print
- Contrast ratio of at least 4.5:1 is required for normal text (WCAG AA compliance)
- Users form a first impression of a website in approximately 50 milliseconds
- The Gestalt principles (proximity, similarity, continuity, closure) explain how humans perceive grouped visual elements
- Calls-to-action (CTAs) should use the 10% accent color to stand out from surrounding content
- Mobile-first design starts with the smallest screen and progressively enhances for larger screens

### Common Exam Questions
- Q: Name three ways to establish visual hierarchy on a page. A: Size (larger elements draw attention first), color/contrast (bright or high-contrast elements stand out), and placement (top and center positions are seen first).
- Q: What Gestalt principle explains why items near each other appear related? A: Proximity -- elements close together are perceived as belonging to the same group.
- Q: Why is color alone not sufficient to convey information? A: Users with color blindness may not distinguish the colors; information must also be communicated through text, icons, or patterns (an accessibility requirement).
- Q: What is the purpose of a grid system in web design? A: It provides a consistent structure for aligning elements, creating visual order, and maintaining proportional spacing across the layout.

---

## Accessibility

### Key Terms & Definitions
- **Web Accessibility**: The practice of ensuring websites are usable by all people, including those with visual, auditory, motor, or cognitive disabilities
- **WCAG**: Web Content Accessibility Guidelines; the international standard published by W3C for accessible web content (current versions: 2.1 and 2.2)
- **POUR Principles**: The four foundational principles of WCAG: Perceivable, Operable, Understandable, Robust
- **ARIA**: Accessible Rich Internet Applications (WAI-ARIA); a set of roles, states, and properties that supplement HTML to improve accessibility of dynamic content
- **Screen Reader**: Assistive technology that reads page content aloud for users with visual impairments (e.g., JAWS, NVDA, VoiceOver)
- **Alt Text**: The `alt` attribute on `<img>` tags providing a text description of the image for screen readers and when images fail to load
- **Focus Indicator**: A visible outline or highlight on the currently focused interactive element, essential for keyboard navigation
- **Tab Order**: The sequence in which interactive elements receive focus when the user presses the Tab key; should follow a logical reading order
- **Contrast Ratio**: The measured difference in luminance between foreground text and background; WCAG AA requires 4.5:1 for normal text and 3:1 for large text
- **Assistive Technology**: Any device or software that helps people with disabilities interact with content (screen readers, switch devices, magnifiers)

### Core Concepts (Q&A Format)
- Q: What do the POUR principles stand for?
- A: Perceivable (content can be sensed), Operable (interface can be navigated and used), Understandable (content and UI are comprehensible), Robust (content works across diverse technologies and assistive devices).

- Q: What is the first rule of ARIA?
- A: Use native HTML elements with built-in semantics whenever possible before adding ARIA attributes. A `<button>` is inherently accessible; a styled `<div>` is not.

- Q: Why is keyboard navigation important for accessibility?
- A: Many users cannot use a mouse (motor disabilities, screen reader users). All interactive elements must be operable via keyboard alone with visible focus indicators and a logical tab order.

- Q: What are the WCAG conformance levels?
- A: Level A (minimum, essential barriers removed), Level AA (recommended target for most websites, addresses major barriers), Level AAA (highest, most restrictive standard).

- Q: How should images be handled for accessibility?
- A: Informative images need descriptive `alt` text. Decorative images should have `alt=""` (empty) so screen readers skip them. Complex images may need extended descriptions.

- Q: What is the purpose of `aria-label` and `aria-live`?
- A: `aria-label` provides an accessible name for elements without visible text labels. `aria-live` announces dynamic content changes to screen readers (values: `polite`, `assertive`, `off`).

- Q: What laws mandate web accessibility?
- A: The ADA (Americans with Disabilities Act), Section 508 of the Rehabilitation Act (US federal agencies), and the European Accessibility Act, among others.

### Important Facts & Figures
- WCAG 2.1 has 78 success criteria organized under the four POUR principles across three conformance levels (A, AA, AAA)
- Approximately 15% of the global population lives with some form of disability (WHO estimate)
- Color should never be the sole means of conveying information (e.g., red text for errors must also include an icon or label)
- Tools for accessibility auditing: Lighthouse (Chrome), axe (browser extension), WAVE (web tool)
- Links should have descriptive text ("Read the accessibility report") not generic text ("Click here")
- Skip navigation links allow keyboard users to bypass repetitive menus and jump directly to main content
- Video content requires captions (for deaf/hard-of-hearing users) and audio descriptions (for blind users)

### Common Exam Questions
- Q: What contrast ratio is required for normal text under WCAG AA? A: 4.5:1 minimum between text color and background color.
- Q: What is the difference between `aria-label` and `aria-labelledby`? A: `aria-label` provides a direct text label; `aria-labelledby` references the `id` of another visible element whose text serves as the label.
- Q: True or False: Adding `role="button"` to a `<div>` makes it fully accessible as a button. A: False -- you also need keyboard event handlers (`Enter`/`Space`), `tabindex="0"`, and focus management. Using a native `<button>` is preferred.
- Q: Name three accessibility testing tools. A: Lighthouse (built into Chrome DevTools), axe (browser extension by Deque), WAVE (Web Accessibility Evaluation Tool).
- Q: What does a skip navigation link do? A: It provides a hidden (until focused) link at the top of the page that allows keyboard users to skip past the navigation menu and jump directly to the main content.

---

## Client-Side Development

### Key Terms & Definitions
- **Client-Side**: Code that executes in the user's web browser rather than on a remote server; includes HTML, CSS, and JavaScript
- **Browser Rendering Pipeline**: The process by which a browser converts code into pixels: parse HTML into DOM, apply CSS into CSSOM, build render tree, layout (reflow), paint, composite
- **SPA (Single-Page Application)**: A web application that loads a single HTML shell and dynamically updates content via JavaScript without full page reloads
- **CSR (Client-Side Rendering)**: The browser receives minimal HTML and uses JavaScript to build and render all page content
- **SSR (Server-Side Rendering)**: The server generates complete HTML and sends it to the browser, which displays it immediately; used for faster initial load and better SEO
- **Hydration**: The process where client-side JavaScript takes over a server-rendered HTML page, attaching event listeners and making it interactive
- **DevTools**: Built-in browser developer tools for inspecting the DOM, debugging JavaScript, monitoring network requests, profiling performance, and auditing accessibility
- **Module Bundler**: A tool (Webpack, Vite, Parcel) that compiles, bundles, and optimizes multiple JavaScript modules and assets into production-ready files
- **State Management**: Patterns and tools for organizing and synchronizing application data across components (e.g., Redux, Pinia, React Context)
- **Virtual DOM**: An in-memory representation of the real DOM used by frameworks like React to minimize expensive direct DOM manipulations by batching updates

### Core Concepts (Q&A Format)
- Q: What is the browser rendering pipeline?
- A: The browser parses HTML into a DOM tree, parses CSS into a CSSOM, combines them into a render tree, calculates layout (position and size of elements), paints pixels, and composites layers onto the screen.

- Q: What is the difference between CSR and SSR?
- A: CSR sends minimal HTML and JavaScript builds the page in the browser (slower initial load, better interactivity). SSR generates full HTML on the server (faster initial load, better SEO) but requires hydration for interactivity.

- Q: What is hydration?
- A: After the browser receives server-rendered HTML, JavaScript runs to attach event listeners and make the static page interactive. The browser "hydrates" the static content with dynamic behavior.

- Q: What is a Single-Page Application (SPA)?
- A: A web app that loads one HTML page and uses JavaScript to dynamically swap content as the user navigates, avoiding full page reloads. Frameworks like React, Vue, and Angular facilitate SPAs.

- Q: Why are build tools like Webpack and Vite used?
- A: They bundle multiple JS modules into optimized files, process CSS preprocessors, optimize images, enable tree-shaking (removing unused code), and provide development servers with hot module replacement.

- Q: What is state management and why is it needed?
- A: As SPAs grow complex, data shared across many components becomes hard to track. State management tools (Redux, Pinia) provide a centralized store with predictable update patterns.

- Q: What are the trade-offs of SPAs?
- A: Pros: smooth navigation, rich interactivity, reduced server load. Cons: slower initial load, SEO challenges, increased client-side complexity, requires JavaScript to render content.

### Important Facts & Figures
- The three pillars of client-side web: HTML (structure), CSS (presentation), JavaScript (behavior)
- React, Vue, and Angular are the three most widely used client-side frameworks/libraries
- Reflows (layout recalculations) are expensive operations; minimizing DOM changes improves performance
- Lazy loading defers loading of non-critical resources (images, scripts) until they are needed, improving initial page load time
- The Critical Rendering Path is the sequence of steps the browser takes to convert HTML, CSS, and JS into rendered pixels -- optimizing it is key to performance
- Service Workers enable offline functionality and caching strategies for Progressive Web Apps (PWAs)
- Next.js (React), Nuxt.js (Vue), and Angular Universal provide hybrid SSR/CSR capabilities

### Common Exam Questions
- Q: What are the steps of the browser rendering pipeline? A: Parse HTML to DOM, parse CSS to CSSOM, combine into render tree, calculate layout, paint, composite.
- Q: Name one advantage and one disadvantage of client-side rendering. A: Advantage: rich, app-like interactivity after initial load. Disadvantage: slower first meaningful paint because the browser must download and execute JavaScript before content appears.
- Q: What is the purpose of a Virtual DOM? A: It is an in-memory copy of the real DOM that frameworks use to batch and diff changes, updating only the parts of the real DOM that actually changed, improving performance.
- Q: What tool is built into Chrome for inspecting and debugging web pages? A: Chrome DevTools (accessible via F12 or right-click > Inspect).
- Q: What is tree-shaking? A: A build optimization that removes unused code (dead code elimination) from the final JavaScript bundle, reducing file size.
