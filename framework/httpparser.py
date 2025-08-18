from socket import socket as Socket
from typing import Tuple, Callable

from framework.request import Request
from framework.body import Body


def parse_http(read_data: Callable, body_size_threshold: int) -> Request:
    header_bytes, leftover_body_bytes = read_until_body(read_data)
    header_bytes = str(header_bytes).split()
    

def read_until_body(read_data: Callable) -> Tuple[bytes, bytes]:
    buffer = b""
    while b"\r\n\r\n" not in buffer:
        buffer += read_data()
    
    return buffer.split(b"\r\n\r\n")
