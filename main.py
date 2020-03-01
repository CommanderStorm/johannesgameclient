import socket
import threading
from typing import Dict

import handler

# Consts
PORT = 3000
IP_ADRESS = "localhost"

# Var
socki = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socki.connect((IP_ADRESS, PORT))
opponents: Dict[str, handler.Handle] = {}

while True:
    global socki, opponents

    s = str(socki.recv(1024), "utf8")
    signature, s = s.split("ä")

    if not signature in opponents.keys():
        opponents[signature] = handler.Handle(socki)
    threading.Thread(target=opponents[signature].handle, args=s).start()
