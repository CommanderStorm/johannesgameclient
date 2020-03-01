import threading
import socket
import handler

socki = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socki.connect(("localhost", 3000))

def socki_recv(s):
    global socki
    handler.hanle(s, socki).handle()


while True:
    s = str(socki.recv(1024), "utf8")
    reci = threading.Thread(target=socki_recv, args=s)
    reci.start()
