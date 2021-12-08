'''Implementation of the Cohen-Sutherland clipping algorithm'''

def region_code(value:int, min_value:int, max_value:int, extremities:tuple[int, int]) -> int:
    low, high = extremities

    if value < min_value:
        return low
    if value > max_value:
        return high

    return 0


# returns visible boolean and result
def cohen_sutherland(line:tuple[tuple, tuple]) -> tuple[bool, tuple[tuple, tuple]]:
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
    rc_up    = 8  # 1000
    rc_down  = 4  # 0100
    rc_right = 2  # 0010
    rc_left  = 1  # 0001

    p1, p2 = line

    min_value = -1
    max_value = 1

    x1, y1 = p1
    x2, y2 = p2

    x_extremities = (rc_left, rc_right)
    y_extremities = (rc_down, rc_up)

    p1_rc = region_code(x1, min_value, max_value, x_extremities) + region_code(y1, min_value, max_value, y_extremities)
    p2_rc = region_code(x2, min_value, max_value, x_extremities) + region_code(y2, min_value, max_value, y_extremities)

    while True:
        if (p1_rc & p2_rc) != 0:
            '''Line is completely outside the window'''
            return False, ((x1,y1), (x2, y2))

        if p1_rc | p2_rc == 0:
            '''Line is completely inside the window'''
            return True, ((x1,y1),(x2,y2))

        x, y = 0, 0

        '''Line is partially outside the window'''
        rc_outer = max(p1_rc, p2_rc)

        '''Test which region contains the outer point'''
        if rc_outer & rc_left == rc_left:
            x = min_value
            y = y1 + (y2 - y1) * (min_value - x1) / (x2 - x1)

        if rc_outer & rc_right == rc_right:
            x = max_value
            y = y1 + (y2 - y1) * (max_value - x1) / (x2 - x1)

        if rc_outer & rc_up == rc_up:
            x = x1 + (x2 - x1) * (max_value - y1) / (y2 - y1)
            y = max_value

        if rc_outer & rc_down == rc_down:
            x = x1 + (x2 - x1) * (min_value - y1) / (y2 - y1)
            y = min_value

        if rc_outer == p1_rc:
            x1 = x
            y1 = y
            p1_rc = region_code(x1, min_value, max_value, x_extremities) + region_code(y1, min_value, max_value, y_extremities)
        else:
            x2 = x
            y2 = y
            p2_rc = region_code(x2, min_value, max_value, x_extremities) + region_code(y2, min_value, max_value, y_extremities)
