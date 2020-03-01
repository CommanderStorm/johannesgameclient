import socket


class hanle:
    socki: socket = None
    s: str = None

    def __init__(self, s_i: str, socki_i: socket):
        global s, socki

        s = s_i
        socki = socki_i

    def handle(self):
        global s, socki
        response = ""
        print(s, " -> ", response)

        socki.send(bytes(response, "utf8") + b'\r\n')
