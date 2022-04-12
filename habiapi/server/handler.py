"""Implement a simple HTTP server handler"""

import json
from http.server import BaseHTTPRequestHandler

from server.router import request_router


class ServerHandler(BaseHTTPRequestHandler):
    """Handler to manage incoming request"""

    def do_GET(self):
        response, status_code = request_router(
            request_method=self.command,
            request_url=self.path
        )
        self.respond(status_code, response)

    def handle_http(self, status_code: int, data: dict) -> bytes:
        """Setup response header and encode response data

        :param status_code: response status code
        :type status_code: int
        :param data: data to return
        :type data: dict
        :return: bytes with response data
        :rtype: bytes
        """

        self.send_response(status_code)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        content = json.dumps(data)
        return bytes(content, 'UTF-8')

    def respond(self, status_code: int, data: dict=None):
        """Manage reponse request

        :param status_code: response status code
        :type status_code: int
        :param data: data to return, defaults to None
        :type data: dict, optional
        """

        response = self.handle_http(status_code, data)
        self.wfile.write(response)