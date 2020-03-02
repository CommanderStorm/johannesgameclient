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


def send(string):
    gamesocket.send(bytes(string, "utf8") + b'\n')


send(NAME)
while True:
    first = str(gamesocket.recv(1024), "utf8").strip("\n")
    if first == "Welcome":
        print("Connected")
    elif first == "Ping":
        send("PONG")
    elif first is not "":
        requests = first.split("/")
        response = ""
        for req in requests:
            direction, roundid, gameid, enemy, gamefield = req.split(";")
            move = "(0,0)"
            response = f'{response}\\{roundid};{gameid};{move}'

        send(response[1:])
        print(response)
#  H;71;11;JS-IterativeBad;300000300000300000300000300000300000000000000000000800080000000000000000/H;13;11;JS-RandomBad;000000000000000000010000014080004000000000038000030000000000000080000000/V;96;11;JS-IterativeGood;003010883010000000810030010033880003003310883310000310880310000000800000/V;70;11;JS-IterativeBad;883100883133830433830410880010880100880100810000810010180410133400833000/V;191;11;3chtuin;881013881013800001800031803340804411801401800400800100800100800100800000
