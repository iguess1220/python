def fn(self,name='world'):
    print("Hello,%s" % name)
Hello = type('Hello',(object,),dict(test=fn)) # object 位置为多重继承，需要是元祖，所以当为一个还得是元祖时加个逗号
cy = Hello()
cy.test()