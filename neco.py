import csv
import json

from models import NearEarthObject, CloseApproach
from extract import load_approaches, load_neos
from database import NEODatabase
import pickle

database = NEODatabase(neos=load_neos(), approaches=load_approaches())

with open("database.pickle", "wb") as outfile:
    pickle.dump(database, outfile)
