import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from square import area, perimeter


def test_area():
    result = area(5)
    assert result == 25


def test_area_invalid():
    with pytest.raises(TypeError):
        area("5")


def test_perimeter():
    result = perimeter(5)
    assert result == 20


def test_invalid_size_perimeter():
    with pytest.raises(TypeError):
        perimeter(9, 10)
