#客户端
import socket

SERVER_IP = "127.0.0.1"

SERVER_PORT = 8000

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

nickname = input("Please enter your name: ")
print("wlecome, %s!" % nickname)

while True:
    message = input(">>: ").strip()
    if not message:
        break
    message = "%s|%s" %(nickname,message)
    client.sendto(message.encode(),(SERVER_IP,SERVER_PORT))

client.close()