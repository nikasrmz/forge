from typing import Callable

from framework.httpparser import parse_http

class RequestHandler:
    def __init__(self, body_size_threshold: int):
        self.body_size_threshold = body_size_threshold

    def handle(self, read_data: Callable) -> bytes:
        request = parse_http(read_data, self.body_size_threshold)