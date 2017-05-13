#!/usr/bin/env python
# Verifi Application - Weather App
# https://github.com/computermax11/verifiweather.git

import BaseHTTPServer
import CGIHTTPServer
server = BaseHTTPServer.HTTPServer
handler = CGIHTTPServer.CGIHTTPRequestHandler
server_address = ("", 8000)
httpd = server(server_address, handler)
httpd.serve_forever()


