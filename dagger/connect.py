import socket


class PlutoConnection:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self._socket.connect((self.ip, self.port))

    def close(self):
        self._socket.close()
