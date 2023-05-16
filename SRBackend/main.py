from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

app = FastAPI(title='ShatteredRealms API')

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from routing.main import recursive_path_finding
recursive_path_finding(app, './routing/routes')
