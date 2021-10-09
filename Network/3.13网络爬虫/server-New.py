# coding = utf-8
#服务器

import socket

server = socket.socket()
server.bind(("127.0.0.1",8888))

server.listen(5)

print("等待连接请求.....")
conn,addr = server.accept()
print('接收到来自 %s 的连接' % addr[0])

data = conn.recv(1024)
print(data.decode())
conn.send(data.upper())

conn.close()
print("连接已断开")
server.close()
print("服务器已关闭")