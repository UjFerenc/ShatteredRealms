import importlib
import os.path


def list_dirs(folder):
    return [d for d in os.listdir(folder) if os.path.isdir(os.path.join(folder, d))]


def replace_path_variables(path, root):
    endpoint_path = ''
    split_path_array = path[root.__len__():].replace('var/', '{').split('{')
    for index, split_path in enumerate(split_path_array):
        if index != 0:
            if index < split_path_array.__len__():
                split_path = '{' + split_path + '}'
            else:
                split_path = split_path.replace('/', '}/', 1)

        endpoint_path += split_path
    return endpoint_path


def recursive_path_finding(app, path, root=''):
    if root == '':
        root = path
    if path.split('/')[-1:] == 'var':
        path = path + list_dirs(path)[0]
    rabbit_hole = list_dirs(path)

    methods = ['get', 'post', 'put', 'delete']
    for method in methods:
        file_path = path + '/' + method + '.py'
        if os.path.isfile(file_path):
            # https://i.ytimg.com/vi/CZFKWt3S2Ys/maxresdefault.jpg
            handler_import = importlib.import_module((path + '/' + method).replace('/', '.')[2:])
            if not hasattr(handler_import, 'tags'):
                handler_import.tags = ["default"]
            if not hasattr(handler_import, 'dependencies'):
                handler_import.dependencies = []
            if hasattr(handler_import, 'handler'):
                endpoint_path = replace_path_variables(path, root)
                getattr(app, method)(endpoint_path, tags=handler_import.tags, dependencies=handler_import.dependencies)(handler_import.handler)

            else:
                print('\033[93mFile: "{}" exists, but has no handler function!\033[0m'.format(file_path))

    for deeperPath in rabbit_hole:
        recursive_path_finding(app, path + '/' + deeperPath, root)
