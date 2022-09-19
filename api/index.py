from http.server import BaseHTTPRequestHandler,HTTPServer
from requests import get
from os.path import join,dirname,abspath
import json
import dns.message
dirs = dirname(abspath(__file__))
 
class handler(BaseHTTPRequestHandler):
 
    def do_GET(self):
        if "dns" not in self.path:
            self.send_response(400)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open(dirs + "/../data/400.html","r",encoding="utf-8") as h:
                self.wfile.write(h.read().encode())
            return
        else:
            dnsres = get("https://1.0.0.1/dns-query"+self.path[1:],
                         headers={"Content-type": "application/dns-message"})
            if dnsres.status_code != 200:
                self.send_response_only(dnsres.status_code)
                return
            rhead = dict(dnsres.headers)
            self.send_response(200)
            self.send_header('Content-Type',rhead['Content-Type'])
            self.send_header('Date',rhead['Date'])
            self.send_header('Content-Length',rhead['Content-Length'])
            self.end_headers()
            self.wfile.write(dnsres.content)
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        with open(dirs + "/../data/404.html","r",encoding="utf-8") as h:
            self.wfile.write(h.read().encode())
        return
