import sys
import os
import pytest
from triangle import area, perimeter


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def test_area():
    assert area(5, 12, 13) == 30


def test_area_invalid():
    with pytest.raises(TypeError):
        area(5, 12, "13")


def test_invalid_size_area():
    with pytest.raises(TypeError):
        area(5, 12)


def test_perimeter():
    assert perimeter(5, 12, 13) == 30


def test_perimeter_invalid():
    with pytest.raises(TypeError):
        perimeter(5, 12, "13")


def test_invalid_size_perimeter():
    with pytest.raises(TypeError):
        perimeter(5, 12)
