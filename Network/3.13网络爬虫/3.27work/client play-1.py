#客户端
import socket

SERVER_IP = "127.0.0.1"

SERVER_PORT = 8000

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto("loading game".encode(),(SERVER_IP,SERVER_PORT))

while True:
    message, address = client.recvfrom(1024)
    message = message.decode()
    if message == "starting":
        print("Game is starting...")
    if message == "playing":
        print("Game is working!")
    if message == "ending":
        print("game is over")