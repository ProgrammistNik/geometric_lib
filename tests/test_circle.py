import sys
import os
import pytest
import math
from circle import area, perimeter
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
)


def test_area():
    result = area(2)
    expected_result = math.pi * 2 * 2
    assert result == pytest.approx(expected_result, rel=5e-2)


def test_area_invalid():
    with pytest.raises(TypeError):
        area("2")


def test_perimeter():
    result = perimeter(2)
    expected_result = 2 * math.pi * 2
    assert result == pytest.approx(expected_result, rel=5e-2)


def test_perimeter_invalid():
    with pytest.raises(TypeError):
        perimeter("2")
