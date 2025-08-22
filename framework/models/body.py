from typing import Dict, Callable
from abc import ABC, abstractmethod


class Body(ABC):
    @classmethod
    def create(
        cls,
        read_data: Callable,
        content_length: int,
        threshold: int,
        leftover_bytes: bytes,
    ):
        if not content_length:
            return EmptyBody()

        if content_length < threshold:
            bytes_data = read_data(size=threshold)
            return BufferedBody(leftover_bytes + bytes_data)
        else:
            raise NotImplementedError()

    @abstractmethod
    def read(self) -> bytes:
        pass


class EmptyBody(Body):
    def read(self) -> bytes:
        return b""


class BufferedBody(Body):
    def __init__(self, bytes_data: bytes):
        self.bytes_data = bytes_data

    def read(self) -> bytes:
        return self.bytes_data


class StreamingBody(Body):
    pass
