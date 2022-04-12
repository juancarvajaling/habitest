"""Tests for queries module"""

from unittest.mock import Mock

from propertyfinder.queries import get_properties


def test_get_properties_not_ok(monkeypatch):
    """Test bad result when getting properties"""

    expected_result = {
        "is_ok": False,
        "result": {"message": "Something went wrong while retrieving the data"} 
    }
    monkeypatch.setattr(
        "propertyfinder.queries.do_select", Mock(return_value=expected_result)
    )
    result = get_properties()

    assert result == expected_result


def test_get_properties_no_filter(monkeypatch):
    """Test getting properties without filters"""

    query = ""
    with open("propertyfinder/tests/test_data/query_no_filters.sql") as query_sql:
        query = query_sql.read()

    do_select_mock = Mock()
    monkeypatch.setattr("propertyfinder.queries.do_select", do_select_mock)

    get_properties()

    do_select_mock.assert_called_once()
    do_select_mock.assert_called_with(query)


def test_get_properties_year(monkeypatch):
    """Test getting properties filtering only by year"""

    query = ""
    with open("propertyfinder/tests/test_data/query_year.sql") as query_sql:
        query = query_sql.read()

    do_select_mock = Mock()
    monkeypatch.setattr("propertyfinder.queries.do_select", do_select_mock)

    get_properties(year="2022")

    do_select_mock.assert_called_once()
    do_select_mock.assert_called_with(query)


def test_get_properties_city(monkeypatch):
    """Test getting properties filtering only by city"""

    query = ""
    with open("propertyfinder/tests/test_data/query_city.sql") as query_sql:
        query = query_sql.read()

    do_select_mock = Mock()
    monkeypatch.setattr("propertyfinder.queries.do_select", do_select_mock)

    get_properties(city="medellin")

    do_select_mock.assert_called_once()
    do_select_mock.assert_called_with(query)


def test_get_properties_status(monkeypatch):
    """Test getting properties filtering only by status"""

    query = ""
    with open("propertyfinder/tests/test_data/query_status.sql") as query_sql:
        query = query_sql.read()

    do_select_mock = Mock()
    monkeypatch.setattr("propertyfinder.queries.do_select", do_select_mock)

    get_properties(status="vendido")

    do_select_mock.assert_called_once()
    do_select_mock.assert_called_with(query)


def test_get_properties_all(monkeypatch):
    """Test getting properties filtering only by all filters"""

    query = ""
    with open("propertyfinder/tests/test_data/query_all.sql") as query_sql:
        query = query_sql.read()

    do_select_mock = Mock()
    monkeypatch.setattr("propertyfinder.queries.do_select", do_select_mock)

    get_properties(year="2022", city="medellin", status="vendido")

    do_select_mock.assert_called_once()
    do_select_mock.assert_called_with(query)
