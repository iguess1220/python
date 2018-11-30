class Animal:
    pass
class Mammal(Animal):
    def body(self):
        print("eat milk")
class Bird(Animal):
    def body(self):
        print("有翅膀")
class Runable(Animal):
    def run(self):
        print("running")
class Flyable(Animal):
    def fly(self):
        print("fly")
class Bat(Mammal,Flyable):
    pass
b = Bat()
b.fly()
class tuoniao(Bird,Runable,Flyable):
    pass
c = tuoniao()
c.run()
c.body()


