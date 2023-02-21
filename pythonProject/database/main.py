import importlib
import os

from sqlalchemy import create_engine

from database.base import Base

modelList = os.listdir("./database/models")
if '__pycache__' in modelList:
    modelList.remove('__pycache__')

for model in modelList:
    importlib.import_module('database.models.' + (model[:-3]))

engine = create_engine("sqlite:///database/mydb.db", echo=True)
Base.metadata.create_all(bind=engine)
