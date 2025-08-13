from socket import socket as Socket

from framework.router import Router
from server.connection import ConnectionHandler

class Application:
    def __init__(self):
        self.router = Router()

    def create_handler(self, connection_socket: Socket):
        return ConnectionHandler(connection_socket, self.router)