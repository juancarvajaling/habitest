"""Tests for database connection and query executions"""

from unittest.mock import Mock

import mysql.connector

from database.dbhandler import _mysql_cursor, do_select


def test_db_connection_fail(monkeypatch):
    """Test exception during database connection"""

    monkeypatch.setattr(
        "mysql.connector.connect", Mock(side_effect=mysql.connector.Error)
    )
    with _mysql_cursor() as cursor:
        assert cursor is None


def test_db_connection_ok(monkeypatch):
    """Test database connection successfull"""

    monkeypatch.setattr("mysql.connector.connect", Mock())
    with _mysql_cursor() as cursor:
        assert cursor


def test_select_query_none_cursor(monkeypatch):
    """"Test select_query method getting a None cursor"""

    expected_result = {
        "is_ok": False,
        "result": {"message": "Something went wrong while retrieving the data"}
    }
    monkeypatch.setattr(
        "mysql.connector.connect", Mock(side_effect=mysql.connector.Error)
    )
    query_result = do_select("a query")
    
    assert query_result == expected_result


def test_select_query_execute_error(monkeypatch):
    """Test select_query method failing while executing a query"""

    expected_result = {
        "is_ok": False,
        "result": {"message": "Something went wrong while retrieving the data"}
    }
    conn_mock = Mock()
    conn_mock.return_value.cursor.return_value.execute.side_effect = Exception
    monkeypatch.setattr("database.dbhandler.mysql.connector.connect", conn_mock)
    query_result = do_select("a query")
    
    assert query_result == expected_result


def test_select_query_ok(monkeypatch, cursor_mock):
    """Test select_query method whithout problems"""

    expected_result = {
        "is_ok": True,
        "result": [
            {"key1": "val11", "key2": "val12"},
            {"key1": "val21", "key2": "val22"},
        ]
    }

    conn_mock = Mock()
    conn_mock.return_value.cursor.return_value = cursor_mock
    monkeypatch.setattr(mysql.connector, "connect", conn_mock)
    query_result = do_select("a query")

    assert query_result == expected_result
