import csv
import json

from models import NearEarthObject, CloseApproach

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


with open("data/cad.json", "r") as infile:
    contents = json.load(infile)
print(contents["fields"])
print(contents["data"][1])
ca = CloseApproach(
    designation=contents["data"][1][1],
    time=contents["data"][1][3],
    distance=contents["data"][1][4],
    velocity=contents["data"][1][7],
)
print(ca)
