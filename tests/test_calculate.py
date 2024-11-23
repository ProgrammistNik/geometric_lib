import sys
import os
import math
import pytest
from calculate import calc
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
)


def test_square_area():
    result = calc('square', 'area', [5])
    expected_result = 25
    assert result == expected_result


def test_square_perimeter():
    result = calc('square', 'perimeter', [5])
    expected_result = 20
    assert result == expected_result


def test_circle_area():
    result = calc('circle', 'area', [2])
    expected_result = math.pi * 2 * 2
    assert result == pytest.approx(expected_result, rel=1e-2)


def test_circle_perimeter():
    result = calc('circle', 'perimeter', [2])
    expected_result = 2 * math.pi * 2
    assert result == pytest.approx(expected_result, rel=1e-2)


def test_triangle_area():
    result = calc('triangle', 'area', [5, 12, 13])
    assert result == 30


def test_invalid_size_square():
    with pytest.raises(AssertionError, match="Error"):
        calc('circle', 'area', [8, 12, 16])


def test_invalid_size_circle():
    with pytest.raises(AssertionError, match="Error"):
        calc('circle', 'area', [1, 2, 3])


def test_triangle_perimeter():
    result = calc('triangle', 'perimeter', [5, 12, 13])
    assert result == 30


def test_invalid_function():
    with pytest.raises(AssertionError, match="Error"):
        calc('circle', 'speed', [2])


def test_invalid_figure():
    with pytest.raises(AssertionError, match="Error"):
        calc('oval', 'area', [2])


def test_invalid_size_triangle():
    with pytest.raises(AssertionError, match="Error"):
        calc('triangle', 'area', [9])
