import json
class Student:
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score


s = Student('chenyang',30,100)
#json.dumps(s)
#a = json.dumps(s.__dict__)   # __dict__ 可以提取实例的变量属性
#print(a)

def student2dict(obj):
    return {
        'name': obj.name,
        'age': obj.age,
        'score': obj.score
    }
c = json.dumps(s, default=student2dict) # default 默认函数来获取dict
print(c)



def dict2student(d):
    return Student(d['name'],'d[age]','d[score]')
g = json.loads(c,object_hook=dict2student)
print(g.name)