import http.server
import socketserver
import json
from pathlib import Path

DATA_ROOT = Path('extracted_maestras')
PORT = 8000

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/tesis/'):
            number = self.path.split('/')[-1]
            file = DATA_ROOT / f'tesis_{number}' / 'tesis_maestra.json'
            if file.exists():
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(file.read_bytes())
                return
            else:
                self.send_error(404, 'Not Found')
                return
        return super().do_GET()

def run(server_class=http.server.HTTPServer, handler_class=Handler):
    with socketserver.TCPServer(('', PORT), handler_class) as httpd:
        print(f'Serving on port {PORT}')
        httpd.serve_forever()

if __name__ == '__main__':
    run()
