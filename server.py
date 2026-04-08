"""
Syllabot Server — Static file server + /upload + /generate endpoints.
Run: python server.py
"""
import http.server
import json
import os
import tempfile
import urllib.request
import re

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

# ===== CONTENT GENERATION ENGINE =====
# Generates quiz questions, written questions, and flashcards from module topics
# using keyword extraction and template-based question generation.

QUESTION_TEMPLATES = {
    "definition": [
        {"template": "Which of the following best defines {term}?", "type": "definition"},
        {"template": "The concept of {term} refers to:", "type": "definition"},
        {"template": "{term} is best described as:", "type": "definition"},
    ],
    "application": [
        {"template": "Which scenario best illustrates {term}?", "type": "application"},
        {"template": "A real-world example of {term} would be:", "type": "application"},
    ],
    "comparison": [
        {"template": "What is the key difference between {term_a} and {term_b}?", "type": "comparison"},
        {"template": "{term_a} differs from {term_b} in that:", "type": "comparison"},
    ],
    "cause_effect": [
        {"template": "What is the most likely result of {term}?", "type": "cause_effect"},
        {"template": "If {term} occurs, the expected outcome is:", "type": "cause_effect"},
    ],
}

FLASHCARD_TEMPLATES = [
    {"front": "Define {term}", "back_prompt": "definition"},
    {"front": "What is the significance of {term}?", "back_prompt": "significance"},
    {"front": "Give an example of {term}", "back_prompt": "example"},
    {"front": "How does {term} relate to the broader topic?", "back_prompt": "relationship"},
]

WRITTEN_TEMPLATES = [
    "Explain the concept of {term} and why it matters in the context of {topic}.",
    "Compare and contrast {term_a} and {term_b}. What are the key similarities and differences?",
    "Using a real-world example, explain how {term} works in practice.",
    "Why is {term} important for understanding {topic}? Discuss its implications.",
]


def scrape_topic_info(topic, reading=""):
    """Try to fetch relevant content from OpenStax or generate from topic keywords."""
    content_lines = []

    # Use the topic and reading info to generate keyword-rich context
    topic_lower = topic.lower()
    keywords = [w.strip() for w in re.split(r'[,&/]+', topic) if len(w.strip()) > 2]

    # Try to fetch from OpenStax if we have a chapter reference
    if reading:
        ch_match = re.search(r'Ch\.?\s*(\d+)', reading)
        if ch_match:
            chapter = ch_match.group(1)
            # Common OpenStax micro/macro URLs
            urls = [
                f"https://openstax.org/books/principles-microeconomics-3e/pages/{chapter}-introduction",
                f"https://openstax.org/books/principles-microeconomics-3e/pages/{chapter}-key-terms",
            ]
            for url in urls:
                try:
                    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                    with urllib.request.urlopen(req, timeout=5) as resp:
                        html = resp.read().decode('utf-8', errors='replace')
                        # Extract text between <p> tags
                        paragraphs = re.findall(r'<p[^>]*>(.+?)</p>', html, re.DOTALL)
                        for p in paragraphs:
                            text = re.sub(r'<[^>]+>', '', p).strip()
                            if len(text) > 30:
                                content_lines.append(text)
                except Exception:
                    pass

    return {
        'topic': topic,
        'keywords': keywords,
        'reading': reading,
        'scraped_content': content_lines[:20]  # Limit to prevent huge payloads
    }


def extract_key_terms(topic_info):
    """Extract key terms from topic info for question generation."""
    terms = list(topic_info['keywords'])

    # Extract capitalized terms from scraped content
    for line in topic_info.get('scraped_content', []):
        # Find terms that look like definitions (bold or capitalized multi-word phrases)
        found = re.findall(r'\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\b', line)
        for f in found:
            if len(f) > 3 and f not in terms and f.lower() not in ['the', 'this', 'that', 'these', 'those']:
                terms.append(f)

    # Common term extraction from topic name
    topic_words = re.split(r'[,&/]+', topic_info['topic'])
    for tw in topic_words:
        tw = tw.strip()
        if len(tw) > 2 and tw not in terms:
            terms.append(tw)

    return terms[:15]  # Limit


