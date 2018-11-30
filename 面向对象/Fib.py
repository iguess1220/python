class Fib:
    def __init__(self):
        self.a,self.b = 0,1
    def __iter__(self): # 实例本身就是可迭代对象，故返回自己
        return  self
    def __next__(self):
        self.a,self.b = self.b,self.a+self.b
        if self.a > 10000:
            raise StopIteration("end")
        return self.a

c = Fib() # 可迭代对象实例
print(next(c))
print(next(c))
print(next(c))
print(next(c))
for i in c:
    print(i)
