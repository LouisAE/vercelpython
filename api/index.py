from http.server import BaseHTTPRequestHandler
from os.path import join,dirname,abspath
dirs = dirname(abspath(__file__))
 
class handler(BaseHTTPRequestHandler):
 
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plaintext')
        self.end_headers()
        #with open(dirs + "../data/404.html","r") as h:
            #self.wfile.write(h.encode())
        self.wfile.write( "<html><head><title>Hello World</title></head><body><div><p>Hello World</p></div></body></html>")
        return
