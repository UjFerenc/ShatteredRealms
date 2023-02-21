from http.server import BaseHTTPRequestHandler

from routes.main import routes


class Server(BaseHTTPRequestHandler):
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
                if pathVariables.keys().__len__() > 0:
                    return route['handler'](self, pathVariables)
                route['handler'](self)
