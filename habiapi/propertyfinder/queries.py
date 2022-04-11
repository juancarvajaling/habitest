"""
Module to build queries to retrieve property information
"""
from database.dbhandler import do_select


def get_properties(year: str=None, city: str=None, status: str=None) -> dict:
    """
    Build a SQL query base on received parameter and get properties from
    database.

    :param str year: property construction year to search
    :param str city: city where property belongs
    :param str status: system property status

    :return: dictionary with the query result.
    """

    query = ""
    with open("propertyfinder/utils/query.sql") as query_sql:
        query = query_sql.read()

    if year is not None:
        query += f' AND property.year="{year}"'

    if city is not None:
        query += f' AND property.city="{city}"'

    if status is not None:
        query += f' AND status.name="{status}"'

    result = do_select(query)
    return result
