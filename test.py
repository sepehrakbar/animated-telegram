#!/usr/bin/env python3
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.request import urlopen, Request
کزمننلم
م
وو../../../....//
گ
import sys

TARGET_BASE = "http://youtube.com"  # <-- آدرس سایتی که می‌خواهید پروکسی شود

class ProxyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # ساخت URL کامل مقصد (حفظ مسیر و کوئری استرینگ)
        target_url = TARGET_BASE + self.path
        try:
            req = Request(target_url, headers={'User-Agent': 'Mozilla/5.0'})
            with urlopen(req) as response:
                content = response.read()
                self.send_response(200)
                self.send_header('Content-type', response.headers.get('Content-type', 'text/html'))
                self.end_headers()
                self.wfile.write(content)
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(f"Error: {e}".encode())

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 80), ProxyHandler)
    print("Proxy running on port 80...")
    server.serve_forever()
