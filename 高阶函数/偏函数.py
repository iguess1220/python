def int2(x,base=2):
    return int(x,base)
import functools

int8 = functools.partial(int,base=8)
c = int8('11111')
print(c)
print(int2('10101'))



max2 = functools.partial(max,10)
c = max2(5,7,3)
print(c)

