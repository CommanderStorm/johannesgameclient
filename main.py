import socket
import threading
from typing import Dict

import handler

# Consts

GAMEPORT = 1337
RESULTPORT = 1338
SCOREPORT = 1339
IP_ADRESS = "10.183.83.127"
NAME = "Python"

# Var
gamesocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
gamesocket.connect((IP_ADRESS, GAMEPORT))
opponents: Dict[str, handler.Handle] = {}

while True:

    s = str(gamesocket.recv(1024), "utf8")
    signature, s = s.split("ä")

    if signature not in opponents.keys():
        opponents[signature] = handler.Handle(gamesocket)
    threading.Thread(target=opponents[signature].handle, args=s).start()
