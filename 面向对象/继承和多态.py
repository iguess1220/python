class Animal:
    def run(self):
        print("Animal is running")
class Dog(Animal):
    pass
class Cat(Animal):
    def run(self):
        print("cat  is running" )
dog = Dog()
dog.run()
cat = Cat()
cat.run()


# 多态性： 向不同的对象发送同一条消息，不同的对象在接收时会产生不同的行为，也就是说，
# 每个对象可以用自己的方式去相应共同的消息，所谓消息就是调用函数，
"""Python本身就是支持多态性的，这么做的好处是什么呢？
（1）增加了程序的灵活性
　　以不变应万变，不论对象千变万化，使用者都是同一种形式去调用，如func(animal)
（2）增加了程序额可扩展性
　　通过继承animal类创建了一个新的类，使用者无需更改自己的代码，还是用func(animal)去调用
"""
