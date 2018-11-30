# 装饰器，可将类内方法变成属性的形式，可通过函数内部进行数据类型限制，又可通过setter getter之类对属性进行操作
class Student:
    @property
    def score(self):  # 调用getter
        return self.__score
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise  ValueError("score must be an integer")
        if value < 0 or value > 100:
            raise  ValueError("score must be 1 ~ 100")
        self.__score = value
    @score.deleter
    def score(self):
        print("test")
        #del self.__score
        print("done")

c =Student()
c.score = 100  # 调用setter下的函数
print(c.score)
del c.score  # 调用deleter下的方法，如果真要删除，需在函数内对应执行 del self.__score



# test


class Screen:
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self,value):
        if isinstance(value,int):
            self.__width = value
        else:
            raise ValueError("must be int")
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self,value2):
        if isinstance(value2,int):
            self.__height = value2
        else:
            raise ValueError("must be int")
    @property
    def resolution(self):
        return self.__width * self.__height



s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')



















