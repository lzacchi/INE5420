import numpy as np
from enum import Enum, auto
from utils.wireframe_structure import WireframeStructure
from utils.clipping.cohen_sutherland import cohen_sutherland
from utils.clipping.liang_barsky import liang_barsky
from utils.clipping.sutherland_hodgman import sutherland_hodgman


class ClippingMethod(Enum):
    NONE = auto()
    COHEN_SUTHERLAND = auto()
    LIANG_BARKSY = auto()


WINDOW_MAX = 1
WINDOW_MIN = -1


def apply_clipping(
    wireframe: WireframeStructure, method: ClippingMethod
) -> tuple[bool, list]:
    if wireframe.vertices == 1:
        """Clip point"""
        coordinates = np.array(wireframe.transformed_coordinates[0])

        """Test if point is visible"""
        if np.any((coordinates < WINDOW_MIN) | (coordinates > WINDOW_MAX)):
            return False, []
        else:
            return True, [[coordinates]]

    if wireframe.vertices == 2:
        """Clip line"""
        p1, p2 = wireframe.transformed_coordinates

        if method == ClippingMethod.COHEN_SUTHERLAND:
            visibility, clipped_coordinates = cohen_sutherland((p1, p2))
        else:
            visibility, clipped_coordinates = liang_barsky((p1, p2))

        return visibility, [clipped_coordinates]
    # else:

    # TODO: Clip polygon
    visibility, clipped_polygon = sutherland_hodgman(
        wireframe.transformed_coordinates)
    return visibility, clipped_polygon
