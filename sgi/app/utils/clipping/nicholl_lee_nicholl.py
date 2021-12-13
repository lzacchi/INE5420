def nicholl_lee_nicholl(
    line: tuple[tuple[bool, bool], tuple[bool, bool]]
) -> tuple[bool, tuple[tuple, tuple]]:

    bottom_left = (-1, -1)
    top_left = (1, -1)
    top_right = (1, 1)
    bottom_right = (1, -1)

    p1, p2 = line
    x1, y1 = p1
    x2, y2 = p2

    m1 = (-1 - y1) / (-1 - x1)  # bottom_left
    m2 = (-1 - y1) / (1 - x1)  # top_left
    m3 = (1 - y1) / (1 - x1)  # top_right
    m4 = (-1 - y1) / (1 - x1)  # bottom_right

    m = (y2 - y1) / (x2 - x1)

    """Test if the line is outside the values"""

    return False, ((None, None), (None, None))
