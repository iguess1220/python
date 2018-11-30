from types import MethodType
class student:
    pass
s = student()
def set_age(self,age):  # 定义一个函数作为实例方法
    self.age = age

# s.set_age = MethodType(set_age,s)# 给实例绑定一个方法,
# s.set_age(23) # 调用实例方法
# print(s.age)


"""以上绑定对其他实例是无效的，如果要有有效，可以给类本身绑定"""

student.set_age = set_age
c =student()
c.set_age(39)
print(c.age)



# __slots__
"""通过__slots__限制实例能自行添加的变量"""
class ss:
    __slots__ = ("name",'age')

class cc(ss):
    pass
w = ss()
w.name = 'asd'
w.age = 50
#w.score = 50 # 这里就无法定义属性
ss.score =50 # 但类本身可以定义属性
print(w.age,ss.score)









