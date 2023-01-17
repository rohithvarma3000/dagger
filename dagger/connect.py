import socket


class PlutoConnection(socket.socket):

    def __init__(self):
        super().__init__(socket.AF_INET, socket.SOCK_STREAM)
