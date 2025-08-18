from socket import socket as Socket

from framework.router import Router
from server.listener import Listener
from server.connection import ConnectionHandler
from framework.httphandler import handle_http_request

class Application:
    def __init__(self, body_threshold: int = 10 * 1024 * 1024):
        self.router = Router()
        self.body_threshold = body_threshold

    def run(self):
        with Listener() as listener:
            listener.run(self.create_handler)

    def create_handler(self, connection_socket: Socket):
        return ConnectionHandler(connection_socket, handle_http_request)