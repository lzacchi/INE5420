import numpy as np
from enum import Enum, auto
from utils.wireframe_structure import WireframeStructure
from utils.clipping.cohen_sutherland import cohen_sutherland


class ClippingMethod(Enum):
    NONE = auto()
    COHEN_SUTHERLAND = auto()
    LIANG_BARKSY = auto()


def apply_clipping(wireframe: WireframeStructure, method: ClippingMethod) -> tuple[bool, list]:
    if wireframe.vertices == 1:
        coordinates = np.array(wireframe.transformed_coordinates[0])

        '''Test if point is visible'''
        if np.any((coordinates < -1) | (coordinates > 1)):
            return False, []
        else:
            return True, [[coordinates]]


    if wireframe.vertices == 2:
        '''Clip line'''
        p1, p2 = wireframe.transformed_coordinates

        if method == ClippingMethod.COHEN_SUTHERLAND:
            visibility, clipped_coordinates = cohen_sutherland((p1, p2))

        return visibility, [clipped_coordinates]

    return False, []
