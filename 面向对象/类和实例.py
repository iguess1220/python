class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print("%s: %s"  %(self.name,self.score))

    def get_grade(self):
        if self.score >= 90:
            return "A"
        elif self.score >= 60:
            return "B"
        else:
            return "C"
cy = Student('chenyang',90)
xy = Student('xiaoyong',59)
yy = Student('fangyue',66)
print(cy.name,cy.get_grade())
print(xy.name,xy.get_grade())
print(yy.name,yy.get_grade())


