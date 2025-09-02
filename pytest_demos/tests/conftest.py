from src import shapes
import pytest

@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(10, 20)

@pytest.fixture
def second_rectangle():
    return shapes.Rectangle(5, 4)