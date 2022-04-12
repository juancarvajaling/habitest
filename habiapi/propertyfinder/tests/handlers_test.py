"""Tests form handlers module"""

from unittest.mock import Mock

from propertyfinder.handlers import PropertyFinderHandler
from server import status


def test_handlers_bad_method():
    """Test handler for an unmanaged request method"""

    expected_data = {"message": "Method POST not supported"}
    expected_status = status.HTTP_400_BAD_REQUEST

    propertyfinder_handler = PropertyFinderHandler("POST", "/")
    data, status_code = propertyfinder_handler.execute_request()

    assert data == expected_data
    assert status_code == expected_status


def test_handlers_invalid_query_params(monkeypatch):
    """Test valid request with wrong query params"""

    expected_result = {"is_ok": False, "result": "bad result"}
    expected_status = status.HTTP_400_BAD_REQUEST
    monkeypatch.setattr(
        "propertyfinder.handlers.validate_query_params",
        Mock(return_value=expected_result)
    )
    propertyfinder_handler = PropertyFinderHandler("GET", "/")
    data, status_code = propertyfinder_handler.execute_request()

    assert data == expected_result["result"]
    assert status_code == expected_status


def test_handlers_do_select_error(monkeypatch):
    """Test error while hiting datase"""

    validate_query_params_result = {"is_ok": True, "result": {"yeat": "2022"}}
    monkeypatch.setattr(
        "propertyfinder.handlers.validate_query_params",
        Mock(return_value=validate_query_params_result)
    )
    get_properties_result = {"is_ok": False, "result": "bad result"}
    expected_status = status.HTTP_500_INTERNAL_SERVER_ERROR
    monkeypatch.setattr(
        "propertyfinder.handlers.get_properties",
        Mock(return_value=get_properties_result)
    )

    propertyfinder_handler = PropertyFinderHandler("GET", "/")
    data, status_code = propertyfinder_handler.execute_request()

    assert data == get_properties_result["result"]
    assert status_code == expected_status


def test_handlers_valid_execution(monkeypatch):
    """Test a valid handler execution"""

    validate_query_params_result = {"is_ok": True, "result": {"yeat": "2022"}}
    monkeypatch.setattr(
        "propertyfinder.handlers.validate_query_params",
        Mock(return_value=validate_query_params_result)
    )
    get_properties_result = {"is_ok": True, "result": "ok result"}
    expected_status = status.HTTP_200_OK
    monkeypatch.setattr(
        "propertyfinder.handlers.get_properties",
        Mock(return_value=get_properties_result)
    )

    propertyfinder_handler = PropertyFinderHandler("GET", "/")
    data, status_code = propertyfinder_handler.execute_request()

    assert data == get_properties_result["result"]
    assert status_code == expected_status
