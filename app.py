import json
from http.server import BaseHTTPRequestHandler,  HTTPServer
import os

PORT = 7000
APP_VERSION = os.environ.get("APP_VERSION", "development")

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':

            response = {
                    "status": "ok",
                    "version": APP_VERSION
                    }

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())

        else:
            self.send_response(404)
            self.end_headers()

server = HTTPServer(("0.0.0.0", PORT), Handler)
print(f"Application running version {APP_VERSION} on internal port {PORT}")
server.serve_forever()


