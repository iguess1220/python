import os
print(os.name) # posix  是linux系列  nt 为 windows系列
print(os.uname())
print('hello')
#print(os.environ) # 环境变量 为dict格式 下面为获取具体的值
print(os.environ.get('PATH'))
print(os.environ.get('LOGNAME'))
print(os.environ.get('PYTHONIOENCODING'))
print(os.environ.get('SHELL','default'))
print(os.environ.get('USER','default'))
print(os.environ.get('HOME','default'))



