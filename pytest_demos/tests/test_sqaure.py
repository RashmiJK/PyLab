from src import shapes
import pytest

@pytest.mark.parametrize("side, expected_result", [(5, 25),(9, 81),(4, 16)])
def test_multiple_sqaure_areas(side, expected_result):
    assert shapes.Square(side).area() == expected_result

@pytest.mark.parametrize("side, expected_result", [(5, 20),(9, 36),(4, 16)])
def test_multiple_square_perimeters(side, expected_result):
    assert shapes.Square(side).perimeter() == expected_result
