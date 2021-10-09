# coding = utf-8
#服务器

import socket

server = socket.socket()
server.bind(("127.0.0.1",8888))

server.listen(5)

print("等待连接请求.....")
conn,addr = server.accept()
print('接收到来自 %s 的连接' % addr[0])