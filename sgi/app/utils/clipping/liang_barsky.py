def liang_barsky(line:tuple[tuple, tuple]) -> tuple[bool, tuple[tuple, tuple]]:
    min_value = -1
    max_value = 1

    point1, point2 = line

    x1, y1 = point1
    x2, y2 = point2

    p1 = -(x2 - x1)
    p2 = -p1
    p3 = -(y2 - y1)
    p4 = -p3

    q1 = x1 - min_value
    q2 = max_value - x1
    q3 = y1 - min_value
    q4 = max_value - y1


    pk = list(zip([p1, p2, p3, p4], [q1, q2, q3, q4]))

    first_check = any([p == 0 and q < 0 for (p, q) in pk])
    if first_check:
        return False, ((), ())

    r_negative = [(q / p) for (p, q) in pk if p < 0]
    u1 = max(0, max(r_negative, default=0))

    r_positive = [(q / p) for (p, q) in pk if p > 0]
    u2 = min(1, min(r_positive, default=1))

    # Completly outside
    if u1 > u2:
        return (False, ((None, None), (None, None)))

    new_x1 = x1 + u1 * p2
    new_y1 = y1 + u1 * p4
    new_x2 = x1 + u2 * p2
    new_y2 = y1 + u2 * p4

    return (True, ((new_x1, new_y1), (new_x2, new_y2)))
