from http.server import BaseHTTPRequestHandler
from os.path import join,dirname,abspath
dirs = dirname(abspath(__file__))
 
class handler(BaseHTTPRequestHandler):
 
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        with open(dirs + "\\..\\404.html","r",encoding="utf-8") as h:
            self.wfile.write(h.read().encode())
        return
