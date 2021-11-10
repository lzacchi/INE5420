import random
import typing

from enum import Enum

class WireframeStructure():
    def __init__(self, coordinates: list, struct_index: int) -> None:
        self.coordinates = coordinates
        self.vertices = len(self.coordinates)
        self.struct_type = WireframeType(self.vertices).name
        self.name = f"{self.struct_type}_{struct_index}"
        self.color = WireframeColor(random.randrange(1, 8)).name
        self.struct_name = f"{self.struct_type}_{struct_index}"


class WireframeType(Enum):
    """ The Structure type is defined by how many coordinates it has.
        The Polygon type is accessed if the amount cannot be found,
        using the Enum class method '_missing_'
    """
    INVALID = 0
    POINT = 1
    LINE = 2
    POLYGON = -1

    @classmethod
    @typing.no_type_check  # Keeps 'mypy' from typechecking this function
    def _missing_(cls, value):
        return WireframeType.POLYGON

class WireframeColor(Enum):
    """Uses PyQt5.QtCore.Qt colors"""
    white = 1
    red = 2
    green = 3
    blue = 4
    cyan = 5
    magenta = 6
    yellow = 7
