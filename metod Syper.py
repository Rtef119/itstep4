class Grandparent:
    def about(self):
        print("Я дідусь")

    def about_me(self):
        print("Я бабуся")

class Parent(Grandparent):
    def about_me(self):
        print("Я батько")
class Child(Parent):
    def __init__(self):
        super().about()
        super().about_me()

kira = Child