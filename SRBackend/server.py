from http.server import BaseHTTPRequestHandler
from routes.main import routes
from database import main
from middleware.main import middlewares

import json

class Server(BaseHTTPRequestHandler):
    def sendResponse(self, code, message):
        self.send_response(code)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(message.encode() if isinstance(message, str) else (json.dumps(message)))
        self.end_headers()

    def do_HEAD(self):
        return

    def do_GET(self):
        self.doRoute(routes, 'GET', self.path)

    def do_POST(self):
        self.doRoute(routes, 'POST', self.path)

    def do_PUT(self):
        self.doRoute(routes, 'PUT', self.path)

    def do_DELETE(self):
        self.doRoute(routes, 'DELETE', self.path)

    def doRoute(self, routes, method, path):
        if path == '/':
            path = ''

        for route in routes:
            if route['method'] != method:
                continue

            splitRoutePath = route['path'].split('/')
            splitRequestPath = path.split('/')
            if splitRoutePath.__len__() != splitRequestPath.__len__():
                continue

            match = True
            pathVariables = {}
            for index, requestPath in enumerate(splitRequestPath):
                if splitRoutePath[index][:1] == ':':
                    pathVariables[splitRoutePath[index][1:]] = requestPath
                    continue

                if requestPath != splitRoutePath[index]:
                    match = False
                    break

            if match:
                self.pathVariables = pathVariables if pathVariables else {}
                if self.headers['Content-Type'] == 'application/json' and self.headers['Content-Length']:
                    try:
                        self.jsonData = json.loads((self.rfile.read(int(self.headers['Content-Length'])).decode()))
                    except json.decoder.JSONDecodeError as e:
                        self.send_response(400)
                        self.send_header("Content-type", "text/html")
                        self.end_headers()
                        self.wfile.write('INVALID_JSON'.encode())
                        return
                for middleware in route['middlewares']:
                    if not middlewares[middleware]():
                        return
                return route['handler'](self)

