class Fib:
    def __getitem__(self, item):
        if isinstance(item,int):
            a,b = 1,1
            for x in range(item):
                a,b = b,a+b
            return a
        elif isinstance(item,slice):
            print(item)
            start = item.start
            stop  = item.stop
            step  = item.step
            if start is None:
                start = 0
            a,b = 1,1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a,b = b,a+b
            return L

f = Fib()
b = f[1:5:10]
print(b)
L = [x for x in range(99)]
c = slice(1,80,3)   # slice是默认切片类对象

print(L[c])
