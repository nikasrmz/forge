from typing import Dict
from abc import ABC, abstractmethod
from socket import socket as Socket

class Body(ABC):
    @classmethod
    def create(cls, socket: Socket, headers: Dict[str, str], threshold: int):
        content_length = headers.get("content-length")
        if not content_length:
            return EmptyBody()
        
        if content_length < threshold:
            request = socket.recv()
            BufferedBody()
        
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