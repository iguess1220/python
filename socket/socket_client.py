import socket
# 实例化对象
# client = socket.socket()
# # 定义地址
# ip_port = ("127.0.0.1",8888)
# # 连接服务端
# client.connect(ip_port)
# # 接收数据，解码
# data = client.recv(1024)
# print(data.decode())


Cl = socket.socket()
Cl.connect(("127.0.0.1",8888))
print(Cl.recv(1024).decode())
