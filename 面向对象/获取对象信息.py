"""type() 基本类型可以通过type()来判断"""
a = type(123)
b = type('str')
c = type(None)
print(a,b,c)

# 如果一个变量指向函数或类，也可以使用type
type(abs)


#使用type内部模块的常量来判断
import types
def fn():
    pass
f = type(fn) == types.FunctionType
print(f)
f = type(abs) == types.BuiltinFunctionType  # 内建函数
print(f)
f = type(lambda x:x) == types.LambdaType # 匿名函数类型
print(f)
f = type((x for x in range(10))) == types.GeneratorType # 生成器类型
print(f)
