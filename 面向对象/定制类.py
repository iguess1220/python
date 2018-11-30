class Student:
    def __init__(self,name):
        self.name = name
    def __repr__(self):  # 在交互模式直接调用实例时会调用此方法
        return "test repr"
    def __str__(self):  # 打印实例是会调用此方法
        return "test str"
c = Student('cy')
print(c)
print(c.__repr__())