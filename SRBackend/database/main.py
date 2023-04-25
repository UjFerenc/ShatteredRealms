import importlib
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from utils.genericFunctions import list_dirs

from database.base import Base


def recursive_model_finding(root):
    folderList = list_dirs(root)
    if '__pycache__' in folderList:
        folderList.remove('__pycache__')
    if folderList.__len__() is not 0:
        for folder in folderList:
            recursive_model_finding(f'{root}/{folder}')
    else:
        modelList = os.listdir(root)
        for model in modelList:
            if '.py' in model:
                importlib.import_module(f'{root[2:].replace("/", ".")}.{model[:-3]}')


recursive_model_finding('./database/models')

engine = create_engine('sqlite:///database/mydatabase.db', echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()
