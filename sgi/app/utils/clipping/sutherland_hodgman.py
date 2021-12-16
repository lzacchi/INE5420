'''Sutherland-Hodgman algorithm for polygon clipping'''
from functools import reduce
import numpy as np
from utils.wireframe_structure import WireframeStructure


def region_code(value: int, min_value: int, max_value: int, extremities: tuple[int, int]) -> int:
    low, high = extremities

    if value < min_value:
        return low
    if value > max_value:
        return high

    return 0

# Cohen-Sutherland inspired clipping function helpers


def clip_up(x: float, y: float, m: float) -> tuple[float, float]:
    clip_x = x + 1/m * (1 - y)
    clip_y = 1
    clipped_point = (clip_x, clip_y)
    return clipped_point


def clip_down(x: float, y: float, m: float) -> tuple[float, float]:
    clip_x = x + 1/m * (-1 - y)
    clip_y = -1
    clipped_point = (clip_x, clip_y)
    return clipped_point


def clip_right(x: float, y: float, m: float) -> tuple[float, float]:
    clip_x = 1
    clip_y = m * (1 - x) + y
    clipped_point = (clip_x, clip_y)
    return clipped_point


def clip_left(x: float, y: float, m: float) -> tuple[float, float]:
    clip_x = -1
    clip_y = m * (-1 - x) + y
    clipped_point = (clip_x, clip_y)
    return clipped_point


CLIP_EDGE_HELPER = {
    1: clip_left,
    2: clip_right,
    4: clip_down,
    8: clip_up
}


def sutherland_hodgman(coordinates: list) -> tuple[bool, list]:
    '''
    region code (rc) is 4 bits
    rc[1] = up    (1000)
    rc[2] = down  (0100)
    rc[3] = right (0010)
    rc[4] = left  (0001)

    window = 0000

    diagonals are compositions.

    e.g: diagonal right = up + right = 1000 + 0010 = 10100

    @return:    (True,  line) if line is drawable
                (False, line) if line is not drawable
    '''
    rc_up = 8  # 1000
    rc_down = 4  # 0100
    rc_right = 2  # 0010
    rc_left = 1  # 0001

    x_extremities = (rc_left, rc_right)
    y_extremities = (rc_down, rc_up)

    min_value = -1
    max_value = 1

    # define a clipping window as a polygon (in this case, a rectangle)
    clipping_window = [rc_up, rc_down, rc_right, rc_left]

    # get the region code for eath vertex
    region_codes = []
    for coordinate in coordinates:
        x1, y1 = coordinate
        coordinate_rc = region_code(x1, min_value, max_value, x_extremities) + \
            region_code(y1, min_value, max_value, y_extremities)

        region_codes.append(coordinate_rc)

    # test trivial cases:

    # 1: whole polygon inside
    if all(rc == 0 for rc in region_codes):
        return True, coordinates

    # 2: whole polygon outside
    if reduce(lambda x, y: x & y, region_codes) != 0:
        return False, coordinates

    clipped_coordinates = []
    # loop through the edges of the clipping window
    for edge in clipping_window:
        # loop through the polygon vertices
        for c in range(len(coordinates)):
            c_next = (c + 1) % len(coordinates)
            c_rc = [region_codes[c], region_codes[c_next]]

            # if both vertices are inside the clipping window,
            # they're added to clipped_coordinates
            if c_rc[0] | c_rc[1] == 0:
                clipped_coordinates.append(coordinates[c])
            # if C is outside and C+1 is inside,
            # clip C and calculate intersection
            if edge & c_rc[c] != 0:
                x1, y1 = coordinates[c]
                x2, y2 = coordinates[c_next]
                m = (y2 - y1) / (x2 - x1)
                clipped_c = CLIP_EDGE_HELPER[edge](x1, y1, m)
                clipped_coordinates.append(clipped_c)

            if edge & c_rc[c_next] != 0:
                x1, y1 = coordinates[c]
                x2, y2 = coordinates[c_next]
                m = (y2 - y1) / (x2 - x1)
                clipped_c = CLIP_EDGE_HELPER[edge](x2, y2, m)
                clipped_coordinates.append(clipped_c)

            if any([(edge & code != 0) for code in c_rc]):
                c_clipped = c if c_rc[0] & edge else c_next

                x1, y1 = coordinates[c]
                x2, y2 = coordinates[c_next]

        coordinates = clipped_coordinates
        clipped_coordinates = []
    return True, clipped_coordinates
