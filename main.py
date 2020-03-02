import socket
import threading

# pyinstaller --onefile -w main.py
# Consts
GAMEPORT = 1337
RESULTPORT = 1338
IP_ADRESS = "10.183.83.127"
NAME = "Python"

# Var
gamesocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
gamesocket.connect((IP_ADRESS, GAMEPORT))


def send(string):
    gamesocket.send(bytes(string, "utf8") + b'\n')


def findpos(req):
    direction, roundid, gameid, enemy, gamefield = req.split(";")
    broken = False
    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
        if broken:
            break
        for j in [1, 2, 3, 4, 5, 6]:
            if gamefield[i * j * 2 - 1] == "0":
                return f'\\{roundid};{gameid};({j * 2},{i})'
    return f'\\{roundid};{gameid};(4,4)'


send(NAME)
while True:
    first = str(gamesocket.recv(32768), "utf8").strip("\n")
    if first == "Welcome":
        print("Connected")
    elif first == "Ping":
        send("PONG")
    elif first is not "":
        requests = first.split("/")
        respon = ""
        response = ""
        for req in requests:
            response = findpos(req)
            respon = f'{respon}{response}'
        send(respon[1:])
