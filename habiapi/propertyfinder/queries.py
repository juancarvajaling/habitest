"""
Module to build queries to retrieve property information
"""
from database.dbhandler import do_select


def get_properties(year: str=None, city: str=None, status: str=None) -> dict:
    """Build a SQL query base on received parameter and get properties from
    database

    :param year: property construction year to search, defaults to None
    :type year: str, optional
    :param city: city where property belongs, defaults to None
    :type city: str, optional
    :param status: system property status, defaults to None
    :type status: str, optional
    :return: dictionary with the query result
    :rtype: dict
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
