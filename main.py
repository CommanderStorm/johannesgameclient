import socket
import threading

import handler

# Consts
PORT = 3000
IP_ADRESS = "localhost"
# Var
socki = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socki.connect((IP_ADRESS, PORT))


# Methods
def socki_recv(s):
    global socki
    handler.Hanle(s, socki).handle()


while True:
    s = str(socki.recv(1024), "utf8")
    reci = threading.Thread(target=socki_recv, args=s)
    reci.start()
