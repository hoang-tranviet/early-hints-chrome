#!/usr/bin/env python3
"""
HTTP server in python.

Send normal 200 OK response with preload header

To send a GET request:
    curl http://localhost:8000

"""
from http.server import BaseHTTPRequestHandler

import time
import socketserver

PORT = 8000

class MyHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        time.sleep(1000000)
        self.send_header('Link', '</stylesheets/screen.css>;rel=preload;as=style')
        self.end_headers()

    def do_GET(self):
        if (self.path.strip() == '/'):
            self._set_headers()
            self.wfile.write(bytes("<html><body><h1>hi!</h1></body></html>", "utf-8"))
        else:
            print("request for non-root object, not reply")

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
