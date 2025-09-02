from src import my_functions

# For the moment run ```export PYTHONPATH=/Users/rashmikare/Learn/Repos/MyRepos/PyLab/pytest_demos:$PYTHONPATH``` to add the directory to the Python module search path
def test_add():
    """Test the add function."""
    assert my_functions.add(1, 2) == 3
    assert my_functions.add(-1, 1) == 0
    assert my_functions.add(0, 0) == 0
    assert my_functions.add(1.5, 2.5) == 4.0

def test_divide():
    """Test the divide function."""
    assert my_functions.divide(4, 2) == 2
    assert my_functions.divide(5, 2) == 2.5
    assert my_functions.divide(-4, -2) == 2
    assert my_functions.divide(-4, 2) == -2
    assert my_functions.divide(0, 1) == 0

def test_divide_by_zero():
    # Test for both ValueError and ZeroDivisionError
    import pytest
    with pytest.raises((ValueError, ZeroDivisionError)):
        my_functions.divide(1, 0)

def test_add_strings():
    assert my_functions.add("Hello ", "World") == "Hello World"

