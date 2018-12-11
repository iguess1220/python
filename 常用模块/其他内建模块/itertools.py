# import itertools,time
# natuals = itertools.count(start=1,step=0.1)
# for i in natuals:
#     time.sleep(1)
#     print(i)
import itertools,time
# cs = itertools.cycle('ChenYang')
# for i in cs:
#     time.sleep(0.5)
#     print(i)

# ns = itertools.repeat('chenyang',3)
# for i in ns:
#     time.sleep(1)
#     print(i)


# 截取有限的序列

# natuals = itertools.count(1)
# exa = itertools.takewhile(lambda x:x<=10,natuals)
# print(list(exa))
#
#
# for c in itertools.chain('abc','zxv'):
#     print(c)
#
# for a,group in itertools.groupby('ccccaaaererggggg'):
#     print(a,list(group))


from functools import reduce
def pi(N):
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    jishu = itertools.count(start=1,step=2)
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    ns = itertools.takewhile(lambda x:x<=2*N-1,jishu)
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    cc = itertools.cycle([4,-4])
    return sum(map(lambda x:next(cc)/x,ns))
print(pi(10))
assert 3.04 < pi(10) < 3.05
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415