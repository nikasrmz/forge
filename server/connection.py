from socket import socket as Socket

class ConnectionHandler:
    connection_socket: Socket
    address: str
    threshold: int

    def __init__(self, socket: Socket, router, threshold: int):
        self.connection_socket = socket
        self.router = router
        self.threshold = threshold

    def handle(self):
        data_bytes = self.connection_socket.recv()
        print(f"received data: {data_bytes}")
        self.connection_socket.send(b"HTTP/1.1 200 OK\r\n\r\nHello World")
        self.connection_socket.close()
