import logging
from socket import socket as Socket, AF_INET, SOCK_STREAM

class Listener:
    host: str
    port: int
    listener_socket: Socket

    def __init__(self, host: str = 'localhost', port: int = 8000):
        self.host = host
        self.port = port

    def __enter__(self):
        self.listener_socket = Socket(AF_INET, SOCK_STREAM)
        self.listener_socket.bind((self.host, self.port))
        self.listener_socket.listen()
        self.listener_socket.settimeout(1.0)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.listener_socket.close()

    def run(self):
        try:
            while True:
                try:
                    connection_socket, address = self.listener_socket.accept()
                    print(f"got connection from {address}")
                except TimeoutError:
                    continue
                except Exception as e:
                    logging.error(e)
        except KeyboardInterrupt:
            print("\n\nShutting down server...")