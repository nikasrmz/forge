from typing import Callable

from framework.core.router import Router
from framework.core.parameters import build_handler_kwargs
from framework.core.httpparser import create_request_from_bytes


class RequestHandler:
    def __init__(self, body_size_threshold: int, router: Router):
        self.body_size_threshold = body_size_threshold
        self.router = router

    def handle(self, read_data: Callable) -> bytes:
        request = create_request_from_bytes(read_data, self.body_size_threshold)
        route, path_params = self.router.find_handler(method=request.method, route=request.path)
        handler_kwargs = build_handler_kwargs(route, path_params, request)
        handler_output = route.handler(**handler_kwargs)
        response = handler_output.encode() # TODO: needs implementation, temporary solution for testing
        return f"HTTP/1.1 200 OK\r\nContent-Length: {len(response)}\r\n\r\n{response}".encode()
