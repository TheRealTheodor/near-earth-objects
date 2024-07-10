import csv

from models import NearEarthObject

with open("data/neos.csv", "r") as infile:
    reader = csv.reader(infile)
    print(next(reader))
    first_row = next(reader)
    print(first_row)
    neo = NearEarthObject(
        designation=first_row[3],
        name=first_row[4],
        diameter=first_row[15],
        hazardous=first_row[7],
    )
    print(neo)
