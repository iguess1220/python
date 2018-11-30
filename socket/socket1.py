
# 导入模块
import  socket

# 实例化
sk = socket.socket()
# 指定ip端口
ip_port = ("127.0.0.1",8888)
# 绑定端口
sk.bind(ip_port)
# 限制队列连接数
sk.listen(5)
#接收数据
print("开始接收数据")
conn,address = sk.accept()

# 定义信息
msg = "hello world"

conn.send(msg.encode())

conn.close()