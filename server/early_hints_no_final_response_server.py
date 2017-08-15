#!/usr/bin/env python3
"""
HTTP server in python:
    send 103 early hints only,
    no final response


"""
from http.server import BaseHTTPRequestHandler

import socketserver

PORT = 10300

class MyHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(103)
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