def generate_mcq(topic_info, terms, count=15):
    """Generate multiple choice questions from topic info and terms."""
    questions = []
    scraped = topic_info.get('scraped_content', [])
    topic = topic_info['topic']

    for i, term in enumerate(terms):
        if len(questions) >= count:
            break

        # Generate definition-style question
        correct_text = ""
        for line in scraped:
            if term.lower() in line.lower() and len(line) > 40:
                # Use the scraped line as the correct answer basis
                correct_text = line[:150]
                break

        if not correct_text:
            correct_text = f"A key concept in {topic} related to {term}"

        # Create plausible wrong answers
        wrong = [
            f"An unrelated concept from a different field of study",
            f"The opposite of what {term} actually describes",
            f"A concept that only applies in theoretical models, not real-world scenarios",
        ]

        q = {
            "q": f"Which of the following best describes {term} in the context of {topic}?",
            "opts": [wrong[0], correct_text, wrong[1], wrong[2]],
            "correct": 1,
            "explain": f"{term} is a key concept in {topic}. {correct_text}"
        }
        questions.append(q)

        # Generate application question if we have enough terms
        if i + 1 < len(terms) and len(questions) < count:
            q2 = {
                "q": f"How does {term} relate to the study of {topic}?",
                "opts": [
                    f"It provides a framework for understanding real-world {topic.lower()} scenarios",
                    f"It only applies to advanced graduate-level coursework",
                    f"It has been disproven by modern research",
                    f"It is only relevant to a different subject area entirely"
                ],
                "correct": 0,
                "explain": f"{term} is fundamental to understanding {topic} and has practical real-world applications."
            }
            questions.append(q2)

    return questions


def generate_flashcards(topic_info, terms, count=12):
    """Generate flashcards from topic info and terms."""
    cards = []
    scraped = topic_info.get('scraped_content', [])
    topic = topic_info['topic']

    for term in terms:
        if len(cards) >= count:
            break

        # Find the best scraped description
        description = f"A key concept in {topic}."
        for line in scraped:
            if term.lower() in line.lower() and len(line) > 30:
                description = line[:300]
                break

        cards.append({
            "front": f"What is {term}?",
            "back": description
        })

        # Add a second card for important terms
        if len(cards) < count:
            cards.append({
                "front": f"Why is {term} important in {topic}?",
                "back": f"{term} is significant because it helps explain key patterns and relationships in {topic}. Understanding {term} is essential for analyzing real-world situations in this field."
            })

    return cards


def generate_written(topic_info, terms, count=3):
    """Generate written response questions."""
    questions = []
    topic = topic_info['topic']

    if len(terms) >= 1:
        questions.append({
            "q": f"Explain the concept of {terms[0]} and why it matters in {topic}.",
            "keywords": [t.lower() for t in terms[:5]] + [topic.lower().split()[0]],
            "idealAnswer": f"{terms[0]} is a fundamental concept in {topic}. It helps us understand how key mechanisms work in this area of study. Understanding {terms[0]} is essential because it provides the foundation for analyzing real-world scenarios related to {topic}."
        })

    if len(terms) >= 3:
        questions.append({
            "q": f"Compare and contrast {terms[0]} and {terms[1]}. How do they relate to each other within {topic}?",
            "keywords": [terms[0].lower(), terms[1].lower(), "difference", "similar", "compare", topic.lower().split()[0]],
            "idealAnswer": f"{terms[0]} and {terms[1]} are both important concepts in {topic}. While they share some similarities, they differ in key ways. {terms[0]} focuses on one aspect, while {terms[1]} addresses another dimension. Together, they provide a more complete picture of {topic}."
        })

    if len(terms) >= 2:
        questions.append({
            "q": f"Using a real-world example, explain how {terms[1] if len(terms) > 1 else terms[0]} works in practice. Why is this concept relevant?",
            "keywords": [terms[1].lower() if len(terms) > 1 else terms[0].lower(), "example", "real world", "practice", "relevant"],
            "idealAnswer": f"A real-world example of {terms[1] if len(terms) > 1 else terms[0]} can be seen in everyday economic decisions. This concept is relevant because it directly impacts how individuals, firms, or governments make choices in the context of {topic}."
        })

    return questions[:count]


def generate_content_for_modules(course_name, modules, types):
    """Main generation function — processes all modules and returns content."""
    result = {}
    if types.get('quiz'):
        result['quiz'] = {}
    if types.get('written'):
        result['written'] = {}
    if types.get('flashcards'):
        result['flashcards'] = {}

    for mod in modules:
        module_key = f"Module {mod['num']}"
        topic = mod['topic']
        reading = mod.get('reading', '')

        # Scrape and analyze
        topic_info = scrape_topic_info(topic, reading)
        terms = extract_key_terms(topic_info)

        if types.get('quiz'):
            result['quiz'][module_key] = generate_mcq(topic_info, terms)

        if types.get('written'):
            result['written'][module_key] = generate_written(topic_info, terms)

        if types.get('flashcards'):
            result['flashcards'][module_key] = generate_flashcards(topic_info, terms)

    return result


# ===== FILE PARSING =====
def parse_docx(filepath):
    from docx import Document
    doc = Document(filepath)
    lines = []
    for p in doc.paragraphs:
        if p.text.strip():
            lines.append(p.text)
    for table in doc.tables:
        for row in table.rows:
            cells = [cell.text.strip() for cell in row.cells if cell.text.strip()]
            if cells:
                lines.append('\t'.join(cells))
    return '\n'.join(lines)


