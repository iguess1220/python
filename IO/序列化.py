import pickle
import os
# d = dict(name='bob',age=20,score=88)
# c = pickle.dumps(d)
# e = pickle.loads(c)
# f = open('test.txt','wb')  # 打开文件生成操作对象f,使用二进制写入
# pickle.dump(d,f)   # 将序列话对象存入文件对象
# f.close()

f = open('test.txt','rb')
a = pickle.load(f)
f.close()
print(a)
