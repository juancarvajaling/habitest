"""Module to handle incoming request for propertyfinder"""

from urllib.parse import urlparse, parse_qs

from server import status
from propertyfinder.validators import validate_query_params
from propertyfinder.queries import get_properties


class PropertyFinderHandler:
    """Handle queries to retrieve property information"""

    methods = ('GET',)

    def __init__(self, request_method: str, path: str="/") -> None:
        self.request_method = request_method
        self.path = path

    def execute_request(self):
        """Executes request to get property information

        :return: tuple with content response and status code
        """

        if self.request_method not in self.methods:
            error = {"message": f"Method {self.request_method} not supported"}
            return error, status.HTTP_400_BAD_REQUEST

        return self.get()

    def get(self):
        """Return properties that match with reques query params

        :return: tuple with resulting data and HTTP status
        """

        path_parsed = urlparse(self.path)
        raw_query_params = parse_qs(path_parsed.query)
        query_params = {key: value[0] for key, value in raw_query_params.items()}

        query_params_validated = validate_query_params(query_params)
        if not query_params_validated["is_ok"]:
            return query_params_validated["result"], status.HTTP_400_BAD_REQUEST

        result = get_properties(**query_params_validated["result"])
        if not result["is_ok"]:
            return result["result"], status.HTTP_500_INTERNAL_SERVER_ERROR

        return result["result"], status.HTTP_200_OK




