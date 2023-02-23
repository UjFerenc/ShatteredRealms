import os, importlib

middlewares = {}

sources = [d for d in os.listdir('./middleware') if os.path.isdir(os.path.join('./middleware', d))]

for source in sources:
    if source == '__pycache__':
        continue

    sourcedMidlewares = os.listdir('./middleware/' + source)

    for middleware in sourcedMidlewares:
        if middleware == '__pycache__':
            continue

        print(('./middleware/{}/{}'.format(source, middleware)).replace('/', '.')[2:-3])
        middlewareImport = importlib.import_module(('./middleware/{}/{}'.format(source, middleware)).replace('/', '.')[2:-3])

        if middleware[:-3] in middlewares:
            print('\033 Middleware: {} is already exists! skipping file'.format(middleware))
            continue

        if not hasattr(middlewareImport, 'check'):
            print('\033 Middleware: {} found, but has no check function! \033'.format(middleware[:-3]))
            continue

        middlewares[middleware[:-3]] = middlewareImport.check