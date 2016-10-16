#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, HTTPServer
from docker import Client

from cgibin import generate,stats,container
import os

os.chdir("/www")
cli=Client()

PORT = int(os.environ.get('PORT',8000))

class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

  def do_GET(self):

        message=""
        Ctype=[]

        if (self.path=="/"):
            message = bytes(open("index.html").read(),"utf-8")
            Ctype=['Content-type','text/html']

        if (self.path=="/favicon.ico"):
            message = open("favicon.ico","rb").read()
            Ctype=['Content-type','image/png']

        if (self.path=="/cgi-bin/generate.py"):
            message=bytes(generate.GetInfo(cli),'utf8')
            Ctype=['Content-type','application/json']

        if (self.path=="/cgi-bin/stats.py"):
            message=bytes(stats.GetInfo(cli),'utf8')
            Ctype=['Content-type','application/json']

        if (self.path=="/cgi-bin/container.py"):
            message=bytes(container.GetInfo(cli),'utf8')
            Ctype=['Content-type','application/json']


        # Write content as utf-8 data
        if (message):
            self.send_response(200)
            # Send headers
            self.send_header(Ctype[0],Ctype[1])
            self.end_headers()
            self.wfile.write(message)
        else:
            self.send_response(404)
            self.end_headers()
            message="pena"
            self.wfile.write(bytes(message, "utf8"))

        return

def run():
  print('starting server...')
  # Server settings
  # Choose port 8080, for port 80, which is normally used for a http server, you need root access
  server_address = ("", 8000)
  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
  print('running server...')
  httpd.serve_forever()

run()
