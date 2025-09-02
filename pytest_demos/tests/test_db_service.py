import unittest.mock as mock
from src import db_service
import pytest
import requests

# The order of arguments to the test function is the reverse of the decorator order.
@mock.patch("src.db_service.get_user_by_id")
@mock.patch("src.db_service.get_email_by_id")
def test_get_user_by_id_from_db(mocked_get_email, mocked_get_user):
    mocked_get_user.return_value = "mocked Christopher"
    mocked_get_email.return_value = "mockedc@abc.com"

    user_name = db_service.get_user_by_id(3)
    email = db_service.get_email_by_id(3)
    
    assert user_name == "mocked Christopher"
    assert email == "mockedc@abc.com"


@mock.patch("requests.get")
def test_get_user_requests(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"id": 1, "name": "abc"}
    mock_get.return_value = mock_response

    data = db_service.get_users()
    assert data == {"id": 1, "name": "abc"}


@mock.patch("requests.get")
def test_get_user_requests_error(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 400
    mock_get.return_value = mock_response

    with pytest.raises(requests.HTTPError):
        db_service.get_users()