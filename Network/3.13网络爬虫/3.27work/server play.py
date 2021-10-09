#服务器
import socket
import time

SERVER_IP = "127.0.0.1"

SERVER_PORT = 8000

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((SERVER_IP,SERVER_PORT))

print("Waiting...")
players = []
while len(players) < 4:
    message, address = server.recvfrom(1024)
    message = message.decode()
    if message == "loading game":
        print("players [%s%s]加入游戏" % (address[0],address[1]))
        if(address not in players):
            players.append(address)

print("game is starting!")

for player in players:
    server.sento('starting'.encode(),player)

for i in range(5):
    for player in players:
        server.sendto("playing".encode(),player)
    time.sleep(1)

for player in players:
    server.sendto("ending".encode(),player())

server.close()