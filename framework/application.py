from typing import Callable
from socket import socket as Socket

from framework.router import Router
from server.listener import Listener
from server.connection import ConnectionHandler
from framework.request_handler import RequestHandler

class Application:
    def __init__(self, body_threshold: int = 10 * 1024 * 1024):
        self.router = Router()
        self.request_handler = RequestHandler(body_threshold)

    def run(self):
        with Listener() as listener:
            listener.run(self.create_handler)

    def create_handler(self, connection_socket: Socket) -> ConnectionHandler:
        return ConnectionHandler(connection_socket, self.request_handler.handle)
    
    def get(self, path: str) -> Callable:
        def dec(func: Callable) -> Callable:
            self.router.add_route("GET", path, func)
            return func
        return dec
    
    def post(self, path: str) -> Callable:
        def dec(func: Callable) -> Callable:
            self.router.add_route("POST", path, func)
            return func
        return dec