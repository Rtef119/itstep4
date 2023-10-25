class Grandparent:
    heigth = 170
    gladness = 100
    age = 60

class Parent(Grandparent):
    age = 40

class Child(Parent):
    heigth = 50 #age =
    def __init__(self):
        print(self.heigth)
        print(self.gladness)
        print(self.age)

kira = Child()