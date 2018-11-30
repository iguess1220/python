#三元操作符

"""三元操作符是 if-else 语句也就是条件操作符的一个快捷方式：

[表达式为真的返回值] if [表达式] else [表达式为假的返回值]

"""
y = 19
x = 10 if (y == 9) else 20
print(x)


class test:
    def __init__(self,name):
        self.name = name
        print(self.name)
class test2:
    def __init__(self):
        print("test2")

x = (test('cy') if y == 19 else test2())
