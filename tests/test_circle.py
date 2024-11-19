import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from circle import area, perimeter


def test_area():
    result = area(2)
    expected_result = 12,566
    assert result == pytest.approx(expected_result, rel=5e-2)


def test_area_invalid():
    with pytest.raises(TypeError):
        area("2")


def test_perimeter():
    result = perimeter(2)
    expected_result = 12,566
    assert result == pytest.approx(expected_result, rel=5e-2)


def test_perimeter_invalid():
    with pytest.raises(TypeError):
        perimeter("2")
