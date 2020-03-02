import socket
import sys
import time as t

# Consts
GAMEPORT = 1337
RESULTPORT = 1338
SCOREPORT = 1339
IP_ADRESS = "10.183.83.127"
NAME = "Python"

# Var
gamesocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
gamesocket.connect((IP_ADRESS, GAMEPORT))
gamesocket.send(bytes(NAME, "utf8") + b'\n')


def send(string):
    gamesocket.send(bytes(string) + b'\n')


while True:
    first = str(gamesocket.recv(1024), "utf8").strip("\n")
    if first == "Welcome":
        print("Connected")
    elif first == "Ping":
        send("PONG")
    elif first is not "":
        print(first)
        requests = first.split("/")
        print(requests)
