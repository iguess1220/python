def lazy_sum(*args):
    def calc_sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return calc_sum

c = [1,2,3,4,5,6]
result = lazy_sum(*c)  # 将相关参数和变量保存在了返回的函数内，为closure（闭包）
print(result())

#闭包
# def count():
#     fs = []
#     for i in range(1,4):
#         def f():
#             return i*i
#         fs.append(f)
#     return fs
# f1,f2,f3 = count()
# print(f1,f2,f3)
# print(f1(),f2(),f3())

# 闭包引用环境变量时，最好不要使用循环变量
#
# def T():
#     def f(j):
#         def g():
#             return j*j
#         return g
#     fs = []
#     for i in range(1,4):
#             fs.append(f(i))
#     return fs
# f1,f2,f3 = T()
# print(f1(),f2(),f3())


# 上边代码缩写
def T():
    f = lambda j: lambda :j*j
    fs = []
    for i in range(1,4):
        fs.append(f(i))
    return fs
f1,f2,f3 = T()

print(f1(),f2(),f3())

