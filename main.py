import socket
import sys
# Consts
GAMEPORT = 1337
RESULTPORT = 1338
SCOREPORT = 1339
IP_ADRESS = "10.183.83.127"
NAME = "Python"

# Var
gamesocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
gamesocket.connect((IP_ADRESS, GAMEPORT))
gamesocket.send(bytes(NAME, "utf8") + b'\r\n')
first = str(gamesocket.recv(1024), "utf8")
if first == "Welcome":
    print("Connected")
else:
    print("Something went wrong")
    sys.exit(0)
