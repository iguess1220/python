# def decor(func):
#     def wrapper(*args,**kwargs):
#         print("test")
#         print("test over")
#         return func()
#     return wrapper
# @decor
# def haha():
#     print("haha")
#     return "hehe"
# a = haha()
# print(a)

import time
import functools
def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args,**kwargs):
        ago = time.time()
        result = fn(*args,**kwargs)
        after = time.time()
        print('%s executed in %.3f ms' % (fn.__name__, (after-ago)*100))
        return result
    return wrapper
@metric
def test():
    time.sleep(0.1)
test()

@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')