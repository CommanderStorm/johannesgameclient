import socket
import time

SCOREPORT = 1339
IP_ADRESS = "10.183.83.127"

while True:
    scoresocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scoresocket.connect((IP_ADRESS, SCOREPORT))
    print(str(scoresocket.recv(32768), "utf8"))
    scoresocket.close()
    time.sleep(360)
