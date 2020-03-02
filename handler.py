import socket


class Handle:
    socki: socket

    def __init__(self, sock: socket):
        self.socki = sock

    def handle(self, s):
        response = ""

        print(s, " -> ", response)
        self.socki.send(bytes(response, "utf8") + b'\r\n')
