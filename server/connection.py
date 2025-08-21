from socket import socket as Socket
from typing import Callable


class ConnectionHandler:
    connection_socket: Socket
    address: str
    threshold: int

    def __init__(self, socket: Socket, handle_request: Callable):
        self.connection_socket = socket
        self.handle_request = handle_request

    def handle(self):
        response_bytes = self.handle_request(self.request_data_callback)
        self.connection_socket.send(response_bytes)
        self.connection_socket.close()

    def request_data_callback(self, size: int = 1024):
        data = self.connection_socket.recv(size)
        if not data:
            raise Exception()  # TODO: ConnectionClosed error
        return data
