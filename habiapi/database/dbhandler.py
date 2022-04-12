"""Manage connections again MySQL database"""

import contextlib
import os
from typing import List

import mysql.connector


@contextlib.contextmanager
def _mysql_cursor():
    """Context manager that yields a MySQL cursor and close it automatically

    :yield: MySQL cursor
    :rtype: mysql.connector.cursor_cext.CMySQLCursorBufferedDict
    """

    try:
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_SCHEMA")
        )
    except mysql.connector.Error:
        conn = None

    cursor = None if conn is None else conn.cursor(buffered=True, dictionary=True)
    try:
        yield cursor
    finally:
        if conn is not None and conn.is_connected():
            cursor.close()
            conn.close()


def execute_query(cursor, query: str) -> dict:
    """_summary_

    :param cursor: MySQL cursor
    :type cursor: mysql.connector.cursor_cext.CMySQLCursorBufferedDict
    :param query: query to be executed
    :type query: str
    :return: dictionary with the execution result
    :rtype: dict
    """

    try:
        cursor.execute(query)
    except Exception:
        return 


def do_select(query: str) -> List[dict]:
    """Executes a SELECT SQL query agains MySQL database

    :param query: query to be executed
    :type query: str
    :return: list of dictionaries. Every dictionary is a register from db
    :rtype: List[dict]
    """

    select_result = {
        "is_ok": False,
        "result": {"message": "Something went wrong while retrieving the data"} 
    }
    with _mysql_cursor() as cursor:
        if cursor is not None:
            try:
                cursor.execute(query)
            except Exception:
                return select_result

            result = []
            row = cursor.fetchone()
            while row is not None:
                result.append(row)
                row = cursor.fetchone()

            select_result["is_ok"] = True
            select_result["result"] = result

    return select_result
