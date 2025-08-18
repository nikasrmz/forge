from typing import Dict
from abc import ABC, abstractmethod
from socket import socket as Socket

class Body(ABC):
    @classmethod
    def create(
        cls, 
        socket: Socket, 
        headers: Dict[str, str], 
        threshold: int, 
        leftover_bytes: bytes
    ):
        content_length = int(headers.get("content-length"))
        if not content_length:
            return EmptyBody()
        
        if content_length < threshold:
            bytes_data = socket.recv(threshold)
            return BufferedBody(leftover_bytes + bytes_data)
        
    @abstractmethod
    def read(self) -> bytes:
        pass

class EmptyBody(Body):
    def read(self) -> bytes:
        return b""

class BufferedBody(Body):
    def __init__(self, bytes_data: bytes):
        self.bytes_data = bytes_data

class StreamingBody(Body):
    pass