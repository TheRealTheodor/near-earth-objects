"""Represent models for near-Earth objects and their close approaches.

The `NearEarthObject` class represents a near-Earth object. Each has a unique
primary designation, an optional unique name, an optional diameter, and a flag
for whether the object is potentially hazardous.

The `CloseApproach` class represents a close approach to Earth by an NEO. Each
has an approach datetime, a nominal approach distance, and a relative approach
velocity.

A `NearEarthObject` maintains a collection of its close approaches, and a
`CloseApproach` maintains a reference to its NEO.

The functions that construct these objects use information extracted from the
data files from NASA, so these objects should be able to handle all of the
quirks of the data set, such as missing names and unknown diameters.

You'll edit this file in Task 1.
"""

from typing import Any, Dict, List

from helpers import cd_to_datetime, datetime_to_str


class NearEarthObject:
    """A near-Earth object (NEO).

    An NEO encapsulates semantic and physical parameters about the object, such
    as its primary designation (required, unique), IAU name (optional), diameter
    in kilometers (optional - sometimes unknown), and whether it's marked as
    potentially hazardous to Earth.

    A `NearEarthObject` also maintains a collection of its close approaches -
    initialized to an empty collection, but eventually populated in the
    `NEODatabase` constructor.
    """

    def __init__(
        self, designation: str, name: str, diameter: str, hazardous: str
    ) -> None:
        """Create a new `NearEarthObject`."""
        self.designation = designation
        self.name = name if name != "" else None
        self.diameter = float(diameter) if diameter != "" else float("nan")
        self.hazardous = True if hazardous == "Y" else False

        # Create an empty initial collection of linked approaches.
        self.approaches: List[CloseApproach] = []

    @property
    def fullname(self) -> str:
        """Return a representation of the full name of this NEO."""
        return (
            self.designation + f" ({self.name})"
            if self.name is not None
            else self.designation
        )

    def __str__(self) -> str:
        """Return `str(self)`."""
        return "NEO {fullname} has a diameter of {diameter} km and {hazardous} potentially hazardous.".format(
            fullname=self.fullname,
            diameter=round(self.diameter, 4) if self.diameter is not None else "?",
            hazardous="is" if self.hazardous is True else "is not",
        )

    def __repr__(self) -> str:
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return "NearEarthObject(designation={designation}, name={name}, diameter={diameter}, hazardous={hazardous}, approaches={approaches})".format(
            designation=self.designation,
            name=self.fullname,
            diameter=(
                round(self.diameter, 4) if self.diameter is not float("nan") else "?"
            ),
            hazardous="is" if self.hazardous is True else "is not",
            approaches=self.approaches,
        )

    def serialize(self) -> Dict[str, Any]:
        """Return a dictionary ready for saving into json file."""
        return {
            "designation": self.designation,
            "name": self.name,
            "diameter_km": self.diameter,
            "potentially_hazardous": self.hazardous,
        }


class CloseApproach:
    """A close approach to Earth by an NEO.

    A `CloseApproach` encapsulates information about the NEO's close approach to
    Earth, such as the date and time (in UTC) of closest approach, the nominal
    approach distance in astronomical units, and the relative approach velocity
    in kilometers per second.

    A `CloseApproach` also maintains a reference to its `NearEarthObject` -
    initally, this information (the NEO's primary designation) is saved in a
    private attribute, but the referenced NEO is eventually replaced in the
    `NEODatabase` constructor.
    """

    def __init__(
        self, designation: str, time: str, distance: str, velocity: str
    ) -> None:
        """Create a new `CloseApproach`.

        :param info: A dictionary of excess keyword arguments supplied to the constructor.
        """
        self._designation = designation
        self.time = cd_to_datetime(time)
        self.distance = float(distance)
        self.velocity = float(velocity)

        # Create an attribute for the referenced NEO, originally None.
        self.neo: None | NearEarthObject = None

    @property
    def time_str(self) -> str:
        """Return a formatted representation of this `CloseApproach`'s approach time.

        The value in `self.time` should be a Python `datetime` object. While a
        `datetime` object has a string representation, the default representation
        includes seconds - significant figures that don't exist in our input
        data set.

        The `datetime_to_str` method converts a `datetime` object to a
        formatted string that can be used in human-readable representations and
        in serialization to CSV and JSON files.
        """
        return f"{self.time.year}-{self.time.month}-{self.time.day} {self.time.hour}:{self.time.minute}"

    def __str__(self) -> str:
        """Return `str(self)`."""
        return "At {timestr}, {neofullname} approaches Earth at a distance of {distance} au and a velocity of {velocity} km/s".format(
            timestr=self.time_str,
            neofullname=(
                self.neo.fullname if self.neo is not None else self._designation
            ),
            distance=round(self.distance, 2),
            velocity=round(self.velocity, 2),
        )

    def __repr__(self) -> str:
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return (
            f"CloseApproach(time={self.time_str!r}, distance={self.distance:.2f}, "
            f"velocity={self.velocity:.2f}, neo={self.neo!r})"
        )

    def serialize(self) -> Dict[str, Any]:
        """Return a dictionary ready for saving into json file."""
        return {
            "datetime_utc": self.time_str,
            "distance_au": self.distance,
            "velocity_km_s": self.distance,
        }
