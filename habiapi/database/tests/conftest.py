"""
Module to set database test configuration
"""

import pytest

class CursorMock:
    """
    Returns an instance that mock a MySQL cursor
    """

    def __init__(self) -> None:
        self.result = self.result_generator()

    def result_generator(self):
        """
        Creates a generator to iterate over query results.
        """

        result = [
            {"key1": "val11", "key2": "val12"},
            {"key1": "val21", "key2": "val22"},
        ]
        for row in result:
            yield row

    def fetchone(self):
        """
        Mock fetchone method
        """

        try:
            return self.result.__next__()
        except StopIteration:
            return None

    def execute(self, query):
        """
        Mock cursor execute method
        """
        return None

    def close(self):
        """
        Mock cursor close method
        """
        return None


@pytest.fixture
def cursor_mock():
    """
    Creates a object that a MySQL cursor
    """

    return CursorMock()
