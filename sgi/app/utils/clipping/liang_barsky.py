# returns visible boolean and result
def liang_barsky(line: tuple[tuple, tuple]) -> tuple[bool, tuple[tuple, tuple]]:
    pt1, pt2 = line
    x1, y1 = pt1
    x2, y2 = pt2

    min_value = -1
    max_value = 1

    delta_x = x2 - x1
    delta_y = y2 - y1

    p1 = -delta_x
    p2 = delta_x
    p3 = -delta_y
    p4 = delta_y

    q1 = x1 - min_value  # left border
    q2 = max_value - x1  # right border
    q3 = y1 - min_value  # bottom border
    q4 = max_value - y1  # top border

    pk = list(zip([p1, p2, p3, p4], [q1, q2, q3, q4]))

    if any([p == 0 and q < 0 for (p, q) in pk]):
        '''line is parallel to clip window'''
        return False, ((x1, y1), (x2, y2))

    r1 = [(q / p) for (p, q) in pk if p < 0]
    r2 = [(q / p) for (p, q) in pk if p > 0]

    '''aux values for comparing max and min'''
    r1.append(0)
    r2.append(1)

    z1 = max(r1)
    z2 = min(r2)

    if z1 > z2:
        '''line is outside cip window'''
        return False, ((x1, y1), (x2, y2))

    clip_x1 = x1 + (z1 * p2)
    clip_y1 = y1 + (z1 * p4)
    clip_x2 = x1 + (z2 * p2)
    clip_y2 = y1 + (z2 * p4)

    clipped_coordinates = ((clip_x1, clip_y1), (clip_x2, clip_y2))
    return True, clipped_coordinates
