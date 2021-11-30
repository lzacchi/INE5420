

def region_code(value:float, min_value:float, max_value:float, extremities:tuple[float, float]) -> float:
    return 0


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

    x1, y1 = p1
    x2, y2 = p2

    p1_rc, p2_rc = 8, 8

    while True:
        if p1_rc & p2_rc != 0:
            '''Line is completely outside the window'''
            return False, ((x1,y1), (x2, y2))

        if p1_rc | p2_rc == 0:
            '''Line is completely inside the window'''
            return True, ((x1,y1),(x2,y2))
