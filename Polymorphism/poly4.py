class Parent:
    def skill(self):
        print("parent")

class Child(Parent):   
    def skill(self):
        super().skill()
        print("child")

class Child2(Parent):
    def skill(self):
        super().skill()
        print("child2")

s = Child()
s.skill()

print()

c2 = Child2()
c2.skill()