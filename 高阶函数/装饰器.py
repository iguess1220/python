
# @ 的意思是 now = log(now)
# def log(func):
#     def wrapper(*args,**kw):
#         print("call %s: "  % func.__name__)
#         return func(*args,**kw)
#     return wrapper
#
#
# @log
# def now():
#     print("2018-11-12")
#
# now()



def log2(text):
    def decorator(func):
        def wrapper(*args,**kwargs):
            print("%s %s : " %(text,func.__name__))
            func()
            print("over")
        return  wrapper
    return decorator

@log2('exec')  #  now= log2('exec')(now) > now= decorator(now) > now = wrapper() (闭包 包含了外部函数传入的变量和参数 text)
def now():
    print("2018-11-12")
now()






def value(m):
    c = 30
    def test3():
        print(c,m)
    return test3  # 返回函数时，可把外部参数和变量打包进函数，闭包！






# 装饰器