def parse_pdf(filepath):
    import pdfplumber
    text_parts = []
    with pdfplumber.open(filepath) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                text_parts.append(text)
            tables = page.extract_tables()
            for table in tables:
                for row in table:
                    cells = [c.strip() if c else '' for c in row]
                    if any(cells):
                        text_parts.append('\t'.join(cells))
    return '\n'.join(text_parts)


def parse_multipart(body, content_type):
    """Manually parse multipart/form-data since cgi module is removed in Python 3.13+."""
    boundary = None
    for part in content_type.split(';'):
        part = part.strip()
        if part.startswith('boundary='):
            boundary = part[9:].strip('"')
            break
    if not boundary:
        return None, None

    boundary_bytes = ('--' + boundary).encode()
    parts = body.split(boundary_bytes)

    for part in parts:
        if b'filename=' not in part:
            continue
        header_end = part.find(b'\r\n\r\n')
        if header_end == -1:
            continue
        headers = part[:header_end].decode('utf-8', errors='replace')
        file_content = part[header_end + 4:]
        if file_content.endswith(b'--\r\n'):
            file_content = file_content[:-4]
        elif file_content.endswith(b'\r\n'):
            file_content = file_content[:-2]

        filename = None
        for line in headers.split('\r\n'):
            if 'filename=' in line:
                fn_start = line.index('filename=') + 9
                fn = line[fn_start:].strip('"').strip("'")
                if '"' in line[fn_start:]:
                    fn = line[fn_start:].split('"')[1]
                filename = fn
                break
        return file_content, filename

    return None, None


# ===== HTTP HANDLER =====
class SyllabotHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_POST(self):
        if self.path == '/upload':
            self.handle_upload()
        elif self.path == '/generate':
            self.handle_generate()
        else:
            self.send_error(404, 'Not Found')

    def handle_generate(self):
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length)
        try:
            data = json.loads(body.decode('utf-8'))
            course_name = data.get('course', 'Unknown Course')
            modules = data.get('modules', [])
            types = data.get('types', {'quiz': True, 'written': True, 'flashcards': True})

            if not modules:
                self.send_json(400, {'error': 'No modules provided'})
                return

            print(f'[GENERATE] Generating content for {course_name}: {len(modules)} modules')
            result = generate_content_for_modules(course_name, modules, types)
            print(f'[GENERATE] Done. Quiz modules: {len(result.get("quiz", {}))}, Flashcard modules: {len(result.get("flashcards", {}))}')
            self.send_json(200, result)

        except json.JSONDecodeError:
            self.send_json(400, {'error': 'Invalid JSON'})
        except Exception as e:
            print(f'[GENERATE ERROR] {e}')
            self.send_json(500, {'error': str(e)})

    def handle_upload(self):
        content_type = self.headers.get('Content-Type', '')
        content_length = int(self.headers.get('Content-Length', 0))

        if 'multipart/form-data' not in content_type:
            self.send_json(400, {'error': 'Expected multipart/form-data'})
            return

        body = self.rfile.read(content_length)
        file_content, filename = parse_multipart(body, content_type)

        if not file_content or not filename:
            self.send_json(400, {'error': 'No file found in upload'})
            return

        ext = os.path.splitext(filename)[1].lower()
        if ext not in ('.pdf', '.docx', '.doc', '.txt', '.json'):
            self.send_json(400, {'error': f'Unsupported file type: {ext}. Use .pdf, .docx, .txt, or .json'})
            return

        with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as tmp:
            tmp.write(file_content)
            tmp_path = tmp.name

        try:
            if ext in ('.docx', '.doc'):
                text = parse_docx(tmp_path)
            elif ext == '.pdf':
                text = parse_pdf(tmp_path)
            elif ext == '.json':
                with open(tmp_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                self.send_json(200, {'type': 'json', 'data': data, 'filename': filename})
                return
            else:
                with open(tmp_path, 'r', encoding='utf-8') as f:
                    text = f.read()

            self.send_json(200, {'type': 'text', 'text': text, 'filename': filename})
        except Exception as e:
            self.send_json(500, {'error': f'Failed to parse {filename}: {str(e)}'})
        finally:
            os.unlink(tmp_path)

    def send_json(self, code, data):
        body = json.dumps(data).encode('utf-8')
        self.send_response(code)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', len(body))
        self.end_headers()
        self.wfile.write(body)

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()


if __name__ == '__main__':
    print(f'Syllabot server running at http://localhost:{PORT}')
    print(f'Serving files from: {DIRECTORY}')
    print('Endpoints:')
    print('  POST /upload   — accepts .pdf, .docx, .txt, .json')
    print('  POST /generate — generates quiz/flashcard/written content from module topics')
    server = http.server.HTTPServer(('', PORT), SyllabotHandler)
    server.serve_forever()
