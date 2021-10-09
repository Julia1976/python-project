# coding = utf-8
#客户端

import socket

client = socket.socket()
client.connect(("127.0.0.1",8888))

message = 'Across the Great Wall we can reach every corner in the world'
client.send(message.encode())

data = client.recv(1024)
print(data.decode())

client.close()
print("客户端已关闭！")