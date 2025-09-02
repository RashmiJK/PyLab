import pytest

@pytest.fixture
def database_connection():
    # setup code
    print("Connecting to database...")
    db = {"connected":True, "data":[]}

    yield db # Place that the test runs

    # teardown code
    print("Closing database connection...")
    db["connected"] = False

def test_database_query(database_connection):
    assert database_connection["connected"] == True
    database_connection["data"].append("test_data")

