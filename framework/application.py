from socket import socket as Socket

from framework.router import Router
from server.listener import Listener
from server.connection import ConnectionHandler

class Application:
    def __init__(self):
        self.router = Router()

    def run(self):
        with Listener() as listener:
            listener.run(self.create_handler)

    def create_handler(self, connection_socket: Socket):
        return ConnectionHandler(connection_socket, self.router)