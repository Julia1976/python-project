#服务器
import socket

SERVER_IP = "127.0.0.1"

SERVER_PORT = 8000

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((SERVER_IP,SERVER_PORT))

while True:
    message, address = server.recvfrom(1024)
    messenger,content = message.decode().split('|')
    print("%s|%s" % (messager,content))