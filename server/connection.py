from socket import socket as Socket

class ConnectionHandler:
    connection_socket: Socket
    address: str

    def __init__(self, socket: Socket, address: str, router):
        self.connection_socket = socket
        self.address = address
        self.router = router

    def handle(self):
        data_bytes = self.connection_socket.recv(1024)
        print(f"received data: {data_bytes}")
        self.connection_socket.send(b"HTTP/1.1 200 OK\r\n\r\nHello World")
        self.connection_socket.close()
