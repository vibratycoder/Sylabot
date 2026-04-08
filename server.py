"""
Syllabot Server — Static file server + /upload endpoint for PDF/DOCX parsing.
Run: python server.py
"""
import http.server
import json
import os
import tempfile

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))


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
    # Extract boundary from content-type
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
        # Split headers from content
        header_end = part.find(b'\r\n\r\n')
        if header_end == -1:
            continue
        headers = part[:header_end].decode('utf-8', errors='replace')
        file_content = part[header_end + 4:]
        # Remove trailing \r\n-- if present
        if file_content.endswith(b'--\r\n'):
            file_content = file_content[:-4]
        elif file_content.endswith(b'\r\n'):
            file_content = file_content[:-2]

        # Extract filename
        filename = None
        for line in headers.split('\r\n'):
            if 'filename=' in line:
                fn_start = line.index('filename=') + 9
                fn = line[fn_start:].strip('"').strip("'")
                # Handle case where there's a ; after filename
                if '"' in line[fn_start:]:
                    fn = line[fn_start:].split('"')[1]
                filename = fn
                break
        return file_content, filename

    return None, None


class SyllabotHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_POST(self):
        if self.path == '/upload':
            self.handle_upload()
        else:
            self.send_error(404, 'Not Found')

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

        # Save to temp file
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
            else:  # .txt
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
    print('Upload endpoint: POST /upload (accepts .pdf, .docx, .txt, .json)')
    server = http.server.HTTPServer(('', PORT), SyllabotHandler)
    server.serve_forever()
