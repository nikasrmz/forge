from typing import Callable

from framework.core.httpparser import create_request_from_bytes
from framework.core.router import Router


class RequestHandler:
    def __init__(self, body_size_threshold: int, router: Router):
        self.body_size_threshold = body_size_threshold
        self.router = router

    def handle(self, read_data: Callable) -> bytes:
        request = create_request_from_bytes(read_data, self.body_size_threshold)
        handler, _ = self.router.find_handler(method=request.method, route=request.path)
        response = handler()
        return f"HTTP/1.1 200 OK\r\nContent-Length: {len(response)}\r\n\r\n{response}".encode()
