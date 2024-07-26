import csv
import json
import pickle

from database import NEODatabase
from extract import load_approaches, load_neos
from models import CloseApproach, NearEarthObject

database = NEODatabase(neos=load_neos(), approaches=load_approaches())

with open("database.pickle", "wb") as outfile:
    pickle.dump(database, outfile)
