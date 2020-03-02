import socket


class Handle:
    socki: socket

    def __init__(self, sock: socket):
        self.socki = sock

    def handle(self, s):
        print(s)
        response = ""
        if s == "Ping":
            self.socki.send(bytes("Pong", "utf8") + b'\r\n')
            return
        self.socki.send(bytes(response, "utf8") + b'\r\n')
