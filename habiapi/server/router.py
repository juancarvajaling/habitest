"""Module redirect incoming request to the appropiate handler"""

import re
from urllib.parse import urlparse

from propertyfinder.handlers import PropertyFinderHandler
from server import status


def request_router(request_method: str=None, request_url: str="") -> tuple:
    """Redirect incoming request to the corresponding handler

    :param request_method: method of the incoming request, defaults to None
    :type request_method: str, optional
    :param request_url: url of the request, defaults to ""
    :type request_url: str, optional
    :return: resulting data and HTTP status
    :rtype: tuple
    """     

    url_parsed = urlparse(request_url)
    if re.search("^(\/api\/property)\/?$", url_parsed.path):
        propertyfinder_handler = PropertyFinderHandler(request_method, request_url)
        return propertyfinder_handler.execute_request()

    data = {"message": "Path not found"}
    return data, status.HTTP_404_NOT_FOUND
