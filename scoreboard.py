import socket

SCOREPORT = 1339
IP_ADRESS = "10.183.83.127"

while True:
    _ = input("press any key to continue")
    scoresocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scoresocket.connect((IP_ADRESS, SCOREPORT))
    print(str(scoresocket.recv(1024), "utf8"))
    scoresocket.close()
