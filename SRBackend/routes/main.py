import importlib, os.path

routes = []

def listdirs(folder):
    return [d for d in os.listdir(folder) if os.path.isdir(os.path.join(folder, d))]


def recursivePathFinding(path, root=''):
    if root == '':
        root = path
    if path.split('/')[-1:] == 'var':
        path = path + listdirs(path)[0]
    rabbitHole = listdirs(path)

    methods = ['GET', 'POST', 'PUT', 'DELETE']
    for method in methods:
        filePath = path + '/' + method.lower() + '.py'
        if os.path.isfile(filePath):
            # https://i.ytimg.com/vi/CZFKWt3S2Ys/maxresdefault.jpg
            hanlderImport = importlib.import_module((path + '/' + method.lower()).replace('/', '.')[2:])
            if hasattr(hanlderImport, 'handler'):
                routes.append({
                    'path': path[root.__len__():].replace('var/', ':'),
                    'method': method,
                    'handler': hanlderImport.handler,
                    'middlewares': hanlderImport.middleswares if hasattr(hanlderImport, 'middlewares') else {}
                })
            else:
                print('\033[93mFile: "{}" exists, but has no handler function!\033[0m'.format(filePath))

    for deeperPath in rabbitHole:
        recursivePathFinding(path + '/' + deeperPath, root)


recursivePathFinding("./routes")
