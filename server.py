"""
server.py — RuleBot Web Server
Uses ONLY Python built-in libraries (http.server, json, urllib)
No Flask, Django, or any third-party packages required.
"""

import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse

# Import core chatbot logic (sanitise + process functions)
from chatbot import sanitise, process

HOST = "localhost"
PORT = 8000
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class RuleBotHandler(BaseHTTPRequestHandler):
    """Handles all incoming HTTP requests."""

    # ── GET — serve static files ───────────────────────────
    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        if path == "/" or path == "/index.html":
            self._serve_file("index.html", "text/html")
        else:
            self._send_404()

    # ── POST — handle chat API ─────────────────────────────
    def do_POST(self):
        if self.path == "/chat":
            try:
                # INPUT: Read and parse request body
                length = int(self.headers.get("Content-Length", 0))
                body = self.rfile.read(length)
                data = json.loads(body)
                raw_input = data.get("message", "")

                # PROCESS: Sanitize then apply if-else + dict logic
                clean_input = sanitise(raw_input)
                response, should_exit = process(clean_input)

                # OUTPUT: Send JSON response back to browser
                self._send_json(200, {"message": response, "exit": should_exit})

            except (json.JSONDecodeError, KeyError):
                self._send_json(400, {"message": "Invalid request.", "exit": False})
        else:
            self._send_404()

    # ── Helpers ────────────────────────────────────────────
    def _serve_file(self, filename, content_type):
        filepath = os.path.join(BASE_DIR, filename)
        try:
            with open(filepath, "rb") as f:
                content = f.read()
            self.send_response(200)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()
            self.wfile.write(content)
        except FileNotFoundError:
            self._send_404()

    def _send_json(self, status, data):
        body = json.dumps(data).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _send_404(self):
        self.send_response(404)
        self.end_headers()
        self.wfile.write(b"404 Not Found")

    def log_message(self, format, *args):
        print(f"  [server] {self.address_string()} — {format % args}")


# ── Entry point ────────────────────────────────────────────
def run():
    server = HTTPServer((HOST, PORT), RuleBotHandler)
    print("=" * 50)
    print("  RuleBot Web Server 🤖")
    print("  DecodeLabs 2026 — Rule-Based AI Chatbot")
    print(f"  Running at: http://{HOST}:{PORT}")
    print("  Press Ctrl+C to stop.")
    print("=" * 50)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n  Server stopped. Goodbye!")
        server.server_close()


if __name__ == "__main__":
    run()