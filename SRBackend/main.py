from fastapi import FastAPI
from routing.main import recursive_path_finding

app = FastAPI(title='ShatteredRealms API')

recursive_path_finding(app, './routing/routes')
