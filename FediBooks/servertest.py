#!/usr/bin/env python3
from http import server
import urllib
import json

class TestServer(server.BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.end_headers()
		print(urllib.parse.parse_qs(self.path[2:]))

def run(server_class=server.ThreadingHTTPServer, handler_class=TestServer):
	server_address = ('127.0.0.1', 0)
	httpd = server_class(server_address, handler_class)
	print(httpd.RequestHandlerClass)
	print(httpd.server_port)
	httpd.serve_forever()

run()
