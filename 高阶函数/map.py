# def test(x,y,f):
#     return f(x)+f(y)
#
# result = test(1,-2,abs)
#
# print(result)

def f(x):
    return x*x

a = map(f,[1,2,3,4,5])
print(type(a))
for i in a:
    print(i)
# map  两个参数，第一个是函数，这个函数只能接收一个参数；  第二个是可迭代对象 Iterator  [] ，这个函数会遍历Iterator，生成新的Iterator


# reduce 接收两个参数，第一个是函数且只能接收两个参数， 后一个是序列[1,2,3,4] 会先引入参数1，2，第二次是[2，3]
from functools import reduce
def f(x,y):
    return x+y
c=reduce(f,range(5))
print(c)


