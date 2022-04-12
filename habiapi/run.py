
import os
import time
from http.server import HTTPServer

from server.handler import ServerHandler

PORT = 8000
ALLOWED_HOST = os.getenv("ALLOWED_HOST", "0.0.0.0")


if __name__ == "__main__":
    httpd = HTTPServer((ALLOWED_HOST, PORT), ServerHandler)
    print(time.asctime(), f"Starting server - {ALLOWED_HOST}:{PORT}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()

    print(time.asctime(), "Stoping server - {ALLOWED_HOST}:{PORT}")