class Student:
    def __init__(self,name):
        self.name = name
    def __call__(self, *args, **kwargs):
        print('My name is %s ' % self.name)


s = Student('chenyang')
s()
# 实例直接调用时会出发__call__函数