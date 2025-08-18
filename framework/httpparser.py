from socket import socket as Socket
from typing import Tuple, Callable

from framework.request import Request
from framework.body import Body


def parse_http(socket: Socket, body_size_threshold: int) -> Request:
    header_bytes, leftover_body_bytes = read_until_body(socket)
    header_bytes = str(header_bytes).split()
    

def read_until_body(socket: Socket) -> Tuple[bytes, bytes]:
    buffer = b""
    while b"\r\n\r\n" not in buffer:
        buffer += socket.recv(1024)
    
    return buffer.split(b"\r\n\r\n")
