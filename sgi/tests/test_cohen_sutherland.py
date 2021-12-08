import pytest
from app.utils.clipping.cohen_sutherland import cohen_sutherland


def test_cohen_points_outside():
    visible, coordinates = cohen_sutherland(((-1.5, -1.5), (1.5, -1.2)))
    print(f"\noutside: {coordinates}")
    assert visible == False

def test_cohen_points_outside2():
    visible, coordinates = cohen_sutherland(((-2.0, -2.0), (2.0, -2.0)))
    print(f"outside2: {coordinates}")
    assert visible == False

def test_cohen_points_inside():
    visible, coordinates = cohen_sutherland(((0.1, 0.1), (0.2, 0.2)))
    print(f"inside: {coordinates}")
    assert visible == True

def test_cohen_points_partially_visible_left():
    visible, coordinates = cohen_sutherland(((-1.5, -1.1), (0, 0)))
    print(f"partially visible <-: {coordinates}")
    assert visible == True

def test_cohen_points_partially_visible_right():
    visible, coordinates = cohen_sutherland(((0, 0), (1.5, 1.1)))
    print(f"partially visible ->: {coordinates}")
    assert visible == True
