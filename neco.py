import csv

from models import NearEarthObject

with open("data/neos.csv", "r") as infile:
    reader = csv.reader(infile)
    for enum, row in enumerate(reader):
        if enum == 0:
            print(enum, row)
        if enum == 1:
            print(enum, row)
            first_row = row
        if enum == 282:
            no_name_row = row
    print(no_name_row)
    neo = NearEarthObject(
        designation=first_row[3],
        name=first_row[4],
        diameter=first_row[15],
        hazardous=first_row[7],
    )
    print(neo)
