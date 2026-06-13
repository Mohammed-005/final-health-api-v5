import json
from http.server import BaseHTTPRequestHandler,  HTTPServer
import redis
import os

PORT = 7000
REDIS_HOST = os.environ.get("REDIS_HOST", "redis")

r = redis.Redis(host=REDIS_HOST, port=6379, decode_responses=True)

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            visits = r.incr("visits")

            response = {
                    "status": "ok",
                    "visits": int(visits),
                    "version": "v5",
                    "service": "final-practice"
                    }

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())

        else:
            self.send_response(404)
            self.end_headers()

server = HTTPServer(("0.0.0.0", PORT), Handler)
print(f"Server running on port {PORT}")
server.serve_forever()


