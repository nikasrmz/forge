from typing import Callable

from framework.httpparser import create_request_from_bytes
from framework.router import Router


class RequestHandler:
    def __init__(self, body_size_threshold: int, router: Router):
        self.body_size_threshold = body_size_threshold
        self.router = router

    def handle(self, read_data: Callable) -> bytes:
        request = create_request_from_bytes(read_data, self.body_size_threshold)
