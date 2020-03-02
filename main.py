import socket
import sys
import time as t

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
    for i in range(1, 13):
        if broken:
            break
        for j in range(1, 7):
            if gamefield[i * j * 2 - 1] == "0":
                return f'{response}\\{roundid};{gameid};({j * 2},{i})'
    return f'{response}\\{roundid};{gameid};(4,4)'


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
        for req in requests:
            response = findpos(req)
            respon = f'{respon}{response}'
        send(respon[1:])
