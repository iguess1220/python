class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score__ = score

    def print_score(self):
        print("%s: %s"  %(self.__name,self.__score__))

    def get_grade(self):
        if self.__score__ >= 90:
            return "A"
        elif self.__score >= 60:
            return "B"
        else:
            return "C"

bart = Student('bart',100)
bart.print_score()
print(bart.get_grade())
print(bart.__score__)  # 前后都有下划线为特殊变量，可直接使用， 私有属性无法直接获取，通过函数获取
#print(bart.__name)




# 练习题

class Student(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender
    def get_gender(self):
        return self.__gender
    def set_gender(self,new_gender):
        self.__gender = new_gender
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')

















