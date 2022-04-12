"""Tests for router module"""

from unittest.mock import Mock

from server.router import request_router
from server import status


def test_router_empty_call():
    """Test calling request router without arguments"""

    expected_data = {"message": "Path not found"}
    expected_status = status.HTTP_404_NOT_FOUND

    data, response_status = request_router()

    assert data == expected_data
    assert response_status == expected_status


def test_handler_path_not_found():
    """Test requesting a non existing path"""

    expected_data = {"message": "Path not found"}
    expected_status = status.HTTP_404_NOT_FOUND

    data, response_status = request_router("GET", "/a-path")

    assert data == expected_data
    assert response_status == expected_status


def test_handler_matching_path(monkeypatch):
    """Test handler execution for a matching path"""

    expected_data = {"is_ok": True, "result": "ok result"}
    expected_status = status.HTTP_200_OK

    handler = Mock()
    handler.return_value.execute_request.return_value = (expected_data, expected_status)
    monkeypatch.setattr(
        "server.router.PropertyFinderHandler", handler
    )
    data, response_status = request_router("GET", "/api/property/?year=2022")

    assert data == expected_data
    assert response_status == expected_status
