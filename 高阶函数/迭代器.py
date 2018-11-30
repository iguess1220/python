# Iterator 成为迭代器  就是既可以for循环，又可以next的对象，自如包括生成器
# Iterable 成为可迭代对象，只要可以for循环就行，包括列表，字典，字符串，元祖，集合等

#要把可迭代对象换成迭代器，可用函数Iter()执行
list = [x * x for x in range(5)]
tuple = (1,2,3,4,5)
dict = {'a':1,'b':2}
str = "hello world"

from  collections import Iterator
from  collections import  Iterable

print(isinstance(list,Iterator))
print(isinstance(tuple,Iterator))
print(isinstance(dict,Iterator))
print(isinstance(str,Iterator))


print(isinstance(iter(list),Iterator))
print(isinstance(iter(tuple),Iterator))
print(isinstance(iter(dict),Iterator))
print(isinstance(iter(str),Iterator))
