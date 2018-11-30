from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# 实例化 DummyAuthorizer 创建ftp用户
authorizer = DummyAuthorizer()

authorizer.add_user('user','12345','/Users/cy/',perm='elr')

handler = FTPHandler
handler.authorizer  = authorizer

handler.passive_ports = range(2000,2333)

server = FTPServer(('127.0.0.1',21),handler)
server.serve_forever()