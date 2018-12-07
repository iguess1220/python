from collections import namedtuple
Point = namedtuple('Point',('x','y')) #创建一个自定义的tuple对象，设定名称和元素数量，且可以不用索引而用属性获取元素
P = Point(1,2)
print(type(Point))
print(P.x)
print(P.y)
print(isinstance(P,tuple))
print(isinstance(P,Point))

# 定义一个圆
Circle = namedtuple('Circle',['x','y','r'])
C = Circle(2,3,4)
print(C.x,C.y,C.r)


# 数据量大时，list是线性存储，删除和插入效率很低，deque可实现高效插入和删除，适合用于队列和栈

from collections import deque

q = deque(['a','b','c'])
q.append('x')
q.appendleft('y')
print(q)
q.popleft()
print(q)
q.pop()
print(q)



from collections import defaultdict
# 定义新的dict类对象，把一个函数作为实参传入，且返回值将是字典找不到key时的默认返回值
New_dict = defaultdict(lambda : "I'm yours")

New_dict['key1']  = 'cy'
New_dict['key2']  = 'yy'
print(New_dict['key2'],New_dict['key1'])
print(New_dict['key3'])


from collections import OrderedDict

d = {}
d['b'] = 1
d['a'] = 2
d['c'] = 3







