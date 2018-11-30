#列表生成式
L = [x * x  for  x  in  range(10)]

for i in L:
    print(i)
# 生成器
T = (x * x for x in range(10))
print(next(T))
print(next(T))
print(next(T))
for i in T: # for 循环不至于报错
    print(i)



#  用函数表示生成器
def generator():
            print('step 1')
            yield 1
            print('step 2')
            yield 2
            print('step 3')
            yield 3



