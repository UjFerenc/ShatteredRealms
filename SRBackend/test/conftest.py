import os
import shutil
from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import app

client = None

def pytest_configure(config):
    print('pytest config started... ')
    src_file = "./test/database/mydatabase.db"
    dst_file = "./database"

    if os.path.exists(dst_file + 'mydatabase.db'):
        os.remove(dst_file + 'mydatabase.db')

    shutil.copy(src_file, dst_file)
    print('database successfully replaced...')

    global client
    client = TestClient(app)

def get_client():
    return client
