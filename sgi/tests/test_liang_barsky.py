import pytest
from app.utils.clipping.liang_barsky import liang_barsky


def test_liang_points_outside():
    visible, coordinates = liang_barsky(((-1.5, -1.5), (1.5, -1.2)))
    print(f"\noutside: {coordinates}")
    assert visible == False
    assert coordinates[0] == (None, None)
    assert coordinates[1] == (None, None)

def test_liang_points_inside():
    visible, coordinates = liang_barsky(((0.1, 0.1), (0.9, 0.9)))
    print(f"inside: {coordinates}")
    assert visible == True

def test_liang_points_partially_visible_left():
    visible, coordinates = liang_barsky(((-1.2, -1.0), (1, -1)))
    print(f"partially visible <-: {coordinates}")
    assert visible == True

def test_liang_points_partially_visible_right():
    visible, coordinates = liang_barsky(((0.5, 0.6), (1.1, -1.3)))
    print(f"partially visible ->: {coordinates}")
    assert visible == True
