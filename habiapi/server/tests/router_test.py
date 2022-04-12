"""Tests for router module"""

from unittest.mock import Mock

from server.router import request_router
from server import status


def test_router_empty_call():
    """Test calling request router without arguments"""

    expected_data = {"message": "Path not found"}
    expected_status = status.HTTP_404_NOT_FOUND

    data, status_code = request_router()

    assert data == expected_data
    assert status_code == expected_status


def test_router_path_not_found():
    """Test requesting a non existing path"""

    expected_data = {"message": "Path not found"}
    expected_status = status.HTTP_404_NOT_FOUND

    data, status_code = request_router("GET", "/a-path")

    assert data == expected_data
    assert status_code == expected_status


def test_router_method_not_supported():
    """Test handling a method not supported"""

    expected_result = {"message": "Method POST not supported"}
    expected_status_code = status.HTTP_400_BAD_REQUEST

    data, status_code = request_router("POST", "/api/property/")

    assert data == expected_result
    assert status_code == expected_status_code


def test_router_bad_request():
    """Test handling a bad request"""

    expected_result = [{
        "loc": ["year"],
        "msg": "value is not a valid integer",
        "type": "type_error.integer"
    }]
    expected_status_code = status.HTTP_400_BAD_REQUEST
    data, status_code = request_router("GET", "/api/property/?year=hi")

    assert data == expected_result
    assert status_code == expected_status_code


def test_router_database_error(monkeypatch):
    """Test database error"""

    expected_result = {"message": "Something went wrong while retrieving the data"}
    expected_status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    conn_mock = Mock()
    conn_mock.return_value.cursor.return_value.execute.side_effect = Exception
    monkeypatch.setattr("database.dbhandler.mysql.connector.connect", conn_mock)

    data, status_code = request_router("GET", "/api/property/")

    assert data == expected_result
    assert status_code == expected_status_code


def test_router_valid_query(monkeypatch):
    """Test handling a valid property query"""

    query = ""
    with open("propertyfinder/tests/test_data/query_all.sql") as query_sql:
        query = query_sql.read()

    do_select_mock = Mock(return_value={"is_ok": True, "result": "ok result"})
    monkeypatch.setattr("propertyfinder.queries.do_select", do_select_mock)
    data, status_code = request_router(
        "GET", "/api/property/?year=2022&city=medellin&status=vendido"
    )

    do_select_mock.assert_called_once()
    do_select_mock.assert_called_with(query)
