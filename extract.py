"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""

import csv
import json

from models import CloseApproach, NearEarthObject


def load_neos(neo_csv_path="data/neos.csv"):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    with open(neo_csv_path, "r") as infile:
        reader = csv.reader(infile)
        list_of_neos = []
        for idx, row in enumerate(reader):
            if idx == 0:
                continue
            list_of_neos.append(
                NearEarthObject(
                    designation=row[3],
                    name=row[4],
                    diameter=row[15],
                    hazardous=row[7],
                )
            )
    return list_of_neos


def load_approaches(cad_json_path="data/cad.json"):
    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    list_of_ca = []
    with open(cad_json_path, "r") as infile:
        contents = json.load(infile)
    for data in contents["data"]:
        list_of_ca.append(
            CloseApproach(
                designation=data[1],
                time=data[3],
                distance=data[4],
                velocity=data[7],
            )
        )
    return list_of_ca
