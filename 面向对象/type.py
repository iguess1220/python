def fn(self,name='world'):
    print('Hello,%s' % name)
Hello = type('Hello',(object,),dict())
h = Hello()
print(dir(h))
