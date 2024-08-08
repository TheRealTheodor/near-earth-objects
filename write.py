"""Write a stream of close approaches to CSV or to JSON.

This module exports two functions: `write_to_csv` and `write_to_json`, each of
which accept an `results` stream of close approaches and a path to which to
write the data.

These functions are invoked by the main module with the output of the `limit`
function and the filename supplied by the user at the command line. The file's
extension determines which of these functions is used.

You'll edit this file in Part 4.
"""

import csv
import json
import pathlib
from typing import List

from models import CloseApproach


def write_to_csv(results: List[CloseApproach], filename: pathlib.PosixPath) -> None:
    """Write an iterable of `CloseApproach` objects to a CSV file.

    The precise output specification is in `README.md`. Roughly, each output row
    corresponds to the information in a single close approach from the `results`
    stream and its associated near-Earth object.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    fieldnames = (
        "datetime_utc",
        "distance_au",
        "velocity_km_s",
        "designation",
        "name",
        "diameter_km",
        "potentially_hazardous",
    )
    with open(filename, "w") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        for result in results:
            row = {
                "datetime_utc": result.time,
                "distance_au": result.distance,
                "velocity_km_s": result.velocity,
                "designation": result._designation,
                "name": result.neo.name if result.neo.name is not None else "",  # type: ignore
                "diameter_km": result.neo.diameter,  # type: ignore
                "potentially_hazardous": result.neo.hazardous,  # type: ignore
            }
            writer.writerow(row)


def write_to_json(results: List[CloseApproach], filename: pathlib.PosixPath) -> None:
    """Write an iterable of `CloseApproach` objects to a JSON file.

    The precise output specification is in `README.md`. Roughly, the output is a
    list containing dictionaries, each mapping `CloseApproach` attributes to
    their values and the 'neo' key mapping to a dictionary of the associated
    NEO's attributes.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    with open(filename, "w") as outfile:
        final_json_list = []
        for result in results:
            result_dict = result.serialize()
            result_dict["neo"] = result.neo.serialize()  # type: ignore
            final_json_list.append(result_dict)
        json.dump(final_json_list, outfile)
