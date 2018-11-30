
class Student:
    def __getattr__(self, item):
        print(item)
        def test():
            return 'arg'
        #if item == 'haha':
        #    return lambda :'ok'
        #else:
        #    raise  AttributeError("没有这个属性")
        return test
s = Student()
print(s.haha())
""" 找不到此函数时，也找不到属性时，会去执行__getattr__方法里是否有,返回值须是函数"""
#s.haha() 会先通过s.haha来获取__getattr__的返回值，因为还有()调用，所以返回值必须为函数




class Chain:
    def __init__(self,path=''):
        self._path = path
    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path,path))
    def __str__(self):
        return self._path
    __repr__ = __str__()
