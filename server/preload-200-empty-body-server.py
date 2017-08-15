#!/usr/bin/env python3
"""
Very simple HTTP server in python.

To send a GET request:
    curl http://localhost:8000

"""
from http.server import BaseHTTPRequestHandler

import socketserver

PORT = 20000

class MyHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Link', '</stylesheets/screen.css>;rel=preload;as=style')
        self.end_headers()

    def do_GET(self):
        if (self.path.strip() == '/'):
            self._set_headers()
            #self.wfile.write(bytes("<html><body><h1>hi!</h1></body></html>", "utf-8"))
        else:
            print("request for non-root object, not reply")

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
